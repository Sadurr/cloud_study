from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello_world():
    db = mysql.connector.connect(
    host="sadurskidatabase.mysql.database.azure.com",
    user="filip_sadurski",
    passwd="AzurePa$$w0rd",
    database="sadurskidatabase")

    cursor=db.cursor()

    cursor.execute("CREATE TABLE Names (name VARCHAR(50))")
    cursor.execute("INSERT INTO Names (name) VALUES ('Filip')")

    cursor.execute("SELECT * FROM Names")

    result=cursor.fetchall()

    for row in result:
        print("Hello " + row)

if __name__ == '__main__':
    app.run()
    
