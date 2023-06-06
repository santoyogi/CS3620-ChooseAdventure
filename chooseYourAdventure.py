# Gissel Santoyo
# CS 3620
# Choose Your Own Adventure
# Professor Squadroni
# Due: 6/05/23
# File: chooseYourAdventure.py
# This is a program where the user will go through a story and
# input their decisions on what to do next.
# Assumptions:
# The assignment states to use conditional statements, so I used
# switch cases, and it says the user will input a word to choose their
# destiny, but I used numbers instead

# ----------------------------- LISTS OF CHOICES ----------------------------------
planets = ["Aireese", "Leos", "Saggitar",
           "Tarrow", "Virgon", "Caprico",
           "Gemi", "Libro", "Aquas",
           "Scorpen", "Pisca", "Cansar"]

ship_problem = ["There is a hole in the ship",
                "Foreign body in ship detected"]

hole_in_ship = ["Jump into action anyway",
                "Turn around and inform crew"]

foreign_body = ["Investigate",
                "Go back to sleep"]

low_oxygen = ["Make early landing",
              "Take chances and continue hyper-sleep"]

ominous_fate = ["Ominous fate one",
                "Ominous fate two"]

landing_decision = ["Leave ship",
                    "Stay in ship"]

leaving_ship = ["Go east", "Go West"]

east = ["Eat Lunch", "Signal Home"]

borse = ["Escape Planet", "Attack bear/horse"]

final_decision = ["Warn Earth 2.0", "Escape Planet"]

# ----------------------------- FUNCTIONS -------------------------------------
def landing_print_write():
    print("\n\tLanding on planet", planets[planet - 1], "is not a smooth ", end="")
    print("ride. The surface makes for\na rocky landing. The good news is",
          planets[planet - 1], "has an oxygen rich atmosphere that \nallows ", end="")
    print("the crew to breathe. Once on the ground the crew must decide if they "
          "\nshould leave the ship immediately or stay inside for a while.\n")

    f = open("story.txt", "a")
    f.write("\n\tLanding on planet ")
    f.write(planets[planet - 1])
    f.write(" is not a smooth ride. The surface makes for\na rocky landing. "
            "The good news is")
    f.write(planets[planet - 1])
    f.write("has an oxygen rich atmosphere that \nallows "
            "the crew to breathe. Once on the ground the crew must decide if they"
            "\nshould leave the ship immediately or stay inside for a while.\n")
    f.close()


def planet_landing():
    landing_print_write()

    for x in range(2):
        print(x + 1, ".", landing_decision[x])
    print("\nChoose action(1-2): ", end="")
    action = input()
    choice_6(int(action))


def planet_landing2():
    landing_print_write()
    for x in range(2):
        print(x + 1, ".", landing_decision[x])
    print("\nChoose action(1-2): ", end="")
    action = input()
    choice_61(int(action))

# ------------------------- SWITCH CASES FOR USER CHOICE  ---------------------------


def choice_10(choice):
    match choice:
        case 1:
            choice_8(2)
        case 2:
            choice_9(1)


def choice_9(choice):
    match choice:
        case 1:
            print("\n\tThe captain makes the scary decision to leave the "
                  "planet as it seems \ntoo dangerous. The leave immediately"
                  " and search for a neighboring planet but \nhave made a "
                  "grave mistake. Next to the planet was a very dark black"
                  " hole that \nthey had not observed before. Sadly the ship"
                  " had gotten too close to it in their \nescape and they "
                  "were swallowed. Losing all connection to earth 2.0. The"
                  " end. ")

            f = open("story.txt", "a")
            f.write("\n\tThe captain makes the scary decision to leave the "
                    "planet as it seems \ntoo dangerous. The leave immediately"
                    " and search for a neighboring planet but \nhave made a "
                    "grave mistake. Next to the planet was a very dark black"
                    " hole that \nthey had not observed before. Sadly the ship"
                    " had gotten too close to it in their \nescape and they "
                    "were swallowed. Losing all connection to earth 2.0. The"
                    " end. ")
            f.close()

        case 2:
            print("\n\tThe Captain decides they have to fight the borse and so"
                  " they gear up with \nmakeshift weapons and go out to beat"
                  " the borse. The borse is gigantic, the \nborse is mean but"
                  " the crew is brave and they have numbers. For hours the"
                  " crew \nfights off the borse. In the end, the crew is "
                  "victorious but they fear that \ntheir may be more creatures"
                  " lurking.\n")

            f = open("story.txt", "a")
            f.write("\n\tThe Captain decides they have to fight the borse and so"
                    " they gear up with \nmakeshift weapons and go out to beat"
                    " the borse. The borse is gigantic, the \nborse is mean but"
                    " the crew is brave and they have numbers. For hours the"
                    " crew \nfights off the borse. In the end, the crew is "
                    "victorious but they fear that \ntheir may be more creatures"
                    " lurking.\n")
            f.close()

            for x in range(2):
                print(x + 1, ".", final_decision[x])
            print("\nChoose action(1-2): ", end="")
            action = int(input())
            choice_10(int(action))


