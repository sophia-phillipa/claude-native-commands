# /status: descrição completa

Categoria: Diagnóstico e uso. Tipo: comando embutido do Claude Code.

## O que faz
Abre as configurações na aba Status, com versão, modelo, conta e conectividade. Em uma sessão em segundo plano, a linha Session kind mostra background job · attached ou background job · unattended, conforme haja terminal anexado; nas demais sessões, mostra interactive.

## Por que usar
Ajuda a confirmar a versão, o modelo em uso ou a conectividade quando algo parece errado.

## Como usar
Rode /status. Ele funciona mesmo enquanto o Claude está respondendo.

## Quando usar
Quando algo parece errado e você quer conferir a versão, o modelo, a conta ou a conectividade, inclusive enquanto o Claude está respondendo.

## Observação
Documentado na referência oficial. A doc mostra a aba Status das configurações, com a linha Session kind.

## O que acontece no fluxo do prompt e do motor
1. Você digita /status.
2. A aba Status abre nas configurações.
3. O painel mostra versão, modelo e conta.
4. O painel mostra conectividade e a linha Session kind.
5. Você confere o que parece errado.

## Exemplos
- /status: mostra versão, modelo, conta e conectividade.
- /status: em sessão em segundo plano, a linha Session kind mostra se há terminal anexado.
- /status: pode ser usado enquanto o Claude ainda está respondendo.

## Comandos relacionados
- /doctor: check-up da instalação (mesma categoria, Diagnóstico e uso).

## Armadilhas
- Em segundo plano, não mostra interactive: nessas sessões a linha Session kind mostra background job.

Documentação: https://code.claude.com/docs/en/agent-view
