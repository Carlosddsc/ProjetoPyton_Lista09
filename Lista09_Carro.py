class Carro:
    
    
    def __init__(self):
        self.motor_ligado = False
        self.em_movimento = False

    def ligarMotor(self):
        if not self.motor_ligado:
            print("Motor ligado.")
            self.motor_ligado = True
        else:
            print("O motor já está ligado.")

    def desligarMotor(self):
        if self.motor_ligado:
            if not self.em_movimento:
                print("Motor desligado.")
                self.motor_ligado = False
            else:
                print("Você não pode desligar o motor enquanto o carro está em movimento.")
        else:
            print("O motor já está desligado.")

    def andar(self):
        if self.motor_ligado and not self.em_movimento:
            print("O carro está em movimento.")
            self.em_movimento = True
        elif self.em_movimento:
            print("O carro já está em movimento.")
        else:
            print("Ligue o motor primeiro.")

    def parar(self):
        if self.motor_ligado and self.em_movimento:
            print("O carro parou de se mover.")
            self.em_movimento = False
        elif not self.em_movimento:
            print("O carro já está parado.")
        else:
            print("Ligue o motor primeiro.")


