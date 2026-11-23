# /whiteboard: descrição completa

Categoria: Criação e referência. Tipo: skill embutida do Claude Code.

## O que faz
Cria um artefato novo do tipo Whiteboard, a partir de um briefing que você descreve. Sem briefing, o Claude pergunta antes para que serve o quadro.

## Por que usar
Entrega o quadro como artefato da sua conta, em vez de só texto na conversa.

## Como usar
Digite /whiteboard seguido do objetivo do quadro, como /whiteboard mapa dos módulos do sistema de pagamentos. Sem isso, o Claude pergunta antes de criar.

Parâmetro opcional: [briefing]. Para que serve o quadro. Sem ele, o Claude pergunta antes de criar.

## Quando usar
Quando você quer um quadro publicado como artefato, sobre um tema que descreve no briefing, e a conta tem o tipo Whiteboard.

## Observação
Testado no app Desktop (22/11/2026). Depende da conta: sem o tipo Whiteboard, o app diz que o recurso está em beta e pode não estar disponível na conta ainda. Não está na tabela oficial de comandos: é uma skill embutida da versão 2.1.325. A página de artefatos cita Whiteboards entre os tipos da conta (Sheets, Whiteboards, Data).

## O que acontece no fluxo do prompt e do motor
1. Você digita /whiteboard com briefing
2. A skill recebe o briefing
3. O Claude cria o artefato
4. Quadro entregue como artefato

## Exemplos
- /whiteboard mapa dos módulos do sistema de pagamentos: cria um artefato Whiteboard a partir desse briefing.
- /whiteboard: sem briefing, o Claude pergunta primeiro para que serve o quadro.
- /whiteboard retrospectiva da sprint com o time: cria um Whiteboard novo para a retrospectiva.

## Comandos relacionados
- /design-sync: enviar seu design system ao Claude Design.

## Armadilhas
- Sem o tipo, diz que é beta.
- Sem briefing, o Claude pergunta antes.

Documentação: https://code.claude.com/docs/en/artifacts (seção "Start an artifact from a template": "Your account can include others, such as Sheets, Whiteboards, or Data.").
