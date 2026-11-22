# Portal Programa Músico de Apoio & Sinfonia da Permanência (IFSC Câmpus São José)

Portal institucional **multipágina e expansível (v3.2)** concebido como **guarda-chuva** para o **Projeto Músico de Apoio**, iniciativas artísticas do câmpus (como a **Banda RAC & Roll**), parcerias interdisciplinares (**Sinfonia da Permanência**), vitrine de **Parcerias & Captação 2027** e futuras ações de pesquisa, ensino e extensão (Editais nº 12/2025 e nº 16/2026/PROPPI/DAE).

## Arquitetura Multipágina com Menus Expansíveis (13 Páginas · JAMstack Puro)
- `index.html`: **Início** — visão executiva, indicadores e acesso rápido aos hubs do portal.
- **Projetos ▾**
  - `projeto.html`: Programa Guarda-Chuva, Metodologia PHC/PPE, Sala de Música e Editais.
  - `projeto-rac-and-roll.html`: **Banda RAC & Roll** (iniciativa musical organizada pelo Prof. Jorge Luiz Pereira).
  - `projetos-futuros.html`: Roadmap de Prospecção 2027 (Caderno de Eco-Lutheria, Livro de Coletâneas Multimídia e expansões).
  - `parcerias.html`: **Parcerias & Captação 2027** (enquadramento MDE/LDB, Ações 20RL e 2994, FEESC e Empresas de São José).
- `oficinas.html`: **Oficinas** — participação no EMI e Estúdio Digital (Metrônomo + Diapasão Web Audio sem autoplay).
- **Eventos ▾**
  - `eventos.html`: Portfólio 2026 (23ª SNCT/8ª MCC, Aulão de Vestibular Live e Feira de Jogos 2026.2).
  - `eventos-2027.html`: Agenda & Eventos Previstos para o Ciclo 2027 (incluindo 24ª SNCT e Didascálico).
- **Tecnologia Social ▾**
  - `tecnologia-social.html`: Manual de Implementação e Replicabilidade na Rede Federal.
  - `apostilas.html`: Apostilas Autorais (Bateria, Violão/Dedos-Pivô), Estudos Semanais 2027 e futuro Livro de Coletâneas Multimídia.
- **Sinfonia & Inovação ▾**
  - `sinfonia-inovacao.html`: Parceria *Sinfonia da Permanência* (Fábio Henrique de Carvalho Bartelega) e Calculadoras Client-Side (Tubofones de PVC + Domo Geodésico 2V).
  - `sinfonia-bncc.html`: Matriz Interdisciplinar BNCC (5 UCs / 11 Habilidades) e Trilha dos 7 Encontros.
- `equipe.html`: **Equipe e Ética** — ficha técnica, 6 ODS da ONU, acessibilidade eMAG/WCAG/TEA e conformidade LGPD/ECA.

## Links Oficiais Publicados
- **Portal Online (Cloudflare — Acesso Público sem Senha):** https://musico-apoio-ifsc-sje.hloliveira.workers.dev
- **Repositório GitHub (Público):** https://github.com/Humba-IFSC/musico-apoio-portal

## Como Atualizar e Publicar (Cloudflare CLI)
1. Após editar via `scripts/build_site.py`, faça commit e push na branch `main`.
2. Dentro da pasta do site, execute `wrangler deploy` para atualizar os arquivos estáticos em segundos (ou conecte o repositório diretamente no painel Cloudflare Pages/Workers Builds para deploy automático a cada `git push`).
