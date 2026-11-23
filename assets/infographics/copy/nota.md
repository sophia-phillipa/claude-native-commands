# /copy: descrição completa

Categoria: Revisão de código. Tipo: comando embutido do Claude Code.

## O que faz
Copia a última resposta do Claude para a área de transferência. Com um número N, copia a N-ésima resposta mais recente. Se a resposta tiver blocos de código ou citações, abre um seletor para escolher blocos individuais ou a resposta inteira.

## Por que usar
Você leva o texto para outro lugar sem selecioná-lo na tela, o que ajuda quando a resposta é longa ou traz código.

## Como usar
Rode /copy para a última resposta ou /copy 2 para a penúltima. No seletor, aperte w para gravar a escolha num arquivo em vez de copiar; isso serve, por exemplo, quando você trabalha por SSH.

Parâmetro opcional: [N]. Número da resposta, contando a partir da última: 2 copia a penúltima.

## Quando usar
Quando você quer levar uma resposta do Claude para outro lugar sem selecionar o texto na tela, sobretudo se houver código.

## Observação
Com N, copia a N-ésima resposta mais recente; no seletor, w grava a escolha em arquivo. Documentado na referência oficial.

## O que acontece no fluxo do prompt e do motor
1. Claude já respondeu.
2. Você digita /copy.
3. Escolhe a N-ésima resposta.
4. Abre seletor se houver código.
5. Texto na área de transferência.

## Exemplos
- /copy: copia a última resposta inteira para a área de transferência.
- /copy 2: copia a penúltima resposta, a anterior à última.
- /copy: com blocos de código na resposta, o seletor aparece para escolher o que levar.

## Comandos relacionados
- /code-review: caçar bugs no diff atual.

## Armadilhas
- Com código, o seletor aparece.
- N conta a partir da última.

Documentação: https://code.claude.com/docs/en/commands#all-commands
