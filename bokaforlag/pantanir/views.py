from django.shortcuts import render, redirect

from .models import Bok
from ..pantanir.forms import PontunBokaknippiForm

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Pontun



@staff_member_required
def admin_pontun_lysing(request, pk):
    pontun = get_object_or_404(Pontun, id=pk)
    return render(
        request,
        "admin/pantanir/pontun/lysing.html",
        {"pontun": pontun}
    )


def panta_bokaknippi(request):
    """Til að panta bókaknippið hans S (5 bækur)"""
    bok = Bok.objects.get(titill="Bókaknippi")
    if request.method == "GET":
        baekur = Bok.objects.exclude(titill="Bókaknippi")
        baekur = list(baekur)
        bokaknippi = Bok.objects.get(titill="Bókaknippi")
        # baekur_uppi = baekur[0:3]
        # baekur_nidri = baekur[3:5]
        # form = PontunBokaknippiForm(bok="Bókaknippi")
        form = PontunBokaknippiForm()
        ctx = {
            "baekur": baekur,
            "bokaknippi": bokaknippi,
            # "baekur_uppi": baekur_uppi,
            # "baekur_nidri": baekur_nidri,
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
        else:
            baekur = Bok.objects.exclude(titill="Bókaknippi")
            baekur = list(baekur)
            bokaknippi = Bok.objects.get(titill="Bókaknippi")
            form_error = "Athugið: Fylla þarf út í alla stjörnumerkta reiti!"
            ctx = {
                "baekur": baekur,
                "bokaknippi": bokaknippi,
                "form": form,
                "form_error": form_error,
            }
            return render(request, "pantanir/panta_bokaknippi.html", ctx)

def pontun_tokst(request):
    return render(request, "pantanir/pontun_tokst.html")
