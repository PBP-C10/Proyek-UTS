from django.urls import path
from MyLib.views import show_myLib, BookTracker, EditTracker, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'MyLib'

urlpatterns = [
    path('', show_myLib, name='show_myLib'),
    path('BookTracker', BookTracker, name='BookTracker'),
    path('EditTracker', EditTracker, name='EditTracker'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]