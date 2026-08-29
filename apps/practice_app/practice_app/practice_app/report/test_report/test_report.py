import frappe

def execute(filters=None):

    columns = [
        {
            "label": "Name",
            "fieldname": "name1",
            "fieldtype": "Data"
        },
        {
            "label": "Email",
            "fieldname": "email",
            "fieldtype": "Data"
        },
        {
            "label": "Status",
            "fieldname": "status",
            "fieldtype": "Data"
        },
        {
            "label": "Project ID",
            "fieldname": "project_id",
            "fieldtype": "Data"
        },
        {
            "label": "Project Date",
            "fieldname": "project_date",
            "fieldtype": "Date"
        }
    ]

    status = filters.get("status")

    data = frappe.db.sql("""
        SELECT
            d.name1,
            d.email,
            d.status,
            c.project_id,
            c.project_date
        FROM `tabDetails` d
        LEFT JOIN `tabChild_Table` c
            ON c.parent = d.name
        WHERE d.status = %(status)s
    """, {"status": status}, as_dict=True)

    return columns, data