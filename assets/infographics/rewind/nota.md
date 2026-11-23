# /rewind: descrição completa

Categoria: Contexto e memória. Tipo: comando embutido do Claude Code.

## O que faz
Volta a conversa e/ou o código a um ponto anterior, ou faz um resumo a partir de uma mensagem escolhida. A documentação oficial descreve o recurso como checkpointing.

## Por que usar
Permite desfazer um caminho que não deu certo sem começar a sessão do zero. A conversa e o código voltam a um ponto conhecido.

## Como usar
Rode /rewind para voltar a um ponto anterior. Os aliases /undo e /checkpoint executam o mesmo comando.

## Quando usar
Quando a conversa ou o código seguiu por um caminho que não deu certo, e você quer voltar a um ponto anterior ou resumir a partir de uma mensagem.

## Observação
Documentado na referência oficial. Doc oficial: checkpointing. Aliases /checkpoint e /undo.

## O que acontece no fluxo do prompt e do motor
1. Você digita /rewind.
2. O menu lista os prompts enviados na sessão.
3. O motor restaura código ou conversa, conforme a opção escolhida.
4. A sessão volta ao ponto escolhido.

## Exemplos
- /rewind: volta a conversa ou o código a um ponto anterior.
- /undo: alias de /rewind, a mesma ação com outro nome.
- /checkpoint: outro alias, útil se você lembrar do recurso pelo nome checkpoint.

## Comandos relacionados
- /compact: resumir a conversa e liberar contexto.

## Armadilhas
- Arquivos mudados só pelo Bash não voltam.
- Mudanças externas não são rastreadas.

Documentação: https://code.claude.com/docs/en/checkpointing
