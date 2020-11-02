# from django import forms
#
#
# class PhoneField(forms.Field):
#     widget = forms.TextInput
#
#     def to_python(self, value):
#         phone_dict = {
#             'country_code': value[1:-9],
#             'phone_number': value[-9:]
#         }
#         return phone_dict
#
#     def clean(self, value):
#         if value[0] != '+':
#             raise forms.ValidationError('The first symbol should be +')
#
#         return super(PhoneField, self).clean(value)
#
#     def validate(self, value):
#         if any(
#                 (
#                         not value['country_code'].isdigit(),
#                         not value['phone_number'].isdigit()
#                 )
#         ):
#             raise forms.ValidationError(
#                 '''Phone number should only contain digits'''
#             )
#         elif not 1 <= len(value['country_code']) <= 3:
#             raise forms.ValidationError('Wrong phone number length!')
#         return value
#
#     def widget_attrs(self, widget):
#         attrs = super(PhoneField, self).widget_attrs(widget)
#         return attrs
