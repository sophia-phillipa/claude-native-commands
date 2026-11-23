# /compact: descrição completa

Categoria: Contexto e memória. Tipo: comando embutido do Claude Code.

## O que faz
Resume a conversa até aqui e segue com o resumo no lugar do histórico completo.

## Por que usar
Libera espaço na janela de contexto sem abrir outra sessão. Com instruções, você escolhe o que o resumo deve preservar.

## Como usar
Rode /compact sozinho ou com instruções do que manter.

Parâmetro opcional: [instruções], texto livre. Diz ao resumo o que guardar com prioridade.

## Quando usar
Perto do limite da sessão, antes de a compactação automática rodar sozinha. Rodando na mão, você descreve os critérios do resumo: o que guardar e o que descartar.

## Observação
A compactação automática roda sozinha perto do limite. O comando serve para compactar antes, na hora e com os critérios que você escolher.

## O que acontece no fluxo do prompt e do motor
1. A conversa enche a janela de contexto.
2. Você digita /compact, com ou sem instruções.
3. O motor lê o histórico da conversa.
4. O motor escreve um resumo fiel, guiado pelas instruções.
5. A sessão segue mais leve, com o resumo no lugar do histórico.

## Exemplos
- /compact: resumo padrão da sessão.
- /compact mantenha os arquivos alterados, os testes que falharam e as decisões tomadas: resumo guiado pelo que importa para continuar.
- /compact descarte os logs longos e guarde só as conclusões: bom depois de uma sessão de depuração com muita saída.

## Comandos relacionados
- /context: mede quanto contexto sobrou.
- /autocompact: ajusta a compactação automática.
- /clear: recomeça com contexto vazio.

## Armadilhas
- Sem instruções, detalhes podem sumir.
- Mensagens exatas viram resumo.

Documentação: https://code.claude.com/docs/en/context-window#what-survives-compaction
