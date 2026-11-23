# /slides: descrição completa

Categoria: Criação e referência. Tipo: skill embutida do Claude Code.

## O que faz
Cria uma apresentação nova como artefato do Claude Slides, preenchida a partir do seu resumo. Como o recurso depende da conta e da plataforma, o comando pode não aparecer.

## Por que usar
Gera um primeiro rascunho de apresentação a partir de uma descrição curta, sem montar os slides do zero.

## Como usar
Rode /slides seguido do resumo do que a apresentação deve cobrir, por exemplo /slides revisão trimestral da equipe de plataforma.

Parâmetro opcional: [brief]. O assunto ou o resumo da apresentação.

## Quando usar
Quando você precisa de um primeiro rascunho de apresentação a partir de um resumo, e a conta tem o recurso de artefatos.

## Observação
Exige o Claude Code 2.1.265 ou mais novo, uma sessão com artefatos disponíveis e uma conta com o template de slides. Disponível na API da Anthropic; não está disponível no Amazon Bedrock, no Google Cloud (Agent Platform), no Microsoft Foundry nem no Claude Platform on AWS.

## O que acontece no fluxo do prompt e do motor
1. Você digita /slides com resumo.
2. O Claude preenche os slides.
3. Cria a apresentação como artefato.
4. Primeiro rascunho da apresentação.

## Exemplos
- /slides uma revisão trimestral da equipe de plataforma: monta uma apresentação nova com esse tema.
- /slides resultados do primeiro semestre para a diretoria: cria a apresentação a partir desse resumo.
- /slides: só aparece se a conta e a sessão tiverem o recurso de artefatos.

## Comandos relacionados
- /design-sync: enviar seu design system ao Claude Design.

## Armadilhas
- Exige Claude Code mais novo.
- Depende do template de slides na conta.

Documentação: https://code.claude.com/docs/en/commands#all-commands
