label testScene01:
    # would be nice for the hall way image
    scene temp_woodlands
    "I turn the corner and start heading down the hallway to the Business Office."
    "Of course there's a long line, and of course it's filled with frustrated, impatient Fables who've been waiting all morning to see someone."
    "I try not to make eye contact."
    "Right when I'm two feet away from the door, a hand reaches out to grab my shoulder."
    "A voice I feel like I've heard too many times speaks."
    show gren neutral at truecenter with vpunch
    gren "Oh, so what, you're going to keep doing this shit NOW? It's Christmas, dickhead. How about a little compassion?"
    # show gren neutral with move at right
    show gren neutral:
        xpos 0.75 ypos 0.5

    show bigby neutral at left with dissolve
    show selected_play with dissolve
    $ time = 30 #Place how long you want the timer to run
    $ timer_range = 30
    $ timer_jump = "ts01A" #Option to jump to when the timer runs out
    show screen countdown
    menu:
        "What should I say?"

        "Fresh out.":
            jump ts01A
        "I work here.":
            jump ts01B
        "I'm about as happy as you are.":
            jump ts01C
        "...":
            jump ts01D

label ts01A:
    bigby "Fresh out. Sorry."
    "Gren makes a noise that sounds suspiciously like a \"fuck you\" when I shrug his hand off and reach for the doorknob to the office."
    scene black with dissolve
    return

label ts01B:
    bigby "I WORK here. What, do you want to?"
    gren "I'd probably do a better fucking job than you would."
    "I already feel a headache coming on when I shrug his hand off and reach for the doorknob to the office."
    scene black with dissolve
    return

label ts01C:
    bigby "Trust me, I'm about as happy with this as you are."
    gren "Sure."
    bigby "No, really. Seeing you on Christmas Eve warms my heart."
    "Gren's lip curls in a cruel sneer."
    gren "Maybe I should fuckin' eat your—"
    "I slam the door in his face." with vpunch
    scene black with dissolve
    return

label ts01D:
    bigby "..."
    gren "Yeah, that's par the course with you. Asshole."
    "I shrug his hand off and reach for the doorknob to the office."
    scene black with dissolve
    return
