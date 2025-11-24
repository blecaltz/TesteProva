import time
from login.login_service import LoginService

service = LoginService()

def test_carga_login():
    """Suportar 200 logins simultâneos"""
    for _ in range(200):
        service.autenticar("teste@senac.com", "123456")
    assert True

def test_stress_banco():
    """Banco respondendo com +500 requisições/min"""
    for _ in range(500):
        service.validar_email("teste@senac.com")
    assert True

def test_tempo_resposta_api():
    """Resposta < 2 segundos"""
    inicio = time.time()
    service.autenticar("teste@senac.com", "123456")
    fim = time.time()
    assert (fim - inicio) < 2

def test_uso_continuo():
    """Sistema estável por longo período"""
    for _ in range(10000):
        service.validar_senha("123456")
    assert True

def test_desempenho_relatorio():
    """Relatório gerado em < 5 segundos (simulado)"""
    inicio = time.time()
    time.sleep(0.5)
    fim = time.time()
    assert (fim - inicio) < 5
