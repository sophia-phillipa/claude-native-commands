# /effort: descrição completa

Categoria: Modelo e potência. Tipo: comando embutido do Claude Code.

## O que faz
Define quanto o modelo pensa em cada resposta.

## Por que usar
Esforço baixo é mais rápido e barato para tarefas simples. Esforço alto ajuda em problemas difíceis. Combina com o /usage.

## Como usar
Use /effort <nível>.

Parâmetros:
- low · medium · high: do mais rápido e barato ao mais cuidadoso.
- xhigh · max: os mais caros. O app só aceita os que o modelo atual suporta.
- auto: devolve a escolha do esforço ao Claude.

## Quando usar
Quando o tipo de tarefa muda no meio da sessão: abaixe para ajustes mecânicos de texto e arquivos, suba ao chegar num bug difícil.

## Observação
xhigh e max consomem bem mais tokens. Use-os em tarefas curtas e difíceis, não na sessão inteira.

## O que acontece no fluxo do prompt e do motor
1. Você digita /effort com nível.
2. O motor define o nível.
3. Cada resposta usa esse esforço.
4. Modelo pensa no nível escolhido.

## Exemplos
- /effort high: Mais raciocínio para um bug difícil.
- /effort low: Rápido e barato para renomear arquivos ou ajustar texto.
- /effort auto: Devolve a escolha do esforço ao Claude.

## Comandos relacionados
- /usage: Combina com o custo da sessão.

## Armadilhas
- xhigh gasta mais tokens.
- Não use na sessão inteira.

Documentação: https://code.claude.com/docs/en/model-config#adjust-effort-level
