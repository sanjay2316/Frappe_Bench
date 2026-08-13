import frappe

@frappe.whitelist()
def create_task(task_subject):
    doc = frappe.new_doc("Task")
    doc.task_subject = task_subject
    doc.save()

    return doc.name
@frappe.whitelist()
def custom_logic(doc, method):
    frappe.msgprint("Hook executed!")

#get the full list

@frappe.whitelist()
def get_details():
    return frappe.db.get_list(
        "Details",
        filters={
            "status": "Approve"
        },
        fields=["name", "name1", "email", "status"]
    )

#same as get_list but without permission

@frappe.whitelist()
def get_all_details():
    return frappe.db.get_all(
        "Details",
        filters={
            "status": "Approved"
        },
        fields=["name", "name1", "email", "status"]
    )

#get one value of one record
#http://site1.local/api/method/practice_app.api.get_detail_email?docname=igvdlia5lq
@frappe.whitelist()
def get_detail_email(docname):
    return frappe.db.get_value(
        "Details",
        docname,
        "email"
    )
#get multiple value of one record
#http://site1.local/api/method/practice_app.api.get_detail_info?docname=igvdlia5lq


# @frappe.whitelist()
# def get_detail_info(docname):
#     return frappe.db.get_value(
#         "Details",
#         docname,
#         ["name1", "email", "status"]
#     )


# output : {
#   "message": [
#     "sanjaysanjaysanjay",
#     "yajnas@gmail.com",
#     "Pending"
#   ]
# }


#as_dict=1
#http://site1.local/api/method/practice_app.api.get_detail_info?docname=igvdlia5lq

@frappe.whitelist()
def get_detail_info(docname):
    return frappe.db.get_value(
        "Details",
        docname,
        ["name1", "email", "status"],
        as_dict=1
    )


# output : {
#   "message": {
#     "name1": "sanjaysanjaysanjay",
#     "email": "yajnas@gmail.com",
#     "status": "Pending"
#   }
# }

#fetch based on filter
#http://site1.local/api/method/practice_app.api.get_approved_name

@frappe.whitelist()
def get_approved_name():
    return frappe.db.get_value(
        "Details",
        {"status": "Approve"},
        "name1"
    )

#update
#http://site1.local/api/method/practice_app.api.update_status?docname=igvdlia5lq&status=Approve
@frappe.whitelist()
def update_status(docname, status):
    return frappe.db.set_value(
        "Details",
        docname,
        "status",
        status
    )

#db.exists
#http://site1.local/api/method/practice_app.api.check_detail_exists?docname=igvdlia5lq

@frappe.whitelist()
def check_detail_exists(docname):
    return frappe.db.exists(
        "Details",
        docname
    )

#count
#http://site1.local/api/method/practice_app.api.count_details
@frappe.whitelist()
def count_details():
    return frappe.db.count("Details")


#assignment databaseapi

#http://site1.local/api/method/practice_app.api.process_details

@frappe.whitelist()
def process_details():

    # Query Builder DocTypes
    details = frappe.qb.DocType("Details")
    details_email = frappe.qb.DocType("Details_email")

    # Query
    query = (
        frappe.qb
        .from_(details)
        .join(details_email)
        .on(details.email == details_email.email)
        .select(
            details.name,
            details.name1,
            details.email,
            details.status,
            details_email.emp_id
        )
        .where(details.status == "Pending")
        .limit(10)
    )

    # Execute query
    results = query.run(as_dict=True)

    if not results:
        return {
            "message": "No pending records found",
            "results": []
        }

    # Document API
    # Fetch the first record
    first_record = results[0]

    doc = frappe.get_doc("Details", first_record["name"])

    # Update first record
    doc.status = "Approve"
    doc.save()

    # Update the returned Python result
    first_record["status"] = "Approve"

    # Database API
    # Update all records returned by the query
    for row in results:

        frappe.db.set_value(
            "Details",
            row["name"],
            "status",
            "Approve"
        )

        # Update the result dictionary too
        row["status"] = "Approve"

    return results

#assignment Frappe Utilities
#http://site1.local/api/method/practice_app.api.get_recent_records

@frappe.whitelist()
def get_recent_records():
    details = frappe.get_list(
        "Details",
        fields=["name","name1","email","status","owner"],
        order_by="creation desc",
        limit_page_length=5
    )
    res = []
    for d in details:
        owner_email = frappe.db.get_value(
            "User",
            d.owner,
            "email"
        )
        res.append({
            "name": d.name,
            "name1": d.name1,
            "email": d.email,
            "status": d.status,
            "owner_email": owner_email
        })
    return {
        "Time" : frappe.utils.now(),
        "Recent Result" : res
    }