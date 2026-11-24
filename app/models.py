from . import db


class Curso(db.Model):
    __tablename__ = 'cursos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Curso {self.nome}>'