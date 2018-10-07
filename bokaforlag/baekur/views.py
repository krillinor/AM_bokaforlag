from django.shortcuts import render, redirect

from .models import Bok, Hofundur
from ..pantanir.forms import PontunForm



def panta_baekur(request):
    """Til að panta bókaknippið hans S (5 bækur)"""
    if request.method == "GET":
        form = PontunForm(bok="Bókaknippi")
        ctx = {
            "form": form,
        }
        return render(request, "baekur/panta_baekur.html", ctx)
    else:
        form = PontunForm(request.POST, bok="Bókaknippi")
        if form.is_valid():
            form.save()
            return redirect("home")
        # else:
            # TODO


def baekur_forsida(request):
    baekur = Bok.objects.filter(hofundur__nafn="Sverrir Norland")
    ctx = {"baekur": baekur,}
    return render(request, "baekur/baekur_forsida.html", ctx)


def baekur_listi(request):
    baekur = Bok.objects.only("titill", "mynd")
    ctx = {"baekur": baekur}
    return render(request, "baekur/baekur_listi.html", ctx)


def baekur_lysing(request, pk):
    bok = Bok.objects.get(pk=pk)
    baekur = Bok.objects.all()
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


def hofundar_listi(request):
    hofundar = Hofundur.objects.all()
    ctx = {"hofundar": hofundar}
    return render(request, "baekur/hofundar_listi.html", ctx)

def hofundar_baekur(request, pk):
    hofundur = Hofundur.objects.get(pk=pk)
    baekur = hofundur.baekur.all()
    ctx = {
        "hofundur": hofundur,
        "baekur": baekur,
    }
    return render(request, "baekur/hofundar_baekur.html", ctx)
