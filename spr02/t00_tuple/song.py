def song(verses, chorus):
    res = ()
    for buf in verses:
        res += buf + chorus
    res += chorus
    return res