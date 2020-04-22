from django.contrib import admin

# Register your models here.
from .models import mail_content

admin.site.register(mail_content)