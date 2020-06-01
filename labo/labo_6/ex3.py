def print_all(contacts: dict) -> None:

    for contact in contacts:
        print(f"Nom: {contact} - Email: {contacts[contact]}")


contacts = {
    "Kevin": 'azert1@aaaaa.be',
    "John": "azerty1@aaaa.be"
}
print_all(contacts)
