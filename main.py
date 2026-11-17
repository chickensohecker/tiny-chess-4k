import json,os,random,sys,urllib.request as R
E=os.environ.get('MAKEFUN_ENV_URL') or sys.exit('no env')
V=[0,100,320,330,500,900,0]
M=100000
BUD=100000
B=[0]*128
w=1;C=0;EP=-1;HM=0;S=0;H=0;K=[0,0];BP=[0,0];ZH=0
U=[];N=[0];RP={}
KL=[[0,0] for _ in range(128)]
TH=[0]*(1<<17);TD=[0]*(1<<17);TF=[0]*(1<<17);TS=[0]*(1<<17);TM=[0]*(1<<17)
CL={(4,6):(7,5),(4,2):(0,3),(116,118):(119,117),(116,114):(112,115)}
CB={0:2,7:1,112:8,119:4}
g=random.Random(12345)
Z=[[g.getrandbits(64) for _ in range(128)] for _ in range(12)]
ZS=g.getrandbits(64);ZC=[g.getrandbits(64) for _ in range(16)];ZE=[g.getrandbits(64) for _ in range(8)]
def T(t,r,f):
 c=min(f,7-f)+min(r,7-r)
 return[0,0,4,8,14,24,40,0][r]+([0,0,0,10,15,10,5,0][r] if f==3 or f==4 else 0)if t==1 else 6*c-20 if t==2 else 4*c-8 if t==3 else(15 if r==6 else 0)+(5 if r==0 and(f==3 or f==4)else 0)if t==4 else 2*c-6 if t==5 else[20,25,10,0,0,10,25,20][f] if r==0 else max(-50,-15*r)if t==6 else 8*c-24
def W(x,s):
 a=abs(x);r=s>>4 if x>0 else 7-(s>>4)
 return(V[a]+T(a,r,s&7))*(1 if x>0 else-1)
def ev():
 p=min(H,7800);d=7800-p
 a=K[0];b=K[1]
 e=(T(7,a>>4,a&7)-T(6,a>>4,a&7)-T(7,7-(b>>4),b&7)+T(6,7-(b>>4),b&7))*d//7800
 s=S+e+30*((BP[0]>1)-(BP[1]>1))
 return s if w else-s
def A(s,y):
 for o in(-15,-17)if y else(15,17):
  t=s+o
  if not t&0x88 and B[t]==(1 if y else-1):return 1
 for o,v in((-33,2),(-31,2),(-18,2),(-14,2),(14,2),(18,2),(31,2),(33,2),(-17,6),(-16,6),(-15,6),(-1,6),(1,6),(15,6),(16,6),(17,6)):
  t=s+o
  if not t&0x88 and B[t]==(v if y else-v):return 1
 for d in(-17,-15,15,17):
  t=s+d
  while not t&0x88:
   q=B[t]
   if q:
    if q in((3,5) if y else(-3,-5)):return 1
    break
   t+=d
 for d in(-16,-1,1,16):
  t=s+d
  while not t&0x88:
   q=B[t]
   if q:
    if q in((4,5) if y else(-4,-5)):return 1
    break
   t+=d
 return 0
def G(q):
 L=[]
 for s in range(128):
  if s&0x88:continue
  p=B[s]
  if not p or(p>0)!=w:continue
  a=abs(p);f=s&7;r=s>>4
  if a==1:
   d=16 if p>0 else-16
   t=s+d
   if not t&0x88 and not B[t]:
    if r==(6 if p>0 else 1):
     for pr in(5,4,3,2):L.append(s|(t<<7)|(pr<<14))
    elif not q:
     L.append(s|(t<<7))
     if r==(1 if p>0 else 6):
      t2=s+2*d
      if not B[t2]:L.append(s|(t2<<7))
   for t in(s+d-1,s+d+1):
    if t&0x88:continue
    c=B[t]
    if(c and abs(c)!=6 and(c>0)!=w)or t==EP:
     if r==(6 if p>0 else 1):
      for pr in(5,4,3,2):L.append(s|(t<<7)|(pr<<14))
     else:L.append(s|(t<<7))
  elif a==2 or a==6:
   for o in(-33,-31,-18,-14,14,18,31,33) if a==2 else(-17,-16,-15,-1,1,15,16,17):
    t=s+o
    if t&0x88:continue
    c=B[t]
    if not c:
     if not q:L.append(s|(t<<7))
    elif abs(c)!=6 and(c>0)!=w:L.append(s|(t<<7))
  else:
   for d in((-17,-15,15,17) if a==3 else(-16,-1,1,16) if a==4 else(-17,-16,-15,-1,1,15,16,17)):
    t=s+d
    while not t&0x88:
     c=B[t]
     if not c:
      if not q:L.append(s|(t<<7))
     else:
      if abs(c)!=6 and(c>0)!=w:L.append(s|(t<<7))
      break
     t+=d
 if not q:
  if w:
   if B[4]==6 and C&1 and not B[5] and not B[6] and B[7]==4 and not A(4,0) and not A(5,0) and not A(6,0):L.append(4|(6<<7))
   if B[4]==6 and C&2 and not B[3] and not B[2] and not B[1] and B[0]==4 and not A(4,0) and not A(3,0) and not A(2,0):L.append(4|(2<<7))
  else:
   if B[116]==-6 and C&4 and not B[117] and not B[118] and B[119]==-4 and not A(116,1) and not A(117,1) and not A(118,1):L.append(116|(118<<7))
   if B[116]==-6 and C&8 and not B[115] and not B[114] and not B[113] and B[112]==-4 and not A(116,1) and not A(115,1) and not A(114,1):L.append(116|(114<<7))
 return L
