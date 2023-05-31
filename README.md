# mysql_conn
This is a mysql plugin for python with light and flexible

# use it

from mysql_conn import MySQLConn

mysql = MySQLConn()

result = mysql.execute('SELECT status FROM users WHERE uuid=%s', (YOUR_UUID, ))