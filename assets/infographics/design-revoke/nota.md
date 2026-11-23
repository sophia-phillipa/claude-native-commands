# /design-revoke: descrição completa

Categoria: Extensões e conexões. Tipo: comando embutido do Claude Code.

## O que faz
Retira o acesso que o Claude tem ao Claude Design. É o oposto do /design consent, que concede esse acesso.

## Por que usar
Permite cortar o acesso quando ele não for mais necessário.

## Como usar
Rode /design revoke no prompt do Claude Code.

## Quando usar
Quando você quer retirar o acesso do Claude aos projetos do Claude Design.

## Exemplos
- /design revoke: retira o acesso do Claude aos projetos de design.
- /design revoke: use quando não quiser mais que o Claude acesse os projetos.
- /design revoke: para conceder de novo, rode /design consent.

## Comandos relacionados
- /design consent: concede o acesso de novo.

## O que acontece no fluxo do prompt e do motor
1. Você digita /design revoke.
2. O motor retira o acesso.
3. Claude deixa de ter acesso.

## Armadilhas
- Volta só com /design consent.

Documentação: https://code.claude.com/docs/en/commands#all-commands
