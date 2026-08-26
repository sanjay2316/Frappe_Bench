console.log("🔥 DETAILS.JS LOADED");

frappe.templates["custom_timeline_template"] = `
<div>
    <strong>Details Information</strong>
    <p>Name: {{ name }}</p>
    <p>Email: {{ email }}</p>
    <p>Status: {{ status }}</p>
</div>
`;

frappe.ui.form.on("Details", {
    refresh: function(frm) {
        console.log("Details form loaded");

        frm.add_custom_button("My Button", function() {
            frappe.msgprint("Button clicked!");
        });
    },

    email: function(frm) {
        console.log("Email changed:", frm.doc.email);
    },

    status: function(frm) {
        if (frm.doc.status === "Approved") {
            frm.set_value("check", 1);
        }
    }
});