# /simplify: descrição completa

Categoria: Revisão de código. Tipo: skill embutida do Claude Code.

## O que faz
Revisa o código alterado procurando reuso, simplificação, eficiência e o nível certo de abstração, e aplica as correções.

## Por que usar
Deixa o diff menor e mais legível antes do commit. Não procura bugs: para isso existe o /code-review.

## Como usar
Rode /simplify sem parâmetros, com mudanças no working tree.

## Quando usar
Depois que a funcionalidade já funciona e os testes passam, antes do commit: é a hora de enxugar sem mudar o comportamento.

## O que acontece no fluxo do prompt e do motor
1. Você digita /simplify.
2. O motor lê o código.
3. Quatro agentes revisam em paralelo.
4. O motor aplica as correções.
5. Diff fica menor e legível.

## Exemplos
- /simplify: limpa o diff atual e aplica as melhorias.
- /code-review high: primeiro passo da dupla, caça bugs.
- /simplify: segundo passo, enxuga o que sobrou. Envie um comando por vez.

## Comandos relacionados
- /code-review: caça bugs que ele não procura.

## Armadilhas
- Não procura bugs de correção.

Documentação: https://code.claude.com/docs/en/commands#all-commands
