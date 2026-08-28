// Copyright (c) 2026, sanjay and contributors
// For license information, please see license.txt

frappe.ui.form.on("Income", {
	refresh(frm) {
        
	},
    before_save(frm){
        if(frm.is_new()){
            frm.doc.remaining_amount = frm.doc.principal_amount
        }
    }
});
