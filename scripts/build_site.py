import re
from pathlib import Path

OUT = Path("/media/humba/Projetos/Meus_Projetos/ensino-ifsc/musico-apoio/site-2027")

# Estrutura central de navegação (Menu Horizontal + Submenus Verticais Expansíveis)
# Para adicionar uma nova subpágina no futuro, basta acrescentar uma tupla na lista "sub"!
NAV_STRUCTURE = [
    {"href": "index.html", "label": "Início", "sub": []},
    {
        "href": "projeto.html",
        "label": "Projetos",
        "sub": [
            ("projeto.html", "Músico de Apoio (Base &amp; Editais)", "Metodologia PHC/PPE, Sala de Música e ciclos PROPPI/DAE"),
            ("projeto-rac-and-roll.html", "Banda RAC &amp; Roll", "Projeto musical organizado pelo Prof. Jorge Luiz Pereira"),
            ("projetos-futuros.html", "Projetos Futuros · Ciclo 2027", "Incubadora de novas iniciativas e roadmap em desenvolvimento"),
            ("parcerias.html", "Parcerias &amp; Captação 2027", "Como apoiar via Emendas (MDE/LDB), FEESC ou Empresas de São José"),
        ],
    },
    {"href": "oficinas.html", "label": "Oficinas", "sub": []},
    {
        "href": "eventos.html",
        "label": "Eventos",
        "sub": [
            ("eventos.html", "Portfólio 2026 (Realizados)", "SNCT/MCC, Aulão de Vestibular Live e Feira de Jogos"),
            ("eventos-2027.html", "Agenda &amp; Eventos 2027", "Calendário anual de apresentações e participações previstas"),
        ],
    },
    {
        "href": "tecnologia-social.html",
        "label": "Tecnologia Social",
        "sub": [
            ("tecnologia-social.html", "Manual &amp; Replicabilidade", "Guia de implantação na Rede Federal e ciência aberta"),
            ("apostilas.html", "Apostilas &amp; Materiais Didáticos", "Bateria, Violão (dedos-pivô) e futuras tecnologias compartilhadas"),
        ],
    },
    {
        "href": "sinfonia-inovacao.html",
        "label": "Sinfonia &amp; Inovação",
        "sub": [
            ("sinfonia-inovacao.html", "Calculadoras Científicas (PVC &amp; Domo 2V)", "Eco-Lutheria e Geometria Geodésica 100% no navegador"),
            ("sinfonia-bncc.html", "Matriz BNCC &amp; 7 Encontros", "5 Unidades Curriculares, 11 habilidades e trilha didática"),
        ],
    },
    {"href": "equipe.html", "label": "Equipe e Ética", "sub": []},
]

def build_nav_html(current_file):
    items_html = []
    for item in NAV_STRUCTURE:
        sub_files = [s[0] for s in item["sub"]]
        is_parent_active = (item["href"] == current_file) or (current_file in sub_files)
        active_cls = " active" if is_parent_active else ""
        aria_curr = ' aria-current="page"' if item["href"] == current_file else ""
        if not item["sub"]:
            items_html.append(
                f'          <li class="nav-item"><a class="nav-link{active_cls}" href="{item["href"]}"{aria_curr}>{item["label"]}</a></li>'
            )
        else:
            sub_li = "\n".join(
                f'              <li><a class="dropdown-link{" active" if sf == current_file else ""}" href="{sf}"{" aria-current=\"page\"" if sf == current_file else ""}>{stitle}<small>{sdesc}</small></a></li>'
                for sf, stitle, sdesc in item["sub"]
            )
            items_html.append(f"""          <li class="nav-item nav-item--has-sub">
            <a class="nav-link{active_cls}" href="{item["href"]}"{aria_curr}>{item["label"]}</a>
            <button type="button" class="nav-caret-btn" aria-expanded="false" aria-label="Expandir submenu de {item["label"]}">▾</button>
            <ul class="dropdown-menu" aria-label="Submenu de {item["label"]}">
{sub_li}
            </ul>
          </li>""")
    return "\n".join(items_html)

