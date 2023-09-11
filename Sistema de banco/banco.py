import contas
import pessoas

class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        cleintes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None
        ):
        self.agencias = agencias or []
        self.clientes = cleintes or []
        self.contas = contas or []
        
    def _checa_agencia(self,conta):
        if conta.agencia in self.agencias:
            return True
        return False
        
    def _checa_cleinte(self,cliente):
        if cliente in self.clientes:
            return True
        return False
        
    def _checa_conta(self,conta):
        if conta in self.contas:
            return True
        return False
    
    def _checa_conta_cliente(self, cliente, conta):
        if conta in cliente.conta:
            print('_checa_conta_cliente', True)
            return True
        print('_checa_conta_cliente', False)
        return False
        
    
    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
                self._checa_cleinte(cliente) and \
                self._checa_conta(conta)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'

if __name__ == '__main__':
    c1= pessoas.Cliente('Arthur', 28)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    print()
    c2= pessoas.Cliente('Suellen', 25)
    cp1= contas.ContaPoupanca(11, 24, 5000)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1,c2])
    banco.contas.extend([cc1,cp1])
    banco.agencias.extend([111,222])
    
    print(banco.autenticar(c1,cc1))
    print(banco)