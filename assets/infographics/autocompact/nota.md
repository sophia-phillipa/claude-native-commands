# /autocompact: descrição completa

Categoria: Contexto e memória. Tipo: comando embutido do Claude Code.

## O que faz
Define em que tamanho de contexto a compactação automática entra, ou devolve essa escolha ao Claude Code.

## Por que usar
O ponto padrão pode compactar cedo demais, cortando detalhes, ou tarde demais, deixando a sessão lenta e cara.

## Como usar
Use /autocompact com um número de tokens ou com auto.

Parâmetros:
- <tokens>: número de tokens em que a compactação automática entra, como 300000.
- auto: devolve o tamanho ao ajuste automático do Claude Code.

## Quando usar
Quando a compactação automática chega cedo ou tarde demais para o seu jeito de trabalhar, ou quando outra ferramenta já compacta a sessão e você quer que o Claude Code compacte antes dela.

## Observação
Escolha um valor com folga abaixo do tamanho da janela do modelo. Se a variável CLAUDE_CODE_AUTO_COMPACT_WINDOW estiver definida, ela tem prioridade sobre o comando, a flag e a configuração autoCompactWindow, a não ser que o Claude Code ignore o valor.

## O que acontece no fluxo do prompt e do motor
1. Você digita /autocompact com valor
2. O valor define a janela
3. A compactação entra nesse tamanho
4. Sessão compacta antes do fim

## Exemplos
- /autocompact 300000: compacta quando o contexto chega a 300 mil tokens, sem passar do limite de contexto do modelo.
- /autocompact 200000: sessões mais leves, para quem compacta com frequência.
- /autocompact auto: volta ao ajuste automático.

## Comandos relacionados
- /compact: resumir a conversa e liberar contexto.

## Armadilhas
- Valor sem folga abaixo da janela.
- Tarde demais deixa a sessão cara.

Documentação: https://code.claude.com/docs/en/model-config#set-the-auto-compact-window
