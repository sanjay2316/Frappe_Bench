frappe.ui.form.on("Details", {
    refresh(frm) {

        frm.add_custom_button("Create Document", function () {
            frappe.call({
                method: "practice_app.practice_app.doctype.details.details.create_document",
                callback: function(r) {
                    frappe.msgprint("Document Created");
                    frappe.msgprint(r.message);
                }
            });
        });

        frm.add_custom_button("Update Document", function () {
            frappe.call({
                method: "practice_app.practice_app.doctype.details.details.update_document",
                args: {
                    docname: frm.doc.name
                },
                callback: function(r) {
                    frappe.msgprint("Document Updated");
                    frm.reload_doc();
                }
            });
        });

        frm.add_custom_button("Reload Document", function () {
            frappe.call({
                method: "practice_app.practice_app.doctype.details.details.reload_document",
                args: {
                    docname: frm.doc.name
                },
                callback: function(r) {
                    frappe.msgprint("Current Status: " + r.message);
                    frm.reload_doc();
                }
            });
        });

        frm.add_custom_button("Send Emails", function () {

            frappe.call({
                method: "practice_app.practice_app.doctype.details.details.queue_emails",
                args: {
                    docname: frm.doc.name
                },
                callback: function(r) {
                    frappe.msgprint(r.message);
                }
            });

        });

    }
});
