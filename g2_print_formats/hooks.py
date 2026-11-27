app_name = "g2_print_formats"
app_title = "G2 Print Formats"
app_publisher = "Savad Ibrahim"
app_description = "G2 Print Formats"
app_email = "savadibrahim@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "g2_print_formats",
# 		"logo": "/assets/g2_print_formats/logo.png",
# 		"title": "G2 Print Formats",
# 		"route": "/g2_print_formats",
# 		"has_permission": "g2_print_formats.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/g2_print_formats/css/g2_print_formats.css"
app_include_js = [
	"/assets/g2_print_formats/js/finance_book_print_format.js",
	"/assets/g2_print_formats/js/general_ledger_print_format.js?v=3",
]

# include js, css files in header of web template
# web_include_css = "/assets/g2_print_formats/css/g2_print_formats.css"
# web_include_js = "/assets/g2_print_formats/js/g2_print_formats.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "g2_print_formats/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "g2_print_formats/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
jinja = {
	"filters": "g2_print_formats.utils.jinja_filters",
}

# Installation
# ------------

# before_install = "g2_print_formats.install.before_install"
after_install = "g2_print_formats.install.after_install"
after_migrate = "g2_print_formats.install.after_migrate"

G2_PRINT_FORMAT_NAMES = [
	"G2 Purchase Order",
	"G2 Sales Invoice",
	"G2 Quotation",
	"G2 Sales Order",
	"G2 Delivery Note",
	"G2 Purchase Invoice",
	"G2 Purchase Receipt",
	"G2 Payment Voucher",
	"G2 Payment Voucher Bulk",
	"G2 Expense Entry",
	"G2 Payment Request",
	"G2 Proforma Invoice",
	"G2 Quote",
	"G2 Consolidated Proforma Invoice",
	"G2 Journal Entry",
	"G2 Pay Slip",
	"G2 FZ Purchase Order",
	"G2 FZ Sales Invoice",
	"G2 FZ Quotation",
	"G2 FZ Sales Order",
	"G2 FZ Delivery Note",
	"G2 FZ Purchase Invoice",
	"G2 FZ Purchase Receipt",
	"G2 FZ Payment Voucher",
	"G2 FZ Payment Voucher Bulk",
	"G2 FZ Expense Entry",
	"G2 FZ Payment Request",
	"G2 FZ Proforma Invoice",
	"G2 FZ Quote",
	"G2 FZ Consolidated Proforma Invoice",
	"G2 FZ Journal Entry",
	"G2 Quotation Delivery Note",
	"G2 Monthly Profit and Loss",
	"G2 Balance Sheet",
	"G2 Party Ledger",
	"G2 Outstanding Invoices",
	"G2 Outstanding Payables",
	"G2 Customer Outstanding",
]

G2_DEFAULT_PRINT_FORMAT_PROPERTY_SETTERS = [
	"Purchase Order-main-default_print_format",
	"Sales Invoice-main-default_print_format",
	"Quotation-main-default_print_format",
	"Sales Order-main-default_print_format",
	"Delivery Note-main-default_print_format",
	"Purchase Invoice-main-default_print_format",
	"Purchase Receipt-main-default_print_format",
	"Payment Entry-main-default_print_format",
	"Payment Voucher-main-default_print_format",
	"Expense Entry-main-default_print_format",
	"Payment Request-main-default_print_format",
	"Proforma Invoice-main-default_print_format",
	"Quote-main-default_print_format",
	"Consolidated Proforma Invoice-main-default_print_format",
	"Journal Entry-main-default_print_format",
	"Salary Slip-main-default_print_format",
]

G2_PRINT_FORMAT_CUSTOM_DOCPERM_ROLES = [
	"Accounts Manager",
]

fixtures = [
	{
		"doctype": "Print Format",
		"filters": [["name", "in", G2_PRINT_FORMAT_NAMES]],
	},
	{
		"doctype": "Property Setter",
		"filters": [["name", "in", G2_DEFAULT_PRINT_FORMAT_PROPERTY_SETTERS]],
	},
	{
		"doctype": "Custom DocPerm",
		"filters": [
			["parent", "=", "Print Format"],
			["role", "in", G2_PRINT_FORMAT_CUSTOM_DOCPERM_ROLES],
		],
	},
]

# Uninstallation
# ------------

before_uninstall = "g2_print_formats.install.before_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "g2_print_formats.utils.before_app_install"
# after_app_install = "g2_print_formats.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "g2_print_formats.utils.before_app_uninstall"
# after_app_uninstall = "g2_print_formats.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "g2_print_formats.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "g2_print_formats.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"g2_print_formats.tasks.all"
# 	],
# 	"daily": [
# 		"g2_print_formats.tasks.daily"
# 	],
# 	"hourly": [
# 		"g2_print_formats.tasks.hourly"
# 	],
# 	"weekly": [
# 		"g2_print_formats.tasks.weekly"
# 	],
# 	"monthly": [
# 		"g2_print_formats.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "g2_print_formats.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "g2_print_formats.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "g2_print_formats.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "g2_print_formats.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["g2_print_formats.utils.before_request"]
# after_request = ["g2_print_formats.utils.after_request"]

# Job Events
# ----------
# before_job = ["g2_print_formats.utils.before_job"]
# after_job = ["g2_print_formats.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"g2_print_formats.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

