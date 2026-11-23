# /ultrareview: descrição completa

Categoria: Revisão de código. Tipo: comando embutido do Claude Code.

## O que faz
Faz uma revisão de código profunda, com vários agentes, num sandbox na nuvem. Com uma referência de PR, revisa aquele pull request; com uma branch ou commit, muda a base da comparação.

## Por que usar
Dá uma revisão mais profunda que a comum, feita fora da sua máquina, para alterações grandes antes do merge.

## Como usar
Rode /ultrareview sozinho ou seguido de um PR, uma branch ou um commit. A forma preferida pela referência é /code-review ultra.

Parâmetro opcional: [PR ou branch]. Um PR para revisar, ou a branch ou commit base da comparação.

## Quando usar
Quando uma alteração grande merece uma revisão mais profunda que a comum antes de um merge.

## Observação
/ultrareview é alias de /code-review ultra.

## O que acontece no fluxo do prompt e do motor
1. Você digita /ultrareview.
2. Opcional: PR ou base.
3. Sandbox recebe o repositório.
4. Agentes revisam e verificam bugs.
5. Achados voltam à sua sessão.

## Exemplos
- /ultrareview: inicia a revisão profunda em sandbox na nuvem, sem indicar PR nem branch.
- /ultrareview 482: revisa o pull request de número 482.
- /ultrareview main: muda a base da comparação para a branch main.

## Comandos relacionados
- /code-review: caça bugs no diff atual.

## Armadilhas
- Diff grande demais é recusado.
- Revisão parada não traz achados.

Documentação: https://code.claude.com/docs/en/ultrareview
