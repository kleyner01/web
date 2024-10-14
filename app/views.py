import os
import json
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import render
from . import metrics


@login_required(login_url='login')
def home(request):
    product_metrics = metrics.get_product_metrics()
    sales_metrics = metrics.get_sales_metrics()
    daily_sales_data = metrics.get_daily_sales_data()
    daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()
    graphic_product_category_metric = metrics.get_graphic_product_category_metric()
    graphic_product_brand_metric = metrics.get_graphic_product_brand_metric()

    context = {

        'product_metrics': product_metrics,
        'sales_metrics': sales_metrics,
        'daily_sales_data': json.dumps(daily_sales_data),
        'daily_sales_quantity_data': json.dumps(daily_sales_quantity_data),
        'product_count_by_category': json.dumps(graphic_product_category_metric),
        'product_count_by_brand': json.dumps(graphic_product_brand_metric),
    }
    return render(request, 'home.html', context)


def quem_somos(request):
    # Caminho para a pasta de imagens dentro de static/path/somos
    image_dir = os.path.join(settings.BASE_DIR, 'static', 'path', 'somos')  # Caminho absoluto para o diretório de imagens
    video_dir = os.path.join(settings.BASE_DIR, 'static', 'path', 'somos', 'videos')  # Caminho absoluto para o diretório de vídeos

    # Verifica se o diretório existe e lista os arquivos de imagem e vídeo
    if os.path.exists(image_dir):
        image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    else:
        image_files = []  # Se o diretório não existir, lista estará vazia

    if os.path.exists(video_dir):
        video_files = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]
    else:
        video_files = []

    # URL para acessar os arquivos estáticos
    image_url = os.path.join(settings.STATIC_URL, 'path/somos')
    video_url = os.path.join(settings.STATIC_URL, 'path/somos/videos')

    context = {
        'image_files': image_files,
        'video_files': video_files,
        'image_url': image_url,
        'video_url': video_url
    }

    return render(request, 'quem_somos.html', context)


def parceiros(request):
    # Caminho para o diretório de imagens dos parceiros
    image_dir = os.path.join(settings.STATICFILES_DIRS[0], 'path', 'parceiros')

    # Filtrar arquivos de imagem (qualquer formato)
    image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # Caminho para as imagens no template
    image_url = '/static/path/parceiros'

    # Passar a lista de imagens para o template
    context = {
        'image_files': image_files,
        'image_url': image_url,
    }

    return render(request, 'parceiros.html', context)


