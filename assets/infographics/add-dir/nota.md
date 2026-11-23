# /add-dir: descrição completa

Categoria: Ajustes e permissões. Tipo: comando embutido do Claude Code.

## O que faz
Adiciona uma pasta ao conjunto de diretórios de trabalho da sessão, para o Claude ler e editar arquivos fora da pasta onde você abriu.

## Por que usar
Projetos reais se espalham por pastas: uma biblioteca ao lado do app, um repositório de documentação. Adicionar a pasta evita copiar arquivos ou reabrir a sessão.

## Como usar
Rode /add-dir seguido do caminho da pasta.

Parâmetro: <path>. O caminho da pasta a adicionar.

## Quando usar
Quando a tarefa atravessa pastas, como um app e a biblioteca ao lado, e o Claude precisa ler ou editar nas duas.

## Observação
No Desktop, a tela "Add folders to a session" faz o mesmo.

## O que acontece no fluxo do prompt e do motor
1. Você digita /add-dir.
2. A sessão ganha a pasta.
3. Claude lê e edita nela.

## Exemplos
- /add-dir ../minha-biblioteca: inclui a biblioteca vizinha ao app.
- /add-dir ~/projetos/docs: inclui um repositório de documentação.
- /add-dir /srv/config-compartilhada: inclui uma pasta de configuração usada por vários projetos.

## Comandos relacionados
- /config: mudar uma configuração pelo nome.

## Armadilhas
- Maior parte de .claude/ não é carregada.

Documentação: https://code.claude.com/docs/en/permissions#additional-directories-grant-file-access-not-configuration
