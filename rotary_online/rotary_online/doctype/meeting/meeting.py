# -*- coding: utf-8 -*-
# Copyright (c) 2020, Neil Lasrado, Rotaract Charitable Trust and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cint, getdate, today, to_timedelta
from frappe.model.document import Document

class Meeting(Document):
	def validate(self):
		self.validate_date()
		self.calculate_totals()
		self.set_zone()
		self.document_status='draft'
		self.reporting_month = getdate(self.date).strftime("%B")

	def on_submit(self):
		frappe.db.set_value('Meeting', self.name, 'document_status', 'submitted')

	def on_cancel(self):
		frappe.db.set_value('Meeting', self.name, 'document_status', 'cancelled')

	def calculate_totals(self):
		self.total = cint(self.rotarians) + cint(self.other_club) + cint(self.partners) \
			+ cint(self.guest)
	
	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")

	def validate_date(self):
		if self.date > today():
			frappe.throw("Did you fix the Flux Capacitor ? \n Meeting Date is Greater than today.")

		if to_timedelta(self.start_time) > to_timedelta(self.end_time):
			frappe.throw("Start Time cannot be greater than End Time.")
