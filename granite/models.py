from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin, AnonymousUserMixin
from geoalchemy2 import Geometry
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, value):
        return check_password_hash(self.password, value)

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.username


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    geom = db.Column(Geometry('MULTIPOLYGON', 4326))
    public = db.Column(db.Boolean)

    def __repr__(self):
        return '<Project {}>'.format(self.name)

    def __str__(self):
        return self.name


class Slope(db.Model):
    __tablename__ = 'slopes'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    geom = db.Column(Geometry('MULTIPOLYGON', 4326))
    public = db.Column(db.Boolean)

    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    project = db.relationship('Project', backref=db.backref('slopes', lazy='dynamic'))


class Parking(db.Model):
    __tablename__ = 'parking'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    geom = db.Column(Geometry('MULTIPOLYGON', 4326))
    public = db.Column(db.Boolean)

    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    project = db.relationship('Project', backref=db.backref('parking', lazy='dynamic'))


class Path(db.Model):
    __tablename__ = 'paths'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    geom = db.Column(Geometry('MULTILINESTRING', 4326))
    public = db.Column(db.Boolean)

    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    project = db.relationship('Project', backref=db.backref('paths', lazy='dynamic'))
