### $Id: forms.py,v 1.1 2017/09/03 02:18:04 muntaza Exp $


from django import forms


class BantuanForm(forms.ModelForm):
    bantuan = forms.DecimalField(label="Bantuan", max_digits=15, decimal_places=0, localize=True, initial=0)
