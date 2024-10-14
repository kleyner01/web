from django.db import models


class Candidato(models.Model):
    class Sexo(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'F', 'Feminino'

    class EstadoCivil(models.TextChoices):
        CASADO = 'CASADO', 'Casado'
        SOLTEIRO = 'SOLTEIRO', 'Solteiro'
        DIVORCIADO = 'DIVORCIADO', 'Divorciado'

    class TipoHabilitacao(models.TextChoices):
        A = 'A', 'Categoria A'
        B = 'B', 'Categoria B'
        C = 'C', 'Categoria C'
        D = 'D', 'Categoria D'

    class Formacao(models.TextChoices):
        GRAU_1_COMPLETO = '1G_COMPLETO', '1 Grau Completo'
        GRAU_2_COMPLETO = '2G_COMPLETO', '2 Grau Completo'
        GRAU_2_INCOMPLETO = '2G_INCOMPLETO', '2 Grau Incompleto'
        SUPERIOR = 'SUPERIOR', 'Superior Completo'
        SUPERIOR_INCOMPLETO = 'SUPERIOR_INCOMPLETO', 'Superior Incompleto'
        POS_GRADUACAO = 'POS_GRADUACAO', 'Pós-Graduação'
        MBA = 'MBA', 'MBA'
        MESTRADO = 'MESTRADO', 'Mestrado'
        DOUTORADO = 'DOUTORADO', 'Doutorado'

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    prefixo = models.CharField(max_length=2, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    curriculo = models.FileField(upload_to='curriculos/', blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    mensagem = models.TextField(blank=True, null=True)
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=200)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=2)
    data_nasc = models.DateField()
    estado_civil = models.CharField(max_length=10, choices=EstadoCivil.choices, default=EstadoCivil.SOLTEIRO)
    rg = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    sexo = models.CharField(max_length=1, choices=Sexo.choices, default=Sexo.MASCULINO)
    nome_pai = models.CharField(max_length=100, blank=True, null=True)
    nome_mae = models.CharField(max_length=100, blank=True, null=True)
    possui_habilitacao = models.BooleanField(default=False)
    tipo_habilitacao = models.CharField(max_length=1, choices=TipoHabilitacao.choices, blank=True, null=True)
    carteira_profissional = models.BooleanField(default=False)
    serie_carteira_profissional = models.CharField(max_length=10, blank=True, null=True)
    formacao = models.CharField(max_length=50, choices=Formacao.choices, default=Formacao.GRAU_1_COMPLETO)
    curso = models.CharField(max_length=500, blank=True, null=True)
    ano_conclusao = models.IntegerField(blank=True, null=True)
    empresa_atual = models.CharField(max_length=200, blank=True, null=True)
    segmento_atual = models.CharField(max_length=100, blank=True, null=True)
    cargo_atual = models.CharField(max_length=50, blank=True, null=True)
    data_inicio_atual = models.DateField(blank=True, null=True)
    data_saida_atual = models.DateField(blank=True, null=True)
    atribuicoes_atual = models.TextField(max_length=200, blank=True, null=True)

    empresa_anterior_1 = models.CharField(max_length=200, blank=True, null=True)
    segmento_anterior_1 = models.CharField(max_length=100, blank=True, null=True)
    cargo_anterior_1 = models.CharField(max_length=50, blank=True, null=True)
    data_inicio_anterior_1 = models.DateField(blank=True, null=True)
    data_saida_anterior_1 = models.DateField(blank=True, null=True)
    atribuicoes_anterior_1 = models.TextField(max_length=200, blank=True, null=True)

    empresa_anterior_2 = models.CharField(max_length=200, blank=True, null=True)
    segmento_anterior_2 = models.CharField(max_length=100, blank=True, null=True)
    cargo_anterior_2 = models.CharField(max_length=50, blank=True, null=True)
    data_inicio_anterior_2 = models.DateField(blank=True, null=True)
    data_saida_anterior_2 = models.DateField(blank=True, null=True)
    atribuicoes_anterior_2 = models.TextField(max_length=200, blank=True, null=True)

    cargo_pretendido = models.CharField(max_length=100)
    faixa_salarial_desejada = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
