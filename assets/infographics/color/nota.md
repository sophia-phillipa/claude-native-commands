# /color: descrição completa

Categoria: Ajustes e permissões. Tipo: comando embutido do Claude Code.

## O que faz
Muda a cor da barra de prompt desta sessão.

## Por que usar
Com várias sessões abertas lado a lado, a cor mostra de relance em qual você está: uma cor por projeto ou por tipo de tarefa.

## Como usar
Use /color com o nome da cor, ou /color default para voltar à cor padrão.

Parâmetros: <cor>, uma destas cores: red, blue, green, yellow, purple, orange, pink ou cyan. default, palavra fixa que volta à cor padrão.

## Quando usar
Quando você trabalha com duas ou mais sessões ao mesmo tempo, como uma de código e outra de revisão, e quer saber de relance qual é qual antes de digitar.

## Observação
Um nome fora da lista devolve as cores aceitas. Numa sessão que é colega de uma equipe de agentes, quem lidera a equipe define a cor e o comando recusa a troca.

## O que acontece no fluxo do prompt e do motor
1. Você digita /color.
2. A barra muda de cor.
3. A cor vale nesta sessão.
4. Você reconhece a sessão.

## Exemplos
- /color green: verde para a sessão de testes.
- /color red: vermelho para a sessão que mexe em produção, um alerta visual antes de digitar.
- /color default: volta à cor padrão.

## Comandos relacionados
- /doctor: Check-up da instalação.

## Armadilhas
- Vale só para esta sessão.

Documentação: https://code.claude.com/docs/en/commands#all-commands
