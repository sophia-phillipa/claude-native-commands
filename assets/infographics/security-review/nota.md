# /security-review: descrição completa

Categoria: Revisão de código. Tipo: comando embutido do Claude Code.

## O que faz
Faz uma revisão de segurança completa das mudanças pendentes no branch atual e entrega um relatório em markdown.

## Por que usar
Usa subtarefas em paralelo para filtrar falsos positivos e descarta achados com confiança abaixo de 8 em 10.

## Como usar
Rode /security-review sem parâmetros, num branch com mudanças ainda não integradas.

## Quando usar
Antes de abrir um PR que mexe em login, tokens, cookies, entrada de usuário ou chamadas a serviços externos.

## O que acontece no fluxo do prompt e do motor
1. Você digita /security-review.
2. O motor lê o diff.
3. O motor busca riscos.
4. Riscos aparecem para você.

## Exemplos
- /security-review: relatório de riscos das mudanças pendentes.
- /security-review: rode antes de abrir um PR que mexe em login, tokens ou entrada de usuário.
- /security-review: rode de novo depois das correções para confirmar que os achados sumiram.

## Comandos relacionados
- /code-review: use junto em mudanças de segurança.

## Armadilhas
- Sem remoto origin, a revisão falha.

Documentação: https://code.claude.com/docs/en/commands#all-commands
