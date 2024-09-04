# Programa para verificar a existência da letra 'a' (maiúscula ou minúscula) e contar sua ocorrência
def contar_a(texto):
    count_a = texto.lower().count('a')  # Converte o texto para minúsculo e conta as ocorrências de 'a'
    
    if count_a > 0:
        return f"A letra 'a' aparece {count_a} vezes na string."
    else:
        return "A letra 'a' não aparece na string."

# Definindo a string ou recebendo como input
texto = input("Informe uma string para verificar a ocorrência da letra 'a': ")
print(contar_a(texto))