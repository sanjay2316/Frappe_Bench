frappe.ui.form.on("Employee Portal", {
    async validate(frm) {
        if (frm.doc.log === "In") {
            if (!frm.doc.employee_id) {
                frappe.throw("Please select Employee ID");
            }
            if (!frm.doc.date) {
                frappe.throw("Please select Date");
            }
            if (!frm.doc.log_in_time) {
                frappe.throw("Please enter Log In Time");
            }

            let response = await frappe.call({
                method: "practice_app.api.check_first_in",
                args: {
                    date: frm.doc.date,
                    emp_id: frm.doc.employee_id
                }
            });

            if (response.message === true) {
                frappe.msgprint("Can Log In!");
            } else {
                frappe.throw("You Cannot check more than one time!");
            }
        }
        else if (frm.doc.log === "Out") {
            if (!frm.doc.employee_id) {
                frappe.throw("Please select Employee ID");
            }
            if (!frm.doc.date) {
                frappe.throw("Please select Date");
            }
            if (!frm.doc.log_out_time) {
                frappe.throw("Please enter Log Out Time");
            }

            let response = await frappe.call({
                method: "practice_app.api.check_out",
                args: {
                    date: frm.doc.date,
                    emp_id: frm.doc.employee_id
                }
            });

            if (response.message !== true) {
                frappe.throw("Please Log In before Log Out!");
            }

            let logindetail = await frappe.call({
                method: "practice_app.api.check_out_details",
                args: {
                    date: frm.doc.date,
                    emp_id: frm.doc.employee_id
                }
            });

            let login = logindetail.message;

            if (!login) {
                frappe.throw("Login details not found!");
            }

            let start = moment(
                login.log_in_time,
                "HH:mm:ss"
            );

            let end = moment(
                frm.doc.log_out_time,
                "HH:mm:ss"
            );

            let minutes = end.diff(
                start,
                "minutes"
            );

            if (minutes < 0) {
                frappe.throw(
                    "Log Out Time cannot be before Log In Time!"
                );
            }

            let hours = minutes / 60;
            let status;

            if (hours >= 8) {
                status = "Full day";
            }
            else if (hours > 4) {
                status = "Half day";
            }
            else {
                status = "Leave";
            }

            let attendance_response = await frappe.call({
                method: "practice_app.api.update_attendance",
                args: {
                    date: frm.doc.date,
                    emp_id: frm.doc.employee_id,
                    status: status,
                    hours: hours,
                    intime : login.log_in_time,
                    outtime : frm.doc.log_out_time
                }
            });

            if (attendance_response.message === true) {
                frappe.msgprint(
                    "Attendance added successfully!"
                );
            }
        }
    }
});