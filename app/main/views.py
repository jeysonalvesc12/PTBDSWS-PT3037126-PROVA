from datetime import datetime
from flask import render_template, redirect, url_for, flash
from . import main
from .forms import CursoForm
from .. import db
from ..models import Curso


@main.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@main.route('/cursos', methods=['GET', 'POST'])
def cursos():
    form = CursoForm()
    if form.validate_on_submit():
        novo_curso = Curso(
            nome=form.nome.data.strip(),
            descricao=form.descricao.data.strip()
        )
        db.session.add(novo_curso)
        db.session.commit()
        flash('Curso cadastrado com sucesso!')
        return redirect(url_for('main.cursos'))

    lista_cursos = Curso.query.all()
    return render_template('cursos.html', form=form, cursos=lista_cursos)