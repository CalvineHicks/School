# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 21:03:41 2015

@author: calvinehicks

"""
def ternarySearch(a,k):
        if len(a) == 0:  
            print "should return FALSE"
            return  False
        elif len(a) == 1:
            if a[0] == k:
                print "should return true"
                return True
            else:
                print "should return false"
                return False
        else:
            print "else called"
            firstThird = (len(a)/3)
            secondThird = (2*len(a))/3
            if k < a[firstThird]:
                print "calling search first third"
                return ternarySearch(a[0:firstThird],k)
            elif (a[firstThird] <= k & k < a[secondThird]):
                print "calling search second third"
                return ternarySearch(a[firstThird:secondThird], k)
            else:
                print "calling search final third"               
                return ternarySearch(a[secondThird:], k)

print ternarySearch([5,6,7,56], 56)
