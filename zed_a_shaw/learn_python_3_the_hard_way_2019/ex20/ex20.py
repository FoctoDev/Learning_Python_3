from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

# каждый раз считывается одна строка из файла до символа \n
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file, encoding ="utf-8")

print("Первым делом выведем этот файл целиком:\n")

print_all(current_file)

print("Теперь отматаем назад, словно это кассета.")

rewind(current_file)

print("Выведем три строки:"),

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
