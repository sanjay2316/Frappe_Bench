import frappe

@frappe.whitelist()
def create_task(task_subject):
    doc = frappe.new_doc("Task")
    doc.task_subject = task_subject
    doc.save()

    return doc.name