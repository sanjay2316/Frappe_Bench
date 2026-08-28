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
        },
        {
            "label": _("Amount"),
            "fieldname": "amount",
            "fieldtype": "Currency"
        }
    ]

    data = frappe.get_all(
        "Details",
        filters={"status": filters.get("status")} if filters.get("status") else {},
        fields=["name", "name1", "status"]
    )

    for i, row in enumerate(data):
        row["amount"] = (i + 1) * 1000

    return columns, data