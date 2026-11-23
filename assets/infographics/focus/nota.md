# /focus: descrição completa

Categoria: Ajustes e permissões. Tipo: comando embutido do Claude Code.

## O que faz
Liga ou desliga a visão de foco, que mostra só o seu último prompt, um resumo de uma linha das chamadas de ferramenta com as estatísticas de edição e a resposta final. O resumo também conta os subagentes lançados no turno e junta as notificações de tarefas em segundo plano concluídas em uma única contagem.

## Por que usar
Deixa a conversa mais limpa quando você quer ver só o pedido e o resultado, sem a sequência de ferramentas.

## Como usar
Rode /focus para alternar. A escolha fica salva e vale nas próximas sessões; a configuração viewMode pode substituí-la.

## Quando usar
Quando a conversa ficou longa demais e você quer enxergar só o pedido e o resultado final.

## Observação
Só funciona com renderização em tela cheia. Pelo Remote Control, /focus on e /focus off valem só para a sessão, a partir da versão 2.1.281.

## O que acontece no fluxo do prompt e do motor
1. Você digita /focus.
2. Liga ou desliga a visão.
3. Mostra prompt, resumo e resposta.
4. A escolha fica salva e vale nas próximas sessões.

## Exemplos
- /focus: liga a visão de foco com prompt, resumo e resposta final.
- /focus: chamado de novo, volta à visão normal da conversa.
- /focus: a escolha fica salva e vale nas próximas sessões.

## Comandos relacionados
- /config: Mudar uma configuração pelo nome

## Armadilhas
- Só com renderização em tela cheia
- Configuração viewMode pode substituí-la

Documentação: https://code.claude.com/docs/en/settings-reference#viewmode
