Configurando o ambiente de desenvolvimento:

```bash
poetry new <name>
cd ./<name>
git init . 
gh repo create
touch .gitignore
git add .
git commit -m "Commit inicial com a estrutura básica do projeto"
git remote add origin <link>.git
git branch -M main
git push -u origin main
poetry add --group dev pytest
poetry add --group dev pytest-cov
poetry add --group dev blue
poetry add --group dev isort
poetry add --group doc mkdocs-material
poetry add --group doc mkdocstrings
poetry add --group dev takipy
 ```


Configurando o mkdocs:

```bash
poetry shell
mkdocs new .

```
