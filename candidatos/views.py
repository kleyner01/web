# web/candidatos/views.py
from django.shortcuts import render
from .forms import CandidatoForm


def CandidatoViews(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = CandidatoForm()

    return render(request, 'trabalhe_conoscos.html', {'form': form})
