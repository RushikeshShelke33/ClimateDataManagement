from django.contrib import admin
from django.urls import path, include
from .import views as v
# from .views import AddData, ListData, ListDataByArea, ListDataByAreaAndClimate


urlpatterns = [
    # path('',v.home),
    # path('addemp',v.CreateEmp.as_view()),
    # path('lemp',v.ListEmp.as_view()),
    # path('gemp/<int:pk>',v.GetEmp.as_view()),
    # path('uemp/<int:pk>',v.UpdateEmp.as_view()),
    # path('demp/<int:pk>',v.DeleteEmp.as_view()),
    # path('lcemp',v.ListCreateEmp.as_view()),
    # path('gudemp/<int:pk>',v.GUDEmp.as_view()),
    #
    # path('list_create_data2/<int:area_code>/<str:climate>/',
    #  v.ListCreateData2.as_view(), name='list_create_data2'),

    # path('', v.home),
    # path('add_data/', v.AddData.as_view()),
    # path('list_data/', v.ListData.as_view()),
    # path('data/by_area/<int:area_code>/', v.ListCreateData.as_view()),
    # path('data/by_area_and_climate/<int:area_code>/<str:climate>/',v.ListCreateData2.as_view()),


    path('', v.home),

    path('add_data/', v.AddData.as_view(), name='add_data'),
    path('list_data/', v.ListData.as_view(), name='list_data'),
    path('data/by_area/<int:area_code>/',
         v.ListDataByArea.as_view(), name='data_by_area'),
    path('data/by_area_and_climate/<int:area_code>/<str:climate>/',
         v.ListDataByAreaAndClimate.as_view(), name='data_by_area_and_climate'),
    path('climate_delta/', v.ClimateDeltaView.as_view(), name='climate_delta'),


]
