import frappe


def validate_details(doc, method=None):
    frappe.logger().info(
        f"Validating Details: {doc.name}"
    )

    if doc.email:
        doc.email = doc.email.lower()


def before_insert_details(doc, method=None):
    frappe.logger().info(
        f"Before inserting Details: {doc.name}"
    )


def after_insert_details(doc, method=None):
    frappe.logger().info(
        f"Details created: {doc.name}"
    )


def on_update_details(doc, method=None):
    frappe.logger().info(
        f"Details updated: {doc.name}"
    )


def on_trash_details(doc, method=None):
    frappe.logger().info(
        f"Details deleted: {doc.name}"
    )