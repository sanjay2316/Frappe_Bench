# Copyright (c) 2026, sanjay and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class EmployeePortal(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		date: DF.Date
		employee_id: DF.Link
		log: DF.Literal["In", "Out"]
		log_in_time: DF.Time | None
		log_out_time: DF.Time | None
	# end: auto-generated types

	pass
