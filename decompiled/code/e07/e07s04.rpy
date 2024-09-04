image e07s04-a45-1 = Movie(play = "images/E-07/s04/anim/e07s04-a45-1-2x-50fps.webm", start_image = "e07s04-a45-1 mc-gb-pegging-anim-01")
image e07s04-a45-1-f = Movie(play = "images/E-07/s04/anim/e07s04-a45-1-2x-60fps.webm", start_image = "e07s04-a45-1 mc-gb-pegging-anim-01")
image e07s04-a45-2 = Movie(play = "images/E-07/s04/anim/e07s04-a45-2-2x-50fps.webm", start_image = "e07s04-a45-2 mc-gb-pegging-anim-01")
image e07s04-a45-2-f = Movie(play = "images/E-07/s04/anim/e07s04-a45-2-2x-60fps.webm", start_image = "e07s04-a45-2 mc-gb-pegging-anim-01")
image e07s04-a45-3 = Movie(play = "images/E-07/s04/anim/e07s04-a45-3-2x-50fps.webm", start_image = "e07s04-a45-3 mc-gb-pegging-anim-01")
image e07s04-a45-3-f = Movie(play = "images/E-07/s04/anim/e07s04-a45-3-2x-60fps.webm", start_image = "e07s04-a45-3 mc-gb-pegging-anim-01")
image e07s04-a45-4 = Movie(play = "images/E-07/s04/anim/e07s04-a45-4-2x-50fps.webm", start_image = "e07s04-a45-4 mc-gb-pegging-anim-01")
image e07s04-a45-4-f = Movie(play = "images/E-07/s04/anim/e07s04-a45-4-2x-60fps.webm", start_image = "e07s04-a45-4 mc-gb-pegging-anim-01")

image e07s04-a58-1 = Movie(play = "images/E-07/s04/anim/e07s04-a58-1-2x-50fps.webm", start_image = "e07s04-a58-1 mc-gb-pegging-fast-anim-01")
image e07s04-a58-1-f = Movie(play = "images/E-07/s04/anim/e07s04-a58-1-2x-60fps.webm", start_image = "e07s04-a58-1 mc-gb-pegging-fast-anim-01")
image e07s04-a58-2 = Movie(play = "images/E-07/s04/anim/e07s04-a58-2-2x-50fps.webm", start_image = "e07s04-a58-2 mc-gb-pegging-fast-anim-01")
image e07s04-a58-2-f = Movie(play = "images/E-07/s04/anim/e07s04-a58-2-2x-60fps.webm", start_image = "e07s04-a58-2 mc-gb-pegging-fast-anim-01")
image e07s04-a58-3 = Movie(play = "images/E-07/s04/anim/e07s04-a58-3-2x-50fps.webm", start_image = "e07s04-a58-3 mc-gb-pegging-fast-anim-01")
image e07s04-a58-3-f = Movie(play = "images/E-07/s04/anim/e07s04-a58-3-2x-60fps.webm", start_image = "e07s04-a58-3 mc-gb-pegging-fast-anim-01")

image e07s04-a78-1 = Movie(play = "images/E-07/s04/anim/e07s04-a78-1-2x-50fps.webm", start_image = "e07s04-a78-1 mc-arj-bj-anim-00")
image e07s04-a78-1-f = Movie(play = "images/E-07/s04/anim/e07s04-a78-1-2x-60fps.webm", start_image = "e07s04-a78-1 mc-arj-bj-anim-00")
image e07s04-a78-2 = Movie(play = "images/E-07/s04/anim/e07s04-a78-2-2x-50fps.webm", start_image = "e07s04-a78-2 mc-arj-bj-anim-00")
image e07s04-a78-2-f = Movie(play = "images/E-07/s04/anim/e07s04-a78-2-2x-60fps.webm", start_image = "e07s04-a78-2 mc-arj-bj-anim-00")
image e07s04-a78-3 = Movie(play = "images/E-07/s04/anim/e07s04-a78-3-2x-50fps.webm", start_image = "e07s04-a78-3 mc-arj-bj-anim-00")
image e07s04-a78-3-f = Movie(play = "images/E-07/s04/anim/e07s04-a78-3-2x-60fps.webm", start_image = "e07s04-a78-3 mc-arj-bj-anim-00")

