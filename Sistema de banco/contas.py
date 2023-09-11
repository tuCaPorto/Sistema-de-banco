"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
"""
import abc
class Conta(abc.ABC):
    
    def __init__(self, agencia: int, conta: int, saldo: float = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        ...
        
    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(Deposito: {valor} R$)')
    
    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r},{self.saldo!r})'
        return f'{class_name}{attrs}'
        
        
class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(Saque: {valor} R$)')
            return self.saldo
    
        print('Não foi possivel sacar o valor desejado')
        self.detalhes(f'(Saque negado: {valor})')
        
class ContaCorrente(Conta):
    
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: int = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite
        
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(Saque: {valor} R$)')
            return self.saldo
    
        print('Não foi possivel sacar o valor desejado')
        print(f'Seu limiete é {-self.limite:.2f}')
        self.detalhes(f'(Saque negado: {valor})')
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r},{self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'
        
if __name__ == '__main__':
    cp1 = ContaPoupanca(14,23)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    cp1.sacar(1)

    cc1 = ContaCorrente(14,23, 0 , 100)
    cc1.sacar(1)
    cc1.depositar(1)
