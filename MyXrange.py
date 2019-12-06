def xrange(start, end, strobe=1):
    while start < end:
        yield start
        start += strobe

"""
>>>
>>> from MyXrange import xrange
>>>
>>> for i in xrange(1, 5):print i
...
1
2
3
4
>>>
>>> for i in xrange(1, 10, 3):print i
...
1
4
7
>>>
"""
