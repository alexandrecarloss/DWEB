# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Avaliacao(models.Model):
    produto_proid = models.ForeignKey('Produto', models.DO_NOTHING, db_column='produto_proid', blank=True, null=True, related_name='avaliacoes')
    servico_serid = models.ForeignKey('Servico', models.DO_NOTHING, db_column='servico_serid', blank=True, null=True, related_name='avaliacoes')
    avadescricao = models.CharField(max_length=100, blank=True, null=True)
    avavalor = models.IntegerField()
    pessoa_pesid = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='pessoa_pesid', related_name='avaliacoes')
    avacod = models.AutoField(primary_key=True)
    avadthora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avaliacao'
        ordering = ['avacod']

    def __str__(self):
        return f'{self.pessoa_pesid.pesnome} nota {self.avavalor}'
     


class Carrinho(models.Model):
    carid = models.AutoField(primary_key=True)
    carpro = models.ForeignKey('Produto', models.DO_NOTHING, db_column='carpro', blank=True, null=True, related_name='carrinhos')
    carpes = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='carpes', related_name='carrinhos')
    carser = models.ForeignKey('Servico', models.DO_NOTHING, db_column='carser', blank=True, null=True, related_name='carrinhos')
    carquant = models.IntegerField()
    carpreco = models.FloatField()

    class Meta:
        managed = False
        db_table = 'carrinho'
        ordering = ['carid']

    def __str__(self):
        return self.carid

class CategoriaProduto(models.Model):
    ctpid = models.AutoField(primary_key=True)
    ctpnome = models.CharField(max_length=60)
    ctpdescricao = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'categoria_produto'

    def __str__(self):
        return self.ctpnome

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Formapagamento(models.Model):
    fpgid = models.AutoField(primary_key=True)
    fpgdescricao = models.CharField(max_length=65, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formapagamento'
        ordering = ['fpgid']

    def __str__(self):
        return self.fpgdescricao


class Login(models.Model):
    logemail = models.CharField(primary_key=True, max_length=70)
    logsenha = models.CharField(max_length=45, blank=True, null=True)
    petshop_ptsid = models.ForeignKey('Petshop', models.DO_NOTHING, db_column='petshop_ptsid', blank=True, null=True, related_name='login')
    pessoa_pesid = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='pessoa_pesid', blank=True, null=True, related_name='login')
    ong_ongid = models.ForeignKey('Ong', models.DO_NOTHING, db_column='ong_ongid', blank=True, null=True, related_name='login')

    class Meta:
        managed = False
        db_table = 'login'
        ordering = ['logemail']


class Notafiscal(models.Model):
    petshop_ptsid = models.ForeignKey('Petshop', models.DO_NOTHING, db_column='petshop_ptsid', related_name='notasfiscais')
    venda_venid = models.ForeignKey('Venda', models.DO_NOTHING, db_column='venda_venid', related_name='notasfiscais')
    ntfcod = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'notafiscal'
        ordering = ['ntfcod']


class Ong(models.Model):
    ongid = models.AutoField(primary_key=True)
    ongnome = models.CharField(max_length=65)
    ongcidade = models.CharField(max_length=70, blank=True, null=True)
    ongbairro = models.CharField(max_length=70)
    ongrua = models.CharField(max_length=70)
    ongnum = models.SmallIntegerField()
    ongtelefone = models.CharField(max_length=15, blank=True, null=True)
    ongemail = models.CharField(max_length=70, blank=True, null=True)
    ongestado = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'ong'
        ordering = ['ongid']

    def __str__(self):
        return self.ongnome


class Pessoa(models.Model):
    pesid = models.AutoField(primary_key=True)
    pescpf = models.CharField(unique=True, max_length=11)
    pesdtnascto = models.DateField()
    pessexo = models.CharField(max_length=1)
    pescidade = models.CharField(max_length=65)
    pesbairro = models.CharField(max_length=65)
    pesrua = models.CharField(max_length=65)
    pesemail = models.CharField(max_length=70)
    pesnumero = models.SmallIntegerField()
    pestelefone = models.CharField(max_length=15)
    pesnome = models.CharField(max_length=100)
    pesestado = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'pessoa'
        ordering = ['pesid']

    def __str__(self):
        return self.pesnome