def render_shell(filename, page_title, meta_desc, body_html, extra_scripts=""):
    nav_html = build_nav_html(filename)
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title} | Programa Músico de Apoio — IFSC São José</title>
  <meta name="description" content="{meta_desc}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&family=Open+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

  <!-- BARRA DE ACESSIBILIDADE GOVERNAMENTAL (eMAG 3.1 / WCAG 2.2 AA / TEA) -->
  <div class="a11y-bar" role="region" aria-label="Barra de acessibilidade">
    <div class="container a11y-bar__inner">
      <ul class="a11y-shortcuts">
        <li><a href="#conteudo-principal" accesskey="1"><span class="a11y-key">1</span> Ir para o conteúdo</a></li>
        <li><a href="#menu-principal" accesskey="2"><span class="a11y-key">2</span> Ir para o menu</a></li>
        <li><a href="index.html" accesskey="3"><span class="a11y-key">3</span> Página inicial</a></li>
        <li><a href="#search-drawer" id="trigger-search" accesskey="4"><span class="a11y-key">4</span> Filtrar página</a></li>
      </ul>
      <div class="a11y-controls" role="group" aria-label="Controles visuais e sensoriais">
        <button type="button" class="a11y-btn" id="btn-font-dec" title="Diminuir tamanho da fonte" aria-label="Diminuir tamanho da fonte">A−</button>
        <button type="button" class="a11y-btn" id="btn-font-reset" title="Restaurar tamanho padrão da fonte" aria-label="Restaurar tamanho da fonte">A</button>
        <button type="button" class="a11y-btn" id="btn-font-inc" title="Aumentar tamanho da fonte" aria-label="Aumentar tamanho da fonte">A+</button>
        <button type="button" class="a11y-btn" id="btn-contrast" accesskey="5" aria-pressed="false" title="Alternar modo de alto contraste (Alt + 5)">
          <span class="a11y-key">5</span> Alto Contraste
        </button>
        <button type="button" class="a11y-btn" id="btn-motion" aria-pressed="false" title="Reduzir animações para conforto sensorial">
          Conforto Sensorial
        </button>
      </div>
    </div>
  </div>

  <!-- CABEÇALHO INSTITUCIONAL & MENU PRINCIPAL EXPANSÍVEL -->
  <header class="site-header" role="banner">
    <div class="container site-header__inner">
      <a href="index.html" class="brand-group" aria-label="IFSC Câmpus São José — Início do Portal Músico de Apoio">
        <div class="brand-logo-wrap">
          <img src="assets/img/ifsc-horizontal-cor.png" alt="Instituto Federal de Santa Catarina — IFSC" class="brand-logo logo-light" width="111" height="38">
          <img src="assets/img/ifsc-horizontal-branco.png" alt="Instituto Federal de Santa Catarina — IFSC" class="brand-logo logo-dark" width="111" height="38">
        </div>
        <div class="brand-text">
          <span class="brand-title">Músico de Apoio</span>
          <span class="brand-subtitle">Programa Guarda-Chuva · IFSC São José</span>
        </div>
      </a>

      <button type="button" class="nav-toggle" id="nav-toggle" aria-expanded="false" aria-controls="menu-principal">
        ☰ Menu
      </button>

      <nav class="main-nav" id="menu-principal" aria-label="Navegação principal do portal">
        <ul class="nav-list">
{nav_html}
        </ul>
      </nav>
    </div>

    <div class="search-drawer" id="search-drawer" hidden>
      <div class="container search-drawer__inner">
        <label for="site-search-input" class="sr-only">Filtrar conteúdos nesta página</label>
        <input type="search" id="site-search-input" class="search-input" placeholder="Filtrar conteúdos desta página (ex.: RAC &amp; Roll, BNCC, Domo, Tubofone, SNCT, ODS)...">
        <span class="search-results-count" id="search-results-count" aria-live="polite">Digite para filtrar</span>
        <button type="button" class="btn btn-secondary btn-sm" id="search-close">Fechar</button>
      </div>
    </div>
  </header>

  <main id="conteudo-principal" tabindex="-1">
{body_html}
  </main>

  <!-- RODAPÉ INSTITUCIONAL -->
  <footer class="site-footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <div>
          <img src="assets/img/ifsc-horizontal-branco.png" alt="Instituto Federal de Santa Catarina — IFSC" class="footer-logo" width="128" height="44">
          <p style="font-size:0.86rem;color:var(--text-on-dark-muted);margin:0;max-width:44ch;">
            <strong>Programa Músico de Apoio &amp; Sinfonia da Permanência</strong><br>
            Instituto Federal de Santa Catarina — Câmpus São José.<br>
            Pesquisa Aplicada, Cultura e Tecnologia Social (Editais nº 12/2025 e nº 16/2026/PROPPI/DAE).
          </p>
        </div>

        <div>
          <h3>Páginas &amp; Submenus</h3>
          <ul class="footer-links">
            <li><a href="projeto.html">Projetos (Músico de Apoio · RAC &amp; Roll · 2027)</a></li>
            <li><a href="parcerias.html">Parcerias &amp; Captação 2027 (Emendas / FEESC / Empresas)</a></li>
            <li><a href="oficinas.html">Oficinas &amp; Estúdio Digital</a></li>
            <li><a href="eventos.html">Eventos (Portfólio 2026 · Agenda 2027)</a></li>
            <li><a href="tecnologia-social.html">Tecnologia Social &amp; Apostilas</a></li>
            <li><a href="sinfonia-inovacao.html">Sinfonia &amp; Inovação (Calculadoras · BNCC)</a></li>
            <li><a href="equipe.html">Equipe e Ética</a></li>
          </ul>
        </div>

        <div>
          <h3>Acervos e Links Institucionais</h3>
          <ul class="footer-links">
            <li><a href="https://www.ifsc.edu.br/web/campus-sao-jose" target="_blank" rel="noopener noreferrer">Portal IFSC Câmpus São José ↗</a></li>
            <li><a href="https://drive.google.com/drive/folders/19b-qqgw5ElqcGSa6ewLfSHoE83AjjyEx?usp=sharing" target="_blank" rel="noopener noreferrer">Acervo SNCT / MCC 2026 ↗</a></li>
            <li><a href="https://www.youtube.com/live/t1BAm_mXt-0" target="_blank" rel="noopener noreferrer">Aulão de Vestibular (YouTube Live) ↗</a></li>
            <li><a href="https://drive.google.com/drive/folders/1a1DQWz-fpDmJqDzLh6jj91_zjrW52owD?usp=drive_link" target="_blank" rel="noopener noreferrer">Gravações Feira de Jogos 2026.2 ↗</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <span><strong>Desenvolvido por Prof. Humberto Luz Oliveira</strong> · IFSC Câmpus São José · Tecnologia Social Aberta (GitHub + Cloudflare Pages)</span>
        <span>Em conformidade com eMAG 3.1, WCAG 2.2 AA, LGPD e Manual da Marca IFSC</span>
      </div>
    </div>
  </footer>

  <!-- VLibras Widget Oficial do Governo Federal -->
  <div vw class="enabled">
    <div vw-access-button class="active"></div>
    <div vw-plugin-wrapper>
      <div class="vw-plugin-top-wrapper"></div>
    </div>
  </div>
  <script src="https://vlibras.gov.br/app/vlibras-plugin.js"></script>
  <script>if (window.VLibras) {{ new window.VLibras.Widget('https://vlibras.gov.br/app'); }}</script>

  <script src="assets/js/main.js"></script>
{extra_scripts}</body>
</html>
"""

def page_hero(crumbs, title, subtitle):
    crumb_items = ['<li><a href="index.html">Início</a></li>']
    for i, (label, href) in enumerate(crumbs):
        crumb_items.append('<li aria-hidden="true">/</li>')
        if i == len(crumbs) - 1 or not href:
            crumb_items.append(f'<li aria-current="page">{label}</li>')
        else:
            crumb_items.append(f'<li><a href="{href}">{label}</a></li>')
    return f"""    <section class="page-hero">
      <div class="container">
        <nav aria-label="Caminho de navegação">
          <ol class="breadcrumb">
            {" ".join(crumb_items)}
          </ol>
        </nav>
        <h1>{title}</h1>
        <p>{subtitle}</p>
      </div>
    </section>"""

def pager(prev_item, next_item):
    parts = ['      <nav class="page-pager" aria-label="Navegação entre páginas">']
    if prev_item:
        href, label = prev_item
        parts.append(f'        <a href="{href}" class="pager-link"><span class="pager-dir">← Página anterior</span><span class="pager-title">{label}</span></a>')
    if next_item:
        href, label = next_item
        parts.append(f'        <a href="{href}" class="pager-link pager-link--next"><span class="pager-dir">Próxima página →</span><span class="pager-title">{label}</span></a>')
    parts.append('      </nav>')
    return "\n".join(parts)

# ============================================================================
# 1. INDEX.HTML — INÍCIO
# ============================================================================
INDEX_BODY = """    <section class="hero" id="inicio" aria-labelledby="hero-heading">
      <div class="container hero__grid">
        <div>
          <div class="eyebrow">
            <span class="eyebrow-dot" aria-hidden="true"></span>
            Programa Guarda-Chuva · PROPPI / DAE · IFSC Câmpus São José
          </div>
          <h1 id="hero-heading">
            Música por Pares, Inclusão e <span class="highlight">Eco-Lutheria Científica</span> no Ensino Médio Integrado
          </h1>
          <p class="hero__lead">
            O <strong>Programa Músico de Apoio</strong> abriga projetos de pesquisa, formação musical por pares, bandas estudantis e parcerias interdisciplinares — como a <strong>Banda RAC &amp; Roll</strong> e o projeto parceiro <strong>Sinfonia da Permanência</strong>, de autoria de <strong>Fábio Henrique de Carvalho Bartelega</strong>.
          </p>
          <div class="hero__actions">
            <a href="projeto.html" class="btn btn-primary">Explorar Projetos →</a>
            <a href="parcerias.html" class="btn btn-secondary">Parcerias &amp; Captação 2027</a>
            <a href="sinfonia-inovacao.html" class="btn btn-secondary">Calculadoras 2027</a>
          </div>

          <div class="hero__metrics" aria-label="Principais indicadores do programa">
            <div class="metric-item"><span class="metric-value">1 Sala</span><span class="metric-label">Sala de Música acústica permanente</span></div>
            <div class="metric-item"><span class="metric-value">3+ Projetos</span><span class="metric-label">Músico de Apoio, RAC &amp; Roll e Ciclo 2027</span></div>
            <div class="metric-item"><span class="metric-value">65 Barras</span><span class="metric-label">Domo Geodésico 2V (R = 2,0 m)</span></div>
            <div class="metric-item"><span class="metric-value">11 BNCC</span><span class="metric-label">5 Unidades Curriculares integradas</span></div>
          </div>
        </div>

        <aside class="hero-visual" aria-label="Esquema visual do Domo Geodésico 2V e ondas acústicas">
          <svg viewBox="0 0 420 290" role="img" aria-labelledby="svg-hero-title svg-hero-desc" width="100%">
            <title id="svg-hero-title">Esquema do Domo Geodésico 2V e Ressonância Acústica</title>
            <desc id="svg-hero-desc">Diagrama de um domo geodésico hemisférico de frequência 2V com três níveis de altura ecológica sobreposto a ondas estacionárias de um tubofone aberto.</desc>
            <defs>
              <linearGradient id="waveGrad" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="#32A041"/><stop offset="50%" stop-color="#5CE671"/><stop offset="100%" stop-color="#C8191E"/>
              </linearGradient>
            </defs>
            <line x1="25" y1="55" x2="395" y2="55" stroke="#C8191E" stroke-dasharray="4 4" stroke-opacity="0.55"/>
            <line x1="25" y1="138" x2="395" y2="138" stroke="#F59E0B" stroke-dasharray="4 4" stroke-opacity="0.55"/>
            <line x1="25" y1="220" x2="395" y2="220" stroke="#32A041" stroke-dasharray="4 4" stroke-opacity="0.65"/>
            <g stroke="#5CE671" stroke-width="2" fill="none" stroke-linejoin="round">
              <polyline points="55,220 75,145 130,82 210,55 290,82 345,145 365,220" stroke="#FFFFFF" stroke-width="2.4"/>
              <line x1="55" y1="220" x2="365" y2="220" stroke="#FFFFFF" stroke-width="2.4"/>
              <polyline points="55,220 135,145 210,55 285,145 365,220"/>
              <polyline points="75,145 155,220 210,145 265,220 345,145"/>
              <line x1="75" y1="145" x2="345" y2="145"/><line x1="130" y1="82" x2="290" y2="82"/>
              <line x1="130" y1="82" x2="135" y2="145"/><line x1="290" y1="82" x2="285" y2="145"/>
              <line x1="130" y1="82" x2="210" y2="145"/><line x1="290" y1="82" x2="210" y2="145"/>
              <line x1="135" y1="145" x2="155" y2="220"/><line x1="285" y1="145" x2="265" y2="220"/>
              <line x1="210" y1="55" x2="210" y2="145"/>
            </g>
            <g fill="#FFFFFF" stroke="#0F172A" stroke-width="1.5">
              <circle cx="210" cy="55" r="5" fill="#C8191E"/>
              <circle cx="130" cy="82" r="4"/><circle cx="290" cy="82" r="4"/>
              <circle cx="75" cy="145" r="4"/><circle cx="135" cy="145" r="4"/>
              <circle cx="210" cy="145" r="4.5" fill="#5CE671"/>
              <circle cx="285" cy="145" r="4"/><circle cx="345" cy="145" r="4"/>
              <circle cx="55" cy="220" r="4"/><circle cx="155" cy="220" r="4"/>
              <circle cx="265" cy="220" r="4"/><circle cx="365" cy="220" r="4"/>
            </g>
            <path d="M 55 252 Q 132 225, 210 252 T 365 252" fill="none" stroke="url(#waveGrad)" stroke-width="2.5"/>
            <path d="M 55 252 Q 132 279, 210 252 T 365 252" fill="none" stroke="url(#waveGrad)" stroke-width="1.6" stroke-dasharray="4 3"/>
            <text x="28" y="48" fill="#FCA5A5" font-size="10" font-family="Open Sans, sans-serif" font-weight="700">Estrato 3 · Ápice (2,0 m) · PVC/PET</text>
            <text x="28" y="132" fill="#FDE68A" font-size="10" font-family="Open Sans, sans-serif" font-weight="700">Estrato 2 · Médio (1,0 m) · Metais</text>
            <text x="28" y="213" fill="#86EFAC" font-size="10" font-family="Open Sans, sans-serif" font-weight="700">Estrato 1 · Base (0,1 m) · Celulose</text>
            <text x="210" y="282" text-anchor="middle" fill="#CBD5E1" font-size="10" font-family="JetBrains Mono, monospace">f = v / [2(L + 1,22·r)]  |  V − A + F = 26 − 65 + 40 = 1</text>
          </svg>
          <div class="hero-visual__caption">
            <span><strong>Organizador Prévio 3D</strong> · Escala de Permanência</span>
            <span class="mono">IFSC · 2026 → 2027</span>
          </div>
        </aside>
      </div>
    </section>

    <section class="section section--alt" aria-labelledby="hub-heading">
      <div class="container">
        <header class="section-header">
          <span class="section-tag">Ecossistema do Portal</span>
          <h2 id="hub-heading">Explore os Núcleos e Subpáginas</h2>
          <p>Utilize os menus expansíveis no topo ou acesse diretamente cada área temática do programa.</p>
        </header>

        <div class="grid-3">
          <a href="projeto.html" class="hub-card card--accent-green" data-searchable>
            <span class="pill">Guarda-Chuva · 4 Subpáginas</span>
            <h3>Projetos &amp; Parcerias 2027</h3>
            <p>Músico de Apoio (PHC/PPE e Editais), Banda RAC &amp; Roll (Prof. Jorge Luiz Pereira), Roadmap 2027 e Vitrine de Parcerias &amp; Captação.</p>
            <span class="hub-card__cta">Ver Projetos e Parcerias →</span>
          </a>

          <a href="oficinas.html" class="hub-card card--accent-blue" data-searchable>
            <span class="pill pill--blue">Prática Musical</span>
            <h3>Oficinas &amp; Estúdio</h3>
            <p>Como participar nos cursos de Telecom e Refrigeração, tutoria por pares e Estúdio Rítmico (Metrônomo + Diapasão sem autoplay).</p>
            <span class="hub-card__cta">Acessar Oficinas →</span>
          </a>

          <a href="eventos.html" class="hub-card card--accent-red" data-searchable>
            <span class="pill pill--red">Portfólio &amp; Agenda</span>
            <h3>Eventos</h3>
            <p>Portfólio realizado em 2026 (SNCT, Aulão Live, Feira de Jogos) e Agenda de participações previstas para o ciclo 2027.</p>
            <span class="hub-card__cta">Acessar Eventos →</span>
          </a>

          <a href="tecnologia-social.html" class="hub-card card--accent-green" data-searchable>
            <span class="pill">Ciência Aberta</span>
            <h3>Tecnologia Social</h3>
            <p>Manual de Implementação replicável na Rede Federal e subpágina dedicada às Apostilas de Bateria, Violão e materiais compartilhados.</p>
            <span class="hub-card__cta">Acessar Tecnologia Social →</span>
          </a>

          <a href="sinfonia-inovacao.html" class="hub-card card--accent-blue" data-searchable>
            <span class="pill pill--blue">Calculadoras &amp; BNCC</span>
            <h3>Sinfonia &amp; Inovação</h3>
            <p>Parceria com a <em>Sinfonia da Permanência</em> (Fábio Henrique de Carvalho Bartelega), Calculadoras PVC/Domo 2V e Matriz BNCC.</p>
            <span class="hub-card__cta">Abrir Calculadoras →</span>
          </a>

          <a href="equipe.html" class="hub-card card--accent-red" data-searchable>
            <span class="pill pill--red">Governança</span>
            <h3>Equipe e Ética</h3>
            <p>Ficha técnica dos pesquisadores e tutores, alinhamento aos 6 ODS da ONU, acessibilidade eMAG/WCAG/TEA e protocolo LGPD/ECA.</p>
            <span class="hub-card__cta">Acessar Equipe e Ética →</span>
          </a>
        </div>
      </div>
    </section>"""

# ============================================================================
# 2A. PROJETO.HTML — HUB GUARDA-CHUVA DE PROJETOS + METODOLOGIA BASE
# ============================================================================
PROJETO_BODY = page_hero(
    [("Projetos", "projeto.html"), ("Músico de Apoio", None)],
    "Projetos · Programa Guarda-Chuva Músico de Apoio",
    "O Músico de Apoio atua como um ecossistema guarda-chuva no IFSC Câmpus São José, reunindo pesquisa aplicada, bandas estudantis, formação por pares e novas iniciativas musicais."
) + """
    <section class="section">
      <div class="container">
        <!-- Subprojetos abrigados sob o guarda-chuva -->
        <header class="section-header">
          <span class="section-tag">Subprojetos Integrados</span>
          <h2>Iniciativas Abrigadas pelo Programa</h2>
        </header>
        <div class="grid-4" style="margin-bottom:2.75rem;">
          <div class="card card--accent-green" data-searchable>
            <span class="pill">Núcleo Principal · Editais 12/2025 e 16/2026</span>
            <h3>Músico de Apoio (Pesquisa &amp; Tutoria)</h3>
            <p>Validação da tutoria musical por pares (PHC/PPE), Sala de Música acústica e integração interdisciplinar com a <em>Sinfonia da Permanência</em>.</p>
            <span style="font-size:0.82rem;font-weight:700;color:var(--ifsc-verde-escuro);margin-top:auto;">Você está nesta página ↓</span>
          </div>
          <a href="projeto-rac-and-roll.html" class="hub-card card--accent-red" data-searchable>
            <span class="pill pill--red">Prática de Conjunto · Cultura</span>
            <h3>Banda RAC &amp; Roll</h3>
            <p>Projeto musical de integração estudantil e prática de banda organizado pelo Prof. Jorge Luiz Pereira no Câmpus São José.</p>
            <span class="hub-card__cta">Abrir página RAC &amp; Roll →</span>
          </a>
          <a href="projetos-futuros.html" class="hub-card card--accent-blue" data-searchable>
            <span class="pill pill--blue">Roadmap · Ciclo 2027</span>
            <h3>Projetos Futuros &amp; Novas Frentes</h3>
            <p>Caderno de Eco-Lutheria, Livro de Coletâneas Multimídia e propostas em planejamento para o ano letivo de 2027.</p>
            <span class="hub-card__cta">Ver Projetos Futuros →</span>
          </a>
          <a href="parcerias.html" class="hub-card card--accent-green" data-searchable>
            <span class="pill pill--amber">Captação · MDE / FEESC</span>
            <h3>Parcerias &amp; Captação 2027</h3>
            <p>Plano orçamentário 2027 (Ações 20RL e 2994) e vias legais de apoio via Emendas Federais e Empresas de São José.</p>
            <span class="hub-card__cta">Ver Parcerias 2027 →</span>
          </a>
        </div>

        <!-- Evolução 2026 -> 2027 -->
        <div class="grid-2" style="margin-bottom:2.25rem;">
          <article class="card card--accent-blue" data-searchable>
            <span class="pill pill--blue">Ciclo 1 Concluído · Edital 12/2025</span>
            <h3>Base Consolidada em 2026 (SIGAA: PISJE4706-2025)</h3>
            <ul class="check-list">
              <li><strong>Sala de Música Permanente:</strong> adequação da antiga sala de projeções anexa ao auditório, com 32 calços antivibração e isolamento acústico.</li>
              <li><strong>Acervo Instrumental Revitalizado:</strong> restauração da bateria acústica e aquisição de 11 pandeiros/pandeirolas, 6 ganzás, triângulo, afinadores e microfonia sem fio (execução integral do AFP).</li>
              <li><strong>Protagonismo e Regência Discente:</strong> o bolsista João Alvarenga Lourenção expandiu o domínio da bateria para violão, guitarra, baixo e teclado, assumindo a regência das oficinas e decidindo cursar Licenciatura em Música (UDESC).</li>
              <li><strong>Avaliação Qualitativa Contínua:</strong> observação participante e diários de campo alinhados às dimensões de autonomia (IAAD), humor/vigor (POMS) e letramento científico (GSLQ).</li>
            </ul>
          </article>

          <article class="card card--accent-green" data-searchable>
            <span class="pill">Ciclo 2 · Parceria 2027 (Edital 16/2026)</span>
            <h3>Integração com a Sinfonia da Permanência</h3>
            <p>Em parceria com o especialista em Educação Ambiental <strong>Fábio Henrique de Carvalho Bartelega</strong>, autor do projeto <em>Sinfonia da Permanência</em>, a edição 2027 une a tutoria <em>Músico de Apoio</em> à Eco-Lutheria e à Dupla Ancoragem (TAS + PNL-VAC):</p>
            <ul class="check-list">
              <li><strong>Bancada de Eco-Lutheria Experimental:</strong> construção de 15+ instrumentos afinados (<span class="mono">&lt; 5 cents</span>) com PVC, PET, latas metálicas e celulose.</li>
              <li><strong>Domo Geodésico 2V (Organizador Prévio 3D):</strong> estrutura autoportante de 65 barras e 26 conectores organizada por tempo de degradação ambiental.</li>
              <li><strong>Biossegurança e Metrologia:</strong> triagem com EPIs, balanço gravimétrico (kg) e validação espectral digital.</li>
              <li><strong>Transferência de Tecnologia Social:</strong> portal web aberto e Guia Técnico-Pedagógico replicável.</li>
            </ul>
          </article>
        </div>

        <header class="section-header">
          <span class="section-tag">Alicerce Didático</span>
          <h2>Cinco Momentos da Pedagogia Histórico-Crítica (Gasparin / Saviani)</h2>
        </header>
        <div class="steps-grid">
          <div class="step-box" data-searchable><span class="step-num">1</span><h4>Prática Social Inicial</h4><p>Escuta ativa das vivências musicais dos discentes e sensibilização socioambiental.</p></div>
          <div class="step-box" data-searchable><span class="step-num">2</span><h4>Problematização</h4><p>Análise do acesso à música, inclusão no EMI e impacto químico-ambiental dos resíduos.</p></div>
          <div class="step-box" data-searchable><span class="step-num">3</span><h4>Instrumentalização</h4><p>Oficinas práticas de harmonia, ritmo, acústica física e engenharia do Domo 2V.</p></div>
          <div class="step-box" data-searchable><span class="step-num">4</span><h4>Catarse</h4><p>Ensaios cooperativos liderados pelos tutores pares e síntese conceitual integrada.</p></div>
          <div class="step-box" data-searchable><span class="step-num">5</span><h4>Prática Social Final</h4><p>Apresentações públicas abertas à comunidade e difusão do manual como Tecnologia Social.</p></div>
        </div>

