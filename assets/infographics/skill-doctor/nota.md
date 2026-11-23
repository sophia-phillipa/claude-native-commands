# /skill-doctor: descrição completa

Categoria: Diagnóstico e uso. Tipo: comando embutido do Claude Code.

## O que faz
Lista as skills carregadas na sessão com a origem, o contexto que cada uma ocupa por turno, os tokens dos últimos 7 dias, quantas vezes foi usada e quando.

## Por que usar
Toda skill carregada entra no prompt de sistema em todo turno. Saber quais nunca são usadas mostra onde dá para economizar contexto.

## Como usar
Rode /skill-doctor no painel Terminal: abra claude e digite /skill-doctor. No app Desktop ele responde "Skill usage reports are not available on this connection".

## Quando usar
Quando a sessão já começa pesada e o /context mostra as skills ocupando milhares de tokens antes da primeira mensagem. Rode no terminal para decidir quais desligar.

## Observação
No app: indisponível nesta conexão. Testado no app Desktop, ele não funcionou. No terminal ele roda normalmente e aponta as skills carregadas que nunca foram usadas. O /context, que funciona no app, mostra a parte "Skills" do contexto.

## O que acontece no fluxo do prompt e do motor
1. Você digita /skill-doctor no terminal.
2. O motor lista as skills carregadas na sessão.
3. O motor mede o contexto que cada skill ocupa por turno, com o seu uso.
4. O motor marca as skills que nunca foram usadas.
5. O relatório aponta as skills que podem ser desligadas.

## Exemplos
- /skill-doctor: relatório completo das skills da sessão, no terminal.
- /skill-doctor: rode de novo depois de instalar um plugin e compare a coluna context.
- /context: alternativa que funciona no app; veja a linha Skills na tabela.

## Comandos relacionados
- /context: mostra a parte Skills do contexto.

## Armadilhas
- Não funciona no app Desktop.

Documentação: https://code.claude.com/docs/en/skills#find-unused-skills
