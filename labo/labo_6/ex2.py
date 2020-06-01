def print_mail(contacts: dict, name: str) -> None:

    if name in contacts:
        print(contacts[name])

    else:
        print(f"Name: '{name}' not in the dictionnary.")


contacts = {
    "Kevin": 'azert1@aaaaa.be',
    "John": "azerty1@aaaa.be"
}
print(f"Dict: {contacts}\n")
print_mail(contacts, "John")
print_mail(contacts, "Johnny")
