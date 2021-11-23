import re


def get_phone_numbers(file_path, write_path):
    regex = r"\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})"

    final_result = ""
    results = []
    with open(file_path) as f:
        for i in f.readlines():
            match = re.search(regex, i)
            # print(match.group())
            if match:
                phone_number = match.group()
                phone_number = phone_number.replace(".", "-")
                if len(phone_number) == 10:
                    split_string = list(phone_number)
                    split_string.insert(3, "-")
                    split_string.insert(7, "-")
                    phone_number = "".join(split_string)
                results.append(phone_number)
    for i in results:
        final_result += f"{i}\n"
    with open(write_path, "w") as f:
        f.write(final_result)


def get_emails(file_path, write_path):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    final_result = ""
    results = []
    with open(file_path) as f:
        for i in f.readlines():
            match = re.search(regex, i)
            results.append(match.group())
    for i in results:
        final_result += f"{i}\n"
    with open(write_path, "w") as f:
        f.write(final_result)


if __name__ == "__main__":
    get_phone_numbers("assets/potential-contacts.txt",
                      "info_files/phone_numbers.txt")
    get_emails("assets/potential-contacts.txt", "info_files/emails.txt")
