import kubernetes as k8s
from kubernetes.client.models import V1ConfigMap


class ConfigMapManager:
    """
    Clase para crear ConfigMaps en Kubernetes.

    Atributos:
        - k8s_client: Cliente de la API de Kubernetes.

    Métodos:
        - crear_configmap(nombre, datos): Crea un ConfigMap con el nombre y datos especificados.
    """

    def __init__(self, k8s_client):
        self.k8s_client = k8s_client

    def crear_configmap(self, nombre, datos):
        """
        Crea un ConfigMap con el nombre y datos especificados.

        Argumentos:
            - nombre: Nombre del ConfigMap.
            - datos: Diccionario con los datos del ConfigMap.

        Retorna:
            - V1ConfigMap: Objeto ConfigMap creado.
        """

        # Crear objeto ConfigMap
        configmap = V1ConfigMap(
            metadata=k8s.client.V1ObjectMeta(name=nombre),
            data=datos,
        )

        # Crear ConfigMap en Kubernetes
        api_response = self.k8s_client.CoreV1Api.create_namespaced_config_map(
            namespace="default", body=configmap
        )

        # Devolver el ConfigMap creado
        return api_response.to_dict()


# Ejemplo de uso
k8s_client = k8s.client.ApiClient()

configmap_manager = ConfigMapManager(k8s_client)

# Crear un ConfigMap con datos literales
datos_literales = {
    "clave1": "valor1",
    "clave2": "valor2",
}

configmap_manager.crear_configmap(nombre="configmap-literal", datos=datos_literales)

# Crear un ConfigMap desde un directorio
datos_directorio = {"directorio": "/ruta/al/directorio/con/archivos"}

configmap_manager.crear_configmap(nombre="configmap-directorio", datos=datos_directorio)
