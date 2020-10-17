#Модуль гамес

def ask_yes_no(question):
    #Задаёт вопрос с ответом йес или но
    response = None
    while response not in("y", "n"):   
        response = input(question + " (y/n)? ".lower())
    return response

def ask_number(question, low, high):
    #Просит ввести число из заданного диапазона
    response = None
    while response not in range(low, high + 1):   
        response = int(input(question))
    return response

if __name__ == "__main__":
    print("Вы запустили модулт гамес, а не импортировали его")
    input("\n\nНажмите ентер, чтобы выйти")
