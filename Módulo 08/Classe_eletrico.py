# Classe CarroEletrico
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        print(f"⚡ {self.marca} {self.modelo} - luxo sustentável com {self.autonomia_bateria}km de autonomia.")

    def __str__(self):
        return f"{self.marca} {self.modelo} ⚡ ({self.autonomia_bateria}km)"

