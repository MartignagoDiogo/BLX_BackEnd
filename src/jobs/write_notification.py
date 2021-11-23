

def write_notification(email: str, mensagem=''):
    with open('log_txt', mode='a') as email_file:
        conteudo = f'E-mail: {email} - msg: {mensagem} \n'
        email_file.write(conteudo)