import MySQLdb

conn = MySQLdb.connect("localhost","root","pokemon8897","testing")

cursor = conn.cursor()

data = cursor.execute("use testing;")
data = cursor.execute("select * from task;")
print cursor.fetchall()

conn.close()