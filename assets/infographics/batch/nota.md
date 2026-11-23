# /batch: descrição completa

Categoria: Automação. Tipo: skill embutida do Claude Code.

## O que faz
Pesquisa e planeja uma mudança grande e depois a executa em paralelo com 5 a 30 agentes, cada um num worktree isolado e cada um abrindo o seu PR.

## Por que usar
Serve para mudanças mecânicas em muitos arquivos, como migrações, refatorações e renomeações em massa, que se dividem em partes independentes.

## Como usar
Use /batch <instrução>. Só você consegue chamar: o Claude não o dispara sozinho.

Parâmetro obrigatório: <instrução>, texto livre. A mudança completa que você quer, com o critério de pronto.

## Quando usar
Mudanças grandes, repetitivas e independentes em muitos arquivos, que fariam uma sessão só levar horas. Não serve para partes que dependem umas das outras.

## Observação
É o mais caro do guia: abre muitos agentes e muitos PRs de uma vez. Confira o plano e o custo antes de deixar executar.

## O que acontece no fluxo do prompt e do motor
1. Você digita /batch com a instrução.
2. Claude pesquisa o código e planeja a divisão em partes.
3. Você aprova o plano.
4. Um agente roda em cada parte, em worktrees isolados.
5. Cada agente abre o seu PR ou relata o que aconteceu.

## Exemplos
- /batch troque todos os print() por logging no pacote src/: migração mecânica dividida por arquivo.
- /batch renomeie a função load_cfg para load_config em todos os módulos e testes: renomeação em massa, um PR por área.
- /batch adicione type hints a todas as funções públicas de scripts/: refatoração grande e repetitiva.

## Comandos relacionados
- /usage: custo da sessão e uso do plano.

## Armadilhas
- Muitos agentes e PRs de uma vez.
- Custo alto sem conferir o plano.

Documentação: https://code.claude.com/docs/en/skills#bundled-skills
