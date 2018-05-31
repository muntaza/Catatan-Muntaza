### $Id: forms.py,v 1.1 2016/07/12 01:12:31 muntaza Exp $


from django import forms


class DibayarForm(forms.ModelForm):
    dibayar = forms.DecimalField(label="Dibayar (Rp)", max_digits=15, decimal_places=0, localize=True, initial=0)
