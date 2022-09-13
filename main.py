from exceptions import SaldoInsuficienteError, OperacaoFinanceiraError


class Cliente:
    def __init__(self, nome: str, cpf: str, profissao: str):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.cliente = cliente
        self.__saldo = 100
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        self.saques_invalidos = 0
        self.transferencias_invalidas = 0
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo 'agencia' deve ser um valor inteiro.", value)
        if value <= 0:
            raise ValueError("O atributo 'agencia' deve ser maior do que 0.")

        self.__agencia = value

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo 'numero' deve ser um valor inteiro.")
        if value <= 0:
            raise ValueError("O atributo 'numero' deve ser maior do que zero.")
        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise ValueError("O atributo 'saldo' deve ser do tipo float.")
        if value < 0:
            raise ValueError("O atributo 'saldo' deve ser maior do que zero.")

        self.__saldo = value

    def transferir(self, valor, destino):
        if valor < 0:
            raise ValueError("O valor a ser transferido não pode ser menor do que zero.")
        try:
            self.sacar(valor)
        except SaldoInsuficienteError as E:
            self.transferencias_invalidas += 1
            E.args = ()
            raise OperacaoFinanceiraError("Operação não finalizada") from E
        destino.depositar(valor)

    def sacar(self, valor):
        if valor < 0:
            raise ValueError("O Valor a ser sacado não pode ser menor que zero.")
        if self.saldo < valor:
            self.saques_invalidos += 1
            raise SaldoInsuficienteError("", self.saldo, valor)
        self.saldo -= valor

    def depositar(self, valor):
        if valor < 0:
            raise ValueError("O valor a ser depositado não pode ser menor que zero")
        self.saldo += valor
