# /loop: descrição completa

Categoria: Automação. Tipo: skill embutida do Claude Code. Alias: /proactive.

## O que faz
Roda um prompt ou um comando de barra repetidamente, num intervalo fixo ou no ritmo que o Claude escolher.

## Por que usar
Bom para acompanhar algo que demora, como um deploy ou uma fila, sem você precisar pedir de novo a cada vez.

## Como usar
Use /loop [intervalo] [prompt].

Parâmetros:
- [intervalo]: opcional. Tempo entre as voltas, como 5m ou 1h. Sem intervalo, o Claude decide quando voltar.
- [prompt]: o pedido ou o comando de barra que vai se repetir.

## Quando usar
Para acompanhar algo que demora, como um deploy ou uma fila, sem pedir de novo a cada vez.

## Observação
Não serve para tarefas de uma vez só. Para parar um loop com intervalo, peça na conversa para cancelá-lo; um loop sem intervalo para com Esc, com a caixa de prompt vazia.
Serve para repetir dentro da sessão. As tarefas agendadas do Desktop são outro recurso.

## O que acontece no fluxo do prompt e do motor
1. Você digita /loop com o prompt.
2. O Claude roda o prompt.
3. O Claude espera o intervalo ou decide quando voltar.
4. O loop repete até você pedir para encerrar.
5. Você acompanha sem novo pedido.

## Exemplos
- /loop 10m confira se o deploy de staging terminou: repete a cada 10 minutos.
- /loop 1h rode os testes e me avise se algum falhar: repete o pedido de hora em hora. Comandos embutidos, como /usage, não rodam dentro do loop: chegam ao Claude como texto.
- /loop resuma em uma linha o que foi feito na sessão: sem intervalo, o Claude escolhe o ritmo.

## Comandos relacionados
- /usage: não roda no loop; chega como texto.

## Armadilhas
- Não serve para tarefa única.
- Com intervalo, peça para cancelar.
- Sem intervalo, Esc com a caixa vazia.

Documentação: https://code.claude.com/docs/en/scheduled-tasks
