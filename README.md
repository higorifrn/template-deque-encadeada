# 1. Propósito
---
Esta tarefa tem os seguintes propósitos:
- Desenvolver as habilidades de criação e manipulação de estruturas de dados do tipo deque;
- Implementar e validar os conceitos relacionados ao métodos de esturas de dados deque.

# 2. Orientações
---

As subsessões a seguir orientam sobre o uso de soluções as quais poderão auxiliar na realização dessa tarefa, bem como os aspectos gerais relativos à implementação (código fonte) da sua solução.

## 2.1. Instalação do framework pytest
---
A estrutura do código fonte está montada para ser validada com a framework pytest, o qual poderá ser instalado com o comando:

```console
$ pip install pytest
```

Você não está obrigado a instalar o pytest e rodar os testes de validação antes do envio da tarefa, entretanto pode ser bastante útil para que você consiga identificar onde estão os pontos de falhas no seu projeto.

Para realizar um teste de validação de todos os métodos da sua implementação, basta executar o seguinte comando:

```console
$ pytest test/test_deque.py -v
```

O pytest permite que você realize o teste em métodos específicos. Portanto, também é válido o comando:

```console
$ pytest test/test_deque.py -k is_empty -v --no-header
```
A opção -k is_empty avaliará apenas os métodos dentro do arquivo test/test_deque.py que contenham a string "is_empty" no nome do método. No caso de todos os testes serem aprovados, o resultado de saída no terminal deverá ser algo como mostrado em: 

```console
$ pytest test/test_deque.py -k is_empty -v --no-header
================================================== test session starts ==================================================
collected 29 items / 27 deselected / 2 selected                                                                         

test/test_deque.py::test_is_empty_true PASSED                                                                     [ 50%]
test/test_deque.py::test_is_empty_false PASSED                                                                    [100%]

=========================================== 2 passed, 27 deselected in 0.02s ============================================
```

No caso de algum dos testes sobre o método falhar, o resultado de saída no terminal poderá ser algo como mostrado em: 

```console
$ pytest test/test_deque.py -k is_empty -v --no-header
================================================== test session starts ==================================================
collected 29 items / 27 deselected / 2 selected                                                                                

test/test_deque.py::test_is_empty_true PASSED                                                                      [ 50%]
test/test_deque.py::test_is_empty_false FAILED                                                                     [100%]

======================================================== FAILURES =======================================================
__________________________________________________ test_is_empty_false __________________________________________________

    def test_is_empty_false():
    
        try:
            exists = os.path.exists("deque.py")
            assert exists == True
        except:
            sys.exit()
    
        deque = Deque(3)
        deque.add_rear(1)
        deque.add_rear(2)
    
        result = deque.is_empty()
        expected = False
    
>       assert result == expected and deque.size() == 2
E       assert (True == False)

test/test_deque.py:42: AssertionError
-------------------------------------------------- Captured stdout call -------------------------------------------------
Criada EDD Deque com capacidade: 3
Item (Dado: 1) inserido no início da EDD Deque!
Item (Dado: 2) inserido no início da EDD Deque!
================================================ short test summary info ================================================
FAILED test/test_deque.py::test_is_empty_false - assert (True == False)
======================================= 1 failed, 1 passed, 27 deselected in 0.06s ======================================
```

