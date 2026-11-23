# /run-skill-generator: descrição completa

Categoria: Criação e referência. Tipo: skill embutida do Claude Code.

## O que faz
Cria ou melhora uma skill por projeto, a "run", que diz aos agentes como compilar, iniciar e operar o app. Ela vem com um modelo e exemplos para você partir de algo pronto.

## Por que usar
Sem instruções de execução, cada sessão redescobre como subir o app, e erra. Com a skill escrita uma vez, o /run e os agentes já sabem os passos.

## Como usar
Digite /run-skill-generator. Use quando for preparar o projeto, escrever instruções de execução ou conferir que o build e a execução funcionam num ambiente limpo.

## Quando usar
Logo depois de o projeto ficar utilizável, ou quando cada sessão nova gasta tempo descobrindo como subir o app.

## Observação
Só você chama: o Claude não a dispara sozinho. Combina com o /run, que usa a skill gerada.

## O que acontece no fluxo do prompt e do motor
1. Você digita /run-skill-generator.
2. Claude cria a skill.
3. A skill fica no projeto.
4. Agentes já sabem os passos.

## Exemplos
- /run-skill-generator: cria a skill de execução do projeto atual.
- /run-skill-generator revise a skill run: o comando de build mudou: atualiza uma skill existente.
- /run-skill-generator confira se dá para subir o app a partir de um clone novo: valida os passos num ambiente limpo.

## Comandos relacionados
- /run: usa a skill gerada aqui.

## Armadilhas
- Sem ela, cada sessão redescobre o app.

Documentação: https://code.claude.com/docs/en/skills#run-and-verify-your-app
