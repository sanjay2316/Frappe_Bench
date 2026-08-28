import frappe


def get_context(context):
    context.users = frappe.get_all(
        "Details",
        filters={"check": 1},
        fields=["name1", "email"]
    )

    context.title = "Our Team"
    context.no_cache = True