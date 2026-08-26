import frappe


def details_timeline(doctype, docname):

    doc = frappe.get_doc(doctype, docname)

    return [
        {
            "creation": doc.modified,
            "content": f"""
                <div>
                    <strong>Details Information</strong>
                    <p>Name: {doc.name1}</p>
                    <p>Email: {doc.email}</p>
                    <p>Status: {doc.status}</p>
                </div>
            """
        }
    ]