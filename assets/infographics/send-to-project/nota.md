# /send-to-project: descrição completa

Categoria: Criação e referência. Tipo: comando embutido, para usuário.

## O que faz
Leva o trabalho desta sessão a um Claude Project, no claude.ai. O comando lê o que o Claude Code leu desta pasta e aceita o nome ou o id do projeto de destino e, se você quiser, uma mensagem ou nota.

## Por que usar
Continua o trabalho num projeto do claude.ai, sem recomeçar do zero numa conversa nova.

## Como usar
Digite /send-to-project com o nome ou o id do projeto e, se quiser, a palavra nota ou mensagem seguida do texto. Só você roda o comando, porque ele envia o trabalho a um projeto na nuvem.

## Quando usar
Quando o trabalho de uma sessão deve continuar num Claude Project, no claude.ai, em vez de virar uma conversa nova.

## Observação
Não consta na tabela oficial de comandos. Aparece no binário 2.1.325 como comando de usuário e no menu do app em vídeo de 22/11/2026, com o nome cortado no tooltip. Ainda não foi testado no app.

## O que acontece no fluxo do prompt e do motor
1. Você digita /send-to-project.
2. Informa o projeto de destino.
3. Envia o que o Claude Code leu desta pasta.
4. O trabalho segue no projeto.

## Exemplos
- /send-to-project: Pede o projeto de destino antes de enviar.
- /send-to-project Pesquisa de fornecedores: Envia o trabalho ao projeto com esse nome.
- /send-to-project <nome-do-projeto> nota: revisar os custos: Envia o trabalho com uma nota para quem for continuar.

## Comandos relacionados
- /fork: Bifurca a conversa em outra sessão.

## Armadilhas
- Não consta na tabela oficial.
- Ainda não testado no app.

Documentação: https://code.claude.com/docs/en/commands#all-commands (não consta na tabela consultada em 26/11/2026)
