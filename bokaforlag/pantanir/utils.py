from django.core.mail import send_mail
from django.conf import settings


# MAILSTUFF
def pontun_stadfestingarpostur(form):
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
        form_texti += str(label) + ': ' + str(value) + '\n'
    form_texti += 'Verð: ' + str(form.verd) + '. kr. auk sendingarkostnaðar'
    # annað
    subject = 'Kærar þakkir fyrir pöntunina!'
    message = ('Kærar þakkir fyrir pöntunina! '
               'Þú færð glaðning í póstinum á næstu dögum.\n')
    message += ('Krafa verður send í heimabankann þinn, '
                'frá sérlegum fjármálastjóra AM forlags, Jóni Norland, '
                'um leið og við höfum póstlagt bækurnar.\n\n')
    message += 'AM forlag\n\n\n\n'
    message += 'Pöntunarupplýsingar:\n\n' + form_texti
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [form.cleaned_data["netfang"], 'amforlag@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
