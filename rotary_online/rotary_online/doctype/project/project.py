# -*- coding: utf-8 -*-
# Copyright (c) 2020, Neil Lasrado, Rotaract Charitable Trust and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cint, cstr, now, getdate, add_months, add_days
from frappe.model.document import Document

class Project(Document):
	def validate(self):
		self.validate_date()
		self.calculate_totals()
		self.set_zone()
		self.document_status='draft'
		self.reporting_month = getdate(self.end_time).strftime("%B")

	def on_submit(self):
		frappe.db.set_value('Project', self.name, 'document_status', 'submitted')

	def on_cancel(self):
		frappe.db.set_value('Project', self.name, 'document_status', 'cancelled')

	def calculate_totals(self):
		self.rotarians = len(self.project_attendance)
		self.total = cint(self.rotarians) + cint(self.other_club) + cint(self.partners) \
			+ cint(self.guest)
		self.income = self.club_fund + self.club_member + self.district_grant + self.district_fund + \
			self.global_grant + self.sponsor + self.csr + self.other

	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")

	def validate_date(self):
		if self.end_time > now():
			frappe.throw("Did you fix the Flux Capacitor ? \n Project End Time is Greater than today.")

		if self.start_time > self.end_time:
			frappe.throw("Start Time cannot be greater than End Time.")
