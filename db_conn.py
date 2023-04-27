import psycopg2

g_pass = 'gjhtdj12'

conn = psycopg2.connect(dbname='postgres', user='postgres', host='localhost', port = 5432, password = g_pass)

cursor = conn.cursor()

cursor.execute('select * from verbs_1')

print(cursor.fetchone()[0 : 6])
# print(cursor.fetchall())

cursor.close()
