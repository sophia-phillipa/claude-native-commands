# /theme: descrição completa

Categoria: Ajustes e permissões. Tipo: comando embutido do Claude Code.

## O que faz
Muda o tema de cores. Há a opção auto, que acompanha o fundo claro ou escuro do terminal, variantes claras e escuras, temas para daltonismo, temas ANSI que usam a paleta do terminal e temas personalizados de ~/.claude/themes/ ou de plugins.

## Por que usar
Deixa a leitura confortável no seu terminal e, para quem tem daltonismo, facilita a distinção entre as cores.

## Como usar
Rode /theme e escolha na lista. Para criar um tema próprio, selecione a opção New custom theme…

## Quando usar
Quando o contraste da interface não combina com o fundo do terminal, ou quando você precisa de cores mais fáceis de distinguir.

## Observação
Documentado na referência oficial. Inclui temas personalizados em ~/.claude/themes/ e de plugins.

## O que acontece no fluxo do prompt e do motor
1. Você digita /theme.
2. Abre a lista de temas.
3. Você escolhe o tema.
4. Interface troca as cores.

## Exemplos
- /theme: abre a lista de temas para escolher um.
- /theme: escolha auto para acompanhar o fundo claro ou escuro do terminal.
- /theme: selecione New custom theme… para criar um tema próprio.

## Comandos relacionados
- /config: Mudar uma configuração pelo nome

## Armadilhas
- Não muda as cores do terminal
- Primeiro tema em pasta nova pede reinício

Documentação: https://code.claude.com/docs/en/terminal-config#create-a-custom-theme
