import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_screen():
    os.system('pause' if os.name == 'nt' else 'echo "Aperte ENTER para fechar..."\n read')
    clear_screen()

def get_spoons(cup_qnt) -> float:
    return (14 * cup_qnt) / 7

def get_water(cup_qnt, cup_size) -> float:
    if cup_qnt > 1:
        return (float(14.285714285714) * cup_size / 100) * cup_qnt
    else:
        return cup_size / 7

def get_milk(cup_qnt, cup_size) -> float:
    if cup_qnt > 1:
        return (float(85.714285714286) * cup_size / 100) * cup_qnt
    else:
        return cup_size - get_water(cup_qnt, cup_size)

def show_recipe(cup_qnt, cup_size) -> str:
    return (
        'Ingredientes: \n\n'
        f'[+] {get_spoons(cup_qnt):.0f} colheres de pó de capuccino.\n'
        f'[+] {get_water(cup_qnt, cup_size):.2f}ml de água.\n'
        f'[+] {get_milk(cup_qnt, cup_size):.2f}ml de leite.\n')

def show_steps(cup_qnt, cup_size) -> str:
    return (
        'Modo de Preparo: \n\n'
        f'[!] Esquente {get_water(cup_qnt, cup_size):.2f}ml de água (sem deixar ferver!).\n'
        f'[!] Adicione {get_spoons(cup_qnt):.0f} colheres (de sopa) de pó de capuccino e misture bem.\n'
        f'[!] Pegue essa mistura e coloque na geladeira, até que esfrie.\n'
        f'[!] Após a mistura esfriar, coloque no liquidificador e bata junto com {get_milk(cup_qnt, cup_size):.2f}ml de leite.\n'
        f'[!] E pronto, seu capuccino gelado está feito! Receita by: Rafaelvis Presley!.'
    )

def main():
    clear_screen()
    cup_qnt = int(input('Digite a quantidade de copos: '))
    cup_size = float(input('Digite o tamanho dos copos em ml: '))
    clear_screen()
    print(show_recipe(cup_qnt, cup_size))
    print(show_steps(cup_qnt, cup_size), "\n")

main()
exit_screen()