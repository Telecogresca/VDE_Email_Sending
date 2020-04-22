from __future__ import absolute_import, unicode_literals
from torns.models import Torn
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from .models import mail_content

import datetime

from celery import task
from celery import shared_task


# Create your views here.
@task(name='send_emails')
def send_emails():
    # get values
    sub = mail_content.objects.first()
    field_sub = mail_content._meta.get_field('subject')
    subject = field_sub.value_from_object(sub)

    mes = mail_content.objects.first()
    field_mes = mail_content._meta.get_field('body')
    message = field_mes.value_from_object(mes)

    from_em = mail_content.objects.first()
    field_from_em = mail_content._meta.get_field('from_email')
    from_email = field_from_em.value_from_object(from_em)

    to_email_list = []
    torns_list = list(Torn.objects.all())

    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    for torn in torns_list:
        field_dmy = Torn._meta.get_field('date')
        dmy = field_dmy.value_from_object(torn)
        day, month, year = dmy.split('/')
        date_torn = datetime.date(int(year), int(month), int(day))

        if tomorrow == date_torn:
            field_nomb1 = Torn._meta.get_field('kapo1')
            kapo1 = field_nomb1.value_from_object(torn)

            field_nomb2 = Torn._meta.get_field('kapo2')
            kapo2 = field_nomb2.value_from_object(torn)

            field_to_em1 = Torn._meta.get_field('email1')
            to_email_list.append(field_to_em1.value_from_object(torn))

            field_to_em2 = Torn._meta.get_field('email2')
            to_email_list.append(field_to_em2.value_from_object(torn))

            field_day_w = Torn._meta.get_field('day_of_week')
            day_of_week = field_day_w.value_from_object(torn)

            field_day = Torn._meta.get_field('num_day')
            num_day = field_day.value_from_object(torn)

            field_sh = Torn._meta.get_field('start_h')
            start_h = field_sh.value_from_object(torn)

            field_fh = Torn._meta.get_field('finish_h')
            finish_h = field_fh.value_from_object(torn)

            salutacio = "Bon dia " + kapo1 + " i " + kapo2 + "!\n"
            recordatori = "Recordeu que demà " + day_of_week + " " + num_day + " teniu torn de Venda d'Entrades de " + \
                          start_h + " a " + finish_h + ".\n"

            body = salutacio + recordatori + message
            print(body)
            send_mail(subject=subject, message=body, from_email=from_email, recipient_list=to_email_list,
                      fail_silently=False)

    context = {}
    return to_email_list
