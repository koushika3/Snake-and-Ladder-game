import random
k=0
ps={}

n=int(input("Enter the number of players:"))
for i in range(n):
    ps[i]=0
LAD={3:22,11:26,20:29,5:8}
SNA={21:9,17:4,19:7}
while(sum(ps.values())!=n*30):
    k+=1
    for i in range (n):
        if(ps[i]!=30):
            j=(input("\nPlayer {}: Press r to roll the die\n\n".format(i+1)))
            if((j).lower()=='r'):
                
                p=(random.randint(1,6))
                print("\nYou got a {} !\n".format(p))
                if(k!=1):
                    ps[i]+=p
                else:
                    ps[i]=p

                if( ps[i] in LAD.keys()):
                    for k in LAD.keys():
                        if(ps[i]==k):
                            ps[i]=LAD[k]
                            print("Yay you got a ladder :D\n")
                            break

                elif( ps[i] in SNA.keys()):
                    for k in SNA.keys():
                        if(ps[i]==k):
                            ps[i]=SNA[k]
                            print("Oh no :/, got bit by a snake !\n")
                            break

                if(ps[i])>30:
                    print("Better luck next time :3\n ")
                    ps[i]=ps[i]-p
                
                
                print("Your current position is: ",ps[i],"\n")

                
                if(ps[i]==30):
                    print("Congrats player {}! You reached 30 !! You won !!!\n".format(i+1))
                    
                p=0

            else:
                print("Your turn will come in the next round\n") 
                
        else:
            continue
