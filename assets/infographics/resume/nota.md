# /resume: descrição completa

Categoria: Contexto e memória. Tipo: comando embutido do Claude Code.

## O que faz
Retoma uma conversa anterior pelo ID ou pelo nome, ou abre o seletor de sessões, onde as que estão em segundo plano aparecem marcadas com bg. Se a sessão escolhida ainda estiver rodando, a conversa atual vai para o segundo plano e este terminal se conecta à que estava rodando.

## Por que usar
Retoma o trabalho do ponto em que parou, sem começar uma conversa nova do zero.

## Como usar
Digite /resume para abrir o seletor, ou acrescente o ID ou o nome da sessão. Com o prompt vazio, a seta para a esquerda volta à visão de agentes, que também lista a conversa que você deixou.

Parâmetro opcional: [session]. O ID ou o nome da conversa. Sem ele, abre o seletor de sessões.

## Quando usar
Quando quer voltar a uma conversa anterior, ou entrar numa sessão que continua rodando em segundo plano.

## Observação
Documentado na referência oficial. A documentação do Desktop descreve a lista de sessões da CLI; não vale para SSH, WSL ou nuvem.

## O que acontece no fluxo do prompt e do motor
1. Você digita /resume.
2. O seletor lista as sessões recentes.
3. O motor carrega a conversa escolhida.
4. O trabalho continua do ponto em que parou.

## Exemplos
- /resume: abre o seletor com as sessões recentes e as que estão em segundo plano.
- /resume refatoracao-login: retoma a conversa cujo nome é refatoracao-login.
- /continue 3f9a2c: mesmo comando pelo alias, retomando a sessão de ID 3f9a2c.

## Comandos relacionados
- /compact: resumir a conversa e liberar contexto.

## Armadilhas
- SSH, WSL e nuvem ficam de fora.

Documentação: https://code.claude.com/docs/en/agent-view
