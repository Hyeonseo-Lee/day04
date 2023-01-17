#7.11

start1 = ["fee", "fie", "foe"]
rhymes = [
 ("flop", "get a mop"),
 ("fope", "turn the rope"),
 ("fa", "get your ma"),
 ("fudge", "call the judge"),
 ("fat", "pet the cat"),
 ("fog", "walk the dog"),
 ("fun", "say we're done"),
 ]

start2 = "Someone better"


start1 = '! '.join(start1)
start1 = start1 + '!'
start2 = start2 + ' '
for number in range(7):
    rhymes1 = rhymes[number][0]
    answer1 = start1 + ' ' + rhymes1 + '!'
    answer1 = answer1.title()
    #print(rhymes1)
    #print(start1)
    print(answer1)
    new_rhymes = rhymes[number][1]
    new_rhymes = start2 + new_rhymes
    print(new_rhymes)









