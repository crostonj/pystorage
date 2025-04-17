from azure_blob_utils import AzureBlobStorageHelper

# Your Azure Blob Storage connection string
connection_string = "DefaultEndpointsProtocol=https;AccountName=...;AccountKey=...;EndpointSuffix=core.windows.net"
container_name = "my-container"
local_file_path = "sample_upload.txt"
blob_name = "uploaded_sample.txt"
download_path = "downloaded_sample.txt"

# Create a helper instance
blob_helper = AzureBlobStorageHelper(connection_string, container_name)

# Upload a file
blob_helper.upload_file(local_file_path, blob_name)
print(f"Uploaded '{local_file_path}' as blob '{blob_name}'")

# List blobs in the container
blobs = blob_helper.list_blobs()
print("Blobs in container:", blobs)

# Download it back
blob_helper.download_file(blob_name, download_path)
print(f"Downloaded blob to '{download_path}'")
