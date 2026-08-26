# Copyright (c) 2026, sanjay and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Check_Calendar(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		end_date: DF.Date
		start_date: DF.Date
	# end: auto-generated types

	pass
