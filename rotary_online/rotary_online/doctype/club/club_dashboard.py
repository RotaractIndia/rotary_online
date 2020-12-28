from frappe import _

def get_data():
	return {
		'heatmap': True,
		'fieldname': 'club',
		'transactions': [
			{
				'label': 'Activities',
				'items': ['Meeting', 'Project', 'District Event']
			},
			{
				'label': 'Entity',
				'items': ['Member', 'Registrations']
			}
		]
	}