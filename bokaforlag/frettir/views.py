from django.shortcuts import render
from .models import Frett

def frettir_view(request):
    frettir = Frett.objects.all()
    return render(request, "frettir/frettir.html",
                  {"frettir_allar": frettir})