""" + pager(("index.html", "Início"), ("projeto-rac-and-roll.html", "Banda RAC &amp; Roll")) + """
      </div>
    </section>"""

# ============================================================================
# 2B. PROJETO-RAC-AND-ROLL.HTML — SUBPÁGINA BANDA RAC & ROLL
# ============================================================================
RAC_BODY = page_hero(
    [("Projetos", "projeto.html"), ("Banda RAC &amp; Roll", None)],
    "Projeto Banda RAC &amp; Roll",
    "Iniciativa artístico-cultural organizada pelo Prof. Jorge Luiz Pereira no IFSC Câmpus São José, integrando estudantes, servidores e egressos por meio da música de conjunto."
) + """
    <section class="section">
      <div class="container">
        <div class="grid-2" style="margin-bottom:2rem;">
          <article class="card card--accent-red" data-searchable>
            <span class="pill pill--red">Coordenação · Prof. Jorge Luiz Pereira</span>
            <h3>Identidade e Propósito da RAC &amp; Roll</h3>
            <p>
              Nascida no ambiente da Coordenadoria de <strong>Refrigeração e Ar Condicionado (RAC)</strong> e aberta a toda a comunidade acadêmica do Câmpus São José, a <strong>Banda RAC &amp; Roll</strong> fortalece o pertencimento escolar, a convivência intergeracional entre docentes e estudantes e o palco de estreia para novos instrumentistas formados nas oficinas do <em>Músico de Apoio</em>.
            </p>
            <ul class="check-list">
              <li><strong>Ponte com as Oficinas:</strong> oferece repertório vivo e experiência real de palco para os aprendizes e tutores do projeto.</li>
              <li><strong>Espaço Permanente:</strong> utiliza a infraestrutura acústica da Sala de Música e o acervo compartilhado do câmpus.</li>
              <li><strong>Integração Comunitária:</strong> atua em datas comemorativas, recepção de calouros, mostras culturais e eventos institucionais.</li>
            </ul>
          </article>

          <article class="card card--accent-green" data-searchable>
            <span class="pill">Integração com o Programa Guarda-Chuva</span>
            <h3>Sinergia RAC &amp; Roll + Músico de Apoio</h3>
            <p>
              A parceria entre a <strong>RAC &amp; Roll</strong> e o <strong>Músico de Apoio</strong> cria uma trilha contínua de desenvolvimento musical dentro do IFSC Câmpus São José:
            </p>
            <ul class="check-list">
              <li><strong>Iniciação nas Oficinas:</strong> o estudante dá os primeiros passos na bateria, violão, baixo, guitarra, teclado ou percussão.</li>
              <li><strong>Prática de Conjunto:</strong> vivência de arranjo, dinâmica de banda, passagem de som e entrosamento coletivo.</li>
              <li><strong>Formação de Tutores:</strong> participantes mais experientes apoiam os novos ingressantes na filosofia do <em>sideman</em>.</li>
              <li><strong>Espaço em Expansão:</strong> esta página receberá o histórico de formações, galeria oficial, repertórios e agenda de ensaios da banda.</li>
            </ul>
          </article>
        </div>

        <div class="card" data-searchable>
          <span class="pill pill--blue">Participação &amp; Repertório</span>
          <h3>Quer tocar ou participar dos ensaios?</h3>
          <p>
            Estudantes de todas as fases (Telecomunicações, Refrigeração e demais cursos do câmpus) e servidores interessados podem procurar o <strong>Prof. Jorge Luiz Pereira</strong> ou acompanhar o cronograma de ensaios na <a href="oficinas.html">página de Oficinas</a> e na <a href="eventos-2027.html">Agenda 2027</a>.
          </p>
        </div>

""" + pager(("projeto.html", "Músico de Apoio"), ("projetos-futuros.html", "Projetos Futuros · 2027")) + """
      </div>
    </section>"""

# ============================================================================
# 2C. PROJETOS-FUTUROS.HTML — ROADMAP & PROSPECÇÃO 2027 (SEM SIGILO)
# ============================================================================
FUTUROS_BODY = page_hero(
    [("Projetos", "projeto.html"), ("Projetos Futuros · 2027", None)],
    "Projetos Futuros &amp; Roadmap de Prospecção (Ciclo 2027)",
    "Painel de iniciativas, materiais didáticos e expansões estruturais em discussão e desenvolvimento para o ciclo 2027 no IFSC Câmpus São José."
) + """
    <section class="section">
      <div class="container">
        <div class="grid-2" style="margin-bottom:2rem;">
          <article class="card card--accent-green" data-searchable>
            <span class="pill">🔬 Em Desenvolvimento · Ciclo 2027</span>
            <h3>Caderno de Eco-Lutheria &amp; Calculadora Web</h3>
            <p>Frente de investigação científica liderada por <strong>Fábio Henrique de Carvalho Bartelega</strong>, <strong>Prof. Humberto Luz Oliveira</strong> e <strong>Prof. Jorge Luiz Pereira</strong>, transformando PVC, garrafas PET e latas metálicas em instrumentos afinados (<span class="mono">f = v / 2L</span>) acoplados ao Domo Geodésico 2V.</p>
            <div style="margin-top:auto;padding-top:0.5rem;">
              <a href="sinfonia-inovacao.html" class="btn btn-primary btn-sm">Abrir Calculadoras Científicas →</a>
            </div>
          </article>

          <article class="card card--accent-blue" data-searchable>
            <span class="pill pill--blue">💬 Em Discussão com a Equipe</span>
            <h3>Livro de Coletâneas Multimídia (MP3 · MP4 · PDF · E-book)</h3>
            <p>Consolidação dos estudos semanais por instrumento (Baixo Elétrico, Violão/Guitarra e Teclado) em um E-book integrado com playbacks em áudio (MP3), demonstrações em vídeo (MP4) e cifras/partituras em PDF.</p>
            <div style="margin-top:auto;padding-top:0.5rem;">
              <a href="apostilas.html" class="btn btn-secondary btn-sm">Ver Estudos Semanais →</a>
            </div>
          </article>

          <article class="card card--accent-red" data-searchable>
            <span class="pill pill--amber">🏛 Em Captação · Ação 20RL (GND 4 / GND 3)</span>
            <h3>Modernização do Acervo &amp; Almoxarifado Próprio</h3>
            <p>Aquisição patrimonial de contrabaixo elétrico, guitarra com amplificadores, bateria acústica completa, reposição contínua de cordas/peles e instalação de almoxarifado dedicado com fechadura na Sala de Música para conservação dos equipamentos.</p>
            <div style="margin-top:auto;padding-top:0.5rem;">
              <a href="parcerias.html" class="btn btn-secondary btn-sm">Ver Plano de Captação →</a>
            </div>
          </article>

          <article class="card card--accent-green" data-searchable>
            <span class="pill pill--amber">🤝 Em Captação · Ação 2994 (PNAES / FEESC)</span>
            <h3>Expansão de Bolsas de Permanência em 2 Turnos</h3>
            <p>Ampliação das cotas de bolsas de tutoria e permanência (custeio de alimentação e transporte em dois turnos letivos) para que estudantes multiplicadores e oficineiros atuem com dedicação integral ao projeto.</p>
            <div style="margin-top:auto;padding-top:0.5rem;">
              <a href="parcerias.html" class="btn btn-primary btn-sm">Como Apoiar em 2027 →</a>
            </div>
          </article>
        </div>

        <div class="grid-2" style="margin-bottom:1.5rem;">
          <article class="card" data-searchable>
            <span class="pill pill--blue">💬 Em Planejamento · 2027</span>
            <h3>Oficinas Temáticas &amp; Repertórios Especiais</h3>
            <p>Novas frentes artísticas e didáticas articulando oficineiros, tutores formados em 2026 e docentes parceiros na criação de arranjos temáticos e apresentações integradas para a comunidade do câmpus.</p>
          </article>

          <article class="card" data-searchable>
            <span class="pill">🌐 Transferência Social</span>
            <h3>Rede Colaborativa de Câmpus IFSC</h3>
            <p>Compartilhamento do <em>Manual de Implementação Músico de Apoio</em>, dos estudos semanais e das calculadoras web com outros câmpus da Rede Federal e escolas públicas.</p>
          </article>
        </div>

