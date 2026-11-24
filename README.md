Avaliação Semestral — Aplicação Web com Flask

Aplicação web desenvolvida com o framework Flask e hospedada na plataforma PythonAnywhere, implementando a rota principal e o módulo de Cadastro de Cursos com persistência em banco de dados.

Aluno: Jeyson

Prontuário: PT3037126

Link da aplicação (PythonAnywhere): https://jeysonpt3037126.pythonanywhere.com

Tela Inicial

Funcionalidades Implementadas

Rota Principal (/): Exibe as informações da avaliação semestral, identificação do aluno (nome e prontuário) e data/hora local atualizada dinamicamente.

Cadastro de Cursos (/cursos): Formulário validado para cadastro de cursos (nome e descrição de até 250 caracteres), com salvamento em banco de dados SQLite e exibição da relação de cursos cadastrados.

Tratamento de Erros (404 e 500): Os demais módulos do menu (Professores, Disciplinas, Alunos e Ocorrências) não foram implementados conforme especificação e exibem automaticamente a página "Não disponível" com a data e hora local.

Templates e Herança: Interface padronizada utilizando Jinja2 e integração com Flask-Bootstrap.

Tecnologias Utilizadas

Python 3

Flask

Flask-Bootstrap

Flask-Moment

Flask-WTF / WTForms

Flask-SQLAlchemy (SQLite)

PythonAnywhere (hospedagem)

Estrutura do Projeto

├── flasky.py           # Arquivo principal da aplicação, modelos, formulários e rotas
├── requirements.txt    # Dependências do projeto
├── tela_inicial.png    # Captura de tela da página inicial
└── templates/
    ├── base.html       # Template base com barra de navegação e Flask-Moment
    ├── index.html      # Página inicial
    ├── cursos.html     # Formulário e tabela de cursos cadastrados
    ├── 404.html        # Página de erro 404 ("Não disponível")
    └── 500.html        # Página de erro interno do servidor


Como Executar Localmente

Clone o repositório:

git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO


Crie e ative o ambiente virtual:

python3 -m venv venv
source venv/bin/activate
# No Windows (PowerShell): .\venv\Scripts\Activate.ps1


Instale as dependências:

pip install -r requirements.txt


Execute a aplicação:

export FLASK_APP=flasky.py
# No Windows (PowerShell): $env:FLASK_APP="flasky.py"

flask run


Acesse http://127.0.0.1:5000 no navegador.
