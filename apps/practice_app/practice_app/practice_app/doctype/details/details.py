import frappe
from frappe.model.document import Document


class Details(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF
        from practice_app.practice_app.doctype.child_table.child_table import Child_Table

        attachment: DF.Attach | None
        check: DF.Check
        email: DF.Data
        name1: DF.Data
        name: DF.Int | None
        new_data: DF.Data | None
        status: DF.Literal["Pending", "Approve", "Reject"]
        table: DF.Table[Child_Table]
    # end: auto-generated types

    def validate(self):
        if self.has_value_changed("status"):
            print("Status Changed")

    def after_save(self):
        self.add_comment("Comment", "Document Validated")
        self.add_tag("Important")


    def send_notification(self):
        frappe.msgprint("Notification Sent")

    def send_emails(self, emails, message):
        frappe.sendmail(recipients=emails,subject="Welcome",message=message)

    def on_update(self):
    	self.notify_update()


@frappe.whitelist()
def create_document():
    doc = frappe.new_doc("Details")
    doc.name1 = "SanjaySanjaySanjaySanjayyyy"
    doc.email="sanja@email.com"
    doc.insert()
    return doc.name1

@frappe.whitelist()
def update_document(docname):
    doc = frappe.get_doc("Details", docname)
    doc.status = "Approve"
    doc.save()


@frappe.whitelist()
def reload_document(docname):
    doc = frappe.get_doc("Details", docname)
    doc.reload()
    return doc.status

@frappe.whitelist()
def queue_emails(docname):
    email_list = [
        "sanjayk.sde27@gmail.com",
        "monikarthik2122@gmail.com"
    ]
    doc = frappe.get_doc("Details", docname)
    doc.queue_action(
        "send_emails",
        emails=email_list,
        message="Hello everyone! This email was sent using queue_action()."
    )
    return "Emails queued successfully."