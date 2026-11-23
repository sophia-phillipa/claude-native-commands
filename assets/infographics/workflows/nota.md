# /workflows: descrição completa

Categoria: Automação. Tipo: comando embutido do Claude Code.

## O que faz
Abre a visão de andamento dos workflows, onde você acompanha, pausa, retoma e salva os que estão rodando ou já terminaram.

## Por que usar
Com vários agentes rodando, esta tela mostra em que ponto cada workflow está e permite pausar ou retomar um deles.

## Como usar
Digite /workflows para abrir a visão. Dali, acompanhe a execução escolhida, pause, retome ou salve. No app, /workflow também funciona e aparece como /workflows (workflow).

## Quando usar
Quando um workflow com vários agentes está rodando ou já terminou, e você quer ver em que ponto ele está.

## Observação
Documentado na referência oficial. A documentação descreve a visão de andamento na página de workflows.

## O que acontece no fluxo do prompt e do motor
1. Você digita /workflows.
2. O motor lista execuções rodando e terminadas.
3. A visão mostra fases e agentes da execução escolhida.
4. A execução fica pausada, retomada ou salva.

## Exemplos
- /workflows: mostra os workflows em execução e os que já terminaram.
- /workflows: pausa uma execução em andamento para retomá-la depois.
- /workflows: salva uma execução concluída para consulta posterior.

## Comandos relacionados
- /goal: trabalhar até a meta ser cumprida.

## Armadilhas
- Sair da sessão não retoma o workflow sozinho: é preciso pedir ao Claude para relançá-lo.
- Muitos agentes gastam mais tokens que uma conversa comum.

Documentação: https://code.claude.com/docs/en/workflows#watch-the-run
