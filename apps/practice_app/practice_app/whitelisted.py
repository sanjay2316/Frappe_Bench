import frappe


def custom_get_count(
    doctype,
    filters=None,
    debug=False,
    cache=False
):
    frappe.logger().info(
        f"Custom get_count called for {doctype}"
    )

    return frappe.db.count(
        doctype,
        filters=filters
    )