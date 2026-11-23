# /init: descrição completa

Categoria: Ajustes e permissões. Tipo: comando embutido do Claude Code.

## O que faz
Analisa o código do projeto e cria um arquivo CLAUDE.md com a documentação que o Claude precisa para trabalhar nele.

## Por que usar
Com o CLAUDE.md, toda sessão nova já começa sabendo como o projeto se organiza e como trabalhar nele.

## Como usar
Rode /init sem parâmetros na pasta do projeto. Revise o arquivo antes de fazer o commit.

## Quando usar
No primeiro dia num repositório novo ou recém-clonado, e depois de uma reorganização grande da estrutura do projeto.

## O que acontece no fluxo do prompt e do motor
1. Você roda /init na pasta.
2. O Claude analisa o código.
3. O Claude cria o CLAUDE.md.
4. Sessões novas já começam informadas.

## Exemplos
- /init: cria o CLAUDE.md num projeto novo.
- /init: rode de novo depois de uma mudança grande para comparar com o CLAUDE.md atual.
- /init: rode num repositório que você acabou de clonar, antes da primeira tarefa.

## Comandos relacionados
- /config: Mudar uma configuração pelo nome.

## Armadilhas
- Revise o CLAUDE.md antes do commit.

Documentação: https://code.claude.com/docs/en/memory
