
def  test_function ():
    def inner_function ():
        print("Я в области видимости функции test_function")

    inner_function()# Вызов внутренней функции
test_function()# Вызов test_function для демонстрации

# inner_function() #выдас ошибку "NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?"
