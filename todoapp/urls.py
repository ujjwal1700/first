from todoapp import views
from django.urls import path


urlpatterns=[
   path('',views.index,name="index"),
   path('delete/<id>/',views.delete,name="delete"),
   path('update/<id>/',views.update,name="update"),
   path('status/<id>',views.status,name="status"),

]
