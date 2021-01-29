# -*- coding: utf-8 -*-
# Copyright (c) 2020, Neil Lasrado, Rotaract Charitable Trust and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class EventParticipation(Document):
	def validate(self):
		self.set_zone()
		self.rotarians = len(self.project_attendance)

	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")


