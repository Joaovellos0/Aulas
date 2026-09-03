import pyfiglet

frase = input("Digite algo: ")
frase_format = pyfiglet.figlet_format(frase)

print(frase_format)