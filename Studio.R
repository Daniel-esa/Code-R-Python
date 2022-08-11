# Correction TP1 : R learning by doing : Objets et manipulation de donnees sous R
## Les Objets : 2.1 Manipulation de vecteurs
### Operation sur les vecteurs
x = c(4,3,6,1,3.2,-5)
x
x[1]
x[5]
d = x[c(3,4,5)]
d= x[3:5]
x*2
sum(x)
prod(x)
dim(x)
x[1]=5
x[6]=4
tx=t(x)
tx
bool<-(x==4)
bool
text<-c("education", "age","sexe")
text
ls()
rm(d)
rm(list=ls())

### Utilisation des fonctions seq rep et c
rep(c(0,6),3)
seq(1,10,3)
rep(1:3, 2)
rep(1:3, 1:3)
rep(1:3, seq(3,1,-1))
rep(1:3, 3:1)
c(rep(1,4), rep(2,2), rep(1:3,2),rep(3,3))
seq(1,2,0.1)
rep(-2:2,2)
rep(-2:0,rep(2,3))

## 2.2 Manipulation de matrices
#1-
(M= matrix(c(1,3,6,2,7,2,2,1,4,5,1,3,8,3,8,6),nrow=4, ncol=4,byrow=TRUE))
M
#2-
dim(M)
ncol(M)
nrow(M)
length(M)
#3-
(A=M[,1])
(B=M[4,])
# 4-
(C=M[,c(1,3)])
# 5-
(D=M[3:4,])
# 6-
M[3,2]
M[4,1]
# 
(tM=t(M))
(dM=diag(M))
#
(S=M+tM)
(P=M%*%tM)
#
(K=M[2:4,2:4])
#
(cbind(M,c(1,9,0,2)))
(Mr=rbind(c(2,3,1,6),M))
#
help(apply)
(sc=apply(M,2,sum))
(pc=apply(M,2,prod))
(mc=apply(M,2,mean))

(sl=apply(M,1,sum))
(pl=apply(M,1,prod))
(ml=apply(M,1,mean))


#### Manipulation de Listes
S= c("H","F", "H", rep("F",3),"H",rep("F",2),"H")
P= c(59,77,76,51,69,75,53,96,77,57)
Tl=c(162,170,199,162,198,178,175,177,183,191)
L=list(Sexe=S, Poids=P, Taille=Tl)
Prenom=c("Leo", "Lucy", "Theo", "Marie", "Lan", "Tran", "Kali", "Louise", "Lala", "Idy")
L[[1]]=Prenom
names(L)[1]="Prenom"
L
IMC= L$Poids/L$Taille^2
L$Poids = IMC
names(L)[2]="IMC"
L=L[-3]
L

#####Manipulation de data frame

(T=data.frame(Sexe=S, Poids=P, Taille=Tl))

attach(T) ## 
Sexe
mode(Sexe)
IMC= Poids/Taille^2
IMC

T[,1]=Prenom
T
names(T)[1]="Prenom"
T=T[,-3]
T
######
Mexp=matrix(rexp(70,0.2),nrow=10,ncol=7,byrow=TRUE)
Mexp
apply(Mexp,2,sum)
apply(Mexp,2,mean)
max(Mexp[1:3,1:3])
v1=rnorm(20,70,sqrt(10))
v2=rnorm(20,25,sqrt(4))
v3=runif(20,0,5)
v3=as.integer(v3)
?as.integer
data=data.frame(poids=v1, age=v2, douleur=v3)
attach(data)
mean(poids)
mean(age)
########
nf= 312
nh= 257
Tf=rnorm(nf,165,sqrt(6))
Th=rnorm(nh,175,sqrt(7))
Pf=rnorm(nf,60,sqrt(2))
Ph=rnorm(nh,75,sqrt(4))
Taille=c(Tf,Th)
Poids=c(Pf,Ph)
Sexe=as.factor(c(rep("F",nf),rep("H",nh)))
dat=data.frame(Taille= Taille, Poids=Poids, Sexe=Sexe, row.names=NULL)
attach(dat)
by(Poids,Sexe,min)
by(Poids,Sexe,which.min)
by(Poids,Sexe,summary)

tapply(Poids,Sexe,min)
sapply(Poids,Sexe,min)
##############














###################
dtext=read.table("donnees/dataset.txt", header=TRUE)
dtext
ddat=read.table("donnees/dataset.dat", header=TRUE)
dcsv=read.csv("donnees/dataset.csv",   header=TRUE)
############# 
library("foreign")
ddta=read.dta("donnees/dataset.dta")
dspss=read.spss("donnees/dataset.sav")

attach(dtext)
score=dtext[,c(1,2,7:11)]
score2=dtext[,c("id","female","read","write","math", "science", "socst")]
write.table(score, file="scoreHF.txt",sep=",")
