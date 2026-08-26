from frappe.model.document import Document


class CustomDetails(Document):

    def validate(self):
        super().validate()

        if self.email:
            self.email = self.email.lower()

    def custom_method(self):
        return "Custom Details method"