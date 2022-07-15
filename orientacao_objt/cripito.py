def cripto(frase):
    tradutor = ""
    for letra in frase:
        print(frase)
        if letra in   "E": tradutor = tradutor + "3"
        elif letra in "A": tradutor = tradutor + "4"
        elif letra in "S": tradutor = tradutor + "5"
        elif letra in "3": tradutor = tradutor + "E"
        elif letra in "4": tradutor = tradutor + "A"
        elif letra in "5": tradutor = tradutor + "S"
        else:
         tradutor = tradutor + letra
    
        return tradutor
    




print(cripto(input("digite sua frase:")))            
