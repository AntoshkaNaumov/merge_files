import os

def merge_files(path_1, path_2, path_3):

    out_file = "merge_file.txt" # создаем переменную которой присваеваем название файла
    file1_path = os.path.join(os.getcwd(), path_1)
    file2_path = os.path.join(os.getcwd(), path_2)
    file3_path = os.path.join(os.getcwd(), path_3)
    with open(file1_path, 'r', encoding='utf-8') as file1: # читаем файл 
        file1 = file1.readlines()
    with open(file2_path, 'r', encoding='utf-8') as file2:
        file2 = file2.readlines()
    with open(file3_path, 'r', encoding='utf-8') as file3:
        file3 = file3.readlines()
    with open(out_file, 'w', encoding='utf-8') as f_total: # запись данных в файл

        if len(file1) < len(file2) and len(file1) < len(file3):
                f_total.write(path_1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
        elif len(file2) < len(file1) and len(file2) < len(file3):
                f_total.write(path_2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
        elif len(file3) < len(file1) and len(file3) < len(file2):
                f_total.write(path_3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
        if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(
                    file3):
                f_total.write(path_1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
        elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(
                    file3):
                f_total.write(path_2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
        elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(
                    file2):
                f_total.write(path_3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
        if len(file1) > len(file2) and len(file1) > len(file3):
                f_total.write(path_1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
        elif len(file2) > len(file1) and len(file2) > len(file3):
                f_total.write(path_2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
        elif len(file3) > len(file1) and len(file3) > len(file2):
                f_total.write(path_3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
    print('Файл записан')

file_1 = '1.txt'

file_2 = '2.txt'

file_3 = '3.txt'

merge_files(file_1, file_2, file_3)

