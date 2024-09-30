class Personaje:
    
    estado = True  # Vivo
    vida = 100 
    
    def __init__(self, nombre, altura, velocidad, resistencia, fuerza, debilidad):
        self.nombre = nombre
        self.altura = altura
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.fuerza = fuerza
        self.debilidad = debilidad
        self.estado = Personaje.estado
        self.vida = Personaje.vida

    def atacar(self, otro_personaje): 
        if self.estado:
            danio = self.fuerza - otro_personaje.resistencia
            danio = max(0, danio)  
            print(f"{self.nombre} ataca a {otro_personaje.nombre} causando {danio} puntos de daño")
            otro_personaje.recibir_dano(danio)
        else: 
            print(f"{self.nombre} está muerto y no puede atacar.")

    
    def recibir_dano(self, cantidad):
        if self.estado:
            self.vida -= cantidad
            print(f"{self.nombre} ha recibido {cantidad} puntos de daño. Vida restante: {self.vida}")
            if self.vida <= 0:
                self.vida = 0
                self.estado = False
                print(f"{self.nombre} ha muerto.")
    
    
    def mostrar_info(self):
        estado_texto = "vivo" if self.estado else "muerto"
        print(f"Nombre: {self.nombre}, Estado: {estado_texto}, Vida: {self.vida}, Fuerza: {self.fuerza}, Resistencia: {self.resistencia}")
