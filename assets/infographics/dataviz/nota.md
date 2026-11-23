# /dataviz: descrição completa

Categoria: Criação e referência. Tipo: skill embutida do Claude Code.

## O que faz
Uma skill de visualização de dados: guia a escolha do tipo de gráfico, das cores e do layout de painéis, valendo para qualquer saída, seja página HTML, SVG, código de plot ou imagem.

## Por que usar
Gráficos feitos "no olho" saem com cores sem relação, legendas confusas e contraste ruim. A skill dá um método e uma paleta validada, e funciona em tema claro e escuro.

## Como usar
Digite /dataviz com o que você quer mostrar. Ela é lida antes de escrever qualquer código de gráfico, de cartão de indicador ou de painel.

## Quando usar
Antes de montar um gráfico, um cartão de indicadores ou um painel, para que cores, legendas e tema fiquem coerentes.

## O que acontece no fluxo do prompt e do motor
1. Você digita /dataviz com o que quer mostrar.
2. A skill é lida antes de qualquer código de gráfico.
3. Ela guia o tipo, as cores e o layout.
4. O código do gráfico é escrito.
5. A saída sai com cores coerentes.

## Exemplos
- /dataviz vendas por mês em 2026 em um gráfico de linha: gráfico simples com eixo e legenda claros.
- /dataviz painel com 4 indicadores e um gráfico de barras por região: layout de painel consistente.
- /dataviz refaça esse gráfico do matplotlib com cores acessíveis: revisão de um gráfico existente.

## Comandos relacionados
- /design-sync: Enviar seu design system ao Claude Design. O card não cita outro comando; a ligação segue o critério E8 (mesma categoria).

## Armadilhas
- Cores sem relação entre si.
- Legendas confusas e contraste ruim.

Documentação: https://code.claude.com/docs/en/commands#all-commands
