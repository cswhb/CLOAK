#coding:utf-8
import random
import numpy as np
import defenselayer_bwl_climber as dl
import sys
tracepath = 'trace.dat'
endstatpath = 'endstat.dat'
logpath = 'log.dat'
endlifepath = 'endlife.dat'
initlifepath = 'initlife.dat'
areashift = 0 
maxpagenums = (4194304>>2) >> areashift 
isbreak = 0#
attacktype = 0
attackpp = 1
endnums = 200001000
climbershift = 17
##########################################################
class AcListGenerator:
    def __init__(self, type1, areasize, attackpp,climberenable, randomenable, stallenable):
        self.type = type1
        self.areasize = maxpagenums
        self.flag = 0
        self.index = 0
        self.round = 0
        self.count = 0
        self.hot = 100000
        pageshift = 12
        self.filelength = 0
        self.tracepoint = 0
        self.visitcountnow = 0
        with open(tracepath) as tracefile:
            for line in tracefile:
                temp = int(line)
                self.filelength = self.filelength + 1
        self.d1 = dl.DefenseLayer(self.areasize, self.type, climberenable, randomenable, stallenable,climbershift)
        self.visitlist = [0 for i in range(self.filelength)]
        self.filelength = 0
        with open(tracepath) as tracefile:
            for line in tracefile:
                temp = int(line)
                self.visitlist[self.filelength] = temp>>pageshift
                self.filelength = self.filelength + 1
    def getindex(self):
        if self.tracepoint >= self.filelength:
            self.tracepoint = 0
        self.visitcountnow = self.visitcountnow + 1
        if self.visitcountnow == endnums:
            return -1
        ans = self.visitlist[self.tracepoint] % self.areasize
        self.tracepoint = self.tracepoint + 1
        return ans

if len(sys.argv) == 1:
    g1 = AcListGenerator(attacktype,maxpagenums,attackpp,0,0,0)
elif len(sys.argv) == 2:
    g1 = AcListGenerator(attacktype,maxpagenums,attackpp,int(sys.argv[1]),0,0)
elif len(sys.argv) == 3:
    g1 = AcListGenerator(attacktype,maxpagenums,attackpp,int(sys.argv[1]),int(sys.argv[2]),0)
elif len(sys.argv) == 4:
    g1 = AcListGenerator(attacktype,maxpagenums,attackpp,int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
#d1 = dl.memorymodel(maxpagenums, self.type)
while isbreak == 0:
    addr = g1.getindex()
    if addr == -1:
        g1.d1.m1.printstat()
        isbreak = 1
        break
    memorystat = g1.d1.access(addr)
    if memorystat[0] == -1:
        m1.printstat()
        isbreak = 1
print("end");
