#from django.contrib import admin
#from inventario_2.apps.mercancia.models import cliente,producto,camposPrueba


#admin.site.register(cliente)
#admin.site.register(producto)
#admin.site.register(camposPrueba)


from django.contrib import admin
from suescunet.apps.articulos.models import articulos_model

admin.site.register(articulos_model)