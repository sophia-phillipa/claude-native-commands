# /feedback: descrição completa

Categoria: Diagnóstico e uso. Tipo: comando embutido do Claude Code.

## O que faz
Envia feedback sobre o Claude Code pelo mesmo diálogo do /bug, com o mesmo consentimento e as mesmas regras de envio. Nas sessões com feedback sugerido pelo Claude, /feedback sem argumento abre a fila de rascunhos, com os de todas as sessões, onde você revisa, edita, envia ou descarta cada um.

## Por que usar
Permite relatar o que faltou ou não funcionou, com uma etapa de consentimento antes do envio.

## Como usar
Rode /feedback seguido do texto do relatório para abrir o diálogo direto, ou só /feedback para ver a fila de rascunhos, quando houver.

Parâmetro opcional: [report]. Texto do relatório; com ele, o diálogo de envio abre direto.

## Quando usar
Quando algo não funcionou como esperado no Claude Code e você quer deixar um relato para o fabricante.

## Observação
Documentado na referência oficial.

## O que acontece no fluxo do prompt e do motor
1. Algo não funcionou como esperado.
2. Você digita /feedback com relato.
3. O motor abre o diálogo de envio.
4. Você dá o consentimento antes do envio.
5. O relato segue ao fabricante.

## Exemplos
- /feedback a busca de arquivos demora muito em pastas com milhares de itens: abre o diálogo de envio direto, com esse relato.
- /feedback: mostra os rascunhos que o Claude deixou na fila, se houver.
- /feedback seria útil um atalho para repetir o último comando: abre o diálogo de envio com essa sugestão; nada sai antes do seu consentimento.

## Comandos relacionados
- /bug: abre o diálogo de envio direto.

## Armadilhas
- Sem texto: fila de rascunhos, se houver.
- Nada sai sem sua confirmação.

Documentação: https://code.claude.com/docs/en/tools-reference#sendfeedback-tool-behavior
