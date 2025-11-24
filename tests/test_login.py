import pytest
from login.login_service import LoginService

service = LoginService()

def test_validar_email_valido():
    assert service.validar_email("teste@senac.com") is True

def test_validar_email_invalido():
    assert service.validar_email("abc123") is False

def test_validar_senha_valida():
    assert service.validar_senha("123456") is True

def test_validar_senha_invalida():
    assert service.validar_senha("123") is False

def test_autenticar_sucesso():
    assert service.autenticar("teste@senac.com", "123456") is not None

def test_autenticar_usuario_inexistente():
    assert service.autenticar("naoexiste@x.com", "123456") is None

def test_autenticar_senha_errada():
    assert service.autenticar("teste@senac.com", "000000") is None
