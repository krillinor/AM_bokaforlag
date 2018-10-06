from django.shortcuts import render

from .models import Bok, Hofundur



def baekur_listi(request):
    baekur = Bok.objects.all()
    ctx = {"baekur": baekur}
    return render(request, "baekur/baekur_listi.html", ctx)


def baekur_lysing(request, pk):
    bok = Bok.objects.get(pk=pk)

    # TODO tækla ef bara ein bók
    baekur = Bok.objects.all()
    n_baekur = len(baekur)
    baekur_pks = [x.pk for x in baekur]
    bok_index = baekur_pks.index(pk)
    if bok_index == 0:
        fyrri = -1
        naesta = baekur_pks[bok_index + 1]
    elif bok_index == n_baekur - 1:
        fyrri = baekur_pks[bok_index - 1]
        naesta = -1
    else:
        fyrri = baekur_pks[bok_index - 1]
        naesta = baekur_pks[bok_index + 1]
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
