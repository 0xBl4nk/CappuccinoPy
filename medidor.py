import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

QUANTIDADE_COPO = float(input("Digite quantos copos utilizará: "))
TAMANHO_COPO = float(input("Digite o tamanho em ml do seu copo: "))

clear_screen()

def medirColheres():
    return (14 * QUANTIDADE_COPO) / 7

def medirAgua():
    return (14.285714285714 * TAMANHO_COPO / 100) * QUANTIDADE_COPO if  QUANTIDADE_COPO > 1 else TAMANHO_COPO / 7

def medirLeite():
    return (85.714285714286 * TAMANHO_COPO / 100) * QUANTIDADE_COPO if QUANTIDADE_COPO > 1 else TAMANHO_COPO - medirAgua()

def ingredientes():
    print("\nIngredientes: \n")
    print(f"[+] {medirColheres()} colheres de pó de capuccino.")
    print(f"[+] {medirAgua():.2f} ml de água.")
    print(f"[+] {medirLeite():.2f} ml de leite.")


def preparo():
    print("\nModo de preparo: \n")
    print(f"[+] Esquente {medirAgua():.2f} ml de água e adicione {medirColheres()} colheres de pó de capuccino (NÃO DEIXA FERVER NÃO HEIM!)")
    print("[+] Pegue a mistura e coloque na geladeira até que esfrie.")
    print(f"[+] Após esfriar coloque a mistura no liquidificador junto com {medirLeite():.2f} e bata.")
    print("[+] Está pronto seu capuccino gelado da Rafaelvis Presley!\n")


ingredientes()
preparo()

input("Aperte qualquer tecla para sair...")
clear_screen()
