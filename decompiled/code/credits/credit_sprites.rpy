default trying_skip = False

screen credits_roll():

    key "mouseup_1" action SetVariable("trying_skip", True)
    key "mouseup_3" action SetVariable("trying_skip", True)
    key "K_ESCAPE" action SetVariable("trying_skip", True)
    key "K_MENU" action SetVariable("trying_skip", True)
    key "K_RETURN" action SetVariable("trying_skip", True)
    key "K_KP_ENTER" action SetVariable("trying_skip", True)
    key "K_PAUSE" action SetVariable("trying_skip", True)
    key "K_SPACE" action SetVariable("trying_skip", True)

    vbox:
        style_prefix "credits_roll"
        spacing 598
        at credits_roll_effect

        null height 800

        frame:
            xsize 1920
            background None
            has vbox
            xpos 100
            spacing -30
            text _("Story Writing -") xpos -30
            null height 60
            add "writer1"
            add "writer2"
            add "writer3"
            add "writer4"
            add "writer7"
            add "writer5"
            add "writer6"

        frame:
            xsize 1920
            background None
            has vbox
            xpos 1350
            spacing -30
            text _("Art -") xpos -30
            null height 60
            add "artist1"
            add "artist2"
            add "artist3"
            add "artist4"
            add "artist5"
            add "artist6"
            add "artist7"
            add "artist8"
            add "artist9"
            add "artist10"
            add "artist11"

        frame:
            xsize 1920
            background None
            has vbox
            xpos 1350
            spacing -30
            text _("Programming -") xpos -30
            null height 60
            add "coder1"
            add "coder2"
            add "coder3"
            add "coder4"

        frame:
            xsize 1920
            background None
            has vbox
            xpos 100
            spacing -30
            text _("Sound design -") xpos -30
            null height 60
            add "sound1"

        frame:
            xsize 1920
            background None
            has vbox
            xpos 100
            spacing -30
            text _("Music -") xpos -30
            null height 60
            add "music1"
            add "music2"
            add "music3"
            add "music4"

        frame:
            xsize 1920
            background None
            has vbox
            xpos 1350
            spacing -30
            text _("Testing, Proofreading\n& Translation -") xpos -30
            null height 60
            add "tester1"
            add "tester2"
            add "tester3"

        frame:
            xsize 1920
            background None
            has vbox
            xpos 1350
            spacing -30
            text _("Special Thanks -") xpos -30
            null height 60
            add "special1"
            add "special2"
            add "special3"

        frame:
            xsize 1920
            background None
            has vbox
            style_prefix "thank_you"
            xpos 100
            text _("This game was only\nmade possible with\nall the support we have\nfrom Patreon\nand SubscribeStar")

        frame:
            xsize 1920
            background None
            has vbox
            style_prefix "thank_you"
            xpos 100
            text _("Huge thanks to\nall of our fans\nand everyone who\nsupported us and\nhelped to bring\nthis story to life")

        null height 1500

    if trying_skip is True:
        hbox:
            style_prefix "skip_recap"
            yalign 0.95
            xalign 0.5
            textbutton _("SKIP") action [Hide("credits_roll"), Jump("end_credits_end")]

        timer 3.0 action SetVariable("trying_skip", False)

style credits_roll_text:
    size 45
    font "fonts/Andika-Regular.ttf"
    color "#ffffff"
    outlines [(1, "#000", 0, 0)]

style thank_you_text:
    size 47
    font "fonts/Andika-Regular.ttf"
    color "#ffffff"
    outlines [(1, "#000", 0, 0)]
    line_spacing 10

transform credits_roll_effect:
    subpixel True
    yalign 0.0
    linear 71.0 yalign 1.0



image credit_anim_bg = Movie(play = "images/utility/credit_anim/credit_anim_bg.webm", start_image = "credit-first-frame", image = "credit-first-frame", loop = False)



image thank_you = Text(_("Thank you for playing the game!"), style="credit_start_text")
image week_three = Text(_("We'll see you soon!"), style="credit_start_text")
image freelanceTranslatorIntroduce = Text(_("Russian localization - Bada774"), style="freelanceTraslatorIntroduceStyle")
image freelanceTranslatorSteam = Text("({a=https://steamcommunity.com/id/bada774/)}Steam{/a})", style="freelanceTraslatorIntroduceStyle")


image writer1 = Text("Theo Malt", style="team_memeber_name")
image writer2 = Text("Oddity", style="team_memeber_name")
image writer3 = Text("Wildquill", style="team_memeber_name")
image writer4 = Text("Riverrun\n   Studios", style="team_memeber_name")
image writer5 = Text("Venus", style="team_memeber_name")
image writer6 = Text("Vi", style="team_memeber_name")
image writer7 = Text("Krash", style="team_memeber_name")


image artist1 = Text("Venus", style="team_memeber_name")
image artist2 = Text("BlackMoon", style="team_memeber_name")
image artist3 = Text("Hooli", style="team_memeber_name")
image artist4 = Text("Wise2face", style="team_memeber_name")
image artist5 = Text("Mer", style="team_memeber_name")
image artist6 = Text("Melody", style="team_memeber_name")
image artist7 = Text("Raur", style="team_memeber_name")
image artist8 = Text("Fenrir", style="team_memeber_name")
image artist9 = Text("Xlore", style="team_memeber_name")
image artist10 = Text("Kaim", style="team_memeber_name")
image artist11 = Text("Vi", style="team_memeber_name")


image coder1 = Text("RockStar8", style="team_memeber_name")
image coder2 = Text("LoudLout", style="team_memeber_name")
image coder3 = Text("Venus", style="team_memeber_name")
image coder4 = Text("Vi", style="team_memeber_name")


image sound1 = Text("LoudLout", style="team_memeber_name")


image music1 = Text("Mike Zimean", style="team_memeber_name")
image music2 = Text("Vitali Ezekiev", style="team_memeber_name")
image music3 = Text("Loudlout", style="team_memeber_name")
image music4 = Text("Eric Graham", style="team_memeber_name")



image tester1 = Text("Simfer", style="special_credit_name")
image tester2 = Text("Da Sechs", style="special_credit_name")
image tester3 = Text("Grubb", style="special_credit_name")



image special1 = Text("Zairus", style="special_credit_name")
image special2 = Text("Lovense", style="special_credit_name")
image special3 = Text("Infernozilla", style="special_credit_name")



style team_memeber_name:
    size 90
    font "fonts/new/KaushanScript-Regular.ttf"
    color "#cc0066"
    outlines [(2, "#61192b", 2, 2)]
    line_spacing -30

style special_credit_name:
    size 80
    font "fonts/new/KaushanScript-Regular.ttf"
    color "#ffffff"
    outlines [(2, "#444444", 2, 2)]

style credit_start_text:
    size 90
    font "fonts/Andika-Regular.ttf"
    color "#f4426b"
    outlines [(2, "#61192b", 2, 2)]
    text_align 0.5

style freelanceTraslatorIntroduceStyle:
    size 90
    font "fonts/Andika-Regular.ttf"
    color "#ffffff"
    outlines [(2, "#61192b", 2, 2)]
    text_align 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
