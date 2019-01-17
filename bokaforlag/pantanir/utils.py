from django.core.mail import send_mail
from django.conf import settings


# MAILSTUFF
def pontun_senda_stadfestingarpost(form, pontun):
    # formið
    labels = [str(field.label) for field in form]
    values = list(form.cleaned_data.values())
    # textinn sjálfur
    form_texti = ''
    for label, value in zip(labels, values):
        form_texti += f'{str(label)}: {str(value)}\n'
    form_texti += f'Verð: {str(pontun.verd)} kr. auk sendingarkostnaðar'
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
