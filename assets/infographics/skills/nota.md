# /skills: descrição completa

Categoria: Extensões e conexões. Tipo: comando embutido do Claude Code.

## O que faz
Lista as skills disponíveis. Você filtra digitando parte do nome, da descrição ou da origem, ordena pelo número de tokens com a tecla t e alterna a visibilidade de cada skill para o Claude e para o menu /.

## Por que usar
Mostra quais skills o Claude enxerga e quanto cada uma pesa em tokens, antes de você decidir esconder alguma.

## Como usar
Rode /skills, digite para filtrar, pressione t para ordenar por tokens e Espaço ou Enter para alternar a visibilidade. Esc salva e fecha.

## Quando usar
Quando a lista de skills ficou longa e você quer filtrar, ordenar por tokens ou esconder algumas do Claude e do menu /.

## Observação
Documentado na referência oficial. Skills de plugin e certas skills não podem ter a visibilidade alterada.

## O que acontece no fluxo do prompt e do motor
1. Você digita /skills.
2. O motor lista skills disponíveis.
3. Espaço alterna a visibilidade.
4. Visibilidade fica salva.

## Exemplos
- /skills: Abre a lista de skills disponíveis.
- /skills: Digite parte do nome de uma skill para filtrar a lista.
- /skills: Pressione t para ordenar pelo número de tokens de cada uma.

## Comandos relacionados
- /mcp: gerenciar servidores MCP.

## Armadilhas
- Skill de plugin não muda aqui.

Documentação: https://code.claude.com/docs/en/skills