""" + pager(("projeto-rac-and-roll.html", "Banda RAC &amp; Roll"), ("parcerias.html", "Parcerias &amp; Captação 2027")) + """
      </div>
    </section>"""

# ============================================================================
# 2D. PARCERIAS.HTML — VITRINE INSTITUCIONAL DE PARCERIAS & CAPTAÇÃO 2027
# ============================================================================
PARCERIAS_BODY = page_hero(
    [("Projetos", "projeto.html"), ("Parcerias &amp; Captação 2027", None)],
    "Parcerias &amp; Captação Institucional (Ciclo 2027)",
    "Vitrine técnica e apartidária de apoio ao Programa Músico de Apoio &amp; Sinfonia da Permanência (IFSC Câmpus São José): entregas comprovadas em 2026, rubricas de investimento 2027 e vias legais de fomento."
) + """
    <section class="section">
      <div class="container">
        <!-- Provas de Entrega 2026 -->
        <header class="section-header">
          <span class="section-tag">Retorno Institucional Comprovado</span>
          <h2>Por que Investir no Programa Músico de Apoio?</h2>
          <p>Enquadrado na <strong>Manutenção e Desenvolvimento do Ensino (MDE — LDB)</strong>, o projeto combate a evasão escolar no Ensino Médio Integrado por meio de inclusão, protagonismo discente e ciência aplicada.</p>
        </header>

        <div class="grid-4" style="margin-bottom:2.5rem;">
          <div class="metric-item" data-searchable>
            <span class="metric-value">100% AFP</span>
            <span class="metric-label">Execução integral do fomento 2026 (PISJE4706-2025)</span>
          </div>
          <div class="metric-item" data-searchable>
            <span class="metric-value">1 Estúdio</span>
            <span class="metric-label">Sala de Música reformada com 32 calços acústicos</span>
          </div>
          <div class="metric-item" data-searchable>
            <span class="metric-value">3 Eventos</span>
            <span class="metric-label">23ª SNCT, Aulão Live estadual e Feira de Jogos</span>
          </div>
          <div class="metric-item" data-searchable>
            <span class="metric-value">6 ODS ONU</span>
            <span class="metric-label">ODS 3, 4, 10, 11, 12 e 13 + inclusão PNAES/NAPNE</span>
          </div>
        </div>

        <!-- 3 Frentes de Investimento 2027 -->
        <header class="section-header">
          <span class="section-tag">Plano Orçamentário 2027 · Enquadramento MDE / SIOP</span>
          <h2>3 Frentes de Investimento para a Expansão 2027</h2>
          <p>Superando o teto dos editais internos, o fomento externo estrutura o acervo permanente do câmpus e amplia a permanência estudantil em dois turnos.</p>
        </header>

        <div class="grid-3" style="margin-bottom:2.5rem;">
          <article class="card card--accent-green" data-searchable>
            <span class="pill">Ação 20RL · GND 4 (Investimento)</span>
            <h3>1. Equipamentos &amp; Almoxarifado</h3>
            <ul class="check-list">
              <li>Aquisição patrimonial de contrabaixo elétrico, guitarra e amplificadores.</li>
              <li>Bateria acústica completa, jogo de pratos e ferragens permanentes do câmpus.</li>
              <li>Implantação física de <strong>almoxarifado próprio com porta e fechadura</strong> na Sala de Música.</li>
            </ul>
          </article>

          <article class="card card--accent-blue" data-searchable>
            <span class="pill pill--blue">Ação 20RL · GND 3 (Custeio)</span>
            <h3>2. Manutenção &amp; Eco-Lutheria</h3>
            <ul class="check-list">
              <li>Reposição contínua de encordoamentos, peles hidráulicas, palhetas, cabos P10/XLR e conectores.</li>
              <li>Insumos para o <strong>Caderno de Eco-Lutheria</strong> (tubos de PVC, conectores do Domo 2V e EPIs).</li>
              <li>Produção e diagramação do <em>Livro de Coletâneas Multimídia</em> e apostilas abertas.</li>
            </ul>
          </article>

          <article class="card card--accent-red" data-searchable>
            <span class="pill pill--red">Ação 2994 · PNAES / FEESC</span>
            <h3>3. Bolsas de Permanência (2 Turnos)</h3>
            <ul class="check-list">
              <li>Cotas de bolsas de tutoria e extensão para estudantes multiplicadores e oficineiros.</li>
              <li>Auxílio para permanência em <strong>dois turnos letivos</strong> (alimentação e transporte).</li>
              <li>Combate direto à vulnerabilidade socioeconômica e fortalecimento da PPE.</li>
            </ul>
          </article>
        </div>

        <!-- 3 Caminhos Legais de Apoio -->
        <header class="section-header">
          <span class="section-tag">Segurança Jurídica e Fluxo Institucional</span>
          <h2>Caminhos Legais para Apoiar o Projeto</h2>
        </header>

        <div class="grid-3" style="margin-bottom:2rem;">
          <article class="card" data-searchable>
            <span class="pill">Via Orçamentária Direta · MEC</span>
            <h3>Emendas Parlamentares Federais</h3>
            <p>Indicação no Orçamento da União vinculada ao MEC / IFSC (Ações 20RL e 2994, fundamentadas em MDE), com acompanhamento institucional da Reitoria e da Direção-Geral do Câmpus São José.</p>
          </article>

          <article class="card" data-searchable>
            <span class="pill pill--blue">Fundação de Apoio · FEESC</span>
            <h3>Empresas de São José &amp; ESG</h3>
            <p>Parcerias com empresas da região via <strong>FEESC</strong> (Fundação Stemmer para Pesquisa, Desenvolvimento e Inovação — credenciada ao IFSC pela <strong>Lei nº 8.958/1994</strong> e <strong>Resolução CONSUP/IFSC nº 61/2016</strong>).</p>
          </article>

          <article class="card" data-searchable>
            <span class="pill pill--red">Termo de Doação · Patrimônio</span>
            <h3>Doação Patrimonial de Instrumentos</h3>
            <p>Empresas, instituições e apoiadores podem doar instrumentos musicais ou insumos didáticos diretamente ao patrimônio do IFSC Câmpus São José mediante termo oficial.</p>
          </article>
        </div>

        <div class="ethics-box" data-searchable>
          <h2 style="margin:0 0 0.65rem;font-size:1.1rem;">Compromisso de Transparência e Prestação de Contas Pública</h2>
          <p style="margin:0 0 0.65rem;font-size:0.9rem;color:var(--text-secondary);">
            Todos os recursos captados e equipamentos incorporados são acompanhados pelos órgãos de controle do IFSC, divulgados com transparência institucional neste portal e apresentados publicamente à comunidade no concerto didático da <strong>24ª SNCT / MCC</strong> e no <strong>Didascálico</strong> (Mostra de Arte e Cultura do IFSC).
          </p>
          <p style="margin:0;font-size:0.86rem;">
            <strong>Contato para parcerias institucionais:</strong> Prof. Jorge Luiz Pereira (Coordenação) e Prof. Humberto Luz Oliveira (Colaboração) — IFSC Câmpus São José (<a href="equipe.html">ver Ficha Técnica e Governança</a>).
          </p>
        </div>

