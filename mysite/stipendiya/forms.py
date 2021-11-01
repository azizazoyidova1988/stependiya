from django import forms
from .models import *


class VazirlikForm(forms.ModelForm):
    class Meta:
        model = Vazirlik()
        fields = '__all__'


class OTMForm(forms.ModelForm):
    class Meta:
        model = OTM()
        fields = '__all__'


class TalabaForm(forms.ModelForm):
    class Meta:
        model = Talaba()
        fields = "__all__"


class ArizaStatusForm(forms.ModelForm):
    class Meta:
        model = Ariza_statusi()
        fields = '__all__'



class TalimTuriForm(forms.ModelForm):
    class Meta:
        model = Talim_turi()
        fields = '__all__'


class YangiArizalarForm(forms.ModelForm):
    class Meta:
        model = Yangi_arizalar()
        fields = '__all__'


class QabulqilinganarizaForm(forms.ModelForm):
    class Meta:
        model = Qabul_qilingan_arizalar()
        fields = '__all__'


class RadqilinganarizaForm(forms.ModelForm):
    class Meta:
        model = Rad_qilingan_arizalar()
        fields = '__all__'


class AdminstratorForm(forms.ModelForm):
    class Meta:
        model = Administrator_royxati()
        fields = '__all__'