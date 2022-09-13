class OperacaoFinanceiraError(Exception):
    pass

class SaldoInsuficienteError(OperacaoFinanceiraError):
    def __init__(self, msg="", saldo=None, value=None, *args):
        self.saldo = saldo
        self.value = value
        message = "Saldo Insuficiente para a realizar a transação "\
            f"Saldo atual: R$ {self.saldo} - Valor a ser sacado: R$ {self.value}"
        self.msg = message or msg
        super().__init__(self.msg, self.saldo, self.value, *args)