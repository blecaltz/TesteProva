from .user import User

class LoginService:

    def validar_email(self, email):
        return "@" in email and "." in email

    def validar_senha(self, senha):
        return len(senha) >= 6

    def autenticar(self, email, senha):
        if not self.validar_email(email) or not self.validar_senha(senha):
            return None

        if email == "teste@senac.com" and senha == "123456":
            return User("Guilherme", email)

        return None