""" + pager(("projetos-futuros.html", "Projetos Futuros · 2027"), ("oficinas.html", "Oficinas")) + """
      </div>
    </section>"""

# ============================================================================
# 3. OFICINAS.HTML — OFICINAS & ESTÚDIO
# ============================================================================
OFICINAS_BODY = page_hero(
    [("Oficinas", None)],
    "Oficinas, Participação e Estúdio Digital",
    "Formação musical cooperativa para estudantes do Ensino Médio Integrado (Telecomunicações e Refrigeração), acompanhada de ferramentas rítmicas e de afinação 100% no navegador."
) + """
    <section class="section">
      <div class="container">
        <div class="grid-3" style="margin-bottom:2rem;">
          <article class="card card--accent-green" data-searchable>
            <span class="pill">Bolsista &amp; Tutores</span>
            <h3>Papel do "Músico de Apoio"</h3>
            <p>Estudantes selecionados atuam como pares-tutores: acompanham o andamento, sustentam a base harmônica e rítmica e apoiam os colegas iniciantes sem hierarquia excludente.</p>
          </article>
          <article class="card card--accent-blue" data-searchable>
            <span class="pill pill--blue">Dinâmica das Oficinas</span>
            <h3>Encontros Semanais na Sala de Música</h3>
            <p>Ciclos presenciais com 2 encontros semanais de 1h30 na Sala de Música (anexa ao auditório), combinando teoria aplicada, percepção rítmica e prática de conjunto.</p>
          </article>
          <article class="card card--accent-red" data-searchable>
            <span class="pill pill--red">Sem Pré-requisito</span>
            <h3>Iniciação Acolhedora</h3>
            <p>Não é necessário possuir instrumento próprio nem experiência prévia. O laboratório fornece bateria, percussão coletiva, violões, guitarra, baixo, teclado e instrumentos de Eco-Lutheria.</p>
          </article>
        </div>

        <div class="sensory-notice" role="note" aria-label="Aviso de conforto sensorial e controle de áudio">
          <div>
            <strong>Proteção Sensorial (TEA/NAPNE):</strong> nenhum som inicia automaticamente neste portal. O metrônomo e o diapasão abaixo permanecem silenciados até o seu clique.
            <span id="audio-live-status" class="sr-only" aria-live="polite">Áudio silenciado.</span>
          </div>
          <button type="button" class="btn btn-secondary btn-sm" id="btn-mute-all">🔇 Silenciar Tudo</button>
        </div>

        <div class="grid-2">
          <div class="studio-panel" data-searchable>
            <h3>Metrônomo Digital das Oficinas</h3>
            <p>Treino de pulsação e divisão rítmica no navegador (100% offline via Web Audio API).</p>
            <div class="bpm-row">
              <button type="button" class="bpm-step-btn" data-bpm-delta="-5" aria-label="Diminuir 5 BPM">−5</button>
              <button type="button" class="bpm-step-btn" data-bpm-delta="-1" aria-label="Diminuir 1 BPM">−1</button>
              <div class="bpm-readout"><span class="bpm-number mono" id="bpm-display">90</span><span class="bpm-unit">BPM</span></div>
              <button type="button" class="bpm-step-btn" data-bpm-delta="1" aria-label="Aumentar 1 BPM">+1</button>
              <button type="button" class="bpm-step-btn" data-bpm-delta="5" aria-label="Aumentar 5 BPM">+5</button>
            </div>
            <label for="bpm-slider" class="sr-only">Ajustar andamento em batidas por minuto</label>
            <input type="range" id="bpm-slider" min="40" max="200" value="90" style="width:100%;accent-color:#32A041;">
            <div class="beat-bar" id="beat-bar" aria-label="Indicador visual de tempos do compasso"></div>
            <div class="grid-2" style="gap:0.75rem;align-items:end;">
              <div class="field">
                <label for="metro-beats" style="color:#E2E8F0;">Fórmula de Compasso</label>
                <select id="metro-beats">
                  <option value="4" selected>4/4 — Quaternário (Rock/Pop)</option>
                  <option value="3">3/4 — Ternário (Valsa/Guarânia)</option>
                  <option value="2">2/4 — Binário (Baião/Samba)</option>
                  <option value="6">6/8 — Composto (Balada/Blues)</option>
                </select>
              </div>
              <button type="button" class="btn btn-primary" id="metro-toggle" aria-pressed="false">▶ Iniciar Metrônomo</button>
            </div>
            <div class="setlist-tags" style="margin-top:1rem;">
              <button type="button" class="a11y-btn" data-bpm-preset="70">70 BPM · Acordes</button>
              <button type="button" class="a11y-btn" data-bpm-preset="90">90 BPM · Pop/MPB</button>
              <button type="button" class="a11y-btn" data-bpm-preset="108">108 BPM · Rock</button>
              <button type="button" class="a11y-btn" data-bpm-preset="120">120 BPM · Baião</button>
            </div>
          </div>

          <div class="card" data-searchable>
            <span class="pill">Referência Auditiva · A4 = 440 Hz</span>
            <h3>Diapasão Web para Cordas e Tubofones</h3>
            <p>Clique em uma corda ou nota diatônica para emitir a frequência fundamental exata de referência durante os ensaios e a afinação na bancada.</p>
            <div class="field">
              <label for="tone-waveform">Timbre do Sintetizador</label>
              <select id="tone-waveform">
                <option value="triangle" selected>Triangular (Suave — Tubofone / Flauta)</option>
                <option value="sine">Senoidal Pura (Diapasão Acústico)</option>
                <option value="sawtooth">Rico em Harmônicos (Referência para Cordas)</option>
              </select>
            </div>
            <div>
              <strong style="font-size:0.78rem;text-transform:uppercase;color:var(--text-muted);display:block;margin-bottom:0.45rem;">Violão e Guitarra (Afinação Padrão)</strong>
              <div class="notes-grid" style="grid-template-columns:repeat(3,1fr);">
                <button type="button" class="note-btn" data-tone-freq="82.41" data-tone-label="6ª Corda E2">6ª E2 <small>82,4 Hz</small></button>
                <button type="button" class="note-btn" data-tone-freq="110.00" data-tone-label="5ª Corda A2">5ª A2 <small>110,0 Hz</small></button>
                <button type="button" class="note-btn" data-tone-freq="146.83" data-tone-label="4ª Corda D3">4ª D3 <small>146,8 Hz</small></button>
                <button type="button" class="note-btn" data-tone-freq="196.00" data-tone-label="3ª Corda G3">3ª G3 <small>196,0 Hz</small></button>
                <button type="button" class="note-btn" data-tone-freq="246.94" data-tone-label="2ª Corda B3">2ª B3 <small>246,9 Hz</small></button>
                <button type="button" class="note-btn" data-tone-freq="329.63" data-tone-label="1ª Corda E4">1ª E4 <small>329,6 Hz</small></button>
              </div>
            </div>
            <div>
              <strong style="font-size:0.78rem;text-transform:uppercase;color:var(--text-muted);display:block;margin-bottom:0.45rem;">Escala Diatônica Maior (Dó4 a Dó5)</strong>
              <div class="notes-grid">
                <button type="button" class="note-btn" data-tone-freq="261.63" data-tone-label="Dó4 (C4)">Dó (C4) <small>261,6 Hz</small></button>
                <button type="button" class="note-btn" data-tone-freq="293.66" data-tone-label="Ré4 (D4)">Ré (D4) <small>293,7 Hz</small></button>
                <button type="button" class="note-btn" data-tone-freq="329.63" data-tone-label="Mi4 (E4)">Mi (E4) <small>329,6 Hz</small></button>
                <button type="button" class="note-btn" data-tone-freq="349.23" data-tone-label="Fá4 (F4)">Fá (F4) <small>349,2 Hz</small></button>
                <button type="button" class="note-btn" data-tone-freq="392.00" data-tone-label="Sol4 (G4)">Sol (G4) <small>392,0 Hz</small></button>
                <button type="button" class="note-btn" data-tone-freq="440.00" data-tone-label="Lá4 (A4)">Lá (A4) <small>440,0 Hz</small></button>
                <button type="button" class="note-btn" data-tone-freq="493.88" data-tone-label="Si4 (B4)">Si (B4) <small>493,9 Hz</small></button>
                <button type="button" class="note-btn" data-tone-freq="523.25" data-tone-label="Dó5 (C5)">Dó (C5) <small>523,3 Hz</small></button>
              </div>
            </div>
          </div>
        </div>

""" + pager(("parcerias.html", "Parcerias &amp; Captação 2027"), ("eventos.html", "Eventos · Portfólio 2026")) + """
      </div>
    </section>"""

# ============================================================================
# 4A. EVENTOS.HTML — PORTFÓLIO 2026 (REALIZADOS)
# ============================================================================
EVENTOS_BODY = page_hero(
    [("Eventos", "eventos.html"), ("Portfólio 2026", None)],
    "Eventos · Portfólio Realizado em 2026",
    "Registros públicos, acervos oficiais e apresentações realizadas pelo Projeto Músico de Apoio no IFSC Câmpus São José ao longo do ciclo 2026."
) + """
    <section class="section">
      <div class="container">
        <div style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:0.75rem;margin-bottom:1.75rem;">
          <span class="pill">Ciclo 2026 Concluído · 3 Grandes Eventos</span>
          <a href="eventos-2027.html" class="btn btn-secondary btn-sm">Ver Agenda &amp; Eventos 2027 →</a>
        </div>

        <div class="grid-3">
          <article class="card card--accent-green" data-searchable>
            <span class="pill">30/10/2026 · Culminância</span>
            <h3>23ª SNCT &amp; 8ª Mostra Científica Cultural</h3>
            <p>Apresentação da <strong>Banda dos Músicos de Apoio</strong> no <em>Show de Talentos</em> do câmpus, reunindo discentes aprendizes e tutores na execução de peças preparadas nas oficinas presenciais de outubro.</p>
            <p style="font-size:0.82rem;color:var(--text-muted);">
              <strong>Certificado Oficial IFSC:</strong> autenticidade <span class="mono">20089782.04217683.8443185.8.00897820421768384431858</span>.
            </p>
            <div style="margin-top:auto;padding-top:0.5rem;">
              <a href="https://drive.google.com/drive/folders/19b-qqgw5ElqcGSa6ewLfSHoE83AjjyEx?usp=sharing" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm">
                Abrir Acervo Oficial (Extensão) ↗
              </a>
            </div>
          </article>

          <article class="card card--accent-red" data-searchable>
            <span class="pill pill--red">YouTube Live · Alcance Estadual</span>
            <h3>Aulão Musical de Vestibular do IFSC</h3>
            <p>Bolsista, tutor e o coordenador Prof. Jorge Luiz Pereira atuaram ao vivo como <em>músicos de apoio</em> dos docentes do câmpus em paródias interdisciplinares com dicas para o vestibular, transmitidas ao vivo pelo YouTube.</p>
            <div class="video-facade" aria-label="Player sob demanda do Aulão Musical de Vestibular do IFSC">
              <p style="color:#E2E8F0;font-size:0.82rem;margin:0 0 0.85rem;">Carregamento sob demanda (sem reprodução automática · áudio inicia mudo).</p>
              <button type="button" class="video-play-btn" data-yt-load="t1BAm_mXt-0" data-yt-title="Vestibular IFSC 2027/1 — Aulão Musical">▶ Carregar Vídeo do YouTube</button>
            </div>
            <div style="margin-top:auto;padding-top:0.4rem;">
              <a href="https://www.youtube.com/live/t1BAm_mXt-0" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-sm">Assistir no YouTube Oficial ↗</a>
            </div>
          </article>

          <article class="card card--accent-blue" data-searchable>
            <span class="pill pill--blue">19/11/2026 · Abertura Oficial</span>
            <h3>Feira de Jogos 2026.2 — Banda Músicos de Apoio</h3>
            <p>Show de abertura da Feira de Jogos no auditório do Câmpus São José com 13 registros audiovisuais, consolidando o repertório coletivo e formando o núcleo inicial de tutores para a edição 2027.</p>
            <div>
              <strong style="font-size:0.76rem;text-transform:uppercase;color:var(--text-muted);display:block;margin-bottom:0.4rem;">Repertório Executado:</strong>
              <div class="setlist-tags">
                <span class="setlist-tag">Sangue Latino</span><span class="setlist-tag">Preta Pretinha</span>
                <span class="setlist-tag">Vampiro Doidão</span><span class="setlist-tag">S.O.S.</span>
                <span class="setlist-tag">Sweet Home Alabama</span><span class="setlist-tag">What's Up?</span>
                <span class="setlist-tag">Versão Nazareth</span>
              </div>
            </div>
            <div style="margin-top:auto;padding-top:0.5rem;">
              <a href="https://drive.google.com/drive/folders/1a1DQWz-fpDmJqDzLh6jj91_zjrW52owD?usp=drive_link" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm">Abrir Pasta das 13 Gravações ↗</a>
            </div>
          </article>
        </div>

""" + pager(("oficinas.html", "Oficinas"), ("eventos-2027.html", "Agenda &amp; Eventos 2027")) + """
      </div>
    </section>"""

# ============================================================================
# 4B. EVENTOS-2027.HTML — AGENDA & EVENTOS DO ANO CORRENTE / 2027
# ============================================================================
EVENTOS_2027_BODY = page_hero(
    [("Eventos", "eventos.html"), ("Agenda &amp; Eventos 2027", None)],
    "Agenda &amp; Eventos Previstos — Ciclo 2027",
    "Calendário anual de apresentações culturais, oficinas abertas e eventos científicos nos quais o Programa Músico de Apoio e seus projetos integrados participarão ao longo de 2027."
) + """
    <section class="section">
      <div class="container">
        <div class="table-wrap" style="margin-bottom:2rem;" data-searchable>
          <table>
            <thead>
              <tr>
                <th scope="col">Período Previsto</th>
                <th scope="col">Evento / Ação</th>
                <th scope="col">Projetos Envolvidos</th>
                <th scope="col">Situação</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="mono">Março / 2027</td>
                <td><strong>Acolhida Estudantil &amp; Seleção de Tutores</strong> — Apresentação musical de boas-vindas e abertura de inscrições das oficinas.</td>
                <td>Músico de Apoio · Banda RAC &amp; Roll</td>
                <td><span class="pill pill--blue">Previsto</span></td>
              </tr>
              <tr>
                <td class="mono">Abr–Jul / 2027</td>
                <td><strong>Ciclo de Oficinas de Eco-Lutheria e Montagem do Domo 2V</strong> — Encontros práticos interdisciplinares no Câmpus São José.</td>
                <td>Músico de Apoio · Sinfonia da Permanência</td>
                <td><span class="pill pill--blue">Previsto</span></td>
              </tr>
              <tr>
                <td class="mono">2º Sem / 2027</td>
                <td><strong>Aulão Musical de Vestibular do IFSC</strong> — Nova edição com paródias interdisciplinares transmitidas ao vivo.</td>
                <td>Músico de Apoio · Docentes do Câmpus</td>
                <td><span class="pill pill--blue">Previsto</span></td>
              </tr>
              <tr>
                <td class="mono">Outubro / 2027</td>
                <td><strong>SNCT &amp; Mostra Científica Cultural (MCC 2027) / SEPEI</strong> — Culminância da <em>Sinfonia da Permanência</em> no Domo 2V e socialização científica.</td>
                <td>Todos os Projetos do Guarda-Chuva</td>
                <td><span class="pill">Marco Principal</span></td>
              </tr>
              <tr>
                <td class="mono">Novembro / 2027</td>
                <td><strong>Didascálico (Mostra de Arte e Cultura do IFSC) &amp; Feira de Jogos</strong> — Apresentações artísticas no Câmpus São José, concerto didático comemorativo de prestação de contas pública e formatura da nova geração de tutores.</td>
                <td>Músico de Apoio · Banda RAC &amp; Roll · Sinfonia da Permanência</td>
                <td><span class="pill pill--blue">Previsto</span></td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="card" data-searchable>
          <span class="pill">Atualização Contínua</span>
          <h3>Acompanhe e convide o projeto para eventos do Câmpus</h3>
          <p>À medida que cada evento de 2027 for confirmado e realizado, esta página será atualizada com datas exatas, links de transmissão, registros fotográficos e certificados institucionais — mantendo o histórico completo organizado por ano no submenu <strong>Eventos</strong>.</p>
        </div>

