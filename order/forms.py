from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	STATE_CHOICES = (
		('tamilnadu', 'tamilnadu'),
	
	)

	DISCRICT_CHOICES = (
		('chennai', 'chennai'), 
		('tirunelveli', 'tirunelveli'),
		('tirichi', 'tirichi'),
		('tuticorin','tuticorin'),
		('madurai','madurai'),
	)

	PAYMENT_METHOD_CHOICES = (
		('gpay', 'gpay'),
		('phone pay','PHONE PAY'),
		('COD available','cash on delievery'),
		
	)

	division = forms.ChoiceField(choices=STATE_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
