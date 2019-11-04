

d1 >> play("|x(13)| V... ")

t1 >> play("V...",dur =1,room=1, mix=2, amp=linvar([0.1,10],1))


t1 >> play("V....+....o",dur =1,room=1, mix=2, amp=linvar([1,10],2)).sometimes("offadd", 4) + var([0,2],4)

LL= P[-50]
e2 >> pulse((LL),room=1,amp=0.5)

LL = P[degree_sequence1]
e3 >> pulse((LL),room=1,amp=linvar([0.1,0.5],1))

e3 >> noise([-3]).sometimes("offadd", 4) + var([0,2],4)

p1 >> donk([0, -1, -5], amp=1.6)
t1.stop()


p1 >> space([0, 2, 5], decay=0.35)

LL= P[-50]
e2 >> pulse((LL),room=1,amp=0.5)



d1 >> play("|x(13)| V... ")

t1 >> play("V.......",dur =1,room=1, mix=2, amp=linvar([0.1,10],1))












