from flask import Flask, render_template, request
from flask import session, redirect, url_for, render_template, request
from users import add_user, get_all_users, find_user_by_username

app = Flask(__name__)
app = Flask(__name__)
app.secret_key = 'uma_chave_secreta_bem_forte_aqui'

@app.route('/register', methods=['GET', 'POST'])

def register():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

# validação campo vazio
        if not username or not password:
            return render_template(
                'register.html',
                error="Por favor, preencha todos os campos.",
                username=username
            )
# fim validação

# validação duplicidade
        if find_user_by_username(username):
            return render_template('register.html', error="Usuário já existe!", username=username)

# salva dados no array
        add_user(username, password)

# exibe dados para teste
        print(f"Usuário: {username}, Senha: {password}")  # Só para testes

        return f"Usuário {username} cadastrado com sucesso!"

    return render_template('register.html')



@app.route('/users')
def users():
    todos_usuarios = get_all_users()
    return render_template('users.html', users=todos_usuarios)

# LOGIN
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        usuario = find_user_by_username(username)

        if usuario and usuario['password'] == password:

            return f"Login bem sucedido! Bem vindo(a), {username}!"
            session['username'] = username

        else:
             return render_template('login.html', error="Usuario ou senha incorretos", username=username)
    return render_template('login.html')
# fim login

# DASHBOARD
@app.route('/dashboard')
def dashboard():
    if 'usuario' in session:
        return render_template('dashboard.html', username=session['usuario'])
    else:
        return redirect(url_for('login'))

# fim dashboard


if __name__ == '__main__':
    app.run(debug=True)