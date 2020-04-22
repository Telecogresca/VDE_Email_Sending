"""tgk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from torns.views import torns_upload
from mail.tasks import send_emails

urlpatterns = [
    path('', include('mail.urls')),
    path('admin/', admin.site.urls),
    path('upload-csv/', torns_upload, name="torns_upload"),
    #path('send-emails/', send_emails),
]