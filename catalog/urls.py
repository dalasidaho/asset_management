from django.urls import path
from . import views
from django.conf.urls import url
from .views import ListView, SearchResultsView

app_name = 'catalog'
urlpatterns = [
    path('', views.index, name='index1'),
    path('search/', SearchResultsView.as_view(), name='search_result'),
    url(r'^inventorys/$', views.InventoryListView.as_view(), name='inventory'),
    url(r'^devices/$', views.DeviceListView.as_view(), name='devices'),
    url(r'^device/(?P<pk>\d+)$', views.DeviceDetailView.as_view(), name='device-detail'),
    url(r'^customers/$', views.CustomerListView.as_view(), name='customers'),
    url(r'^customer/(?P<pk>\d+)$', views.CustomerDetailView.as_view(), name='customer_detail'),
    url(r'^trackers/$', views.TrackerListView.as_view(), name='trackers'),
    url(r'^tracker/(?P<pk>\d+)$', views.TrackerDetailView.as_view(), name='tracker_detail'),

]