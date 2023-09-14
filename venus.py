import math as m
def COMPACT(Y:float,X:float):
    Y=X*(Y/X-m.floor(Y/X))
    if(int(X)==360 and Y<0):
        Y=Y+360.0
    return Y
Y=int(input("年"))
M=int(input("月"))
D=int(input("日"))
H=int(input("時"))
LAT=float(input("緯度"))
LON=float(input("経度"))
if M<3:
    Y=Y-1
    M=M+12
S=int(365.25*Y)+int(30.59*(M-2))
JD=S+D+H/24+-LON/360+1721086.5
T=2299161
if JD>T:
    A=int(Y/400)-int(Y/100)+2
    JD=JD+A
C=float((JD-2415021)/36525)
P=m.pi/180
#SML:太陽の平均黄経
SML=280.6824+36000.769325*C+7.22222E-4*C*C
SML=COMPACT(SML,360)
#SEC:軌道離心率
SEC=0.0167498-4.258E-5*C-1.373E-7*C*C
#SPL:近日点黄経
SPL=281.2206+1.717697*C+4.83333e-4*C*C+2.77777e-6*C*C*C
SPL=COMPACT(SPL,360)
#SMA:平均近点角
SMA=(SML-SPL)*P
#SMPG:太陽の中心差
SMPG=1.91946*m.sin(SMA)+2.00939E-2*m.sin(2*SMA)-4.78889E-3*m.sin(SMA)*C-1.44444E-5*m.sin(SMA)*C*C
#SL:真太陽の黄経
SL=SML+SMPG
#SAX:軌道半長径
SAX=1.00000129
#STA:真近点角
STA=SL-SPL
#SRR:動径
SRR=SAX*(1-SEC*SEC)/(1+SEC*m.cos(STA*P))
#SS:視半径
SS=0.2666/SRR
#太陽の座標
SX=SRR*m.cos(SL*P)
SY=SRR*m.sin(SL*P)
SZ=0
AX=0.72333015
ML=344.36936+58519.2126*C+9.8055E-4*C*C
ML=COMPACT(ML,360)
PNL=130.14057+1.3723*C-1.6472E-3*C*C
MA=ML-PNL
MA=COMPACT(MA,360)
if MA<0:
    MA=MA+3

OMG=75.7881+0.91403*C+4.189E-4*C*C
INC=3.3936+1.2522E-03*C-4.333E-6*C*C
EC=6.81636E-3-5.384E-5*C+1.26E-7*C*C
MPG=(2*EC-EC*EC*EC/4)*m.sin(MA*P)+5/4*EC*EC*m.sin(2*MA*P)+13/12*EC*EC*EC*m.sin(3*MA*P)
TA=MA+MPG
UU=TA+PNL-OMG
AA=m.cos(INC*P)*m.tan(UU*P)
CC=m.atan(AA)/P
if UU>90 and UU<270:
    CC=CC+180
if UU>270:
    CC=CC+360
LL=CC+OMG
if LL>360:
    LL=LL-360
BB=m.tan(INC*P)*m.sin(CC*P)
TB=m.atan(BB)/P
RR=AX*(1-EC*EC)/(1+EC*m.cos(TA*P))
XX=RR*(m.cos(UU*P)*m.cos(OMG*P)-m.sin(UU*P)*m.sin(OMG*P)*m.cos(INC*P))
YY=RR*(m.cos(UU*P)*m.sin(OMG*P)+m.sin(UU*P)*m.cos(OMG*P)*m.cos(INC*P))
ZZ=RR*m.sin(UU*P)*m.sin(INC*P)
TT=m.sqrt(XX*XX+YY*YY+ZZ*ZZ)
EX=XX+SX
EY=YY+SY
EZ=ZZ+SZ
DD=m.sqrt(EX*EX+EY*EY+EZ*EZ)
LAM=m.atan(EY/EX)/P
SS=EZ/DD
BET=m.atan(SS/m.sqrt(1-SS*SS))/P
if EX<0:
    LAM=LAM+180
if LAM<0:
    LAM=LAM+360
print(LAM,BET)