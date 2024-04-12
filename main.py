class Dog:
    kind = 'border collie'

    def __init__(self, name):
        self.name = name


a = Dog('하나')
b = Dog('둘')

print(f'a의 종: {a.kind}), 이름: {a.name}')
print(f'b의 종: {b.kind}), 이름: {b.name}')