""" + pager(("eventos.html", "Portfólio 2026"), ("tecnologia-social.html", "Tecnologia Social")) + """
      </div>
    </section>"""

# ============================================================================
# 5A. TECNOLOGIA-SOCIAL.HTML — MANUAL & REPLICABILIDADE
# ============================================================================
TS_BODY = page_hero(
    [("Tecnologia Social", "tecnologia-social.html"), ("Manual &amp; Replicabilidade", None)],
    "Tecnologia Social &amp; Replicabilidade na Rede Federal",
    "O modelo Músico de Apoio é sistematizado como Tecnologia Social aberta, permitindo que qualquer câmpus ou escola pública implante oficinas inclusivas de música e acústica a baixo custo."
) + """
    <section class="section">
      <div class="container">
        <div class="grid-2" style="margin-bottom:2.25rem;">
          <article class="card card--accent-green" data-searchable>
            <span class="pill">Produto Principal · Edital 12/2025</span>
            <h3>Manual de Implementação Músico de Apoio-IFSC</h3>
            <p>Guia aberto com protocolos práticos para docentes, coordenadores de extensão e núcleos de acessibilidade (NAPNE):</p>
            <ul class="check-list">
              <li>Adequação de sala de música com desacoplamento antivibração por calços de borracha de alta densidade.</li>
              <li>Seleção e capacitação de discentes tutores (<em>sidemen</em>) em grupos heterogêneos inclusivos.</li>
              <li>Articulação curricular com o Projeto Integrador e eventos culturais do câmpus.</li>
            </ul>
          </article>

          <article class="card card--accent-blue" data-searchable>
            <span class="pill pill--blue">Acervo Compartilhado</span>
            <h3>Apostilas e Novas Tecnologias Sociais</h3>
            <p>Todas as apostilas criadas nas oficinas — bem como novas soluções testadas e validadas com a comunidade — ficam reunidas na subpágina de materiais didáticos.</p>
            <div style="margin-top:auto;padding-top:0.5rem;">
              <a href="apostilas.html" class="btn btn-primary btn-sm">Abrir Apostilas &amp; Materiais →</a>
            </div>
          </article>
        </div>

        <header class="section-header">
          <span class="section-tag">Transferência Social</span>
          <h2>4 Passos para Replicar em Outras Escolas</h2>
        </header>
        <div class="grid-4">
          <div class="step-box" data-searchable><span class="step-num">1</span><h4>Espaço Acústico</h4><p>Reaproveitar uma sala ociosa com isolamento e calços antivibração de baixo custo.</p></div>
          <div class="step-box" data-searchable><span class="step-num">2</span><h4>Tutoria por Pares</h4><p>Capacitar estudantes multiplicadores para mediar oficinas sem hierarquia excludente.</p></div>
          <div class="step-box" data-searchable><span class="step-num">3</span><h4>Eco-Lutheria</h4><p>Construir tubofones de PVC e percussão afinada quando não houver verba para instrumentos caros.</p></div>
          <div class="step-box" data-searchable><span class="step-num">4</span><h4>Difusão Aberta</h4><p>Compartilhar apostilas, planos de corte e calculadoras em arquitetura web gratuita.</p></div>
        </div>

""" + pager(("eventos-2027.html", "Agenda &amp; Eventos 2027"), ("apostilas.html", "Apostilas &amp; Materiais")) + """
      </div>
    </section>"""

# ============================================================================
# 5B. APOSTILAS.HTML — SUBPÁGINA DE APOSTILAS E MATERIAIS DIDÁTICOS
# ============================================================================
APOSTILAS_BODY = page_hero(
    [("Tecnologia Social", "tecnologia-social.html"), ("Apostilas &amp; Materiais Didáticos", None)],
    "Apostilas &amp; Materiais Didáticos Abertos",
    "Materiais produzidos pelos bolsistas, tutores e docentes do projeto para estudo autônomo e aplicação em oficinas musicais inclusivas."
) + """
    <section class="section">
      <div class="container">
        <div class="grid-3" style="margin-bottom:2rem;">
          <article class="card card--accent-green" data-searchable>
            <span class="pill">Apostila 1 · Percussão</span>
            <h3>Fundamentos de Bateria e Pulsação</h3>
            <p>Elaborada pelo bolsista João Alvarenga Lourenção e equipe docente para iniciação rápida sem experiência prévia:</p>
            <ul class="check-list">
              <li>Ergonomia e empunhadura (<em>matched grip</em>) e controle de rebote.</li>
              <li>Anatomia do kit acústico e leitura de figuras rítmicas (mínima, semínima, colcheia e pausas).</li>
              <li>Independência motora cooperativa integrada à percussão coletiva (pandeirolas, ganzás e triângulo).</li>
            </ul>
          </article>

          <article class="card card--accent-blue" data-searchable>
            <span class="pill pill--blue">Apostila 2 · Harmonia</span>
            <h3>Violão, Cifras e Técnica de Dedos-Pivô</h3>
            <p>Roteiro prático das oficinas voltado a destravar as primeiras progressões harmônicas e o papel do <em>sideman</em> em grupo:</p>
            <ul class="check-list">
              <li>Leitura universal de cifras (<span class="mono">C, D, E, F, G, A, B</span>), acordes maiores, menores e com sétima.</li>
              <li>Técnica de dedos-pivô (<span class="mono">Em ↔ G ↔ D ↔ C</span>) reduzindo a ansiedade motora em iniciantes.</li>
              <li>Sincronismo rítmico da mão direita com o bumbo e a caixa da bateria.</li>
            </ul>
          </article>

          <article class="card card--accent-red" data-searchable>
            <span class="pill pill--red">Em Expansão · 2027</span>
            <h3>Cadernos de Eco-Lutheria &amp; Novas Tecnologias</h3>
            <p>Caderno técnico desenvolvido com <strong>Fábio Henrique de Carvalho Bartelega</strong>, <strong>Prof. Humberto Luz Oliveira</strong> e <strong>Prof. Jorge Luiz Pereira</strong> para fabricação afinada de tubofones de PVC, latas metálicas e garrafas PET.</p>
            <div style="margin-top:auto;padding-top:0.5rem;">
              <a href="sinfonia-inovacao.html" class="btn btn-secondary btn-sm">Ir para Calculadoras →</a>
            </div>
          </article>
        </div>

        <header class="section-header" style="margin-top:2.5rem;">
          <span class="section-tag">Ciclo 2027 · Planejamento Pedagógico-Musical</span>
          <h2>Estudos Semanais por Instrumento &amp; Livro de Coletâneas Multimídia</h2>
          <p>Rotina contínua de estudos técnicos semanais para aprendizes e oficineiros, consolidando o repertório do ano letivo em um acervo multimídia unificado.</p>
        </header>

        <div class="grid-4" style="margin-bottom:1.5rem;">
          <article class="card card--accent-green" data-searchable>
            <span class="pill">Em Desenvolvimento · 2027</span>
            <h3>🎸 Baixo Elétrico</h3>
            <p>Estudos semanais de <em>riffs</em>, fraseados de condução, construção de motivos rítmicos, <em>grooves</em> e levadas para sustentação de banda.</p>
          </article>

          <article class="card card--accent-blue" data-searchable>
            <span class="pill pill--blue">Em Desenvolvimento · 2027</span>
            <h3>🎵 Violão &amp; Guitarra</h3>
            <p>Fraseados melódicos, acompanhamento harmônico com dedos-pivô, levadas rítmicas e condução pedagógica coletiva nas oficinas.</p>
          </article>

          <article class="card card--accent-green" data-searchable>
            <span class="pill">Em Desenvolvimento · 2027</span>
            <h3>🎹 Teclado</h3>
            <p>Mapeamento de acordes, inversões práticas, harmonização básica e apoio à base harmônica do conjunto estudantil.</p>
          </article>

          <article class="card card--accent-red" data-searchable>
            <span class="pill pill--amber">Produto Editorial · Meta 2027</span>
            <h3>📚 Livro de Coletâneas Multimídia</h3>
            <p>Compilação anual em <strong>E-book / PDF</strong> (partituras e cifras) integrada a <strong>playbacks MP3</strong> e <strong>vídeos demonstrativos MP4</strong> para estudo autônomo.</p>
          </article>
        </div>

