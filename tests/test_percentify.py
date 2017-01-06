#!/usr/bin/env python

if __name__ == "__main__":

    from formatlib import percentify

    x = ['a','b','c','d','e','f']
    y = [25,15,10,20,17,13]
    z = [393,94,149,300,371,469]
    w = [1,2,4,4,5,7,0]
    v = [1991,219,7390,722,972,1234,8920,7]
    ls = [y, z, w, v]
    for l in ls:
        lp = percentify(l,4)
        s = sum(lp)
        print l, '\n', lp
        for each in l:
            print each, lp.pop(0)
        print s, '\n'
    d = dict()
    lx = y[:]
    for each in x:
        d[each] = lx.pop()
    dp = percentify(d)
    print d, dp, sum(dp[k] for k in dp.keys())
    

