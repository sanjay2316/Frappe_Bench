import frappe
def allocate_free_credits(login_manager):
    user = login_manager.user
    frappe.msgprint(f"--- SESSION HOOK TRIGGERED FOR: {user} ---")
