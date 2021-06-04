import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_language():
    language = input('Choose a language: english or portuguese (type E or P):  ')
    return language

def get_spoons(cup_qnt: float) -> float:
    return (14 * cup_qnt) / 7

def get_water(cup_qnt: float, cup_size: float) -> float:
    if cup_qnt > 1:
        return (float(14.285714285714) * cup_size / 100) * cup_qnt
    else:
        return cup_size / 7

def get_milk(cup_qnt: float, cup_size: float) -> float:
    if cup_qnt > 1:
        return (float(85.714285714286) * cup_size / 100) * cup_qnt
    else:
        return cup_size - get_water(cup_qnt, cup_size)

def show_recipe(cup_qnt: float, cup_size: float, language) -> None:
    if language == 'P':
        print(f'''Ingredientes para {cup_qnt} copos de {cup_size}ml: \n
    [+] {get_spoons(cup_qnt):.0f} colheres de pó de capuccino. (Tamanho_da_colher = "sopa")
    [+] {get_water(cup_qnt, cup_size):.2f}ml de água.
    [+] {get_milk(cup_qnt, cup_size):.2f}ml de leite.
        ''')

    elif language == 'E' or language == 'e':
         print(f'''Ingredients for {cup_qnt} cups of {cup_size}ml: \n
    [+] {get_spoons(cup_qnt):.0f} soup spoons of capuccino.
    [+] {get_water(cup_qnt, cup_size):.2f}ml of water.
    [+] {get_milk(cup_qnt, cup_size):.2f}ml of milk.
        ''')

def show_steps(cup_qnt, cup_size, language) -> None:
    if language == 'P' or language == 'p':
        print(f'''Modo de Preparo: \n
    [!] Esquente {get_water(cup_qnt, cup_size):.2f}ml de água (sem deixar ferver!).
    [!] Adicione {get_spoons(cup_qnt):.0f} colheres (de sopa) de pó de capuccino e misture bem.
    [!] Pegue essa mistura e coloque na geladeira, até que esfrie.
    [!] Após esfriar, coloque no liquidificador e bata junto com {get_milk(cup_qnt, cup_size):.2f}ml de leite.
    [!] E pronto, seu capuccino gelado está pronto para beber!!

    OBS:
        [+] O liquidificador deixa mais cremoso
        [+] Use canudo de metal, bambu, madeira e papel. Temos que salvar as tartaruguinhas SZ.
        [!] Receita by: Rafa Ballerini!
        [!] Script by: Arthur Ottoni!
        ''')

    elif language == 'E' or language == 'e':
        print(f'''How to prepare: \n
    [!] Warm up {get_water(cup_qnt, cup_size):.2f}ml of water (don't let it boil!).
    [!] Add {get_spoons(cup_qnt):.0f} soup spoons of cappucino and mix it.
    [!] Take that mix and put it in the fridge untill it gets cold.
    [!] After it got cold, put it in the blender and blend it with {get_milk(cup_qnt, cup_size):.2f}ml of milk.
    [!] All set, your iced capuccino is ready to drink!!

    Observations:
        [+] The blender leaves it creamier.
        [+] Use metal, wood or paper straws. We have to save the turtles SZ.
        [!] Recipe by: Rafa Ballerini!
        [!] Script by: Arthur Ottoni!
        ''')
def main():
    clear_screen()
    language = get_language()
    
    if language == 'E' or language == 'e':
        cup_size = float(input('Enter cup size (ml): '))
        cup_qnt = int(input('Enter how many cups: '))

    elif language == 'P' or language == 'e':
        cup_size = float(input('Digite o tamanho do copo em ml: '))
        cup_qnt = int(input('Digite a quantidade de copos: '))

    show_recipe(cup_qnt, cup_size, language)
    show_steps(cup_qnt, cup_size, language)

    if language == 'P' or language == 'p':
        input('Pressione ENTER para sair...')

    elif language == 'E' or language == 'e':
        input('Press ENTER to quit')

if __name__ == '__main__':
    main()