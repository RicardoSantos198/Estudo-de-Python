<H1>🏧Caixa eletrônico em Python</H1>
<br>

<h4>O objetivo foi criar uma aplicação interativa via terminal onde o usuário pudesse gerenciar seu saldo.</h4>
<br>

<h4>Funcionalidades</h4>

- **Consulta de Saldo:** Exibe o valor disponível com formatação de moeda (`R$ 0.00`).<br>
- **Depósito:** Permite adicionar fundos à conta, com validação para impedir valores negativos.<br>
- **Saque com Verificação:** - Bloqueia saques se o valor for superior ao saldo em conta.
  - Bloqueia valores de saque inválidos (menores ou iguais a zero).<br>
- **Menu Persistente:** O programa utiliza um laço de repetição para permitir várias operações sem fechar.
<br>

<h4>Conceitos Utilizados</h4>
<strong>Linguagem: Python 3</strong><br>
-<strong>Estruturas Lógicas:</strong> <br>
    <strong>-while True:</strong> Para manter o sistema rodando.<br>
   <strong>- if / elif / else:</strong> Para o processamento das escolhas do usuário.<br>
    <strong>- try / except (Opcional)</strong>: Para futuras implementações de tratamento de erros.<br>
<strong>- Manipulação de Dados:</strong> Operadores de atribuição composta (`+=` e `-=`) para atualização de saldo em tempo real.