def choice_8(choice):
    match choice:
        case 1:
            print("\n\tThe crew eats their lunch happily. They talk about"
                  " home, about their \nloved ones and the future. In the"
                  " distance they hear a noise. A thundering \nfall of trees."
                  " A couple seconds after, they hear it again. They all "
                  "become alert \nand look around. Closer and closer the trees"
                  " fall until the trees next to the \nship collapse and they"
                  " see it. A gigantic bear with the head of a horse. With \na"
                  " mighty neigh the bear/horse charges at the crew. It "
                  "tramples two members \nand the rest barely escape into the"
                  " ship. The ship however, is no match for \nthis bear. What"
                  " is there to do???\n")

            f = open("story.txt", "a")
            f.write("\n\tThe crew eats their lunch happily. They talk about"
                    " home, about their \nloved ones and the future. In the"
                    " distance they hear a noise. A thundering \nfall of trees."
                    " A couple seconds after, they hear it again. They all "
                    "become alert \nand look around. Closer and closer the trees"
                    " fall until the trees next to the \nship collapse and they"
                    " see it. A gigantic bear with the head of a horse. With \na"
                    " mighty neigh the bear/horse charges at the crew. It "
                    "tramples two members \nand the rest barely escape into the"
                    " ship. The ship however, is no match for \nthis bear. What"
                    " is there to do???\n")
            f.close()

            for x in range(2):
                print(x + 1, ".", borse[x])
            print("\nChoose action(1-2): ", end="")
            action = int(input())
            choice_9(int(action))
        case 2:
            print("\n\tCaptain decides that they must warn Earth 2.0 of their"
                  " discovery. They \nsend a signal and wait. A day "
                  "passes.. Nothing. They go about their \ndays. Gather"
                  " resources, eat, signal, fight off creatures, wait. "
                  "Nothing. \nWeeks pass and nothing. The crew now has a "
                  "nice little base \ncamp and they thrive. Some even begin"
                  " the process of re-population. \nYears pass and nothing. "
                  "There are babies on Earth 3.0 now and \nhope of Earth 2.0 "
                  "responding has vanished. The new colony of Earth 3.0 is"
                  " \nthe lonely future of humanity. The end. ")
            f = open("story.txt", "a")
            f.write("\n\tCaptain decides that they must warn Earth 2.0 of their"
                    " discovery. They \nsend a signal and wait. A day "
                    "passes.. Nothing. They go about their \ndays. Gather"
                    " resources, eat, signal, fight off creatures, wait. "
                    "Nothing. \nWeeks pass and nothing. The crew now has a "
                    "nice little base \ncamp and they thrive. Some even begin"
                    " the process of re=population. \nYears pass and nothing. "
                    "There are babies on Earth 3.0 now and \nhope of Earth 2.0 "
                    "responding has vanished. The new colony of Earth 3.0 is"
                    " \nthe lonely future of humanity. The end. ")
            f.close()


