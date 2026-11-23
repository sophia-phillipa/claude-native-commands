# /sandbox: descrição completa

Categoria: Ajustes e permissões. Tipo: comando embutido do Claude Code.

## O que faz
Liga ou desliga o modo sandbox. Segundo a documentação oficial, o comando só está disponível em plataformas compatíveis.

## Por que usar
Permite trocar o modo sandbox direto na sessão, quando o recurso estiver disponível na plataforma em uso.

## Como usar
Rode /sandbox para alternar o modo. O comando está disponível só em plataformas compatíveis.

## Quando usar
Quer ligar ou desligar o sandbox, numa plataforma compatível.

## Observação
Documentado na referência oficial. Disponível só em plataformas compatíveis. Doc oficial: sandboxing. Só em plataformas compatíveis. Testado no app: funcionou.

## O que acontece no fluxo do prompt e do motor
1. Você digita /sandbox
2. Abre o painel do sandbox
3. Você liga ou desliga
4. Modo sandbox muda de estado

## Exemplos
- /sandbox: alterna o modo sandbox nesta plataforma.
- /sandbox: se a plataforma não for compatível, o comando não está disponível.
- /sandbox: rode de novo para abrir o painel, com as abas Mode, Overrides e Config.

## Comandos relacionados
- /config: Mudar uma configuração pelo nome

## Armadilhas
- Vem desligado por padrão
- Só em plataformas compatíveis
- Windows nativo roda sem sandbox

Documentação: https://code.claude.com/docs/en/sandboxing
