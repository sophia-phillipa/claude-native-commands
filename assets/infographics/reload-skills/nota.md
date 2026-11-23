# /reload-skills: descrição completa

Categoria: Extensões e conexões. Tipo: comando embutido do Claude Code.

## O que faz
Carrega as skills criadas ou alteradas no disco durante a sessão.

## Por que usar
Sem ele, uma skill nova ou editada só passa a valer numa sessão nova.

## Como usar
Rode /reload-skills sem parâmetros.

## Quando usar
Logo depois de criar ou editar uma skill no meio da sessão, por exemplo com a skill skill-creator, para usá-la sem abrir outra janela.

## O que acontece no fluxo do prompt e do motor
1. Você digita /reload-skills.
2. O motor relê skills do disco.
3. Skill nova vale nesta sessão.

## Exemplos
- /reload-skills: Depois de criar uma skill, para chamá-la nesta mesma sessão.
- /reload-skills: Depois de mudar a descrição de uma skill, para o Claude ler a versão nova.
- /context: Em seguida, confira a linha Skills para ver quanto a skill nova custa.

## Comandos relacionados
- /context: mostra quanto as skills ocupam.

## Armadilhas
- Mudança em plugin usa /reload-plugins.
- Skill nova pode não aparecer.

Documentação: https://code.claude.com/docs/en/skills
