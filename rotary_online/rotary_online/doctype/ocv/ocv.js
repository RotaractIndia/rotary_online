// Copyright (c) 2021, Neil Lasrado, Rotaract Charitable Trust and contributors
// For license information, please see license.txt

frappe.ui.form.on('OCV', {
	open_ocv_report: function(frm) {
		var win = window.open(frm.doc.ocv_report, '_blank');
 		win.focus();
	}
});
