from django import template
register = template.Library()

def remove_slash(url):
    if 'add' in url:
        return url.replace('/add/','').replace('/','')
    return url.replace('/','')

register.filter('remove_slash', remove_slash)