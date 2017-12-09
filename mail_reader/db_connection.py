import MySQLdb

def addToTable(data):
	conn = MySQLdb.connect("localhost","root","pokemon8897","task1")
	cursor = conn.cursor()
	s = cursor.execute('insert into email_data values("{}","{}","{}","{}","{}","{}");'.format(data['date'],data['from_email'],data['to_email'],data['mailing_list'],data['subject'],data['id']))
	conn.commit()
	conn.close()
