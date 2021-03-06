import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"D:\\My Documents"', 'D:\\Code']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки снутри строки.

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'D:\\Backup' # подставьте ваш путь.

# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y-%m-%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0: # проверяем, введён ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +
        comment.replace(' ', '_') + '.zip'

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today) # создание каталога
    print('Каталог успешно создан', today)

# 5. Используем команду "7z" для помещения файлов в zip-архив
zip_command = "7z a -tzip -mx5 -r0 {0} {1}".format(target, ' '.join(source))

# print(zip_command)
# 7z a -tzip -mx5 -r0 D:\Backup\20200618132559.zip "D:\My Documents" D:\Code

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
