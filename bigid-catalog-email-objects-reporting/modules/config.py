import yaml, os
import modules.create_access_token as access_token

# Set parent directory
path = os.path.abspath(__file__)
dir_path = os.path.dirname(os.path.dirname(path))

# Get configuration from yaml file
try:
    # Run this if executing from cx_Freeze binary
    with open(dir_path + '/../env_config.yaml', "r") as f:
        config_yaml = yaml.safe_load(f)
except:
    #Run this if executing from python interpreter
    with open(dir_path + '/env_config.yaml', "r") as f:
        config_yaml = yaml.safe_load(f)

print('env_config.yaml found in: ' + dir_path + '/')

# Set global variables with values from yaml file
bigid_url = config_yaml['BigID Server'][0]['bigid_url']
refresh_token = config_yaml['BigID Server'][1]['bigid_auth_token']
catalog_export_path = config_yaml['Script Parameters'][0]['catalog_export_file_path']
final_reports_path = config_yaml['Script Parameters'][1]['final_reports_folder_path']
max_threads = config_yaml['Script Parameters'][2]['max_threads']

bigid_auth_token = access_token.get_access_token()