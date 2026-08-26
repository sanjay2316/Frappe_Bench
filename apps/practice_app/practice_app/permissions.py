import frappe


def details_query(user=None):
    if not user:
        user = frappe.session.user

    return "`tabDetails`.email = {user}".format(
        user=frappe.db.escape(user)
    )
def details_has_permission(doc, user=None, permission_type=None):
    if not user:
        user = frappe.session.user

    if permission_type == "read" and doc.status == "Approve":
        return True

    if permission_type == "write" and doc.email == user:
        return True

    return None