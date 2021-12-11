def zombie_shootout(zombies, distance, ammo):
    # your code goes here
    x=zombies
    y=float(distance)
    z=ammo
    while y != 0:
        if x!= 0:
            if z==0:
                y=0
                return("You shot " + str(zombies-x) +" zombies before being eaten: ran out of ammo.")
                continue
            elif x==0:
                y=0
                return("You shot all "+str(zombies)+" zombies.")
                continue
            else:
                y-=0.5
                z-=1
                x-=1
                if x==0:
                    y=0
                    return("You shot all "+str(zombies)+" zombies.")
                    continue
        else:
            y-=0.5
            z-=1
            x-=1 
    return("You shot "+str(zombies-x)+" zombies before being eaten: overwhelmed.")
