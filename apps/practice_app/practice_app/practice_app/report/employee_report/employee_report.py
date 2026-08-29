# Copyright (c) 2026, sanjay and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters = None):

	columns = [
		{
			"label": _("Employee ID"),
			"fieldname": "employee_id",
			"fieldtype": "Data",
		},
		{
			"label": _("Date"),
			"fieldname": "date",
			"fieldtype": "Date",
		},
		{
			"label": _("In Time"),
			"fieldname": "in_time",
			"fieldtype": "Time",
		},
		{
			"label": _("Out Time"),
			"fieldname": "out_time",
			"fieldtype": "Time",
		},
		{
			"label": _("Total Hours"),
			"fieldname": "total_hours",
			"fieldtype": "Int",
		},
		{
			"label":_("Status"),
			"fieldname": "status",
			"fieldtype": "Data", 
		}
	]
	date = filters.get("date")
	data = frappe.db.sql("""
		SELECT e.name as employee_id , ea.date as date , ea.in_time as in_time , ea.out_time as out_time , ea.total_working_hours as total_hours , ea.status as status
		FROM `tabEmployee` e INNER JOIN `tabEmployee Attendance` ea ON e.name = ea.parent WHERE ((%(date)s IS NULL OR ea.date = %(date)s)) ORDER BY ea.date 
	""",{
		"date":date
	},as_dict=True)
	return columns, data
