class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

if __name__ == '__main__':
    televisao = Televisao()
    print('Televisão está ligada? {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada? {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada? {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada? {}'.format(televisao.ligada))
    print('Canal: {}'.format(televisao.canal))
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))




# class Calculadora:
#     def __init__(self):
#         pass
#
#     def soma(self, valor_a, valor_b):
#         return valor_a + valor_b
#
#     def subtracao(self, valor_a, valor_b):
#         return valor_a - valor_b
#
#     def multiplicacao(self, valor_a, valor_b):
#         return valor_a * valor_b
#
#     def divisao(self, valor_a, valor_b):
#         return valor_a / valor_b
#
# calculadora = Calculadora()
# print(calculadora.soma(5, 2))
# print(calculadora.subtracao(5, 2))
# print(calculadora.multiplicacao(5, 2))
# print(calculadora.divisao(5, 2))


class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b
#
# calculadora = Calculadora(5, 2)
# print(calculadora.soma())
# print(calculadora.subtracao())
# print(calculadora.multiplicacao())
# print(calculadora.divisao())