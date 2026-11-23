# /design-sync: descrição completa

Categoria: Criação e referência. Tipo: skill embutida do Claude Code.

## O que faz
Empacota os componentes React reais do seu design system, vindos do Storybook ou de um pacote, e os envia para um projeto no claude.ai/design.

## Por que usar
O Claude Design passa a trabalhar com os componentes que o seu código usa de verdade, não com imitações desenhadas à mão.

## Como usar
Digite /design-sync e acompanhe as perguntas. Ele roda um conversor que junta o código dos componentes e faz o envio, pedindo a sua confirmação antes de criar o projeto ou mexer em arquivos.

## Quando usar
Quando o design system do seu time já existe em código e você quer que o Claude Design use os mesmos componentes.

## Observação
Exige uma conta com acesso ao Claude Design e a liberação de acesso aos seus projetos de design. Pode pedir login antes de começar.

## O que acontece no fluxo do prompt e do motor
1. Você digita /design-sync.
2. Motor converte o design system.
3. Claude Design recebe os componentes.

## Exemplos
- /design-sync: inicia o envio do design system do projeto atual.
- /design-sync meu Storybook está em packages/ui: aponta de onde vêm os componentes.
- /design-sync atualize o projeto de design depois das mudanças nos botões: reenvia o que mudou.

## Comandos relacionados
- /dataviz: Gráficos que seguem um só sistema visual.

## Armadilhas
- Repo grande pode levar horas.
- Pode pedir login antes de começar.

Documentação: https://code.claude.com/docs/en/commands#all-commands
