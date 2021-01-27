from frappe import _

def get_data():
	return {
		'heatmap': False,
		'fieldname': 'ocv',
		'transactions': [
			{
				'label': "AG's Reports",
				'items': ['AG OCV Report']
			}
		]
	}