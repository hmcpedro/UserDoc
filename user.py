"""Representa um usuário do programa"""

class User():
    """Uma simples representação de um usuário"""

    def __init__(self,user_info):
        """Instância um obejto usuário"""
        self.first_name = user_info['first_name']
        self.last_name = user_info['last_name']
        self.email = user_info['email']
        self.username = user_info['username']
        self.age = user_info['age']
        self.location = user_info['location']        

    def describe_user(self):
        """Um método que descreve o objeto usuário de forma elegante"""
        print(
            f"Username: @{self.username}\n"
            f"Name: {self.first_name.title()} {self.last_name.title()}\n"
            f"Age : {self.age}\n"
            f"Location: {self.location.title()}"
        )

    def user_documentation(self):
        """Retorna um valor de texto para ser documentado"""
        message = (
            f"Username: @{self.username}\n"
            f"Name: {self.first_name.title()} {self.last_name.title()}\n"
            f"Email : {self.email}\n"
            f"Age : {str(self.age)}\n"
            f"Location: {self.location.title()}"
        )
        return message

    def doc_user(self):
        """Um método que cria um arquivo txt com as informações do usuário"""
        filename = self.username + "_info.txt"
        with open(filename, 'w') as file:
            file.write(self.user_documentation())