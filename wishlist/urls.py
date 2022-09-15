from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import export_to_xml
from wishlist.views import export_to_json
from wishlist.views import export_xml_id
from wishlist.views import export_json_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', export_to_xml, name = 'export_to_xml'),
    path('json/', export_to_json, name = 'export_to_json'),
    path('xml/<int:id>', export_xml_id, name= 'export_xml_id'),
    path('json/<int:id>', export_json_id, name= 'export_json_id')
]