# classe carta
#recebe dos atributos: valor e naipe(copas, espada, paus, ouro)
#método:
# - revela o naipe e o valor da carta. como? imprimindo na tela
# - validação do naipe e do valor da carta[]

class carta:
    
    NAIPES = ['copas', 'ouros', 'paus', 'espadas']
    NAIPES_UNICODE = {
        'paus'    : '\u2663',
        'copas'   : '\u2665',
        'espadas' : '\u2660',
        'ouros'   : '\u2666',
    }
    #valores = [str(n)for n in ranger(2, 11)] + list('AQJK')

    VALORES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K',]

    def _init_(self, valor, naipe):
        self.valida_carta(valor, naipe)
        self.valor = valor
        self.naipe = naipe

        def valida_carta(self, valor, naipe):
            if valor not in self.valores:
                raise Exception(f"este valor não é um valor aceito: {valor}")
                if naipe not in self.NAIPE:
                    raise Exception(f'este naipe não é um valor aceito:{naipe}')
                    
        def _str_(self):
            naipe_unicode = self.NAIPES_UNICODES[self.naipe]          
            print(f"{self.valor}\n{naipe_unicode}")

        def _str_(self): 
            naipe_unicode = self.naipe_unicode[self.naipe]
            return f"carta: {self.valor}{naipe_unicode}"
           
        self.validar_carta(10,'espada')          
        self.validar_carta(20,'maico')    
            
            



     



