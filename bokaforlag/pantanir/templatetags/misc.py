from django import template


register = template.Library()


@register.filter(name="verd")
def verd(value):
    return str("{:,}".format(value)).replace(",", ".")
