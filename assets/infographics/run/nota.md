# /run: descrição completa

Categoria: Automação. Tipo: skill embutida do Claude Code.

## O que faz
Inicia o app do projeto e o conduz para mostrar uma mudança funcionando de verdade, além dos testes.

## Por que usar
Teste verde não garante que a tela abre. O /run sobe o app e mostra o resultado real, inclusive com captura de tela.

## Como usar
Use /run sozinho ou com um pedido do que mostrar.

Parâmetro opcional: [pedido], texto livre. Diz o que abrir, clicar ou conferir no app.

## Quando usar
Depois de mudar algo visível, como uma tela, um painel ou uma CLI, quando teste verde não basta e você quer ver o app de verdade.

## O que acontece no fluxo do prompt e do motor
1. Você digita /run com o pedido.
2. Claude descobre como subir o app, pelo tipo de projeto e pelo README.
3. Claude sobe e conduz o app.
4. Claude confere a mudança no app.
5. Você vê a mudança funcionando.

## Exemplos
- /run: sobe o app do projeto do jeito padrão.
- /run abra a tela de login e tire uma captura: vai direto para a tela que você quer ver.
- /run confirme que o botão Salvar aparece no formulário de cadastro: verifica uma mudança específica no app real.

## Comandos relacionados
- /run-skill-generator: cria ou melhora uma skill por projeto.

## Armadilhas
- Projeto com banco ou build em etapas.
- Inferência pouco confiável em projetos especiais.

Documentação: https://code.claude.com/docs/en/skills#run-and-verify-your-app
