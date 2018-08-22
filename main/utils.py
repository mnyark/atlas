import pandas as pd
from .models import Record


def convert_excel_to_dict(filename, sheet_name='Sheet1'):
	df = pd.read_excel(filename, sheet_name=sheet_name)
	#strip whitespaces in columns + lowercase
	df.columns = df.columns.str.strip().lower()
	data = df.to_dict('data')
	return data


def ingest_bulk_data(data):
	""" Bulk inserts data(form of dictionary) into database """
	instances = [
		Record(time=a['time'], RER=a['rer'],Flow=a['flow'], delta_O2=a['delta o2'],
			delta_CO2=a['delta co2'], raw_O2=a['raw o2'], raw_CO2=a['raw co2'],
			tempearature=a['temp'], pressure=a['press'], RH=a['rh']) for a in data
	]
	Record.objects.bulk_create(instances)

