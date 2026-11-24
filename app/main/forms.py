from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class CursoForm(FlaskForm):
    nome = StringField(
        'Qual é o nome do curso?',
        validators=[DataRequired(), Length(max=120)]
    )
    descricao = TextAreaField(
        'Descrição (250 caracteres)',
        validators=[DataRequired(), Length(max=250)]
    )
    submit = SubmitField('Cadastrar')