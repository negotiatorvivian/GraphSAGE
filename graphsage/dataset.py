import subprocess
from os import listdir
from os.path import isfile, join, split, splitext


def data_parser(folder_path, des_folder_path):
    file_list = [join(folder_path, f) for f in listdir(folder_path) if isfile(join(folder_path, f))]
    for file in file_list:
        output = des_folder_path + '/' + file.split('/')[-1]
        with open(output, 'w') as f:
            input = open(file, 'r')
            process = subprocess.run('/home/ziwei/Downloads/MapleLCMDistChronoBT/bin/glucose_static', stdin = input,
                                     stdout = f, encoding = 'utf-8')


if __name__ == '__main__':
    data_parser('datasets/SAT', 'datasets/SAT_ANS')
