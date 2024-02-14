import re, requests, urllib3
from urllib.parse import urlencode
import modules.config as config

# Extract email directory path from the fullyQualifiedName
object_directory_pattern = r'(?:\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}\b)(.+\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}\b)'

# Use email object FQN to retrieve CSV report fields from the BigID data catalog API and store them in a dictionary
def get_fields_for_csv(object, bigid_auth_token):

    headers = {
    'Authorization': bigid_auth_token
    }

    # URL encode the fully qualified name
    encoded_fqn = urlencode({'object_name': object})
    # Suppress non https warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = requests.request("GET", config.bigid_url + '/api/v1/data-catalog/object-details/?' + encoded_fqn, headers=headers, verify=False).json()

    # Replace original attribute names with business names
    replacements = {'LONG DESCRIPTION': 'ICD9 Description', 'classifier.PatientID': 'Companyname PatientID'}
    response["data"]["attribute"] = [replacements.get(item, item) for item in response["data"]["attribute"]]

    report_row = {}
    report_row["Owner"] = response["data"]["owner"]
    report_row["Created Date"] = response ["data"]["created_date"]
    report_row["Email Message"] = response["data"]["objectName"]
    report_row["Sensitive Data Found"] = response["data"]["attribute"]
    # If the To and/or CC fields are empty, set to NONE
    report_row["To: Email List"] = response["data"]["additionalProperties"].get("To", "NONE")
    report_row["Cc: Email List"] = response["data"]["additionalProperties"].get("CC", "NONE")
    report_row["Email Path"] = re.search(object_directory_pattern, response["data"]["fullyQualifiedName"]).group(1)

    return report_row