# /diff: descrição completa

Categoria: Revisão de código. Tipo: comando embutido do Claude Code.

## O que faz
Mostra as alterações na árvore de trabalho (working tree), incluindo as edições que o Claude já fez na sessão.

## Por que usar
Permite conferir o que mudou nos arquivos antes de seguir adiante.

## Como usar
Rode /diff no prompt do Claude Code.

## Quando usar
Antes de aceitar o resultado de uma sessão, para conferir o que mudou na árvore de trabalho.

## Observação
Documentado na referência oficial.

## O que acontece no fluxo do prompt e do motor
1. Claude edita arquivos.
2. Você digita /diff.
3. Lê as mudanças do git.
4. Conta linhas por arquivo.
5. Mostra as mudanças por arquivo.

## Exemplos
- /diff: mostra as alterações feitas até agora nesta sessão.
- /diff: use para revisar o que mudou na árvore de trabalho antes de continuar.
- /diff: lista as edições do Claude junto com as suas mudanças pendentes.

## Comandos relacionados
- /code-review: caçar bugs no diff atual.

## Armadilhas
- Edição em submódulo não aparece.
- Edição por shell não aparece nos turnos.

Documentação: https://code.claude.com/docs/en/interactive-mode#review-changes-with-%2Fdiff
