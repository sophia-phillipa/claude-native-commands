# /workflow-authoring: descrição completa

Categoria: Criação e referência. Tipo: skill embutida do Claude Code.

## O que faz
Uma referência para escrever um script da ferramenta Workflow, que coordena vários subagentes: a API do script, armadilhas, como retomar uma execução, padrões de qualidade e exemplos.

## Por que usar
Um script de workflow pode disparar dezenas de agentes e gastar muito. Ler a referência antes evita erros caros de estrutura.

## Como usar
Digite /workflow-authoring antes de montar o script. Carregar a skill não autoriza rodar nada: a execução continua dependendo do seu pedido.

## Quando usar
Só depois de decidir que a tarefa pede vários agentes coordenados por script, e antes de escrever o primeiro.

## Observação
Pensada para quando você já decidiu usar um workflow. Para uma tarefa comum, um subagente basta. Os workflows dinâmicos rodam no Desktop.

## O que acontece no fluxo do prompt e do motor
1. Você decide usar um workflow.
2. Você digita /workflow-authoring.
3. A referência ensina a API do script, as armadilhas e a retomada.
4. Você monta o script.
5. O script fica pronto, sem rodar nada.

## Exemplos
- /workflow-authoring: carrega a referência para escrever o script.
- /workflow-authoring revisar todos os módulos em paralelo e juntar os achados: monta o esqueleto de um script de revisão.
- /workflow-authoring como retomar uma execução que parou no meio?: consulta a seção de retomada.

## Comandos relacionados
- /design-sync: Enviar seu design system ao Claude Design. O card não cita outro comando; a ligação segue o critério E8 (mesma categoria).

## Armadilhas
- Tarefa comum não pede workflow.
- Script pode disparar muitos agentes.

Documentação: https://code.claude.com/docs/en/workflows
