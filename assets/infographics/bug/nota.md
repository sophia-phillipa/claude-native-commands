# /bug: descrição completa

Categoria: Diagnóstico e uso. Tipo: comando embutido, com alias /share.

## O que faz
Relata um problema ao fabricante ou compartilha a conversa. Antes do envio, você escolhe quanto do histórico entra e confirma numa tela de consentimento.

## Por que usar
Quem procura como reportar um erro encontra o comando certo, com consentimento antes do envio.

## Como usar
Use /bug com o problema descrito, como em /bug a busca de arquivos demora muito. O cartão de /feedback explica o comando vizinho, que envia feedback ao Anthropic.

## Quando usar
Quando algo do Claude Code falha e você quer relatar ao fabricante, escolhendo quanto do histórico da sessão vai junto.

## Observação
Observado em 22/11/2026, no app Desktop (Claude Code 2.1.325): /bug abriu o diálogo de /feedback. O binário 2.1.325 define /bug como comando próprio, com alias /share. A diferença não foi explicada.

## O que acontece no fluxo do prompt e do motor
1. Você digita /bug.
2. Escolhe quanto do histórico entra.
3. Abre o diálogo de consentimento.
4. Você confirma antes do envio.

## Exemplos
- /bug: Abre o diálogo de envio, com consentimento antes do envio.
- /bug a busca de arquivos demora muito: Relato direto, com o texto do problema.
- /bug: Com a conversa aberta, o diálogo deixa escolher quanto do histórico entra.

## Comandos relacionados
- /feedback: Feedback, outro comando embutido.

## Armadilhas
- Alias do comando: /share.
- No app de 22/11/2026, abriu o /feedback.

Documentação: https://code.claude.com/docs/en/commands#all-commands
