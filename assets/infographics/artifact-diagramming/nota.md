# /artifact-diagramming: descrição completa

Categoria: Criação e referência. Tipo: skill embutida do Claude Code.

## O que faz
Uma skill sobre quando um desenho vale a pena e como fazê-lo em SVG: mostrar por onde os dados passam, quem conversa com quem e como duas opções diferem, legível em tema claro e escuro.

## Por que usar
Uma caixa escrita "cache" diz menos que o texto. A skill orienta o desenho a mostrar o caminho real de um pedido, e a desistir do diagrama quando uma frase explica mais rápido.

## Como usar
Digite /artifact-diagramming com o que precisa ser explicado. Ela serve de guia quando um artefato ou página precisa de um diagrama.

## Quando usar
Quando um texto sobre fluxo, arquitetura ou estados ficou difícil de seguir e um desenho mostraria o caminho de uma vez.

## Observação
Exige a versão 2.1.221 ou mais nova e artifacts disponíveis.

## O que acontece no fluxo do prompt e do motor
1. Você digita /artifact-diagramming com o que precisa ser explicado.
2. A skill confere se vale desenhar, ou se uma frase explica mais rápido.
3. O desenho mostra o caminho dos dados, quem conversa com quem ou a diferença entre duas opções.
4. O diagrama sai legível nos dois temas.

## Exemplos
- /artifact-diagramming fluxo de login com token de sessão: sequência de quem chama quem, passo a passo.
- /artifact-diagramming comparar fila simples e fila com tentativas: duas opções lado a lado, mostrando a diferença.
- /artifact-diagramming estados de um pedido de compra: diagrama de estados e transições.

## Comandos relacionados
- /design-sync: Enviar seu design system ao Claude Design. O card não cita outro comando; a ligação segue o critério E8 (mesma categoria).

## Armadilhas
- Caixa escrita só com o nome diz menos que o texto.
- Desenho quando uma frase explica mais rápido.

Documentação: https://code.claude.com/docs/en/commands#all-commands
