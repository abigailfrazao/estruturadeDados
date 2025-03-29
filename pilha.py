from pilha import Pilha

def reverter_string_com_pilha(texto):
    pilha = Pilha()
    string_revertida = ""
   
    for caractere in texto:
        pilha.push(caractere)

    while not pilha.is_empty():
        string_revertida += pilha.pop()

    return string_revertida

if __name__ == "__main__":
    entrada = input("Digite a string que deseja reverter: ")
    string_invertida = reverter_string_com_pilha(entrada)
    print(f"A string invertida é: {string_invertida}")
    print("\n--- Testes ---")
    print(f"Revertendo 'hello': {reverter_string_com_pilha('hello')}")
    print(f"Revertendo 'mundo': {reverter_string_com_pilha('mundo')}")
    print(f"Revertendo 'Programando em Python': {reverter_string_com_pilha('Programando em Python')}")
    print(f"Revertendo 'String123': {reverter_string_com_pilha('String123')}")
    print(f"Revertendo '': {reverter_string_com_pilha('')}")
    print(f"Revertendo 'Abigail': {reverter_string_com_pilha('Abigail')}")