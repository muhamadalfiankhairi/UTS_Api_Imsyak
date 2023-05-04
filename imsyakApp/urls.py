from django.urls import path
from . import views

app_name='imsyakApp'

urlpatterns = [
    path('',views.readJadwal),
    path('detail/<int:id>',views.detailJadwal),
    path('buat/',views.createJadwal),
    path('edit/<int:id>',views.updateJadwal),
    path('hapus/<int:id>',views.deletJadwal),
]
