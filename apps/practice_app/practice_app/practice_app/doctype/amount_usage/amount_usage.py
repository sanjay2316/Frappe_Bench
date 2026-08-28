# Copyright (c) 2026, sanjay and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Amount_Usage(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		invoice: DF.Data
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		used_amount: DF.Float
		used_reason: DF.Data
	# end: auto-generated types

	pass
