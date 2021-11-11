import random

##################################         CARDS CREATION       #################################

cards_symbols = [ '♣', '♦','♥', '♠']                                              
cards_no = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']     

suffle = []                                                                     
for card_symb in cards_symbols:                                                     
  for card_n in cards_no:                                                          
    suffle.append(card_symb + card_n )                                              
cards_1 = ['♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K', '♣A']     
cards_2 = ['♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K', '♦A']        
cards_3 = ['♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K', '♥A']       
cards_4 = ['♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K', '♠A']       

#######################        PLAYER ASSIGNMENT     #############################

players = []                                                                  
for i in range(4):                                                     
  player_name = input('enter ' + str(i + 1) + ' player name : ')           
  players.append(player_name)                                             

###############################     PLAYERS CARD SUFFLING    ###########################

p_1_cards = []                    
p_2_cards = []                    
p_3_cards = []                     
p_4_cards = []                      
                                                              
for i in random.sample( suffle, 52):                                    
  if i not in (p_1_cards) and len(p_1_cards) < 13:
    p_1_cards.append(i)
  elif i not in (p_1_cards) and len(p_2_cards) < 13:
    p_2_cards.append(i)
  elif i not in (p_1_cards and p_2_cards and p_3_cards) and len(p_3_cards) < 13:
    p_3_cards.append(i)
  elif i not in (p_1_cards and p_2_cards and p_3_cards and p_4_cards) and len(p_4_cards) < 13:
    p_4_cards.append(i)

players_cards = [p_1_cards, p_2_cards, p_3_cards, p_4_cards]

#####################      ASSIGNING CARDS TO PLAYERS   ######################

cards_assignment = {}

for i in range (len(players)):
  cards_assignment[players[i]] = players_cards[i]

#######################    CARD CHOOSING   #############################

card_sign = {1 : '♣', 2 : '♦', 3 : '♥', 4 : '♠'} 
card_sign_choose = ''                               
card_no_choose = ""                                
card_choosen = int()                                                                 
indx = 0
a=0
card_point={}
for i in cards_assignment.keys():     
                                      
  print ("\nIt's your turn {}, Please choose a card from your cards : \n{}\n".format(i, cards_assignment[i]))
  card_sign_choose = int(input('Choose a number from your card sign for your cards :\n{}\nEnter a number : '.format(card_sign)))
  card_no_choose = input("Enter card : ").upper()
  if (card_no_choose=="2")or(card_no_choose=="3")or(card_no_choose=="4")or(card_no_choose=="5")or(card_no_choose=="6")or(card_no_choose=="7")or(card_no_choose=="8")or(card_no_choose=="9")or(card_no_choose=="10"):
      card_point[i]=(int(card_no_choose))
  else:
    if card_no_choose=="J":
      card_no_choose=11
      card_point[i]=card_no_choose
      card_no_choose="J"
    elif card_no_choose=="Q":
      card_no_choose=12
      card_point[i]=card_no_choose
      card_no_choose="Q"
    elif card_no_choose=="K":
      card_no_choose=13
      card_point[i]=card_no_choose
      card_no_choose="K"
    elif card_no_choose=="A":
      card_no_choose=14
      card_point[i]=card_no_choose
      card_no_choose="A"
  card_choosen = cards_symbols[card_sign_choose-1] + str(card_no_choose)
  
###############  CHECKING CHOOSEN CARD IN PLAYERS CARD   ########################

  if (a==0 or a==1 or a==2 or a==3):
    C=players_cards[a]
    for j in cards_assignment.values():                 
      if (card_choosen in players_cards[a]):                                                          
        if card_choosen in p_1_cards:                                                               
          indx = p_1_cards.index(card_choosen)                                     
          del p_1_cards[indx]                            
        elif card_choosen in p_2_cards :                                   
          indx = p_2_cards.index(card_choosen)                                    
          del p_2_cards[indx]                                    
        elif card_choosen in p_3_cards:                                                  
          indx = p_3_cards.index(card_choosen)                                 
          del p_3_cards[indx]  
        elif card_choosen in p_4_cards:                                 
          indx = p_4_cards.index(card_choosen)                              
          del p_4_cards[indx]                     
        else:                                                                 
          print("this card is not avilable in the card distribution")                                                                                                              
        break
      else:                                                                  
        print('Sorry, {} Card is not yours!  You lost your Turn...\n\n'.format(card_choosen))                                                        
        break
    a+=1            
ind =sorted(card_point.values())                                                              
win = ind[3]
for r,s in card_point.items():
  if s==win:
    print ("{} WIN because it's point is high:-{}".format(r,s))
  else:
    print("{} your loss because your poient is low:-{}".format(r,s))                                                 