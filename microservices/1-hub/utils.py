from json import loads
from requests import get

def login(message):
    message_dict = loads(message)

    login = message_dict['login']
    password = message_dict['password']
    by_pass = False

    # Consultar dados do Banco de Dados
    users = get('http://localhost:3000/logins/')
    response_data = users.json()

    for value in response_data['user_logins']:

        if ((value['login'].upper() == login.upper()) and (value['password'].upper() == password.upper())):
            by_pass = True
    
    return by_pass
        
