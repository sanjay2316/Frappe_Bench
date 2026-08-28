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
            "status": "Approve"
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

#qb.get_query practice
#http://site1.local/api/method/practice_app.api.getusinggetquery?name=Details
@frappe.whitelist()
def getusinggetquery(name):
    newquery = frappe.qb.get_query(name, fields=["name1 as emp_name","status as current_status",{"table": ["project_id","project_date"]}] , filters={"name":"1"})
    result = newquery.run(as_dict=True)
    return result

#http://site1.local/api/method/practice_app.api.getusinggetquerywithfilter?name=Details&filters={"status":"Approved"}
#http://site1.local/api/method/practice_app.api.getusinggetquerywithfilter?name=Details&filters=%7B%22status%22%3A%22Approved%22%7D
# @frappe.whitelist()
# def getusinggetquerywithfilter(name,filters=None):
#     newquery = frappe.qb.get_query(name,filters=filters)
#     result = newquery.run(as_dict=True)
#     return result

#http://site1.local/api/method/practice_app.api.getlinkfield
@frappe.whitelist()
def getlinkfield():
    newquery = frappe.qb.get_query("Details_email",fields=["select_data.name1 as name","email"])
    result = newquery.run(as_dict=True)
    return result
#http://site1.local/api/method/practice_app.api.countdetails
@frappe.whitelist()
def countdetails():
    q = frappe.qb.get_query(
        "Details",
        fields=[{"COUNT": "*", "as": "total_emp"}]
    )
    res = q.run(as_dict=True)
    return res
#http://site1.local/api/method/practice_app.api.currenttime

@frappe.whitelist()
def currenttime():
    query = frappe.qb.get_query(
    "Details",
    fields=[{"NOW": None, "as": "current_time"}])
    return(query.run(as_dict=True))

#http://site1.local/api/method/practice_app.api.listfilter
@frappe.whitelist()
def listfilter():
    q = frappe.qb.get_query(
        "Details",
        fields=["*"],
        filters=[["name","=","1"]]
    )
    return(q.run(as_dict=True))
#http://site1.local/api/method/practice_app.api.nestedfilter
@frappe.whitelist()
def nestedfilter():
    filters_nested = [
        ["status", "=", "Approve"],
        "and",
        [
            ["name1", "=", "Sanjay"],
            "or",
            ["name1", "=", "Monika"],
        ]
    ]

    query = frappe.qb.get_query(
        "Details",
        filters=filters_nested
    )

    return(query.run(as_dict=True))

@frappe.whitelist()
def childtable():
    q = frappe.qb.get_query(
        "Details",
        fields=[
            "name",
            "name1",
            "status",
            {"table": ["project_id", "project_date"]}
        ],
        filters={"name": "1"},
        ignore_permissions=False 
    )
    
    try:
        sql_string = q.get_sql()
        print(sql_string)
        res = q.run(as_dict=True)
        return(res)

    except frappe.PermissionError:
        print("User does not have permission to read DocType!")

#doubt session

# In [13]: q = frappe.qb.get_query(
#     ...:     "Details",
#     ...:     fields=[
#     ...:         "name",
#     ...:         "name1",
#     ...:         "status",
#     ...:         {"table": ["project_id", "project_date"]}
#     ...:     ],
#     ...:     filters={"name": "1"}
#     ...: )
#     ...:
#     ...: q.run(as_dict=True)
# Out[13]:
# [{'name': 1,
#   'name1': 'Sanjay',
#   'status': 'Approve',
#   'table': [{'project_id': 'PJ1',
#     'project_date': datetime.date(2026, 8, 26)}]}]

# In [14]: q = frappe.qb.get_query(
#     ...:     "Details",
#     ...:     fields=[
#     ...:         "name1 as emp_name",
#     ...:         "status as current_status",
#     ...:         {"table": ["project_id", "project_date"]}
#     ...:     ],
#     ...:     filters={"name": "1"}
#     ...: )
#     ...:
#     ...: q.run(as_dict=True)
# Out[14]: [{'emp_name': 'Sanjay', 'current_status': 'Approve'}]


# explanation
# when use "as" alias you will not get the child table filter



@frappe.whitelist()
def check_income_amount(income, using_amount):
    docu = frappe.get_doc("Income", income)

    if docu.remaining_amount < float(using_amount):
        frappe.throw(
            "INVALID AMOUNT REMAINING AMT : "
            + str(docu.remaining_amount)
        )


@frappe.whitelist()
def update_income(income, invoice, using_amount, using_reason):
    docu = frappe.get_doc("Income", income)

    docu.remaining_amount = (
        docu.remaining_amount - float(using_amount)
    )

    docu.append("reference", {
        "invoice": invoice,
        "used_amount": using_amount,
        "used_reason": using_reason
    })

    docu.save()