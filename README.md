# HearthstoneAgent
Prototype of Hearthstone AI that wins over CPU (The Innkeeper) in practice mode (Normal/Expert)

Task: Card detection -|Here|- Status Analyzation - Command - Notable Win Rate vs Expert CPU

![](https://geps.dev/progress/30)



11/02/2023 14:00
Finally, I got a remarkable trained model. Somehow local training doesn't pick up the models higher than Yolov5s.pt (or .yaml) making the precision score at absolute zero. And using yolov5s.yaml only gave me about 15% successful detection. After some experiments on batch size and epoch numbers, I felt like it would be very challenging to train without a more complex model, so I decided to implement the train into Google Colab and it worked (97.7% successful card detection rate). 
![image](https://github.com/HyunwookJung0827/HearthstoneAgent/assets/90017772/4489d3f8-bf74-4581-9985-a1b65285b06d)

![image](https://github.com/HyunwookJung0827/HearthstoneAgent/assets/90017772/bd9c8496-097e-49ca-8bcc-fefe7e967545)


11/01/2023 11:00
Still having a hard time training a credible model.pt using train.py of Yolov5. I've tried a monitor screening with a model.pt I made for the first time, and it was not detecting any cards in the screen. I found that the metrics/precision stayed under 0.020 in results.png. I suspect that the precision of recognizing each card(excluding minions on the field) is very poor because I used the screenshots that has minions on the field (which of course use the same portrait) thus many false-positive cases appeared during the training. Plus I replaced any golden cards to normal cards for sustainability.

![image](https://github.com/HyunwookJung0827/HearthstoneAgent/assets/90017772/41558d16-45f9-42b0-a2ac-5d34b694ba5b)


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
