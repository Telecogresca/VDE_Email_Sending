from django.db import models


# Create your models here.
class mail_content(models.Model):
    subject = models.CharField("assumpte", max_length=150, blank=True)
    from_email = models.EmailField("sender", default='********************@gmail.com')
    body = models.TextField("Missatge", blank=True)

    def __str__(self):
        return self.subject
