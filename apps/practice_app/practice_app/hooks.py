app_name = "practice_app"
app_title = "Practice_App"
homepage = "homepage"
app_publisher = "sanjay"
app_description = "Application to practice the frappe"
app_email = "sanjay@email.com"
app_license = "mit"
export_python_type_annotations = True
app_include_js = ["custom_desk.bundle.js"]
app_include_css = ["/assets/practice_app/css/practice_app.css"]
doctype_list_js = {
    "Details": "public/js/details_list.js"
}
webform_include_js = {
    "Details": "public/js/webform.js"
}
web_include_css = ["/assets/practice_app/css/practice_app.css"]
webform_include_css = {
    "test_webform": "public/css/weform.css"
}
get_website_user_home_page = "practice_app.website.get_home_page"
portal_menu_items = [
   {
       "title": "Customer Home",
       "route": "/customer",
       "role": "Sales Manager"  
   },
   {
       "title": "Profile",
       "route": "/profile",
       "role": "Sales Manager"
   }
]
brand_html = """
<div>
   <img src="/assets/practice_app/images/tennismart.png" height="35">
   TennisMart
</div>
"""
base_template = "practice_app/templates/my_custom_base.html"
override_email_send = "practice_app.override.email.send_email"
get_sender_details = "practice_app.overrides.email.get_sender_details"
doc_events = {
    "Test_Document": {
        "validate": "practice_app.api.custom_logic"
    }
}