image e07s04-a91-1 = Movie(play = "images/E-07/s04/anim/e07s04-a91-1-2x-50fps.webm", start_image = "e07s04-a91-1 mc-lc-face-fuck-anim-01")
image e07s04-a91-1-f = Movie(play = "images/E-07/s04/anim/e07s04-a91-1-2x-60fps.webm", start_image = "e07s04-a91-1 mc-lc-face-fuck-anim-01")
image e07s04-a91-2 = Movie(play = "images/E-07/s04/anim/e07s04-a91-2-2x-50fps.webm", start_image = "e07s04-a91-2 mc-lc-face-fuck-anim-01")
image e07s04-a91-2-f = Movie(play = "images/E-07/s04/anim/e07s04-a91-2-2x-60fps.webm", start_image = "e07s04-a91-2 mc-lc-face-fuck-anim-01")

image e07s04-a06-glam-1 = Movie(play = "images/E-07/s04/anim/e07s04-a06-2x-50fps.webm", start_image = "e07s04-a06 lc-talking-glambot-06-000", image = "e07s04-a06 lc-talking-glambot-06-198", loop = False)

label e07s04:

    $ e07s04_challenge_win = False

    scene black
    show screen scene_transistion(_("Back in the Dungeon"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_double_door1
label replay_e07s04 hide:
    if _in_replay:
        $ renpy.music.set_volume(0.6, 0.0, "music")
    scene e07s04-02-lc-welcoming
    with Fade(0.5, 0.5, 0.5)
    play music music_bdsm_overload
    pause
    play voice3 lydia_lydiahey noloop
    lc "Welcome to Crowning, Domina Gizela."
    play sound sfx_chains_swings1 volume 2.0
    scene e07s04-01-gb-zh-bringing-them-in with dissolve
    stop sound fadeout 1.0
    play voice4 girl24_arrogant_hm1 noloop
    gb "Sedět"
    scene e07s04-03-gb-thanking with dissolve
    play voice4 girl24_hey_greeting noloop
    gb "Děkuji, Mistress Cox. For both welcoming me to your fine city, as well as the accommodations you provided me."
    scene e07s04-04-lc-talking with dissolve
    play voice3 dahlia_yes_aga noloop
    lc "Of course, I had to reciprocate the welcome I was given when I visited Prague. I expect there are no complaints so far?"
    scene e07s04-05-gb-denying with dissolve
    play voice4 girl24_no_nah noloop
    gb "Ne, none at all."
    scene e07s04-a06 lc-talking-glambot-06-000 with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    lc "Very good! Shall we proceed to the day's event?"
    play sound sfx_camera_fly1 volume 2.5
    play sound2 ["<silence 2.0>", sfx_camera_fly1] volume 2.5 noloop
    play sound3 ["<silence 4.0>", sfx_camera_fly1] volume 2.5 noloop
    scene e07s04-a06-glam-1
    pause
    play voice4 girl24_yes_ugu noloop
    if e07s03_give_all is True:
        gb "Ano. I hope today that I will receive the same treatment that I did in Praha."
    elif True:
        scene e07s04-08-gb-if-challenge-lose with dissolve
        gb "Ano. This time, I hope your little slave performs better for me."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene e07s04-09-lc-asking with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    lc "As the visiting Mistress, it is up to you to pick today's activity. Have you made a decision?"
    scene e07s04-10-gb-asking with dissolve
    play voice4 girl24_yes_yeah noloop
    gb "Ano. I think it will also be one that you approve of."
    scene e07s04-11-lc-surprised with dissolve
    play voice3 dahlia_thinking_oh noloop
    lc "Oh, you've piqued my curiosity."
    scene e07s04-12-gb-talking with dissolve
    play voice4 girl24_happy_laugh1 noloop
    gb "Today, I have chosen that we are to use a strap-on to fuck our submissives."
    scene e07s04-13-lc-asking with dissolve
    play voice3 dahlia_arrogant_yeah noloop
    lc "And which hole do you want us to use?"
    scene e07s04-14-gb-wicked-smile with dissolve
    play voice4 girl24_disgust_ooh2 noloop
    gb "Anal, of course."
    scene e07s04-15-lc-wicked-smile with dissolve
    play voice3 dahlia_arrogant_ha noloop
    lc "Of course. Any other restrictions?"
    scene e07s04-16-gb-talking with dissolve
    play voice4 girl24_no_simple1 noloop
    gb "Ne."
    scene e07s04-06-lc-talking with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    lc "How will we determine the winner?"
    scene e07s04-07-gb-if-challenge-won with dissolve
    play voice4 girl24_disappointed_ohh1 noloop
    gb "Whoever makes the other domina's submissive cum first shall be crowned vítězný. The victor."
    gb "And as a token of my appreciation for allowing me to use both of your subs in Praha, I have brought you a gift."
    play sound sfx_metal_chain1
    scene e07s04-17-zo-being-pointed-at with dissolve
    gb "I offer you one of my finest submissives. She can take quite the anal punishment, I think you will be pleased."
    scene e07s04-16-gb-talking with dissolve
    play voice4 girl24_arrogant_huh2 noloop
    gb "And you? Which of these will I have the privilege of ruining today?"
    scene e07s04-15-lc-wicked-smile with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    lc "Decisions..."
    scene e07s04-19-arj-shot with dissolve
    pause
    scene e07s04-20-pb-shot with dissolve
    pause
    scene e07s04-18-mc-shot with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    lc "Decisions..."
    menu:
        "Volunteer"(hint="e07s04m01c01"):
            $ e07s04_challenge_win = True
            $ e07_mc_wins += 1
            scene e07s04-21-mc-speaking with dissolve
            play voice2 d1s5_mcthinks noloop volume 1.7
            mc "Mistress, I-"
            play voice3 dahlia_angry_argh1 noloop
            scene e07s04-22-lc-angry with hpunch
            lc "How {i}dare{/i} you speak without permission! For that, I choose you, [e07_mcname!t]."
        "Stay Quiet"(hint="e07s04m01c02"):

            $ e07s04_challenge_win = False
            scene e07s04-23-lc-calmly-choosing with dissolve
            play voice3 dahlia_hey_active1 noloop
            lc "[e07_mcname!t]. I think you are the {i}perfect{/i} sub for this challenge. Lest we forget your first time as my little play thing here with [e07_arjname!t]."

    scene e07s04-24-mc-agreeing with dissolve
    play voice2 d2s12_emmm noloop volume 1.5
    mc "Uhm... Of course [e07_lcname!t]. Your wish is my command."
    scene e07s04-25-lc-arj-asking with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    lc "[e07_arjname!t], please retrieve the accoutrement for this challenge."
    scene e07s04-26-arj-following with dissolve
    play voice5 amrose_yes_confident2 noloop
    arj "Right away, [e07_lcname!t]."
    scene e07s04-27-mc-lc-talking with dissolve
    play voice3 dahlia_disgust_meh noloop
    lc "You better not disappoint me today, [e07_mcname!t]."
    scene e07s04-28-mc-talking with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "I will do my very best, [e07_lcname!t]."
    scene e07s04-29-lc-talking with dissolve
    play voice3 dahlia_angry_ah2 noloop
    lc "Do better than your best. If we win I promise that you'll get a nice little treat. But if we lose, well, then [e07_pbname!t] wins and is one step closer to the grand prize."
    scene e07s04-30-lc-mc-talking with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, [e07_lcname!t]. I will do better. Better than my best."
    lc "Good."
    play sound sfx_cloth_rustling2
    scene e07s04-31-arj-coming with dissolve
    pause
    scene e07s04-32-lc-asking-to-choose with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    lc "As the visiting mistress Gizela, you may have your pick of strap-ons."
    scene e07s04-33-gb-choosing with dissolve
    play voice4 girl24_disappointed_eeh2 noloop
    gb "Děkuji, I shall take this one."
    scene e07s04-34-lc-talking with dissolve
    play voice3 dahlia_yes_ugu noloop
    lc "All right, [e07_mcname!t]. Assume your place."
    scene e07s04-35-mc-thinking with dissolve
    play voice2 d1s1_mmm noloop
    mct "Do I really have to let her fuck me in the ass?"
    pause
    scene e07s04-36-lc-zh-looking-at-them with dissolve
    mct "If it makes her happy..."
    play sound sfx_cloth_rustling3
    scene e07s04-37-mc-on-fours with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "Then I'll do it."
    scene e07s04-38-mc-lc-talking with dissolve
    play voice3 dahlia_arrogant_hm noloop
    lc "[e07_arjname!t], you will be in charge of giving us the green light."
    scene e07s04-39-mc-lc-talking with dissolve
    play voice5 amrose_yes_confident1 noloop
    arj "Yes, [e07_lcname!t]."
    play sound sfx_sextoy_uncuff1
    scene e07s04-40-arj-gb-lc-race-about-to-start with dissolve
    pause
    play sound sfx_flag_wiggle2
    scene e07s04-41-arj-gb-lc-race-about-to-start with dissolve
    play voice5 amrose_hey_attention noloop
    arj "On your marks."
    arj "Get set."
    play sound sfx_flag_wiggle1
    play voice5 amrose_happy_woo noloop
    with hpunch
    arj "Go!"
    scene e07s04-42-mc-gb-getting-him-ready with dissolve
    play voice4 girl24_happy_laugh2 noloop
    gb "I promise to be gentle."
    scene e07s04-43-mc-gb-getting-him-ready with dissolve
    play voice4 girl24_happy_mmm noloop
    gb "At least to start."
    scene e07s04-44-mc-gb-talking with dissolve
    play voice4 girl24_arrogant_huh1 noloop
    gb "Are you prepared?"
    play voice2 mc_disappointed_ah1 noloop
    mc "Uhh..."
    gb "I assume that is a yes, then."


    $ Lovense.stop()

    scene e07s04-a45-1 mc-gb-pegging-anim-01 with dissolve
    pause
    play voice5 chastity_closedmoans1
    play voice3 iona_moans2
    play voice4 girl24_sex_openmoans1
    play voice2 mc_scared_huuuh3 noloop volume 1.6
    queue voice2 d7s4_mcbreathing volume 2.0
    play sound sfx_vagina_penetration1_fast loop
    $ Lovense.pattern("7;10", 1400)
    scene e07s04-a45-1
    gb "Oh, my little subby, your asshole is so tight!!"
    pause
    gb "She does not ride you enough, does she?"
    mc "Fuh... Fuh... No... She... She doesn't."
    scene e07s04-a45-2 with dissolve
    gb "This will be easy then! I gave her my little slave whose ass is loose."
    gb "She takes a lot to feel pleasure in her ass now."
    pause
    scene e07s04-a45-3 with dissolve
    pause
    scene e07s04-a45-4 with dissolve
    pause
    $ Lovense.pattern("7;10", 700)
    scene e07s04-a45-1-f with dissolve
    pause
    scene e07s04-a45-2-f with dissolve
    pause
    if e07s03_give_all is True:
        gb "This time, I shall come out on top!"
    elif True:
        gb "This shall be easy, like when you were in my dungeon."
    gb "It is okay, you may cum now."
    scene e07s04-a45-3-f with dissolve
    gb "Come, little man, cum from your ass!"
    mc "Mmmm, mmmMMM- it's- It's going to take more than that!"
    pause
    scene e07s04-a45-4-f with dissolve
    mct "Fuck... This does feel pretty good."
    mct "I don't know how long I can hold out. I hope [e07_lcname!t] makes her cum soon."
    pause
    scene e07s04-46-arj-pb-far with dissolve
    pause
    stop sound fadeout 1.0
    $ renpy.music.set_pan(-0.5, 1.0, "voice2")
    $ renpy.music.set_pan(-0.5, 1.0, "voice3")
    $ renpy.music.set_pan(-0.5, 1.0, "voice4")
    $ renpy.music.set_pan(-0.5, 1.0, "voice5")
    $ renpy.music.set_volume(0.5, 1.0, "voice2")
    $ renpy.music.set_volume(0.5, 1.0, "voice3")
    $ renpy.music.set_volume(0.5, 1.0, "voice4")
    $ renpy.music.set_volume(0.5, 1.0, "voice5")
    scene e07s04-47-arj-pb-talking with dissolve
    play voice6 amrose_thinking_emm noloop
    arj "You, uh, seem pretty excited by this, Pete."
    scene e07s04-48-arj-pb-talking with dissolve
    play voice7 pete_hey_attention noloop
    pb "Wanna know a secret?"
    scene e07s04-49-arj-pb-talking with dissolve
    play voice6 amrose_yes_yeah2 noloop
    arj "Sure?"
    scene e07s04-50-arj-pb-happy with dissolve
    play voice7 pete_disappointed_oof1 noloop
    pb "Anyone touches my asshole, I cum, like, immediately. So this is kind of a turn-on."
    scene e07s04-51-arj-pb-happy with dissolve
    play voice6 amrose_thinking_hmm4 noloop
    arj "I can tell..."
    scene e07s04-52-pb-surprised with dissolve
    play voice7 pete_arrogant_heh5 noloop
    pb "Man, it feels fucking great."
    play voice6 amrose_yes_ugu noloop
    arj "I bet..."
    play voice7 pete_disappointed_mmf1 noloop
    pb "Real happy [e07_lcname!t] didn't pick me. She'd have lost right away, but man, this is giving me some ideas."
    scene e07s04-51-arj-pb-happy with dissolve
    play voice6 amrose_disappointed_ehh1 noloop
    arj "Me too..."
    scene e07s04-52-pb-surprised with dissolve
    play voice7 pete_surprised_huh4 noloop
    pb "Huh?"
    scene e07s04-53-arj-coming-back-to-her-senses with dissolve
    play voice6 amrose_disappointed_oh3 noloop
    arj "Oh, uhhh, nothing."
    scene e07s04-54-arj-coming-back-to-her-senses with dissolve
    play voice7 pete_thinking_emm2 noloop
    pb "AmRose, you got some shit..."
    play sound sfx_hair_scratch1
    scene e07s04-55-pb-touching-her-cheek with dissolve
    play voice6 amrose_surprised_huh3 noloop
    arj "Wha...?"
    play voice7 pete_disappointed_aah2 noloop
    pb "Just, uh, hang on a sec."
    pb "Got it."
    scene e07s04-56-pb-being-gentle with dissolve
    play voice7 pete_happy_laugh2 noloop
    pb "Don't want you looking like shit. Too fucking hot for that."
    play voice6 amrose_thinking_hmm2 noloop
    arj "Th-thanks, Pete."
    play voice7 pete_yes_yeah noloop
    pb "Yeah, don't mention it."
    $ renpy.music.set_pan(0.0, 1.0, "voice2")
    $ renpy.music.set_pan(0.0, 1.0, "voice3")
    $ renpy.music.set_pan(0.0, 1.0, "voice4")
    $ renpy.music.set_pan(0.0, 1.0, "voice5")
    $ renpy.music.set_volume(1.0, 1.0, "voice2")
    $ renpy.music.set_volume(1.0, 1.0, "voice3")
    $ renpy.music.set_volume(1.0, 1.0, "voice4")
    $ renpy.music.set_volume(1.0, 1.0, "voice5")
    play sound sfx_vagina_penetration1_fast loop
    scene e07s04-57-02-mc-gb-talking with dissolve
    pause
    $ renpy.music.set_pan(-0.5, 1.0, "voice2")
    $ renpy.music.set_pan(-0.5, 1.0, "voice3")
    $ renpy.music.set_pan(-0.5, 1.0, "voice4")
    $ renpy.music.set_pan(-0.5, 1.0, "voice5")
    $ renpy.music.set_volume(0.5, 1.0, "voice2")
    $ renpy.music.set_volume(0.5, 1.0, "voice3")
    $ renpy.music.set_volume(0.5, 1.0, "voice4")
    $ renpy.music.set_volume(0.5, 1.0, "voice5")
    stop sound fadeout 1.0
    scene e07s04-57-pb-shocked with dissolve
    play voice7 pete_surprised_ohmy2 noloop
    pb "Holy shit."
    $ renpy.music.set_pan(0.0, 1.0, "voice2")
    $ renpy.music.set_pan(0.0, 1.0, "voice3")
    $ renpy.music.set_pan(0.0, 1.0, "voice4")
    $ renpy.music.set_pan(0.0, 1.0, "voice5")
    $ renpy.music.set_volume(1.0, 1.0, "voice2")
    $ renpy.music.set_volume(1.0, 1.0, "voice3")
    $ renpy.music.set_volume(1.0, 1.0, "voice4")
    $ renpy.music.set_volume(1.0, 1.0, "voice5")
    play sound sfx_vagina_penetration1_fast loop
    scene e07s04-a58-1 mc-gb-pegging-fast-anim-01 with dissolve
    pause
    $ Lovense.pattern("7;10", 1400)
    scene e07s04-a58-1
    gb "It is time, as you say, to take it up a notch, ano?"
    mc "I - uh - think you were doing just fine before."
    pause
    gb "I think that is exactly perfect, then."
    scene e07s04-a58-2 with dissolve
    mc "Well, wait, just hang on a second-"
    gb "Ano, ano! I think this is it."
    pause
    scene e07s04-a58-3 with dissolve
    play voice4 girl24_sex_openmoans4
    mc "Holllly shit!"
    pause
    $ Lovense.pattern("7;12", 700)
    scene e07s04-a58-1-f with dissolve
    gb "Yes, you little anal slave! Submit before your domina!"
    gb "Cum for me! You are putty, cum in my hand you little ass slut!"
    mc "Fuck, fuuuuuuck!"
    pause
    scene e07s04-a58-2-f with dissolve
    mct "Come on, [e07_lcname!t]. I - I can't hold out much longer."
    mct "Fuck... That's..."
    mct "{i}That's pretty hot. Shit!{/i}"
    pause
    mct "Fuck, look away [e07_mcname!t]. Look awwaaaaaaay!"
    mct "Shit this isn't any better."
    scene e07s04-a58-3-f with dissolve
    pause
    gb "Yes, I can feel you."
    mc "Whaa... Wai... Oh God..."
    gb "Yes, yes-"

    if e07s04_challenge_win is True:
        jump e07s04_challenge_win
    elif True:
        jump e07s04_challenge_lose

label e07s04_challenge_win:

    scene e07s04-59-gb-lc-angry with dissolve
    play voice4 girl24_angry_argh3 noloop
    stop voice2 fadeout 1.0
    gb "No!"
    $ Lovense.stop()
    $ Lovense.vibrate(14)
    play voice5 chastity_orgasm noloop
    stop voice3 fadeout 1.0
    stop sound fadeout 1.0
    scene e07s04-60-zh-cumming with hpunch
    "Servant" "-God, I'm cumming!"
    scene e07s04-61-zh-cumming with dissolve
    play voice3 dahlia_happy_laugh4 noloop
    lc "My, my. It looks like I made your little slave cum first."
    scene e07s04-62-mc-thinking with dissolve
    $ Lovense.vibrate(3)
    play voice2 mc_scared_oh1 noloop
    mct "And not a moment too soon, fuck."
    scene e07s04-63-gb-angry with dissolve
    play voice4 girl24_angry_argh2 noloop
    gb "No, no, no! I was to experience the pleasure first!"
    scene e07s04-64-lc-mc-impressed with dissolve
    play voice3 dahlia_surprised_wow noloop
    lc "I'm impressed, [e07_mcname!t]. Very impressed."
    scene e07s04-65-lc-mc-impressed with dissolve
    play voice2 mc_happy_oof2 noloop
    mc "Thank you, [e07_lcname!t]. I'm happy I've pleased you."
    scene e07s04-66-gb-lc-talking with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    lc "Domina Gizela, may I have my little submissive back? I promised him a reward if he did a good job."
    play voice4 girl24_yes_simple1 noloop
    gb "Of course, Mistress Lydia."
    scene e07s04-67-mc-lc-talking with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    lc "Mmmm, you do deserve a little reward."
    scene e07s04-68-mc-lc-talking with dissolve
    play voice2 d1s5_orgasm noloop
    mct "Yesss, God. If this is what it takes to receive anything from [e07_lcname!t], it was worth it."
    scene e07s04-69-mc-lc-opening-cage with dissolve
    play voice3 lydia_thinking noloop volume 1.5
    lc "What would you want as your reward, [e07_mcname!t]."
    play voice2 mc_happy_a1 noloop volume 1.7
    mc "I'll take anything you will give me. It would be an honor."
    mct "Fuck, I think Lydia is going to make me cum! It's a dream cum true!"
    play sound sfx_sextoy_uncuff1
    scene e07s04-70-lc-arj-talking with dissolve
    play voice3 dahlia_yes_simple noloop
    lc "Good, that's the only acceptable answer."
    lc "[e07_arjname!t], come."
    play voice3 dahlia_hey_active2 noloop
    lc "[e07_arjname!t]!"
    scene e07s04-71-lc-arj-talking with dissolve
    play voice5 amrose_surprised_uh2 noloop
    arj "Uh, yes, [e07_lcname!t]?"
    play voice3 dahlia_angry_ah1 noloop
    lc "Fuck, get over here!"
    scene e07s04-72-lc-arj-talking with dissolve
    play voice5 amrose_yes_questioning noloop
    arj "Yes, [e07_lcname!t]?"
    scene e07s04-73-lc-arj-talking with dissolve
    play voice3 dahlia_arrogant_heh noloop
    lc "I want you to give [e07_mcname!t] a blowjob."
    play voice5 amrose_arrogant_huh4 noloop
    arj "What?"
    scene e07s04-74-mc-thinking with dissolve
    play voice2 mc_angry_errr1 noloop
    mct "Fuck... I thought [e07_lcname!t] was going to give me the reward..."
    scene e07s04-75-lc-ordering with dissolve
    play voice3 dahlia_angry_oof noloop
    lc "You heard me. Get on your knees and suck his dick."
    arj "..."
    lc "What?"
    scene e07s04-76-arj-surprised with dissolve
    play voice5 amrose_disappointed_ehh2 noloop
    arj "... Do I have to?"
    play voice3 dahlia_angry_argh2 noloop
    scene e07s04-77-lc-angry with hpunch
    lc "I will not repeat myself."
    play voice5 amrose_yes_yeah4 noloop
    arj "... Yes, [e07_lcname!t]."
    scene e07s04-a78-1 mc-arj-bj-anim-00 with dissolve
    pause
    play voice5 daisy_sucking
    play voice2 d7s4_mcbreathing volume 2.0
    play voice3 dahlia_disappointed_hmm1 noloop
    $ Lovense.pattern("7;10", 1400)
    scene e07s04-a78-1
    pause
    lc "How does that feel, [e07_mcname!t]?"
    lc "Better than Gizela fucking you, I bet."
    scene e07s04-a78-2 with dissolve
    mc "It feels... Mmmm... Good, [e07_lcname!t]."
    lc "Good, you should enjoy anything I give you."
    pause
    scene e07s04-a78-3 with dissolve
    play voice3 dahlia_surprised_huh2 noloop
    lc "But is it even better than when [e07_arjname!t] fucked you in the ass?"
    mc "Mmmhmmm, yeah - fuck, yes."
    pause
    $ Lovense.pattern("7;10", 700)
    scene e07s04-a78-1-f with dissolve
    pause
    scene e07s04-a78-2-f with dissolve
    lc "Good. Good boys deserve a treat."
    play voice3 dahlia_yes_angry noloop
    lc "Now cum, [e07_mcname!t], cum."
    pause
    scene e07s04-a78-3-f with dissolve
    pause
    mc "Fuck, I'm so close."
    lc "Cum, [mcname]."
    mc "Oh fuck!"
    play voice2 d1s5_orgasm2 noloop
    play voice5 samiya_mfff3 noloop
    play sound mc_cum_sound1
    $ Lovense.stop()
    $ Lovense.vibrate(17)
    scene e07s04-79-arj-cumming with hpunch
    pause
    scene e07s04-80-lc-impressed with dissolve
    $ Lovense.vibrate(3)
    play voice3 lydia_lydwow noloop
    lc "Wow, look at that. Even after being sissified and fucked in the ass by a beautiful woman, and you can cum so much."

    jump e07s04_ending

label e07s04_challenge_lose:

    scene e07s04-81-gb-mc-losing with dissolve
    play voice4 girl24_happy_yeah2 noloop
    gb "Yes!"
    $ Lovense.stop()
    $ Lovense.vibrate(17)
    play voice2 mc_pain_argh1 noloop
    with hpunch
    mc "Fuck, I'm cumming!"
    queue voice2 d1s5_orgasm2 noloop
    stop voice3 fadeout 1.0
    stop voice5 fadeout 1.0
    play sound mc_cum_sound1
    $ Lovense.vibrate(18)
    scene e07s04-82-mc-cum with hpunch
    pause
    scene e07s04-83-lc-disappointed with dissolve
    $ Lovense.vibrate(3)
    play voice3 dahlia_disgust_yah noloop
    lc "God... Worthless."
    scene e07s04-84-lc-angry with dissolve
    play voice3 dahlia_angry_argh2 noloop
    lc "Do you know that? That you're fucking useless?"
    scene e07s04-85-mc-sorry with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I... I'm sorry, [e07_lcname!t]."
    scene e07s04-86-lc-angry with dissolve
    play voice3 dahlia_angry_oh noloop
    lc "You should be. You are. You're a sorry excuse for a submissive."
    scene e07s04-87-mc-sorry with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yes... I am..."
    play voice3 dahlia_angry_hm1 noloop
    lc "There's only one thing you deserve. {i}Punishment.{/i}"
    mc "... Yes, [e07_lcname!t]."
    scene e07s04-88-lc-ordering with dissolve
    play voice3 dahlia_angry_hm2 noloop
    lc "Get to work."
    scene e07s04-89-mc-surprised with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "Wait... What..."
    play voice3 dahlia_disgust_oof noloop
    lc "Clean it. With your mouth. If you're so eager to cum from someone fucking your ass, then you should be as eager to clean your Mistress' strap-on."
    play voice2 d9s2_mcyes2 noloop volume 2.5
    mc "... Yes, [e07_lcname!t]."
    scene e07s04-90-lc-commanding with dissolve
    play voice3 dahlia_angry_oof noloop
    play sound mc_sex_sucking_fast2 loop volume 1.5
    lc "How does dirty asshole taste? Do you like sucking on this filthy strap-on!?"

    scene e07s04-a91-1 mc-lc-face-fuck-anim-01 with dissolve
    pause
    play voice2 [mc_pain_mff2, mc_pain_mff1] noloop
    $ Lovense.pattern("5;8", 1400)
    scene e07s04-a91-1
    mc "Gllllck - glllllck!"
    pause
    scene e07s04-a91-2 with dissolve
    play voice3 dahlia_happy_laugh1 noloop
    queue voice3 iona_moans2
    lc "It sounds like you {i}love it!{/i}"
    lc "Feel it in the back of your throat, I can see my fake dick bulging your throat!"
    pause
    $ Lovense.pattern("5;10", 700)
    scene e07s04-a91-1-f with dissolve
    lc "Get it nice and slobbery, I don't want to see a speck of shit when I pull it out of your throat."
    lc "Mmmmm, this is definitely turning me on. Using you as a little fuck puppet."
    pause
    scene e07s04-a91-2-f with dissolve
    pause
    stop voice2 fadeout 1.0
    stop sound fadeout 1.0
    scene e07s04-93-lc-satisfied with dissolve
    $ Lovense.stop()
    $ Lovense.vibrate(3)
    play voice3 dahlia_happy_hmm1 noloop
    lc "Hmmm. You've done a... Satisfactory job."

    jump e07s04_ending

label e07s04_ending:

    $ Lovense.stop()


    $ renpy.end_replay()
    scene e07s04-02-lc-welcoming with fade
    play voice3 dahlia_hey_angry noloop
    lc "And with that, I think our business is concluded, Domina."
    scene e07s04-03-gb-thanking with dissolve
    play voice4 girl24_yes_simple2 noloop
    gb "Yes. Again, I want to thank you for suggesting this, Mistress Lydia. I did enjoy every second of it."
    gb "And every inch."
    scene e07s04-04-lc-talking with dissolve
    play voice3 dahlia_yes_aga noloop
    lc "Of course. I do have some business to attend to, so you will have to excuse me if I don't walk you out."
    scene e07s04-05-gb-denying with dissolve
    play voice4 girl24_yes_ugu noloop
    gb "Of course. We can find our own way."
    play sound sfx_chains_swings1 volume 2.0
    scene e07s04-94-gb-leaving with dissolve
    stop sound fadeout 1.0
    play voice4 girl24_arrogant_hm3 noloop
    gb "Come."
    scene e07s04-22-lc-angry with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    lc "[e07_mcname!t], you can go. Rest. I have more challenges for you, and I need you in tip-top shape."
    scene e07s04-96-mc-walking-away with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Of course, [e07_lcname!t]."
    scene e07s04-06-lc-talking with dissolve
    play voice3 dahlia_arrogant_ha noloop
    lc "And, [e07_arjname!t]."
    scene e07s04-19-arj-shot with dissolve
    play voice4 amrose_yes_ugu noloop
    arj "Uhm, yes, [e07_lcname!t]?"
    scene e07s04-13-lc-asking with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    lc "I want you to clean up the dungeon. Make sure the strap-ons are tidy, floors mopped."
    scene e07s04-26-arj-following with dissolve
    play voice4 amrose_yes_okay2 noloop
    arj "Of course, [e07_lcname!t]."
    scene e07s04-15-lc-wicked-smile with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    lc "And as a reward for doing that, you can stay and watch [e07_pbname!t] do his job."
    scene e07s04-95-pb-talking with dissolve
    play voice5 pete_surprised_huh1 noloop
    pb "And what am I going to be doing?"
    scene e07s04-22-lc-angry with dissolve
    play voice3 dahlia_angry_argh1 noloop
    lc "Fucking me, of course. This whole event has just made me so insanely wet. I need to be satisfied."
    $ unlock_gallery_slot("scene", "e07s04")
    scene e07s04-38-mc-lc-talking with dissolve
    play voice3 dahlia_happy_yeah noloop
    lc "All right, everyone - chop, chop!"

    stop music fadeout 3.0
    jump e07s05

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
