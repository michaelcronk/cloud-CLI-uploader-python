from azure.storage.blob import BlobServiceClient

STORAGE_ACCOUNT_KEY = ""
STORAGE_ACCOUNT_NAME = ""
CONNECTION_STRING = ""
CONTAINER_NAME = ""

def uploadFileToBlob(file_path, file_name):
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file_name)

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)
    print(f"Uploaded {file_name} to {STORAGE_ACCOUNT_NAME}.")


file_path = input("file path: ")
file_name = input("file name: ")

uploadFileToBlob(file_path, file_name)