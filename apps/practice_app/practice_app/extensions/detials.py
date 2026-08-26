from frappe.model.document import Document


class DetailsMixin(Document):

    @property
    def full_details(self):
        return f"{self.name1} - {self.email}"

    def custom_method(self):
        return "This is custom functionality"

    def validate(self):
        super().validate()

        if self.status == "Approved":
            self.check = 1