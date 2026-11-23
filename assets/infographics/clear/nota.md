# /clear: descrição completa

Categoria: Contexto e memória. Tipo: comando embutido do Claude Code. Alias: /reset, /new.

## O que faz
Começa uma sessão nova com o contexto vazio. A sessão anterior fica salva no disco.

## Por que usar
Contexto limpo custa menos e evita que restos da tarefa anterior atrapalhem a nova. Diferente do /compact, nada da conversa passa para a sessão nova.

## Como usar
Use /clear, com ou sem um nome.

Parâmetro: [nome]. Opcional. Um nome para a conversa anterior, que aparece assim na lista do /resume.

## Quando usar
Ao terminar uma tarefa e começar outra sem relação com ela, na mesma pasta: contexto limpo sai mais barato e não confunde a tarefa nova com a anterior.

## O que acontece no fluxo do prompt e do motor
1. Você digita /clear
2. Salva a sessão anterior
3. Abre sessão nova, contexto vazio
4. Próxima tarefa sem restos antigos

## Exemplos
- /clear: contexto vazio para a próxima tarefa.
- /clear revisão dos READMEs: começa de novo; o nome vai para a conversa anterior, na lista do /resume.
- /new: mesmo comando pelo apelido.

## Comandos relacionados
- /compact: segue com resumo da conversa.

## Armadilhas
- Para seguir a conversa, use /compact.

Documentação: https://code.claude.com/docs/en/commands#all-commands
