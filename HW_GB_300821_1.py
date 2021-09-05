from time import sleep
class TrafficLights:
    # локальная переменная класса
    __colours = 'красный, желтый, зеленый'

    # системный метод класса
    def __init__(self, condition_1, condition_2 = None):
        print(f'режим светофора - {condition_1}')
        if condition_2 == None:
            while True: # светофор будет работать бесконечно
                new_list = self.__colours.split(', ')
                # выводим элементы массива
                for i in range(len(new_list)):
                    print(new_list[i])
                    if new_list[i] == 'красный':
                        sleep(2)
                    elif new_list[i] == 'желтый':
                        sleep(7)
                    else:
                        sleep(10)
        else: # светофор сработает один раз и выключится
            new_list = self.__colours.split(', ')
            # выводим элементы массива
            for i in range(len(new_list)):
                print(new_list[i])
                if new_list[i] == 'красный':
                    sleep(2)
                elif new_list[i] == 'желтый':
                    sleep(7)
                else:
                    sleep(10)
        print(f'режим светофора - {condition_2}')

# объект класса
trafficlight_1 = TrafficLights('включен', 'выключен')



    

    