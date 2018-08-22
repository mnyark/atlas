from django.db import models

class Record(models.Model):
	time = models.DecimalField(max_digits=8, decimal_places=5)
	RER = models.IntegerField(null=True)
	Flow = models.DecimalField(max_digits=8, decimal_places=5)
	delta_O2 = models.DecimalField(max_digits=8, decimal_places=5)
	delta_CO2 = models.DecimalField(max_digits=8, decimal_places=5)
	VES = models.DecimalField(max_digits=8, decimal_places=5, null=True)
	raw_O2 = models.DecimalField(max_digits=8, decimal_places=5)
	raw_CO2 = models.DecimalField(max_digits=8, decimal_places=5)
	Temperature = models.DecimalField(max_digits=8, decimal_places=5, null=True)
	Pressure = models.DecimalField(max_digits=8, decimal_places=5, null=True)
	RH_percentage = models.DecimalField(max_digits=8, decimal_places=5, null=True)
	RH = models.DecimalField(max_digits=8, decimal_places=5, null=True)

	#attrs to compute
	#EE(Energy Expenditure),
	#RH(Relative Humidity),
	#RER(Respiratory Exchange Ratio), 
	#RQ(Respiratory Quotient),
	#VO_2(Oxygen Consumption),
	#VCO_2(Carbondioxide Consumption),
	#Haldane
	EE = models.DecimalField(max_digits=8, decimal_places=5, null=True) 
	RH = models.DecimalField(max_digits=8, decimal_places=5, null=True)
	RQ = models.DecimalField(max_digits=8, decimal_places=5, null=True)
	VO_2 = models.DecimalField(max_digits=8, decimal_places=5, null=True)
	VCO_2 = models.DecimalField(max_digits=8, decimal_places=5, null=True)
	Haldane = models.DecimalField(max_digits=8, decimal_places=5, null=True)

	def compute(self):
		pass

	def compute_EE(self):
		pass

	def compute_VO_2(self):
		pass

	def compute_VCO_2(self):
		pass

	def compute_RQ(self):
		pass

	def compute_Haldane(self):
		pass

	def compute_RH(self):
		pass

	def save(self, *args, **kwargs):
		self.compute()
		super().save(*args, **kwargs)

	def __str__(self):
		return f'<{self.EE} {self.RQ}>'