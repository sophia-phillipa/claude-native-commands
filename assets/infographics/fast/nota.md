# /fast: descrição completa

Categoria: Modelo e potência. Tipo: comando embutido do Claude Code.

## O que faz
Liga ou desliga o modo rápido, que acelera a saída do modelo da sessão quando ele suporta.

## Por que usar
Útil quando você quer respostas mais ligeiras numa sequência de ajustes pequenos.

## Como usar
Use /fast para alternar, ou diga on ou off.

Parâmetro: on · off, opcional. Liga ou desliga. Sem parâmetro, alterna o estado atual.

## Quando usar
Numa sequência de ajustes pequenos e rápidos, em que esperar a resposta pesa mais que a profundidade dela.

## Observação
Se o modelo atual não suporta o modo rápido, ligá-lo troca o modelo; na API da Anthropic, a sessão passa para o Opus.

## O que acontece no fluxo do prompt e do motor
1. Você digita /fast para alternar.
2. O motor alterna o modo.
3. Acelera a saída do modelo.
4. Respostas saem mais rápidas.

## Exemplos
- /fast: alterna o modo rápido.
- /fast on: liga para uma rodada de ajustes pequenos.
- /fast off: desliga e volta ao ritmo normal.

## Comandos relacionados
- /model: trocar o modelo da sessão.

## Armadilhas
- Modelo sem suporte: sessão muda de modelo.
- Custa mais por token.

Documentação: https://code.claude.com/docs/en/fast-mode#toggle-fast-mode
