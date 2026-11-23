# /code-review: descrição completa

Categoria: Revisão de código. Tipo: skill embutida do Claude Code.

## O que faz
Revisa o diff atual, um PR, um branch ou um caminho em busca de bugs de correção, no nível de esforço que você escolher.

## Por que usar
Pega erros antes do commit. O nível controla quantos achados vêm: low traz poucos e certeiros, high e xhigh trazem mais.

## Como usar
Use /code-review <nível> [alvo] [opções]. Sem nível, ele repete o último que você usou.

Parâmetros:
- <nível>: low, medium, high, xhigh ou max. ultra roda uma revisão com vários agentes na nuvem.
- [alvo]: opcional, número de PR, branch ou caminho. Sem alvo, revisa o diff atual.
- --fix: aplica as correções no working tree depois da revisão.
- --comment: publica os achados como comentários no PR.
- --max-findings <n>: limita a quantidade de achados. all mostra todos; default volta ao padrão.

## Quando usar
Logo antes do commit ou de abrir um PR, com o diff ainda pequeno. Em mudanças de segurança, use junto com o /security-review.

## Observação
max e ultra são os mais caros: use só quando precisar.

## O que acontece no fluxo do prompt e do motor
1. Você digita /code-review com nível.
2. Revisão lê o alvo.
3. Revisão busca bugs de correção.
4. Nível controla quantos achados vêm.
5. Achados chegam antes do commit.

## Exemplos
- /code-review high: revisão cuidadosa do que está alterado agora.
- /code-review medium --fix: revisa e já aplica as correções no working tree.
- /code-review high src/cli.py --max-findings 5: só um arquivo, com no máximo cinco achados.

## Comandos relacionados
- /security-review: use junto em mudanças de segurança.

## Armadilhas
- Sem nível, repete o último usado.
- max e ultra são os mais caros.

Documentação: https://code.claude.com/docs/en/code-review-local
