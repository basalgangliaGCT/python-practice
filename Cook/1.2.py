records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4), 
]
def do_foo(x, y=None): 
    print('foo', x, y)

def do_bar(s): 
    # print(s)
    print('bar', s)

for tag, *args in records:
    # print(args)
    # print(*args) 
    if tag == 'foo':
        do_foo(args) 
        do_foo(*args) 
    elif tag == 'bar':
        do_bar(args)
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(fields)
print(*fields)
print(homedir)
print(sh)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

items = [1, 10, 7, 4, 5, 9]
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
print(sum(items))