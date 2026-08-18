# Changelog

Todas as mudanças relevantes dos guias publicados neste repositório são registradas neste arquivo.

A fonte canônica dos guias é `guias/` neste site. Não há segunda cópia de edição em `0-CONFIG-GERAL/00-guias`.

## [Unreleased]

### Changed

- Os guias passaram a viver em `guias/` no repositório `patrick-andrade.github.io`.
- O guia de GitHub deixa explícito que `0-CONFIG-GERAL` é o toolkit, não a casa dos guias.
- Correção de digitação no Codex: “Este guia mostra que o salto…”.
- Listas Markdown dos três guias passam a ter linha em branco antes dos bullets, para o Pandoc renderizar como lista e não como continuação do parágrafo.
- Prosa dos três guias alinhada ao tom do site: português direto, segunda pessoa, sem anúncio de seção nem ênfase genérica.

### Added

- Guia *Quarto e GitHub Pages* (0.1.0), no mesmo ritmo de 5 minutos + Saiba mais.

## GitHub na Prática

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