class Pet(models.Model):
    petid = models.AutoField(primary_key=True)
    petnome = models.CharField(max_length=65)
    petsexo = models.CharField(max_length=1)
    petcastrado = models.CharField(max_length=12)
    petdtnascto = models.DateField()
    petpeso = models.FloatField()
    pessoa_pesid = models.ForeignKey(Pessoa, models.DO_NOTHING, db_column='pessoa_pesid', blank=True, null=True, related_name='pets')
    pet_porte_ptpid = models.ForeignKey('PetPorte', models.DO_NOTHING, db_column='pet_porte_ptpid', related_name='pets')
    pet_raca_ptrid = models.ForeignKey('PetRaca', models.DO_NOTHING, db_column='pet_raca_ptrid', related_name='pets')
    pet_tipo_pttid = models.ForeignKey('PetTipo', models.DO_NOTHING, db_column='pet_tipo_pttid', related_name='pets')

    class Meta:
        managed = False
        db_table = 'pet'
        ordering = ['petid']

    def __str__(self):
        return self.petnome


class PetAdocao(models.Model):
    ong_ongid = models.ForeignKey(Ong, models.DO_NOTHING, db_column='ong_ongid', related_name='petadocoes')
    pet_petid = models.ForeignKey(Pet, models.DO_NOTHING, db_column='pet_petid', related_name='petadocoes')
    adoid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pet_adocao'
        ordering = ['adoid']

    def __str__(self):
        return f'{self.ong_ongid.ongnome} e {self.pet_petid.petnome}'


class PetFoto(models.Model):
    pftid = models.AutoField(primary_key=True)
    pftfoto = models.ImageField(upload_to='adocao/images/pet', max_length=100)
    pet_petid = models.ForeignKey(Pet, models.DO_NOTHING, db_column='pet_petid', related_name='petfotos')

    class Meta:
        managed = False
        db_table = 'pet_foto'
        ordering = ['pftid']

    def delete(self, *args, **kwargs):
        self.pftfoto.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.pftfoto.name


class PetPorte(models.Model):
    ptpid = models.AutoField(primary_key=True)
    ptpnome = models.CharField(max_length=65)
    ptpdescricao = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pet_porte'
        ordering = ['ptpid']

    def __str__(self):
        return self.ptpnome


class PetRaca(models.Model):
    ptrid = models.AutoField(primary_key=True)
    ptrnome = models.CharField(max_length=65, blank=True, null=True)
    pet_tipo_pttid = models.ForeignKey('PetTipo', models.DO_NOTHING, db_column='pet_tipo_pttid', related_name='petracas')

    class Meta:
        managed = False
        db_table = 'pet_raca'
        ordering = ['ptrid']

    def __str__(self):
        return self.ptrnome


class PetTipo(models.Model):
    pttid = models.AutoField(primary_key=True)
    pttnome = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'pet_tipo'
        ordering = ['pttid']

    def __str__(self):
        return self.pttnome


class Petshop(models.Model):
    ptsid = models.AutoField(primary_key=True)
    ptsnome = models.CharField(max_length=65, blank=True, null=True)
    ptscnpj = models.CharField(max_length=20)
    ptscidade = models.CharField(max_length=65, blank=True, null=True)
    ptsbairro = models.CharField(max_length=65, blank=True, null=True)
    ptsrua = models.CharField(max_length=65, blank=True, null=True)
    ptsnumero = models.SmallIntegerField(blank=True, null=True)
    ptstelefone = models.CharField(max_length=15, blank=True, null=True)
    ptsemail = models.CharField(max_length=70, blank=True, null=True)
    ptsestado = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'petshop'
        ordering = ['ptsid']

    def __str__(self):
        return self.ptsnome


