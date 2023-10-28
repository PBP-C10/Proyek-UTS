from django.urls import path
from myLibrary.views import show_myLibrary, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, edit_product, reset_product, edit_quote, get_product_json, add_product_ajax

app_name = 'myLibrary'

urlpatterns = [
    path('', show_myLibrary, name='show_myLibrary'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('reset/<int:id>', reset_product, name='reset_product'),
    path('edit-quote/<int:id>', edit_quote, name='edit_quote'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax')
]