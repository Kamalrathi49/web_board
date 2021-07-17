from django import template
register = template.Library()

def remove_slash(url):
    return url.replace('/','')

register.filter('remove_slash', remove_slash)