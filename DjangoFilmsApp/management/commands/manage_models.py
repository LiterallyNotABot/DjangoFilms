from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    help = 'Set managed=True for all models in models.py'

    def handle(self, *args, **kwargs):
        models_file_path = 'DJangoFilmsApp/models.py'  # Cambia esto a la ruta real

        # Estado actual y deseado para managed
        current_managed_state = False  # Cambia esto a False si necesitas que el estado inicial sea False
        desired_managed_state = True  # Cambia esto a True si necesitas que el estado final sea True

        # Determinar los valores de managed según los estados
        current_value = 'managed = True' if current_managed_state else 'managed = False'
        new_value = 'managed = True' if desired_managed_state else 'managed = False'

        with open(models_file_path, 'r') as file:
            lines = file.readlines()

        # Reemplazar las líneas de managed
        lines = [line.replace(current_value, new_value) for line in lines]

        # Escribir las líneas modificadas de vuelta al archivo
        with open(models_file_path, 'w') as file:
            file.writelines(lines)

        print(f"managed set to {new_value} for all models in models.py")

