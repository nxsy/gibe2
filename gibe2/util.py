import itertools

def multigroupby(it, *funcs):
    grp = itertools.groupby(it, funcs[0])
    if len(funcs) == 1:
        return grp
    return ((key, multigroupby(grpit, *funcs[1:])) for key, grpit in grp)

def day(r):
    return r.meta['published'].day

def month(r):
    return r.meta['published'].month

def year(r):
    return r.meta['published'].year

class DatedPost(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

def datedposts(posts):
    for y, posts in multigroupby(posts, year, month, day):
        firsty = True
        for m, posts in posts:
            firstm = True
            for d, posts in posts:
                firstd = True
                for post in posts:
                    yield DatedPost(year=year(post),month=month(post),day=day(post),firsty=firsty,firstm=firstm,firstd=firstd), post
                    firsty = firstm = firstd = False

