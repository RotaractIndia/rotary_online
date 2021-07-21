# Copyright (c) 2013, Neil Lasrado, Rotaract Charitable Trust and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns = ["Club Name::150", "Members::80", "Projects::80", "Global Grant:Currency:150", "Total Expenses:Currency:150", "Foundation Contribution(USD):Currency:250"]
	data = []

	for club in frappe.get_all("Club"):
		row = [club.name]
		row.append(get_member_count(club.name))
		project_stats = get_project_stat(club.name)
		row.append(project_stats[0])
		row.append(project_stats[1])
		row.append(project_stats[2])
		row.append(foundation_conntribution(club.name))
		data.append(row)
	return columns, data

def get_member_count(club):
	members = frappe.db.sql("SELECT count(name) from `tabMember` where club = %s and status!='Ex Rotarian'",club)
	return members[0][0]

def get_project_stat(club):
	project = frappe.db.sql("SELECT count(name), sum(global_grant), sum(expenditure) from `tabProject` where club = %s and docstatus=1",club)
	return project[0]

def foundation_conntribution(club):
	contribution = frappe.db.sql("SELECT sum(amount_contributed) from `tabFoundation Contribution` where club = %s and docstatus=1",club)
	return contribution[0][0]
