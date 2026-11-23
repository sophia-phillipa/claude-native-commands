# /review: descrição completa

Categoria: Revisão de código. Tipo: alias do /code-review.

## O que faz
No app, /review é enviado para /code-review, que revisa o diff atual.

## Por que usar
Quem conhece o nome antigo encontra o comando atual sem procurar.

## Como usar
Use /code-review, que é o nome atual. Com /review você chega ao mesmo comando.

## Quando usar
Quando você lembra do nome antigo e quer revisar o diff antes de entregar.

## Observação
Alias de /code-review; as regras de nível e flags estão na página de revisão local. Testado no app: vai para /code-review. No app aparece como /code-review (review).

## O que acontece no fluxo do prompt e do motor
1. Você digita /review.
2. O app envia para /code-review.
3. /code-review revisa o diff atual.

## Exemplos
- /review: Revisa o diff atual, como o /code-review.
- /code-review: Nome atual do mesmo comando.
- /review 1234: Revisa um PR pelo número, como o /code-review com PR.

## Comandos relacionados
- /code-review: Nome atual do mesmo comando.

## Armadilhas
- No app, aparece /code-review (review).
- Nível e flags ficam no /code-review.

Documentação: https://code.claude.com/docs/en/code-review-local
