# /skill-doctor: descrição completa

Categoria: Diagnóstico e uso. Tipo: comando embutido do Claude Code.

## O que faz
Lista as skills da sessão, exceto as embutidas e as de empresa, com o contexto que cada uma ocupa por turno, os tokens dos últimos 7 dias e quantas vezes foi usada.

## Por que usar
Toda skill carregada entra no prompt de sistema em todo turno. Saber quais nunca são usadas mostra onde dá para economizar contexto.

## Como usar
No app Desktop ele responde “Skill usage reports are not available on this connection”. Rode no painel Terminal: abra claude e digite /skill-doctor.

## Quando usar
Quando a sessão já começa pesada e o /context mostra as skills ocupando milhares de tokens antes da primeira mensagem. Rode no terminal para decidir quais desligar.

## Observação
Testado no app Desktop, ele não funcionou. No terminal ele roda normalmente e aponta as skills carregadas que nunca foram usadas. O /context, que funciona no app, mostra a parte “Skills” do contexto.

## O que acontece no fluxo do prompt e do motor
1. Você digita /skill-doctor.
2. O motor lista skills carregadas.
3. Mede contexto de cada skill.
4. Marca skills nunca usadas.
5. Relatório aponta o que desligar.

## Exemplos
- /skill-doctor: no terminal, relatório completo das skills da sessão.
- /skill-doctor: rode de novo depois de instalar um plugin e compare a coluna context.
- /context: alternativa que funciona no app; veja a linha Skills na tabela.

## Comandos relacionados
- /context: mostra a parte Skills do contexto.

## Armadilhas
- Não funciona no app Desktop.

Documentação: https://code.claude.com/docs/en/skills#find-unused-skills
