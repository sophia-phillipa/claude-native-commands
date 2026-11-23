# /design: descrição completa

Categoria: Criação e referência. Tipo: skill embutida do Claude Code.

## O que faz
Rascunha telas, fluxos, landing pages ou pôsteres como pranchetas (artboards) em uma mesma tela, publicados como artefato do Claude Design. Você edita as pranchetas num navegador no computador, e as mudanças são salvas sozinhas.

## Por que usar
Cada prancheta pode ser exportada em PNG ou PDF.

## Como usar
Digite /design seguido do briefing, como /design tela de configurações para um app de banco digital.

Parâmetro opcional: [brief]. Descrição do que desenhar, como uma tela ou uma landing page.

## Quando usar
Quando você precisa de um rascunho visual de tela, landing page ou pôster antes de codar ou publicar.

## Observação
Exige Claude Code v2.1.265 ou posterior, uma sessão com artefatos disponíveis e uma conta com o template Design liberado. Disponível na API da Anthropic; no Amazon Bedrock, no Google Cloud Agent Platform, no Microsoft Foundry e no Claude Platform on AWS os artefatos não estão disponíveis, e o comando fica indisponível.

## O que acontece no fluxo do prompt e do motor
1. Você digita /design com briefing.
2. O Claude rascunha as pranchetas.
3. Publica o canvas como artefato.
4. Pranchetas prontas para exportar.

## Exemplos
- /design tela de configurações para um app de banco digital: cria as pranchetas da tela de ajustes no mesmo canvas.
- /design landing page de uma loja de cafés: rascunha a página inicial como artefato do Claude Design.
- /design pôster para o evento de lançamento do produto: gera o pôster como prancheta, pronta para exportar em PNG ou PDF.

## Comandos relacionados
- /design consent: concede ao Claude acesso ao Claude Design.
- /design revoke: retira o acesso ao Claude Design.

## Armadilhas
- Exige Claude Code mais novo.
- Não funciona no Amazon Bedrock.

Documentação: https://code.claude.com/docs/en/artifacts#draft-a-design-canvas
