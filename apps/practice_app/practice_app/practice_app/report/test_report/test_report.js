// Copyright (c) 2026, sanjay and contributors
// For license information, please see license.txt

frappe.query_reports["Test Report"] = {
	filters: [
		{
			"fieldname": "status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": "\nApprove\nReject\nPending"
		},
	],
};
