import frappe
from frappe import _

@frappe.whitelist()
def set_desktop_icons():
	directory_file_link = frappe.db.get_single_value("Resource Settings", 'e_directory')
	desktop = {
		"Club Administration": [
			{
				"label": _('Club'),
				"icon": "octicon octicon-home",
				"type": 'doctype',
				"name": 'Club',
				"link": '#List/Club/List'
			},
			{
				"label": _('Member'),
				"icon": "octicon octicon-organization",
				"type": 'doctype',
				"name": 'Member',
				"link": '#List/Member/List'
			}
		],
		"Reporting": [
			{
				"label": _('Project'),
				"icon": "octicon octicon-checklist",
				"type": 'doctype',
				"name": 'Project',
				"link": '#List/Project/List'
			},
			{
				"label": _('Meeting'),
				"icon": "octicon octicon-briefcase",
				"type": 'doctype',
				"name": 'Meeting',
				"link": '#List/Meeting/List'
			},
			{
				"label": _('District Event'),
				"icon": "octicon octicon-globe",
				"type": 'doctype',
				"name": 'District Event',
				"link": '#List/District Event/List'
			},
			{
				"label": _('OCV'),
				"icon": "octicon octicon-checklist",
				"type": 'doctype',
				"name": 'OCV',
				"link": '#List/OCV/List'
			}
		],
		"Tools": [
			{
				"label": _('District E-Directory'),
				"icon": "octicon octicon-file-submodule",
				"type": 'page',
				"name": 'Directory',
				"link": directory_file_link
			},
			{
				"label": _('GML'),
				"icon": "octicon octicon-repo",
				"type": 'doctype',
				"name": 'GML',
				"link": '#List/GML/Image'
			},
			{
				"label": _('Insight Engine'),
				"icon": "octicon octicon-light-bulb",
				"type": 'page',
				"name": 'Insight Engine',
				"link": '#insight-engine'
			},
			{
				"label": _('User Registration'),
				"icon": "octicon octicon-diff-added",
				"type": 'doctype',
				"name": 'Registrations',
				"link": '#List/Registrations/List'
			}
		]
	}
	hook_icons = frappe.get_hooks("icons")
	for icon in hook_icons:
		 desktop.get(icon.get('module')).append(icon)

	return desktop