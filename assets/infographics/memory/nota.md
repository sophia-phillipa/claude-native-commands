# /memory: descrição completa

Categoria: Contexto e memória. Tipo: comando embutido do Claude Code.

## O que faz
Edita os arquivos CLAUDE.md, liga ou desliga a memória automática e mostra as entradas que ela guardou.

## Por que usar
As instruções em CLAUDE.md valem em toda sessão do projeto. Ver a memória automática evita que o Claude siga uma nota antiga.

## Como usar
Rode /memory e escolha o arquivo ou a opção que quer editar.

## Quando usar
Quando o projeto ganha regras que devem valer em toda sessão, ou quando uma nota antiga do Claude começa a atrapalhar.

## Observação
Documentado na referência oficial. A referência cobre a memória automática e as entradas que ela registra.

## O que acontece no fluxo do prompt e do motor
1. Você digita /memory.
2. O motor lista os arquivos CLAUDE.md e de memória.
3. O motor abre o arquivo escolhido no editor.
4. Toda sessão lê as instruções do CLAUDE.md.

## Exemplos
- /memory: abre os arquivos CLAUDE.md para editar as instruções do projeto.
- /memory: mostra o que a memória automática registrou até agora.
- /memory: desliga a memória automática para que novas notas deixem de ser guardadas.

## Comandos relacionados
- /compact: resumir a conversa e liberar contexto.

## Armadilhas
- Memória automática não sai da máquina.
- Notas antigas ficam até alguém apagar.

Documentação: https://code.claude.com/docs/en/memory#auto-memory
