'''

import os
import sys

# Asegúrate de estar en el entorno virtual adecuado
# y de tener configurada la variable de entorno para Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pDjangoFilms.pDjangoFilms.settings')
import django
django.setup()

from django.apps import apps

# Cambia 'DjangoFilmsApp' por el nombre de tu aplicación
app_name = 'DjangoFilmsApp'

# Obtén todos los modelos de la aplicación
models = apps.get_app_config(app_name).get_models()

#setteamos a true o false
state=True

# Cambia `managed` a True en cada modelo
for model in models:
    if hasattr(model.Meta, 'managed'):
        model.Meta.managed = state
        print(f"{model.__name__}: managed set to "+str(state))

# Puedes guardar el archivo de modelos después de modificar
'''

import os
import sys
from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    help = 'Set managed state of all models in the DjangoFilmsApp'

    def handle(self, *args, **options):
        # Asegúrate de que estás en el entorno correcto
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pDjangoFilms.settings')

        # Inicia Django
        import django
        django.setup()

        app_name = 'DjangoFilmsApp'  # Cambia esto si es necesario
        models = apps.get_app_config(app_name).get_models()
        state = True  # Cambia a False si deseas desactivar

        for model in models:
            if hasattr(model._meta, 'managed'):
                model._meta.managed = state
                self.stdout.write(f"{model.__name__}: managed set to {state}")