def choice_7(choice):
    match choice:
        case 1:
            print("The crew decides to go east and they find a lake of"
                  " fresh water. Carelessly, \nsome of the crew jumps in "
                  "for a soak. 1, 2 ,3 of them jump in and \nthey splash "
                  "around playfully and surprisingly nothing goes wrong."
                  " \nAfter collecting water they go back to the ship.\n")

            f = open("story.txt", "a")
            f.write("The crew decides to go east and they find a lake of"
                    " fresh water. Carelessly, \nsome of the crew jumps in "
                    "for a soak. 1, 2 ,3 of them jump in and \nthey splash "
                    "around playfully and surprisingly nothing goes wrong."
                    " \nAfter collecting water they go back to the ship.\n")
            f.close()

            for x in range(2):
                print(x + 1, ".", east[x])
            print("\nChoose action(1-2): ", end="")
            action = input()
            choice_8(int(action))
        case 2:
            print("\n\tCaptain Decides to go west. There they find a river of"
                  " fresh water. They \ncollect it and return to camp. They"
                  " boil it and drink it. All is fine for the rest\nof the"
                  " day. They sleep to regain their energy for the next day"
                  " but everybody \nstarts to get a tummy ache. Something"
                  " isn’t right. The next morning half \nof the crew has"
                  " turned green. Captain sends them away from camp for"
                  " the day to \nquarantine them. Later in the day one of "
                  "the green members return. They have \nno emotion on their"
                  " face. Captain tells them to leave. They don’t, instead\n"
                  "the green member throws up acid all over the captain."
                  " The Captain screams in \npain and writhers around, "
                  "transforming into a venus fly trap creature. Captain\n"
                  "Venus begins growing vines that are strong and long."
                  " He wraps them \naround the remaining crew and brings them"
                  " to his mouth. He eats them like the \nflies that they are."
                  " The end. ")
            f = open("story.txt", "a")
            f.write("\n\tCaptain Decides to go west. There they find a river of"
                    " fresh water. They \ncollect it and return to camp. They"
                    " boil it and drink it. All is fine for the rest\nof the"
                    " day. They sleep to regain their energy for the next day"
                    " but everybody \nstarts to get a tummy ache. Something"
                    " isn’t right. The next morning half \nof the crew has"
                    " turned green. Captain sends them away from camp for"
                    " the day to \nquarantine them. Later in the day one of "
                    "the green members return. They have \nno emotion on their"
                    " face. Captain tells them to leave. They don’t, instead\n"
                    "the green member throws up acid all over the captain."
                    " The Captain screams in \npain and writhers around, "
                    "transforming into a venus fly trap creature. Captain\n"
                    "Venus begins growing vines that are strong and long."
                    " He wraps them \naround the remaining crew and brings them"
                    " to his mouth. He eats them like the \nflies that they are."
                    " The end. ")
            f.close()


def choice_61(choice):
    match choice:
        case 1:
            print("\n\tThe crew fights captain to convince them to leave the"
                  " ship. Captain \nis being weird and not themselves. They leads"
                  " them away from the \nship and to where they believe there's"
                  " water but instead they go \ntowards an area with tar. The"
                  " crew pleads for captain to turn \naround but instead they"
                  " push a crew member into the tar. The member \nstruggles to get"
                  " out but they can't. Another member tries to \nfree them but"
                  " gets stuck themselves. One by one, Captain shoves the \n"
                  "members into the tar. They plead but Captain doesn't look"
                  " like \ncaptain anymore. They stands over the team as the tar"
                  " consumes them. \nCaptain laughs. The end.")
            f = open("story.txt", "a")
            f.write("\n\tThe crew fights captain to convince them to leave the"
                    " ship. Captain \nis being weird and not themselves. They leads"
                    " them away from the \nship and to where they believe there's"
                    " water but instead they go \ntowards an area with tar. The"
                    " crew pleads for captain to turn \naround but instead they"
                    " push a crew member into the tar. The member \nstruggles to get"
                    " out but they can't. Another member tries to \nfree them but"
                    " gets stuck themselves. One by one, Captain shoves the \n"
                    "members into the tar. They plead but Captain doesn't look"
                    " like \ncaptain anymore. They stands over the team as the tar"
                    " consumes them. \nCaptain laughs. The end.")
            f.close()
        case 2:
            print("\n\tCaptain Decides it's best to stay in the ship. But "
                  "Captain is being \nweird, they talk to themselves in the "
                  "corner and stares too \nseriously at the crew. The crew "
                  "decides to have dinner. \nCaptain doesn't eat but they "
                  "lick their lips and watch. \nAfter dinner Captain invites "
                  "the crew to the supply room. Once \ninside Captain leaves "
                  "the crew in the room alone and locks \nthe door behind them. "
                  "The remains of old captain rises from the \ncorner. "
                  "The crew screams in horror as the mangled corpse of \ntheir "
                  "former captain charges at them. Burnt up captain touches "
                  "\nthe members and they spontaneously combust. The room "
                  "soon \nfills with flames and kills everyone but “Captain”. The end.")

            f = open("story.txt", "a")
            f.write("\n\tCaptain Decides it's best to stay in the ship. But "
                    "Captain is being \nweird, they talk to themselves in the "
                    "corner and stares too \nseriously at the crew. The crew "
                    "decides to have dinner. \nCaptain doesn't eat but they "
                    "lick their lips and watch. \nAfter dinner Captain invites "
                    "the crew to the supply room. Once \ninside Captain leaves "
                    "the crew in the room alone and locks \nthe door behind them. "
                    "The remains of old captain rises from the \ncorner. "
                    "The crew screams in horror as the mangled corpse of \ntheir "
                    "former captain charges at them. Burnt up captain touches "
                    "\nthe members and they spontaneously combust. The room "
                    "soon \nfills with flames and kills everyone but “Captain”. The end.")
            f.close()


