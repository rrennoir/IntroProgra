def update_contact(contacts: dict, name: str, mail: str) -> None:

    if name in contacts:
        contacts[name] = mail

    else:
        contacts.update({name: mail})


contacts = {
    "Kevin": 'azert1@aaaaa.be',
    "John": "azerty1@aaaa.be"
}
print(f"Before: {contacts}\n")

update_contact(contacts, "Johnny", "changer@bbbb.com")
print(f"After: {contacts}\n")