def pi(x):return abs(x)-1+(0 if x>0 else 6)
def mk(m):
 global w,C,EP,HM,S,H,ZH
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7
 p=B[f];a=abs(p);cs=t;c=B[t]
 if a==1 and t==EP and not c:
  cs=t-16 if p>0 else t+16;c=B[cs]
 np=pr*(1 if p>0 else-1) if pr else p
 U.append((m,c,cs,C,EP,HM,S,H,BP[0],BP[1],ZH))
 ZH^=Z[pi(p)][f]
 if pr:ZH^=Z[pi(np)][t]
 else:ZH^=Z[pi(p)][t]
 if c:ZH^=Z[pi(c)][cs]
 S-=W(p,f);S+=W(np,t)
 if c:S-=W(c,cs)
 if a!=1 and pr:H+=V[pr]-100
 if c and abs(c)!=1:H-=V[abs(c)]
 if c and abs(c)==3:BP[0 if c>0 else 1]-=1
 if pr==3:BP[0 if p>0 else 1]+=1
 if a==6:K[0 if p>0 else 1]=t
 HM=0 if a==1 or c else HM+1
 nC=C
 if a==6:nC&=~(3 if p>0 else 12)
 if a==4:nC&=~CB.get(f,0)
 if c and abs(c)==4:nC&=~CB.get(cs,0)
 if nC!=C:ZH^=ZC[C]^ZC[nC];C=nC
 nE=(f+t)//2 if a==1 and abs(t-f)==32 else-1
 if EP!=-1:ZH^=ZE[EP&7]
 if nE!=-1:ZH^=ZE[nE&7]
 EP=nE
 if a==6 and abs(t-f)==2:
  rf,rt=CL[(f,t)]
  rk=B[rf];B[rt]=rk;B[rf]=0
  S-=W(rk,rf);S+=W(rk,rt);ZH^=Z[pi(rk)][rf]^Z[pi(rk)][rt]
 B[f]=0;B[t]=np
 if cs!=t:B[cs]=0
 ZH^=ZS;w=not w
 RP[ZH]=RP.get(ZH,0)+1
def um():
 global w,C,EP,HM,S,H,ZH
 m,c,cs,oc,oep,ohm,os,oh,ob0,ob1,ozh=U.pop()
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7
 p=B[t]
 RP[ZH]-=1
 if pr:B[f]=1 if p>0 else-1
 else:B[f]=p
 B[t]=0
 if c:B[cs]=c
 if abs(p)==6:
  K[0 if p>0 else 1]=f
  if abs(t-f)==2:
   rf,rt=CL[(f,t)]
   B[rf]=B[rt];B[rt]=0
 C,EP,HM,S,H,ZH=oc,oep,ohm,os,oh,ozh
 BP[0],BP[1]=ob0,ob1
 w=not w
def O(ms,tm,pl):
 def k(m):
  if m==tm:return-99999
  c=B[(m>>7)&127]
  if c:return-1000-V[abs(c)]*16+V[abs(B[m&127])]
  if(m>>14)&7:return-900-V[(m>>14)&7]
  if m==KL[pl][0]:return-800
  if m==KL[pl][1]:return-700
  return 0
 return sorted(ms,key=lambda m:(k(m),m))
class X(Exception):pass
def F(d,a,b,pl):
 global w,EP,ZH
 N[0]+=1
 if N[0]>BUD:raise X
 if HM>=100 or RP.get(ZH,0)>1:return 0
 i=ZH&131071
 if TH[i]==ZH and TD[i]>=d:
  s=TS[i]
  if s>M-128:s-=pl
  elif s<-M+128:s+=pl
  fl=TF[i]
  if fl==1:return s
  if fl==2 and s>=b:return s
  if fl==3 and s<=a:return s
  tm=TM[i]
 else:tm=0
 ck=A(K[0] if w else K[1],not w)
 if d<=0:return Q(a,b,pl)
 if d>=3 and not ck and H>900:
  oE=EP;oZ=ZH
  if EP!=-1:ZH^=ZE[EP&7]
  EP=-1;ZH^=ZS;w=not w
  s=-F(d-3,-b,-b+1,pl+1)
  w=not w;EP=oE;ZH=oZ
  if s>=b:return b
 a0=a
 ms=O(G(0),tm,pl)
 bs=-M;bm=0;lg=0
 for m in ms:
  mw=w;c=B[(m>>7)&127];pr=(m>>14)&7;mk(m)
  if A(K[0] if mw else K[1],not mw):um();continue
  lg+=1
  r=1 if lg>3 and d>=3 and not ck and not c and not pr else 0
  s=-F(d-1-r,-b,-a,pl+1)
  if r and s>a:s=-F(d-1,-b,-a,pl+1)
  um()
  if s>bs:bs=s;bm=m
  if s>a:a=s
  if a>=b:
   if not B[(m>>7)&127] and not(m>>14)&7:
    KL[pl][1]=KL[pl][0];KL[pl][0]=m
   break
 if lg==0:return-M+pl if ck else 0
 TH[i]=ZH;TD[i]=d;TM[i]=bm
 TS[i]=bs+pl if bs>M-128 else bs-pl if bs<-M+128 else bs
 TF[i]=3 if bs<=a0 else 2 if bs>=b else 1
 return bs
