import win32com.client
#stabilishes connection
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")


#retrieves informtion - in this case I created a email called test and sent to myself - it sits in my inbox
for folder in outlook.Folders:
    for subfolder in folder.Folders:
        print(f"Subfolder Name: {subfolder.Name}")
        if subfolder.Name == "Inbox":
            for item in subfolder.Items:
                if item.Subject == "test":
                    print(f"Item Subject: {item.Subject}")
                    print(f"Item Body: {item.Body}")
                    break
                
               