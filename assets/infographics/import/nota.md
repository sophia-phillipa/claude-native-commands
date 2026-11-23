# /import: descrição completa

Categoria: Ajustes e permissões. Tipo: comando embutido do Claude Code.

## O que faz
Importa configuração de outro agente de código: servidores MCP, comandos de barra, subagentes, skills e instruções. Primeiro ele só varre e lista o que dá para importar.

## Por que usar
Quem usa outra ferramenta não precisa recriar tudo à mão. A importação aplica verificações de nomes e de caminhos seguras, em vez de você copiar arquivos por conta própria.

## Como usar
Rode /import para escanear e listar. A saída informa um código; depois rode /import --yes=<código> para aplicar o que foi listado.

Parâmetro: --yes=<código>. Aplica a importação listada. O código vem da saída do escaneamento.

## Quando usar
Ao trocar de outro agente de código para o Claude Code, para não recriar à mão servidores MCP, skills e instruções.

## Observação
Aparece só em algumas versões e contas. Se o comando não estiver na sua lista, ele não está liberado aí.

## O que acontece no fluxo do prompt e do motor
1. Você digita /import.
2. Acha o que pode importar.
3. Você confirma o que importar.
4. Claude Code recebe a configuração.

## Exemplos
- /import: escaneia e lista o que pode ser importado.
- /import: rode de novo depois de configurar o outro agente, para ver a lista atualizada.
- /import --yes=<código>: aplica a importação, usando o código da listagem.

## Comandos relacionados
- /config: mudar uma configuração pelo nome.

## Armadilhas
- Pode não aparecer na sua lista.

Documentação: https://code.claude.com/docs/en/commands#all-commands