def choice_6(choice):
    match choice:
        case 1:
            print("\n\tLeaving the ship is a risky move but the planet of"
                  , planets[planet - 1], "is beautiful. \nThe air is clean,"
                     " the ground is covered in greenery. Could this be \nEarth"
                     " 3.0??? Captain and the crew set up a small camp outside"
                     " the ship. \nThey collect resources and notify Earth 2.0 of"
                     " their discovery. Night \ntime comes and things feel "
                     "hopeful for once. In the morning, they look for \nfresh"
                     " water. \n")

            f = open("story.txt", "a")
            f.write("\n\tLeaving the ship is a risky move but the planet of ")
            f.write(planets[planet - 1])
            f.write(" is beautiful. \nThe air is clean,"
                    " the ground is covered in greenery. Could this be \nEarth"
                    " 3.0??? Captain and the crew set up a small camp outside"
                    " the ship. \nThey collect resources and notify Earth 2.0 of"
                    " their discovery. Night \ntime comes and things feel "
                    "hopeful for once. In the morning, they look for \nfresh"
                    " water. \n")
            f.close()

            for x in range(2):
                print(x + 1, ".", leaving_ship[x])
            print("\nChoose action(1-2): ", end="")
            action = input()
            choice_7(int(action))


def choice_5(choice):
    match choice:
        case 1:
            print("\n\tThe Captain and crew make the decision to land on a"
                  " nearby planet as\n they fear they will lose all their"
                  " oxygen. However when they land, they\nmake a dark "
                  "realization. The planet is covered in worms. Big worms, "
                  "little \nworms, pink worms, yellow worms and of course;"
                  " man eating worms. They stay\nin the ship as it is too"
                  " dangerous to step outside. The oxygen still dwindles\n"
                  "and within a couple weeks the crew resorts to stepping"
                  " outside. Once they open \nthe door. One humongous purple"
                  " worm swallows the team whole. The end.")
            f = open("story.txt", "a")
            f.write("\n\tThe Captain and crew make the decision to land on a"
                    " nearby planet as\n they fear they will lose all their"
                    " oxygen. However when they land, they\nmake a dark "
                    "realization. The planet is covered in worms. Big worms, "
                    "little \nworms, pink worms, yellow worms and of course;"
                    " man eating worms. They stay\nin the ship as it is too"
                    " dangerous to step outside. The oxygen still dwindles\n"
                    "and within a couple weeks the crew resorts to stepping"
                    " outside. Once they open \nthe door. One humongous purple"
                    " worm swallows the team whole. The end.")
            f.close()
        case 2:
            print("\n\tThe crew decides to sleep in the hopes of conserving"
                  " oxygen. They close\n their eyes and pray for the best.",
                  planets[planet - 1], "is only a couple weeks away.\n")
            f = open("story.txt", "a")
            f.write("\n\tThe crew decides to sleep in the hopes of conserving"
                    " oxygen. They close\n their eyes and pray for the best. ")
            f.write(planets[planet - 1])
            f.write(" is only a couple weeks away.\n")
            f.close()

            planet_landing()


