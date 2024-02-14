import csv, os, re, threading
import modules.config as config
import modules.get_reporting_fields as get_reporting_fields

def process_email_object(object, loop_counter, bigid_auth_token):
    # Create directory where individual CSV reports get written to
    try:
        os.mkdir(config.final_reports_path)
        print("Creating reports_output folder")
        reports_folder = config.final_reports_path + "/"
    except:
        reports_folder = config.final_reports_path + "/"

    # Get To: and/or CC: fields as well as all other fields from BigID catalog to be used in individual CSV file reports
    report_output = get_reporting_fields.get_fields_for_csv(object, bigid_auth_token)

    # Get only email addresses in instances where there are additional strings/characters such as "fname.lname@company.com::In-Place Archive". In this example,
    # the extracted value would be fname.lname@company.com and will be used as the final csv file name.
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,3}\b'
    get_only_email = re.search(email_pattern, report_output["Owner"])
    report_owner = get_only_email.group()

    # Create a lock when creating a new csv to write the header row first before other parallel threads write data rows to the file
    header_lock = threading.Lock()

    # Check if csv already exists
    file_exists = os.path.exists(reports_folder + report_owner + ".csv")

    # Create a new csv report and use the owner email as the file name
    with open(reports_folder + report_owner + ".csv", 'a', newline='') as csv_file:
        # Remove the Owner element so we don't have this column in the final csv output
        report_output.pop('Owner', None)

        csv_writer = csv.DictWriter(csv_file, fieldnames=report_output.keys())

        # if the csv does not exist write out the header row, otherwise skip
        if not file_exists:
            # Acquire the lock to ensure the thread writing the header writes it first before other threads write the data rows.
            # Otherwise, the header may show up in the middle of the csv file.
            with header_lock:
                if not file_exists:
                    csv_writer.writeheader()

        csv_writer.writerow(report_output)
    
    print(f"Email object: {loop_counter} has been written to " + report_owner + ".csv")