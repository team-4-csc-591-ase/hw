
'''
local NUM,SYM = obj"NUM",obj"SYM"
function SYM.new(i) --> SYM; constructor
  i.n   = 0
  i.has = {}
  i.most, i.mode = 0,nil end

function SYM.add(i,x) 
  if x ~= "?" then 
   i.n = i.n + 1 
   i.has[x] = 1 + (i.has[x] or 0)
   if i.has[x] > i.most then
     i.most,i.mode = i.has[x], x end end end 

function SYM.mid(i,x) return i.mode end --> n; return the mode
function SYM.div(i,x,    fun,e) --> n; return the entropy
  function fun(p) return p*math.log(p,2) end
  e=0; for _,n in pairs(i.has) do e = e + fun(n/i.n) end 
  return -e end
'''

import math
import sys

class Newclass():
    n = 0
    has ={}
    most = 0
    mode = None    

    def rnd(self,nPlaces):
        mult = math.pow(10,3)
        return math.floor((self.n * mult)+0.5)/mult

    def add(self,x):
        # print(x)
        if x!="?":
            self.n = self.n+1
            if (x in self.has):
                y = self.has[x]
            else:
                y = 0
            self.has[x] = 1 + y
            if self.has[x]>self.most:
                self.most,self.mode = self.has[x],x

    def mid(self,x):
        return self.mode

    def div(self,x):
        def fun(p):
            return p*(math.log2(p))
        e = 0
        for k,v in self.has.items():
            e = e+fun(v/self.n)
        return -e

testobj = Newclass()

l = ["a","a","a","a","b","b","c"]
for x in l:
    testobj.add(x)
findMid = testobj.mid(x)
divValue = testobj.rnd(testobj.div(x))
print("a"==findMid and 1.379==round(testobj.div(x),3))


#NUM
'''
function NUM.new(i) --> NUM;  constructor; 
  i.n, i.mu, i.m2 = 0, 0, 0
  i.lo, i.hi = math.huge, -math.huge end

function NUM.add(i,n) --> NUM; add `n`, update lo,hi and stuff needed for standard deviation
  if n ~= "?" then
    i.n  = i.n + 1
    local d = n - i.mu
    i.mu = i.mu + d/i.n
    i.m2 = i.m2 + d*(n - i.mu)
    i.lo = math.min(n, i.lo)
    i.hi = math.max(n, i.hi) end end

eg("rand","generate, reset, regenerate same", function()
  local num1,num2 = NUM(),NUM()
  Seed=the.seed; for i=1,10^3 do num1:add( rand(0,1) ) end
  Seed=the.seed; for i=1,10^3 do num2:add( rand(0,1) ) end
  local m1,m2 = rnd(num1:mid(),10), rnd(num2:mid(),10)
  return m1==m2 and .5 == rnd(m1,1) end )


function NUM.mid(i,x) return i.mu end --> n; return mean
function NUM.div(i,x)  --> n; return standard deviation using Welford's algorithm http://t.ly/nn_W
    return (i.m2 <0 or i.n < 2) and 0 or (i.m2/(i.n-1))^0.5  end

eg("num", "check nums", function()
  local num=NUM()
  for _,x in pairs{1,1,1,1,2,2,3} do num:add(x) end
  return 11/7 == num:mid() and 0.787 == rnd(num:div()) end )
'''
class newNum():
    Seed=937162211
    n, mu, m2 = 0, 0, 0
    lo, hi = sys.maxsize, -sys.maxsize

    def add(self,n):
        if n != "?":
            self.n = self.n+1
            d = self.n-self.mu
            self.mu = self.mu+(d/self.n)
            self.m2=self.m2+(d*(self.n-self.mu))
            self.lo=min(self.n,self.lo)
            self.hi=max(self.n,self.hi)
    
    def mid(self,x):
        return self.mu

    def div(self,x):
        return (self.m2 <0 or self.n < 2) and 0 or pow((self.m2/(self.n-1)),0.5)

    def rand(self,ho,li):
        lo,hi = self.lo or 0, self.hi or 1
        Seed = (16807 * self.Seed) % 2147483647
        return lo + (hi-lo) * Seed / 2147483647

    def rnd(self,n,nPlaces=3):
        mult=pow(10,nPlaces)
        return math.floor(n * mult + 0.5) / mult

numobj = newNum()

numList = [1,1,1,1,2,2,3]
for x in numList:
    numobj.add(x)
print(numobj.mid(x))
print(round(numobj.div(x),3))
print(11/7==numobj.mid(x) and 0.787==round(numobj.div(x),3))

num1,num2 = newNum(), newNum()
print(num1.lo)
print(num1.hi)
for i in range(1,pow(10,3)):
    num1.add(num1.rand(0,1))
for i in range(1,pow(10,3)):
    num2.add(num2.rand(0,1))
m1,m2 = num1.rnd(num1.mid(x),10), num2.rnd(num2.mid(x),10)
print(m1)
print(m2)
print(m1==m2 and 0.5==round(m1,1))







