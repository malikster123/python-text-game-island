# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

player_input = input('''
          <|
           A             
          /.\       
     <|  [""M#      
      A   | #              
     /.\ [""M#             
    [""M# | #  U"U#U                 
     | #  | #  \ .:/    
     | #  | #___| #     
     | "--'     .-"     
   |"-"-"-"-"-#-#-##    
   |     # ## ######     
    \       .::::'/     
     \      ::::'/      
   :8a|    # # ##      
   ::88a      ###       
  ::::888a  8a ##::.    
  ::::::888a88a[]::::
 :::::::::SUNDOGa8a::::. ..              
 :::::8::::888:Y8888:::::::::...      
::':::88::::888::Y88a______________________________________________________
:: ::::88a::::88a:Y88a                                  __---__-- __
' .: ::Y88a:::::8a:Y88a                            __----_-- -------_-__
  :' ::::8P::::::::::88aa.                   _ _- --  --_ --- __  --- __--
.::  :::::::::::::::::::Y88as88a...s88aa.

You have been walking endlessly for days, you do not remember you why you are on this journey, 
or what you are seeking for but feel compelled to see this to the end......

There is and end to this journey, you dont know what it is but something deep within tells you it exists...... 

whether it is a treasure or eternal happiness you do not know......

but it drives you forwards........

In the distance you see a castle, it is a tall intimidating structure, you can feel the aura from a distance, it invokes fear and at the same time intrigues you...

You see a path ahead, it looks rather long and strenuous but to your left to see a wooden booth with a sign that reads "FREE TELEPORTATION TO CASTLE".

     _.------._
 _.-'          '-._
/                  \
'------------------'
| .--------------. |
| |      ||      | |
|[]      ||      | |
| |======||======| |
| |      ||      | |
| |      ||      | |
|[]======||======[ |
| |======||======| |
| |      ||      | |
| |      ||      | |
|[]======||======| |
| |      ||      | |
| '------''------' |
|__________________| 

Type "go" to follow the strenuous path to castle...
Type "Tele" to use the teleportation device... \n
''')
if player_input == "go":
  player_input2 = input('''_      _      _      _      _      _      _      _
)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_
_     _     _     _     _     _     _     _
)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,
_    _    _    _    _    _    _    _    _
)'-.,)'-.,)'-.,)'-.,)'-.,)'-.,)'-.,)'-.,)'-.,
 _       _      _       _      _      _
( `'-.,_( `'-.,( `'-.,_( `'-._( `'-.,( `'-.,
 _    _     _      _
( '-.( '-.,( '-.,_( `'-.,_  \nan hour into your journey you come across a black river and at the other end of the river you see the entrance the castle. A sign reads 'Do not swim across across the river, it contains ██████████████. patience and it will clear by itself'.... it is only a small distance to swim across... surely nothing that bad can happen?... do you really want to wait? \n Type "wait or swim"...\n''')
  if player_input2 == "wait":
    player_input3 = input('''
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________| \nAs you sit there waiting, you look up the sky to get a reading on what     time it is, you look back down at the black river, it has completely disappeared and a path leading to the entrance has been made clear.... as walk into the castle, you see it is abandoned you start to think about the empire and kingdom this castle housed and what history lies within this caslte... you are preseneted with 3 doors that all have different signs.. the red door reads "wealth and power"...that sounds appealing... the blue door reads "Struggle"... that sounds scary.. and the final door which is yellow says "The End"... which door you pick?\n''')
    if player_input3 == "red":
      print('''      
                                    o
                                   $""$o
                                  $"  $$
                                   $$$$
                                   o "$o
                                  o"  "$
             oo"$$$"  oo$"$ooo   o$    "$    ooo"$oo  $$$"o
o o o o    oo"  o"      "o    $$o$"     o o$""  o$      "$  "oo   o o o o
"$o   ""$$$"   $$         $      "   o   ""    o"         $   "o$$"    o$$
  ""o       o  $          $"       $$$$$       o          $  ooo     o""
     "o   $$$$o $o       o$        $$$$$"       $o        " $$$$   o"
      ""o $$$$o  oo o  o$"         $$$$$"        "o o o o"  "$$$  $
        "" "$"     """""            ""$"            """      """ "
         "oooooooooooooooooooooooooooooooooooooooooooooooooooooo$
          "$$$$"$$$$" $$$$$$$"$$$$$$ " "$$$$$"$$$$$$"  $$$""$$$$
           $$$oo$$$$   $$$$$$o$$$$$$o" $$$$$$$$$$$$$$ o$$$$o$$$"
           $"""""""""""""""""""""""""""""""""""""""""""""""""""$
           $"                                                  o
           $"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$$
         
                      \nyou wake up a 500 years before from now, you are king of the land with enough wealth to buy the freshest garments 1000 horses. however your people facing a drought which causes the crops to not grow. This leads to the economy crashing and greater wealth inequality, which leads to hostility towards your thrown. You try your best to remedy this situation by spreading your own wealth but it is too late, the people have already organised a mob heading right for your castle and even some of your own knights have abandoned their posts... you hear slamming at the castle doors.... the doors cant last that long......''')
    elif player_input3 == "blue":
      print(''' 
                          ,dM
                         dMMP
                        dMMM'
                        \MM/
                        dMMm.
                       dMMP'_\---.
                      _| _  p ;88;`.
                    ,db; p >  ;8P|  `.
                   (``T8b,__,'dP |   |
                   |   `Y8b..dP  ;_  |
                   |    |`T88P_ /  `\;
                   :_.-~|d8P'`Y/    /
                    \_   TP    ;   7`\
         ,,__        >   `._  /'  /   `\_
         `._ """"~~~~------|`\;' ;     ,'
            """~~~-----~~~'\__[|;' _.-'  `\
                    ;--..._     .-'-._     ;
                   /      /`~~"'   ,'`\_ ,/
                  ;_    /'        /    ,/
                  | `~-l         ;    /
                  `\    ;       /\.._|
                    \    \      \     \
                    /`---';      `----'
                   (     /            fsc
                    `---'

you come across a warrior holding a massive sword. He is twice your size and looks like he wants to kill you. The door shuts behind and on the floor next to you lays a sword.... There is only one way forwards and you know what you must do, you have been training for a very long time but have always shied away from competition, you have made constant excuses but now there is no excuse. You must face him head on. You swing your sword and miss and the warrior cuts you. "Next time you die" he says. You realize you are still scared and hesitant, you finally muster the confidence to go in and attack with all your might and finally stab the the warrior directly into his heart. As he bleeds to death the world around begins the crumble and darkness surrounds you. You wake up back at your house and think "Was it all just a dream?" and return back to your normal life but this time with a sense of confidence. up until this point you lived a life of a coward, scared to make any real decisions and avoiding conflicts resulting in your current sitation. "I cannot live this life anymore i will no longer run away from struggle and challanges, i will face them head on regardless of how many times i lose"

''')
    elif player_input3 == "yellow":
      print('''
            _.-""}
      / "" ;
  .-"` __] ',               ___
  I_ ""__.`-,;             |   |
    I_.,-"ii"{             !___!
    | ||  ||  |        ,    | |
    | ||  ||  |       .;    | |
    | ||  ||  |       | \   | |
    | ||  ||  |       |  |  | |
    | ||  ||  |       |  |  | |   __
    | ||  ||  |       |  |  | |  |  |
    | ||  ||  |   ;|  |  |  | |  |  |
    | ||  ||  |"\_/`,_|  |  | |  |  |  ___.--""`\
    | ||  ||  |       |  |\.| |=,|  |""          `,
    | ||  ||  |       |  |  | |  |  |____________.-+.__
   _:_!|_,'!__!       |  |  | |_,!  !         __,I   `"|
  :     |      `-""`,.!__!-,!_!_ '--'`,_,--"""         |
  |     ;___          `"-.-'    `,_.-'"            _..-'
   `-._ |   """--,,_     |`""-.--'|         __.--""
       `"--..__     ""--.|    |   |_,_  _.-'
               ""--.._   `-,__!_.-' _,""     
                      ""--,____.--'"
The world around you begins to tremble and collapse.... everything is being shrouded in darkness... until you cannot see anything... until nothing else exists.. you are stuck in the eternal abyss. A small light which represents the universe is becoming smaller and smaller... its gone.. darkness surrounds you.. nothing surrounds you.....
                      
                      ''')
    else: print("you have failed.. so close")
  else: print('''                    __.............__
           .--""```                 ```""--.
            ':--..___             ___..--:'
              \      ```"""""""```      /
            .-`  ___.....-----.....___  '-.
          .:-""``     ~          ~    ``""-:.
         /`-..___ ~        ~         ~___..-'\
        /  ~    '`""---.........---""`        \
       ;                                       ;
      ; '::.   '          _,           _,       ;
      |   ':::    '     .' (    ~   .-'./    ~  |
      |~  .:'   .     _/..._'.    .'.-'/        |
      | .:'       .-'`      ` '-./.'_.'         |
      |  ':.     ( o)   ))      ;= <_           |
      ; '::.      '-.,\\__ __.-;`\'. '.  .      ;
       ;    ':         \) |`\ \)  '.'-.\       ;
        \.:'.:':.         \_/       '-._\     /
         \ ':.     ~                    `    /
          '. '::..  _ . - - -- .~ _      ~ .'
            '-._':'                 `'-_.-'
              (``''--..._____...--''``)
                `"--...__     __...--"`
                         `````
You try swimming but the river does not allow you... it overpowers you and sucks you in...\n you wake up in a fish bowl, confused.... you look into the reflection and see that you are indeed a fish, you look outside beyond the bowl to see that you are inside someones house... confused and unable to do anything....\n"is this my fate forever" you think?.... \ni would've waited if i was you..."''')
else: print('''
 |"""""""i"""""""""""""i"""""""""""""i"""""""""""""i"""""""""""""i"""""""|
 |""3D"""""X"""""3D"""""X"""""3D"""""X"""""3D"""""X"""""3D"""""X"""""3D""|
 |["""""""""]X["""""""""]X["""""""""]X["""""""""]X["""""""""]X["""""""""]|
 |"XXX""SIG"""XXX""SIG"""XXX""SIG"""XXX""SIG"""XXX""SIG"""XXX""SIG"""XXX"|
 |""""XXX"""""""XXX"""""""XXX"""""""XXX"""""""XXX"""""""XXX"""""""XXX""""|
 |X["LS"]XXX["LS"]XXX["LS"]XXX["LS"]XXX["LS"]XXX["LS"]XXX["LS"]XXX["LS"]X|
 |"XXXXX"""XXXXX"""XXXXX"""XXXXX"""XXXXX"""XXXXX"""XXXXX"""XXXXX"""XXXXX"|
 |XXX""XXXXX""XXXXX""XXXXX""XXXXX""XXXXX""XXXXX""XXXXX""XXXXX""XXXXX""XXX|

A hole opens up underneath you fall into the ocean with ferocious waves. you do not survive..... teleportation has not been invented yet..... silly.''')

