# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange, Optional, ValidationError
from app.constants import *
from app.models import User
# Documentation http://wtforms.simplecodes.com/docs/0.6.1/fields.html
# http://wtforms.readthedocs.io/en/latest/validators.html


# Class for registration
class DoctorRegistrationForm(FlaskForm):
    # Doctor infos
    email = StringField('Email', validators=[DataRequired(message='Email inválido'), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=4, max=16)])
    confirm_password = PasswordField('Confirme a senha', validators=[DataRequired(), Length(min=4, max=32), EqualTo('password')])
    crm = IntegerField('CRM', validators=[DataRequired()])
    fullname = StringField('Nome completo', validators=[DataRequired()])
    birthdate = DateField('Data de nascimento', format='%d/%m/%Y',validators=[Optional()])
    birthcity = StringField('Cidade de nascimento')
    # full_state = states.values()
    birthstate = SelectField('Estado de nascimento', choices=states_dict.items())
    rg = StringField('RG', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired(), Length(min=10, max=12)])
    cep = IntegerField('CEP', validators=[Optional()])
    place = SelectField('Logradouro', choices=logradouro_dict.items())
    residence_address = StringField('Endereço residencial')
    neighborhood = StringField('Bairro')
    city = StringField('Cidade')
    state = SelectField('Estado', choices=states_dict.items())
    phone_1 = IntegerField('Telefone celular', validators=[DataRequired()])
    phone_2 = IntegerField('Telefone fixo', validators=[Optional()])
    specialty = SelectField('Especialidade', validators=[DataRequired()], choices=specialties_dict.items())

    submit = SubmitField('Cadastrar colaborador')

    # Validando email (contra repeticao)
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Este email já foi utilizado. Escolha outro.')

    def validate_crm(self,crm):
        crm = User.query.filter_by(crm=crm.data).first()
        if crm:
            raise ValidationError('Este CRM já está cadastrado.')

    def validate_rg(self,rg):
        rg = User.query.filter_by(rg=rg.data).first()
        if rg:
            raise ValidationError('Este RG já está cadastrado.')

    def validate_cpf(self,cpf):
        cpf = User.query.filter_by(cpf=cpf.data).first()
        if cpf:
            raise ValidationError('Este CPF já está cadastrado.')
# LoginForm
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Salvar informações')
    submit = SubmitField('Entrar')