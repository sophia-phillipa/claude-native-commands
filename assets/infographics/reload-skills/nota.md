# /reload-skills: descrição completa

Categoria: Extensões e conexões. Tipo: comando embutido do Claude Code.

## O que faz
Carrega as skills criadas ou alteradas no disco durante a sessão.

## Por que usar
Uma skill nova que não aparece na lista entra na sessão com ele, sem reabrir o Claude Code. Edições em skills já carregadas entram sozinhas.

## Como usar
Rode /reload-skills sem parâmetros.

## Quando usar
Depois de criar uma skill, para chamá-la nesta mesma sessão. Depois de criar uma skill que ainda não aparece na lista.

## Observação
Edições em skills já carregadas entram sozinhas.

## O que acontece no fluxo do prompt e do motor
1. Você digita /reload-skills
2. Motor relê skills do disco
3. Skill nova vale nesta sessão

## Exemplos
- /reload-skills: Depois de criar uma skill, para chamá-la nesta mesma sessão.
- /reload-skills: Depois de criar uma skill que ainda não aparece na lista.
- /context: Em seguida, confira a linha Skills para ver quanto a skill nova custa.

## Comandos relacionados
- /context: Mostra quanto as skills ocupam

## Armadilhas
- Mudança em plugin usa /reload-plugins
- Skill nova pode não aparecer

Documentação: https://code.claude.com/docs/en/skills
