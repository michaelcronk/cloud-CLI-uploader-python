# Cloud CLI Uploader - Python

## Upload files from your local system to Microsoft Azure using a CLI

> <sub>To get started, you first need to have a Microsoft Azure account. If you don't have one, you can create a free account [here.](https://azure.microsoft.com/en-us/free/search/?&ef_id=_k_Cj0KCQiA4NWrBhD-ARIsAFCKwWv39zVXs4ww7bj_IGmTJngZol8ZX835NOuvRgv7ygSk_rEe9lnrcGcaAg2vEALw_wcB_k_&OCID=AIDcmm5edswduu_SEM__k_Cj0KCQiA4NWrBhD-ARIsAFCKwWv39zVXs4ww7bj_IGmTJngZol8ZX835NOuvRgv7ygSk_rEe9lnrcGcaAg2vEALw_wcB_k_&gad_source=1&gclid=Cj0KCQiA4NWrBhD-ARIsAFCKwWv39zVXs4ww7bj_IGmTJngZol8ZX835NOuvRgv7ygSk_rEe9lnrcGcaAg2vEALw_wcB)</sub>

This project takes a file from your local system and will upload it to an Azure Storage Account all through a command line interface, in this example it will be through the terminal on MacOS.

- **How to use the CLI Uploader:**
  - Input your "Azure Storage Key" into the `STORAGE_ACCOUNT_KEY` constant.
  - Input your "Azure Storage Account Name" into the `STORAGE_ACCOUNT_NAME` constant.
  - Input your "Connection String" into the `CONNECTION_STRING` constant.
  - Input your "Container Name" into the `CONTAINER_NAME` constant.
  - Run the `main.py` file and provide the file path when prompted and the file name when prompted.