def Q(a,b,pl):
 N[0]+=1
 if N[0]>BUD:raise X
 if HM>=100 or RP.get(ZH,0)>1:return 0
 st=ev()
 if st>=b:return b
 if st>a:a=st
 ck=A(K[0] if w else K[1],not w)
 ms=O(G(0) if ck else G(1),0,pl)
 lg=0
 for m in ms:
  c=B[(m>>7)&127]
  if not ck and c and st+V[abs(c)]+200<a:continue
  mw=w;mk(m)
  if A(K[0] if mw else K[1],not mw):um();continue
  lg+=1
  s=-Q(-b,-a,pl+1)
  um()
  if s>a:a=s
  if a>=b:break
 if ck and lg==0:return-M+pl
 return a
def RT():
 N[0]=0
 ms=O(G(0),0,0)
 bm=ms[0];d=1
 while d<64:
  try:
   v=-M;b2=bm;a=-M
   for m in ms:
    mw=w;mk(m)
    if A(K[0] if mw else K[1],not mw):um();continue
    s=-F(d-1,-M,-a,1)
    um()
    if s>v:v=s;b2=m
    if s>a:a=s
   bm=b2
   ms.remove(bm);ms.insert(0,bm)
  except X:break
  d+=1
 return bm
def P(p,b):
 q=R.Request(E+p,data=json.dumps(b).encode(),headers={'content-type':'application/json'})
 try:
  with R.urlopen(q)as r:return json.load(r)
 except Exception:return{}
def uc(m):
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7
 return'abcdefgh'[f&7]+str((f>>4)+1)+'abcdefgh'[t&7]+str((t>>4)+1)+('' if not pr else'nbrq'[pr-2])
def mu(u):
 return(ord(u[0])-97)+(int(u[1])-1)*16|(((ord(u[2])-97)+(int(u[3])-1)*16)<<7)|(({'q':5,'r':4,'b':3,'n':2}.get(u[4:5],0))<<14)
def setup(fen):
 global B,w,C,EP,HM,S,H,K,BP,ZH,U,RP
 B=[0]*128;U=[];RP={};S=0;H=0;BP=[0,0];ZH=0
 z=fen.split()
 for r,row in enumerate(z[0].split('/')):
  s=(7-r)*16;f=0
  for ch in row:
   if ch.isdigit():f+=int(ch)
   else:
    i='PNBRQKpnbrqk'.index(ch);x=i+1 if i<6 else 5-i;B[s+f]=x
    S+=W(x,s+f)
    if abs(x)!=1:H+=V[abs(x)]
    if abs(x)==3:BP[0 if x>0 else 1]+=1
    if abs(x)==6:K[0 if x>0 else 1]=s+f
    ZH^=Z[pi(x)][s+f]
    f+=1
 w=z[1]=='w'
 C=0
 if z[2]!='-':
  for ch in z[2]:C|={'K':1,'Q':2,'k':4,'q':8}[ch]
 ZH^=ZC[C]
 if z[3]!='-':
  EP=(ord(z[3][0])-97)+(int(z[3][1])-1)*16
  ZH^=ZE[EP&7]
 else:EP=-1
 HM=int(z[4]) if len(z)>4 else 0
 if not w:ZH^=ZS
 RP[ZH]=1
def choose(g):
 setup(g['start_fen'])
 for u in g['moves']:mk(mu(u))
 try:m=RT()
 except Exception:m=None
 if m is not None and uc(m) in g['legal_moves']:return uc(m)
 return max(g['legal_moves'],key=lambda u:V[abs(B[(ord(u[2])-97)+(int(u[3])-1)*16])]+(V[{'q':5,'r':4,'b':3,'n':2}[u[4]]]-100 if len(u)==5 else 0))
if __name__=='__main__':
 while True:
  g=P('/game',{})
  if g.get('status')=='done':break
  while g.get('status')=='your_move':
   mv=choose(g)
   g=P('/move',{'game':g['game'],'move':mv})
   if not g:break
