from django import template
register = template.Library()

def remove_slash(url):
    if 'add' in url:
        return url.replace('/add/','').replace('/','')
    return url.replace('/','')

def remove_board(url):
    if 'board' in url:
        return url.replace('board','').replace('/','')
    return url.replace('/','')


def remove_text(url):
    if 'board' in url:
        return url.replace('board','').replace('/','')
    return url.replace('/','')

register.filter('remove_slash', remove_slash)
register.filter('remove_board', remove_board)