""" + pager(("tecnologia-social.html", "Manual &amp; Replicabilidade"), ("sinfonia-inovacao.html", "Sinfonia &amp; Inovação")) + """
      </div>
    </section>"""

# ============================================================================
# 6A. SINFONIA-INOVACAO.HTML — CALCULADORAS CLIENT-SIDE (LIMPO E FOCADO)
# ============================================================================
SINFONIA_BODY = page_hero(
    [("Sinfonia &amp; Inovação", "sinfonia-inovacao.html"), ("Calculadoras Científicas", None)],
    "Sinfonia &amp; Inovação — Calculadoras Científicas",
    "Parceria com o projeto Sinfonia da Permanência (autoria do especialista em Educação Ambiental Fábio Henrique de Carvalho Bartelega): ferramentas 100% client-side para Eco-Lutheria e Domo Geodésico 2V."
) + """
    <section class="section">
      <div class="container">
        <div class="sensory-notice" role="note">
          <div>
            <strong>100% Client-Side &amp; Conforto Sensorial:</strong> funciona offline no navegador; os tons de conferência só tocam após o seu clique.
            <span id="audio-live-status" class="sr-only" aria-live="polite">Áudio silenciado.</span>
          </div>
          <div style="display:flex;gap:0.5rem;flex-wrap:wrap;">
            <a href="sinfonia-bncc.html" class="btn btn-secondary btn-sm">Ver Matriz BNCC &amp; 7 Encontros →</a>
            <button type="button" class="btn btn-secondary btn-sm" id="btn-mute-all">🔇 Silenciar Som</button>
          </div>
        </div>

        <div class="calc-tabs" role="tablist" aria-label="Módulos das calculadoras científicas">
          <button type="button" class="calc-tab-btn" role="tab" id="tab-btn-pvc" aria-selected="true" aria-controls="panel-pvc">
            Módulo A · Tubofones de PVC (Física Acústica)
          </button>
          <button type="button" class="calc-tab-btn" role="tab" id="tab-btn-dome" aria-selected="false" aria-controls="panel-dome">
            Módulo B · Domo Geodésico 2V (Geometria &amp; Ecologia)
          </button>
          <button type="button" class="btn btn-secondary btn-sm" id="btn-print-plan" style="margin-left:auto;">
            🖨 Imprimir / Salvar Plano de Corte
          </button>
        </div>

        <!-- MÓDULO A -->
        <div class="calc-panel" id="panel-pvc" role="tabpanel" aria-labelledby="tab-btn-pvc">
          <div class="card" data-searchable>
            <div style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:0.75rem;">
              <div>
                <span class="pill">BNCC: EM13CNT301 · Ondulatória Aplicada</span>
                <h2 style="margin:0.35rem 0 0;font-size:1.25rem;">Dimensionamento de Tubos Abertos com Correção de Helmholtz</h2>
              </div>
              <code class="mono" style="background:var(--bg-dark);color:#5CE671;padding:0.45rem 0.8rem;border-radius:var(--radius-sm);font-size:0.84rem;">L = v / (2·f) − 1,22·r</code>
            </div>

            <div class="calc-controls">
              <div class="field">
                <label for="pvc-temp">Temperatura da Oficina (°C)</label>
                <input type="number" id="pvc-temp" value="20" min="5" max="40" step="1">
                <span class="field-hint" id="pvc-speed-out">v = 343,40 m/s (20 °C)</span>
              </div>
              <div class="field">
                <label for="pvc-diameter">Bitola do Tubo PVC (Diâmetro Interno)</label>
                <select id="pvc-diameter">
                  <option value="21.6">PVC 25 mm (Ø interno 21,6 mm)</option>
                  <option value="27.8">PVC 32 mm (Ø interno 27,8 mm)</option>
                  <option value="36.0">PVC 40 mm — Esgoto (Ø interno 36,0 mm)</option>
                  <option value="46.4" selected>PVC 50 mm — Esgoto (Ø interno 46,4 mm · Padrão)</option>
                  <option value="71.2">PVC 75 mm — Esgoto (Ø interno 71,2 mm · Graves)</option>
                  <option value="96.4">PVC 100 mm — Esgoto (Ø interno 96,4 mm · Subgraves)</option>
                </select>
                <span class="field-hint" id="pvc-corr-out">Correção 1,22·r = 2,83 cm</span>
              </div>
              <div class="field">
                <label for="pvc-octave">Oitava Musical</label>
                <select id="pvc-octave">
                  <option value="3">Oitava 3 (C3–C4 · Grave)</option>
                  <option value="4" selected>Oitava 4 (C4–C5 · Médio Escolar)</option>
                  <option value="5">Oitava 5 (C5–C6 · Agudo)</option>
                </select>
                <label style="display:flex;align-items:center;gap:0.4rem;margin-top:0.45rem;font-weight:600;font-size:0.78rem;cursor:pointer;">
                  <input type="checkbox" id="pvc-only-natural" style="width:auto;"> Mostrar apenas notas naturais (escala diatônica)
                </label>
              </div>
            </div>

            <div style="display:flex;flex-wrap:wrap;align-items:center;gap:0.75rem;padding:0.75rem 1rem;background:var(--ifsc-verde-suave);border-radius:var(--radius-sm);border:1px solid rgba(50,160,65,0.3);">
              <label for="pvc-custom-freq" style="font-size:0.84rem;font-weight:700;">Frequência livre (Hz):</label>
              <input type="number" id="pvc-custom-freq" value="440" min="50" max="2000" step="0.5" style="width:110px;padding:0.38rem 0.6rem;border-radius:5px;border:1.5px solid var(--border-strong);font-family:var(--font-mono);font-weight:700;">
              <strong id="pvc-custom-out" class="mono" style="font-size:0.86rem;color:var(--ifsc-verde-escuro);"></strong>
            </div>

            <div class="table-wrap">
              <table>
                <caption class="sr-only">Tabela de comprimento de corte para tubofones de PVC conforme temperatura e bitola</caption>
                <thead>
                  <tr>
                    <th scope="col">Nota / Cifra</th><th scope="col">Classificação</th><th scope="col">Frequência (f)</th>
                    <th scope="col">Teórico (v/2f)</th><th scope="col">Corte Exato (L)</th><th scope="col">Proporção</th><th scope="col">Áudio (Clique)</th>
                  </tr>
                </thead>
                <tbody id="pvc-tbody"></tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- MÓDULO B -->
        <div class="calc-panel" id="panel-dome" role="tabpanel" aria-labelledby="tab-btn-dome" hidden>
          <div class="card" data-searchable>
            <div style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:0.75rem;">
              <div>
                <span class="pill pill--blue">BNCC: EM13MAT308 · EM13CNT105</span>
                <h2 style="margin:0.35rem 0 0;font-size:1.25rem;">Dimensionamento do Domo Geodésico 2V &amp; Escala de Permanência</h2>
              </div>
              <code class="mono" style="background:var(--bg-dark);color:#93C5FD;padding:0.45rem 0.8rem;border-radius:var(--radius-sm);font-size:0.84rem;">Euler: V − A + F = 26 − 65 + 40 = 1</code>
            </div>

            <div class="grid-2" style="align-items:start;">
              <div>
                <div class="calc-controls" style="grid-template-columns:1fr;margin-bottom:1rem;">
                  <div class="field">
                    <label for="dome-radius">Raio do Domo Geodésico 2V — R (em metros)</label>
                    <input type="number" id="dome-radius" value="2.00" min="0.50" max="8.00" step="0.10">
                    <div class="setlist-tags" style="margin-top:0.6rem;">
                      <button type="button" class="btn btn-secondary btn-sm" data-dome-preset="1.00">Maquete (1,0 m)</button>
                      <button type="button" class="btn btn-primary btn-sm" data-dome-preset="2.00">Padrão IFSC (2,0 m)</button>
                      <button type="button" class="btn btn-secondary btn-sm" data-dome-preset="3.00">Pátio (3,0 m)</button>
                    </div>
                  </div>
                </div>

                <div class="table-wrap">
                  <table>
                    <caption class="sr-only">Lista de usinagem das 65 barras e parâmetros geométricos do Domo 2V</caption>
                    <thead><tr><th scope="col">Parâmetro / Peça</th><th scope="col">Fator / Quantidade</th><th scope="col">Medida Calculada</th></tr></thead>
                    <tbody>
                      <tr><td><strong>Barras Tipo A</strong></td><td class="mono">0,6180·R · 35 un.</td><td class="cut-highlight" id="dome-out-la">1,236 m</td></tr>
                      <tr><td><strong>Barras Tipo B</strong></td><td class="mono">0,5465·R · 30 un.</td><td class="cut-highlight" id="dome-out-lb">1,093 m</td></tr>
                      <tr><td>Metragem Linear (Tipo A)</td><td>35 barras</td><td class="mono" id="dome-out-tot-a">43,26 m</td></tr>
                      <tr><td>Metragem Linear (Tipo B)</td><td>30 barras</td><td class="mono" id="dome-out-tot-b">32,79 m</td></tr>
                      <tr><td><strong>Total de Material Linear</strong></td><td><strong>65 barras · 26 nós</strong></td><td class="cut-highlight" id="dome-out-linear">76,05 m</td></tr>
                      <tr><td>Diâmetro / Altura (2R / R)</td><td>Hemisfério 2V</td><td class="mono"><span id="dome-out-diam">4,00 m</span> / <span id="dome-out-height">2,00 m</span></td></tr>
                      <tr><td>Área Circular de Piso</td><td class="mono">π·R²</td><td class="mono" id="dome-out-area">12,57 m²</td></tr>
                    </tbody>
                  </table>
                </div>
              </div>

              <div style="display:flex;flex-direction:column;gap:1rem;">
                <div style="background:var(--bg-dark);border-radius:var(--radius-md);padding:1rem;color:#FFFFFF;">
                  <svg viewBox="0 0 360 170" role="img" aria-label="Corte vertical do Domo 2V com os 3 estratos de permanência ecológica" width="100%">
                    <path d="M 40 145 A 140 120 0 0 1 320 145 Z" fill="rgba(50,160,65,0.14)" stroke="#5CE671" stroke-width="2"/>
                    <line x1="30" y1="25" x2="330" y2="25" stroke="#FCA5A5" stroke-dasharray="4 3"/>
                    <line x1="30" y1="85" x2="330" y2="85" stroke="#FDE68A" stroke-dasharray="4 3"/>
                    <line x1="30" y1="138" x2="330" y2="138" stroke="#86EFAC" stroke-dasharray="4 3"/>
                    <text x="180" y="20" text-anchor="middle" fill="#FCA5A5" font-size="10" font-family="Open Sans, sans-serif" font-weight="700" id="svg-cota-3">Ápice: 2,00 m (400–4.000 anos)</text>
                    <text x="180" y="80" text-anchor="middle" fill="#FDE68A" font-size="10" font-family="Open Sans, sans-serif" font-weight="700" id="svg-cota-2">Médio: 1,00 m (50–500 anos)</text>
                    <text x="180" y="133" text-anchor="middle" fill="#86EFAC" font-size="10" font-family="Open Sans, sans-serif" font-weight="700" id="svg-cota-1">Base: 0,10 m (Semanas–Meses)</text>
                    <text x="180" y="162" text-anchor="middle" fill="#CBD5E1" font-size="10" font-family="JetBrains Mono, monospace" id="svg-dome-r">R = 2,00 m · Diâmetro = 4,00 m</text>
                  </svg>
                </div>

                <div class="strata-list">
                  <div class="stratum-card stratum--high"><div class="stratum-head"><span>▲ Estrato 3 · Alta Persistência (400–4.000 anos)</span><span class="mono" id="stratum-cota-3">2,00 m</span></div><p style="font-size:0.82rem;">Tubofones de PVC, idiófonos de garrafas PET e vidro (ligações C–C e SiO₂).</p></div>
                  <div class="stratum-card stratum--mid"><div class="stratum-head"><span>◆ Estrato 2 · Persistência Intermediária (50–500 anos)</span><span class="mono" id="stratum-cota-2">1,00 m</span></div><p style="font-size:0.82rem;">Membranofones de latas de aço e alumínio passivado (Al₂O₃).</p></div>
                  <div class="stratum-card stratum--low"><div class="stratum-head"><span>● Estrato 1 · Degradação Rápida (Semanas a Meses)</span><span class="mono" id="stratum-cota-1">0,10 m</span></div><p style="font-size:0.82rem;">Chocalhos e ressonadores de papelão, celulose e sementes naturais.</p></div>
                </div>
              </div>
            </div>
          </div>
        </div>

