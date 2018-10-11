from django.shortcuts import render, redirect

from .models import Bok
from ..pantanir.forms import PontunBokaknippiForm



def panta_bokaknippi(request):
    """Til að panta bókaknippið hans S (5 bækur)"""
    bok = Bok.objects.get(titill="Bókaknippi")
    if request.method == "GET":
        baekur = Bok.objects.exclude(titill="Bókaknippi")
        baekur = list(baekur)
        baekur_uppi = baekur[0:3]
        baekur_nidri = baekur[3:5]
        # form = PontunBokaknippiForm(bok="Bókaknippi")
        form = PontunBokaknippiForm()
        ctx = {
            "baekur_uppi": baekur_uppi,
            "baekur_nidri": baekur_nidri,
            "form": form,
        }
        return render(request, "pantanir/panta_bokaknippi.html", ctx)
    else:
        # form = PontunBokaknippiForm(request.POST, bok="Bókaknippi")
        form = PontunBokaknippiForm(request.POST)
        if form.is_valid():
            form_bok = form.save(commit=False)
            form_bok.bok = bok
            verd = bok.verd
            magn = form.cleaned_data["magn"]
            form_bok.verd = verd * magn
            form_bok.save()
            form.save_m2m()
            return redirect("pantanir:pontun_tokst")
        # else:
            # TODO

def pontun_tokst(request):
    return render(request, "pantanir/pontun_tokst.html")
