# /claude-api: descrição completa

Categoria: Criação e referência. Tipo: skill embutida do Claude Code.

## O que faz
Uma skill com a referência da API da Claude e do SDK da Anthropic: ids de modelos, preços, parâmetros, streaming, uso de ferramentas, MCP, agentes, cache de prompt, contagem de tokens e migração entre modelos.

## Por que usar
Evita que o Claude responda de memória sobre modelos e preços, que mudam. Com a skill carregada, ele consulta a referência antes de escrever o código ou de explicar um limite.

## Como usar
Digite /claude-api seguido da pergunta ou da tarefa. Ela também é acionada sozinha quando a conversa fala de Claude, Anthropic ou de um app com LLM.

## Quando usar
Ao construir ou depurar um app que usa a API da Claude, e ao trocar de modelo ou calcular custo, quando o número tem que estar certo.

## Observação
Ela libera a consulta ao domínio platform.claude.com para buscar a documentação. Pode ser desligada pela configuração de skills embutidas.

## O que acontece no fluxo do prompt e do motor
1. Você digita /claude-api com a pergunta ou a tarefa.
2. Claude carrega a referência da API.
3. A resposta usa a referência, no lugar da memória.

## Exemplos
- /claude-api como ligo o cache de prompt no meu chatbot em Python?: passo a passo com o SDK, usando a referência.
- /claude-api qual a diferença de preço entre os modelos atuais?: consulta a tabela em vez de chutar.
- /claude-api migrar meu código do modelo antigo para o mais novo: lista o que muda em parâmetros e comportamento.

## Comandos relacionados
- /design-sync: Enviar seu design system ao Claude Design.

## Armadilhas
- Pode ser desligada pela configuração de skills embutidas.

Documentação: https://code.claude.com/docs/en/skills#work-on-claude-api-projects
