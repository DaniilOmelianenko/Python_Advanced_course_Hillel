import random
import time
start_time = time.time()
start_number = 0
end_number = 50000000
step = random.randint()
# start_number = int(input('put the start number: '))
# end_number = int(input('put the end number: '))
my_list = list(range(start_number, end_number, 2))
#print(my_list)
start_numbers_sum = sum(my_list)
num = random.randint((start_number + 1), (len(my_list)-1))
changed_list = my_list.pop(num)
#print(my_list)
end_num_sum = sum(changed_list)
print(f'The lost number is: {start_numbers_sum - end_num_sum}')
print("--- %s seconds ---" % (time.time() - start_time))
