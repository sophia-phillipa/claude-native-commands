# /btw: descrição completa

Categoria: Contexto e memória. Tipo: comando embutido do Claude Code.

## O que faz
Faz uma pergunta lateral sobre a sessão atual sem acrescentá-la à conversa. Sem pergunta, mostra a última pergunta lateral feita, para rever respostas anteriores; se ainda não houve nenhuma, imprime uma linha de uso.

## Por que usar
Tira uma dúvida rápida no meio do trabalho sem poluir o histórico da conversa principal.

## Como usar
Digite /btw seguido da pergunta. Sem pergunta, /btw mostra a última que você fez.

Parâmetro opcional: [question]. A pergunta lateral; sem ela, o comando mostra a última feita.

## Quando usar
Quando surge uma dúvida rápida no meio do trabalho e você não quer que a resposta entre no histórico da conversa.

## Observação
Doc do Desktop: há um "side chat" para perguntas laterais.

## O que acontece no fluxo do prompt e do motor
1. Você digita /btw e pergunta.
2. O motor lê o contexto atual da conversa.
3. O motor gera uma resposta lateral.
4. O histórico principal segue intacto.

## Exemplos
- /btw qual a diferença entre fork e branch?: pergunta lateral, que não entra no histórico principal.
- /btw: mostra a última pergunta lateral, para rever a resposta.
- /btw o nome dessa função é o mesmo do arquivo?: dúvida rápida, respondida sem mudar a conversa.

## Comandos relacionados
- /compact: resumir a conversa e liberar contexto.

## Armadilhas
- Não lê arquivos nem executa comandos.
- Resposta única, sem turnos seguintes.

Documentação: https://code.claude.com/docs/en/interactive-mode#side-questions-with-%2Fbtw
