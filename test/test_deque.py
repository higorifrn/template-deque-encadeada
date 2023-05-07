# ATENÇÃO: Não altere o código de arquivo
import os.path
import sys
from pytest import raises
from no import No
from deque import Deque

# ---- INÍCIO: teste método is_empty()

def test_is_empty_true():

    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()

    result = deque.is_empty()
    expected = True

    assert result == expected and deque.size() == 0


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

    assert result == expected and deque.size() == 2

# ---- FIM: teste método is_empty()


# ---- INÍCIO: teste método is_full()

def test_is_full_true():

    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque(1)
    deque.add_rear(1)

    result = deque.is_full()
    expected = True

    assert result == expected and deque.size() == 1


def test_is_full_false():

    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque(3)
    deque.add_front(1)
    deque.add_front(2)

    result = deque.is_full()
    expected = False

    assert result == expected and deque.size() == 2

# ---- FIM: teste método is_full()


# ---- INÍCIO: teste método add_front()

def test_add_front_em_deque_cheia():

    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque(1)

    deque.add_front(1)

    assert deque.peek_front().dado == 1
    with raises(Exception):
        deque.add_front(2) # deve gerar erro


def test_add_front_em_deque_vazia():

    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()

    assert deque.add_front(2) == True and deque.peek_front().dado == 2


def test_add_front_em_deque_nao_cheia():

    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque(3)

    deque.add_front(1)
    assert deque.peek_front().dado == 1
    deque.add_front(2)
    assert deque.peek_front().dado == 2
    
# ---- FIM: teste método add_front()


# ---- INÍCIO: teste método add_rear()

def test_add_rear_em_deque_cheia():

    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque(1)

    deque.add_rear(1)

    assert deque.peek_rear().dado == 1
    with raises(Exception):
        deque.add_rear(2) # deve gerar erro


def test_add_rear_em_deque_vazia():

    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()

    assert deque.add_rear(2) == True and deque.peek_rear().dado == 2


def test_add_rear_em_deque_nao_cheia():

    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque(3)

    deque.add_rear(1)
    assert deque.peek_rear().dado == 1
    deque.add_rear(2)
    assert deque.peek_rear().dado == 2
    
# ---- FIM: teste método add_rear()


# ---- INÍCIO: teste método remove_front()

def test_remove_front_em_deque_sem_itens():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()

    with raises(Exception):
        deque.remove_front() # deve gerar erro


def test_remove_front_em_deque_com_itens():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            deque.add_rear(item[:-1])

    expected = No('1')
    result = deque.remove_front()

    assert expected.dado == result.dado and deque.peek_front().dado == '2'


def test_remove_front_em_deque_com_itens_ate_esvaziar():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            deque.add_rear(item[:-1])

    for x in range(5):
      deque.remove_front()

    with raises(Exception):
        deque.remove_front() # deve gerar erro

# ---- FIM: teste método remove_front()


# ---- INÍCIO: teste método remove_rear()

def test_remove_rear_em_deque_sem_itens():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()

    with raises(Exception):
        deque.remove_rear() # deve gerar erro


def test_remove_rear_em_deque_com_itens():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            deque.add_front(item[:-1])

    expected = No('1')
    result = deque.remove_rear()

    assert expected.dado == result.dado and deque.peek_rear().dado == '2'


def test_remove_rear_em_deque_com_itens_ate_esvaziar():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            deque.add_rear(item[:-1])

    for x in range(5):
      deque.remove_rear()

    with raises(Exception):
        deque.remove_rear() # deve gerar erro

# ---- FIM: teste método remove_rear()


# ---- INÍCIO: teste método peek_front()

def test_peek_front_em_deque_sem_itens():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()

    assert deque.peek_front() == None


def test_peek_front_em_deque_sem_itens_apos_remove():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()
    deque.add_front(1)
    deque.remove_front()

    assert deque.peek_front() == None


def test_peek_front_em_deque_com_itens():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)

    expected = No(2)
    result = deque.peek_front()

    assert expected.dado == result.dado

# ---- FIM: teste método peek_front()


# ---- INÍCIO: teste método peek_rear()

def test_peek_rear_em_deque_sem_itens():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()

    assert deque.peek_rear() == None


def test_peek_rear_em_deque_sem_itens_apos_remove():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()
    deque.add_rear(1)
    deque.remove_rear()

    assert deque.peek_rear() == None


def test_peek_rear_em_deque_com_itens():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()
    deque.add_rear(1)
    deque.add_rear(2)

    expected = No(2)
    result = deque.peek_rear()

    assert expected.dado == result.dado

# ---- FIM: teste método peek_rear()


# ---- INÍCIO: teste método display()

def test_display_em_deque_com_elementos_string():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            deque.add_rear(item[:-1])

    result = deque.display()
    expected = [
        "1",
        "2",
        "3",
        "4",
        "5",
    ]

    assert result == expected


def test_display_em_deque_com_elementos_int():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()

    deque.add_rear(1)
    deque.add_rear(2)
    deque.add_rear(3)

    result = deque.display()
    expected = [
        1,
        2,
        3,
    ]

    assert result == expected


def test_display_em_deque_sem_elementos_ao_criar_deque():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()

    result = deque.display()
    expected = []
    
    assert result == expected


def test_display_em_deque_sem_elementos_ao_esvaziar_deque():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()

    deque.add_rear(1)
    deque.add_rear(2)
    deque.remove_front()
    deque.remove_front()

    result = deque.display()
    expected = []
    
    assert result == expected

# ---- FIM: teste método display()


# ---- INÍCIO: teste método size()

def test_size_ao_criar_deque():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()

    result = deque.size()
    expected = 0
    
    assert result == expected


def test_size_em_deque_ao_inserir_itens():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()

    deque.add_rear(1)
    expected = 1
    assert deque.size() == expected

    deque.add_rear(1)
    expected = 2
    assert deque.size() == expected

    deque.add_front(1)
    expected = 3
    assert deque.size() == expected


def test_size_em_deque_ao_remover_itens():
    try:
        exists = os.path.exists("deque.py")
        assert exists == True
    except:
        sys.exit()

    deque = Deque()

    deque.add_rear(1)
    deque.add_rear(1)
    deque.add_front(1)

    deque.remove_rear()
    expected = 2
    assert deque.size() == expected

    deque.remove_rear()
    expected = 1
    assert deque.size() == expected

    deque.remove_front()
    expected = 0
    assert deque.size() == expected

# ---- FIM: teste método size()