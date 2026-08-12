import frappe


def get_sender_details():
    return "John Doe", "johndoe@example.com"


def send(self, sender, recipient, msg):
    frappe.log_error(
        title="EMAIL HOOK TEST",
        message=f"""
Sender: {sender}
Recipient: {recipient}
Message: {msg}
"""
    )

    self.update_status("Sending")