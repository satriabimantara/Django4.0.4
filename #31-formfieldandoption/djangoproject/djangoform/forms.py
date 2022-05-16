from django import forms

"""
Please Refers to:
URL: Django forms on Google
"""


class FormField(forms.Form):
    # python form data field
    interger_field = forms.IntegerField()
    decimal_field = forms.DecimalField()
    float_field = forms.FloatField()
    boolean_field = forms.BooleanField()
    char_field = forms.CharField()

    # string input
    email_field = forms.EmailField()
    regex_field = forms.RegexField(regex=r'(P?<test>)')
    slug_field = forms.SlugField()
    url_field = forms.URLField()
    ip_field = forms.GenericIPAddressField()

    # select input
    PILIHAN = (
        ("nilai1", "Pilihan1"),
        ("nilai2", "Pilihan2"),
        ("nilai3", "Pilihan3"),
        ("nilai4", "Pilihan4"),
        ("nilai5", "Pilihan5"),
    )
    choice_field = forms.ChoiceField(choices=PILIHAN)
    multi_choice_field = forms.MultipleChoiceField(choices=PILIHAN)
    multi_typed_choice = forms.TypedMultipleChoiceField(choices=PILIHAN)
    null_boolean_field = forms.NullBooleanField()

    # date time
    date_field = forms.DateField()
    datetime_field = forms.DateTimeField()
    duration_field = forms.DurationField()
    time_field = forms.TimeField()
    splitdatetime_field = forms.SplitDateTimeField()

    # file input
    file_field = forms.FileField()
    img_field = forms.ImageField()
