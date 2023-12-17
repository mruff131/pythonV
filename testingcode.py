import re
my_emails = ["jordanw@codingtemple.orgcom", "pocohontas1776@gmail.com", "helloworld@aol..com",
             "yourfavoriteband@g6.org", "@codingtemple.com"]

def verifyEmail(list_emails):
    valid_email = re.compile(r"[a-zA-Z0-9_.-]+@[a-zA-Z]+\.(com|org)\b")
    for email in list_emails:
        match = valid_email.search(email)
        if match:
            print(email)
        else:
            print(None)

verifyEmail(my_emails)