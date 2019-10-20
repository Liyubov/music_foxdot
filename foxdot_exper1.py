
#############################################
Scale.default="minor"
c1 >> play(" oooo#  oo W ", dur=10, sample=P[:4].rotate([0,1,30]),cutoff = linvar([1,200],10), rate=100, pan=-0.5, amp=linvar([1,100],20))
g1 >> gong([0,2,3,4,5,5], amp=20, chop = var[2,2,3,4,5,5]) #drive = var([0.1,0.2])
#g1.stop()


c2 >> play("   oo ", dur=40, room=10, amp=30, pan=0.5)
d1 >> play("")
b1 >> dbass(dur=PDur(3,8), sus=2, chop=4, shape=PWhite(0,1/2), pan=PWhite(-10,10)).sometimes("offadd", 4) + var([0,2],4)

c2.stop()
d1.stop()
b1.stop()

d1 >> play("@ # oo", dur=1/4, sample=P[:8].rotate([0,1,2]), rate=4, pan=-0.5, amp= linvar([1,200],10))
d2 >> play("1 ", dur=40, room=1, amp=2, pan=0.5)