# /design-consent: descrição completa

Categoria: Extensões e conexões. Tipo: comando embutido do Claude Code.

## O que faz
Concede ao Claude acesso ao Claude Design. Quando uma resposta do Claude pedir que você rode este comando, digite-o no prompt do Claude Code você mesmo.

## Por que usar
Mantém a decisão de dar acesso com você, já que o comando é digitado por você e não pelo Claude.

## Como usar
Rode /design consent no prompt do Claude Code quando o Claude pedir. Para retirar o acesso depois, use /design revoke.

## Quando usar
Quando uma resposta do Claude pedir que você conceda acesso ao Claude Design.

## Observação
A referência oficial descreve o comando. Testado no app: funcionou.

## O que acontece no fluxo do prompt e do motor
1. Você digita /design consent.
2. O motor concede o acesso.
3. Claude passa a ter acesso.

## Exemplos
- /design consent: concede o acesso aos projetos do Claude Design.
- /design consent: digite você mesmo no prompt quando o Claude pedir.
- /design consent: para desfazer, use /design revoke.

## Comandos relacionados
- /design-revoke: retira o acesso ao Claude Design.

## Armadilhas
- Claude não digita este comando.

Documentação: https://code.claude.com/docs/en/commands#all-commands
