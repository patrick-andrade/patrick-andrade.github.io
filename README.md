# patrick-andrade.github.io

Código-fonte do site público de Patrick Andrade, gerado com Quarto e publicado no GitHub Pages.

**URL:** <https://patrick-andrade.github.io>

**Remote:** `https://github.com/patrick-andrade/patrick-andrade.github.io.git`

## Objetivo

Organizar uma presença acadêmica e técnica sóbria: economia aplicada, políticas públicas e análise de dados reprodutível. O Início identifica o autor (Departamento de Economia, PUC-SP), aponta o trabalho em curso, um recorte de publicações e o contato. As demais páginas separam projetos, publicações, ensino e [guias](https://patrick-andrade.github.io/guias.html) curtos sobre o fluxo de trabalho no computador.

## Trabalhe nesta pasta

Esta pasta **é** a raiz do Git do site. Edite, rode `quarto render`, faça commit e `push` **aqui**.

Não rode `git init` na pasta agregadora `3-PRESENCA-DIGITAL`, que não é um repositório. O prefixo local `01-` existe só no disco, para ordem visual; o repositório no GitHub continua `patrick-andrade.github.io`.

## Publicar

No PowerShell, um comando por linha, nesta pasta:

```powershell
quarto render
git status
git add .
git commit -m "Mensagem clara do porquê."
git push
```

O Quarto grava o HTML em `docs/`. O GitHub Pages está configurado para servir `main` `/docs`. Confirme `docs/.nojekyll` após o render.

## Navegação pública

Início, Projetos, Publicações, Ensino, Guias.

Rascunhos internos ficam em `_rascunhos/` e não entram no menu nem na lista de renderização.
