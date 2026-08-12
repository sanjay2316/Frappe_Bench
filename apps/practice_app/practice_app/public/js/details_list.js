frappe.listview_settings["Details"] = {

    onload(listview) {

        frappe.msgprint("Details List Loaded");
        listview.filter_area.add([
            ["Details", "status", "=","Pending"]
        ]);
    },

    formatters: {
        email(value) {
            return `<span style="color:blue">${value}</span>`;
        }
    },

    get_indicator(doc) {
        if (doc.status === "Approve") {
            return [
                "Approved",
                "green",
                "status,=,Approve"
            ];
        }
        return [
            "Pending",
            "orange",
            "status,=,Pending"
        ];
    },
    hide_name_column:true,
    hide_name_filter:true
    

};