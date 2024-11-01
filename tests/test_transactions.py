from finances import Transaction
from finances.transaction import CATEGORIES
from datetime import datetime

DEFAULT_AMOUNT = 100.0
DEFAULT_CATEGORY = 1
DEFAULT_DESCRIPTION = "Transação de teste"

def get_transaction():
    return Transaction(DEFAULT_AMOUNT, DEFAULT_CATEGORY, DEFAULT_DESCRIPTION)

def test_transaction_instance():
    tr = get_transaction()
    assert isinstance(tr, Transaction), "Falha ao instanciar o objeto"

def test_transaction_types():
    tr = get_transaction()
    # Checa os tipos
    assert type(tr.amount) is float
    assert type(tr.date) is datetime
    assert type(tr.category) is int
    assert type(tr.description) is str
    # Checa os valores
    assert tr.amount == DEFAULT_AMOUNT
    assert tr.category == DEFAULT_CATEGORY
    assert tr.description == DEFAULT_DESCRIPTION

def test_transaction_cat():
    tr = get_transaction()
    assert tr.category in CATEGORIES.keys()

def test_transaction_update():
    tr = get_transaction()
    tr.update(amount=200.0)
    assert tr.amount == 200.0
    new_date = datetime.now()
    tr.update(date=new_date)
    assert tr.date == new_date
    tr.update(category=2)
    assert tr.category == 2
    tr.update(description="Teste")
    assert tr.description == "Teste"

def test_transaction_representation():
    tr = get_transaction()
    expected = f"Transação: {DEFAULT_DESCRIPTION} R$ {DEFAULT_AMOUNT:.2f} ({CATEGORIES[DEFAULT_CATEGORY]})"
    assert str(tr) == expected, "Representação fora do formato esperado."