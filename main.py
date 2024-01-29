import random

# обучающая выборка (идеальное изображение цифр от 0 до 9)
num0 = list('111101101101111')
num1 = list('001001001001001')
num2 = list('111001111100111')
num3 = list('111001111001111')
num4 = list('101101111001001')
num5 = list('111100111001111')
num6 = list('111100111101111')
num7 = list('111001001001001')
num8 = list('111101111101111')
num9 = list('111101111001111')

# список всех цифр от 0 до 9 в одном массиве
nums = [num0, num1, num2, num3, num4, num5,
        num6, num7, num8, num9]


# создание класса перцептрон
class Perceptron:
    def __init__(self, num_neurons, threshold):  # конструктор (на входе 1) количество сенсоров; 2) порог активации)
        self.num_neurons = num_neurons
        self.threshold = threshold
        self.weights = [0 for _ in range(num_neurons)]  # для всех сенсоров устанавливается значение 0

    def activate(self, inputs):
        print(self.weights) # вывод процесса обучения и как изменяются веса
        summation = sum(int(x) * w for x, w in zip(inputs, self.weights)) # сумма весов на входные значения
        return summation >= self.threshold # если сумма больше порога

    def train(self, training_data, target_digit, iterations): # функция обучения
        for i in range(iterations): # по количеству iterations
            j = random.randint(0, 9) # случайное число
            result = self.activate(training_data[j]) # в результат записывается значение после активации функции
            if j != target_digit: # если случайное число не соответствует теме (заданному)
                if result: # если Да (но это не пять)
                    self.decrease(training_data[j])
            else: # если случайное равно заданному
                if not result: # Если нет (но это 5)
                    self.increase(training_data[target_digit])

    def decrease(self, inputs):
        for i in range(self.num_neurons):
            if inputs[i] == '1':
                self.weights[i] -= 1

    def increase(self, inputs):
        for i in range(self.num_neurons):
            if inputs[i] == '1':
                self.weights[i] += 1


perceptron = Perceptron(num_neurons=15, threshold=7) # создание объекта класса
perceptron.train(nums, target_digit=9, iterations=1000) # вызов функции обучения

print("0 это 6? ", perceptron.activate(num0))
print("1 это 6? ", perceptron.activate(num1))
print("2 это 6? ", perceptron.activate(num2))
print("3 это 6? ", perceptron.activate(num3))
print("4 это 6? ", perceptron.activate(num4))
print("5 это 6? ", perceptron.activate(num5))
print("6 это 6? ", perceptron.activate(num6))
print("7 это 6? ", perceptron.activate(num7))
print("8 это 6? ", perceptron.activate(num8))
print("9 это 6? ", perceptron.activate(num9))
