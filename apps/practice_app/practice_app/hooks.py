app_name = "practice_app"
app_title = "Practice_App"
#homepage = "homepage"
app_publisher = "sanjay"
app_description = "Application to practice the frappe"
app_email = "sanjay@email.com"
app_license = "mit"
export_python_type_annotations = True
# add_to_apps_screen = [
#     {
#         "name": "practice_app",
#         "logo": "/assets/practice_app/tennismart.png",
#         "title": "Practice App",
#         "route": "/practice_app"
#     }
# ]
# website_theme_scss = "practice_app/public/scss/website"
# app_include_icons = [
#     "/assets/practice_app/icons/practice_app.svg"
# ]
# importable_doctypes = [
#     "Student",
#     "Details"
# ]
# before_app_install = "practice_app.install.before_install"

# after_app_install = "practice_app.install.after_install"
#app_include_js = ["custom_desk.bundle.js"]
#app_include_css = ["/assets/practice_app/css/practice_app.css"]
# doctype_list_js = {
#     "Details": "public/js/details_list.js"
# }
webform_include_js = {
    "Details": "public/js/webform.js"
}
web_include_css = ["/assets/practice_app/css/practice_app.css"]
webform_include_css = {
    "test_webform": "public/css/weform.css"
}
# get_website_user_home_page = "practice_app.website.get_home_page"
# # portal_menu_items = [
# #    {
# #        "title": "Customer Home",
# #        "route": "/customer",
# #        "role": "Sales Manager"  
# #    },
# #    {
# #        "title": "Profile",
# #        "route": "/profile",
# #        "role": "Sales Manager"
# #    }
# # ]
# brand_html = """
# <div>
#    <img src="/assets/practice_app/images/tennismart.png" height="35">
#    TennisMart
# </div>
# """
# # base_template = "practice_app/templates/my_custom_base.html"
# override_email_send = "practice_app.override.email.send_email"
# base_template_map = {
#     "/": "practice_app/templates/my_custom_base.html",
# }
# get_sender_details = "practice_app.overrides.email.get_sender_details"
# # doc_events = {
# #     "Test_Document": {
# #         "validate": "practice_app.api.custom_logic"
# #     }
# # }
# # scheduler_events = {
# #     "cron": {
# #         "*/5 * * * *": [
# #             "practice_app.tasks.daily_maintenance"
# #         ]
# #     }
# # }
# base_template_map = {
#     "/": "practice_app/templates/my_custom_base.html",
# }
# get_web_pages_with_dynamic_routes = "practice_app.website.get_dynamic_pages"
# practice_app/hooks.py

# website_route_rules = [
#     {"from_route": "/profile/<name1>", "to_route": "user_profile"}
# ]

# get_web_pages_with_dynamic_routes = "practice_app.website.get_dynamic_pages"
# calendars = ["Check_Calendar"]
# on_session_creation = "practice_app.overrides.allocate_free_credits.allocate_free_credits"
# permission_query_conditions = {
#     "Details": "practice_app.permissions.details_query"
# }
# has_permission = {
#     "Details": "practice_app.permissions.details_has_permission"
# }
# extend_doctype_class = {
#     "Details": [
#         "practice_app.extensions.details.DetailsMixin"
#     ]
# }
# override_doctype_class = {
#     "Details": "practice_app.overrides.details.CustomDetails"
# }
doctype_js = {
    "Details": "public/js/details.js"
}
# doc_events = {
#     "Test_Document": {
#         "validate": "practice_app.api.custom_logic"
#     },

#     "Details": {
#         "validate": "practice_app.crud_events.validate_details",
#         "before_insert": "practice_app.crud_events.before_insert_details",
#         "after_insert": "practice_app.crud_events.after_insert_details",
#         "on_update": "practice_app.crud_events.on_update_details",
#         "on_trash": "practice_app.crud_events.on_trash_details"
#     }
# }
override_whitelisted_methods = {
    "frappe.client.get_count": "practice_app.whitelisted.custom_get_count"
}
additional_timeline_content = {
    "Details": [
        "practice_app.timeline.details_timeline"
    ]
}
fixtures = ["Client Script"]