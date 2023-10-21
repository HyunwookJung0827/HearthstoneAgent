# HearthstoneAgent
Prototype of Hearthstone AI that wins over CPU (The Innkeeper) in practice mode (Normal/Expert)

10/21/2023 15:00
I've been thinking of Paladin Expert instead of Mage Normal deck. There are some reasons: First, I could not make the same Mage-Normal Innkeeper's deck because there were some "Legacy" cards such as "Oasis Snapturtle" which means they are not in use in game, and a user cannot use it anymore, only NPC can. Second, after I looked up the deck for mage Expert, I noticed that the Innkeeper's deck of mage expert has some complex mechanics to calculate (i.e. "Discover a random magic"). After playing some games, I could collect all the Paladin cards I needed for the Innkeeper's deck.

##############################################################
Paladin Expert Deck (I made it myself in notepad)

1 Warhorse Trainer x2
2 Truesilver Champion x2
3 Ardor Peacekeeper x2
4 Argent Squire x2
5 Equality x2
6 Guardian of Kings x2
7 Blessing of Kings x2
8 Annoy-o-Tron x2
9 Dire Wolf Alpha x2
10 Righteous Protector x2
11 Consecration x2
12 Argent Protector x2
13 Stand Against Darkness x2
14 Pursuit of Justice x2

15 Taelan Fordring x1
15 Tirion Fordring x1
Ashbringer x1 - The weapon from Tirion Fordring
The Coin x1 - If you are the second turn
Reinforce - Hero ability: Summon a 1/1 Silver Hand Recruit.
##############################################################

Other than the deck, I had some issue implementing YOLOv5 utils.py, so I am following other instructions using "Make Sense" website. https://www.youtube.com/watch?v=GRtgLlwxpc4

10/19/2023 20:00
Succeeded in fixing Yolov5 prototype. It was all about Linux, so I built a new virtual environment in my anaconda.
Will report again if I succeed in implementing it in my main code.

10/6/2023 03:11
Succeeded with Video screening with OBS.
I want a card number recognizer. It sounds hard. I'm thinking about recognizing some blue colors of each card (mana cost is blue) in specific (x, y) position. And having some templates for each number of cards 0 - 10.
Any card content would be considered after I am done with the card number recognizer. Next is Field unit number recognizer I assume.
