# /storage: descrição completa

Categoria: Ajustes e permissões. Tipo: comando do app, que abre o diálogo Armazenamento.

## O que faz
Abre o diálogo Armazenamento do app Claude Desktop, com o espaço usado neste computador. O total aparece dividido em tarefas Cowork, sessões de código e worktrees, runtime e caches do app. Cada seção tem detalhes, e a seção de caches tem um botão para limpar o cache e reiniciar o app.

## Por que usar
Mostra onde está o espaço antes de apagar qualquer coisa.

## Como usar
Digite /storage no app para abrir o diálogo, depois confira cada seção. O botão Atualizar recalcula os números.

## Quando usar
Quando o disco está cheio ou você quer saber o que o Claude ocupa neste computador antes de limpar algo.

## Observação
Não consta na tabela oficial nem como nome de comando no binário Claude Code 2.1.325. Confirmado por captura de tela do app Desktop em 26/11/2026. Os valores variam de computador para computador, por isso o cartão não mostra números.

## O que acontece no fluxo do prompt e do motor
1. Você digita /storage.
2. Calcula o espaço por categoria.
3. Mostra o total e as seções.
4. Limpa caches, se quiser.

## Exemplos
- /storage: Abre o diálogo de armazenamento do app.
- /storage: Mostra o total em uso e a divisão por categoria.
- /storage: Atualiza os números com Atualizar, antes de limpar caches.

## Comandos relacionados
- /send-to-project: Leva o trabalho a um projeto.

## Armadilhas
- Não consta na tabela oficial.
- Ainda não testado no app.

Documentação: https://code.claude.com/docs/en/commands#all-commands (não consta na tabela consultada em 26/11/2026)
