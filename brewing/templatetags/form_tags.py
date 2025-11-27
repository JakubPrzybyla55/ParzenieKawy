from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    """
    Adds a CSS class to a form field.
    Usage: {{ form.field|add_class:"class-name" }}
    """
    if hasattr(value, 'as_widget'):
        return value.as_widget(attrs={'class': arg})
    return value
