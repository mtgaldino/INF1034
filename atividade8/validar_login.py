def valida_email(email):
    return email[-8:] == "@puc.com"

def possuiMaiuscula(palavra):
    for letra in palavra:
        if 'A' <= letra <= 'Z':
            return True
    return False

def possuiMinuscula(palavra):
    for letra in palavra:
        if 'a' <= letra <= 'z':
            return True
    return False

def possuiNumero(palavra):
    for caracter in palavra:
        if '0' <= caracter <= '9':
            return True
    return False

def valida_senha(senha):
    check_tamanho = len(senha) >= 8
    check_maiuscula = possuiMaiuscula(senha)
    check_minuscula = possuiMinuscula(senha)
    check_numero = possuiNumero(senha)
    return check_tamanho and check_maiuscula and check_minuscula and check_numero

def desloca_char(char, deslocamento):
    if 'A' <= char <= 'Z':
        ref = ord('A')
        qtd = 26
    elif 'a' <= char <= 'z':
        ref = ord('a')
        qtd = 26
    elif '0' <= char <= '9':
        ref = ord('0')
        qtd = 10
    else:
        return char                                  
    pos = ord(char) - ref                            
    pos_cesar = (pos + deslocamento) % qtd           
    return chr(ref + pos_cesar)

def criptografa_senha(senha):
    senha_cripto = ""
    for char in senha:
        senha_cripto += desloca_char(char, 3)        
    return senha_cripto

def descriptografa_senha(senha_cripto):
    senha = ""
    for char in senha_cripto:
        senha += desloca_char(char, -3)              
    return senha

if __name__ == "__main__":
    
    assert valida_email("aluno@puc.com") == True
    assert valida_email("aluno@gmail.com") == False
    assert valida_email("aluno@puc.com.br") == False

    assert valida_senha("Abcdef12") == True
    assert valida_senha("abcdef12") == False    
    assert valida_senha("ABCDEF12") == False    
    assert valida_senha("Abcdefgh") == False    
    assert valida_senha("Abc123") == False      
    
    assert criptografa_senha("abc") == "def"
    assert criptografa_senha("ABC") == "DEF"
    assert criptografa_senha("123") == "456"
    assert criptografa_senha("xyz") == "abc"    
    assert criptografa_senha("XYZ") == "ABC"    
    assert criptografa_senha("789") == "012"    
    assert criptografa_senha("a!b") == "d!e"    
    assert criptografa_senha("Abc123") == "Def456"
    
    assert descriptografa_senha("def") == "abc"
    assert descriptografa_senha("abc") == "xyz"
    assert descriptografa_senha("012") == "789"
    assert descriptografa_senha(criptografa_senha("Senha123")) == "Senha123"

    print("Todos os testes passaram!")
    senha = "Senha123"
    cripto = criptografa_senha(senha)
    print("Senha original:       ", senha)
    print("Senha criptografada:  ", cripto)
    print("Senha descriptografada:", descriptografa_senha(cripto))