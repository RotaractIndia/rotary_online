# -*- coding: utf-8 -*-
# Copyright (c) 2021, Neil Lasrado, Rotaract Charitable Trust and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class OCV(Document):
	def validate(self):
		if self.ag_report:
			report_file = frappe.get_all("File", 
			filters={"file_url": self.ag_report, "attached_to_doctype": "OCV", "attached_to_name": self.name})
			if report_file:
				frappe.db.set_value("File", report_file[0].name, "attached_to_name", "")