# /doctor: descrição completa

Categoria: Diagnóstico e uso. Tipo: skill embutida do Claude Code.

## O que faz
Faz um check-up da sua instalação e corrige problemas: saúde da instalação, extensões sem uso, arquivos de memória duplicados ou inchados, hooks lentos, atualizações e permissões. O Claude apresenta os achados primeiro e pede confirmação antes de mudar qualquer coisa.

## Por que usar
Junta num só lugar o que normalmente se descobre aos poucos quando algo fica lento ou estranho.

## Como usar
Rode /doctor ou o apelido /checkup. Segundo a documentação, /doctor prompt-audit audita as suas instruções em vez de fazer o check-up. Se não aparecer no menu do app, abra claude no painel Terminal e rode lá.

## Quando usar
Quando algo fica estranho sem motivo claro, como o app lento, um hook que demora, um aviso de versão ou memórias repetidas. Também logo depois de atualizar o app.

## Observação
Na lista do modo Desktop, o comando aparece marcado como comando de terminal.

## O que acontece no fluxo do prompt e do motor
1. Você digita /doctor.
2. O motor confere a instalação.
3. Ele confere extensões, arquivos de memória e permissões.
4. Ele mostra os achados e pede confirmação.
5. As correções confirmadas são aplicadas.

## Exemplos
- /doctor: check-up completo com sugestões de correção.
- /checkup: mesmo comando pelo apelido.
- /doctor: rode depois de atualizar o app para ver se sobrou algo da versão anterior.

## Comandos relacionados
- /color: cor da barra de prompt da sessão.
- /reload-plugins: ativar plugins sem abrir outra sessão.

## Armadilhas
- Pode não aparecer no menu do app; nesse caso, rode pelo terminal.
- No modo Desktop, o comando é marcado como terminal.

Documentação: https://code.claude.com/docs/en/skills#check-your-setup-with-/doctor
