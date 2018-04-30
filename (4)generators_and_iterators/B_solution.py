def flatit(obj):
    try:
        for x in obj:
            yield from flatit(x)
    except:
        yield obj
