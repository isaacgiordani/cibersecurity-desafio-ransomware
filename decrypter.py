import os
import pyaes

def descriptografar_arquivo(file_name, chave):
    try:
        # Abrir o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()
        
        # Descriptografar o arquivo
        aes = pyaes.AESModeOfOperationCTR(chave)
        decrypt_data = aes.decrypt(file_data)
        
        # Criar o arquivo descriptografado
        new_file_name = file_name.replace(".ransomwaretroll", "")
        with open(new_file_name, "wb") as new_file:
            new_file.write(decrypt_data)
        
        # Remover o arquivo criptografado após a descriptografia
        os.remove(file_name)
        print(f"Arquivo descriptografado com sucesso: {new_file_name}")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo {file_name} não foi encontrado.")
    
    except Exception as e:
        print(f"Ocorreu um erro durante a descriptografia: {e}")

# Chave para descriptografia
chave = b"testeransomwares"

# Nome do arquivo criptografado
file_name = "teste.txt.ransomwaretroll"

# Descriptografar o arquivo
descriptografar_arquivo(file_name, chave)
