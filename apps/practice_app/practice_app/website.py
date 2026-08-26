import frappe

def get_home_page(user):
    if user == "sanjay@email.com":
        return "homepage"
    return "login"

def get_dynamic_pages():
    return [
        frappe._dict({
            "doctype": "Details",
            "route": "profile/<name>",
            "name": "user_profile"  # Points to user_profile.html & user_profile.py
        })
    ]