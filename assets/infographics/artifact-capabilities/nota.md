# /artifact-capabilities: descrição completa

Categoria: Extensões e conexões. Tipo: skill embutida do Claude Code.

## O que faz
Carrega a referência dos recursos de execução que um artefato publicado pode usar, como chamar seus conectores ou oferecer um arquivo para download, junto com os recursos que a sua conta tem. Normalmente o Claude a carrega sozinho antes de criar uma página que use um desses recursos.

## Por que usar
Ajuda a conferir o que a conta pode usar antes de a página depender de um conector ou de um download.

## Como usar
Digite /artifact-capabilities quando quiser ver a referência antes de montar a página. Você também pode deixar o Claude carregá-la sozinho.

## Quando usar
Ao montar uma página publicada que precise chamar um conector ou oferecer um arquivo para download, e você quer saber o que a sua conta pode usar.

## Observação
Documentado na referência oficial. Disponível onde os artefatos estão disponíveis. Testado no app: funcionou.

## O que acontece no fluxo do prompt e do motor
1. Você digita /artifact-capabilities.
2. O motor carrega a referência.
3. Motor inclui recursos da conta.
4. Recursos da conta ficam conferidos.

## Exemplos
- /artifact-capabilities: carrega a referência dos recursos que a página pode usar.
- /artifact-capabilities: mostra quais recursos a sua conta tem disponíveis.
- /artifact-capabilities: consulta a referência antes de criar uma página que chama um conector.

## Comandos relacionados
- /mcp: gerenciar servidores MCP.

## Armadilhas
- Só vale para páginas publicadas.

Documentação: https://code.claude.com/docs/en/commands#all-commands
