# *****************************************************************************
#  I used the name my_email.py instead email.py to avoid
#  the debugger error created by name conflict with Python email module
#  I place my classes in a different file named my_utilities.py for readability
# *****************************************************************************

# Import  files

from my_utilities import Inbox, GREEN, BLUE, RED, END


# Instantiate Inbox class as inbox
inbox = Inbox()
print(inbox.demo_email())

# Create main menu
while True:
    print(f"""{BLUE}============== Main menu ==========================={END}""")

    menu = input(f'''Select one of the following Options below:
                {GREEN}a{END}    - Add a new email
                {GREEN}l{END}    - List all emails
                {GREEN}lf{END}   - List emails from one sender
                {GREEN}lu{END}   - List all unread emails
                {GREEN}ls{END}   - List all spam emails
                {GREEN}e{END}    - Exit
    {GREEN}Enter your choice{END}: ''').lower()

    # ==================add an email ===========
    # Request input to add a new email and call the class to add it
    if menu == 'a':
        print(f"""
{BLUE}================ Ad a new email to database =========================={END}""")
        from_address = ""
        subject_line = ""
        email_contents = ""
        while True:
            if from_address == "":
                from_address = input(" Please enter senders address : ").strip().lower()
                continue
            elif subject_line == "":
                subject_line = input(" Please enter subject : ").strip()
                continue
            elif email_contents == "":
                email_contents = input(" Please enter email contents : ").strip()
            else:
                print(
                    f"{GREEN}{inbox.add_email(from_address, subject_line, email_contents)}{END}")
                break

    # ================== list all emails ===========
    # Call the class to list all emails
    elif menu == 'l':
        print(f"""
{BLUE}================ List of all emails ==========================={END}""")
        emails_list = ""
        for i in range(len(inbox.my_emails)):
            emails_list += f" {GREEN}No. {i + 1}{END} - {inbox.my_emails[i].from_address} {GREEN}- " \
                           f"Subject:{END} {inbox.my_emails[i].subject_line} \n"
        print(f"\n{GREEN} The list of all emails:{END} \n{emails_list}")

    # ================== list emails from chosen sender ===========
    # Request input to add a new email and call the class list emails from chosen sender
    elif menu == 'lf':
        print(f"""
{BLUE}============== List emails from chosen sender ==================={END}
        """)
        sender_address = ""
        while True:
            if sender_address == "":
                sender_address = input(" Please enter sender address : ")
                continue
            break

        print(inbox.list_messages_from_sender(sender_address))

        # ================== Get the requested email content ===========
        # Read all data from the chosen email
        while True:
            if inbox.list_messages_from_sender(sender_address) == f"\n{RED}Email {END}{sender_address} " \
                                                                  f"{RED}is not found in the inbox.{END}\n":
                break
            email_n = input(
                f'{GREEN} \nTo read an email type the {END}email number{GREEN}.'
                f' To return to the main menu type{END} m: ').strip().lower()
            if email_n == "m":
                break
            try:
                n = int(email_n)
            except ValueError:
                print(f"{RED} Please enter a number or m.{END}\n")
                continue
            result = inbox.get_email(sender_address, n)
            if result == "":
                print(f"\n{RED} Please enter a number from 0 to max email number.{END}")
            else:
                print(f"\n{result}")
                # Request input to add a new email
                # and call the class to mark the current email as spam
                # or the class to delete it
                # or to read another one
                spam = input(
                    f'''{GREEN} \n 
    To {BLUE}mark as spam{END} this email type {END}s{GREEN}
    To {BLUE}delete{END} this email type {END}d{GREEN}
    To read another email type the {END}email number{GREEN}.
    To return to the main menu type {END}m: ''').strip().lower()
                if spam == "s":
                    print(inbox.mark_as_spam(sender_address, n - 1))
                elif spam == "m":
                    break
                elif spam == "d":
                    print(inbox.delete(sender_address, n - 1))
                    break

    # ================== List of all unread emails ===========
    # Call the class to list of all unread emails
    elif menu == 'lu':
        print(f"""
    {BLUE}================ List of all unread emails ==========================={END}
""")
        print(inbox.get_unread_emails())

    # ================== List of all spam  emails ===========
    # Call the class to list of all emails marked as spam
    elif menu == 'ls':
        print(f"""
            {BLUE}================ List of all spam emails ==========================={END}
        """)
        print(inbox.get_spam_emails())

        # ==================exit program===========
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    # ================== Wrong choice ===========
    else:
        print(f"{RED}\nYou have made a wrong choice, Please Try again{END}")
