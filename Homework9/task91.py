# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


from pathlib import Path

# Прописала в общем виде путь
with open(Path.cwd().joinpath('test_file', 'task1_data.txt'), 'r', encoding='utf-8') as file:
    data = file.read()

data = ''.join(c for c in data if not c.isdigit())

with open(Path.cwd().joinpath('test_file', 'task1_answer.txt'), 'w', encoding='utf-8') as file:
    file.write(data)

# Файлы не закрываю через .close(), так как используется менеджер контекста with...as..


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
