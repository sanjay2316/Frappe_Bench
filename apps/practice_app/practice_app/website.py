import frappe

def get_home_page(user):
    print("Hook called for:", user)

    if user == "sanjay@email.com":
        return "homepage"

    return "login"