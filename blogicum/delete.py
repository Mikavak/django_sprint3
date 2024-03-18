import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

# Запрашиваем все столбцы всех записей из таблицы video_products;
# символ * после SELECT означает "верни все поля найденных записей".
r = '''
DELETE FROM django_migrations WHERE id=20;
'''

# В results получим итерируемый объект, который можно перебрать циклом:

cur.execute(r)
# При получении данных из таблицы не нужно вызывать метод con.commit()!
con.close()