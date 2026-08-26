import frappe

def get_context(context):
    # Retrieve 'name' from URL parameter (/profile/<name>)
    doc_id = frappe.form_dict.get("name") or frappe.form_dict.get("name1")

    if doc_id and not context.get("doc"):
        # Query by name OR name1 field depending on your Doctype primary key setting
        doc = frappe.db.get_value(
            "Details",
            {"name1": doc_id},
            ["name1", "email", "check", "new_data", "status", "attachment"],
            as_dict=True
        ) or frappe.db.get_value(
            "Details",
            doc_id,
            ["name1", "email", "check", "new_data", "status", "attachment"],
            as_dict=True
        )
        context.doc = doc or {}

    return context