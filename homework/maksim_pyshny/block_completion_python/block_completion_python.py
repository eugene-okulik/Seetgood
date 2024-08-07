import os
import argparse


def main():
    parser = argparse.ArgumentParser(description='Поиск текста в логах.')
    parser.add_argument('log_dir', help='Путь к папке, содержащей файлы с логами.')
    parser.add_argument('--text', required=True, help='Текст, который необходимо найти в логах.')
    args = parser.parse_args()

    file_path = args.log_dir
    text_file = args.text

    list_file_path = os.listdir(file_path)
    found = False

    for file_name in list_file_path:
        file_text = os.path.join(file_path, file_name)
        if os.path.isfile(file_text):
            with open(file_text, 'r', encoding='utf-8') as file:
                line_number = 0
                for line in file:
                    line_number += 1
                    if text_file in line:
                        found = True
                        print(f'Найдено в файле: {file_name}. Порядковый номер строки файла: {line_number}')

                        words = line.split()
                        for index in range(len(words)):
                            if text_file in words[index]:
                                start = max(0, index - 5)
                                end = min(len(words), index + 6)
                                context = ' '.join(words[start:end])
                                print(context)
                        break

    if not found:
        print('Введенный текст не содержится в файлах с логами')


if __name__ == "__main__":
    main()
