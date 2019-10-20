#Synchronisation of the group

#Clock.connect('192.168.1.30')

#simple drums 
d1 >> play("x[-------]while(=[-o])")

d2 >> play("x[--]o(=[-o])")

d3 >> play("x[----]Or(=[-o])")

d3 >> play("x[--o-]Or(=[-o])")

d3.stop()

d1.stop()

d2.stop()

# Drums session 

# Plays the kick drum with sample 2 but the rest with sample 0
d1 >> play("|x2|-o-")
d1.stop()

# You can use square brackets to play multiple samples
d1 >> play("|x[12]| o ")

# Round brackets alternate which sample is used on each loop through the sequence
p1 >> play("|x(13)| oooo ")
p1.stop()

# Curly braces will pick a sample at random
p1 >> play("|x{0123}| o ")


# Pentatonic

p1 >> pluck(PRange(5) | PRange(5,0,-1), scale=Scale.default.pentatonic)

p1.stop()

p2 >> pluck(PRange(13) | PRange(13,0,-1), scale=Scale.default.pentatonic)

p2.stop()

p1 >> pluck(PTri(15), scale=Scale.default.pentatonic)
p1 >> pluck(PTree)
p1.stop()

# Variables in Time 

p1 >> pluck([0, 1, 4] + var([0, 4]), dur=PDur(3,8) * var([1, 2], 8))



