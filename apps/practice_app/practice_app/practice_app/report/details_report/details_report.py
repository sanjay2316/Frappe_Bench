import frappe
from frappe import _


def execute(filters=None):
    columns = [
        {
            "label": _("Name"),
            "fieldname": "name",
            "fieldtype": "Data"
        },
        {
            "label": _("Name 1"),
            "fieldname": "name1",
            "fieldtype": "Data"
        },
        {
            "label": _("Status"),
            "fieldname": "status",
            "fieldtype": "Data"
        }
    ]

    data = frappe.get_all(
        "Details",
        filters={"status": filters.get("status")} if filters.get("status") else {},
        fields=["name", "name1", "status"]
    )

    return columns, data