// frappe.ui.form.on("Details", {
//     refresh(frm) {

//         frm.add_custom_button("Create Document", function () {
//             let dialog = new frappe.ui.Dialog({
//                 title : "Enter Name",
//                 fields : [
//                     {
//                         label : "Name",
//                         fieldname : "name2",
//                         fieldtype : "Data"
//                     }
//                 ],
//                 primary_action_label : "Create" ,
//                 primary_action(values){
//                     let newname = values.name2;
//                     frappe.route_options = {
//                         name1: newname
//                     };
//                     console.log(values.name2);
//                     dialog.hide();
//                     frappe.new_doc("Details");
//                 }
//             });
//             dialog.show();
//         });
         
//     }

// });
