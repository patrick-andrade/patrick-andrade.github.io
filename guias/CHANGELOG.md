# Changelog

Todas as mudanças relevantes dos guias publicados neste repositório são registradas neste arquivo.

A fonte canônica dos guias é `guias/` neste site. Não há segunda cópia de edição fora deste repositório.

## [Unreleased]

### Changed

- O índice de Guias troca o cabeçalho "O que o salto organiza" por "O que o guia resolve".
- Referências a estruturas locais do autor (pasta agregadora e toolkit) saem dos guias; os pré-requisitos passam a ser declarados de forma neutra (ferramentas instaladas e no PATH).

- Os guias passaram a viver em `guias/` no repositório `patrick-andrade.github.io`.
- O guia de GitHub deixa explícito que `0-CONFIG-GERAL` é o toolkit, não a casa dos guias.
- Correção de digitação no Codex: “Este guia mostra que o salto…”.
- Listas Markdown dos três guias passam a ter linha em branco antes dos bullets, para o Pandoc renderizar como lista e não como continuação do parágrafo.
- Prosa dos três guias alinhada ao tom do site: português direto, segunda pessoa, sem anúncio de seção nem ênfase genérica.

### Added

- Guia *Quarto e GitHub Pages* (0.1.0), no mesmo ritmo de 5 minutos + Saiba mais.
- Guia *Skills na Prática* (0.1.0).

## Skills na Prática

### [0.1.2] - 2026-08-20

### Changed

- Prosa da introdução e das seções: tira abertura formulaica, metáfora do salto e travessões; mantém tabelas, callouts e os blocos Recomendação / Por que / ganhos / Na prática.

### [0.1.1] - 2026-08-19

### Changed

- Sai a subseção sobre o toolkit local (6.3); Fontes oficiais passa a ser 6.3.

### [0.1.0] - 2026-08-18

### Added

- Guia introdutório de cerca de 5 minutos: o que é uma skill em IA;
  diferença entre skill e `AGENTS.md`; criar, instalar e pedir a ficha;
  Codex como ponto de partida, com menção a Claude Code e Cursor.
- Callouts em tom de dica (tip) e nota (note).
- Seção Saiba mais, opcional, com divulgação progressiva, caminhos por
  aplicativo e ligações à especificação Agent Skills, ao humanizer e à
  skill [aula-academica](https://github.com/patrick-andrade/aula-academica).

## GitHub na Prática

### [0.1.3] - 2026-08-20

### Changed

- Prosa da introdução e da `description`: tira a metáfora do salto e os travessões; mantém comandos, callouts e a estrutura pedagógica.

### [0.1.2] - 2026-08-19

### Changed

- O callout sobre pasta agregadora deixa de citar a estrutura local do autor e vira regra geral (não rodar `git init` em pasta agregadora).
- Pré-requisitos declarados de forma neutra: `git` e `gh` instalados e no PATH, sem menção ao toolkit.

### [0.1.1] - 2026-08-18

### Changed

- Listas Markdown passam a ter linha em branco antes dos bullets, para o Pandoc renderizar como lista.
- Prosa alinhada ao tom do site.

### [0.1.0] - 2026-08-18

### Added

- Guia introdutório de cerca de 5 minutos: Git versus GitHub, benefícios do
  remoto, GitHub Pro pelo Student Pack e comandos no Windows PowerShell 5.1
  (`init`, `add`, `commit`, `pull`, `push`, `clone`, `status`, `gh auth login`).
- Seção Saiba mais, opcional, com `.gitignore`, `fetch` versus `pull`,
  `gh repo create`, identidade do commit e pastas no OneDrive.

## Quarto e GitHub Pages

### [0.1.4] - 2026-08-20

### Changed

- Prosa da introdução e da `description`: tira a metáfora do salto e os travessões; o id `{#o-salto-pasta-versionada-e-site-estatico}` permanece.

### [0.1.3] - 2026-08-19

### Changed

- Pré-requisitos declarados de forma neutra: `git` e `quarto` instalados e no PATH, sem menção ao toolkit.

### [0.1.2] - 2026-08-18

### Changed

- O guia registra *Skills na Prática* (e *Codex na Prática*) na pasta `guias/` e em Fontes oficiais, no mesmo ritmo dos demais guias do site.

### [0.1.1] - 2026-08-18

### Changed

- Listas Markdown passam a ter linha em branco antes dos bullets, para o Pandoc renderizar como lista.
- Prosa alinhada ao tom do site.

### [0.1.0] - 2026-08-18

### Added

- Núcleo de cerca de 5 minutos: pasta versionada e site estático; repositório
  `usuario.github.io` no GitHub; `_quarto.yml` com `output-dir: docs`; fluxo
  `preview` → `render` → commit na raiz do Git → `push` → Pages em `main` `/docs`.
- Roteiro de primeira sessão em cinco passos.
- Seção Saiba mais, opcional, com persona Adam Smith e esqueleto das páginas,
  `.nojekyll` e `styles.css`, erros comuns e fluxo depois da publicação.

## Codex na Prática

### [0.2.3] - 2026-08-20

### Changed

- Prosa da introdução e da `description`: tira a abertura formulaica, a metáfora do salto e os travessões; mantém figura, Plan mode e os blocos Recomendação / Por que / ganhos / Na prática.

### [0.2.2] - 2026-08-18

### Changed

- Listas Markdown passam a ter linha em branco antes dos bullets, para o Pandoc renderizar como lista.
- Rótulos **Recomendação**, **Por que / ganhos** e **Na prática** uniformizados, sem dois-pontos nem ponto colado na prosa.
- Prosa alinhada ao tom do site.

### [0.2.1] - 2026-08-14

### Added

- Figura do aplicativo ChatGPT para Windows no modo Codex, com pastas de
  projeto na barra lateral, para ilustrar o salto do chat no navegador para
  a pasta local.

### [0.2.0] - 2026-08-14

### Added

- Núcleo de cerca de 5 minutos para quem vem do chat no navegador: projeto
  local em vez de upload e download, Plan mode como hábito, spec gravada no
  disco, escolha de modelo e esforço por tarefa, chats por resultado e
  controle por permissões.
- Roteiro de primeira sessão em cinco passos e pedido-modelo com atualização
  de `plano.md`.
- Seção Saiba mais, opcional, com Goal mode, detalhes de `AGENTS.md` e PDFs
  extensos.

### Changed

- O guia deixa de ser uma leitura contínua de cerca de 30 minutos e passa a
  ter duas camadas: o essencial para começar e o aprofundamento quando o uso
  já estiver andando.

### [0.1.0] - 2026-08-13

### Added

- Guia introdutório de leitura para o aplicativo desktop.
- Explicações sobre projetos locais, pedidos estruturados, Plan mode, organização
  de chats, `AGENTS.md`, Goal mode, revisão, privacidade e PDFs extensos.
- Links de aprofundamento para a documentação oficial da OpenAI.

### Changed

- O conteúdo principal passou de `README.md` para `codex-na-pratica.qmd`, com
  renderização HTML pelo Quarto e tema Cosmo.
