from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')  # Ruta principal
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM task').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=('POST',))
def add_task():
    task = request.form['task']
    conn = get_db_connection()  # Invoca la conexión correctamente
    conn.execute('INSERT INTO task (name, completed) VALUES (?, ?)', (task, 0))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):  # Cambia el nombre de la función
    conn = get_db_connection()
    conn.execute('UPDATE task SET completed = 1 WHERE id = ?', (task_id,))  # Actualiza la tarea como completada
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM task WHERE id = ?', (task_id,))  # Corrige el paso de task_id
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
