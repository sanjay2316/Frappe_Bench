frappe.ui.form.on("Invoice", {
    refresh(frm) {
        
    },

    validate(frm) {
        if (!frm.doc.select_income || !frm.doc.using_amount) {
            return;
        }

        frappe.call({
            method: "practice_app.api.check_income_amount",
            args: {
                income: frm.doc.select_income,
                using_amount: frm.doc.using_amount
            },
            async: false
        });
    },

    after_save(frm) {
        frappe.call({
            method: "practice_app.api.update_income",
            args: {
                income: frm.doc.select_income,
                invoice: frm.doc.name,
                using_amount: frm.doc.using_amount,
                using_reason: frm.doc.using_reason
            }
        });
    }
});