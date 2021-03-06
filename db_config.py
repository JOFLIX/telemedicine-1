from app import db, bcrypt
from app.models import User, Specialty, Calendar, Consulta
from app.constants import specialties_dict

#from app.models import joinsSpecialtyUser

db.drop_all()
db.create_all()

# Criando registro para especialidades
for k, v in specialties_dict.items():
    spec = Specialty(specialty=v)
    db.session.add(spec)
db.session.commit()

# Criando usuarios
hashed_password = bcrypt.generate_password_hash('admin').decode('utf-8')
'''
paulo = User(email='paulo.camargos@hotmail.com',
             password=hashed_password, crm='1234',
             fullname='Paulo Camargos', rg='123',
             cpf='123', phone_1='92226633', cep='312321')
italo = User(email='italo@hotmail.com',
             password=hashed_password, crm='4321',
             fullname='Italo Fernandes', rg='321',
             cpf='321', phone_1='92102109', cep='312321')

db.session.add(italo)
db.session.add(paulo)
db.session.commit()

especialista = User(email='especialista@gmail.com',
             password=hashed_password, crm='0001',
             fullname='Especialista', rg='001',
             cpf='001', phone_1='0000001', cep='312321')
generalista = User(email='generalista@gmail.com',
             password=hashed_password, crm='0002',
             fullname='Generalista', rg='002',
             cpf='002', phone_1='0000002', cep='312321')

db.session.add(especialista)
db.session.add(generalista)
db.session.commit()

neurologia = Specialty.query.filter_by(specialty='Neurologia').first()
geral = Specialty.query.filter_by(specialty='Geral').first()
neurologia.doctors.append(especialista)
geral.doctors.append(generalista)

db.session.commit()
'''
#image_file = url_for('static',
# filename='profile_pics/' + current_user.image_file)
italo_fernandes = User(email='italo@teleespecialista.com',
                       password=hashed_password,
                       image_file='italo_fernandes.jpeg',
                       crm='10',
                       fullname='Ítalo Fernandes',
                       rg='00000010',
                       cpf='00000000010',
                       phone_1='990000010')
paulo_camargos = User(email='paulo@teleespecialista.com',
                       password=hashed_password,
                       image_file='paulo_camargos.jpg',
                       crm='11',
                       fullname='Paulo Camargos',
                       rg='00000011',
                       cpf='00000000011',
                       phone_1='990000011')
ana_claudia = User(email='ana@teleespecialista.com',
                       password=hashed_password,
                       image_file='ana_claudia.jpg',
                       crm='12',
                       fullname='Ana Cláudia',
                       rg='00000012',
                       cpf='00000000012',
                       phone_1='990000012')
lucas_lemos = User(email='lucas@teleespecialista.com',
                       password=hashed_password,
                       image_file='lucas_lemos.jpg',
                       crm='13',
                       fullname='Lucas Lemos',
                       rg='00000013',
                       cpf='00000000013',
                       phone_1='990000013')
mariane_modesto = User(email='mariane@teleespecialista.com',
                       password=hashed_password,
                       image_file='mariane_modesto.jpg',
                       crm='14',
                       fullname='Mariane Modesto',
                       rg='00000014',
                       cpf='00000000014',
                       phone_1='990000014')
nathalia_rodrigues = User(email='nathalia@teleespecialista.com',
                       password=hashed_password,
                       image_file='nathalia_rodrigues.jpg',
                       crm='15',
                       fullname='Nathália Rodrigues',
                       rg='00000015',
                       cpf='00000000015',
                       phone_1='990000015')
pedro_carneiro = User(email='pedro@teleespecialista.com',
                       password=hashed_password,
                       image_file='pedro_carneiro.jpg',
                       crm='16',
                       fullname='Pedro Carneiro',
                       rg='00000016',
                       cpf='00000000016',
                       phone_1='990000016')

db.session.add(italo_fernandes)
db.session.add(paulo_camargos)
db.session.add(ana_claudia)
db.session.add(lucas_lemos)
db.session.add(mariane_modesto)
db.session.add(nathalia_rodrigues)
db.session.add(pedro_carneiro)

db.session.commit()


radiologia = Specialty.query.filter_by(specialty='Radiologia e Diagnóstico por Imagem').first()
otorrinolaringologia = Specialty.query.filter_by(specialty='Otorrinolaringologia').first()
neurocirurgia = Specialty.query.filter_by(specialty='Neurocirurgia').first()
mastologia = Specialty.query.filter_by(specialty='Mastologia').first()
geral = Specialty.query.filter_by(specialty='Geral').first()


radiologia.doctors.append(italo_fernandes)
otorrinolaringologia.doctors.append(paulo_camargos)
radiologia.doctors.append(ana_claudia)
neurocirurgia.doctors.append(lucas_lemos)
mastologia.doctors.append(pedro_carneiro)
geral.doctors.append(mariane_modesto)
geral.doctors.append(nathalia_rodrigues)
db.session.commit()

nathalia_italo = Consulta(nome_paciente="Giovana Orlovski Nogueira")
mariane_paulo = Consulta(nome_paciente="Catarina dos Santos Gomes")
nathalia_rodrigues.consultas.append(nathalia_italo)
italo_fernandes.consultas.append(nathalia_italo)

mariane_modesto.consultas.append(mariane_paulo)
paulo_camargos.consultas.append(mariane_paulo)
db.session.commit()
