class Cuenta:
    def __init__(self, cliente, saldo_inicial, descubierto_autorizado=0):
        self.cliente = cliente
        self.saldo = saldo_inicial
        self.descubierto_autorizado = descubierto_autorizado

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if self.saldo - monto >= -self.descubierto_autorizado:
            self.saldo -= monto
            return True
        else:
            print("No se puede realizar la operación: fondos insuficientes.")
            return False

# Ejemplo de uso:
cuenta_cliente = Cuenta("Juan", 1000, 200)  # Cuenta de Juan con saldo inicial de 1000 y descubierto autorizado de 200
print("Saldo inicial de la cuenta de", cuenta_cliente.cliente, "es", cuenta_cliente.saldo)
cuenta_cliente.depositar(500)
print("Saldo después del depósito:", cuenta_cliente.saldo)
cuenta_cliente.retirar(1500)
print("Saldo después de retirar 1500:", cuenta_cliente.saldo)
