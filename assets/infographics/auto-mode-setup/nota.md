# /auto-mode-setup: descrição completa

Categoria: Ajustes e permissões. Tipo: comando embutido do Claude Code.

## O que faz
Descreve o seu ambiente para o modo auto e permite ajustar as regras do que ele aprova sem perguntar.

## Por que usar
O modo auto decide sozinho o que pode rodar. Conhecendo o ambiente, ele erra menos: pergunta menos o que é normal e barra mais o que é arriscado.

## Como usar
Rode /auto-mode-setup sem parâmetros e siga o assistente.

Parâmetros avançados: --wizard … --propose responde ao assistente de uma vez, com postura, escopo e profundidade, e só propõe as regras. --apply-file <arquivo> aplica um arquivo de regras já revisado, conferido com --expect-sha256.

## Quando usar
Quando o modo auto pede confirmação para coisas que são normais no seu ambiente, ou deixa passar algo que você preferia bloquear.

## Observação
Só aparece com o modo auto disponível na conta.

## O que acontece no fluxo do prompt e do motor
1. Você roda /auto-mode-setup.
2. O assistente descreve o ambiente.
3. Você ajusta as regras.
4. Modo auto erra menos.

## Exemplos
- /auto-mode-setup: abre o assistente de configuração.
- /auto-mode-setup: rode de novo depois de passar a trabalhar numa pasta ou ferramenta nova.
- /auto-mode-setup: rode quando o modo auto começar a perguntar coisas que você sempre aprova.

## Comandos relacionados
- /config: Mudar uma configuração pelo nome.

## Armadilhas
- Só aparece com modo auto na conta.

Documentação: https://code.claude.com/docs/en/auto-mode-config#generate-environment-entries