""" + pager(("apostilas.html", "Apostilas &amp; Materiais"), ("sinfonia-bncc.html", "Matriz BNCC &amp; 7 Encontros")) + """
      </div>
    </section>"""

# ============================================================================
# 6B. SINFONIA-BNCC.HTML — MATRIZ INTERDISCIPLINAR BNCC & 7 ENCONTROS
# ============================================================================
SINFONIA_BNCC_BODY = page_hero(
    [("Sinfonia &amp; Inovação", "sinfonia-inovacao.html"), ("Matriz BNCC &amp; 7 Encontros", None)],
    "Matriz Interdisciplinar BNCC &amp; Trilha dos 7 Encontros",
    "Engenharia didática do projeto parceiro Sinfonia da Permanência (Fábio Henrique de Carvalho Bartelega) integrada ao Ensino Médio Integrado do IFSC Câmpus São José."
) + """
    <section class="section">
      <div class="container">
        <div class="card" style="margin-bottom:2.25rem;" data-searchable>
          <span class="pill">Integração Curricular EMI · 5 Unidades Curriculares</span>
          <h2>Matriz Interdisciplinar BNCC (11 Habilidades Mobilizadas)</h2>
          <div class="table-wrap">
            <table>
              <thead>
                <tr>
                  <th scope="col">Unidade Curricular</th><th scope="col">Conteúdos e Equações</th>
                  <th scope="col">Aplicação na Eco-Lutheria e Domo 2V</th><th scope="col">Habilidades BNCC</th>
                </tr>
              </thead>
              <tbody>
                <tr><td><strong>Física</strong></td><td>Ondas estacionárias, frequência fundamental (<span class="mono">f = v/2L</span>), efeito de borda de Rayleigh e nível sonoro (dB).</td><td>Corte calibrado dos tubofones de PVC e conferência espectral (<span class="mono">&lt; 5 cents</span>).</td><td class="mono">EM13CNT301, EM13MAT306</td></tr>
                <tr><td><strong>Química</strong></td><td>Polímeros sintéticos (PET/PVC), oxirredução/passivação (<span class="mono">Al₂O₃</span>), sílica e celulose.</td><td>Correlação entre estabilidade química e rigidez acústica dos materiais reciclados.</td><td class="mono">EM13CNT104, EM13CNT307</td></tr>
                <tr><td><strong>Biologia &amp; Ed. Ambiental</strong></td><td>Ciclos biogeoquímicos, tempo de residência na biosfera, microplásticos e biossegurança.</td><td>Triagem com EPIs, balanço de massa (kg) e organização nos 3 estratos do Domo.</td><td class="mono">EM13CNT105, EM13CNT306</td></tr>
                <tr><td><strong>Matemática</strong></td><td>Icosaedro, Relação de Euler (<span class="mono">V−A+F=1</span>), fatores de corda e estatística descritiva.</td><td>Usinagem das 65 barras / 26 conectores e tabulação de desvios de afinação.</td><td class="mono">EM13MAT105, 201, 202, 308</td></tr>
                <tr><td><strong>Artes &amp; Projeto Integrador</strong></td><td>Abordagem Triangular, pulsação rítmica e tutoria musical cooperativa por pares.</td><td>Ensaios inclusivos e culminância pública da <em>Sinfonia da Permanência</em>.</td><td class="mono">EM13LGG602, EM13LGG603</td></tr>
              </tbody>
            </table>
          </div>
        </div>

        <header class="section-header">
          <span class="section-tag">Sequência Didática · Dupla Ancoragem (TAS + PNL-VAC)</span>
          <h2>Trilha dos 7 Encontros Formativos</h2>
        </header>
        <div class="grid-4">
          <div class="step-box" data-searchable><span class="step-num">1</span><h4>Sensibilização VAC</h4><p>Contraste auditivo-visual entre paisagens sonoras e descarte urbano; 1º Mapa Mental.</p></div>
          <div class="step-box" data-searchable><span class="step-num">2</span><h4>Química &amp; EPIs</h4><p>Triagem higienizada com biossegurança, pesagem gravimétrica e estudo dos polímeros.</p></div>
          <div class="step-box" data-searchable><span class="step-num">3</span><h4>Domo Geodésico 2V</h4><p>Estudo do icosaedro, Relação de Euler e montagem cooperativa das 65 barras e 26 nós.</p></div>
          <div class="step-box" data-searchable><span class="step-num">4</span><h4>Bancada Eco-Lutheria</h4><p>Corte e afinação acústica (<span class="mono">f = v/2L</span>) de tubofones PVC, membranofones e idiófonos.</p></div>
          <div class="step-box" data-searchable><span class="step-num">5</span><h4>Organizador Prévio 3D</h4><p>Suspensão dos instrumentos nas 3 cotas verticais do Domo conforme a persistência ecológica.</p></div>
          <div class="step-box" data-searchable><span class="step-num">6</span><h4>Ensaio Cooperativo</h4><p>Prática <em>Músico de Apoio</em> unindo os instrumentos reciclados à bateria, violão e teclado.</p></div>
          <div class="step-box" data-searchable style="grid-column:span 2;"><span class="step-num">7</span><h4>Culminância &amp; Transferência Social</h4><p>Apresentação da <em>Sinfonia da Permanência</em> na SNCT/MCC e difusão pública do Guia Técnico-Pedagógico Aberto.</p></div>
        </div>

""" + pager(("sinfonia-inovacao.html", "Calculadoras Científicas"), ("equipe.html", "Equipe e Ética")) + """
      </div>
    </section>"""

# ============================================================================
# 7. EQUIPE.HTML — EQUIPE E ÉTICA
# ============================================================================
EQUIPE_BODY = page_hero(
    [("Equipe e Ética", None)],
    "Equipe, Governança, ODS e Conformidade Ética",
    "Pesquisadores, parceiros e tutores do IFSC Câmpus São José, alinhamento à Agenda 2030 da ONU e compromissos de acessibilidade digital, LGPD, ECA e direitos autorais."
) + """
    <section class="section">
      <div class="container">
        <header class="section-header">
          <span class="section-tag">Ficha Técnica</span>
          <h2>Equipe Executora e Parceria</h2>
        </header>

        <div class="grid-4" style="margin-bottom:2.5rem;">
          <article class="card card--accent-green" data-searchable>
            <span class="pill">Coordenação</span>
            <h3>Prof. Jorge Luiz Pereira</h3>
            <p>Coordenador do Projeto Músico de Apoio-IFSC e organizador da Banda RAC &amp; Roll · Coordenadoria de Refrigeração e Climatização.</p>
          </article>
          <article class="card card--accent-blue" data-searchable>
            <span class="pill pill--blue">Colaboração &amp; Física</span>
            <h3>Prof. Humberto Luz Oliveira</h3>
            <p>Pesquisador Colaborador · Física Acústica, Arquitetura Web e Tecnologia Social (NeDEC · IFSC Câmpus São José).</p>
          </article>
          <article class="card card--accent-red" data-searchable>
            <span class="pill pill--red">Parceria · Sinfonia</span>
            <h3>Fábio Henrique de Carvalho Bartelega</h3>
            <p>Especialista em Educação Ambiental e autor do projeto parceiro <em>Sinfonia da Permanência</em> (Eco-Lutheria e Domo Geodésico 2V).</p>
          </article>
          <article class="card card--accent-green" data-searchable>
            <span class="pill">Bolsista &amp; Tutores</span>
            <h3>João Alvarenga Lourenção</h3>
            <p>Discente Pesquisador Bolsista (Ciclo 2026 · EMI Telecomunicações), autor das apostilas de base e formador do núcleo inicial de tutores para 2027.</p>
          </article>
        </div>

        <header class="section-header">
          <span class="section-tag">Agenda 2030 da ONU</span>
          <h2>Objetivos de Desenvolvimento Sustentável (ODS)</h2>
        </header>

        <div class="ods-grid" style="margin-bottom:2.5rem;">
          <div class="ods-card" data-searchable><span class="ods-badge">ODS 4</span><div><h4>Educação de Qualidade</h4><p>Educação inclusiva, equitativa e voltada ao desenvolvimento sustentável no EMI.</p></div></div>
          <div class="ods-card" data-searchable><span class="ods-badge">ODS 10</span><div><h4>Redução das Desigualdades</h4><p>Inversão de papéis pedagógicos com protagonismo estudantil em tutoria por pares.</p></div></div>
          <div class="ods-card" data-searchable><span class="ods-badge">ODS 12</span><div><h4>Consumo Responsável</h4><p>Transformação de resíduos recicláveis (PVC, PET, latas) em instrumentos calibrados.</p></div></div>
          <div class="ods-card" data-searchable><span class="ods-badge">ODS 3</span><div><h4>Saúde e Bem-Estar</h4><p>Promoção da saúde socioemocional e redução do isolamento juvenil pela música coletiva.</p></div></div>
          <div class="ods-card" data-searchable><span class="ods-badge">ODS 11</span><div><h4>Cidades Sustentáveis</h4><p>Gestão educativa de resíduos urbanos e transferência social para escolas públicas.</p></div></div>
          <div class="ods-card" data-searchable><span class="ods-badge">ODS 13</span><div><h4>Ação Contra Mudança do Clima</h4><p>Conscientização crítica sobre ciclos biogeoquímicos e persistência secular de polímeros.</p></div></div>
        </div>

        <div class="ethics-box" data-searchable>
          <h2 style="margin:0 0 0.75rem;font-size:1.15rem;">Declaração de Acessibilidade Digital, LGPD/ECA e Direitos Autorais</h2>
          <ul class="check-list">
            <li><strong>Acessibilidade (eMAG 3.1 · WCAG 2.2 AA · ABNT NBR 17225):</strong> navegação por teclado (<span class="mono">Alt+1</span> a <span class="mono">Alt+5</span>), menus expansíveis acessíveis por teclado e leitor de tela, alto contraste persistente, ajuste de fonte, VLibras oficial e proteção sensorial sem reprodução automática.</li>
            <li><strong>LGPD e Estatuto da Criança e do Adolescente (ECA):</strong> nenhum registro audiovisual ou nome individualizado de discente é associado à condição socioeconômica (IVS) ou a atendimento educacional específico (NAPNE).</li>
            <li><strong>Direitos Autorais (Lei nº 9.610/1998):</strong> paródias didáticas do Aulão de Vestibular são incorporadas diretamente da transmissão oficial do IFSC (Art. 47); fonogramas comerciais de <em>covers</em> não são hospedados neste servidor.</li>
          </ul>
        </div>

""" + pager(("sinfonia-bncc.html", "Matriz BNCC &amp; 7 Encontros"), ("index.html", "Voltar ao Início")) + """
      </div>
    </section>"""

PAGES = [
    ("index.html", "Início", "Portal guarda-chuva do Programa Músico de Apoio, Banda RAC & Roll e Sinfonia da Permanência — IFSC Câmpus São José.", INDEX_BODY, ""),
    ("projeto.html", "Projetos · Músico de Apoio", "Programa guarda-chuva Músico de Apoio, metodologia PHC/PPE, Sala de Música e editais PROPPI/DAE.", PROJETO_BODY, ""),
    ("projeto-rac-and-roll.html", "Banda RAC & Roll", "Projeto musical Banda RAC & Roll organizado pelo Prof. Jorge Luiz Pereira no IFSC Câmpus São José.", RAC_BODY, ""),
    ("projetos-futuros.html", "Projetos Futuros · Ciclo 2027", "Roadmap de prospecção 2027: Caderno de Eco-Lutheria, Livro de Coletâneas Multimídia e expansão do Programa Músico de Apoio.", FUTUROS_BODY, ""),
    ("parcerias.html", "Parcerias & Captação 2027", "Vitrine institucional de parcerias e captação 2027 para o Programa Músico de Apoio: Ação 20RL, Ação 2994 (PNAES) e FEESC.", PARCERIAS_BODY, ""),
    ("oficinas.html", "Oficinas & Estúdio Digital", "Oficinas musicais cooperativas e Estúdio Digital (Metrônomo e Diapasão Web Audio) no IFSC São José.", OFICINAS_BODY, ""),
    ("eventos.html", "Eventos · Portfólio 2026", "Portfólio público 2026: SNCT/MCC, Aulão de Vestibular no YouTube Live e Feira de Jogos 2026.2.", EVENTOS_BODY, ""),
    ("eventos-2027.html", "Eventos · Agenda 2027", "Calendário previsto de eventos e apresentações culturais do Programa Músico de Apoio em 2027.", EVENTOS_2027_BODY, ""),
    ("tecnologia-social.html", "Tecnologia Social", "Manual de Implementação Músico de Apoio e replicabilidade na Rede Federal.", TS_BODY, ""),
    ("apostilas.html", "Apostilas & Materiais Didáticos", "Apostilas de bateria, violão (dedos-pivô) e acervo aberto do Programa Músico de Apoio.", APOSTILAS_BODY, ""),
    ("sinfonia-inovacao.html", "Sinfonia & Inovação · Calculadoras", "Parceria Sinfonia da Permanência (Fábio Henrique de Carvalho Bartelega) e Calculadoras Client-Side de Tubofones PVC e Domo Geodésico 2V.", SINFONIA_BODY, '  <script src="assets/js/calculadoras.js"></script>\n'),
    ("sinfonia-bncc.html", "Sinfonia & Inovação · Matriz BNCC", "Matriz Interdisciplinar BNCC (5 UCs / 11 habilidades) e Trilha dos 7 Encontros Formativos.", SINFONIA_BNCC_BODY, ""),
    ("equipe.html", "Equipe e Ética", "Equipe executora, parceria Sinfonia da Permanência, 6 ODS da ONU, acessibilidade e conformidade LGPD/ECA.", EQUIPE_BODY, ""),
]

generated_files = set()
for fname, title, desc, body, extra in PAGES:
    html = render_shell(fname, title, desc, body, extra)
    (OUT / fname).write_text(html, encoding="utf-8")
    generated_files.add(fname)
    print(f"GENERATED: {fname:<26} ({len(html):,} bytes)")

# Link integrity check across all 12 HTML pages
broken = []
for fname in sorted(generated_files):
    txt = (OUT / fname).read_text(encoding="utf-8")
    for href in re.findall(r'href="([^"]+)"', txt):
        if href.startswith(("http", "#", "mailto:")):
            continue
        target = OUT / href
        if not target.exists():
            broken.append((fname, href))
assert not broken, f"BROKEN LINKS: {broken}"
print(f"LINK CHECK OK: 100% of internal links valid across {len(generated_files)} pages!")
