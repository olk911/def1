def get_absolute_url(url, *arge, **kwarge):
    for i in arge:
        url += '/'
        url += i
        if arge.index(i) > (len(arge)-1):
            url = url + '?'  
    
    for k,v in kwarge.items():
        url += '?'
        url += f'{k}={v}'

    return url

print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))