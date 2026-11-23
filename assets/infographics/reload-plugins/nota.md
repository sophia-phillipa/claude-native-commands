# /reload-plugins: descrição completa

Categoria: Extensões e conexões. Tipo: comando embutido do Claude Code.

## O que faz
Ativa na sessão atual as mudanças de plugins que ficaram pendentes, como um plugin instalado, atualizado, ligado ou desligado.

## Por que usar
Sem ele, um plugin novo ou atualizado só passa a valer numa sessão nova, e você perde o contexto acumulado.

## Como usar
Rode /reload-plugins. Se ele avisar que a próxima mensagem vai reler a conversa inteira, rode /reload-plugins --force para aplicar.

Parâmetro opcional: --force. Aplica a recarga mesmo quando ela muda as ferramentas MCP ou a ferramenta LSP.

## Quando usar
Logo depois de instalar, atualizar, ligar ou desligar um plugin no meio de uma sessão longa, quando abrir outra janela faria perder o contexto acumulado.

## Observação
Quando a recarga muda as ferramentas MCP ou a ferramenta LSP, a próxima mensagem relê a conversa inteira, sem usar o cache. Por isso, nesse caso, o comando só aplica com --force. A documentação confirma que também roda no app Desktop. Testado no app: funcionou.

## O que acontece no fluxo do prompt e do motor
1. Você digita /reload-plugins.
2. O motor aplica plugins pendentes.
3. Plugins valem na sessão atual.

## Exemplos
- /reload-plugins: Depois de instalar um plugin, para usá-lo nesta mesma sessão.
- /reload-plugins --force: Quando o comando avisou que a próxima mensagem vai reler a conversa inteira.
- /reload-skills: Para skills soltas no disco, fora de um plugin, use este outro.

## Comandos relacionados
- /reload-skills: recarrega skills soltas no disco, fora de um plugin.

## Armadilhas
- Mudança de MCP relê a conversa inteira.
- Aviso de releitura exige --force.

Documentação: https://code.claude.com/docs/en/plugins/cli-reference#reload-plugins
