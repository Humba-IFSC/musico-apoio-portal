# 📌 Ponto de Parada — Portal Programa Músico de Apoio & Sinfonia da Permanência

**Última atualização válida:** 21/11/2026 (01h15)  
**Versão atual do site:** `v3.1` (Arquitetura Multipágina Guarda-Chuva com Menus Expansíveis + Créditos + Agente Dedicado)  
**Desenvolvido por:** Prof. Humberto Luz Oliveira — IFSC Câmpus São José  
**Diretório do portal:** `musico-apoio/site-2027/`

---

## 🤖 Agente Oficial para Continuar o Desenvolvimento

Para manter 100% do design gráfico (cores IFSC, tipografia Open Sans, acessibilidade eMAG/WCAG/TEA, menus expansíveis e estrutura multipágina) nas próximas sessões — seja para **adicionar** novos projetos/eventos/apostilas ou **remover/arquivar** páginas antigas — basta invocar o agente oficial já instalado no Antigravity:

- **Nome do Agente (Skill):** `maestro-web-musico-apoio` (**Agente Maestro Web**)
- **Arquivo da Skill (Antigravity):** `.agents/skills/maestro-web-musico-apoio/SKILL.md`
- **Espelho Portável (para o GitHub do site):** `musico-apoio/site-2027/AGENTE_MAESTRO_WEB.md`
- **Frase pronta para retomar em qualquer sessão futura:**
  > *"Zack, acione o agente **maestro-web-musico-apoio** e retome o **Ponto_de_Parada.md** do site Músico de Apoio."*

---

## ✅ Histórico do que foi Concluído na Última Sessão Válida (20–21/11/2026)

### 1. Evolução da Arquitetura e Design (v1.0 → v2.0 → v3.1)
- **Design System Oficial IFSC 2017** em `assets/css/style.css`: paleta oficial (`#32A041`, `#1F6E2A`, `#C8191E`), fonte **Open Sans** (+ `JetBrains Mono` para fórmulas), logomarca horizontal oficial do IFSC (`assets/img/ifsc-horizontal-cor.png` e `ifsc-horizontal-branco.png`), sem mascotes.
- **Acessibilidade Total (eMAG 3.1 · WCAG 2.2 AA · TEA/NAPNE):** barra no topo com `Alt+1` a `Alt+5`, controle de fonte (`A-`/`A`/`A+`), **Alto Contraste (WCAG AAA)** e **Conforto Sensorial** persistidos entre páginas (`localStorage`), widget **VLibras** e **zero autoplay** de áudio/vídeo.
- **Arquitetura Multipágina Guarda-Chuva (12 páginas HTML)** com **menus horizontais e submenus verticais expansíveis** (hover no desktop, botão `▾` para teclado/mobile, fechamento com `Esc` e destaque automático do item pai e da subpágina ativa):
  1. `index.html` — **Início** (Hero editorial + ilustração SVG do Domo 2V/ondas + 6 cards de entrada rápida).
  2. **Projetos ▾** *(Guarda-Chuva)*:
     - `projeto.html` — Músico de Apoio (Metodologia PHC/PPE, Sala de Música, Editais 12/2025 e 16/2026).
     - `projeto-rac-and-roll.html` — **Banda RAC & Roll** (iniciativa musical organizada pelo Prof. Jorge Luiz Pereira).
     - `projetos-futuros.html` — **Projetos Futuros · Ciclo 2027** (incubadora de novas iniciativas em planejamento — mantendo em sigilo projetos ainda não públicos).
  3. `oficinas.html` — **Oficinas** (participação no EMI + Estúdio Digital: Metrônomo e Diapasão Web Audio sob clique).
  4. **Eventos ▾**:
     - `eventos.html` — Portfólio 2026 (23ª SNCT/8ª MCC, Aulão de Vestibular no YouTube Live sob demanda e Feira de Jogos 2026.2 com repertório).
     - `eventos-2027.html` — Agenda & Eventos Previstos para 2027.
  5. **Tecnologia Social ▾**:
     - `tecnologia-social.html` — Manual de Implementação & Replicabilidade em 4 passos na Rede Federal.
     - `apostilas.html` — Apostilas Autorais (Bateria, Violão/Dedos-Pivô) e espaço para novas tecnologias compartilhadas.
  6. **Sinfonia & Inovação ▾**:
     - `sinfonia-inovacao.html` — Parceria *Sinfonia da Permanência* (**Fábio Henrique de Carvalho Bartelega**) + Calculadoras Client-Side (**Tubofones de PVC** com correção de Helmholtz e **Domo Geodésico 2V** com diagrama SVG dinâmico e impressão de plano de corte).
     - `sinfonia-bncc.html` — Matriz Interdisciplinar BNCC (5 UCs / 11 Habilidades) e Trilha dos 7 Encontros.
  7. `equipe.html` — **Equipe e Ética** (ficha técnica, 6 ODS da ONU, Declaração de Acessibilidade e conformidade LGPD/ECA/Lei 9.610/1998).

### 2. Ajustes Finais e Automatização Validados
- **Script gerador mestre preservado em `scripts/build_site.py`:** garante que qualquer inserção ou remoção no menu seja propagada de forma 100% sincronizada para todas as páginas, com verificador automático de links internos (`LINK CHECK OK`).
- **Créditos oficiais conferidos:**
  - `Prof. Humberto Luz Oliveira` (sem "Prof. Dr.") + crédito no rodapé de todas as 12 páginas: *"Desenvolvido por Prof. Humberto Luz Oliveira · IFSC Câmpus São José"*.
  - `Fábio Henrique de Carvalho Bartelega` creditado como especialista em Educação Ambiental e autor do projeto parceiro *Sinfonia da Permanência*.
  - `Prof. Jorge Luiz Pereira` creditado como Coordenador do Projeto Músico de Apoio-IFSC e organizador da Banda RAC & Roll.
- **Integridade validada:** 12/12 páginas com zero links quebrados, zero `autoplay`, zero strings sigilosas/desatualizadas e sintaxe JavaScript limpa (`node --check`).

---

## 📋 Próximos Passos Sugeridos (Backlog para Próximas Sessões)

- [ ] **Publicação Oficial (Deploy):** Criar repositório GitHub dedicado (ex.: `Humba-IFSC/musico-apoio-portal`) com o conteúdo de `musico-apoio/site-2027/` e conectar no **Cloudflare Pages** (custo zero, sem senha de acesso).
- [ ] **Galeria de Imagens Autorizadas:** Inserir fotos da Sala de Música, da Banda RAC & Roll e dos eventos (somente com TALE/autorização de imagem, respeitando LGPD/ECA).
- [ ] **Downloads de PDFs Públicos:** Adicionar na página `apostilas.html` e `tecnologia-social.html` os links de download das apostilas finais e do *Manual de Implementação* assim que revisados para difusão pública.
- [ ] **Expansão 2027:** Quando as novas iniciativas de 2027 deixarem de ser sigilosas, acionar o agente `maestro-web-musico-apoio` para criar as subpáginas dedicadas dentro do submenu **Projetos ▾** e atualizar a **Agenda 2027**.
- [ ] **Integração com o Portal Ensino IFSC:** Substituir ou redirecionar o antigo `musico-apoio/index.html` para o novo domínio público do Cloudflare Pages após a publicação.

