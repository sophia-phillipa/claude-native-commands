# /model: descrição completa

Categoria: Modelo e potência. Tipo: comando embutido do Claude Code.

## O que faz
Define o modelo de IA usado pelo Claude Code na sessão.

## Por que usar
Modelos menores respondem mais rápido e custam menos. Os maiores resolvem melhor problemas difíceis. Combina com o /effort.

## Como usar
Use /model <modelo>.

Parâmetros:
- [modelo]: opcional. O nome do modelo, como opus, sonnet, haiku ou fable; sem ele, abre o seletor. A dica do comando mostra os aceitos na sua conta.

## Quando usar
Quando o trabalho muda de natureza: haiku ou sonnet para tarefas mecânicas e rápidas, opus para um problema difícil ou uma revisão importante.

## Observação
No Desktop, o modelo também pode ser trocado no seletor abaixo da caixa de prompt.

## O que acontece no fluxo do prompt e do motor
1. Você digita /model
2. O motor troca o modelo
3. Próximos pedidos usam o novo
4. Sessão segue no novo modelo

## Exemplos
- /model sonnet: Bom equilíbrio para o trabalho do dia a dia.
- /model haiku: Rápido e barato para tarefas mecânicas.
- /model opus: Volta ao modelo mais forte para um problema difícil.

## Comandos relacionados
- /effort: combina com o nível de esforço.

## Armadilhas
- Vira padrão das próximas sessões.

Documentação: https://code.claude.com/docs/en/model-config
