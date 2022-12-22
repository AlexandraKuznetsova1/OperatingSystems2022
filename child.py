#!/usr/bin/python
#импоритируем необходимые для работы библиотеки 
# для того, чтобы использовать все функции, находящиеся в интерпретаторе Python
import sys
# для того, чтобы имели возможность вытаскивать и получать id
import os
# для того, чтобы могли ставить и использовать sleep
import time
# для генерации случайного числа из выбранного интервала
import random 

#нам нужно знать, какой слип поставить, на какое время программа должна "заснуть"
sleep_time = sys.argv[1]
# необходимо выполнить явное преобразование типа, string привести к int, ведь нам нужно целое число секнуд сна
sleep_time = int(sleep_time)
# по условию задания нам нужно получить свой id
process_id = os.getpid()
# также необходимо получить id нашего родителя
parent_process_id = os.getppid()

# выводим сообщение, которое требовалось по условию задания
print(f"Child [{process_id}]: I am started. PID {process_id}. Parent PID {parent_process_id}")

# по условию программа должна остановиться на какое-то время, используем sleep
time.sleep(sleep_time)

# предупреждение для пользователя, что мы готовы
print(f"Child [{process_id}]: I am ended. PID {process_id}. Parent PID {parent_process_id}")

# генерируем статусный код ответа, по условию из интервала от 0 до 1
exit_status = random.randint(0, 1)

# выходимм из процесса и заканчиваем работу
sys.exit(exit_status)
