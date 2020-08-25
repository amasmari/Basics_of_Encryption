#Helper Functions
def LongDivision(a,b):
    if b>a:
        a,b=b,a
    r=a%b
    q=(a-r)%b
    return q,r
#print(LongDivision(37,16))
#print(LongDivision(85354354693,927256))
def Fgcd(a,b):
    if a>b:# the algorithm works when b>a, so this is a make it woeks at a>b.
        a,b=b,a # I learned Multiple assignments in python from https://stackoverflow.com/questions/52467743/multiple-assignments-in-python
    if a ==0:
        return b
    elif a==b:
        return b
    while b>0:
        b,a=a%b,b
    return a
    if 1:
        return 0 # I used zero as an error output.


def UVgcd(a,b):
    if a>b:
        a,b=b,a
    u,g,x,y=1,a,0,b
    while y>0:
        t=g%y
        q=g//y
        s=u-q*x
        u,g=x,y
        x,y=s,t
    v=(g-a*u)//b
    return int(u),int(v),g


def Finverse(a,N):
    A=UVgcd(a,N)
    if A[2]==1:
        d=A[0]
        while d<0:
            d=d+N # to make sure I get a postive integer
        return d
    else:
        return 0 #Here I also used zero as an error output.
    

def FastP(g,A,N):
    a,b=g,1
    while A>0:
        if A%2==1:
            b=(b*a)%N
        a,A=(a*a)%N,(A-A%2)//2
    return b


#Deffie-Hellman
def KeyExchange(a,g,p):
    c=FastP(g,a,p)
    return c


def SharedSecret(a,B,p):
    s=FastP(B,a,p)
    return s


#ElGamal
def GPkeyEG(a,g,p):#genertar a public key for ElGamal system
    A=FastP(g,a,p)
    return A


import random # I needed random for generating a k for the ciper
def EGEncrypt(m,A,g,p):#make the cipjer with ElGamal system
    k=random.randint(2,p-2)# 1 and -1 are not good options because they are easy to spot
    c2=FastP(g,k,p)
    S=FastP(A,k,p)
    c1=(m*S)%p
    return c1,c2


def EGDecrypt(a,c1,c2,p):#ElGamal Decryption
    A=FastP(c2,a,p)
    AA=Finverse(A,p)
    M=(c1*AA)%p
    return M
def EGDecrypt2(a,C,p):#ElGamal Decryption when the C is an array
    c1=C[0]
    c2=C[1]
    A=FastP(c2,a,p)
    AA=Finverse(A,p)
    M=(c1*AA)%p
    return M

#RSA
def RSAPublicK(P,Q): #creating the public key for RSA system
    a=(P-1)*(Q-1)
    N=P*Q
    e=random.randint(2,a//2)
    while Fgcd(a,e)!=1:
        e=random.randint(2,a//2)
    while e>a:
        e= e-aR
    return N,e

    
def RSADExponent(P,Q,e): #findeing the decryption exponent
    A=(P-1)*(Q-1)
    d= Finverse(e,A)
    return d


def RSAEn(m,e,N): #creating the encryption function for RSA, used RSAEN to make at least short name wise.
    c= FastP(m,e,N) #I think FastP is enough, but RSAEn is resier to write :)
    return c


def RSADe(c,d,N): # Also a short name for convinece
    m=FastP(c,d,N)
    return m
def StoIn(W):
    n=0
    i=0
    for l in W:
        n += (2**(8*i))*ord(l)
        i += 1
    return n
def IntoS(N):
    l=""
    while N !=0:
        n=N%256
        N=(N-n)//256
        l += (chr(n))
    return l

p = 202291242366393541597121485482595402493431736217769136808391
g = 6

#Ali RSA p and q
P=92277265383869935592223696528029165318485808887801975032481813556222501469174956326803647734470230078128339396902211832242695256153153983990517853483943913696391192509045325983186992040554695769485753497822095929541227564193272435576627707266225664768292696507364773674735409172771253294233293993427487277888472717933447774351384323432677710237877124182321068115017749114487623456127742224674782186445097733663540605774682449177529088528994614143789529109110432714124927544367869064624284991671516083794488516290827373975862355381628318399086239384520793531869948491875213104234953103937761587101422190173150678686603555532361645188159990058993794603928742380739398395672733317693765353384879741966725126672300846930171983941697333105925175083571245810479008653904003854005930827406763716103621336427
Q=402949773087429451973958465063144884436375106977188621912920638344586630832385095026304252336309645233107662860673649359940059076253881848113354116886542621578060396218476644737460284056189364152234848131145139597214941860805684197087922640241070991822938224233108435570933281303197893142751359243136725469653490528631690873854829027229399243446321953570027464907455565219796678607241376919360593281658924022324027851713546100829915826616781582589098530894836768397938300818805065998760197562166333914590263754861683666866553439532356301518002861069751868208636869946451365817937286705110482754237486901676952325119189094339601509099828202122265609114251130529321202038524174907336393840681594111452403805673039328447343971256002546837106079997466683


