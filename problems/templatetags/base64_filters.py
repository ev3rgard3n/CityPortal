import base64
from django import template

register = template.Library()

@register.filter
def base64_encode(binary_data):
    if binary_data:
        return base64.b64encode(binary_data).decode('utf-8')
    return None
