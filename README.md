# Lista de Tarefas

Programa de terminal feito em Python para organizar tarefas do dia a dia. Dá pra adicionar, listar, marcar como concluída e remover tarefas, tudo pelo terminal mesmo, sem interface gráfica.
Esse foi um dos meus primeiros projetos próprios, feito para aplicar na prática o que venho aprendendo no curso de Análise e Desenvolvimento de Sistemas.

## Funcionalidades

  - Adicionar uma ou várias tarefas seguidas, sem precisar voltar ao menu a cada uma
  - Listar todas as tarefas cadastradas, numeradas
  - Marcar uma tarefa como concluída
  - Remover uma tarefa
  - Tratamento de erros para entradas inválidas, como texto no lugar de número ou lista vazia
  - Salvamento automático em arquivo (JSON) a cada alteração, para que as tarefas não se percam ao fechar o programa
  - Ao iniciar, se já existir uma lista salva, o programa pergunta se você quer continuar com ela ou começar do zero

## Tecnologias usadas

  - Python 3

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
5 Sair do programa
Escolha uma das ações acima: 1
Adicione uma tarefa (ou 'sair' para voltar): Estudar Python
Adicione uma tarefa (ou 'sair' para voltar): sair
```

## Próximos passos

  - Permitir marcar ou remover várias tarefas de uma vez, seguindo a mesma lógica já usada para adicionar
  - Permitir editar o texto de uma tarefa já criada
  - Guardar a data de criação de cada tarefa
  - Adicionar categorias às tarefas (ex.: Faculdade, Pessoal, Trabalho), com opção de listar por categoria
  - Futuramente, criar uma interface gráfica (com tkinter), substituindo o terminal
  - Reescrever o projeto em Java, como exercício de fixação de lógica em outra linguagem
    
## Autor

Feito por Isabella Tiemi S. N. como projeto de portfólio, aplicando conceitos aprendidos no curso de Análise e Desenvolvimento de Sistemas (ADS).

[LinkedIn](https://www.linkedin.com/in/isabella-tiemi-sn/) - [GitHub](https://github.com/isabellatiemisn)