def choice_4(choice):
    match choice:
        case 1:
            print("\n\tStill, Captain is brave, so they decide to go towards the"
                  " hole\n and patch it with some tape. Not a good idea. When"
                  " they are a\n foot away from the hole. Whoosh! Captain is "
                  "sucked out the hole\n and launched into space. In the "
                  "process their helmet hits the wing\n of the spaceship and"
                  " cracks wide open. Captain is dead\n and in a matter of"
                  " seconds, the ship explodes! The end.")
            f = open("story.txt", "a")
            f.write("\n\tStill, Captain is brave, so they decide to go towards the"
                    " hole\n and patch it with some tape. Not a good idea. When"
                    " they are a\n foot away from the hole. Whoosh! Captain is "
                    "sucked out the hole\n and launched into space. In the "
                    "process their helmet hits the wing\n of the spaceship and"
                    " cracks wide open. Captain is dead\n and in a matter of"
                    " seconds, the ship explodes! The end.")
            f.close()
        case 2:
            print("\n\tQuickly, Captain runs back to the sleeping chambers. "
                  "“Everybody get up\nimmediately!” The crew is up within"
                  " seconds. Although disoriented,\nthey make their way to"
                  " the engine room. With their suits on they enter.\n"
                  "Thankfully the crew is well equipped and they quickly "
                  "fix the ship. \nHowever, their oxygen is now low and a"
                  " decision must be made.\n")
            f = open("story.txt", "a")
            f.write("\n\tQuickly, Captain runs back to the sleeping chambers. "
                    "“Everybody get up\nimmediately!” The crew is up within"
                    " seconds. Although disoriented,\nthey make their way to"
                    " the engine room. With their suits on they enter.\n"
                    "Thankfully the crew is well equipped and they quickly "
                    "fix the ship. \nHowever, their oxygen is now low and a"
                    " decision must be made.\n")
            f.close()

            for x in range(2):
                print(x + 1, ".", low_oxygen[x])
            print("\nChoose action(1-2): ", end="")
            action = input()
            choice_5(int(action))
        case 3:
            print("\n\tAs Captain creeps up to the room they smell something"
                  " putrid. It’s the smell\nof burning flesh. Frightened that"
                  " something may be on fire they slam the door \nto the"
                  " supply room open. There they see themselves. Or more"
                  "the body of their\nburning self. How could that be??"
                  " They look down at their hands and\nflames erupt. Suddenly"
                  " their whole body is on fire! Flailing around, Captain"
                  " \nlooks at the previously burning body and they once again "
                  "see themselves but now \nperfectly fine. Unfortunately"
                  " captain burns to death in the supply room while \nthe"
                  " foreign body steps over them and takes their place"
                  " while none of the crew\nknows. “Captain” goes into the"
                  " sleep chambers and rests until they reach ", planets[planet - 1])
            f = open("story.txt", "a")
            f.write("\n\tAs Captain creeps up to the room they smell something"
                    " putrid. It’s the smell\nof burning flesh. Frightened that"
                    " something may be on fire they slam the door \nto the"
                    " supply room open. There they see themselves. Or more"
                    "the body of their\nburning self. How could that be??"
                    " They look down at their hands and\nflames erupt. Suddenly"
                    " their whole body is on fire! Flailing around, Captain"
                    " \nlooks at the previously burning body and they once again "
                    "see themselves but now \nperfectly fine. Unfortunately"
                    " captain burns to death in the supply room while \nthe"
                    " foreign body steps over them and takes their place"
                    " while none of the crew\nknows. “Captain” goes into the"
                    " sleep chambers and rests until they reach ")
            f.write(planets[planet - 1])
            f.write("\n")
            f.close()

            planet_landing2()
        case 4:
            print("With no hesitation, Captain enters the supply room. "
                  "However, \nwhat they find confuses them. A single crab "
                  "sat in the middle \nof the room. This creature had been "
                  "extinct for hundreds of \nyears. Captain, not knowing "
                  "what crabs are capable of, \napproaches the crustacean. "
                  "Suddenly, Mr.Crabs extends a claw \nthat begins to grow "
                  "in size. In mere seconds the claw is \nlarger than captain. "
                  "And in one smooth clamp, the crab cuts \ncaptain in half! "
                  "Quickly the crab eats the pieces of Captain \nand crashes "
                  "through the ship walls to flee. This causes the \nrest of "
                  "the ship to shut down, killing the rest of the crew. \nThe "
                  "end.")
            f = open("story.txt", "a")
            f.write("With no hesitation, Captain enters the supply room. "
                    "However, \nwhat they find confuses them. A single crab "
                    "sat in the middle \nof the room. This creature had been "
                    "extinct for hundreds of \nyears. Captain, not knowing "
                    "what crabs are capable of, \napproaches the crustacean. "
                    "Suddenly, Mr.Crabs extends a claw \nthat begins to grow "
                    "in size. In mere seconds the claw is \nlarger than captain. "
                    "And in one smooth clamp, the crab cuts \ncaptain in half! "
                    "Quickly the crab eats the pieces of Captain \nand crashes "
                    "through the ship walls to flee. This causes the \nrest of "
                    "the ship to shut down, killing the rest of the crew. \nThe "
                    "end.")
            f.close()


