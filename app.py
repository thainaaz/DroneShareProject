from flask import Flask, render_template, request
from users import add_user, get_all_users

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
# validação
        if not username or not password:
            return render_template(
                'register.html',
                error="Por favor, preencha todos os campos.",
                username=username
            )
# fim validação
# salva dados no array
        add_user(username, password)
# exibe dados para teste
        print(f"Usuário: {username}, Senha: {password}")  # Só para testes

        return f"Usuário {username} cadastrado com sucesso!"

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
