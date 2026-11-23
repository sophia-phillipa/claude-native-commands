# /config: descrição completa

Categoria: Ajustes e permissões. Tipo: comando embutido do Claude Code.

## O que faz
Muda uma configuração do Claude Code no formato chave=valor. Sozinho, sem interface (claude -p), lista as chaves aceitas e os valores de cada uma.

## Por que usar
Ajusta dicas, tema, editor, formato da hora e outras opções na hora, sem abrir arquivos de configuração.

## Como usar
Use /config chave=valor. Dá para passar vários pares de uma vez.

Parâmetros: (sem nada) lista as chaves aceitas e os valores de cada uma; chave=valor é uma configuração, como tips=false, turnDuration=true ou verbose=true; [chave=valor …] são vários pares separados por espaço, aplicados juntos.

## Quando usar
Quando um detalhe do dia a dia incomoda, como dicas que se repetem ou a falta do tempo de cada resposta, e você quer ajustar na hora sem procurar o arquivo de configuração.

## Observação
A mudança fica salva nas configurações, não só nesta sessão. Para desfazer, rode a mesma chave com o valor anterior. Chaves como permissionMode e autoCompact mudam o comportamento de todas as sessões: confira antes de trocar. Na aba Code do app, o /config sozinho abre as Configurações.

## O que acontece no fluxo do prompt e do motor
1. Você digita /config chave=valor.
2. O motor grava o valor.
3. Ajuste fica salvo nas configurações.

## Exemplos
- /config: sem interface, lista as chaves aceitas. Na aba Code, a documentação diz que abre as Configurações.
- /config tips=false turnDuration=true: dois ajustes de uma vez, tira as dicas e mostra quanto durou cada resposta.
- /config verbose=true: mostra mais detalhes de cada passo. Desfaça com verbose=false.

## Comandos relacionados
- /update-config: uma skill que edita o settings.json do Claude Code por você.

## Armadilhas
- Mudança fica salva, não só nesta sessão.
- Confira antes de mudar valores globais.

Documentação: https://code.claude.com/docs/en/settings
