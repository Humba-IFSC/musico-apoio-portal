# 📌 Ponto de Parada — Portal Programa Músico de Apoio & Sinfonia da Permanência

**Última atualização válida:** 22/11/2026 (20h47)  
**Versão atual do site:** `v3.2` (Arquitetura Multipágina Guarda-Chuva 13 páginas · Vitrine de Prospecção & Parcerias 2027 + Sala de Estratégia Interna em `musico-apoio/Prospectar/`)  
**Desenvolvido por:** Prof. Humberto Luz Oliveira — IFSC Câmpus São José  
**Diretório local do portal:** `musico-apoio/site-2027/`  
**Repositório GitHub (Público):** https://github.com/Humba-IFSC/musico-apoio-portal  
**Portal Online (Cloudflare Pages / Static Assets — Acesso Público sem Senha):** https://musico-apoio-ifsc-sje.hloliveira.workers.dev

---

## 🤖 Agente Oficial para Continuar o Desenvolvimento

Para manter 100% do design gráfico (cores IFSC, tipografia Open Sans, acessibilidade eMAG/WCAG/TEA, menus expansíveis e estrutura multipágina) nas próximas sessões — seja para **adicionar** novos projetos/eventos/apostilas ou **remover/arquivar** páginas antigas — basta invocar o agente oficial já instalado no Antigravity:

- **Nome do Agente (Skill):** `maestro-web-musico-apoio` (**Agente Maestro Web**)
- **Arquivo da Skill (Antigravity):** `.agents/skills/maestro-web-musico-apoio/SKILL.md`
- **Espelho Portável (para o GitHub do site):** `musico-apoio/site-2027/AGENTE_MAESTRO_WEB.md`
- **Frase pronta para retomar em qualquer sessão futura:**
  > *"Zack, acione o agente **maestro-web-musico-apoio** e retome o **Ponto_de_Parada.md** do site Músico de Apoio."*

---

## ✅ Histórico do que foi Concluído na Última Sessão Válida (22/11/2026 — Prospecção & Vitrine `v3.2`)

### 1. Sala de Estratégia Interna (`musico-apoio/Prospectar/` — Estritamente Local / Privado)
Criados os 3 documentos táticos de planejamento e captação (mantidos fora do site público e fora do GitHub público):
- `musico-apoio/Prospectar/PAUTA_REUNIAO_EQUIPE_2027.md` — Pauta de deliberação com a equipe (estudos semanais por instrumento, fechamento de 3 orçamentos por rubrica `20RL` GND 4/3 e `2994`/FEESC com previsão de taxa administrativa, e enquadramento jurídico do *Livro de Coletâneas Multimídia*).
- `musico-apoio/Prospectar/AGENDA_ACOES_2027.md` — Cronograma em 4 fases (Nov/2026 a Nov/2027) com estratégia federal (MDE/LDB), articulação estadual (ALESC) e empresas de São José.
- `musico-apoio/Prospectar/DOSSIE_EXECUTIVO_CAPTACAO_2027.pdf` — Dossiê de 2 páginas A4, 100% impessoal e apartidário, com entregas de 2026, rubricas de 2027, vias legais (MEC/IFSC, FEESC Lei nº 8.958/1994 e Res. CONSUP/IFSC nº 61/2016) e QR Code para `/parcerias`.

### 2. Vitrine Institucional Pública (`v3.2` — 13 Páginas HTML)
- **Nova página `parcerias.html` (*Parcerias & Captação 2027*):** adicionada ao submenu **Projetos ▾**, ao card da Home (`4 Subpáginas`), ao Hero e ao rodapé; apresenta provas de entrega 2026, 3 frentes de investimento 2027 vinculadas a MDE/LDB (`20RL` GND 4/3, `2994`/PNAES/FEESC) e caminhos legais de apoio de forma 100% impessoal.
- **Upgrade de `projetos-futuros.html`:** transformada em *Painel de Prospecção & Roadmap 2027* com selos de maturidade (`Em Desenvolvimento`, `Em Discussão com a Equipe`, `Em Captação`).
- **Upgrade de `apostilas.html`:** nova seção *"Estudos Semanais por Instrumento & Livro de Coletâneas Multimídia (Em Desenvolvimento · 2027)"* (Baixo Elétrico, Violão/Guitarra, Teclado e futuro E-book/MP3/MP4/PDF), sem citar nomes de discentes em definição.
- **Upgrade de `eventos-2027.html`:** inclusão do **Didascálico (Mostra de Arte e Cultura do IFSC — Novembro)** junto à 24ª SNCT/MCC 2027 como marcos de culminância e prestação de contas.
- **Design System (`assets/css/style.css`):** adição do modificador `.pill--amber` para selos de captação e metas.
- **Integridade validada (`v3.2`):** 13/13 páginas geradas via `scripts/build_site.py`, zero links quebrados, zero `autoplay`, zero strings partidárias/sigilosas/desatualizadas e crédito preservado em todas as páginas.
- **Atualização de Domínio Provisório (22/11/2026 — 20h22):** URL pública do Cloudflare Workers renomeada de `musico-apoio-ifsc.hloliveira.workers.dev` para `https://musico-apoio-ifsc-sje.hloliveira.workers.dev` (com descontinuação do worker antigo para evitar duplicidade) e regeneração do `DOSSIE_EXECUTIVO_CAPTACAO_2027.pdf` com link e QR Code atualizados.

