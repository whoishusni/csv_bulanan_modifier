import csv
import random

# This Shuffler for test only, to test and shuffle csv data
# to test if other function like ordering number is work
# TODO: change this file
basedata_file: str = './base_data_sample/basedata.csv'
generated_shuffle_file: str = 'test_file.csv'

data_list: list = []
with open(basedata_file, 'r', encoding='utf8') as csv_reader:
    reader = csv.reader(csv_reader, delimiter='|')
    next(reader)
    for data in reader:
        if data:
            data_list.append(data)
    
random.shuffle(data_list)

with open(generated_shuffle_file,'w',encoding='utf8', newline='') as csv_writer:
    writer = csv.writer(csv_writer, delimiter='|')
    writer.writerow(['NO','NAMA_SUPPLIER','NAMA_PEMILIK_REKENING','NO_REKENING','JUMLAH_UANG'])
    for data_again in data_list:
        writer.writerow(data_again)

print('Shuffling Data Done')
    