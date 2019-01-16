from django.shortcuts import render

from .models import Bok
from ..myndir.models import Mynd


def baekur_forsida(request):
    baekur = (Bok.objects
              .exclude(titill="Bókaknippi")
              .filter(hofundur__nafn="Sverrir Norland"))
    count = 4
    b1 = baekur.filter(id__lte=count)
    b2 = baekur.filter(id__gte=count)
    ctx = {"baekur": baekur, "baekur1": b1, "baekur2": b2}
    return render(request, "baekur/baekur_forsida.html", ctx)


def bokaknippi(request):
    bokaknippi = Bok.objects.get(titill="Bókaknippi")
    baekur = Bok.objects.exclude(titill="Bókaknippi")
    myndir = Mynd.objects.all()
    ctx = {
        "bokaknippi": bokaknippi,
        "baekur": baekur,
        "myndir": myndir,
    }
    return render(request, "baekur/bokaknippi.html", ctx)


def baekur_lysing(request, pk):
    bok = Bok.objects.get(pk=pk)
    baekur = Bok.objects.exclude(titill="Bókaknippi")
    n_baekur = baekur.count()
    baekur_pks = [x.pk for x in baekur]
    bok_index = baekur_pks.index(pk)
    if n_baekur > 1:
        if bok_index == 0:
            fyrri = -1
            naesta = baekur_pks[bok_index + 1]
        elif bok_index == n_baekur - 1:
            fyrri = baekur_pks[bok_index - 1]
            naesta = -1
        else:
            fyrri = baekur_pks[bok_index - 1]
            naesta = baekur_pks[bok_index + 1]
    else:
        fyrri = -1
        naesta = -1
    ctx = {
        "bok": bok,
        "fyrri": fyrri,
        "naesta": naesta,
    }
    return render(request, "baekur/baekur_lysing.html", ctx)
