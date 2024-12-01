from storages.backends.gcloud import GoogleCloudStorage
from google.cloud import storage
from google.oauth2 import service_account


class MediaStorage(GoogleCloudStorage):
    ruta_credenciales = 'Google\coocon-f8fd0ce41f93.json'
    credenciales = service_account.Credentials.from_service_account_file(ruta_credenciales)

# Nombre del bucket
    bucket_name = 'coocon'

# Inicializar cliente
    client = storage.Client(credentials=credenciales)
    bucket = client.bucket(bucket_name)

