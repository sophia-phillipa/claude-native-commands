# /verify: descrição completa

Categoria: Revisão de código. Tipo: skill embutida do Claude Code.

## O que faz
Confere se uma mudança no código faz o que deveria: constrói o app, roda e observa o resultado.

## Por que usar
Confirma a mudança construindo e rodando o app, em vez de depender só de testes ou checagens de tipo.

## Como usar
Digite /verify depois da mudança. A skill constrói e roda o app e descreve o que observou.

## Quando usar
Depois de mudar o código, quando os testes e as checagens de tipo passam, mas você ainda não viu o app funcionando.

## Observação
Aparece no menu do app (vídeo de 22/11/2026); ainda não testado. Descrição oficial na tabela de comandos.

## O que acontece no fluxo do prompt e do motor
1. Você muda o código.
2. Você digita /verify.
3. A skill constrói o app.
4. A skill roda o app.
5. Você vê se funciona.

## Exemplos
- /verify: depois de ajustar um formulário, confirma que ele envia os dados como deveria.
- /verify: depois de corrigir um erro de inicialização, sobe o app e vê se ele abre.
- /verify: antes de dar uma tarefa por pronta, checa o resultado rodando o app.

## Comandos relacionados
- /code-review: caçar bugs no diff atual.

## Armadilhas
- Sem receita, grava em SKILL.md.
- Só testes e tipos não bastam.

Documentação: https://code.claude.com/docs/en/commands#all-commands
