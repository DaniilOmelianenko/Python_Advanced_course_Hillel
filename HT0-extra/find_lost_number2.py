import random
import time
start_time = time.time()
start_number = 0
end_number = 100000000
start_step = 149
#-----Генерируем список:
# start_number = int(input('put the start number: '))
# end_number = int(input('put the end number: '))
# start_step = int(input('put the step: '))
start_list = list(range(start_number, end_number, start_step))
print(start_list)
print(len(start_list))
#-----Удаляем случайный элемент из списка:
num = random.randint(1, (len(start_list) - 1))
start_list.pop(num)
print(start_list)

#-----Генерируем список с потерянным числом:
if ((start_list[1])-(start_list[0])) == ((start_list[2])-(start_list[1])):
    step = ((start_list[1])-(start_list[0]))
    print(f'step: {step}')
elif ((start_list[-1])-(start_list[-2])) == ((start_list[-2])-(start_list[-3])):
    step = ((start_list[-1]) - (start_list[-2]))
    print(f'step: {step}')

if start_list[-1] > start_list[-2]:
    new_end = start_list[-1] + 1
elif start_list[-1] < start_list[-2]:
    new_end = start_list[-1] - 1
new_full_list = list(range((start_list[0]), new_end, step))
print(new_full_list)

#-----Находим потерянное число:
full_list_sum = sum(new_full_list)
lost_item_list = sum(start_list)
print(f'The lost number is: {full_list_sum - lost_item_list}')
print("--- %s seconds ---" % (time.time() - start_time))
