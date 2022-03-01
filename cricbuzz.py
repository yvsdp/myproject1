import random
class Player:

    def __init__(self, name, team, role):
        self.name = name
        self.team = team
        self.role = role
batsmanindex = 2
bowlerindex = 1
     
def play():
    
    ##to start the play, we need two batsmen and one bowler.
    ##Choose two batsmen from batting side and one bowler from bowling side.
    
    b1, b2 = chooseOpeningBatsmen()
    
    
    b1.ballsfaced = 0
    b1.score = 0
    
    b2.ballsfaced = 0
    b2.score = 0
    
    
    bw1 = chooseBowler()   
    bw1.ballsbowled = 0
    bw1.runsgiven = 0
    w = 0
    overs = 0
    total_score = 0

    print("The opening batsmen are", b1.name, b2.name)
    
    ###The bowler needs to bowl an over with 6 balls
    for i in range(1,11 ):
        for j in range (1,8):
            if j == 7:
                print("the bowler completed bowling an over: ",bw1.name)
                overs += 1
                print("the team total score is {} and {} wickets down in overs {} :".format(total_score,w,overs))
                bw1 = changeBowler()
                print("the new bowler from pv end",bw1.name)
                global bowlerindex
                bowlerindex += 1
                bw1.ballsbowled += 0
                bw1.runsgiven += 0
            else:
                outcome = random.randint(1,7)
            #global total_score
            #outcome = int(input("enter the value"))
                if outcome == 1:
            ###There is no run. Just increase the ballsfaced and ballsbowled.
                    b1.ballsfaced += 1
                    bw1.ballsbowled += 1
            
                elif outcome == 2:
            ###single run taken by batsman and increase the score, ballsfaced & ballsbowled.
                    b1.ballsfaced += 1
                    b1, b2, bw1 = takeASingle(b1, b2, bw1, 1)
                    bw1.ballsbowled += 1
                #global total_score
                    total_score += 1
        
                elif outcome == 3:
            ###2 runs taken by batsman and increase the score, ballsfaced & ballsbowled.
                    b1.ballsfaced += 1
                    b1, b2, bw1 = takeASingle(b1, b2, bw1, 2)
                    bw1.ballsbowled += 1
                #global total_score
                    total_score += 2        
        
                elif outcome == 4:
            ###3 runs taken by batsman and increase the score, ballsfaced & ballsbowled.
                    b1.ballsfaced += 1
                    b1, b2, bw1 = takeASingle(b1, b2, bw1, 3)
                    bw1.ballsbowled += 1
                #global total_score
                    total_score += 3
        
        
                elif outcome == 5:
            ###4 runs hit by batsman and increase the score, ballsfaced & ballsbowled.
                    b1.ballsfaced += 1
                    b1, b2, bw1 = takeASingle(b1, b2, bw1, 4)
                    bw1.ballsbowled += 1
                #global total_score
                    total_score += 4
        
    
                elif outcome == 6:
            ###6 runs hit by batsman and increase the score, ballsfaced & ballsbowled.
                    b1.ballsfaced += 1
                    b1, b2, bw1 = takeASingle(b1, b2, bw1, 6)
                    bw1.ballsbowled += 1
                #global total_score
                    total_score += 6
        

                elif outcome == 7:
            ###batsman out and we need new batsman, increase the ballsfaced & ballsbowled.
                    print("The batsman {} is bowled by {}".format(b1.name, bw1.name))
                    w += 1
                    print("the team total score is {} and {} wickets down in overs {} :".format(total_score,w,overs))
                    b1.ballsfaced += 1
                    b1 = chooseBatsmanInTheMiddle()
                    print("The new batsman in the middle is: ", b1.name)
                    global batsmanindex
                    batsmanindex += 1
                    bw1.ballsbowled += 1

            print("The batsman {} scored {} runs in {} balls".format(b1.name, b1.score, b1.ballsfaced))
            print("The batsman {} scored {} runs in {} balls".format(b2.name, b2.score, b2.ballsfaced))
        #print("The batsman {} scored {} runs in {} balls".format(b3.name, b3.score, b3.ballsfaced))
            print("The bowler {} gave {} runs in {} balls".format(bw1.name, bw1.runsgiven, bw1.ballsbowled))
        #return b1.name, b2.name, b1.score, b2.score, bw1.name, bw1.ballsbowled, bw1.runsgiven
        #print("the team scored: ",total_score)

India = ['Rohit', 'Rahul', 'Virat', 'Shreyas', 'Pant', 'Jadeja', 'Venky', 'Bhuvi', 'Bumrah', 'Chahal', 'Siraj']
Pak = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11']

def chooseOpeningBatsmen():
    
    b1 = Player(India[0], 'India', 'batsman')
    b2 = Player(India[1], 'India', 'batsman')
    return b1, b2

def chooseBatsmanInTheMiddle():
    newbatsman = Player(India[batsmanindex], 'India', 'batsman')
    newbatsman.score = 0
    newbatsman.ballsfaced = 0
    return newbatsman

def chooseBowler():
    bw1 = Player(Pak[0], 'Pak', 'bowler')
    
    return bw1

def takeASingle(p, q, r, n):
    ###Here b1 takes the single and b2 will get the strike.
    p.score += n
    r.runsgiven +=n
    if(n%2 == 0):
        return p, q, r
    else:
        return q,p,r

def changeBowler():
    newbowler = Player(Pak[bowlerindex], 'pak', 'bowler')
    newbowler.runsgiven = 0
    newbowler.ballsbowled = 0
    return newbowler

play()   