def choice_3(choice):
    match choice:
        case 1:
            print("\n\tOn the panel Captain notes the hole is located at the "
                  "back of the ship\nwhere all their Engines reside. This "
                  "does not look good. Without hesitation,\nCaptain runs to"
                  " fix the problem and fails to \ninform the crew who are "
                  "still recovering from years of sleep.\nQuickly Captain "
                  "suits up and enters the engine room.\nA gigantic hole is"
                  " seen on the left wall. The hole sucks\nany and everything"
                  " out; the machines beep and flash.\nCaptain realizes this"
                  " isn’t something he can handle on his own.")
            f = open("story.txt", "a")
            f.write("\n\tOn the panel Captain notes the hole is located at the "
                    "back of the ship\nwhere all their Engines reside. This "
                    "does not look good. Without hesitation,\nCaptain runs to"
                    " fix the problem and fails to \ninform the crew who are "
                    "still recovering from years of sleep.\nQuickly Captain "
                    "suits up and enters the engine room.\nA gigantic hole is"
                    " seen on the left wall. The hole sucks\nany and everything"
                    " out; the machines beep and flash.\nCaptain realizes this"
                    " isn’t something he can handle on his own.")
            f.close()
            print("\nChoose action(1-2): ", end="")
            action = input()
            choice_3(int(action))
        case 2:
            print("\n\tCaptain decides to check out the situation and let"
                  " the rest of the crew \nsleep. The foreign body is detected"
                  " in the supply room. Slowly, Captain makes \nhis way to the"
                  " room as he is disoriented and slightly frightened. After"
                  " all, what \ncould possibly be in the supply room? \n")

            f = open("story.txt", "a")
            f.write("\n\tCaptain decides to check out the situation and let"
                    " the rest of the crew \nsleep. The foreign body is detected"
                    " in the supply room. Slowly, Captain makes \nhis way to the"
                    " room as he is disoriented and slightly frightened. After"
                    " all, what \ncould possibly be in the supply room? \n")
            f.close()

            for x in range(2):
                print(x + 1, ".", ominous_fate[x])
            print("\nChoose action(1-2): ", end="")
            action = int(input())
            action = action + 2
            choice_4(int(action))
        case 3:
            print("\n\tCaptain makes the decision to continue sleeping. Bad"
                  " mistake. As the crew\nsleeps, a giant tentacled "
                  "creature makes its way to the sleeping chambers. \nThere"
                  " he has a feast on the buffet of bodies. Everyone is "
                  "eaten peacefully in\ntheir sleep. The end.")
            f = open("story.txt", "a")
            f.write("\n\tCaptain makes the decision to continue sleeping. Bad"
                    " mistake. As the crew\nsleeps, a giant tentacled "
                    "creature makes its way to the sleeping chambers. \nThere"
                    " he has a feast on the buffet of bodies. Everyone is "
                    "eaten peacefully in\ntheir sleep. The end.")
            f.close()


