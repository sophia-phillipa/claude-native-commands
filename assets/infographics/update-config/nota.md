# /update-config: descrição completa

Categoria: Ajustes e permissões. Tipo: skill embutida do Claude Code.

## O que faz
Uma skill que edita o settings.json do Claude Code por você. Você descreve o que quer, como "permitir npm" ou "sempre que eu terminar, mostre X", e ela escolhe o arquivo certo e escreve a configuração.

## Por que usar
Comportamentos automáticos ("sempre que…") só funcionam como hook no settings.json: é o programa que executa, não a memória do Claude. Esta skill sabe onde cada coisa vai e evita você errar o formato.

## Como usar
Digite /update-config seguido do que você quer mudar, ou apenas descreva o pedido na conversa. Ela cobre permissões, variáveis de ambiente e hooks, e ajuda a depurar um hook que não dispara.

## Quando usar
Quando você quer que algo aconteça sempre ("depois de cada resposta, rode o formatador") ou parar de aprovar o mesmo comando, e prefere dizer em palavras a editar o arquivo.

## Observação
Para ajustes simples como tema e modelo, o /config é mais direto. A skill é para o que exige editar o arquivo.

## O que acontece no fluxo do prompt e do motor
1. Você descreve a mudança.
2. Claude acha o arquivo certo.
3. Claude grava a configuração.
4. A mudança fica no settings.json.

## Exemplos
- /update-config permitir os comandos npm test e npm run lint sem perguntar: cria a regra de permissão no arquivo de configuração certo.
- /update-config definir a variável DEBUG=true para todos os projetos: grava a variável de ambiente nas configurações.
- /update-config quando o Claude terminar, rodar o formatador do projeto: monta um hook de fim de resposta.

## Comandos relacionados
- /config: ajustes simples como tema e modelo.

## Armadilhas
- Tema e modelo vão no /config.

Documentação: https://code.claude.com/docs/en/commands#all-commands
