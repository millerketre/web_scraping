import win32com.client
import csv

def retrieve_email():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    email_data = []
    for folder in outlook.Folders:
       for subfolder in folder.Folders:
        print(f"Subfolder Name: {subfolder.Name}")
        if subfolder.Name == "Inbox":
            for item in subfolder.Items:
                if item.Subject == "test":
                    # Extract relevant information from the email body
                    body_lines = item.Body.split("\n")
                    for line in body_lines:
                        if "Company:" in line:
                          info_value = line.split(":")[1].strip()
                        elif "Market Cap:" in line:
                           market_cap = line.split(":")[1].strip()
                        elif "Assets" in line:
                            assets_value = line.split(":")[1].strip()
                        elif "Limits" in line:
                            limits_value = line.split(":")[1].strip()
                           
                    # Append the data to the list
                    email_data.append({"Company": info_value, "Market Cap": market_cap, "Assets": assets_value, "Limits": limits_value})
                    print(email_data)
                    
                    # Save the data to a file
                    with open("email_data.csv", "w", newline="") as f:
                        writer = csv.DictWriter(f, fieldnames=["Company", "Market Cap", "Assets", "Limits"])
                        writer.writeheader()
                        writer.writerows(email_data)
                     
            else:
                break

                
retrieve_email()      