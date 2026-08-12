frappe.pages["practice"].on_page_load = function (wrapper) {

    // Create the page
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: "Practice",
        single_column: true
    });

    // --------------------------------------------------
    // PAGE TITLE
    // --------------------------------------------------

    page.set_title("Employee Dashboard");

    page.set_title_sub("Total Employees: 25");

    page.set_indicator("Active", "blue");


    // --------------------------------------------------
    // PRIMARY ACTION
    // --------------------------------------------------

    page.set_primary_action("New Employee", () => {
        frappe.msgprint("Clicked New Employee");
    });


    // --------------------------------------------------
    // SECONDARY ACTION
    // --------------------------------------------------

    page.set_secondary_action("Refresh", () => {
        frappe.msgprint("Refreshing");
    });


    // --------------------------------------------------
    // CLEAR PRIMARY / SECONDARY ACTION
    // --------------------------------------------------

    // Uncomment if you want to remove them

    // page.clear_primary_action();
    // page.clear_secondary_action();


    // --------------------------------------------------
    // MENU ITEM
    // --------------------------------------------------

    page.add_menu_item("Export", () => {
        frappe.msgprint("Export clicked");
    });


    // --------------------------------------------------
    // ACTION ITEMS
    // --------------------------------------------------

    page.add_action_item("Delete", () => {
        frappe.msgprint("Deleted");
    });

    page.add_action_item("Delete All", () => {
        frappe.msgprint("Deleted All");
    });


    // --------------------------------------------------
    // CLEAR MENU
    // --------------------------------------------------

    // page.clear_menu();


    // --------------------------------------------------
    // INNER BUTTON
    // --------------------------------------------------

    page.add_inner_button("Update", () => {
        frappe.msgprint("Updated");
    });


    // --------------------------------------------------
    // REMOVE INNER BUTTON
    // --------------------------------------------------

    // page.remove_inner_button("Update");


    // --------------------------------------------------
    // GROUPED INNER BUTTONS
    // --------------------------------------------------

    page.add_inner_button("PDF", () => {
        frappe.msgprint("PDF Export");
    }, "Export");

    page.add_inner_button("Excel", () => {
        frappe.msgprint("Excel Export");
    }, "Export");


    // --------------------------------------------------
    // CHANGE INNER BUTTON TYPE
    // --------------------------------------------------

    page.change_inner_button_type(
        "Update",
        null,
        "danger"
    );


    // --------------------------------------------------
    // ADD FIELD
    // --------------------------------------------------

    let field = page.add_field({
        label: "Department",
        fieldtype: "Select",
        fieldname: "department",
        options: [
            "IT",
            "HR",
            "Sales"
        ],

        change: function () {
            let values = page.get_form_values();

            console.log(values);
        }
    });


    // --------------------------------------------------
    // GET FIELD VALUES
    // --------------------------------------------------

    let values = page.get_form_values();

    console.log(values);


    // --------------------------------------------------
    // CLEAR FIELDS
    // --------------------------------------------------

    // Uncomment to clear all fields

    // page.clear_fields();


    // --------------------------------------------------
    // CLEAR INNER TOOLBAR
    // --------------------------------------------------

    // page.clear_inner_toolbar();

};