# -*- coding: utf-8 -*-
# Copyright (c) 2020, Neil Lasrado, Rotaract Charitable Trust and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Registrations(Document):
	def before_submit(self):
		user = frappe.new_doc("User")
		user.update({
			"first_name": self.first_name,
			"last_name": self.last_name,
			"email": self.email,
			"mobile_no": self.mobile_number,
			"send_welcome_email": 1
		})
		user.save(ignore_permissions=True)
		user.update({
			"roles": [
				{"role": "Club Member - Full Access"}
			],
			"bio": self.club
		})
		user.save(ignore_permissions=True)
		self.user = user.name
		self.enabled=True
		permission = frappe.new_doc("User Permission")
		permission.user = user.name
		permission.allow = "Club"
		permission.for_value = self.club
		permission.save(ignore_permissions=True)

	def on_update_after_submit(self):
		if self.user:
			user=frappe.get_doc("User", self.user)
			user.enabled=self.enabled
			if self.limited_access:
				user.update({
					"roles": [
						{"role": "Club Member - Limited Access"}
					]
				})
			else:
				user.update({
					"roles": [
						{"role": "Club Member - Full Access"}
					]
				})
			user.save(ignore_permissions=True)