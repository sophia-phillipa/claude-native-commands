# /advisor: descrição completa

Categoria: Modelo e potência. Tipo: comando embutido do Claude Code.

## O que faz
Liga um revisor com um modelo mais forte. Claude o consulta antes de começar o trabalho de verdade, quando trava e antes de dizer que terminou.

## Por que usar
Um segundo olhar no começo evita seguir por um caminho errado, e no fim pega o que faltou conferir. O Claude decide quando consultar o revisor, e cada consulta consome tokens.

## Como usar
Digite /advisor seguido do modelo revisor, ou /advisor off para desligar.

Parâmetros:
- [modelo]: opcional. O modelo que vai revisar; sem ele, abre o seletor de modelos. A dica do comando lista os aceitos na conta; fable, por exemplo, vira Fable 5.2.
- off: palavra fixa. Desliga o revisor.

## Quando usar
Tarefas de várias etapas com risco de errar o caminho, como uma refatoração ou uma decisão de arquitetura. Em perguntas rápidas, desligue para não pagar consultas à toa.

## Observação
Depende do provedor (não Bedrock, Agent Platform nem Foundry), do modelo principal e de uma flag de recurso buscada da Anthropic; pode não aparecer em todas as sessões. A documentação confirma que funciona no app Desktop.

## O que acontece no fluxo do prompt e do motor
1. Você digita /advisor
2. Revisor fica ativo na sessão
3. Claude consulta em momentos-chave
4. Claude aplica a orientação

## Exemplos
- /advisor fable: Revisor Fable 5.2.
- /advisor opus: Troca o revisor para o Opus.
- /advisor off: Desliga o revisor para tarefas curtas e baratas.

## Comandos relacionados
- /model: trocar o modelo da sessão.

## Armadilhas
- Pode não aparecer em todas as sessões.
- Tarefa curta paga consultas à toa.

Documentação: https://code.claude.com/docs/en/advisor
