from flaskext.mysql import MySQL
from flask import Flask

mysql = MySQL()

class MySQLConn:
	def __init__(self, host='localhost', database='xx', user='root', password=''):
		
		app = Flask(__name__)
		app.config['MYSQL_DATABASE_USER'] = user
		app.config['MYSQL_DATABASE_PASSWORD'] = password
		app.config['MYSQL_DATABASE_DB'] = database
		app.config['MYSQL_DATABASE_HOST'] = host
		mysql.init_app(app)
		
	def close(self, conn, cursor):
		cursor.close()
		conn.close()

	def execute(self, sql, args=None, commit=False):

		conn = mysql.connect()
		cursor = conn.cursor()
		if args:
			cursor.execute(sql, args)
		else:
			cursor.execute(sql)

		if commit is True:
			conn.commit()
			self.close(conn, cursor)
			return cursor.rowcount, cursor.lastrowid
		else:
			res = cursor.fetchall()
			self.close(conn, cursor)
			return res

	def executemany(self, sql, args, commit=False):
		
	    conn = mysql.connect()
	    cursor = conn.cursor()
	    cursor.executemany(sql, args)

	    if commit is True:
	    	conn.commit()
	    	self.close(conn, cursor)
	    	return cursor.rowcount
	    else:
		    res = cursor.fetchall()
		    self.close(conn, cursor)
		    return res

	def transaction(self, sql_and_args, rollback=True):
		
		conn = mysql.connect()
		cursor = conn.cursor()
		try:
			for s_v in sql_and_args:
				cursor.execute(s_v[0], s_v[1])
				if not rollback:
					conn.commit() 
		except Exception as e:
			if rollback:
				conn.rollback()
			self.close(conn, cursor)
			raise
		else:
			if rollback:
				conn.commit() 
			self.close(conn, cursor)
			return cursor.rowcount, cursor.lastrowid
