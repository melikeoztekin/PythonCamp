import sqlite3

def listele():
    baglanti=sqlite3.connect("chinook/chinook.db") #veritabanına bağlanmayı sağlar
    cursor= baglanti.execute("select FirstName, LastName from customers")

    for satir in cursor:
        print(satir[1])

    baglanti.close()
listele()