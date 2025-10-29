class Animal():
    def emitir_som(self):
        return "Algum som animal"
    
    class Gato():
        def emitir_som(self):
            return "Miau Miau"
        
    class Cachorro():
        def emitir_som(self):
            return "Au Au"
        
    gato = Gato()
    print(gato.emitir_som())

    cachorro = Cachorro()
    print(cachorro.emitir_som())