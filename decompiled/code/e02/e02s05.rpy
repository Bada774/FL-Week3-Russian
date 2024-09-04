label e02s05:

    $ e02s05_cycle = 0
    $ e02s05_6 = False
    $ e02s05_7 = False
    $ e02s05_8 = False

    scene black
    show screen scene_transistion(_("Later that day"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play voice2 d7s4_mcbreathing fadein 1.5
    play voice3 [lissa_moan2, "<silence 1.0>", lissa_moan3, "<silence 1.0>", lissa_moan4, "<silence 1.0>", lissa_moan5, "<silence 1.0>", lissa_moan1, "<silence 1.0>"] fadein 1.5
    play sound sfx_sex_bodyslaps1 loop volume 0.6

    $ Lovense.stop()

    scene e02s05-01 mc-mh-sex1_c1
    $ Lovense.pattern("7;11", 1700)
    with Fade(0.5, 0.5, 0.5)
    pause
    mc "You want it harder?"
    scene e02s05-01 mc-mh-sex1_c2 with dissolve
    mh "I do, keep going, you're going to make me cum."
    mc "I can feel your asshole twitching."
    mh "That's because you're hitting me in just the right spot."
    mh "There, there!"
    play voice3 lissa_moan9 noloop
    play voice2 d1s5_orgasm2 noloop
    stop sound fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(16)
    scene e02s05-01 mc-mh-sex1_c3 with hpunch
    pause
    $ renpy.music.set_volume(0.4, 1.0, "music" )
    $ Lovense.vibrate(2)
    play music music_everybody_got_aproblem
    scene e02s05-02 mc-mh-getup_c2 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "You want to do it on the bed next time?"
    $ Lovense.vibrate(1)
    scene e02s05-02 mc-mh-getup_c1 with dissolve
    play voice3 polly_breathing noloop
    mh "Give me a minute. I need to drink some water."
    call buzz from _call_buzz_46
    scene e02s05-02-2 mc-mh-getup2_c2 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Let me get this."
    scene e02s05-02-2 mc-mh-getup2_c1 with dissolve
    play voice3 lissa_thinking noloop
    mh "Probably just Oliver."

    $ Lovense.stop()

    scene e02s05-03 mc-mh-phone1_c1 with dissolve
    play voice2 mc_no_no2 noloop
    mc "No, it's a few text messages from Angela."
    scene e02s05-03 mc-mh-phone1_c2 with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    mh "What did she say?"
    play sound sfx_drink_loop1 volume 1.5
    scene e02s05-04 mc-mh-drink_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "She's asking where we are and says she wants to talk to us."
    stop sound fadeout 1.0
    scene e02s05-03 mc-mh-phone1_c2 with dissolve
    play voice3 dahlia_arrogant_huh noloop
    mh "Already?"
    play voice2 mc_yes_yeah2 noloop
    mc "I guess. These texts are from over an hour ago. Let me message her."
    play sound sfx_message_out1
    mct "Sorry for not responding. Where are you?"
    scene e02s05-04 mc-mh-drink_c2 with dissolve
    play voice3 lissa_oh noloop
    mh "Oh, they're all probably at the meeting."
    play sound sfx_drink_loop1 volume 1.3
    scene e02s05-04 mc-mh-drink_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah... We lost track of time."
    stop sound fadeout 1.0
    scene e02s05-03 mc-mh-phone1_c2 with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    mh "Let's shower and go see what's happening."
    play voice2 mc_happy_hah2 noloop
    mc "Work, work, work..."
    play voice3 lissa_lno noloop
    mh "JUST a shower. We're already late."
    play sound sfx_drink_loop1
    scene e02s05-04 mc-mh-drink_c1 with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "Oh, fine."
    stop sound fadeout 1.0

    $ renpy.music.set_volume(0.8, 1.5, "music" )
    jump e02s05_later

label e02s05_later:

    scene black
    show screen scene_transistion(_("One more shower later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.4, 3.0, "music" )
    play sound4 sfx_fire_fireplace1 fadein 3.0 volume 0.7
    $ renpy.music.set_volume(1.0, 0.0, "sound4" )
    scene e02s05-11 mc-mh-entry_c2
    with Fade(0.5, 0.5, 0.5)
    pause
    play voice4 girl12_no_nope1 noloop
    dn "I'm not sure there is any point to this."
    scene e02s05-11 mc-mh-entry_c4 with dissolve
    play voice5 claudie_thinking_hmm2 noloop
    ac "It seems like Frank and I are the only ones sharing."
    scene e02s05-11 mc-mh-entry_c3 with dissolve
    play voice6 girl23_yes_yeeeah2 noloop
    atp "I would share if I could. I just don't have any idea what's wrong."
    scene e02s05-12 mc-mh-ac-fc-dn-ms-ap-atp-entry2_c4 with dissolve
    play voice4 boy5_thinking_oh noloop
    fc "Oh, c'mon. How could that be?"
    scene e02s05-11 mc-mh-entry_c3 with dissolve
    play voice5 boy4_no_simple noloop
    ap "No, she's right. Something feels off, but I couldn't tell you what it is."
    scene e02s05-11 mc-mh-entry_c1 with dissolve
    play voice6 girl12_yes_aga5 noloop
    dn "That sounds familiar."
    scene e02s05-12 mc-mh-ac-fc-dn-ms-ap-atp-entry2_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hey, everyone."
    mc "I hope you don't mind if we join you."
    play voice3 lissa_ugu noloop
    mh "We were kinda invited, but don't want to interrupt."
    scene e02s05-12 mc-mh-ac-fc-dn-ms-ap-atp-entry2_c4 with dissolve
    play voice4 boy5_no_high noloop
    fc "No problem. The more, the merrier."
    mct "I hope everyone feels that way."
    fc "Why don't you two sit down and get started."
    play sound sfx_cloth_rustling4
    scene e02s05-13 mc-mh-ac-fc-dn-ms-ap-atp-talk1_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "Get started?"
    scene e02s05-13 mc-mh-ac-fc-dn-ms-ap-atp-talk1_c4 with dissolve
    play voice5 claudie_yes_aga noloop
    ac "You know. Say your names, tell us a little about yourself and your issues."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, we're not-"
    scene e02s05-18 mc-mh-ac-fc-dn-ms-ap-atp-talk6_c1 with dissolve
    play voice3 nora_hey noloop
    mh "Hi. I'm Melissa Harris and this is my boyfriend, [mcname]."
    scene e02s05-17 mc-mh-ac-fc-dn-ms-ap-atp-talk5_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "Okay... I guess we're doing this."
    scene e02s05-19 mc-mh-ac-fc-dn-ms-ap-atp-talk7_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Her friends call her Lyssa."
    scene e02s05-19 mc-mh-ac-fc-dn-ms-ap-atp-talk7_c5 with dissolve
    play voice4 boy5_hey_calm noloop
    fc "Hi [mcname], Hello Lyssa."
    scene e02s05-20 mc-mh-ac-fc-dn-ms-ap-atp-talk8_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "We've been together for a little while now. I'd say we have a happy and healthy relationship."
    scene e02s05-20 mc-mh-ac-fc-dn-ms-ap-atp-talk8_c2 with dissolve
    play voice3 lissa_aga noloop
    mh "Definitely. We've both had bad experiences in the past, but we've learned from them."
    play voice2 mc_yes_yes1 noloop
    mc "I guess that's why we're here today."
    mh "We just want to listen and see if we can help."
    mc "And if we can't help, you guys can pretend like we aren't here."
    scene e02s05-19 mc-mh-ac-fc-dn-ms-ap-atp-talk7_c5 with dissolve
    play voice4 boy5_arrogant_hm noloop
    fc "Sure, that sounds good. Why don't we all go around."
    scene e02s05-13 mc-mh-ac-fc-dn-ms-ap-atp-talk1_c2 with dissolve
    play voice5 boy4_thinking_emm3 noloop
    ap "I guess we can start-"
    play voice5 girl23_hey_hi noloop
    scene e02s05-20 mc-mh-ac-fc-dn-ms-ap-atp-talk8_c4 with dissolve
    atp "I'm Angela Taylor-Portillo."
    atp "But you already knew that."
    atp "As for the rest of you, I'm basically the person that runs Channel Six and its sister broadcasts."
    scene e02s05-15 mc-mh-ac-fc-dn-ms-ap-atp-talk3_c2 with dissolve
    play voice4 boy4_disappointed_ehh2 noloop
    ap "Hun, I don't-"
    play voice5 girl23_thinking_hmm1 noloop
    atp "And this is my husband, Alexander."
    ap "Alexander Portillo."
    atp "You may have seen him on TV covering the news."
    play sound sfx_cloth_rustling2
    scene e02s05-18 mc-mh-ac-fc-dn-ms-ap-atp-talk6_c4 with dissolve
    play voice4 boy4_yes_confident noloop
    ap "Uh, yeah. If you live in our city. I pretty much just cover local news."
    scene e02s05-15 mc-mh-ac-fc-dn-ms-ap-atp-talk3_c4 with dissolve
    play voice6 boy5_thinking_huh noloop
    fc "Nice. I'm Frank Cooper, and this lovely and talented lady is my wife Ashley."
    play voice5 claudie_hey_simple noloop
    ac "Hi."
    fc "We're happily married, but experiencing some... what would you call it, hon?"
    scene e02s05-14 mc-mh-ac-fc-dn-ms-ap-atp-talk2_c4 with dissolve
    play voice5 claudie_thinking_emm noloop
    ac "You could call them bumps. Or one big erratic bump."
    play voice6 boy5_thinking_hmm1 noloop
    fc "Erratic seems a bit too much. And I actually thought things were growing stale."
    play voice5 claudie_thinking_hmm1 noloop
    ac "That just means we should be trying new things."
    ac "Maybe not exactly the one you want right this moment."
    ac "But other things."
    scene e02s05-13 mc-mh-ac-fc-dn-ms-ap-atp-talk1_c4 with dissolve
    play voice6 boy5_arrogant_hah noloop
    fc "I still don't think I'm being erratic."
    play voice5 claudie_thinking_hmm4 noloop
    ac "At one point on this trip, you said you might get a job and go back to college to help support a child."
    play voice6 boy5_yes_questioning noloop
    fc "I can do two things at once."
    scene e02s05-14 mc-mh-ac-fc-dn-ms-ap-atp-talk2_c2 with dissolve
    play voice4 girl23_yes_yeah noloop
    atp "I think we get the point."
    scene e02s05-16 mc-mh-ac-fc-dn-ms-ap-atp-talk4_c1 with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    mh "What about you two? It's Dorothy and Mikaela, right?"
    scene e02s05-18 mc-mh-ac-fc-dn-ms-ap-atp-talk6_c3 with dissolve
    play voice5 cynthia_thinking_oh noloop
    ms "Oh, we get along like a house on fire."
    scene e02s05-16 mc-mh-ac-fc-dn-ms-ap-atp-talk4_c3 with dissolve
    play voice4 girl12_yes_yeah1 noloop
    dn "Yeah. We communicate well and don't have any issues except for some physiological-"
    play voice5 cynthia_yes_yeah1 noloop
    ms "We are mostly here because of the insurance."
    scene e02s05-22 mc-mh-ac-fc-dn-ms-ap-atp-talk10_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.5
    mc "What does that mean?"
    scene e02s05-14 mc-mh-ac-fc-dn-ms-ap-atp-talk2_c3 with dissolve
    play voice4 girl12_disappointed_mff4 noloop
    dn "The insurance company won't explore other alternatives unless we go to therapy and rule out psychological issues."
    play voice5 cynthia_arrogant_hm noloop
    ms "Which is why I was saying this is kinda pointless for us. No therapist, so none of this counts as far as the insurance is concerned."
    scene e02s05-19 mc-mh-ac-fc-dn-ms-ap-atp-talk7_c1 with dissolve
    play voice2 mc_surprised_wow2 noloop
    mc "Wow, that's kinda fucked up."
    scene e02s05-18 mc-mh-ac-fc-dn-ms-ap-atp-talk6_c3 with dissolve
    play voice4 girl12_hey_greeting noloop
    dn "Hey, at least we're having a nice vacation."
    play voice5 cynthia_yes_aga noloop
    ms "And insurance is covering part of the expense of coming here."
    scene e02s05-20 mc-mh-ac-fc-dn-ms-ap-atp-talk8_c3 with dissolve
    play voice4 girl12_surprised_oh2 noloop
    dn "Or they were when they thought the therapist would be here."
    scene e02s05-18 mc-mh-ac-fc-dn-ms-ap-atp-talk6_c1 with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    mh "Interesting. I'd love to hear more about your issues, if you're okay with sharing."
    scene e02s05-20 mc-mh-ac-fc-dn-ms-ap-atp-talk8_c4 with dissolve
    play voice5 girl23_yes_yeppers noloop
    atp "I'm sure we'd all love that, but we've been going at this for a while now."
    scene e02s05-20 mc-mh-ac-fc-dn-ms-ap-atp-talk8_c5 with dissolve
    play voice6 claudie_yes_yeah1 noloop
    ac "True. I'm getting hungry."
    scene e02s05-22 mc-mh-ac-fc-dn-ms-ap-atp-talk10_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Oh, of course. I'm sorry we showed up so late."
    play voice3 daisy_ugu noloop
    mh "We were kinda indisposed and lost track of time."
    play sound sfx_skirt_off2
    scene e02s05-22 mc-mh-ac-fc-dn-ms-ap-atp-talk10_c3 with dissolve
    play voice4 cynthia_hey_happy noloop
    ms "We'd be happy to talk to you guys anytime, but in a more relaxed setting."
    scene e02s05-22 mc-mh-ac-fc-dn-ms-ap-atp-talk10_c4 with dissolve
    play voice5 girl12_yes_yeah2 noloop
    dn "Yeah. You all seem like interesting people, but we're just going to try to enjoy our trip."
    scene e02s05-22 mc-mh-ac-fc-dn-ms-ap-atp-talk10_c1 with dissolve
    play voice3 lissa_ugu2 noloop
    mh "Of course, I'm sure we all know how to get in touch with each other."
    scene e02s05-22 mc-mh-ac-fc-dn-ms-ap-atp-talk10_c3 with dissolve
    play voice4 cynthia_thinking_hmm5 noloop
    ms "We're usually on the slopes or in the sauna."
    play voice2 mc_arrogant_heh3 noloop
    mc "Sounds like fun."
    play sound sfx_cloth_rustling2
    scene e02s05-22 mc-mh-ac-fc-dn-ms-ap-atp-talk10_c5 with dissolve
    play voice5 boy5_thinking_hmm3 noloop
    fc "Don't be a stranger."
    play sound sfx_heels_steps1 loop
    play sound3 sfx_heels_steps2
    scene e02s05-23 mc-mh-ac-fc-dn-ms-ap-atp-leave_c2 with dissolve
    play voice6 boy4_thinking_mmm2 noloop
    ap "I hope they have more of those gourmet burgers tonight."
    stop sound fadeout 1.0
    stop sound3 fadeout 1.0
    stop sound4 fadeout 1.0

    jump e02s05_menu

label e02s05_menu:

    $ e02s05_cycle += 1

    if e02s05_cycle == 1:
        $ renpy.music.set_volume(0.25, 3.0, "music" )
        scene e02s05-24 mc-mh-bed1_c1 with Fade(0.5, 0.5, 0.5)
        play sound sfx_cloth_rustling4
        play voice2 mc_happy_oof3 noloop
        mc "That was amazing."
        play voice3 lissa_mmm1 noloop
        mh "You're always amazing."
        scene e02s05-24 mc-mh-bed1_c2 with dissolve
        play voice2 mc_thinking_mmm1 noloop
        mc "Only when I'm with you."
        scene e02s05-24 mc-mh-bed1_c3 with dissolve
        play voice3 lissa_ha noloop
        mh "Ha! I like that."
        play voice2 d1s5_mchappy noloop volume 1.5
        mc "Up for another round?"
        scene e02s05-24-2 mc-mh-bed2_c1 with dissolve
        play voice3 lissa_thinking noloop volume 1.4
        mh "Actually... I had something else in mind."
        play voice2 d2s9_confused noloop volume 1.4
        mc "What's that?"
        scene e02s05-24-3 mc-mh-bed3_c1 with dissolve
        play voice3 lissa_moan3 noloop
        mh "First, we get something to eat. I'm famished."
        play voice2 mc_happy_thatsgood noloop
        mc "Oh, that is a good idea."
        scene e02s05-24-4 mc-mh-bed4_c1 with dissolve
        play voice3 dahlia_happy_hmm2 noloop
        mh "Then we track down one of those couples and hang out with them."
        play voice2 mc_yes_okay1 noloop
        mc "Okay. Let's do that tomorrow. Which one?"
        scene e02s05-24-5 mc-mh-bed5_c1 with dissolve
        play voice3 dahlia_thinking_hmm1 noloop
        mh "You can decide."
    elif e02s05_cycle == 2:
        scene e02s05-25 mc-mh-coffee1_c1 with Fade(0.5, 0.5, 0.5)
        play voice2 d1s5_mchappy noloop volume 1.7
        mc "So, what do you want to do tomorrow, Brain?"
        scene e02s05-25 mc-mh-coffee1_c2 with dissolve
        play voice3 lissa_laugh2 noloop
        mh "Same thing we do every night, Pinky."
        scene e02s05-26 mc-mh-coffee2_c1 with dissolve
        play voice2 mc_scared_oh1 noloop
        mc "Try to take over the world?"
        scene e02s05-26 mc-mh-coffee2_c2 with dissolve
        play voice3 dahlia_no_nope noloop
        mh "Nope. I was thinking we could meet with another one of those couples."
        scene e02s05-28 mc-mh-coffee3_c1 with dissolve
        play voice2 mc_thinking_mmm4 noloop
        mc "Hmm. I was kinda hoping to take over the world."
        play sound sfx_drink_slurp2
        scene e02s05-28 mc-mh-coffee3_c2 with dissolve
        play voice3 lissa_mmm1 noloop
        mh "Maybe I can rock your world..."
    elif e02s05_cycle == 3:
        $ renpy.music.set_volume(0.6, 0.0, "sound4" )
        play sound4 sfx_water_jacuzzi fadein 3.0
        scene e02s05-30 mc-mh-tub1_c1 with Fade(0.5, 0.5, 0.5)
        play voice3 lissa_ha noloop
        mh "Guess what."
        scene e02s05-30 mc-mh-tub1_c2 with dissolve
        play voice2 mc_arrogant_heh1 noloop
        mc "Chicken butt."
        scene e02s05-30 mc-mh-tub1_c3 with dissolve
        play voice3 lissa_lno noloop
        mh "No, silly. Guess what I want to do tomorrow."
        scene e02s05-30 mc-mh-tub1_c2 with dissolve
        play voice2 mc_disappointed_off1 noloop
        mc "It's pretty obvious, there's one couple we haven't spent time with yet."
        scene e02s05-31 mc-mh-tub2_c3 with dissolve
        play voice3 lissa_thinking noloop
        mh "Is that okay?"
        scene e02s05-31 mc-mh-tub2_c2 with dissolve
        play voice2 mc_yes_yeah2 noloop
        mc "It did feel really satisfying helping those other couples."
        play sound sfx_water_floatup1
        scene e02s05-32 mc-mh-tub3_c1 with dissolve
        play voice3 lissa_haha noloop
        mh "It's your call. We can help them or not."
    elif True:
        $ unlock_gallery_slot("cg", "e02s05")
        stop music fadeout 3.0
        jump e02s09

    menu:
        "Spend Time with the Coopers"(hint="e02s05m01c01") if e02s05_6 is False:
            $ e02s05_6 = True
            stop music fadeout 3.0
            stop sound4 fadeout 3.0
            jump e02s06

        "Spend Time with the lesbian couple"(hint="e02s05m01c02") if e02s05_7 is False:
            $ e02s05_7 = True
            stop music fadeout 3.0
            stop sound4 fadeout 3.0
            jump e02s07

        "Spend Time with the Portillos"(hint="e02s05m01c03") if e02s05_8 is False:
            $ e02s05_8 = True
            stop music fadeout 3.0
            stop sound4 fadeout 3.0
            jump e02s08

        "Enjoy Your Vacation And Go Home"(hint="e02s05m01c04") if e02s05_cycle > 1:
            stop sound4 fadeout 3.0
            stop music fadeout 3.0
            jump e02s09

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
