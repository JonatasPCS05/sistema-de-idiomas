matriz = [["Digite seu nome: ", "Type your name: ", "Escriba su nombre: ", "Gib deinen Namen ein: ", "Tapez votre nom: "],
          ["Seja bem vindo {}", "Welcome {}", "Bienvenido {}", "Willkommen {}", "Bienvenue {}"]]
idioma = int(input("""Idioma / Language / Idioma / sprache / Langue
  [ 1 ] Português
  [ 2 ] English
  [ 3 ] Espanõl
  [ 4 ] Deutsch
  [ 5 ] Français\n"""))
idioma -= 1
nome = input(matriz[0][idioma])
print(matriz[1][idioma].format(nome))