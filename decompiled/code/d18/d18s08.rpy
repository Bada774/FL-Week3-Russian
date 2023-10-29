image d18s08_slap_1 = Movie(play = "images/Day-18/s08/anim/d18s08-a1-2x-60fps.webm", start_image = "d18s08-a1 tl-smacks-cl-again-anim1-01_i")
image d18s08_slap_2 = Movie(play = "images/Day-18/s08/anim/d18s08-a2-2x-60fps.webm", start_image = "d18s08-a2 tl-smacks-cl-again-anim2-01_i")

label d18s08:

    scene d18s08-01 mc-arj-hr-arive-at-room_c1 with Fade(0.6, 0.6, 0.6)
    pause
    play sound2 sfx_whip_spanking1_muffled fadein 1.5
    scene d18s08-02 gang-notices-muffled-sounds_c1 with dissolve
    "*Muffled slapping noises*"
    scene d18s08-03 hr-eavesdrop_c1 with dissolve
    pause
    scene d18s08-04 hr-explains-noises_c1 with dissolve
    play voice3 hana_hmm noloop
    hr "Someone's in there. And they're...slapping something?"
    play voice4 amrose_surprised_huh2 noloop
    arj "Slapping something?"
    stop sound2 fadeout 1.0
    scene d18s08-05 gang-listens-closer_c1 with dissolve
    play voice3 teresa_angry_argh4_muffled noloop
    "{color=#c46c93}???{/color}" "I'm {i}appalled{/i}, young lady."
    "{color=#c46c93}???{/color}" "I didn't raise you to be some common harlot!"
    scene d18s08-06 arj-suggests-its-tl_c1 with dissolve
    play voice4 amrose_thinking_hmm2 noloop
    arj "Is that Lewald? That sounds like her."
    play music action_tension_extended
    scene d18s08-a1 tl-smacks-cl-again-anim1-01_i with dissolve
    $ renpy.music.set_volume(0.6, 5.0, "music")
    pause
    scene d18s08_slap_1 with dissolve
    play voice3 [cynthia_pain_ah1, "<silence 1.3>", cynthia_pain_ah2, "<silence 0.8>", cynthia_pain_ah3, "<silence 0.9>", cynthia_scared_ah5, "<silence 1.15>", cynthia_scared_oh, "<silence 0.9>", cynthia_scared_ah3, "<silence 0.75>"]
    play sound [sfx_whip_slap1, "<silence 1.15>", sfx_whip_slap3, "<silence 1.1>", sfx_whip_slap4, "<silence 1.2>", sfx_whip_slap5, "<silence 1.15>", sfx_whip_slap6, "<silence 1.0>"] loop
    pause
    scene d18s08_slap_2 with dissolve
    play voice3 [cynthia_pain_ah1, "<silence 1.3>", cynthia_pain_ah2, "<silence 0.8>", cynthia_pain_ah3, "<silence 0.8>", cynthia_scared_ah5, "<silence 1.08>", cynthia_scared_oh, "<silence 0.9>", cynthia_scared_ah3, "<silence 0.63>"]
    play sound [sfx_whip_slap1, "<silence 1.15>", sfx_whip_slap3, "<silence 1.0>", sfx_whip_slap4, "<silence 1.1>", sfx_whip_slap5, "<silence 1.15>", sfx_whip_slap6, "<silence 1.0>"] loop
    pause
    "{color=#54b25a}???{/color}" "*Pained whimpering*"
    stop sound fadeout 0.5
    stop voice3 fadeout 1.0
    scene d18s08-08 tl-slaps-cl-again_c1 with dissolve
    play voice4 teresa_angry_argh3 noloop
    "{color=#c46c93}???{/color}" "I didn't instill the word of our Lord in you since you were a babe so that you can spit in the face of his holy creatio—."
    scene d18s08-03 hr-eavesdrop_c1 with dissolve
    pause
    scene d18s08-07 slap-noise-tl-screams-at-cl_c1 with dissolve
    pause
    scene d18s08-09 tl-notices-door-is-open_c1 with dissolve
    pause
    scene d18s08-09-1 tl-asks-whos-there_c1 with dissolve
    play voice4 teresa_angry_argh1 noloop
    "{color=#c46c93}???{/color}" "Who's there!?"
    scene d18s08-03 hr-eavesdrop_c1 with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "Fuck."
    play sound sfx_door_open6 volume 1.5
    scene d18s08-12 cl-covering-ass_c1 with fade
    pause
    play sound sfx_door_closed2
    scene d18s08-10 mc-arj-hr-enter-room_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mct "Wait... Is that Cynthia?"
    scene d18s08-11 tl-standing-in-front-of-gang_c1 with dissolve
    play voice4 teresa_surprised_huh1 noloop
    tl "Who are you and what are you doing here?"
    scene d18s08-13 arj-steps-forward_c1 with dissolve
    play voice3 amrose_thinking_emm noloop
    arj "We were told that the new I.T. professor was here? We had some questions to ask her..."
    scene d18s08-14 tl-express-disgust_c1 with dissolve
    play voice4 teresa_disappointed_ehh1 noloop
    tl "Oh, {i}her{/i}. No, she's not here."
    scene d18s08-13 arj-steps-forward_c1 with dissolve
    play voice3 amrose_thinking_hmm1 noloop
    arj "Do you know where she is—"
    scene d18s08-15 tl-talking_c1 with dissolve
    play voice4 teresa_no_angry noloop fadein 0.4
    tl "I don't concern myself with the goings-on of heretics."
    play voice3 amrose_yes_okay1 noloop
    arj "I— Okay."
    scene d18s08-16 hr-asks-points-cl_c1 with dissolve
    play voice4 hana_emm noloop
    hr "Can I ask what's going on here?"
    scene d18s08-17 tl-laughs-at-cl_c1 with dissolve
    play voice3 teresa_happy_laugh5 noloop
    tl "*Laughs* Hear that, Cynthia? Should I tell them?"
    play voice4 cynthia_pain_crying3 noloop
    scene d18s08-18 cl-ashamed-embaraced_c1 with dissolve
    stop voice4 fadeout 1.0
    pause
    scene d18s08-19 tl-looks-at-gang-points-cl_c1 with dissolve
    play voice3 teresa_angry_breathing1 noloop
    tl "This tramp of a woman I call my daughter has committed grievous sins, {i}repeatedly{/i}, and is now being punished and shamed for her debaucherous ways."
    play voice2 d1s1_mmm noloop
    mct "Jesus, I can see where Cynthia gets it from."
    play voice3 teresa_angry_dough noloop
    play sound sfx_whip_slap1
    scene d18s08-20 tl-spreads-cl-ass_c1 with vpunch
    if d14s07_deflower is True:
        tl "Within a week of having her purity, her womanhood, her virginity restored, she lost it once more!"
        tl "One week!"
    elif True:
        pause
    play voice4 cynthia_pain_crying1 noloop
    scene d18s08-21 cl-bent-over-slapped_c1 with dissolve
    stop voice4 fadeout 0.5
    tl "Can you imagine the shame I feel as a woman and her mother? The shame that her wanton actions cause our family?"
    scene d18s08-22 tl-points-arj-hr-question_c1 with dissolve
    play voice3 teresa_hey_angry noloop
    tl "You two.{w} You seem like two respectable young women."
    tl "Are your virginities still intact? Are you pure from the corruption of lust?"
    scene d18s08-23 arj-hr-exchange-looks_c1 with dissolve
    pause
    scene d18s08-24 arj-hr-give-thumbs-up_c1 with dissolve
    play voice4 amrose_yes_yap noloop
    play voice2 chloe_yes_aga2 noloop
    "Both" "Yep."
    play voice3 cynthia_pain_crying2 noloop volume 0.7
    scene d18s08-25 tl-smacks-cl-again_c1 with dissolve
    cl "*Cries out in pain*"
    scene d18s08-26 tl-regret_c1 with dissolve
    play voice4 teresa_disappointed_ohh2 noloop
    tl "This is what I get for being loving. For allowing her budding youth to be free."
    tl "I was warned, but I didn't listen. And now... My poor girl."
    stop voice3 fadeout 1.0
    play voice4 teresa_pain_sobs2 noloop
    scene d18s08-27 tl-starts-crying_c1 with dissolve
    pause
    scene d18s08-28 gang-confused_c1 with dissolve
    pause
    scene d18s08-29 arj-consoles-tl_c1 with dissolve
    play voice3 amrose_thinking_hmm3 noloop
    arj "Miss, it's okay..."
    scene d18s08-30 tl-asks-arj-help_c1 with dissolve
    play voice4 teresa_no_active noloop
    tl "No. No, it's not. This must be fixed before she goes deeper into Satan's clutches."
    tl "I know what I need to do, but I can't do it alone."
    tl "Can you accompany me?"
    scene d18s08-31 arj-unsure_c1 with dissolve
    play voice3 amrose_surprised_what noloop
    arj "I— What?"
    scene d18s08-32 tl-insists-arj-helps-her_c1 with dissolve
    play voice4 teresa_disappointed_mph noloop
    tl "She needs to be punished in a way that I cannot perform. A mother can only do so much."
    tl "She needs to properly understand shame so that her course can be corrected."
    scene d18s08-33 arj-reluctantly-agrees_c1 with dissolve
    play voice3 amrose_surprised_uh4 noloop
    arj "I..."
    arj "Uhm... Of course. I'd...be happy to."
    play voice4 teresa_happy_relief1 noloop
    tl "Thank you. It's hard to find a good, pious woman these days."
    scene d18s08-34 tl-instructs-cl_c1 with dissolve
    play voice4 teresa_arrogant_hmm noloop
    tl "Get up and make yourself look presentable. We're going."
    play voice3 cynthia_happy_mmm noloop
    scene d18s08-35 cl-walks-ashamed-sobbing_c1 with dissolve
    pause
    scene d18s08-36 tl-tells-arj-to-follow_c1 with dissolve
    play voice4 teresa_yes_ugu noloop
    tl "Let's go."
    play voice3 amrose_old_psst2 noloop
    scene d18s08-37 arj-begs-for-help-silently_c1 with dissolve
    pause
    play voice2 mc_no_uhuh2 noloop
    scene d18s08-38 mc-hr-helpless_c1 with dissolve
    "..."
    scene d18s08-39 hr-asks-what-happened_c1 with dissolve
    play voice3 hana_argh noloop
    hr "What just happened?"
    scene d18s08-41 mc-has-no-answer_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    pause
    scene d18s08-39 hr-asks-what-happened_c1 with dissolve
    $ unlock_gallery_slot("cg", "d18s08")
    play voice3 hana_argh2 noloop
    hr "Let's go find the new professor. We don't have time to waste."
    stop music fadeout 4.5

    jump d18s09
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
