# Objeto Televisão com atributos e funções de... bem uma televisão.
class Televisor:
    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo
        self.canalAtual = None
        self.listaDeCanais = []
        self.volume = 20

    def aumentar_volume(self, valor):
        if self.volume+valor <= 10:
            self.volume += valor
        else:
            self.volume = 100

    def diminuir_volume(self, valor):
        if self.volume-valor >= 0:
            self.volume -= valor
        else:
            self.volume = 0

    def trocar_canal(self, canal):
        if canal in self.listaDeCanais:
            self.canalAtual = canal

    def sintonizar_canal(self, canal):
        if canal not in self.listaDeCanais:
            self.listaDeCanais.append(canal)

#  Classe que contém funções como aumentar e diminuir o volume,
#  trocar canal, sintonizar canal, etc, do Objeto Televisão.

class ControleRemoto:

    def __init__(self, tv):

        self.tv = tv

    def aumentar_volume(self):
        self.tv.aumentar_volume(90)

    def diminuir_volume(self):
        self.tv.diminuir_volume(90)

    def trocar_canal(self, canal):
        self.tv.trocar_canal(canal)

    def sintonizar_canal(self, canal):
        self.tv.sintonizar_canal(canal)