---

### Histórico Anterior Consolidado (`v1.0 → v3.1`, 20–21/11/2026)
- **Design System Oficial IFSC 2017** em `assets/css/style.css`: paleta oficial (`#32A041`, `#1F6E2A`, `#C8191E`), fonte **Open Sans** (+ `JetBrains Mono` para fórmulas), logomarca horizontal oficial do IFSC (`assets/img/ifsc-horizontal-cor.png` e `ifsc-horizontal-branco.png`), sem mascotes.
- **Acessibilidade Total (eMAG 3.1 · WCAG 2.2 AA · TEA/NAPNE):** barra no topo com `Alt+1` a `Alt+5`, controle de fonte (`A-`/`A`/`A+`), **Alto Contraste (WCAG AAA)** e **Conforto Sensorial** persistidos entre páginas (`localStorage`), widget **VLibras** e **zero autoplay** de áudio/vídeo.
- **Arquitetura Multipágina Guarda-Chuva** com **menus horizontais e submenus verticais expansíveis**:
  1. `index.html` — **Início** (Hero editorial + ilustração SVG do Domo 2V/ondas + 6 cards de entrada rápida).
  2. **Projetos ▾** *(Guarda-Chuva)*: `projeto.html`, `projeto-rac-and-roll.html`, `projetos-futuros.html`, `parcerias.html`.
  3. `oficinas.html` — **Oficinas** (participação no EMI + Estúdio Digital: Metrônomo e Diapasão Web Audio sob clique).
  4. **Eventos ▾**: `eventos.html` (Portfólio 2026) e `eventos-2027.html` (Agenda 2027 com 24ª SNCT/MCC e Didascálico).
  5. **Tecnologia Social ▾**: `tecnologia-social.html` (Manual) e `apostilas.html` (Apostilas + Estudos Semanais 2027).
  6. **Sinfonia & Inovação ▾**: `sinfonia-inovacao.html` (Calculadoras Client-Side) e `sinfonia-bncc.html` (Matriz BNCC & 7 Encontros).
  7. `equipe.html` — **Equipe e Ética** (ficha técnica, 6 ODS da ONU, Declaração de Acessibilidade e conformidade LGPD/ECA/Lei 9.610/1998).
- **Créditos oficiais conferidos:** `Prof. Humberto Luz Oliveira` (sem "Prof. Dr.") + crédito no rodapé de todas as 13 páginas; `Fábio Henrique de Carvalho Bartelega`; `Prof. Jorge Luiz Pereira`.

---

## 📋 Próximos Passos Sugeridos (Backlog para Próximas Sessões)

- [x] **Publicação Oficial (Deploy):** Repositório GitHub público criado (`https://github.com/Humba-IFSC/musico-apoio-portal`) e publicado no Cloudflare (`https://musico-apoio-ifsc-sje.hloliveira.workers.dev`), 100% aberto e sem senha de acesso. ✅ CONCLUÍDO (21/11/2026; URL renomeada em 22/11/2026)
- [ ] **Galeria de Imagens Autorizadas:** Inserir fotos da Sala de Música, da Banda RAC & Roll e dos eventos (somente com TALE/autorização de imagem, respeitando LGPD/ECA).
- [ ] **Downloads de PDFs Públicos:** Adicionar na página `apostilas.html` e `tecnologia-social.html` os links de download das apostilas finais e do *Manual de Implementação* assim que revisados para difusão pública.
- [ ] **Expansão 2027:** Quando as novas iniciativas de 2027 deixarem de ser sigilosas, acionar o agente `maestro-web-musico-apoio` para criar as subpáginas dedicadas dentro do submenu **Projetos ▾** e atualizar a **Agenda 2027**.
- [ ] **Integração com o Portal Ensino IFSC:** Substituir ou redirecionar o antigo `musico-apoio/index.html` para o novo domínio público do portal após a publicação definitiva.
- [ ] **Subdomínio Institucional IFSC (`musicoapoio.sj.ifsc.edu.br`):** Protocolar alinhamento na DIRCOM e chamado técnico na DTIC (`chamados.ifsc.edu.br`) usando o roteiro abaixo, e atualizar o QR Code do Dossiê após a ativação.

---

