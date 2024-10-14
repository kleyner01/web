from django import forms
from django.core.exceptions import ValidationError
from localflavor.br.forms import BRCPFField
from .models import Candidato
import re


def validate_cep(value):
    # Valida se o CEP está no formato XXXXX-XXX
    if not re.match(r'^\d{5}-\d{3}$', value):
        raise ValidationError('O CEP deve estar no formato: XXXXX-XXX')


class CandidatoForm(forms.ModelForm):
    data_nasc = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='Data Nascimento:'
    )

    POSITIVO_NEGATIVO = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]

    SÉRIES_CARTEIRA = [
        ('serie_a', 'Série A'),
        ('serie_b', 'Série B'),
        ('serie_c', 'Série C'),
        ('serie_d', 'Série D'),
    ]

    TIPOS_HABILITACAO = [
        ('tipo_a', 'A'),
        ('tipo_b', 'B'),
        ('tipo_c', 'C'),
        ('tipo_d', 'D'),
    ]

    ESTADO = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]

    estado = forms.ChoiceField(
        choices=ESTADO,
        label='Selecione Estado',
        widget=forms.Select(attrs={'class': 'form-control'})  # Adiciona uma classe de formatação
    )

    possui_habilitacao = forms.ChoiceField(
        choices=POSITIVO_NEGATIVO,
        widget=forms.RadioSelect,
        label='Possui habilitação?'
    )

    carteira_profissional = forms.ChoiceField(
        choices=POSITIVO_NEGATIVO,
        widget=forms.RadioSelect,
        label='Possui Carteira Profissional?'
    )

    serie_carteira_profissional = forms.ChoiceField(
        choices=SÉRIES_CARTEIRA,
        label='Série da Carteira Profissional',
        widget=forms.Select
    )

    tipo_habilitacao = forms.MultipleChoiceField(
        choices=TIPOS_HABILITACAO,
        widget=forms.CheckboxSelectMultiple,
        label='Tipo de Habilitação'
    )

    cpf = BRCPFField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'CPF',
        'required': True}))

    cep = forms.CharField(
        max_length=10,
        validators=[validate_cep],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: 12345-678',
            'required': True
        })
    )

    class Meta:
        model = Candidato
        fields = '__all__'  # Inclui todos os campos do modelo

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome', 'required': True}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu sobrenome', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu email', 'required': True}),
            'prefixo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: +55'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Celular'}),
            'curriculo': forms.FileInput(attrs={'class': 'form-control'}),
            'foto_perfil': forms.FileInput(attrs={'class': 'form-control'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva sua mensagem', 'rows': 3}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço completo'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'data_nasc': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado_civil': forms.Select(attrs={'class': 'form-select'}),
            'rg': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RG'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'nome_pai': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Pai'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Mãe'}),
            'possui_habilitacao': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tipo_habilitacao': forms.Select(attrs={'class': 'form-select'}),
            'carteira_profissional': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'serie_carteira_profissional': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Série da carteira'}),
            'formacao': forms.Select(attrs={'class': 'form-select'}),
            'curso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do curso'}),
            'ano_conclusao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ano de conclusão'}),
            'empresa_atual': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da empresa atual'}),
            'segmento_atual': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segmento'}),
            'cargo_atual': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cargo atual'}),
            'data_inicio_atual': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_saida_atual': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'atribuicoes_atual': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Atribuições na empresa atual'}),
            'empresa_anterior_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Empresa anterior 1'}),
            'segmento_anterior_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segmento'}),
            'cargo_anterior_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cargo anterior 1'}),
            'data_inicio_anterior_1': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_saida_anterior_1': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'atribuicoes_anterior_1': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Atribuições na empresa anterior 1'}),
            'empresa_anterior_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Empresa anterior 2'}),
            'segmento_anterior_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segmento'}),
            'cargo_anterior_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cargo anterior 2'}),
            'data_inicio_anterior_2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_saida_anterior_2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'atribuicoes_anterior_2': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Atribuições na empresa anterior 2'}),
            'cargo_pretendido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cargo pretendido'}),
            'faixa_salarial_desejada': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Faixa salarial'}),
        }
