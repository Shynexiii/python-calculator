"""
Un script python prenant 3 arguments dont le premier est l'opération voulue et les deux suivants 
les deux entiers 
"""

import calc
import sys

print("Bienvenue dans cette petite calculatrice sous Python pour entier.\n")


def run_calc():
    op = input("\nChoisissez une opération entre +, -, x , / et %   : \n")
    term_1 = input("Saisissez votre premier entier \n")
    term_2 = input("Saisissez votre second entier \n")
    res = calc.ope(op, term_1, term_2)
    while res is not None:
        print(f"{term_1} {op} {term_2} = {res}")
        keep_going = input("Voulez-vous continuer ? (O/N) : ").strip().lower()
        if keep_going == 'n':
            print("Fin du programme. Au revoir!")
            sys.exit(0)
        elif keep_going == 'o':
            break  # Exit the loop and continue the program
        else:
            print("Réponse non reconnue. Veuillez répondre par 'O' pour continuer ou 'N' pour arrêter. \n")
    run_calc()


run_calc()
