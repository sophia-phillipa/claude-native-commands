# /goal: descrição completa

Categoria: Automação. Tipo: comando embutido do Claude Code.

## O que faz
Define uma condição de pronto. Depois de cada turno, um modelo avaliador separado confere a condição; enquanto ela não estiver cumprida, Claude segue trabalhando.

## Por que usar
Tarefas longas às vezes param no meio, com “quase pronto”. Com uma meta escrita, a sessão só para quando o critério que você deu é verdadeiro, ou quando o avaliador julga a meta impossível ou um erro exige correção.

## Como usar
Digite /goal seguido da condição. Sem condição, ele mostra a meta atual ou a última cumprida. Para remover a meta, use /goal clear.

Parâmetros:
- [condição]: opcional. Texto livre com o critério de pronto. Quanto mais verificável, melhor: um teste que passa, um arquivo que existe, um comando que sai sem erro.
- clear: palavra fixa. Remove a meta atual.

## Quando usar
Tarefas longas que você deixa rodando sozinhas, como uma migração ou uma bateria de testes, quando você sabe dizer exatamente o que é “pronto” e não quer voltar e achar o trabalho parado no meio.

## Observação
A documentação confirma que funciona no app Desktop.

## O que acontece no fluxo do prompt e do motor
1. Você define a condição de pronto.
2. Claude começa o turno com a condição como pedido.
3. Um modelo confere se a condição vale.
4. Se ainda não vale, Claude segue trabalhando em outro turno.
5. Quando a condição vale, a meta é cumprida e Claude para.

## Exemplos
- /goal todos os testes do pytest passam e o ruff não acusa nada: meta verificável, Claude roda os testes antes de encerrar.
- /goal o README.md e o README.pt-BR.md têm a seção de desinstalação: meta sobre documentação, confere os dois arquivos antes de parar.
- /goal clear: apaga a meta atual quando você quer encerrar do seu jeito.

## Comandos relacionados
- /loop: repetir em intervalos.

## Armadilhas
- Condição que a conversa não mostra.
- Erro que exige correção apaga a meta.

Documentação: https://code.claude.com/docs/en/goal
