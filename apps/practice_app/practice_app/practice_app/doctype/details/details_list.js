frappe.listview_settings['Details'] = {
    add_fields: ['name', 'email'],
    filters: [
        []
    ],
    hide_name_column: true, 
    hide_name_filter: true,
    onload(listview) {
       
    },
    before_render() {
       
    },

    has_indicator_for_draft: false,

    get_indicator(doc) {
        if (doc.status == "Approve") {
            return [__("Appending"), "green", "status,=,Approve"];
        } else if (doc.status == "Pending"){
            return [__("Pending"), "darkgrey", "status,=,Pending"];
        }
    },
    primary_action() {

    },
    get_form_link(doc) {
        
    },
    
    button: {
        show(doc) {
            return doc.reference_name;
        },
        get_label() {
            return 'View';
        },
        get_description(doc) {
            return __('View {0}', [`${doc.reference_type} ${doc.reference_name}`])
        },
        action(doc) {
            frappe.set_route('Form', doc.reference_type, doc.reference_name);
        }
    },
    formatters: {
        title(val) {
            return val.bold();
        },
        public(val) {
            return val ? 'Yes' : 'No';
        }
    }
}
