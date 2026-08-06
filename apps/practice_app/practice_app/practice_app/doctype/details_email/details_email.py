# Copyright (c) 2026, sanjay and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Details_email(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		email: DF.Data | None
		select_data: DF.Link | None
	# end: auto-generated types

	pass
