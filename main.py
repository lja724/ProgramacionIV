from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

app = Flask(__name__)
#Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'DiccionarioSQL'
mysql = MySQL(app)

#Settings
app.secret_key = 'mysecretkey'


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Diccionario')
    data = cur.fetchall()
    return render_template('index.html',Diccionario = data)

@app.route('/add_word',methods=['POST'])
def add_contact():
    if request.method == 'POST':
        Palabra_E = request.form['Palabra_E']
        Palabra_S = request.form['Palabra_S']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Diccionario(Palabra_E,Palabra_S) VALUES(%s,%s)',(Palabra_E,Palabra_S))
        mysql.connection.commit()
        flash('Palabra agregada al diccionario')
        return redirect(url_for('Index'))

@app.route('/edit/<string:id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Diccionario WHERE Palabra_id = (%s)',(id))
    data = cur.fetchall()
    return render_template('editar.html',Diccionario = data[0])

@app.route('/update/<string:id>',methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        Palabra_E = request.form['Palabra_E']
        Palabra_S = request.form['Palabra_S']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Diccionario
            SET Palabra_E = %s,
                Palabra_S = %s
            WHERE Palabra_id = %s
            """,(Palabra_E,Palabra_S,id))
        flash('Palabra actualizada')
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Diccionario WHERE Palabra_id=(%s)',(id))
    mysql.connection.commit()
    flash('Palabra eliminada')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)