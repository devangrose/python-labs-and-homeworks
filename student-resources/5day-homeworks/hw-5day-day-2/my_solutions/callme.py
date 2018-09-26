contacts = {
  "Carly": "333-3333",
  "Blondie": "444-4444",
  "Jenny": "867-5309"
}

def get_contact(contacts, name):
    if name in contacts:
        print('{}\'s phone number is {}'.format(name, contacts[name]))

get_contact(contacts, "Jenny")
