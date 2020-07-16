from django.urls import include,path
from my_portfolio import views

app_name = "my_portfolio"

urlpatterns = [
    path('',views.home,name='home'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('contact',views.contact,name='contact'),
    path('contact_form_submit',views.contact_form_submit,name='contact_form_submit'),
]