class Produto(models.Model):
    proid = models.AutoField(primary_key=True)
    pronome = models.CharField(max_length=65)
    propreco = models.FloatField()
    prosaldo = models.IntegerField(blank=True, null=True)
    propetshop_ptsid = models.ForeignKey(Petshop, models.DO_NOTHING, db_column='propetshop_ptsid', related_name='produtos')
    categoria_produto_ctpid = models.ForeignKey(CategoriaProduto, models.DO_NOTHING, db_column='categoria_produto_ctpid', related_name='categorias')

    class Meta:
        managed = False
        db_table = 'produto'
        ordering = ['proid']

    def __str__(self):
        return self.pronome


class ProdutoFoto(models.Model):
    prfid = models.AutoField(primary_key=True)
    prffoto = models.ImageField(upload_to='venda\images\produto', max_length=100)
    produto_proid = models.ForeignKey(Produto, models.DO_NOTHING, db_column='produto_proid', related_name='produtofotos')

    class Meta:
        managed = False
        db_table = 'produto_foto'
        ordering = ['prfid']

    def delete(self, *args, **kwargs):
        self.prffoto.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.prffoto.name

class Tiposervico(models.Model):
    tpsid = models.AutoField(primary_key=True)
    tpsnome = models.CharField(max_length=70)
    tpsdescricao = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tiposervico'
        ordering = ['tpsid']
    
    def __str__(self):
        return self.tpsnome


class Servico(models.Model):
    serid = models.AutoField(primary_key=True)
    servalor = models.FloatField()
    petshop_ptsid = models.ForeignKey(Petshop, models.DO_NOTHING, db_column='petshop_ptsid', related_name='servicos')
    tiposervico_tpsid = models.ForeignKey(Tiposervico, models.DO_NOTHING, db_column='tiposervico_tpsid', related_name='servicos')
    serdescricao = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servico'
        ordering = ['serid']

    def __str__(self):
        return self.serdescricao


class ServicoFoto(models.Model):
    serftid = models.AutoField(primary_key=True)
    serftvalor = models.ImageField(upload_to='venda/images/servico', max_length=100)
    servico_serid = models.ForeignKey(Servico, models.DO_NOTHING, db_column='servico_serid', related_name='servicofotos')

    class Meta:
        managed = False
        db_table = 'servico_foto'
        ordering = ['serftid']

    def delete(self, *args, **kwargs):
        self.serftvalor.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.serftvalor.name


class Solicita(models.Model):
    pessoa_pesid = models.ForeignKey(Pessoa, models.DO_NOTHING, db_column='pessoa_pesid')
    servico_serid = models.ForeignKey(Servico, models.DO_NOTHING, db_column='servico_serid')
    solid = models.AutoField(primary_key=True)
    soldthr = models.DateTimeField()
    solpetid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'solicita'
        ordering = ['solid']


class TentativaAdota(models.Model):
    ttaid = models.AutoField(primary_key=True)
    ttapes = models.ForeignKey(Pessoa, models.DO_NOTHING, db_column='ttapes')
    tta_petadocao = models.ForeignKey(PetAdocao, models.DO_NOTHING, db_column='tta_petadocao')
    ttastatus = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'tentativa_adota'


class Venda(models.Model):
    venid = models.IntegerField(primary_key=True)
    venser = models.IntegerField(blank=True, null=True)
    venpro = models.ForeignKey(Produto, models.DO_NOTHING, db_column='venpro', blank=True, null=True)
    venformapagamento_fpgid = models.ForeignKey(Formapagamento, models.DO_NOTHING, db_column='venformapagamento_fpgid')
    venpessoa_pesid = models.ForeignKey(Pessoa, models.DO_NOTHING, db_column='venpessoa_pesid')
    venvalor = models.FloatField()
    vendthora = models.DateTimeField(blank=True, null=True)
    venqtd = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'venda'
        ordering = ['venid']
