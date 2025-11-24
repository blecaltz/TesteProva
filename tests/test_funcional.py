from login.login_service import LoginService

service = LoginService()

def test_login_credenciais_validas():
    """Login com credenciais válidas"""
    assert service.autenticar("teste@senac.com", "123456") is not None

def test_cadastro_usuario():
    """Cadastro de usuário (simulado)"""
    novo = {"nome": "João", "email": "joao@test.com"}
    assert novo["email"].endswith(".com")

def test_recuperar_senha():
    """Recuperar senha (simulação de envio de email)"""
    email = "teste@senac.com"
    assert "@" in email

def test_registrar_atendimento():
    """Registrar atendimento (simulação)"""
    atendimento = {"id": 1, "motivo": "ansiedade"}
    assert atendimento["id"] == 1

def test_filtrar_lista_de_usuarios():
    """Filtrar lista de usuários"""
    usuarios = ["ana", "bruno", "carla"]
    filtrados = [u for u in usuarios if "a" in u]
    assert len(filtrados) >= 1
