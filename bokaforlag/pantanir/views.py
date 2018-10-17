from django.shortcuts import render, redirect

from .models import Bok
from ..pantanir.forms import PontunBokaknippiForm

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Pontun

from django.core.mail import EmailMessage, send_mail
from django.conf import settings



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

            # MAILSTUFF
            # labels:
            labels = []
            for field in form:
                labels.append(str(field.label))
            # values:
            values = []
            for key, value in form.cleaned_data.items():
                values.append(value)
            # textinn sjálfur
            form_texti = ''
            for label, value in zip(labels, values):
                form_texti = form_texti + str(label) + ': ' + str(value) + '\n'
            form_texti = form_texti + 'Verð: ' + str(form_bok.verd) + 'kr + sendingarkostnaður'
            # annað
            subject = 'Kærar þakkir fyrir pöntunina!'
            message = 'Kærar þakkir fyrir pöntunina! Þú færð glaðning í póstinum á næstu dögum.\n\nAM forlag\n\n\n\nPöntunarupplýsingar:\n\n' + form_texti
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form.cleaned_data["netfang"], 'amforlag@gmail.com',]
            send_mail(subject, message, email_from, recipient_list)


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
