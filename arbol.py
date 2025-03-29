import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)
    
    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izquierda)
            print(nodo.valor, end=' ')
            self.inorden(nodo.derecha)
    
    def preorden(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=' ')
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)
    
    def postorden(self, nodo):
        if nodo is not None:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.valor, end=' ')


arbol = Arbol()
numeros = random.sample(range(1, 100), 10)  
for num in numeros:
    arbol.insertar(num)

print("Números insertados en el árbol:", numeros)
print("\nRecorrido Inorden:")
arbol.inorden(arbol.raiz)
print("\nRecorrido Preorden:")
arbol.preorden(arbol.raiz)
print("\nRecorrido Postorden:")
arbol.postorden(arbol.raiz)