from django import forms
METRIC_CHOICES=[
        ('Kilograms','kilograms'),
        ('Tonnes','tonnes')
    ]
YEAR_CHOICES=[
        (1990,1990),
        (1991,1991),
        (1992,1992),
        (1993,1993),
        (1994,1994),
        (1995,1995),
        (1996,1996),
        (1997,1997),
        (1998,1998),
        (1999,1999),
        (2000,2000)

    ]
list1=[[]]
class MyForm(forms.Form):
 year1 = forms.IntegerField(widget=forms.Select(choices=YEAR_CHOICES),required=False)
 quantity1 = forms.IntegerField(label='Quantity',required=False)
 metric1= forms.CharField(widget=forms.Select(choices=METRIC_CHOICES),required=False)
 year2 = forms.IntegerField(widget=forms.Select(choices=YEAR_CHOICES),required=False)
 quantity2 = forms.IntegerField(label='end year',required=False)
 metric2= forms.CharField(widget=forms.Select(choices=METRIC_CHOICES),required=False)
 year3 = forms.IntegerField(widget=forms.Select(choices=YEAR_CHOICES),required=False)
 quantity3 = forms.IntegerField(label='end year',required=False)
 metric3= forms.CharField(widget=forms.Select(choices=METRIC_CHOICES),required=False)
 year4 = forms.IntegerField(widget=forms.Select(choices=YEAR_CHOICES),required=False)
 quantity4 = forms.IntegerField(label='end year',required=False)
 metric4= forms.CharField(widget=forms.Select(choices=METRIC_CHOICES),required=False)
 year5 = forms.IntegerField(widget=forms.Select(choices=YEAR_CHOICES),required=False)
 quantity5 = forms.IntegerField(label='end year',required=False)
 metric5= forms.CharField(widget=forms.Select(choices=METRIC_CHOICES),required=False)
 


        
