import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z][a-zA-Z]*(['-][A-Z][a-zA-Z]*)?( [A-Z][a-zA-Z]*(['-][A-Z][a-zA-Z]*)?)*$"
name_regex = re.compile(name)

phone_number = r"\({0,1}[\d]{3}\){0,1}[- ]{0,1}[\d]{3}-{0,1}[\d]{4}"
phone_regex = re.compile(phone_number)

email_address = r"[A-z]([A-z0-9][\.]{0,1})+[A-z0-9]+@[A-z0-9]+\.[a-z]{2,}"
# r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
email_regex = re.compile(email_address)
