# Save colors in constants to decorate the console output
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
END = '\033[0m'


# ************************* class Email *******************************


# Create an object email
class Email:
    has_been_read = False
    is_spam = False

    def __init__(self, from_address, subject_line, email_contents):
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents

    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True


# ************************* class Inbox *******************************
# Create a list of objects email and perform tasks on them:
# list emails filtered by a sender address, read/delete/mark as spam and as read individual email
class Inbox:

    def __init__(self):
        self.my_emails = []

    # **************************************
    # Add a new email to the list
    def add_email(self, from_address, subject_line, email_contents):
        email = Email(from_address, subject_line, email_contents)
        self.my_emails.append(email)
        return f"\nNew email has been added to the list.\n"

    # **************************************
    # Add demo emails to the list
    def demo_email(self):
        count_demo = 0
        try:
            with open("demo_emails.txt", "r+") as text:
                demo = text.read().splitlines()
        except FileNotFoundError:
            return f"\n{count_demo} demo emails has been preloaded.\n"

        for email_demo in demo:
            count_demo += 1
            email_ = email_demo.strip().split(",")
            try:
                email_[1]
            except IndexError:
                break
            email = Email(email_[0], email_[1], email_[2])
            self.my_emails.append(email)
        return f"\n{count_demo} demo emails has been preloaded.\n"

    # **************************************
    # Return a string with all emails from the requested sender address
    def list_messages_from_sender(self, sender_address):
        count = 1
        messages = ""

        for i in range(len(self.my_emails)):
            if sender_address == self.my_emails[i].from_address:
                messages += f"  {GREEN} NO.{END} {count} - {GREEN}Subject:{END} {self.my_emails[i].subject_line}\n"
                count += 1

        if messages == "":
            return f"\n{RED}Email {END}{sender_address} {RED}is not found in the inbox.{END}\n"

        return f"\n{GREEN} Messages from {sender_address}:{END}\n{messages}\n"

    # **************************************
    # Return the content of an email requested by sender address and number
    def get_email(self, sender_address, index):
        count = 1
        for i in range(len(self.my_emails)):
            if sender_address == self.my_emails[i].from_address and count != index:
                count += 1
            elif sender_address == self.my_emails[i].from_address and count == index:
                self.my_emails[i].mark_as_read()
                return f"""    Email: {self.my_emails[i].from_address}
    Subject: {self.my_emails[i].subject_line}
    Content: {self.my_emails[i].email_contents}
    Read: {self.my_emails[i].has_been_read}
    Spam: {self.my_emails[i].is_spam}"""
        return ""

    # **************************************
    # Mark as spam an email requested by sender address and number
    def mark_as_spam(self, sender_address, index):
        count = 0
        for i in range(len(self.my_emails)):
            if sender_address == self.my_emails[i].from_address and count != index:
                count += 1
            elif sender_address == self.my_emails[i].from_address and count == index:
                self.my_emails[i].mark_as_spam()
                return f" Marked as spam: {self.my_emails[i].subject_line}"

    # **************************************
    # Return a string with all unread emails
    def get_unread_emails(self):
        count = 0
        unread_emails = ""
        for i in range(len(self.my_emails)):
            if not self.my_emails[i].has_been_read:
                unread_emails += f" {GREEN}No.{END} {count} - {self.my_emails[i].from_address} " \
                                 f"{GREEN}Subject:{END} {self.my_emails[i].subject_line}\n"
                count += 1
        return f" Unread emails:\n{unread_emails}"

    # **************************************
    # Return a string with all spam emails
    def get_spam_emails(self):
        count = 0
        spam_emails = ""
        for i in range(len(self.my_emails)):
            if self.my_emails[i].is_spam:
                spam_emails += f"{GREEN}No.{END} {count} - {self.my_emails[i].from_address} " \
                               f"{GREEN}Subject:{END} {self.my_emails[i].subject_line}\n"
                count += 1
        return f" Spam emails:\n{spam_emails}"

    # **************************************
    # Delete an email requested by sender address and number
    def delete(self, sender_address, index):
        count = 0
        for i in range(len(self.my_emails)):
            if sender_address == self.my_emails[i].from_address and count != index:
                count += 1
            elif sender_address == self.my_emails[i].from_address and count == index:
                removed_email = f" The email from: {self.my_emails[i].from_address} with subject:" \
                                f" {self.my_emails[i].subject_line} has been removed"
                self.my_emails.remove(self.my_emails[i])
                return removed_email
