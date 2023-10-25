import pytest
from app import app

@pytest.fixture
#se construye cliente que simula solicitudes
def client():
    #habilitar modo de pruebas
    app.config["TESTING"] = True

    with app.test_client() as client:
        #produce el cliente
        yield client

#funcion que realiza el test
def test_index(client):
    rv = client.get('/')
    #valida que exista la cadena string en el texto que obtuvo
    assert b'Prueba DevOps' in rv.data