## 🏛️ Roteiro para Solicitação de Subdomínio Institucional IFSC (DTIC / DIRCOM)

Para migrar futuramente do endereço provisório (`https://musico-apoio-ifsc-sje.hloliveira.workers.dev`) para um domínio oficial do instituto (sugestão: `musicoapoio.sj.ifsc.edu.br` ou `musicoapoio.ifsc.edu.br`), seguir as 4 etapas:

### 1. Alinhamento prévio no Câmpus São José
- Comunicar a Direção-Geral (ou Direção de Ensino/Pesquisa/Extensão) do câmpus sobre o pedido do subdomínio para o **Programa Músico de Apoio**, citando os Editais nº 12/2025 e nº 16/2026/PROPPI/DAE.
- Consultar previamente a Comunicação e a TI locais (CTIC) do câmpus para alinhar a abertura do chamado.

### 2. Validação do canal junto à Comunicação (DIRCOM)
- Pela Política de Comunicação do IFSC, novos sites e subdomínios de projetos passam pela análise da DIRCOM (identidade visual, objetivos institucionais, acessibilidade e servidores responsáveis).
- Enviar consulta/validação para `suporte.comunicacao@ifsc.edu.br` (ou via comunicação do câmpus) com o link da prévia atual (`https://musico-apoio-ifsc-sje.hloliveira.workers.dev`), destacando a conformidade integral com o **Manual da Marca IFSC 2017**, acessibilidade **eMAG 3.1 / WCAG 2.2 AA + VLibras** e **LGPD/ECA**.

### 3. Abertura de chamado técnico na DTIC
- Acessar **https://chamados.ifsc.edu.br** com as credenciais da Intranet e abrir chamado direcionado à **DTIC — Infraestrutura / Redes / Hospedagem de Portais** (contato institucional: `dtic@ifsc.edu.br`).
- Deixar abertas as duas opções técnicas compatíveis com a política da DTIC:
  - **Opção A — Hospedagem estática nos servidores do IFSC:** site 100% estático (HTML5, CSS3, JS puro e PNGs, sem banco de dados ou backend PHP), sem risco de segurança de servidor.
  - **Opção B — Apontamento DNS (`CNAME`):** criação de registro `CNAME` de `musicoapoio.sj.ifsc.edu.br` para hospedagem externa aprovada (Cloudflare / GitHub Pages, com *Custom Domain* e HTTPS automático).

### 4. Configuração final após a aprovação
- **Se hospedagem interna no IFSC:** fornecer o pacote estático gerado em `musico-apoio/site-2027/` (ou o repositório público `https://github.com/Humba-IFSC/musico-apoio-portal`).
- **Se apontamento `CNAME`:** vincular o domínio institucional nas configurações da hospedagem e acionar o agente `maestro-web-musico-apoio` para atualizar URLs, documentação e o QR Code do Dossiê Executivo.

### Modelo Pronto de Texto para o Chamado (`chamados.ifsc.edu.br`)

> **Assunto:** Solicitação de subdomínio institucional (`musicoapoio.sj.ifsc.edu.br`) — Projeto Músico de Apoio (Câmpus São José)
>
> Prezados(as),
>
> Solicito a criação do subdomínio institucional **`musicoapoio.sj.ifsc.edu.br`** (ou alternativa padrão recomendada pela DTIC/DIRCOM) para publicação do portal do **Programa Músico de Apoio & Sinfonia da Permanência**, projeto de extensão e pesquisa do **IFSC Câmpus São José** (Editais nº 12/2025 e nº 16/2026/PROPPI/DAE).
>
> - **Prévia atual para avaliação:** https://musico-apoio-ifsc-sje.hloliveira.workers.dev
> - **Repositório público (código-fonte):** https://github.com/Humba-IFSC/musico-apoio-portal
> - **Arquitetura técnica:** site 100% estático (HTML5, CSS3 e JavaScript puro — sem banco de dados, sem backend e sem coleta de dados pessoais).
> - **Conformidade institucional:** Manual da Marca IFSC 2017, diretrizes de acessibilidade eMAG 3.1 / WCAG 2.2 AA (Alto Contraste, atalhos eMAG, modo Conforto Sensorial TEA e VLibras) e conformidade LGPD/ECA.
> - **Servidores responsáveis pela manutenção:** Prof. Humberto Luz Oliveira (desenvolvimento e atualização técnica) e Prof. Jorge Luiz Pereira (coordenação do projeto — Câmpus São José).
>
> Fico à disposição para seguir o modelo recomendado pela DTIC — seja via **hospedagem estática nos servidores do IFSC** ou via **apontamento DNS (`CNAME`)** — bem como para eventuais ajustes solicitados pela DIRCOM.
>
> Atenciosamente,  
> **Prof. Humberto Luz Oliveira**  
> IFSC — Câmpus São José

