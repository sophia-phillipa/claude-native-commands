# /plugin: descrição completa

Categoria: Extensões e conexões. Tipo: comando embutido do Claude Code.

## O que faz
Gerencia os plugins do Claude Code. Sem argumento, abre o menu de plugins; com list, install, enable ou disable, executa a ação direto.

## Por que usar
Reúne num só lugar a instalação, a ativação e a listagem dos plugins.

## Como usar
Rode /plugin para abrir o menu, ou /plugin list para ver os instalados. Se o resumo da instalação pedir, rode /reload-plugins. Aliases: /plugins e /marketplace.

Parâmetro opcional: [subcommand]. Por exemplo list, install, enable ou disable.

## Quando usar
Quando você quer instalar, ativar ou listar extensões do Claude Code sem sair do terminal.

## Observação
Gerenciamento de plugins documentado na página de plugins. Testado no app: funcionou.

## O que acontece no fluxo do prompt e do motor
1. Você digita /plugin com ação.
2. O motor executa a ação.
3. O motor informa o estado.
4. Plugin fica no estado pedido.

## Exemplos
- /plugin list: lista os plugins instalados.
- /plugin install formatador: instala o plugin formatador e informa se ele já está ativo.
- /plugin disable formatador: desativa o plugin com um comando direto.

## Comandos relacionados
- /reload-plugins: ativa plugins sem abrir outra sessão.

## Armadilhas
- Instalação pode pedir /reload-plugins.

Documentação: https://code.claude.com/docs/en/plugins/overview
