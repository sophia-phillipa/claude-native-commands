# /recap: descrição completa

Categoria: Contexto e memória. Tipo: comando embutido do Claude Code.

## O que faz
Gera na hora um resumo de uma linha da sessão.

## Por que usar
Serve para lembrar onde você parou ao voltar a uma sessão, ou para anotar o estado antes de trocar de tarefa.

## Como usar
Rode /recap sem parâmetros.

## Quando usar
Antes de pausar ou de trocar de sessão, e ao voltar para uma sessão antiga sem lembrar onde parou.

## Observação
A descrição segue a referência oficial do Claude Code.

## O que acontece no fluxo do prompt e do motor
1. Você digita /recap
2. O motor gera o resumo
3. Resume em uma linha
4. Você lembra onde parou

## Exemplos
- /recap: resumo curto do que a sessão fez até aqui.
- /recap: rode antes de pausar e cole a linha nas suas notas do dia.
- /loop 30m /recap: combinado com /loop, um resumo novo a cada meia hora.

## Comandos relacionados
- /loop: resumo novo a cada intervalo.

## Armadilhas
- Resumo tem limite de 400 caracteres.

Documentação: https://code.claude.com/docs/en/interactive-mode#session-recap
