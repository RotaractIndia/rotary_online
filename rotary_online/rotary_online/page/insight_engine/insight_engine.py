from datetime import timedelta

import frappe
import datetime
from frappe.utils import flt, cint
from collections import defaultdict

@frappe.whitelist()
def get_dashboards(club=None):
	if not club:
		return None

	project_stats = frappe.get_all("Project",
		filters={"club": club, "docstatus": 1},
		fields=["""count(name) as project_count, sum(income) as income, sum(expenditure) as expense,
			sum(total) as footfall, sum(number_of_hours) as total_time"""])

	meeting_stats = frappe.get_all("Meeting",
		filters={"club": club, "docstatus": 1},
		fields=["count(name) as meeting_count, sum(TIMEDIFF(end_time, start_time)) as total_time"])

	top_projects = frappe.get_all("Project",
		filters={"club": club, "docstatus": 1},
		fields=["name","project_name", "avenue_1", "avenue_2", "(income - expenditure) as net_profit"],
		order_by="net_profit desc",
		limit=5)

	project_category = frappe.get_all("Project",
		filters={"club": club, "docstatus": 1},
		fields=["project_category", "count(name) as count"],
		group_by="project_category")
	
	type_of_meeting = frappe.get_all("Meeting",
		filters={"club": club, "docstatus": 1},
		fields=["type_of_meeting", "count(name) as count"],
		group_by="type_of_meeting")
	
	project_funds = frappe.get_all("Project",
		filters={"club": club, "docstatus": 1},
		fields=["sum(club_fund) as 'Club Fund'", "sum(club_member) as 'Club Member'", 
			"sum(district_grant) as 'District Grant'", "sum(district_fund) as 'District Fund'",
			"sum(global_grant) as 'Global Grant'", "sum(sponsor) as 'Sponsor'", 
			"sum(csr) as 'CSR'", "sum(trust_fund) as 'Trust Fund'", "sum(other) as 'Other'"])
			
	source_of_funds = []
	for source in project_funds[0]:
		source_of_funds.append({
			"source": source,
			"amount": project_funds[0].get(source)
		})
	
	projects_by_month = frappe.get_all("Project",
		filters={"club": club, "docstatus": 1},
		fields=["month(end_time) as month", "count(name) as count"],
		group_by="month", order_by="month")

	current_month = datetime.datetime.now().strftime("%B")
	reporting_months = []
	for month in ['July', 'August', 'September', 'October', 'November',
		'December','January','Febuary','March', 'April', 'May']:
			reporting_months.append(month)
			if month == current_month:
				break;

	avenues = frappe.get_all("Avenue")
	project_count = defaultdict(list)
	project_hours = defaultdict(list)

	for month in reporting_months:
		month_project_count = defaultdict(int)
		month_project_hours = defaultdict(int)

		projects = get_club_projects(club, month)
		if projects:
			for project in projects:
				month_project_hours[project.avenue_1] +=cint(project.total_time) 
				month_project_hours[project.avenue_2] +=cint(project.total_time)

				month_project_count[project.avenue_1] +=1
				month_project_count[project.avenue_2] +=1

		for avenue in avenues:
			project_count[avenue.name].append(month_project_count[avenue.name])
			project_hours[avenue.name].append(month_project_hours[avenue.name])

	return {
		"total_income": project_stats[0].income,
		"total_expenses": project_stats[0].expense,
		"net_profit": flt(project_stats[0].income) - flt(project_stats[0].expense),
		"total_footfall": cint(project_stats[0].footfall),
		"total_projects": project_stats[0].project_count,
		"total_project_time": cint(project_stats[0].total_time),
		"total_meetings":  cint(meeting_stats[0].meeting_count),
		"total_meeting_time": cint(meeting_stats[0].total_time) // 3600,
		"top_projects": top_projects,
		"project_category": project_category,
		"projects_per_month": project_count,
		"projects_time_per_month": project_hours,
		"reporting_months": reporting_months,
		"source_of_funds": source_of_funds,
		"type_of_meeting": type_of_meeting
	}

def get_club_projects(club, month):
	projects = frappe.get_all("Project",
		filters={"club": club, "reporting_month": month, "docstatus": 1},
		fields=["avenue_1", "avenue_2", "number_of_hours as total_time"])
	return projects

