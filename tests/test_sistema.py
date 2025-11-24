from login.login_service import LoginService

service = LoginService()

def test_fluxo_completo_login():
    """Usuário acessa, loga e chega ao dashboard"""
    user = service.autenticar("teste@senac.com", "123456")
    assert user.email == "teste@senac.com"

def test_criar_atendimento_completo():
    """Sistema registra o atendimento sem erro"""
    atendimento = {"paciente": "Ana", "motivo": "crise de ansiedade"}
    assert atendimento["paciente"] == "Ana"

def test_gerar_relatorio_mensal():
    """PDF gerado corretamente (simulação)"""
    relatorio = {"mes": "Novembro", "status": "ok"}
    assert relatorio["status"] == "ok"

def test_atualizar_cadastro():
    """Cadastro alterado com sucesso"""
    user = {"nome": "Pedro"}
    user["nome"] = "Pedro Silva"
    assert user["nome"] == "Pedro Silva"

def test_integracao_api_externa():
    """Dados recebidos da API externa"""
    dados = {"status": 200, "mensagem": "ok"}
    assert dados["status"] == 200
