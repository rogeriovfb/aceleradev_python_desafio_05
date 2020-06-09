from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator, validate_ipv4_address

# Create your models here.
class User(models.Model):
    name = models.CharField('Nome', max_length=50)
    last_login = models.DateField('Ultimo Login', auto_now=True)
    email = models.CharField('E-mail', max_length=254, validators=[EmailValidator])
    password = models.CharField('Senha', max_length=50, validators=[MinLengthValidator(8)])


class Agent(models.Model):
    name = models.CharField('Nome', max_length=50)
    status = models.BooleanField('Status')
    env = models.CharField('Env', max_length=20)
    version = models.CharField('Versao', max_length=5)
    address = models.CharField('Endereco', max_length=39, validators=[validate_ipv4_address])


class Event(models.Model):
    level = models.CharField('Nivel', max_length=20, validators=['CRITICAL', 'DEBUG', 'ERROR', 'WARNING', 'INFO'])
    data = models.TextField('Dados')
    arquivado = models.BooleanField('Arquivado')
    date = models.DateField('Data', auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.deletion.DO_NOTHING
    )

    agent = models.ForeignKey(
        Agent,
        on_delete=models.deletion.DO_NOTHING
    )


class Group(models.Model):
    name = models.CharField('Nome', max_length=50)


class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)