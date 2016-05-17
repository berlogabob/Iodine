acid_list=[]
###
def acidls():
    summ = one_acid()
    acid_list.append(summ)
    print(acid_list)
    ###
def one_acid():
    N = float(input("Какое количесто двойных связей в жирной кислоте? "))
    print("Количесто двойных связей в жирной кислоте %g " % (N))
    Wi = float(input("Каково содержание данной кислоты в сумме жирных кислот?  "))
    print("Содержание данной кислоты в сумме жирных кислот %g" % (Wi))
    Mi = float(input("Какова молекулярная масса жирной кислоты? "))
    print("Молекулярная масса жирной кислоты %g " % (Mi))
    print("\n", "\n", "\n")
    odna_kislota = (254 * N * Wi) / Mi
    print("Йодное число этой одной жирной кислоты %g " % (odna_kislota))
    return(odna_kislota)
    ###
def question():
    answer = input(" Добавить значения для жирной кислоты?  (да или нет)")
    if answer == "да" or answer == "Да" or answer == "д" or answer == "ДА" or answer == "Д":
        acidls()
        question()
        ###
        # добавить список с значениями, которые будут считаться в след пункте
    elif answer == "нет" or answer == "Нет" or answer == "Н" or answer == "н" or answer == "НЕТ":
        print("Йодовое число равно: ")
        print(sum(acid_list))
        ###
    else:
        print("\n \n введено некорректное значение")
        print("\n")
        question()
        ###
question()
###
input("Для выхода нажмите клавишу Enter")
