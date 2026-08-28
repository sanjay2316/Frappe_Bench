# Copyright (c) 2026, sanjay and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Income(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from practice_app.practice_app.doctype.amount_usage.amount_usage import Amount_Usage

		name: DF.Int | None
		principal_amount: DF.Float
		reference: DF.Table[Amount_Usage]
		remaining_amount: DF.Float
	# end: auto-generated types

	pass
