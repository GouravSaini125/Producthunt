from django.template.defaulttags import register

@register.filter(name='lookup')
def lookup(dict,key):
    return dict.get(key)
