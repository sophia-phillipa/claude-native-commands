# /usage-credits: descrição completa

Categoria: Diagnóstico e uso. Tipo: comando embutido do Claude Code.

## O que faz
Configura créditos de uso ou os pede ao administrador quando você bate num limite.

## Por que usar
Evita ficar parado esperando o limite renovar: com créditos ligados, o trabalho continua, e o pedido ao administrador sai sem você procurar o painel.

## Como usar
Rode /usage-credits sem parâmetros e siga as opções que aparecerem.

## Quando usar
Quando um limite do plano interrompe um trabalho que precisa continuar hoje.

## Observação
Depende do tipo de conta: no app só aparece em contas que têm esse recurso. A referência oficial diz que o comando exige entrar com a assinatura do claude.ai e não funciona com autenticação por chave de API. Quem não tem acesso ao faturamento envia um pedido ao administrador, depois de confirmar.

## O que acontece no fluxo do prompt e do motor
1. Você bate no limite do plano.
2. Você digita /usage-credits.
3. O comando abre as opções de créditos.
4. Os créditos ficam ligados ou o pedido segue ao administrador.

## Exemplos
- /usage-credits: abre a configuração de créditos.
- /usage: antes de tudo, veja quanto do plano já foi usado.
- /usage-credits: depois de bater no limite, peça créditos ao administrador.

## Comandos relacionados
- /usage: mostra quanto do plano já foi usado.

## Armadilhas
- Não aparece com chave de API.
- Depende do tipo de conta.

Documentação: https://code.claude.com/docs/en/costs#add-usage-credits-to-your-subscription
