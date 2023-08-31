# mysql_conn
This is a mysql plugin for python with light and flexible

# use it

from Mysql_conn import MySQLConn

mysql = MySQLConn(host=MYSQL_DATABASE_HOST, user=MYSQL_DATABASE_USER, database=MYSQL_DATABASE_DB, password=MYSQL_DATABASE_PASSWORD)



# single
	# select
	result = mysql.execute('SELECT status FROM users WHERE id=%s', (YOUR_ID,))

	# insert
	the row_id is id of sql insert value
	result, row_id = mysql.execute('INSERT INTO users(status) VALUE(%s)', (0,), True)

	# update
	result, _ = mysql.execute('UPDATE users SET status=0 WHERE uuid=%s', (YOUR_UUID,), True)

# many
	# executemany
	_num = [1, 2, 3]
	_list = [(i, 'Max') for i in _num]
	result = mysql.executemany("INSERT INTO users(status, name) VALUES(%s, %s)", _list, True)

	#transcation
	_res, _ = mysql.transaction([(INSERT INTO users(status) VALUE(%s), (0)), (sql2), (...)])
