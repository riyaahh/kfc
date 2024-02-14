from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('registration',views.registration,name='registration'),
    path('page1',views.page1,name="page1"),
    path('page2',views.page2,name="page2"),
    path('signin',views.signin,name="signin"),
    path('profileform/<int:id>/',views.profileform,name="profileform"),
    path('updateform/<int:id>/',views.updateform,name="updateform"),
    path('delete/<str:id>',views.delete,name="delete"),
    path('table/<int:id>/',views.table,name="table"),

]