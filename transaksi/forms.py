from django.forms import ModelForm
from .models import *
from bootstrap_datepicker_plus.widgets import DatePickerInput
class TransaksiPembelianForm(ModelForm):
    class Meta:
        model = TransaksiPembelian
        exclude = []
        widgets = {
            'tanggal_format': DatePickerInput(format='%d-%m-%Y').start_of('event days'),
        }
class TransaksiPenjualanForm(ModelForm):
    class Meta:
        model = TransaksiPenjualan
        exclude = []

    