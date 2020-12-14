import re


def extract_phone(word):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    match = phone_regex.search(word)
    if match:
        return match.group()
    return None


# print(extract_phone("my number is 123 456-7890"))
# print(extract_phone("my number is 123 456-78901324"))
# print(extract_phone("123 456-7890"))
# print(extract_phone("123 456-7890 fjesoifse"))


def extract_all_phone(word):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    return phone_regex.findall(word)


# print(extract_all_phone("number is 123 456-7890 feeoaisf 123 456-7890"))
# print(extract_all_phone("fesoifjeiso"))


def is_valid_phone(word):
    phone_regex = re.compile(r"^\d{3} \d{3}-\d{4}$")
    # can use original regex and use fullmatch()
    match = phone_regex.search(word)
    if match:
        return True
    return False

print(is_valid_phone("123 456-7890"))
print(is_valid_phone("123 456-7890 fesf"))
print(is_valid_phone("fes123 456-7890fes"))