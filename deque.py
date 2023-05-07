# -*- coding:UTF-8 -*-
from no import No

class Deque:
    def __init__(self, capacidade=5):
        self.__inicio = None
        self.__fim = None
        self.__capacidade = capacidade
        self.__qtdElementos = 0
        print(f"Criada EDD Fila com capacidade: {capacidade}")


    # Verifica se a deque está vazia
    # Retorna True se a deque estiver vazia e False caso contrário
    def is_empty(self) -> bool:
        # implementação do método
       pass


    # Verifica se a deque está cheia
    # Retorna True se a deque estiver cheia e False caso contrário
    def is_full(self) -> bool:
        # implementação do método
        pass
    

    # Insere um elemento no início da deque e retorna True
    # Se a fila estiver cheia, lança uma exceção 
    def add_front(self, valor) -> bool:
        # implementação do método
        pass


    # Insere um elemento no final da deque e retorna True
    # Se a deque estiver cheia, lança uma exceção 
    def add_rear(self, valor) -> bool:
        # implementação do método
        pass


    # Remove um elemento do início da deque e retorna esse elemento
    # Se a deque estiver vazia, lança uma exceção: raise Exception("mensagem de erro")
    def remove_front(self) -> No:
        # implementação do método
        pass
    

    # Remove um elemento do início da deque e retorna esse elemento
    # Se a deque estiver vazia, lança uma exceção: raise Exception("mensagem de erro")
    def remove_rear(self) -> No:
        # implementação do método
        pass
    

    # Retorna o primeiro elemento da deque sem removê-lo
    # Se a deque estiver vazia retorna None
    def peek_front(self) -> No:
        # implementação do método
        pass


    # Retorna o último elemento da deque sem removê-lo
    # Se a deque estiver vazia retorna None
    def peek_rear(self) -> No:
        # implementação do método
        pass
    

    # Retorna uma lista com os valores do atributo dado de cada No
    # da deque na ordem em que os elementos da foram inseridos.
    # Imprime os elementos da deque do primeiro para o último.
    # Caso a deque esteja vazia, imprime uma mensagem informando
    # que a deque está vazia e retorna uma lista vazia
    def display(self) -> list():
        # implementação do método
        pass
    

    # Retorna a quantidade de elementos na deque
    # Se a deque estiver vazia, retorna ZERO
    def size(self) -> int:
        # implementação do método
        pass
