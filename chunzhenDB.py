#coding=gbk
import socket
import struct
import re
        
def ip2long(ip):
    return struct.unpack('!I',socket.inet_aton(ip))[0]

def long2ip(longip):
    return socket.inet_ntoa(struct.pack('!I', ip))

class ChunzhenDB:
    quick_chunzhen={}
    chunzhen_dic={}
    ipList=[]
    def init(self):
        self.quick_chunzhen={}
        self.chunzhen_dic={}
        self.ipList=[]
        
    def CreateNewChunzhen(self, filename='newchunzhen.txt'):
        with open(filename, 'rb') as f:
            lines=f.readlines()
        f=open('chunzhen.csv', 'wb')
        for line in lines:
            line=line.strip('\r\n')
            lineargs=re.split(r' +',line)
            try:
                int_ip=ip2long(lineargs[0])
            except:
                print 'illegal IP addr: %s' % lineargs[0]
                continue
            f.write('%s,%s\n' % (int_ip, ' '.join(lineargs[2:])))
        f.close()
        
    def loadChunzhenDB(self, filename='chunzhen.csv'):
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        firstLine=True
        for line in lines:
            if firstLine:
                firstLine=False
                continue
            lineargs = line.split(',')
            self.chunzhen_dic[long(lineargs[0])] = lineargs[1].decode('utf8','ignore').encode('gbk')
        self.ipList=self.chunzhen_dic.keys()
        self.ipList.sort()
            
    def GetChunzhenInfo(self, ip):
        if self.quick_chunzhen.has_key(ip):
            return self.quick_chunzhen[ip]
        else:
            longip = ip2long(ip)
            x=0
            y=len(self.chunzhen_dic)-1
            while(x!=y-1):
                mid = (x+y)/2
                if self.ipList[mid]==longip:
                    break;
                elif self.ipList[mid]<longip:
                    x=mid
                else:
                    y=mid
            self.quick_chunzhen[ip]=self.chunzhen_dic[self.ipList[x]]
            return self.chunzhen_dic[self.ipList[x]]

def main_demo():
    outfile = open('out.csv', 'w')
    chunzhendb = ChunzhenDB()
    chunzhendb.loadChunzhenDB()
    
    infile = open('ip.txt', 'r')
    lines = infile.readlines()
    for line in lines:
        line = line.strip('\n')
        outfile.write('%s,%s\n' % (line, chunzhendb.GetChunzhenInfo(line)))
    outfile.close()

def main_demo2():
    cz=ChunzhenDB()
    cz.CreateNewChunzhen()
