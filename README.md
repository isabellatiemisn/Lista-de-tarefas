# Lista de Tarefas

Programa de terminal feito em Python para organizar tarefas do dia a dia. Permite adicionar, listar, editar, concluir e remover tarefas, além de organizá-las por categoria e acompanhar a data de criação de cada uma — tudo pelo terminal mesmo, sem interface gráfica.
Esse foi um dos meus primeiros projetos próprios, feito para aplicar na prática o que venho aprendendo no curso de Análise e Desenvolvimento de Sistemas.

## Funcionalidades

  - Adicionar uma ou várias tarefas seguidas, sem precisar voltar ao menu a cada uma
  - Listar todas as tarefas cadastradas, numeradas
  - Marcar uma ou várias tarefas como concluídas, seguidas
  - Remover uma ou várias tarefas, seguidas
  - Tratamento de erros para entradas inválidas, como texto no lugar de número ou lista vazia
  - Salvamento automático em arquivo (JSON) a cada alteração, para que as tarefas não se percam ao fechar o programa
  - Ao iniciar, se já existir uma lista salva, o programa pergunta se você quer continuar com ela ou começar do zero
  - Editar o texto de uma tarefa já criada, mantendo o status de concluída se ela já estava marcada
  - Cada tarefa registra automaticamente a data de criação
  - Categorização das tarefas: escolha uma categoria já existente, crie uma nova, ou deixe sem categoria

## Tecnologias usadas

  - Python 3

## Detalhes técnicos

Cada tarefa é armazenada como um dicionário, contendo texto, status de conclusão, categoria e data de criação. 
O arquivo de persistência guarda tarefas e categorias juntos, numa estrutura combinada, o que facilita expansões futuras (como um banco de dados relacional).
  
## Como rodar

  1. Certifique-se de ter o Python 3 instalado na sua máquina
  2. Copie este repositório ou baixe o arquivo `lista_de_tarefas.py`
  3. No terminal, navegue até a pasta onde o arquivo está salvo
  4. Execute o comando: " python lista_de_tarefas.py "
  5. Siga as instruções do menu exibido na tela

## Exemplo de uso
```
1 Adicionar uma tarefa
2 Listar todas as tarefas
3 Marcar uma tarefa como concluída
4 Remover uma tarefa
5 Editar tarefa
6 Sair do programa
Escolha uma das ações acima: 1
Adicione uma tarefa (ou 'sair' para voltar): Estudar Python
Adicione uma tarefa (ou 'sair' para voltar): sair
```

## Próximos passos

  - Permitir editar categorias
  - Adicionar opção de configurações, para escolher o que aparece na listagem (data, categoria)
  - Adicionar opção de busca/filtro de tarefas (por texto, categoria ou status)
  - Migrar o armazenamento de arquivo JSON para um banco de dados SQLite
  - Futuramente, criar uma interface gráfica, substituindo o terminal
  - Reescrever o projeto em Java, como exercício de fixação de lógica em outra linguagem
    
## Autor

Feito por Isabella Tiemi S. N. como projeto de portfólio, aplicando conceitos aprendidos no curso de Análise e Desenvolvimento de Sistemas (ADS).

[LinkedIn](https://www.linkedin.com/in/isabella-tiemi-sn/) - [GitHub](https://github.com/isabellatiemisn)
