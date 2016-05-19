#!/opt/local/bin/python
import urllib
import MySQLdb
import os

# Database conenction
db = MySQLdb.connect(host = "127.0.0.1", user = "username", passwd = "password", db = "databasename")

cursor = db.cursor()

# Use all the SQL you like
cursor.execute("SELECT column FROM table")

# get current working directory
path = os.getcwd()

# print all the first cell of all the rows
for row in cursor.fetchall():
    file_name = row[0]
    file = path + "/" + file_name

    # Download only files that don't exist at download time.
    if os.path.isfile(file):
      print "file does exist at this time: " + file
    else:
      url = "https://domain.com/public/folder/" + file_name
      urllib.urlretrieve(url, filename = file_name)
      print "New file downloaded: " + file_name

db.close()
