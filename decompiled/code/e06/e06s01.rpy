screen e06_char_choice():

    frame:
        style_prefix "prologue"
        vbox:
            xalign 0.5
            yalign 0.3
            style_prefix "prologue_fetishes"
            vbox:
                xalign 0.5
                null height 10
                text _("Choose optional characters for this ending")
                null height 150
            vbox:
                xalign 0.5
                spacing 30
                hbox:
                    xalign 0.5
                    spacing 50
                    vbox:
                        xsize 300
                        spacing 10
                        imagebutton:
                            idle "images/utility/prologue/girls/idle/dd.webp"
                            hover "images/utility/prologue/girls/hover/dd.webp"
                            selected_idle "images/utility/prologue/girls/selected/dd.webp"
                            selected_hover "images/utility/prologue/girls/hover/dd.webp"
                            action ToggleVariable("date_dd", True)
                            selected date_dd
                        text _("Daisy") style_prefix "name" xalign 0.5
                    vbox:
                        xsize 300
                        spacing 10
                        imagebutton:
                            idle "images/utility/prologue/girls/idle/mh.webp"
                            hover "images/utility/prologue/girls/hover/mh.webp"
                            selected_idle "images/utility/prologue/girls/selected/mh.webp"
                            selected_hover "images/utility/prologue/girls/hover/mh.webp"
                            action ToggleVariable("date_mh", True)
                            selected date_mh
                        text _("Lyssa") style_prefix "name" xalign 0.5

        vbox:
            xalign 0.5
            yalign 0.9
            style_prefix "prologue_yta"
            textbutton _("Continue"):
                action Jump("d21s07_harem_end")

label e06_menu_jump:

    stop music fadeout 2.0
    call start_ending_from_menu from _call_start_ending_from_menu_2
    $ mcname = persistent.mcname
    $ mclogin = persistent.mclogin
    $ cage_ntr = persistent.cage_ntr
    $ fl_watersports = persistent.fl_watersports
    $ fl_footfetish = persistent.fl_footfetish
    $ d12s05_stop = persistent.fuck_nr
    $ stop_all_sound()
    call hide_fl_points_overlay from _call_hide_fl_points_overlay_12

    if persistent.finished_e06 is True:
        $ date_dd = False
        $ date_mh = False
        call screen e06_char_choice()
    elif True:
        $ date_mh = persistent.date_mh
        $ date_dd = persistent.date_dd

    jump d21s07_harem_end

