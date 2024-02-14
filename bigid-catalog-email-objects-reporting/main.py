import concurrent.futures
from datetime import datetime
import modules

# Record the start time
start_time = datetime.now()
print(f"Process start time: {start_time}")

# Get all email object Fully Qualified Names from catalog export
print('getting list of email objects from csv export...')
csv_file_path = modules.catalog_export_path
email_objects = modules.get_email_objects(csv_file_path)

# Create BigID refresh access token from access token in config file 
bigid_auth_token = modules.create_access_token.get_access_token()

# Get To: and/or Cc: fields and all other report fields for each email object and write to individual CSV files per email account.
# Run multithreaded with the configured thread count to reduce runtime. 5 threads has been tested to be the most efficient.
print('creating new individual csv reports...')
loop_counter = 0
with concurrent.futures.ThreadPoolExecutor(modules.max_threads) as executor:
    for object in email_objects:
        loop_counter += 1
        executor.submit(modules.process_email_object, object, loop_counter, bigid_auth_token)

# Record the end time and calculate total runtime
end_time = datetime.now()
total_run_time = end_time - start_time
print(f"Process started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Process finished at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Total run time: {total_run_time}")
input("Press Enter to exit...")