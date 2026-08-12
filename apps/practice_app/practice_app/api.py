import frappe

@frappe.whitelist()
def create_task(task_subject):
    doc = frappe.new_doc("Task")
    doc.task_subject = task_subject
    doc.save()

    return doc.name
@frappe.whitelist()
def custom_logic(doc, method):
    frappe.msgprint("Hook executed!")