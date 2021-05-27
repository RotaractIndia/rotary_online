# -*- coding: utf-8 -*-
# Copyright (c) 2020, Neil Lasrado, Rotaract Charitable Trust and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import add_years
from frappe.model.document import Document

class Club(Document):
	def validate(self):
		if self.assistant_governor:
			set_role_permission(self.assistant_governor)
			set_user_permission(self.assistant_governor, self.name)
		if self.assistant_trainer:
			set_user_permission(self.assistant_trainer, self.name)
		if self.district_secretary:
			set_user_permission(self.district_secretary, self.name)

def set_user_permission(user, club):
	existing_perm = frappe.get_all("User Permission", filters={'user':user, 'allow': 'Club', 'for_value': club})
	if not existing_perm:
		permission = frappe.new_doc("User Permission")
		permission.user = user
		permission.allow = "Club"
		permission.for_value = club
		permission.save(ignore_permissions=True)
	
def set_role_permission(ag):
	user=frappe.get_doc("User", ag)
	user.update({
		"roles": [
			{"role": "Assistant Governor"},
			{"role": "District Official"}		
		]
	})
	user.save(ignore_permissions=True)

def get_timeline_data(doctype, name):
	project_data = dict(frappe.db.sql('''select unix_timestamp(date(end_time)), count(*)
		from `tabProject` where club=%s
			and end_time > date_sub(curdate(), interval 1 year)
			and docstatus < 2
			group by date(end_time)''', name))

	meeting_data = dict(frappe.db.sql('''select unix_timestamp(date), count(*)
		from `tabMeeting` where club=%s
			and date > date_sub(curdate(), interval 1 year)
			and docstatus < 2
			group by date(date)''', name))

	heatmap_data = merge_dicts(project_data, meeting_data)
	return heatmap_data

def merge_dicts(dict1, dict2):
	''' Merge dictionaries and add values of common keys'''
	dict3 = {**dict1, **dict2}
	for key, value in dict3.items():
		if key in dict1 and key in dict2:
			dict3[key] = value + dict1[key]

	return dict3 