Para mais detalhes e informações sobre o framework consultar no [link](https://docs.pytest.org/en/7.3.x/contents.html).

## 2.2. Implementação da solução
---

Você deverá implementar os **métodos da classe Fila** no arquivo **deque.py**, os quais ainda não foram implementados. Esteja atento ao tipo de retorno de cada método, pois isso irá impactar diretamente na avaliação da sua solução após você enviar o commit com as suas implementações para o repositório remoto.

Após concluir a tarefa, você deverá realizar um **git push** para entregar a sua atividade. Você poderá realizar tantos envios ao repositório remoto quanto desejar. Entretanto, esteja atento ao prazo de entreda da atividade para não realizar a entrega com atraso, pois isso irá impactar sobre a nota da atividade. 

Os testes de validação da pontuação realizados pelo GitHub-Classroom não ocorrem imediatamente após o envio do push para o servidor. Normalmente, o GitHub levará o tempo de alguns segundos para realizar o teste sobre a solução enviada por você. Você deverá atualizar a página no GitHub-Classroom a cada 10s, caso não perceba a mudança no resultado da pontuação, até que o GitHub faça o computo dos seus pontos a partir da execução dos testes sobre a sua entrega.

Esteja atento aos tipos de retorno de cada método, os quais se encontram descritos com _type hint_ no próprio método.

## 2.3. Prazo de entrega
---

O prazo de entrega encontra-se descrito no ambiente do Google Sala de Aula da turma e também do GitHub Classroom.


# 3. Tarefas
---

Segue a relação de tarefas a serem observadas na implementação de cada método e a respectiva pontuação do método destacada em parênteses. Toda a tarefa valerá **20pts**, o que corresponde a **20%** da nota da primeira etapa.

- [x] Estudar e analizar os conceitos e técnicas para implementação da estrutura de dados do tipo deque
- [ ] **(1pts)** Implementar o método **is_empty()**
  - [ ] Deve retornar um boolean True se não houver itens (Nó) na deque ou False, caso contrário
- [ ] **(1pts)** Implementar o método **is_full()**
  - [ ] Deve retornar um boolean True se houver itens (Nó) na deque ou False, caso contrário
- [ ] **(3pts)** Implementar o método **add_front()**, o qual deve receber como entrada um valor para criar um nó que deverá ser inserido no início da deque
  - [ ] Criar um objeto Nó a partir do valor recebido pelo método
  - [ ] Deve retornar um boolean True se conseguir inserir um item (Nó) no início da deque
  - [ ] Caso a deque tenha alcançado a sua capacidade máxima deverá lançar uma Exception com uma mensagem de erro relativo ao ocorrido, senão o item (Nó) deve ser inserido no início da deque e método deverá retornar um boolean True
- [ ] **(3pts)** Implementar o método **add_rear()**, o qual deve receber como entrada um valor para criar um nó que deverá ser inserido no final da deque
  - [ ] Criar um objeto Nó a partir do valor recebido pelo método
  - [ ] Deve retornar um boolean True se conseguir inserir um item (Nó) no final da deque
  - [ ] Caso a deque tenha alcançado a sua capacidade máxima deverá lançar uma Exception com uma mensagem de erro relativo ao ocorrido, senão o item (Nó) deve ser inserido no final da deque e método deverá retornar um boolean True
- [ ] **(3pts)** Implementar o método **remove_front()**, o qual deve retornar o primeiro item (Nó) da deque e remover esse item da deque
  - [ ] Caso a deque esteja vazia deverá lançar uma Exception com uma mensagem de erro
  - [ ] Caso a deque possua um ou mais itens, o primeiro item (Nó) da deque deve ser removido e em seguida retornado pelo método
- [ ] **(5pts)** Implementar o método **remove_rear()**, o qual deve retornar o último item (Nó) da deque e remover esse item da deque
  - [ ] Caso a deque esteja vazia deverá lançar uma Exception com uma mensagem de erro
  - [ ] Caso a deque possua um ou mais itens, o último item (Nó) da deque deve ser removido e em seguida retornado pelo método
- [ ] **(1pts)** Implementar o método **peek_front()**, o qual deve retornar o primeiro item (Nó) da deque SEM remover esse item da deque
  - [ ] Caso a deque esteja vazia deverá retornar um None
  - [ ] Caso a deque possua um ou mais itens, o primeiro item (Nó) inserido na deque deve ser retornado pelo método
- [ ] **(1pts)** Implementar o método **peek_rear()**, o qual deve retornar o último item (Nó) da deque SEM remover esse item da deque
  - [ ] Caso a deque esteja vazia deverá retornar um None
  - [ ] Caso a deque possua um ou mais itens, o último item (Nó) inserido na deque deve ser retornado pelo método
- [ ] **(1pts)** Implementar o método **display()**, o qual deve retornar uma lista com os valores (atributo dado) dos itens (Nó) inseridos na deque
  - [ ] Caso a deque esteja vazia deverá retornar uma lista vazia []
  - [ ] Caso a deque possua um ou mais itens, o primeiro elemento da lista deve ser o valor do dado do primeiro item (Nó) na deque, seguido das demais valores que compõem a deque (do primeiro ao último), nessa ordem
- [ ] **(1pts)** Implementar o método **size()**, o qual deve retornar um int
  - [ ] O método deverá retornar ZERO, caso a deque esteja vazia, ou, caso possua algum item na deque, o valor relativo à quantidade de itens presentes na deque