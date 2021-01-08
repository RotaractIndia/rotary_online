// Copyright (c) 2021, Neil Lasrado, Rotaract Charitable Trust and contributors
// For license information, please see license.txt

frappe.ui.form.on('GML', {
	open_gml: function(frm) {
		var win = window.open(frm.doc.gml_link, '_blank');
 		win.focus();
	}
});
