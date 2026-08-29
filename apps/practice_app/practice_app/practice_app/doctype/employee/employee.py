# Copyright (c) 2026, sanjay and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Employee(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from practice_app.practice_app.doctype.employee_attendance.employee_attendance import EmployeeAttendance

		attendance: DF.Table[EmployeeAttendance]
		date_of_birth: DF.Date | None
		employee_id: DF.Data
		employee_name: DF.Data
		name: DF.Int | None
	# end: auto-generated types

	pass
