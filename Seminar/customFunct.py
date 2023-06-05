def LastFib(n):
    if n in [0, 1]:
        return n
    return LastFib(n-1) + LastFib(n-2)
