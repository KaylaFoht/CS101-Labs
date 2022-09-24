########################################################################
##
## CS 101 Lab
## Program # 4
## Name Kayla Foht
## Email kkfzbf@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed


def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    valid_input = False
    while True: #validates that the user entered yes or no
        again = input('Do you want to play again?\n')
        m_again = again.upper()
        if m_again not in ('Y', 'YES', 'N', 'NO'):
            print('You must enter Y/YES/N/NO to continue. Please try again')
            continue
        else:
            break
    while valid_input == False: #outputs True or False to the main
            if m_again == 'N' or m_again == 'NO':
                valid_input = True
                end = False
                return False
        
            elif m_again == 'Y' or m_again == 'YES':
                valid_input = True
                end = True
                return True
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    while True:
        wager = int(input('How many chips do you want to wager? ==> '))
        if wager < 1: #ensures the entered amoutn is creater than 1
            print('The wager amount must be greater than 0. Please enter again.')
        elif wager > bank: #ensures the value entered does not exceed the amount in the bank
            print(f'The wager amount cannot be greater than how much you have. {bank}')
            continue
        else:
            break
    return wager           

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    import random #rolls three random numbers and retruns them
    num1 = random.randint(1,3)
    num2 = random.randint(1,3)
    num3 = random.randint(1,3)
    return num1, num2, num3

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    count = 0
    if (reela == reelb and reela == reelc): #returns 3 if three matches
        count = 3
    elif (reela == reelb) or (reela == reelc) or (reelc == reelb): #returns 2 if one match
        count = 2
    else: #returns 0 if no matches
        count = 0
    return count

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    while True:
        in_bank = int(input('How many chips do you want to start with? ==> ')) #lets the user choose the amount of money they want to start with 
        if in_bank < 1: #makes sure the user puts more than 1 in their bank
            print('Too low a value, you can only choose 1 - 100 chips')
            continue
        elif in_bank > 101: #makes sure the user puts less than 101 in their bank
            print('Too high a value, you can only choose 1 - 100 chips')
            continue
        else:
            break
    return in_bank

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    payout = 0
    if matches == 3: #output if the user had three matches
        payout = wager * 10
        win_loss = payout + wager
    elif matches == 2: #two matches
        payout == wager * 3
        win_loss = payout + wager
    else: #no matches
        return (wager*-1)
    return payout + wager     


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank() #user inputs amount in bank
        original = bank #this will keep track of how much was originally in the bank
        bankmax = bank #used later for telling the user their maximum amount of money
        count = 0 #used to count the number of plays the user does
        while bank > 0:
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout


            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()

            count += 1 #adds to count for each pull
            while bankmax < bank: #keeps track of the largest amount the user has in thier bank
                bankmax = bank
           
        print("You lost all", original, "in", count, "spins") #tells the user how much they originally had and how many turns it took to lose
        print("The most chips you had was", bankmax) #tells the user the maximum amount of money they had
        end = play_again() #has the user choose if they want to play again or not
        if end == False: #this if else statement helps close the while loop that runs the game.
            playing = False
        else:
            playing = True
        
