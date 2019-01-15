from django.shortcuts import render, redirect

from .models import Bok
from ..pantanir.forms import PontunBokaknippiForm

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Pontun
from .utils import pontun_stadfestingarpostur

from ..myndir.models import Mynd


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
    bokaknippi = Bok.objects.get(titill="Bókaknippi")
    if request.method == "GET":
        myndir = Mynd.objects.all()
        form = PontunBokaknippiForm()
        ctx = {
            "bokaknippi": bokaknippi,
            "form": form,
            "myndir": myndir,
        }
        return render(request, "pantanir/panta_bokaknippi.html", ctx)
    else:
        form = PontunBokaknippiForm(request.POST)
        if form.is_valid():
            pontun = form.save(commit=False)
            pontun.bok = Bok.objects.get(titill="Bókaknippi")
            magn = form.cleaned_data["magn"]
            pontun.verd = pontun.bok.verd_m_afslaetti * magn
            pontun_stadfestingarpostur(pontun)
            pontun.save()
            form.save_m2m()
            return redirect("pantanir:pontun_tokst")
        else:
            form_error = "Athugið: Fylla þarf út í alla stjörnumerkta reiti!"
            ctx = {
                "bokaknippi": bokaknippi,
                "form": form,
                "form_error": form_error,
            }
            return render(request, "pantanir/panta_bokaknippi.html", ctx)


def pontun_tokst(request):
    return render(request, "pantanir/pontun_tokst.html")