label e06s01:

    call hide_fl_points_overlay from _call_hide_fl_points_overlay_9
    scene black
    show screen scene_transistion(_("Ending #6\nQueen's Harem"))
    with Fade(0.9, 0.9, 0.9)
    pause
    hide screen scene_transistion
    scene black
    show screen scene_transistion(_("Later That Day"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.6, 0.0, "music" )
    $ renpy.music.set_volume(1.0, 0.0, "sound")
    play sound ["<silence 0.4>", sfx_door_closed1]
    scene e06s01-01 mc-lc-entry1_c1
    play music deep_romance2 fadein 3.0
    with Fade(0.5, 0.5, 0.5)
    pause
    scene e06s01-03 mc-lc-talk1_c2 with dissolve
    play voice3 lydia_lydiahey noloop
    lc "What's wrong?"
    scene e06s01-03 mc-lc-talk1_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "Nothing?"
    $ renpy.music.set_volume(0.5, 4.0, "music" )
    scene e06s01-04 mc-lc-talk2_c2 with dissolve
    play voice3 lydia_hmmmm noloop
    lc "Come on. You can tell me."
    scene e06s01-04 mc-lc-talk2_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Just a little jittery, I guess."
    play sound sfx_hair_scratch1
    scene e06s01-05 mc-lc-talk3_c1 with dissolve
    mc "I'm worried this is a dream."
    mc "Or worse, it's about to turn into a nightmare, and not the fun Tim Burton kind..."
    scene e06s01-05 mc-lc-talk3_c2 with dissolve
    play voice3 lydia_oof noloop
    lc "This is real. I'm here with you."
    lc "I'm here {i}because{/i} of you, [mcname]."
    lc "You're the only one who supported me. Who stood by me."
    scene e06s01-06 mc-lc-talk4_c2 with dissolve
    play voice3 lydia_morningoh noloop
    lc "I saw the look in that Judge's eyes each time she looked at me."
    lc "I don't think she ever believed I could be innocent. Not even at the end..."
    scene e06s01-07 mc-lc-talk5_c2 with dissolve
    lc "Boy. I... I really need to take a shower."
    scene e06s01-07 mc-lc-talk5_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh. Feisty already?"
    scene e06s01-08 mc-lc-talk6_c2 with dissolve
    play voice3 lydia_haha noloop volume 1.5
    lc "Haha. No... nothing like that. After being in that cell and then wearing these clothes again, I feel utterly disgusting."
    scene e06s01-09 mc-lc-talk7_c2 with dissolve
    lc "Make yourself at home, I'll be down shortly."
    scene e06s01-12-1 mc-lc-talk11_c2 with dissolve
    play voice3 dahlia_thinking_oh noloop volume 0.7
    lc "Oh, can you charge my phone please?"
    lc "Battery must have died while I was on the inside."
    scene e06s01-14 mc-lc-charge2_c1 with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "I will be right here."
    $ renpy.music.set_volume(0.8, 4.0, "music" )
    scene e06s01-14-2 mc-lc-talk12_c2 with dissolve
    pause
    scene e06s01-14-2 mc-lc-talk12_c1 with dissolve
    pause
    scene black
    show screen scene_transistion(_("Some time later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.5, 3.0, "music" )
    play sound sfx_heels_steps1 volume 1.4
    scene e06s01-15 mc-lc-reentry1_c2
    with Fade(0.5, 0.5, 0.5)
    pause
    stop sound fadeout 1.5
    scene e06s01-16 mc-lc-reentry2_c1 with dissolve
    play voice2 mc_happy_wow2 noloop
    mc "Wow. You look amazing."
    scene e06s01-16 mc-lc-reentry2_c2 with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    lc "Such a flatterer. I just threw this on."
    lc "Didn't want you regretting anything and leaving."
    scene e06s01-17 mc-lc-talk1_c1 with dissolve
    play voice2 mc_no_no5 noloop
    mc "That would never happen. I love you, and I'll always stand by you, Lydia."
    scene e06s01-17 mc-lc-talk1_c2 with dissolve
    play voice3 lydia_moan1 noloop
    lc "You have no idea how happy that makes me."
    play sound sfx_cloth_rustling3 volume 1.6
    scene e06s01-20 mc-lc-lap1_c2 with dissolve
    lc "Having you hold me like this. I feel safe... Like I can breathe again."
    scene e06s01-20 mc-lc-lap1_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "What's wrong?"
    scene e06s01-21 mc-lc-lap2_c2 with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop volume 0.8
    lc "I just keep playing things over in my mind."
    lc "There is no Fetish Locator without me telling Jerome about my secret."
    scene e06s01-21 mc-lc-lap2_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "You can't think like that. You didn't control the app. And once it was out, you couldn't control its spread."
    mc "It's like trying to catch a snowball after it's been tumbling downhill for ten minutes."
    scene e06s01-23 mc-lc-lap4_c1 with dissolve
    play voice3 lydia_oops noloop
    lc "I could have caught it. Maybe if I came clean to you... Instead of-"
    scene e06s01-23 mc-lc-lap4_c2 with dissolve
    play voice2 mc_no_uhuh1 noloop
    mc "We can't go back, Lydia."
    $ renpy.music.set_volume(1.0, 0.0, "sound3")
    play sound dahlia_kiss_french1
    play sound3 sfx_cloth_rustling3 noloop
    scene e06s01-24 mc-lc-kiss_c1 with dissolve
    pause
    queue sound maria_kiss2
    scene e06s01-24 mc-lc-kiss_c2 with dissolve
    pause
    call buzz from _call_buzz_44
    scene e06s01-29 mc-lc-front5_c2 with dissolve
    play voice3 lydia_thinking noloop volume 1.7
    lc "I guess my phone is alive again."
    call buzz from _call_buzz_45
    scene e06s01-31 mc-lc-phone1_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mct "And that would be mine."
    scene e06s01-30 mc-lc-phone_c2 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Good news?"
    scene e06s01-32 mc-lc-phone2_c2 with dissolve
    play voice3 dahlia_surprised_oh noloop
    lc "Not so much..."
    scene e06s01-32 mc-lc-phone2_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.3
    mc "Let's see. Messages from AmRose and Stacy. Not too surprising. One really angry rant from Hana."
    scene e06s01-33 mc-lc-phone3_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Who needs them, Lydia?"
    scene e06s01-33 mc-lc-phone3_c2 with dissolve
    play voice3 lydia_lydyes noloop
    lc "I need... I'm going to need your help with something, [mcname]..."
    scene e06s01-34 mc-lc-phone4_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Anything."
    scene e06s01-35 mc-lc-phone5_c2 with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    lc "T-there is just so much... anger. It wasn't like this during the case."
    scene e06s01-35 mc-lc-phone5_c1 with dissolve
    play voice2 d9s2_yeah noloop volume 2.2
    mc "I'm sure a lot of people expected you to get locked up."
    mc "Everything changed when the verdict came out."
    scene e06s01-36 mc-lc-phone6_c2 with dissolve
    play voice3 dahlia_old_oh noloop volume 1.4
    lc "I don't want it to change."
    scene e06s01-36 mc-lc-phone6_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "I know. You didn't want this to happen."
    mc "But the elephant in the room is that you're the one who caged my elephant."
    scene e06s01-37 mc-lc-hug1_c2 with dissolve
    play voice3 dahlia_no_high3 noloop
    lc "That wasn't me, that was Ridley. You know, the A.I."
    play sound sfx_cloth_rustling2
    scene e06s01-38 mc-lc-hug2_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "I know that and you know that. But think of all the people who won't care about the difference."
    mc "Besides... I think you enjoyed having my cock locked up in your own way. You can admit it."
    scene e06s01-38 mc-lc-hug2_c2 with dissolve
    play voice3 lydia_lydyes noloop
    lc "Yes... I liked it. Being assured that no matter what, I couldn't give in."
    lc "I was safe then. Now... Now it's out of control. I wish I never met Jerome!"
    scene e06s01-39 mc-lc-hug3_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "We were both looking for something special. And we found it, thanks to you."
    mc "The journey had some bumps, but it was a trip I'd take all over again, just to get here."
    scene e06s01-39 mc-lc-hug3_c2 with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    lc "You're the best, [mcname]."
    play sound dahlia_kiss_french1
    scene e06s01-40 mc-lc-kiss_c2 with dissolve
    pause
    play sound3 sfx_cloth_rustling4 noloop volume 2.0
    scene e06s01-45 mc-lc-hug_c2 with dissolve
    pause
    play voice3 dahlia_thinking_oh noloop volume 0.8
    lc "Speaking of bumps, I... remember what I wanted to ask you, [mcname]."
    scene e06s01-46 mc-lc-walk1_c2 with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    lc "It's Min. I can deal with everyone else calling me a liar and... worse..."
    lc "But not her. Not my best friend."
    scene e06s01-46 mc-lc-walk1_c1 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "Well... you might have to accept that forgiveness will take some time."
    scene e06s01-47 mc-lc-walk1_c2 with dissolve
    play voice3 lydia_morningoh noloop
    lc "I do. I swear I do."
    lc " But... I thought, if you came with me to meet her. Maybe she will hear me out."
    scene e06s01-47 mc-lc-walk1_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mc "Haha. You don't want to lock her up in a cage to make her listen to your side?"
    scene e06s01-48 mc-lc-walk1_c1 with dissolve
    play voice3 dahlia_no_nope noloop
    lc "Nope. And hey..."
    lc "Total forgiveness means forgiving me for keeping you that cell while I was talking."
    scene e06s01-49 mc-lc-walk_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course. Just don't be surprised if I'm more animal than man when we finally make love."
    scene e06s01-49 mc-lc-walk_c2 with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    lc "I would never hold that against you. In fact... I'm a little excited just to see what you're capable of..."
    lc "When you're... unrestrained..."
    scene e06s01-50 mc-lc-end_c2 with dissolve
    pause
    play sound sfx_skirt_off3 volume 2.0
    scene e06s01-51 mc-lc-bed1_c1 with dissolve
    pause
    scene e06s01-51 mc-lc-bed1_c2 with dissolve
    pause
    play sound sfx_cloth_rustling4
    scene e06s01-53 mc-lc-bed3_c2 with dissolve
    play voice3 lydia_moan1 noloop
    lc "Good night, my love. I know I'm making this wait unbearable for you. I just..."
    scene e06s01-53 mc-lc-bed3_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "You don't have to apologize to me, Lydia."
    mc "Good things come to those who wait."
    scene e06s01-53 mc-lc-bed3_c2 with dissolve
    play voice3 lydia_haha noloop
    lc "I promise you won't have to wait much longer..."
    play sound maria_kiss2
    $ unlock_gallery_slot("cg", "e06s01")
    scene e06s01-54 mc-lc-bed4_c1 with dissolve
    pause
    play sound sfx_cloth_rustling1 volume 1.5
    scene e06s01-55 mc-lc-sleep_c1 with dissolve
    play voice2 d14s16_smell noloop
    mc "Good night, Lydia..."

    stop music fadeout 4.0
    jump e06s02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
