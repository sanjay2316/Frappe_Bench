# Copyright (c) 2026, sanjay and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class EmployeeAttendance(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		date: DF.Date | None
		employee_id: DF.Link | None
		in_time: DF.Time | None
		out_time: DF.Time | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		status: DF.Literal["", "Full day", "Half day", "Leave"]
		total_working_hours: DF.Int
	# end: auto-generated types

	pass
