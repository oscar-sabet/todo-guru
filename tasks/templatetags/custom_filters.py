from django import template
import datetime

register = template.Library()


@register.filter
def format_timedelta_days(value):
    if isinstance(value, datetime.timedelta):
        days = value.days
        return f"{days}d"
    return value


@register.filter
def format_timedelta_hours(value):
    if isinstance(value, datetime.timedelta):
        seconds = value.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{hours}h, {minutes}m"
    return value
