# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "rotary_online"
app_title = "Rotary Online"
app_publisher = "Neil Lasrado, Rotaract Charitable Trust"
app_description = "ERP for Rotary District Organizations"
app_icon = "octicon octicon-heart"
app_color = "blue"
app_email = "neil@rotaract3142.org"
app_license = "MIT"

app_logo_url = "/assets/rotary_online/images/rotary-logo.png"
brand_html = "Rotary Online"

website_context = {
	"favicon": "/assets/rotary_online/images/rotary-logo.png",
	"splash_image": "/assets/rotary_online/images/rotary-logo.png",
}

welcome_email = "rotary_online.utils.welcome_email"

override_whitelisted_methods = {
 	"frappe.desk.moduleview.get_desktop_settings": "rotary_online.desk.set_desktop_icons"
}

app_include_css = [
	"/assets/rotary_online/css/desk.css"
]

app_include_js = [
	"/assets/js/rotary_desk.js"
]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rotary_online/css/rotary_online.css"
# app_include_js = "/assets/rotary_online/js/rotary_online.js"

# include js, css files in header of web template
# web_include_css = "/assets/rotary_online/css/rotary_online.css"
# web_include_js = "/assets/rotary_online/js/rotary_online.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "rotary_online.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "rotary_online.install.before_install"
# after_install = "rotary_online.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rotary_online.notifications.get_notification_config"

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
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rotary_online.tasks.all"
# 	],
# 	"daily": [
# 		"rotary_online.tasks.daily"
# 	],
# 	"hourly": [
# 		"rotary_online.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rotary_online.tasks.weekly"
# 	]
# 	"monthly": [
# 		"rotary_online.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "rotary_online.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rotary_online.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "rotary_online.task.get_dashboard_data"
# }

