"""Conjunto de funções relacionadas ao controle de usuários"""

from user import User

def cadastro():
    """Retorna um dicionário com as informações do usuário"""
    user_info = {}
    user_info['first_name'] = input("First Name: ")
    user_info['last_name'] = input("Last name: ")
    user_info['email'] = input("Email: ")
    user_info['username'] = input("Username: ")
    user_info['age'] = int(input("Age: "))
    user_info['location'] = input("Location: ")
    return user_info

def set_user(user_info):
    """Cria um objeto da classe usuário baseado em um dicionário"""
    user = User(user_info)
    return user
