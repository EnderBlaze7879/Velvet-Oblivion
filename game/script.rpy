# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character('Serein', color="#ff6060")

define m = Character("[mcname]", color="#9e9c9c")

image serein normal:
    "Sprites/serein normal.png"
    zoom 1.5

image serein pout:
    "Sprites/serein pout.png"
    zoom 1.5

image bg hallway1:
    "Backgrounds/bg hallway1.jpg"
    zoom 3

image bg classroom1:
    "Backgrounds/bg classroom1.jpg"
    zoom 2.2

image bg classroom1dark:
    "Backgrounds/bg classroom1dark.jpg"
    zoom 2.2

label start:
    scene bg classroom1dark
    with fade

    "{cps=10}Name...{/cps}"
    "{cps=10}Name...{w} Name...{w} Name...{/cps}"
    "{cps=10}It's on the tip of my tongue, but I can't seem to remember it...{/cps}"
    
    python:
        mcname = renpy.input("What is my name?", length=20)

    m "{cps=10}[mcname]...{/cps}"
    m "{cps=10}[mcname]...{/cps}"
    m "{cps=10}Right... My name is [mcname]...{/cps}"
    m "{cps=10}Why was that so difficult..?{/cps}"

    "???" "\"Hey!\""

    scene bg classroom1
    with dissolve

    show serein normal at truecenter
    with dissolve

    "???" "\"[mcname]! Wake up! The bell rang a while ago!\""

    menu:
        "\"Who are you?\"":

            show serein pout at truecenter
            with dissolve

            "???" "\"Ha ha, very funny!\""

        "\"I've been awake...\"":

            show serein pout at truecenter
            with dissolve

            "???" "\"Stop Lying! You've been asleep all day!\""

        "\"I don't know you.\"":

            show serein pout at truecenter
            with dissolve

            "???" "\"Yeah Right! Stop messing with me!\""

    show serein normal at truecenter
    with dissolve

    "???" "\"Anyways, the bell rang a while ago, so we should get to class before the teacher gets mad at us.\""

    menu:
        "Follow Her":
            scene bg hallway1
            hide serein normal
            with dissolve

            m "I follow her to class, but I can't seem to remember her name."
            jump goingtoclass1

        "Ignore Her":
            "..."

            show serein pout at truecenter
            with dissolve

            "..."
            "???" "\"Whatever. I guess i'll go to class by myself then.\""
            
            hide serein pout
            with dissolve

            scene bg hallway1
            with dissolve

            m "with a sigh, I follow her to class, but I can't seem to remember her name."

    label goingtoclass1:

        m "For some reason, she seems to know mine better than I do."

    label class1:

        scene bg classroom1
        with fade

        m "The teacher seems to be in a bad mood today."
        m "What was the teacher's name again?"
        m "Who cares..."

        scene bg classroom1dark
        with dissolve

        m "Who was that girl? I feel like I should know her, but I just cant remember."
        m ""