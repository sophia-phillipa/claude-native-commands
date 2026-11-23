# /permissions: descrição completa

Categoria: Ajustes e permissões. Tipo: comando embutido do Claude Code. Alias: /allowed-tools.

## O que faz
Abre um diálogo para ver, adicionar e remover regras de allow, ask e deny por escopo. Ele também gerencia as pastas de trabalho e mostra as negações recentes do modo automático.

## Por que usar
Define quais ações o Claude pode executar sem perguntar, e reduz aprovações repetidas do mesmo comando.

## Como usar
Rode /permissions para abrir o diálogo, ou edite os arquivos de configuração com as regras.

## Quando usar
Quando o Claude pede aprovação repetida para o mesmo tipo de ação, ou quando precisa liberar ou bloquear uma ferramenta de forma permanente.

## Observação
Documentado na referência oficial. A referência também cobre o modo automático e as regras do classificador.

## O que acontece no fluxo do prompt e do motor
1. Você digita /permissions.
2. Abre o diálogo de regras.
3. Você ajusta regras por escopo.
4. Aprovações repetidas diminuem.

## Exemplos
- /permissions: abre o diálogo com as regras de cada escopo.
- /permissions: mostra as ações que o modo automático negou recentemente.
- /permissions: lista as pastas de trabalho que o Claude pode acessar.

## Comandos relacionados
- /config: Mudar uma configuração pelo nome

## Armadilhas
- Aprovar uma ação não cria regra
- Ação aprovada pode ser bloqueada de novo

Documentação: https://code.claude.com/docs/en/auto-mode-config#review-denials
