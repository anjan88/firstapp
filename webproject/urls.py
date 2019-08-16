"""webproject URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from anjanapp.views import view1,view2,view3,view4,view5,view6,view7,form_name_view8, post_form_upload
from anjanapp.views import employee_record,insertemployee,model_form_upload,home,send_email,circular_nav
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^circularnavigation/',circular_nav,name='circular_nav'),
    url(r'^hello/', view1 ,name="view1"),
    url(r'^datetime/', view2 ,name="view2"),
    url(r'^redirect/', view3 ,name="view3"),
    url(r'^fruits/', view4, name="view4"),
    url(r'^connection1/', TemplateView.as_view(template_name='login.html')),
    url(r'^login/',view5,name='view5'),
    url(r'^connection2/', TemplateView.as_view(template_name='sum.html')),
    url(r'^add/',view6,name='view6'),
    url(r'^connection3/', TemplateView.as_view(template_name='loginpassword.html')),
    url(r'^signin/',view7,name='view7'),
    url(r'^formpage/',form_name_view8,name='form_name_view8'),
    url(r'^connection4/', TemplateView.as_view(template_name='table.html')),
    url(r'^hey/',post_form_upload,name='post_form_upload'),
    url(r'^getemployees/', employee_record, name='employee_record'),
    url(r'^newemployee/', TemplateView.as_view(template_name='forms_insertemployee.html')),
    url(r'^insertemployee/', insertemployee, name='insertemployee'),
    url(r'^home/',home,name='home'),
    url(r'^fileuploads/',model_form_upload, name='model_form_upload'),
    url(r'^mail/', TemplateView.as_view(template_name='mail.html')),
    url(r'^sendemail/',send_email,name='send_email'),

]
