# Cloud CLI Uploader - Python

## Upload files from your local system to Microsoft Azure using a CLI

> <sub>To get started, you first need to have a Microsoft Azure account. If you don't have one, you can create a free account [here.](https://azure.microsoft.com/en-us/free/search/?&ef_id=_k_Cj0KCQiA4NWrBhD-ARIsAFCKwWv39zVXs4ww7bj_IGmTJngZol8ZX835NOuvRgv7ygSk_rEe9lnrcGcaAg2vEALw_wcB_k_&OCID=AIDcmm5edswduu_SEM__k_Cj0KCQiA4NWrBhD-ARIsAFCKwWv39zVXs4ww7bj_IGmTJngZol8ZX835NOuvRgv7ygSk_rEe9lnrcGcaAg2vEALw_wcB_k_&gad_source=1&gclid=Cj0KCQiA4NWrBhD-ARIsAFCKwWv39zVXs4ww7bj_IGmTJngZol8ZX835NOuvRgv7ygSk_rEe9lnrcGcaAg2vEALw_wcB)</sub>

- **What the Python Program does:**

  - This program takes a file from your local system and will upload it to an Azure Storage Account all through a command line interface of your choice. Run the program file `main.py` once all values are set inside your locally cloned file.

- **How to use the CLI Uploader:**
  1. Input your "Azure Storage Key" into the `STORAGE_ACCOUNT_KEY` constant.
  2. Input your "Azure Storage Account Name" into the `STORAGE_ACCOUNT_NAME` constant.
  3. Input your "Container Connection String" into the `CONNECTION_STRING` constant.
  4. Input your "Container Name" into the `CONTAINER_NAME` constant.
  5. Run the `main.py` file and provide the file path when prompted and the file name when prompted.
