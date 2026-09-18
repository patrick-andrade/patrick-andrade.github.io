# Changelog

Todas as mudanças relevantes dos guias publicados neste repositório são registradas neste arquivo.

A fonte canônica dos guias é `guias/` neste site. Não há segunda cópia de edição fora deste repositório.

## [Unreleased]

### Changed

- *Codex na Prática* 0.5.0 (página 1.1.0): leitura de cerca de 3 minutos para quem vem do ChatGPT no navegador. Projects como pasta no desktop; some a tabela de framework, o bloco Git e o jargão de sandbox.
- *Git e GitHub na Prática* 0.4.0: o Git local vem primeiro; GitHub é opcional. O ganho para quem usa agente é ver o diff, voltar atrás e pedir o commit sem publicar. Sai o receituário de `push` e `gh repo create` como caminho principal. O arquivo da guia passa a ser `git-na-pratica.qmd`.
- *Quarto na Prática* 0.6.0: abertura para quem vem do Microsoft 365; Quarto Markdown como o arquivo em que texto e conta convivem; o ganho está em repetir o fluxo com um agente de IA. R, Python e GitHub Pages ficam no mínimo.
- *Quarto na Prática* 0.5.0: o `.qmd` como ferramenta de análise e publicação (R ou Python; Word, PDF, HTML). Público de quem trabalha em Excel, Word e PowerPoint. GitHub Pages vira menção opcional. O arquivo da guia passa a ser `quarto-na-pratica.qmd`.

## Revisão editorial de 17 de setembro de 2026

### Changed

- As cinco guias foram reescritas em tom didático e direto: dizem o que a ferramenta é, sem encenar complexidade.
- Sai a linha de revisão das fontes. Callout fica só quando o risco é concreto (segredo no histórico).
- YAML e exemplos de arquivo só ilustram; o texto de Skills diz que um bom agente monta o `SKILL.md`.
- *GitHub na Prática* 0.3.0 abre por Git local e remoto, e deixa o aviso de backup em prosa.
- *Quarto e GitHub Pages* 0.3.0 reduz o `_quarto.yml` às linhas que importam e tira o fecho das quatro camadas.
- *Codex na Prática* 0.4.0 troca o objetivo abstrato pelo menor contexto que ainda dá para revisar.
- *Skills na Prática* 0.3.0 abre pelo que a pasta é: um prompt versionado, com nome, a um comando de distância.
- *Por que o Codex ainda importa* 0.3.0 datou o registro em prosa e conclui pela escolha da ferramenta pelo requisito.
- O índice de guias e a prosa institucional passaram pelo humanizer: mesmos fatos, menos hábito de texto de modelo.

## Revisão editorial de 28 de agosto de 2026

### Changed

- Os quatro guias rápidos foram reescritos segundo o contrato editorial: problema, premissas, mecanismo, aplicação, resultado, limites e fontes.
- O índice agora distingue quatro guias rápidos de um estudo de caso.
- *GitHub na Prática* 0.2.0 deixa de tratar o remoto como backup completo e incorpora um portão público × interno.
- *Quarto e GitHub Pages* 0.2.0 delimita a opção `main`/`docs`, separa fonte, artefato e publicação e esclarece que não renderizar não torna um arquivo privado.
- *Codex na Prática* 0.3.0 incorpora Projects, precedência de `AGENTS.md`, trabalho longo, sandbox e verificação do diff.
- *Skills na Prática* 0.2.0 retém apenas o uso prático atual: anatomia, divulgação progressiva, descoberta, invocação, testes e manutenção.
- *Por que o Codex ainda importa* 0.2.0 passa a ser explicitamente um estudo de caso datado e substitui afirmações de produto obsoletas por documentação atual do Codex e do Cursor.

## Por que o Codex ainda importa

### [0.1.0] - 2026-08-23

### Added

- Guia didático (cerca de 12 minutos): modelo versus harness; tarefa conceitual em uma plataforma que restringe agentes; três superfícies de interação; post-mortem datado da tentativa no Cursor e comparação com o Codex.
- Callouts `important` (instantâneo de agosto de 2026), `note`, `tip` e `caution`. Sem nome de plataforma, URLs, seletores ou receita de automação.
- Ligação no índice de Guias, em `_quarto.yml`, em `VERSION` e no fim de *Codex na Prática*.

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
