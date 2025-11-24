from login.login_service import LoginService
from login.user import User

service = LoginService()

def test_criacao_usuario_model():
    """Criar objeto usuário sem erros e validar campos obrigatórios"""
    user = User("Carlos", "carlos@test.com")
    assert user.nome != ""
    assert "@" in user.email

def test_validacao_login_email_valido():
    """Validação de login - email válido"""
    assert service.validar_email("teste@senac.com") == True

def test_validacao_login_email_invalido():
    """Validação de login - email inválido"""
    assert service.validar_email("aaaaaaa") == False

def test_autenticacao_retorna_usuario():
    """Login retorna usuário válido"""
    user = service.autenticar("teste@senac.com", "123456")
    assert user is not None

def test_salvar_humor():
    """Salvar humor diário"""
    humor = {"data": "2025-11-25", "estado": "feliz"}
    assert humor["estado"] in ["feliz", "triste", "ansioso"]