def choice_2(choice):
    print("\n\tThe captain is up before the rest of the crew. Limbs "
          "totally weak,\nmind is hazy and vision is low. They "
          "stumble towards the control\npanel and on the screen, "
          "clear as day, a warning message:\n", end="")
    f = open("story.txt", "a")
    f.write("\n\tThe captain is up before the rest of the crew. Limbs "
            "totally weak,\nmind is hazy and vision is low. They "
            "stumble towards the control\npanel and on the screen, "
            "clear as day, a warning message:\n")
    match choice:
        case 1:
            print("“HOLE IN SHIP DETECTED. REPAIR IMMEDIATELY.”\n")
            f.write("“HOLE IN SHIP DETECTED. REPAIR IMMEDIATELY.”\n")
            f.close()
            for x in range(2):
                print(x + 1, ".", hole_in_ship[x])
            print("\nChoose action(1-2): ", end="")
            action = input()
            choice_4(int(action))
        case 2:
            print("“FOREIGN BODY IN SHIP DETECTED.”")
            f.write("“FOREIGN BODY IN SHIP DETECTED.”")
            f.close()
            for x in range(2):
                print(x + 1, ".", foreign_body[x])
            print("\nChoose action(1-2): ", end="")
            action = int(input())
            action = action + 1
            choice_3(int(action))


# ----------------------- STORY BEGINNING ------------------------------
print("\n A Tale of space! \n")
print("\tOff into space, the rocket zoomed. A planet here, a star there. "
      "It’s all\na blur of brightness and darkness at the speed of light. "
      "Following the\nfall of Earth 1.0, the uber-rich destroyed Earth 2.0"
      " with their\nselfishness and greed. The generation of 3000 is humanity's"
      " last chance\nat survival. As a last-ditch attempt to save the human race, "
      "the \ngovernment of the New States of America has sent a team of 5 "
      "on a mission\nto a new planet named:\n")

for x in range(12):
    print(x + 1, ".", planets[x])
print("\nChoose Planet(1-12): ", end="")
planet = int(input())

print("\n\tHowever,", planets[planet - 1],
      "has only been observed from thousands of light-years\n"
      "away and the only thing known about it are that it has water.")
print("\tThe team is made up of regular civilian volunteers as most believe\n"
      "that the mission to", planets[planet - 1], "is a suicide mission. Still, "
      "these brave explorers\nagreed to be the hope of Earth 2.0 and now we "
      "join them on their journey to a\nhospitable planet. Light-years away "
      "the members of the ship are in hyper-sleep.\nOnly weeks away from their "
      "destination something goes terribly wrong. The\nalarms sound, and "
      "the team is ripped out of their resting state.\nWhat could be going on?!\n")

# ----------------------------- WRITING STORY TO FILE -------------------------
f = open("story.txt", "w")
f.write("\n A Tale of space! \n"
        "\tOff into space, the rocket zoomed. A planet here, a star there. "
        "It’s all\na blur of brightness and darkness at the speed of light. "
        "Following the\nfall of Earth 1.0, the uber-rich destroyed Earth 2.0"
        " with their\nselfishness and greed. The generation of 3000 is humanity's"
        " last chance\nat survival. As a last-ditch attempt to save the human race, "
        "the \ngovernment of the New States of America has sent a team of 5 "
        "on a mission\nto a new planet named:\n")
f.write("\n\tHowever, ")
f.write(planets[planet - 1])
f.write("has only been observed from thousands of light-years\n"
        " away and the only thing known about it are that it has water.\n"
        "\tThe team is made up of regular civilian volunteers as most believe\n"
        "that the mission to ")
f.write(planets[planet - 1])
f.write("is a suicide mission. Still, "
        "these brave explorers\nagreed to be the hope of Earth 2.0 and now we "
        "join them on their journey to a\nhospitable planet. Lighters away "
        "the members of the ship are in hyper-sleep.\nOnly weeks away from their "
        "destination something goes terribly wrong. The\nalarms sound, and "
        "the team is ripped out of their resting state.\nWhat could be going on?!\n")
f.close()

# ------------------------------ FIRST MAJOR DECISION --------------------------------

for x in range(2):
    print(x + 1, ".", ship_problem[x])

print("\nChoose Problem with ship(1-2): ", end="")
ship_problem = input()
choice_2(int(ship_problem))
