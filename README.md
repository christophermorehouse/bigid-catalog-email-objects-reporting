# bigid-catalog-email-objects-reporting
Automation utility that enriches email objects report exported from BigID with the cc list

## Author
Christopher Morehouse

## Description
By default, when exporting a csv reporting from the BigID catalog, the CC: field is not included. However, this field does exist in the BigID catalog api, so it is information that BigID extracts when scanning email objects. Including this CC: field in reports can help identify other recipients of emails that may have contained sensitive data. This information can help with data remediation processes.

This utility takes the csv export from a BigID catalog and does a lookup for every email object in the report, extracts the emaili object CC: list, and enriches the report with this information. A new enriched csv is produced as a result.

## Script Configuration

Before running the utility, you will need to generate a refresh token. Refresh tokens are obtained from the BigID UI under Administration -> Access Management.
You will need to create the refresh token under a user who has the proper roles configured for making API calls.
Refer to the BigID documentation for specifics on users and roles.

Once you have the refresh token, edit the env_config.yaml with the proper environment settings:

```yaml

Script Parameters:
- catalog_export_file_path: "The source path of the BigID catalog export csv file"
- final_reports_folder_path: "The destination path where the new enriched csv file will get written"
- max_threads: "number of threads the utility will run. this is 5 by default"

BigID Server:
- bigid_url: "URL of BigID server. example - https://bigidhost.com"
- bigid_auth_token: "Refresh token generated under BigID UI: Administration -> Access Management -> User"
```

Save the changes to the yaml config file and execute the script.

## Running the script

To execute the script using a python interpreter, you will first need to import the dependencies in the requirements.txt.
You can do this by running the following command: 

```sh
pip install -r requirements.txt
```

Once dependencies are installed, run the script with the following command: 

```sh
python main.py
```

## Build an executable binary for deployment

The preferred method for deployment is to build a self-contained package that includes all the dependencies as well as a run-time environment.
Using this method, users will not have to install python or any dependency libraries. They just edit the env_config.yaml and execute the binary.

cx_Freeze is used to build the binary and will need to be installed first in order to create the deployment package. For more information on cx_Freeze:

Project page: https://pypi.org/project/cx-Freeze/

Project documentation: https://cx-freeze.readthedocs.io/en/latest/

You can install cx_Freeze in a Python environment by running the following command:

```sh
pip install --upgrade cx_Freeze
```

Once cx_Freeze is installed you can continue with building the self-contained package by executing the build.sh script with the following command: 

For Windows:
```sh
./build.ps1
```

For Linux:
```sh
./build.sh
```