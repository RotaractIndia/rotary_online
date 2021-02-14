frappe.listview_settings['Member'] = {
	add_fields: ["status"],
	filters: [["status","!=", "Ex Rotarian"]],
	
	get_indicator: function(doc) {
		if(doc.status=="Regular") {
			return [__("Regular"), "green", "status,=,'Regular'"];
		} else if(doc.status=="Honorary")  {
			return [__("Honorary"), "grey",  "status,=,'Honorary'"];
		} else {
			return [__("Ex Rotarian"), "red", "status,=,'Ex Rotarian'"];
		}
	}
};