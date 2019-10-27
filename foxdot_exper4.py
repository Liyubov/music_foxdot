

Scale.default = Scale.minor

#drums 

d1>> play("x[----]while(=[-o])")
d2 >> play("x[--]o(=[-o])")
d3 >> play("x[---]Or(=[-----o])")

print(SynthDefs)

d1.stop()
d2.stop()
d3.stop()

#songs
p1 >> jbass([0,0,4], dur=[1,2,2], amp=linvar([1,2],10))#[1,3/4,3/4])

p1.stop()

a = var([0, 1, 2, 3], [8, 4, 2, 2])
var.chords = var([0, 10, 15, 3])
s1 >> space(var.chords + (0, 2, 4), dur=4, oct=5)

s1.stop()


p1 >> gong(dur=1, amp=linvar([1,10],5))
p1 >> bell(dur=1, amp=linvar([1,2],1))

p1.stop()


d1 >> play("x[--]while(=[-o])")
d2 >> play("x ", sample =2, dur =3)

b1 >> space(dur=PDur(3,8), sus=2, chop=4, sample=P[:4].rotate([0,1,30]), shape=PWhite(0,1/2), pan=PWhite(-10,10)).sometimes("offadd", 4) + var([0,2],4)

b1 >> star(dur=PDur(1,3), sus=2, chop=4, sample=P[:4].rotate([0,1,10]), shape=PWhite(0,1/2), pan=PWhite(-10,10)).sometimes("offadd", 4) + var([0,2],4)

g1 >> space(1, oct = 5, room =1 , mix =0.5, amp=linvar([1,2],10))

g1.stop()

t1 >> play("xo--x-x",dur =2,room=1, mix=2, amp=linvar([1,2],1))

t2 >> play("V...+..xo-x-xo",dur =2,room=1, mix=2, amp=linvar([1,2],2))

t1 >> play("....",dur =1,room=1, mix=2, amp=linvar([0.1,1],1))

LL = P[1,20]

e2 >> pulse((LL),room=1,amp=0.1)

e2 >> pulse((LL).reverse()+3,oct=(2,3),room=1,mix =0.4,amp=0.1)

e2 >> pulse((LL).mirror()+3,oct=(2,3),room=1,mix =0.4,amp=linvar([1,2],1))

e2.stop()

Clock.clear()
