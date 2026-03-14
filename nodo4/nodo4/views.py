import os
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def receive_file(request):

    #Obtiene el archivo
    archivo = request.FILES.get('file')

    #Valida si el archivo siquiera existe
    if not archivo:
        return Response({"error": "No se recibió archivo"}, status=400)

    #Lee el contenido del archivo
    contenido = archivo.read().decode('utf-8') #Debo investigar qué significa utf-8

    lineas = contenido.splitlines() #INVESTIGAR QUÉ HACE ESTA LÍNEA

    total_lineas = len(lineas)
    lineas_por_parte = total_lineas // 5

    #Nodo 1 toma la primera parte
    inicio = lineas_por_parte * 3
    fin = lineas_por_parte * 4

    fragmento_lineas = lineas[inicio:fin]

    # Crear carpeta del nodo
    carpeta_nodo = os.path.join(settings.BASE_DIR, "upload/")
    os.makedirs(carpeta_nodo, exist_ok=True)

    nombre_fragmento = f"{archivo.name}_parte4.txt"
    ruta_fragmento = os.path.join(carpeta_nodo, nombre_fragmento)

    # Guardar fragmento
    with open(ruta_fragmento, "w", encoding="utf-8") as f:
        for linea in fragmento_lineas:
            f.write(linea + "\n")

    return Response({
        "mensaje": "Nodo 4 guardó su fragmento",
        "lineas_guardadas": len(fragmento_lineas),
        "ruta": ruta_fragmento
    })