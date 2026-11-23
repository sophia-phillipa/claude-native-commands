# /rename: descrição completa

Categoria: Ajustes e permissões. Tipo: comando embutido do Claude Code.

## O que faz
Muda o nome da conversa atual. O nome é opcional na linha de comando.

## Por que usar
Com várias sessões abertas, nomes como "conversa de ontem" não ajudam. Um nome curto torna fácil achar e retomar a sessão certa depois.

## Como usar
Rode /rename seguido do nome desejado. O apelido /name faz o mesmo.

Parâmetro opcional: [name]. O novo nome da conversa.

## Quando usar
Assim que a sessão ganha um assunto claro, e sempre que você mantém mais de uma conversa aberta e precisa distingui-las na lista depois.

## Observação
A documentação cita o app Desktop entre os lugares onde funciona.

## O que acontece no fluxo do prompt e do motor
1. Você digita /rename.
2. Nome digitado ou gerado.
3. Sessão ganha o novo nome.
4. Nome aparece na barra.

## Exemplos
- /rename migração do banco para Postgres 16: nome claro para achar a sessão na lista.
- /name revisão do PR de login: mesmo comando pelo apelido.
- /rename migração-v2: nomes curtos e sem espaços também funcionam.

## Comandos relacionados
- /config: mudar uma configuração pelo nome.

## Armadilhas
- Nome só com caracteres invisíveis é recusado.

Documentação: https://code.claude.com/docs/en/commands#all-commands
