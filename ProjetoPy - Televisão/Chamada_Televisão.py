from Objeto_Televisão import *

# Atribuição de valores
tv = Televisor("SONY", "SONY-123")

# Instânciação
controle = ControleRemoto(tv)

# Chamada
controle.sintonizar_canal("SBT")
controle.trocar_canal("SBT")

# Exibição
print(tv.canalAtual)
