def my_shiny_new_decorator(function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate() # Сама функция
        print("А я - код, срабатывающий после")
    # Вернём эту функцию
    return the_wrapper_around_the_original_function

def my_shiny_new_decorator1(f):
    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции 1")
        f() 
        print("А я - код, срабатывающий после 1")
    return the_wrapper_around_the_original_function


# Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
def stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")

#stand_alone_function()
# Однако, чтобы изменить её поведение, мы можем декорировать её, то есть просто передать декоратору,
# который обернет исходную функцию в любой код, который нам потребуется, и вернёт новую,
# готовую к использованию функцию:
#stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
#stand_alone_function_decorated()


#my_shiny_new_decorator(stand_alone_function)()


@my_shiny_new_decorator1
@my_shiny_new_decorator
def another_stand_alone_function():
    print("Оставь меня в покое")

another_stand_alone_function()



print("--------------")

def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print("Смотри, что я получил:", arg1, arg2)
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments

# Теперь, когда мы вызываем функцию, которую возвращает декоратор, мы вызываем её "обёртку",
# передаём ей аргументы и уже в свою очередь она передаёт их декорируемой функции
@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print("Меня зовут", first_name, last_name)

print_full_name("Vasya", "Pupkin")
