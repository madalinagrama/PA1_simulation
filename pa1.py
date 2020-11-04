import sys as sys # nu se foloseste in cod

w , z  = [], [] # 2 liste goale
f = [['you',3.13,'can','be','anything',False,'you','want','to','be','\n',
'just turn', 'yourself', 'into', 'anything','you','think','that',
'you','could', 'ever','be',True]] # lista in lista

w.append(f[0][0])
w8 = f[0][8]
w9 = f[0][9]
x2 = f[0][2] + " " + f[0][3]
w.append(x2)
w6,w4 = f[0][4], f[0][6]
w7 = f[0][7]
w.append(w6)
w.append(w4)
w.append(w7)
w.append(w8)
w10 = f[0][10]
w.append(w9)
w.append(w10)
w16,w12,w13 = f[0][16],f[0][12],f[0][13]
w14,t15,w11 = f[0][14],f[0][15],f[0][11]
w17,w18 = f[0][17],f[0][18]
w.append(w11)
w.append(w12)
w.append(w13)
w.append(w14)
w.append(t15)
w.append(w16)
w.append(w17)
w.append(w18)
w.append(f[0][19])
_w1 = f[0][20]
_w9 = f[0][21]
w.append(_w1)
w.append(_w9)
x = ''

for __t in w:
    x = x + __t + ' '

print(x)