def lojas(request):
    # Dados das lojas
    lojas_info = [
        {
            'nome': 'Cuiabá - Miguel Sutil',
            'endereco': 'Av. Miguel Sutil, 14299',
            'bairro': 'Porto',
            'cep': '78025-700',
            'telefone': '(65) 3637-1010',
            'latitude': '-15.5963',  # Exemplo de latitude
            'longitude': '-56.0961',  # Exemplo de longitude
            'imagem': 'path/lojas/3_SSF.jpg',  # Caminho para a imagem
        },
        {
            'nome': 'Cuiabá - Coxipó',
            'endereco': 'Av. Fernando Corrêa da Costa, 3700 - Coxipó da Ponte',
            'bairro': 'Shangri-lá',
            'cep': '78015-285',
            'telefone': '(65) 3627-2777',
            'latitude': '-15.6000',
            'longitude': '-56.1000',
            'imagem': 'path/lojas/2_SSF.jpg',  # Caminho para a imagem
        },
        {
            'nome': 'Sinop - MT',
            'endereco': 'Av. das Figueiras, 60 - Quadra R-21E',
            'bairro': 'Setor Industrial Norte',
            'cep': '78557-457',
            'telefone': '(66) 3531-5544',
            'latitude': '-15.6100',
            'longitude': '-56.1100',
            'imagem': 'path/lojas/8_SSF.jpg',  # Caminho para a imagem
        },
        {
            'nome': 'Rondonópolis - MT',
            'endereco': 'Av. Presidente Médici, 4640',
            'bairro': 'Vila José Luis',
            'cep': '78705-100',
            'telefone': '(66) 3423-4000',
            'latitude': '-15.6200',
            'longitude': '-56.1200',
            'imagem': 'path/lojas/9_SSF.jpg',  # Caminho para a imagem
        },
        {
            'nome': 'Várzea Grande - MT',
            'endereco': 'Av. Gov. Júlio Campos, 3881',
            'bairro': 'Centro',
            'cep': '78110-000',
            'telefone': '(65) 3684-1300',
            'latitude': '-15.6200',
            'longitude': '-56.1200',
            'imagem': 'path/lojas/5_SSF.jpg',  # Caminho para a imagem
        },
        {
            'nome': 'Cáceres - MT',
            'endereco': 'R. Padre Cassimiro, 1371',
            'bairro': 'Centro',
            'cep': '78200-000',
            'telefone': '(65) 3223-9898',
            'latitude': '-15.6200',
            'longitude': '-56.1200',
            'imagem': 'path/lojas/6_SSF.jpg',  # Caminho para a imagem
        },
        {
            'nome': 'Tangará da Serra - MT',
            'endereco': 'Av. Brasil, 1510W',
            'bairro': 'Nações Unidas',
            'cep': '78300-000',
            'telefone': '(65) 3325-1818',
            'latitude': '-15.6200',
            'longitude': '-56.1200',
            'imagem': 'path/lojas/7_SSF.jpg',  # Caminho para a imagem
        },
        {
            'nome': 'Cuiabá - CPA III',
            'endereco': 'Rua Trinta e Três, Nº 31 - Quadra 58, Setor III',
            'bairro': 'CPA III',
            'cep': '78058-300',
            'telefone': '(65) 3646-4422',
            'latitude': '-15.6200',
            'longitude': '-56.1200',
            'imagem': 'path/lojas/4_SSF.jpg',  # Caminho para a imagem
        },
        {
            'nome': 'Primavera do Leste - MT',
            'endereco': 'Rua Nova Esperança, 18',
            'bairro': 'Cidade Primavera I',
            'cep': '78850-000',
            'telefone': '(65) 2222-2222',
            'latitude': '-15.6200',
            'longitude': '-56.1200',
            'imagem': 'path/lojas/12_SSF.jpg',  # Caminho para a imagem
        },
        {
            'nome': 'Alta Floresta - MT',
            'endereco': 'Av. Julio José de Campos, s/nº - Quadra B1',
            'bairro': 'Setor Industrial',
            'cep': '78580-000',
            'telefone': '(66) 3521-5700',
            'latitude': '-15.6200',
            'longitude': '-56.1200',
            'imagem': 'path/lojas/14_SSF.jpg',  # Caminho para a imagem
        },
        {
            'nome': 'Lucas do Rio Verde - MT',
            'endereco': 'Av. Amazonas, 493-S - Quadra 17 Lote 15',
            'bairro': 'Centro',
            'cep': '78455-000',
            'telefone': '(65) 3549-2777',
            'latitude': '-15.6200',
            'longitude': '-56.1200',
            'imagem': 'path/lojas/13_SSF.jpg',  # Caminho para a imagem
        },
        {
            'nome': 'Cuiabá - Distrito Indústrial',
            'endereco': 'Av. Fernando Correa da Costa , s/n - Km13',
            'bairro': 'Pascoal Ramos',
            'cep': '78000-002',
            'telefone': '(65) 3667-4500',
            'latitude': '-15.6200',
            'longitude': '-56.1200',
            'imagem': 'path/lojas/1_SSF.jpg',  # Caminho para a imagem
        },
        {
            'nome': 'Água Boa',
            'endereco': 'Av. Industrial, 1730, Lote 01, Qdra 59',
            'bairro': 'Industrial V',
            'cep': '78635-000',
            'telefone': '(66) 3468-5100',
            'latitude': '-15.6200',
            'longitude': '-56.1200',
            'imagem': 'path/lojas/1_SSF.jpg',  # Caminho para a imagem
        },
    ]

    context = {
        'lojas': lojas_info,
    }

    return render(request, 'lojas.html', context)
