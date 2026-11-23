# /heapdump: descrição completa

Categoria: Diagnóstico e uso. Tipo: comando embutido do Claude Code.

## O que faz
Grava um snapshot do heap do JavaScript e um resumo de memória na pasta ~/Desktop, ou no seu diretório pessoal no Linux quando não há pasta Desktop. Serve para diagnosticar uso alto de memória.

## Por que usar
Dá material concreto para entender um consumo de memória alto antes de relatar o problema.

## Como usar
Digite /heapdump por inteiro, porque o comando fica oculto na lista. Ao relatar um problema de memória, anexe só o arquivo -diagnostics.json.

## Quando usar
Quando a sessão ou o Claude Code está usando memória demais e você precisa investigar antes de reportar.

## Observação
O arquivo .heapsnapshot contém toda a conversa e credenciais, então não deve ser compartilhado. Pela referência oficial, o comando também imprime na conversa um resumo com a memória total, a parte no heap do JavaScript e a parte fora dele.

## O que acontece no fluxo do prompt e do motor
1. A sessão usa memória demais.
2. Você digita /heapdump por inteiro.
3. O motor grava o snapshot do heap.
4. O motor imprime o resumo.
5. Você anexa o arquivo -diagnostics.json ao relato.

## Exemplos
- /heapdump: grava o snapshot e o resumo de memória na pasta indicada.
- /heapdump: use para investigar memória em excesso antes de reportar o problema.
- /heapdump: envie só o arquivo -diagnostics.json, nunca o .heapsnapshot.

## Comandos relacionados
- /doctor: check-up da instalação (mesma categoria, Diagnóstico e uso).

## Armadilhas
- Contém a conversa e credenciais.
- Não compartilhe o .heapsnapshot.

Documentação: https://code.claude.com/docs/en/troubleshooting#high-cpu-or-memory-usage
