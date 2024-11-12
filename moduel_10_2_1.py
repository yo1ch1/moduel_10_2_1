import threading
from multiprocessing import Pool
import time



def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as f:
        for line in f:
            line = f.readline()
            all_data.append(line)



file_list = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
start_time = time.time()
for name in file_list: #00:00:01.70 - линейный
    read_info(name)
end_time = time.time()
time_cost = end_time - start_time
formatted_time = time.strftime('%H:%M:%S.%g', time.gmtime(time_cost))
print(f'{formatted_time} - линейный')

if __name__ == '__main__': #00:00:00.70 - многопроцессный
    start_time = time.time()
    pool = Pool()
    pool.map(read_info, file_list)
    end_time = time.time()
    time_cost = end_time - start_time
    formatted_time = time.strftime('%H:%M:%S.%g', time.gmtime(time_cost))
    print(f'{formatted_time} - многопроцессный')

