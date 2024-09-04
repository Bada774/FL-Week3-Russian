label e04s08:

    $ e04s08_lc_upstairs = False
    $ e04s08_lc_downstairs = False
    $ e04s08_lc_out = False

    scene black
    show screen scene_transistion(_("Another year later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound2 park fadein 2.0 volume 0.5
    scene e04s08-01 mc-jg-greeting
    with Fade(0.5, 0.5, 0.5)
    $ renpy.music.set_volume(0.6, 3.0, "music")
    queue music music_killbilly fadein 1.5
    pause
    scene e04s08-02 mc-jg-greeting-alt with dissolve
    play voice2 d2s9_mchey noloop
    mc "It is a pleasure to see you."
    play voice4 nora_aga noloop
    jdg "I bet. I take it your first prisoner is doing well?"
    play voice2 mc_yes_yes1 noloop
    mc "Indeed. If she were up for parole I'm sure any board would release her."
    play sound sfx_heels_steps2 loop
    scene e04s08-03 mc-jg-walking-talk with dissolve
    play voice4 nora_hmm noloop
    jdg "I wonder if that is what she wants."
    play voice2 d9s2_yeah noloop volume 1.7
    mc "If I have done my job properly-"
    jdg "Have you given any thought to where your prisoners will go next?"
    scene e04s08-04 mc-jg-walking-talk-alt with dissolve
    play voice2 d3s11b_mcheh noloop
    mc "I'm sure you'll provide something appropriate."
    play voice4 aaleyah_thinking_hmm3 noloop
    jdg "You're not worried about losing your favorite toy?"
    play voice2 mc_no_nah2 noloop
    mc "She is my favorite toy. I doubt she'll go far."
    scene e04s08-05 mc-jg-walking-talk-hand-shoulder with dissolve
    play voice4 nora_heh noloop
    jdg "Well, you don't have to worry about that."
    jdg "Part of her conviction turned this property over to the Court."
    play voice2 d1s2_hmm noloop volume 1.7
    mc "So I can keep using it as a prison?"
    scene e04s08-06 mc-jg-talk-stop-hand-shoulder with dissolve
    play voice4 aaleyah_yes_aga4 noloop
    jdg "Indeed. I wouldn't have given you so many female prisoners otherwise."
    play voice2 mc_arrogant_hm1 noloop
    mc "Excellent. How long will this last?"
    jdg "As long as you continue to impress me."
    scene e04s08-07 mc-jg-talk-smile with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Excellent."
    if date_mh is True and e04s06_mk_available is True:
        $ unlock_gallery_slot("extra", "e04s08n01")
        $ fl_achievement_unlock("e04s08n01")
    stop sound2 fadeout 2.0
    stop sound fadeout 1.0
    scene e04s08-08 sy-arj-talk-walk with dissolve
    queue sound sfx_heels_steps1 loop volume 0.6
    play voice3 stacy_disappointed_ehh2 noloop
    sy "It's almost a shame she's getting released today."
    sy "Almost nothing is quite as enjoyable as torturing her."
    scene e04s08-09 sy-arj-talk-walk-alt with dissolve
    play voice5 amrose_arrogant_huh2 noloop
    arj "Isn't there anything we can do? Can't she stay here as a willing prisoner like I am?"
    play voice3 stacy_yeahno noloop
    sy "I don't know. Above my pay grade."
    scene e04s08-10 sy-arj-talk-walk-behind-closer with dissolve
    play voice5 amrose_happy_mmm noloop
    arj "That's a shame. I'm going to miss her."
    play voice3 stacy_happy_hmm1 noloop
    sy "It's between the warden and the judge, I guess. Maybe she has a say in that too."
    stop sound fadeout 1.0
    scene e04s08-11 sy-arj-lc-talk-stop-cage with dissolve
    play voice3 stacy_yes_fine4 noloop
    sy "Alright, let's get you out of there."
    sy "Prisoner 001! The Judge is here. You're getting released."
    play voice6 lydia_moan1 noloop
    lc "Huh?"
    play sound sfx_keys_jingle1
    scene e04s08-12 sy-arj-lc-pov-opening-cage with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "You've served out your sentence. You're going to be a free woman."
    play voice6 lydia_morningoh noloop
    lc "Oh."
    play voice3 stacy_thinking_well1 noloop
    sy "Well, once we get you to the Warden."
    play sound sfx_jail_door_open1
    scene e04s08-13 sy-arj-lc-pov-talk-cage-open with dissolve
    play voice6 lydia_ah noloop
    lc "[alt_mcname]? Of course! Right away!"
    play voice3 stacy_arrogant_huh3 noloop
    sy "Good girl. Let's go."
    scene e04s08-14 sy-arj-lc-mc-jdg-pov-talk-hidden with dissolve
    play voice3 stacy_hey_attention1 noloop
    sy "I brought you the prisoner scheduled for release."
    play voice2 mc_yes_yeah2 noloop
    mc "Well done."
    play voice4 aaleyah_thinking_hmm2 noloop
    jdg "Why is the other one here?"
    scene e04s08-15 sy-arj-lc-mc-jdg-pov-talk-show with dissolve
    play voice3 stacy_arrogant_huh2 noloop
    sy "Prisoner 002? She follows me around wherever I go, like a faithful puppy."
    play voice4 aaleyah_disappointed_mff noloop
    jdg "I see."
    play voice2 d1s5_mchappy noloop volume 1.5
    mc "She's one of the willing prisoners. There's no risk involved."
    scene e04s08-16 lc-mc-jdg-pov-talk-move-forward with dissolve
    play voice4 aaleyah_yes_aga1 noloop
    jdg "Very well. Let's get this started."
    play voice2 mc_angry_cough1 noloop
    mc "Prisoner 001 - Stand and face the Judge."
    scene e04s08-17 lc-mc-jdg-pov-talk-stand with dissolve
    play voice4 aaleyah_thinking_hmm1 noloop
    jdg "Very good. Lydia Cox, you have served out the term of your sentence."
    jdg "I have signed your release papers and you are free to leave."
    scene e04s08-18 lc-mc-jdg-pov-talk-stand-alt with dissolve
    play voice5 lydia_oops noloop
    lc "[alt_mcname]? I don't understand. What's happening?"
    play voice2 mc_hey_hey3 noloop
    mc "You are getting your freedom. You are no longer a prisoner here."
    scene e04s08-19 lc-mc-jdg-pov-talk-face-judge with dissolve
    play voice4 nora_angrymoan noloop volume 1.4
    jdg "Now, there can be some difficulties re-entering society, but having reviewed your finances I am confident that you have the necessary means."
    jdg "You're a rather wealthy woman, Miss Cox."
    scene e04s08-20 lc-mc-jdg-pov-talk-mc-bored-looking-distance with dissolve
    play voice4 aaleyah_happy_mmm1 noloop
    jdg "I know an excellent lawyer who is also involved in real estate."
    jdg "I'll convince her to help you reacclimate to normal life."
    if date_mh is True:
        play sound sfx_throw_something1
        scene e04s08-22 mh-ah-paddle-hold-lock-up-bdsm with dissolve
        play voice4 aaleyah_surprised_oh noloop
        jdg "Oh, there she is now."
        jdg "Hmm. Looks like she is occupied at the moment."
    scene e04s08-23 lc-mc-jdg-pov-talk-alt-continue with dissolve
    play voice4 aaleyah_thinking_hmm3 noloop
    jdg "She will call you tomorrow."
    play voice2 d1s5_mcthinks noloop volume 1.7
    mc "Is that everything?"
    jdg "I just need to return her personal effects and make sure she is properly dressed."
    mc "Alright. After that we can walk her out."
    scene e04s08-24 lc-mc-jdg-pov-talk-face-each-other with dissolve
    play voice4 aaleyah_disappointed_eeh noloop
    jdg "Would you mind doing that? I would like to spend some time inspecting the prisoners."
    play voice2 mc_yes_sure1 noloop
    mc "Certainly. Enjoy yourself."
    jdg "Thank you. I certainly will."

    jump e04s08_outside

label e04s08_outside:

    play sound sfx_door_openclosed1
    play sound2 park fadein 2.0 volume 0.5
    scene e04s08-31 lc-mc-pov-lc-talk with Fade(0.5, 0.5, 0.5)
    play voice2 vumc_smell noloop
    mc "Give yourself a minute to get used to the sunlight."
    mc "You haven't seen it in a while, have you?"
    scene e04s08-32 lc-mc-talk-pov-lc-mc-turn with dissolve
    play voice3 lydia_lydyes noloop
    lc "It has been a while, [alt_mcname]."
    lc "I believe my eyes have adjusted."
    scene e04s08-33 lc-mc-talk-pov-lc-mc-look-away with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "I believe you remember the way from here."
    mc "There will be a taxi just outside the gate. It will take you anywhere you want."
    mc "At this hour, I recommend getting a hotel."
    scene e04s08-34 lc-mc-talk-pov-lc-feet-walk-away with dissolve
    play voice3 daisy_ugu noloop
    lc "Oh, um, okay."
    lc "Thank you, [alt_mcname]."
    play sound sfx_heels_steps1_slow loop
    scene e04s08-35 lc-mc-talk-pov-lc-walk-towards-exit-gate with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    lc "I'll just be going then."
    scene e04s08-36 lc-mc-talk-pov-lc-remember-pool with dissolve
    lc "I'll just be going..."
    play voice3 dahlia_happy_hmm1 noloop
    lc "Heh. [alt_mcname] tried to drown me there when I first got here."
    scene e04s08-37 lc-mc-talk-pov-lc-walk-continue with dissolve
    lc "When I first got here."
    play voice3 lydia_oof noloop
    lc "I almost forgot that I used to live here before it was a prison."
    scene e04s08-38 lc-mc-talk-pov-lc-stop-look-at-ground with dissolve
    lc "Before it was his prison."
    lc "Before I was his."
    stop sound fadeout 1.0
    scene e04s08-39 lc-mc-wide-shot-lc-stop with dissolve
    play voice3 dahlia_pain_mmh noloop
    lc "This isn't right."
    lc "I can't do this."
    play sound sfx_heels_run2 loop
    scene e04s08-40 lc-mc-pov-lc-running-back with dissolve
    mct "What is this?"
    play voice2 mc_hey_hey2 noloop
    mc "Did you forget something?"
    play sound sfx_bed_fall1
    scene e04s08-41 lc-mc-pov-on-floor-begging with dissolve
    play voice3 dahlia_pain_sobs noloop
    lc "Don't make me go. Please don't make me go."
    lc "I can't imagine life without you."
    scene e04s08-41-02 lc-mc-pov-on-floor-crying-beg with dissolve
    play voice3 dahlia_pain_ah2 noloop
    lc "I don't want to live without you."
    lc "Please let me stay."
    play voice2 mc_angry_errr4 noloop
    mc "Lydia Cox - Get Up Now!"
    play sound sfx_cloth_rustling2
    scene e04s08-42 lc-mc-lc-stand-mc-hold-shoulders-lc-look-away with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "Look At Me!"
    scene e04s08-43 lc-mc-lc-stand-mc-pov-hold-shoulders-decision with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "What am I going to do with you?"
    $ unlock_gallery_slot("cg", "e04s01")
    menu:
        "Bring Lydia Upstairs to Her Bedroom"(hint="e04s08m01c01"):
            $ e04s08_lc_upstairs = True
            jump e04s08_upstairs
        "Bring Lydia Downstairs to Her Cage"(hint="e04s08m01c02"):

            $ e04s08_lc_downstairs = True
            jump e04s08_downstairs
        "Kick Lydia Out"(hint="e04s08m01c03"):

            $ e04s08_lc_out = True
            jump e04s08_bad_end

label e04s08_upstairs:

    mct "That's my girl."
    mct "She is finally completely mine."
    scene e04s08-44 lc-mc-ending-wide-shot-kiss with dissolve
    play voice2 d1s5_orgasm noloop
    play voice3 dahlia_sex_closedmoan2 noloop
    play sound dahlia_kiss_french1
    pause
    scene e04s08-44-02 lc-mc-alt-ending-wide-shot-tell-to-kiss-foot with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "C'mon, Lydia. Let's go inside."
    mc "I've kept your bedroom just the way you left it."
    play sound sfx_heels_steps1
    scene e04s08-45 lc-mc-ending-wide-shot-walk-inside with dissolve
    pause
    stop sound fadeout 2.0
    scene e04s08-46 lc-mc-ending-wide-shot-end with dissolve
    pause

    jump e04s08_end

label e04s08_downstairs:

    scene e04s08-44-02 lc-mc-alt-ending-wide-shot-tell-to-kiss-foot with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Kiss my foot prisonar 001"
    scene e04s08-45-02 lc-mc-ending-alt-kiss-shoe with dissolve
    play voice3 daisy_dlick noloop volume 2.0
    play sound maria_kiss1
    pause
    play voice2 mc_yes_okay2 noloop
    mc "Allright, prisoner. Let's go inside."
    mc "We'll get you out of those clothes and back in your cage."
    play sound sfx_heels_steps1 loop
    scene e04s08-46-02 lc-mc-ending-alt-crawl-inside with dissolve
    pause
    stop sound fadeout 2.0
    scene e04s08-46 lc-mc-ending-wide-shot-end with dissolve
    pause

    jump e04s08_end

label e04s08_bad_end:

    scene e04s08-47 lc-mc-lc-bad-end-wide-shot-standing with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Consider this your final punishment."
    mc "Leave.{w} You are no longer welcome here."
    play sound sfx_cloth_rustling1
    scene e04s08-48 lc-mc-lc-bad-end-wide-shot-push-away with dissolve
    play voice2 mc_angry_hm2 noloop
    mc "Do not return."
    mc "I never want to see your face again."
    play sound sfx_heels_steps2 loop
    scene e04s08-49 lc-mc-lc-bad-end-wide-shot-watch-walk-away with Dissolve(1.0)
    pause
    scene e04s08-50 lc-mc-lc-bad-end-wide-shot-walk-away-inside with Dissolve(1.0)
    pause
    scene e04s08-51 lc-mc-lc-bad-end-wide-shot-walk-away-stairs-mc-gone with Dissolve(1.0)
    pause
    play sound sfx_fall_down1 volume 0.5
    scene e04s08-52 lc-bad-end-wide-shot-collapse with Dissolve(1.0)
    play voice3 dahlia_pain_ah3 noloop
    pause
    stop sound2 fadeout 4.0
    $ renpy.music.set_volume(1.0, 0.0, "sound3")
    play sound3 parknight fadein 4.0 volume 0.7
    scene e04s08-53 lc-bad-end-wide-shot-collapse-darker with Dissolve(2.0)
    play voice3 allison_pain_sniff1 noloop
    pause
    play sound sfx_cloth_rustling1
    scene e04s08-54 lc-bad-end-wide-shot-kneel-over with Dissolve(2.0)
    pause
    play sound sfx_cloth_rustling4 volume 2.0
    scene e04s08-55 lc-bad-end-wide-shot-lay-down with Dissolve(2.0)
    pause
    play sound sfx_camera_fly1
    scene e04s08-56 lc-bad-end-wide-shot-gone with Dissolve(2.0)
    stop sound fadeout 1.0
    pause

    jump e04s08_end

label e04s08_end:

    play sound sfx_camera_fly1 volume 3.0
    stop sound3 fadeout 2.5
    play sound2 ["<silence 1.8>", sfx_jail_door_open1] noloop volume 0.4
    $ renpy.music.set_volume(1.0, 3.0, "music")
    if e04s08_lc_upstairs is True:
        scene ending_04_art_2b with Fade(1.25, 1.0, 1.75, color="#fff")
    elif e04s08_lc_downstairs is True:
        scene ending_04_art_2a with Fade(1.25, 1.0, 1.75, color="#fff")
    elif e04s08_lc_out is True:
        scene ending_04_art_2c with Fade(1.25, 1.0, 1.75, color="#fff")
    pause
    call end_game_text (_("You have finished playing Ending #04!")) from _call_end_game_text_14
    $ persistent.finished_e04 = True
    $ fl_achievement_unlock("e04_finish")
    stop music fadeout 3.0
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0

    jump end

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
