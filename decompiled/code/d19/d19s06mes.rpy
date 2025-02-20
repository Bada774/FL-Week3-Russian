image d19s06mes-a1_smack = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a72-1-2x-60fps.webm", start_image = "d19s06mes-a72-1 mc-mes-cl-paddle-03_i")
image d19s06mes-a2_smack = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a72-2-2x-60fps.webm", start_image = "d19s06mes-a72-2 mc-mes-cl-paddle-03_i")
image d19s06mes-a3_smack = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a72-3-2x-50fps.webm", start_image = "d19s06mes-a72-3 mc-mes-cl-paddle-03_i")
image d19s06mes-a4_smack = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a72-4-2x-60fps.webm", start_image = "d19s06mes-a72-4 mc-mes-cl-paddle-03_i")

image d19s06mes-a1_glam = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a94-3-1-4x-60fps.webm", start_image = "d19s06mes-a94-3-1 mes-galmbot-94-3-1-00_i", image = "d19s06mes-a94-3-1 mes-galmbot-94-3-1-78_i", loop = False)
image d19s06mes-a2_glam = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a94-3-2-4x-60fps.webm", start_image = "d19s06mes-a94-3-2 mes-galmbot-94-3-2-00_i", image = "d19s06mes-a94-3-2 mes-galmbot-94-3-2-78_i", loop = False)

image d19s06mes-a1_start = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a109-4-4x-60fps.webm", start_image = "d19s06mes-a109-4 mc-mes-cl-cynthias-punishment-00")
image d19s06mes-a2_start = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a109-6-4x-60fps.webm", start_image = "d19s06mes-a109-6 mc-mes-cl-cynthias-punishment-00")

image d19s06mes-a1-f = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a109-1-2x-50fps.webm", start_image = "d19s06mes-a109-1 mc-mes-cl-cynthias-punishment-00")
image d19s06mes-a1 = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a109-1-4x-60fps.webm", start_image = "d19s06mes-a109-1 mc-mes-cl-cynthias-punishment-00")
image d19s06mes-a2-f = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a109-2-2x-50fps.webm", start_image = "d19s06mes-a109-2 mc-mes-cl-cynthias-punishment-00")
image d19s06mes-a2 = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a109-2-4x-60fps.webm", start_image = "d19s06mes-a109-2 mc-mes-cl-cynthias-punishment-00")
image d19s06mes-a3-f = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a109-3-2x-50fps.webm", start_image = "d19s06mes-a109-3 mc-mes-cl-cynthias-punishment-00")
image d19s06mes-a3 = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a109-3-4x-60fps.webm", start_image = "d19s06mes-a109-3 mc-mes-cl-cynthias-punishment-00")
image d19s06mes-a4-f = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a109-5-2x-50fps.webm", start_image = "d19s06mes-a109-5 mc-mes-cl-cynthias-punishment-00")
image d19s06mes-a4 = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a109-5-4x-60fps.webm", start_image = "d19s06mes-a109-5 mc-mes-cl-cynthias-punishment-00")

image d19s06mes-a1_piss = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a184-1-2x-50fps.webm", start_image = "d19s06mes-a184-1 mc-mes-cl-piss-anim-184-1-00")
image d19s06mes-a2_piss = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a184-2-2x-50fps.webm", start_image = "d19s06mes-a184-2 mc-mes-cl-piss-anim-184-2-00")
image d19s06mes-a3_piss = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a187-1-2x-50fps.webm", start_image = "d19s06mes-a187-1 mc-mes-cl-piss-anim-187-1-00")
image d19s06mes-a4_piss = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a187-2-2x-50fps.webm", start_image = "d19s06mes-a187-2 mc-mes-cl-piss-anim-187-2-00")
image d19s06mes-a5_piss = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a188-1-2x-50fps.webm", start_image = "d19s06mes-a188-1 mc-mes-cl-piss-anim-188-1-00")
image d19s06mes-a6_piss = Movie(play = "images/Day-19/s06mes/anim/d19s06mes-a188-2-2x-50fps.webm", start_image = "d19s06mes-a188-2 mc-mes-cl-piss-anim-188-2-00")

label d19s06mes:

    $ d19s06_mes = True

    scene black
    show screen scene_transistion(_("20 minutes later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.5, 0.0, "sound4")
    play sound4 park fadein 3.0
    scene d19s06mes-00 mc_mes_cl_cynthias_punishment
    with Fade(0.5, 0.5, 0.9)
    pause
    play sound knockknock
    scene d19s06mes-01 mc_mes_cl_cynthias_punishment with dissolve
    pause
    play sound sfx_door_open6
    scene d19s06mes-02 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_hey_greeting noloop
    mes "Hey [mcname]. Glad you could make it."
    scene d19s06mes-03 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "I got your message.{w} It wasn't specific..."
    scene d19s06mes-04 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_thinking_hmm3 noloop
    mes "Trust me. You're going to love this."
    scene d19s06mes-05 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "What is it?"
    scene d19s06mes-06 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_yes_ugu noloop
    mes "Follow me. I'll show you."
    play sound sfx_door_closed5
    scene d19s06mes-07 mc_mes_cl_cynthias_punishment with dissolve
    pause
    scene d19s06mes-08 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_happy_yay noloop
    mes "Tah-dah!!"
    scene d19s06mes-09 mc_mes_cl_cynthias_punishment with dissolve
    $ renpy.music.set_volume(0.5, 0.7, "music")
    play music felt_in_sex
    play voice2 mc_surprised_wow3 noloop
    mc "Wow!{w} Um, hi Cynthia."
    scene d19s06mes-10 mc_mes_cl_cynthias_punishment with dissolve
    play voice4 cynthia_scared_ah1 noloop
    cl "OMG!{w} Is he... your assistant?"
    scene d19s06mes-11 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 d1s1_mmm noloop
    mct "Holy crap! What is going on here?!"
    play voice3 min_yes_active noloop
    mes "He is, and he addressed you."
    scene d19s06mes-12 mc_mes_cl_cynthias_punishment with dissolve
    play voice4 cynthia_thinking_oh noloop
    cl "Oh, I'm sorry.{w} Hi [mcname]."
    scene d19s06mes-13 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 d4s4_mclaugh noloop
    mc "I have no idea what is going on here{w}, but I love it!"
    scene d19s06mes-14 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_arrogant_huh1 noloop
    mes "As you know, Cynthia is one of my best friends."
    scene d19s06mes-15 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Right."
    scene d19s06mes-16 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_arrogant_hm noloop
    mes "And I'm very close with her mother as well."
    scene d19s06mes-17 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "I see."
    scene d19s06mes-18 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_surprised_ehh2 noloop
    mes "Cynthia, why don't you tell [mcname] why you are here?"
    scene d19s06mes-19 mc_mes_cl_cynthias_punishment with dissolve
    play voice4 cynthia_disappointed_geh noloop
    cl "I'm a whore and a slut and deserve to be punished."
    scene d19s06mes-20 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_yes_yeah1 noloop
    mes "What else?"
    scene d19s06mes-21 mc_mes_cl_cynthias_punishment with dissolve
    play voice4 cynthia_disappointed_oof noloop
    cl "I am a punishment slut who needs to be abused in ways my mother cannot."
    scene d19s06mes-22 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_happy_yeah noloop
    mes "Isn't this delightful?!{w} Of course, I thought of you when she came to me."
    scene d19s06mes-23 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "Thank you, I think."
    scene d19s06mes-24 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_thinking_hmm2 noloop
    mes "Of course, I checked with her mother after Cynthia arrived. She confirmed her daughter is in dire need of humiliation, discipline, and correction."
    scene d19s06mes-25 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 d2s9_confused noloop volume 1.5
    mc "And you want me to..."
    scene d19s06mes-26 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_yes_simple noloop
    mes "Help me punish her, of course!"
    mes "With your cock, as much as possible."
    scene d19s06mes-27 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "I don't know... if she's such a slut... maybe the best punishment would be to withhold my cock from her correction."
    scene d19s06mes-28 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_happy_mmm noloop
    mes "Whatever you think is best. The important thing is that we have carte blanche."
    scene d19s06mes-29 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "You don't mean-"
    scene d19s06mes-30 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_old_laugh noloop
    mes "I mean, obviously we shouldn't murder or maim her, but we can play with her to within an inch of traumatizing her without consequence."
    scene d19s06mes-31 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "You're talking about torture."
    scene d19s06mes-32 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_yes_happy noloop
    mes "YES! Within reason, of course."
    scene d19s06mes-33 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.7
    mc "Interesting. We should set some ground rules."
    scene d19s06mes-34 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_yes_yeah2 noloop
    mes "I concur.{w} Her mom said that permanent marks are okay. If we want to tattoo a penis on her face she's okay with it, but that's a bit excessive to me."
    scene d19s06mes-35 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_thinking_hmm4 noloop
    if hasattr(renpy.store, "date_mes_info"):
        mc "Let's set up safe words. You know mine from last week."
    else:
        mc "Let's set up safe words. You know mine. If I think you're going too far, I'll say [mc_safeword]."
    scene d19s06mes-36 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_old_hmm noloop volume 1.6
    mes "Fair enough. If I think you're going too far, I'll say tomato."
    scene d19s06mes-37 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "You got a little sick just saying that word, didn't you."
    scene d19s06mes-38 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_arrogant_heh2 noloop
    mes "You know me too well."
    scene d19s06mes-39 mc_mes_cl_cynthias_punishment with dissolve
    play voice4 cynthia_disappointed_ehh noloop volume 0.8
    cl "If anyone wants to know, my safe word is Caligula."
    scene d19s06mes-40 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_yes_aga noloop
    mes "Good for you.{w} Where did I put that gag?"
    scene d19s06mes-41 mc_mes_cl_cynthias_punishment with dissolve
    pause
    play sound ["<silence 0.25>", sfx_underpants_off1] volume 3.0
    scene d19s06mes-42 mc_mes_cl_cynthias_punishment with dissolve
    play voice4 cynthia_sex_closedmoan3 noloop
    pause
    scene d19s06mes-43 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_thinking_emm noloop
    mes "If you need to use your safe word..."
    mes "Just shut the fuck up and take it."
    play sound sfx_tracker_cuff1
    scene d19s06mes-44 mc_mes_cl_cynthias_punishment with dissolve
    play voice4 cynthia_arrogant_hm noloop
    cl "mmumph?!"
    scene d19s06mes-45 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_hey_simple noloop
    mes "Don't worry. We're your friends. You can trust us."
    scene d19s06mes-46 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Honestly, I wouldn't trust you if I were in her position."
    scene d19s06mes-47 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_disappointed_off noloop
    mes "Same."
    scene d19s06mes-48 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "If you really object to what we are doing, grunt three times."
    scene d19s06mes-49 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_disappointed_mph noloop
    mes "Pansy."
    scene d19s06mes-50 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What? I'm not about to-"
    scene d19s06mes-51 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_disappointed_ehh3 noloop
    mes "I know, I know. You're right.{w} If you grunt three times we'll stop what we're doing and remove the gag."
    scene d19s06mes-52 mc_mes_cl_cynthias_punishment with dissolve
    play voice4 cynthia_sex_closedmoan5 noloop
    cl "*tries to grunt \"Thank You\" through the ball gag*"
    scene d19s06mes-53 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_arrogant_huh2 noloop
    mes "Alright, how do you want her? Face down or face up?"
    scene d19s06mes-54 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Face up, definitely."

label replay_d19s06mes hide:

    if _in_replay:
        scene black with dissolve
        menu:
            "Do you want to see watersports?"
            "Yes":
                $ fl_watersports = True
                $ d15s07_more_watersports = True
                pass
            "No":

                $ fl_watersports = False
                $ d15s07_more_watersports = False
                pass
        $ renpy.music.set_volume(0.5, 0.7, "music")
        play music felt_in_sex
    scene d19s06mes-55 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_happy_woohoo noloop
    mes "Let's have some fun."
    scene d19s06mes-55-1 mc_mes_cl_cynthias_punishment with dissolve
    pause
    play sound sfx_sextoy_cuff1
    scene d19s06mes-55-2 mc_mes_cl_cynthias_punishment with dissolve
    queue sound sfx_sextoy_cuff2
    pause
    scene d19s06mes-56 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "How do you want to split this up? Should we take turns or-"
    scene d19s06mes-57 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_thinking_oh noloop
    mes "I figure you do whatever you want below the waist, and I'll do whatever I want above the waist."

    $ Lovense.stop()

    scene d19s06mes-58 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Sounds good to me."
    scene d19s06mes-59 mc_mes_cl_cynthias_punishment with dissolve
    $ Lovense.vibrate(1)
    queue voice2 mc_thinking_hmm5 noloop
    mc "You're sure she's okay with this?"
    scene d19s06mes-60 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_happy_relief noloop
    mes "She consented and hasn't complained yet."
    scene d19s06mes-61 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "You know what she would really love?"
    scene d19s06mes-62 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_no_nope noloop
    mes "Not really, but if I had to guess... Figging?"
    scene d19s06mes-63 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Do you mean just anal sex...{w} or with an actual ginger root?"
    play voice3 min_arrogant_heh1 noloop
    scene d19s06mes-64 mc_mes_cl_cynthias_punishment with dissolve
    play voice4 cynthia_sex_closedmoan6 noloop
    mes "Ginger, horseradish, wasabi...{w} I think she'd love the acute burning sensation up her rectum."
    scene d19s06mes-65 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "Well, she does seem to love anal sex."
    scene d19s06mes-66 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_no_uhuh noloop
    mes "Then again, she doesn't seem to be enjoying this conversation."
    scene d19s06mes-67 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "I don't suppose you have any-"
    scene d19s06mes-68 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_disgust_off noloop
    mes "I have that lube that advertised \"A Pleasant Warming Sensation\" which wasn't pleasant and burned like hell for hours."
    scene d19s06mes-69 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_disgust_pfe1 noloop
    mc "That doesn't sound like fun for anyone involved."
    scene d19s06mes-70 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_surprised_huh1 noloop
    mes "Why did you ask?"
    scene d19s06mes-71 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "I have an idea.{w} I'll tell you about it later."
    scene d19s06mes-a72-1 mc-mes-cl-paddle-03_i with dissolve
    pause
    $ renpy.music.set_volume(1.0, 1.7, "music")
    play voice4 "<silence 0.5>" noloop
    queue voice4 cynthia_sex_closedmoans1
    $ renpy.music.set_volume(1.0, 0.0, "sound2")
    play sound2 ["<silence 0.6>", spank1, "<silence 1.3>", spank2, "<silence 1.2>", sfx_whip_slap2, "<silence 0.5>"]
    play sound ["<silence 0.3>", sfx_whip_slap1, "<silence 1.0>", sfx_whip_slap3, "<silence 1.0>", sfx_whip_slap4, "<silence 1.1>", sfx_whip_slap5, "<silence 0.74>"] loop
    $ Lovense.vibrate(5)
    scene d19s06mes-a1_smack
    pause
    play sound2 ["<silence 0.6>", spank1, "<silence 1.3>", spank2, "<silence 1.2>", sfx_whip_slap2, "<silence 0.5>"]
    play sound ["<silence 0.3>", sfx_whip_slap1, "<silence 1.0>", sfx_whip_slap3, "<silence 1.0>", sfx_whip_slap4, "<silence 1.1>", sfx_whip_slap5, "<silence 0.74>"] loop
    scene d19s06mes-a2_smack with dissolve
    pause
    play sound2 ["<silence 0.6>", spank1, "<silence 1.7>", spank2, "<silence 1.5>", sfx_whip_slap2, "<silence 0.8>"]
    play sound ["<silence 0.3>", sfx_whip_slap1, "<silence 1.0>", sfx_whip_slap3, "<silence 1.0>", sfx_whip_slap4, "<silence 1.1>", sfx_whip_slap5, "<silence 0.74>"] loop
    scene d19s06mes-a3_smack with dissolve
    pause
    play sound2 ["<silence 0.6>", spank1, "<silence 1.3>", spank2, "<silence 1.2>", sfx_whip_slap2, "<silence 0.5>"]
    play sound ["<silence 0.3>", sfx_whip_slap1, "<silence 1.0>", sfx_whip_slap3, "<silence 1.0>", sfx_whip_slap4, "<silence 1.1>", sfx_whip_slap5, "<silence 0.74>"] loop
    scene d19s06mes-a4_smack with dissolve
    pause
    stop sound2 fadeout 1.0
    stop sound fadeout 1.0
    $ renpy.music.set_volume(0.5, 1.7, "music")
    $ Lovense.vibrate(3)
    scene d19s06mes-74 mc_mes_cl_cynthias_punishment with dissolve
    play voice4 amrose_pain_sobs3 noloop
    cl "*Whimpers in pain.*"
    scene d19s06mes-75 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_surprised_wow noloop
    mes "Wow! That definitely got a reaction."
    scene d19s06mes-76 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 d9s2_yeah noloop volume 3.0
    mc "Yeah, after all that teasing and building up fear, here comes the pain."
    scene d19s06mes-77 mc_mes_cl_cynthias_punishment with dissolve
    play voice4 cynthia_sex_closedmoan5 noloop
    pause
    $ Lovense.vibrate(2)
    scene d19s06mes-78 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_surprised_ehh1 noloop
    mes "I don't know if pain is the right word...{w} She seems to be orgasming."
    scene d19s06mes-79 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Interesting.{w} How's her tits going?"
    scene d19s06mes-80 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_thinking_mhh noloop
    mes "There will be purple bruises in a few hours, but otherwise it didn't seem to have much effect."
    scene d19s06mes-81 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Say Squizzle, could you fetch me a couple of ice cubes?"
    scene d19s06mes-82 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_happy_wooh noloop
    mesfl "Woof?"
    scene d19s06mes-83 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_happy_a1 noloop
    mc "I'm sorry. Let me rephrase that."
    mc "Min, would you kindly get me a couple of ice cubes, please?"
    scene d19s06mes-84 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_angry_cough noloop
    mes "Much better."
    scene d19s06mes-85 mc_mes_cl_cynthias_punishment with dissolve
    pause
    scene d19s06mes-86 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "While we have a little time to ourselves..."
    $ Lovense.vibrate(4)
    scene d19s06mes-87 mc_mes_cl_cynthias_punishment with dissolve
    mc "...you should know that I'm planning to creampie your little pussy."
    mc "Is that okay with you?"
    scene d19s06mes-88 mc_mes_cl_cynthias_punishment with dissolve
    play voice4 cynthia_yes_ugu noloop
    pause
    scene d19s06mes-89 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.7
    mc "Good. I thought so."
    mc "Don't worry. I have plans to make it more interesting.{w} You're going to love it."
    $ Lovense.vibrate(2)
    scene d19s06mes-90 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_surprised_huh2 noloop
    mes "Here you are, [mcname]. Do you mind if I ride her face for a bit?"
    scene d19s06mes-91 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Please do. You can even remove the gag if you like."
    scene d19s06mes-92 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_no_happy noloop
    mes "Oh, no. I'd prefer to cum while she's gagged."
    play sound sfx_plate_place1
    scene d19s06mes-93 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Grunt thrice if that's not okay with you."
    pause
    scene d19s06mes-94 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_thinking_hmm2 noloop
    mes "It seems we have our answer."
    scene d19s06mes-94-1 mc_mes_cl_cynthias_punishment with dissolve
    pause
    play sound sfx_throw_something1 volume 0.5
    scene d19s06mes-94-2 mc_mes_cl_cynthias_punishment with dissolve
    pause
    play sound sfx_bed_slide3 volume 0.5
    scene d19s06mes-a94-3-1 mes-galmbot-94-3-1-00_i with dissolve
    pause
    $ renpy.music.set_volume(1.0, 0.7, "music")
    play sound sfx_camera_fly1 volume 2.0
    scene d19s06mes-a1_glam
    pause
    play sound sfx_camera_fly1 volume 2.0
    scene d19s06mes-a2_glam with dissolve
    pause
    $ renpy.music.set_volume(0.5, 0.7, "music")
    scene d19s06mes-94-3 mc_mes_cl_cynthias_punishment with dissolve
    pause
    scene d19s06mes-95 mc_mes_cl_cynthias_punishment with dissolve
    pause
    play voice3 min_surprised_oh noloop
    mes "Oh, that's perfect."
    scene d19s06mes-96 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 d1s1_mmm noloop
    mct "Now for my little surprise."
    play sound sfx_ice_cubes1
    scene d19s06mes-97 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_pain_ah noloop
    mes "What are you doing back there?"
    scene d19s06mes-98 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_happy_hah1 noloop
    mc "I'm going to see if she can buck us off in 8 seconds."
    scene d19s06mes-99 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_scared_huh noloop
    mes "Like Bull Riding?"
    scene d19s06mes-100 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Exactly."
    $ renpy.music.set_volume(0.7, 0.7, "music")
    scene d19s06mes-101 mc_mes_cl_cynthias_punishment with dissolve
    pause
    scene d19s06mes-102 mc_mes_cl_cynthias_punishment with dissolve
    pause
    scene d19s06mes-103 mc_mes_cl_cynthias_punishment with dissolve
    pause
    scene d19s06mes-104 mc_mes_cl_cynthias_punishment with dissolve
    $ Lovense.vibrate(5)
    play voice4 cynthia_sex_closedmoan6 noloop
    pause
    scene d19s06mes-105 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_surprised_ohmy noloop
    mes "Woah! That got her going!!"
    scene d19s06mes-106 mc_mes_cl_cynthias_punishment with dissolve
    pause
    scene d19s06mes-107 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_thinking_hmm1 noloop
    pause
    scene d19s06mes-108 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 d4s4_mclaugh noloop
    pause
    scene d19s06mes-a1_start with dissolve
    $ renpy.music.set_volume(1.0, 0.7, "music")
    play voice2 mc_happy_wooh1 noloop
    queue voice2 d7s4_mcbreathing
    play voice3 min_old_moans
    play voice4 cynthia_sex_closedmoans1
    $ Lovense.pattern("6;10", 1700)
    mc "Woo hoo!"
    pause
    scene d19s06mes-a2_start with dissolve
    mes "Fuck yes!!"
    pause
    scene d19s06mes-a1 with dissolve
    pause
    scene d19s06mes-a2 with dissolve
    pause
    scene d19s06mes-a3 with dissolve
    pause
    scene d19s06mes-a4 with dissolve
    pause
    $ Lovense.pattern("6;10", 900)
    scene d19s06mes-a1-f with dissolve
    pause
    scene d19s06mes-a2-f with dissolve
    pause
    scene d19s06mes-a3-f with dissolve
    pause
    scene d19s06mes-a4-f with dissolve
    pause
    play voice3 min_old_orgasm1 noloop
    $ Lovense.stop()
    $ Lovense.vibrate(14)
    scene d19s06mes-110 mc_mes_cl_cynthias_punishment with vpunch
    mes "FUCK YES!!!!!!"
    scene d19s06mes-111 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_pain_ffff noloop
    mc "Right Behind You!!!"
    play voice4 cynthia_sex_closedmoan6 noloop
    play voice2 d1s5_orgasm2 noloop
    $ Lovense.vibrate(16)
    with hpunch
    mc "OOoooo FUCK!!!"
    play voice3 min_scared_ah1 noloop
    scene d19s06mes-112 mc_mes_cl_cynthias_punishment with vpunch
    mes "Oooph!"
    play sound sfx_fall_down1
    $ Lovense.vibrate(3)
    scene d19s06mes-113 mc_mes_cl_cynthias_punishment with vpunch
    pause
    $ renpy.music.set_volume(0.5, 1.7, "music")
    play voice3 min_scared_ah2 noloop
    mes "I'm okay! I'm okay!"
    scene d19s06mes-114 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_scared_oh3 noloop
    mc "Are you sure?"
    scene d19s06mes-115 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_disappointed_ehh1 noloop
    mes "Jelly legs.{w} She knocked me off after I came."
    scene d19s06mes-116 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Understandable."
    $ Lovense.vibrate(1)
    scene d19s06mes-117 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_disappointed_ehh2 noloop
    mes "There you are. I think we're finished with you for today."
    play sound ["<silence 0.25>", sfx_underpants_off1] volume 3.0
    scene d19s06mes-118 mc_mes_cl_cynthias_punishment with dissolve
    play voice4 cynthia_scared_oof noloop
    cl "You-"
    scene d19s06mes-119 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Are you okay?"
    scene d19s06mes-120 mc_mes_cl_cynthias_punishment with dissolve
    play voice4 cynthia_angry_dough noloop
    cl "I'm fine, but Min, dammit.{w} I couldn't breathe."
    scene d19s06mes-121 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_surprised_what noloop
    mes "What? When?!"
    scene d19s06mes-122 mc_mes_cl_cynthias_punishment with dissolve
    play voice4 cynthia_arrogant_he noloop
    cl "You covered my nose and mouth when you came. I had to knock you off."
    scene d19s06mes-123 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_old_argh noloop
    mes "Shit, Cynthia. I'm sorry."
    scene d19s06mes-124 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Well, at least that tells us something."
    scene d19s06mes-125 mc_mes_cl_cynthias_punishment with dissolve
    play voice4 cynthia_thinking_ha noloop
    cl "What's that?"
    scene d19s06mes-126 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "You object to being smothered."
    scene d19s06mes-127 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_old_laugh noloop
    mes "*laughing* True."
    scene d19s06mes-128 mc_mes_cl_cynthias_punishment with dissolve
    play voice4 cynthia_disappointed_ahh noloop
    cl "*sigh* I suppose I should thank you for finding my limits."
    scene d19s06mes-129 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, I doubt this will be the last time."
    scene d19s06mes-130 mc_mes_cl_cynthias_punishment with dissolve
    play voice3 min_yes_aga noloop
    mes "We're looking forward to punishing you again - anytime you want it."
    scene d19s06mes-131 mc_mes_cl_cynthias_punishment with dissolve
    play voice4 cynthia_yes_yeah1 noloop
    cl "Sounds good to me.{w} But after today, I might need a week or two to recover."
    scene d19s06mes-132 mc_mes_cl_cynthias_punishment with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Take all the time you need."

    if d15s07_more_watersports is True and fl_watersports is True:
        scene d19s06mes-133 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 cynthia_sex_closedmoan2 noloop
        cl "Min... er, Mistress Min... er, whatever?"
        scene d19s06mes-134 mc_mes_cl_cynthias_punishment with dissolve
        play sound sfx_sextoy_uncuff1
        play voice3 min_hey_simple noloop
        mes "We're done with the punishment, Cynthia. I'm just your friend Min now."
        scene d19s06mes-135 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 cynthia_yes_aga noloop
        cl "Sure. Can I ask you a question?"
        play sound sfx_sextoy_uncuff1
        scene d19s06mes-136 mc_mes_cl_cynthias_punishment with dissolve
        play voice3 min_yes_yeah1 noloop
        mes "Of course. What's up?"
        scene d19s06mes-137 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 cynthia_thinking_hmm5 noloop
        cl "Last week... at your party... you said you could only cum..."
        scene d19s06mes-138 mc_mes_cl_cynthias_punishment with dissolve
        play voice3 min_old_huh noloop
        mes "If I had pee in my mouth?"
        scene d19s06mes-139 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 cynthia_yes_yep1 noloop
        cl "But, I'm pretty sure you came all over my face just now."
        scene d19s06mes-140 mc_mes_cl_cynthias_punishment with dissolve
        play voice2 mc_thinking_hmm1 noloop
        mc "Min completed her training. She's allowed to cum without urine now."
        scene d19s06mes-141 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 cynthia_surprised_huh noloop
        cl "Huh? I'm confused."
        scene d19s06mes-142 mc_mes_cl_cynthias_punishment with dissolve
        play voice2 mc_arrogant_heh2 noloop
        mct "Shocking. I'm pretty sure that being confused is Cynthia's natural state."
        play voice3 min_old_hmm noloop
        mes "[mcname] was training me.{w} I needed it."
        scene d19s06mes-143 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 cynthia_surprised_ah noloop
        cl "You were...{w} training her?"
        scene d19s06mes-144 mc_mes_cl_cynthias_punishment with dissolve
        play voice2 mc_yes_yes1 noloop
        mc "Yes. She's competitive, ya'know?"
        scene d19s06mes-145 mc_mes_cl_cynthias_punishment with dissolve
        play voice3 min_old_mff noloop volume 1.5
        mes "He beat me at a pissing contest by drinking the bowl."
        scene d19s06mes-146 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 cynthia_surprised_what noloop
        cl "WTF?!{w} I mean, I see how that...{w} Nope, I'm still back at WTF."
        scene d19s06mes-147 mc_mes_cl_cynthias_punishment with dissolve
        play voice3 min_thinking_emm noloop
        mes "I couldn't let him just beat me at something and then walk away, so I asked him to train me."
        scene d19s06mes-148 mc_mes_cl_cynthias_punishment with dissolve
        play voice2 mc_thinking_emm1 noloop
        mc "Begged, more like it."
        scene d19s06mes-149 mc_mes_cl_cynthias_punishment with dissolve
        play voice3 min_old_upset noloop volume 2.5
        mes "I don't really remember the details. But, he agreed to help my get over my, uh...{w} urine phobia?"
        scene d19s06mes-150 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 cynthia_sex_closedmoan4 noloop
        cl "So, now you drink piss."
        scene d19s06mes-151 mc_mes_cl_cynthias_punishment with dissolve
        play voice2 mc_thinking_hmm2 noloop
        mc "It's not bad. Just like white grape juice."
        scene d19s06mes-152 mc_mes_cl_cynthias_punishment with dissolve
        play voice3 min_yes_happy noloop
        mes "Yes. It's actually quite enjoyable."
        scene d19s06mes-153 mc_mes_cl_cynthias_punishment with dissolve
        play voice2 mc_arrogant_huh3 noloop
        mc "Associating drinking urine with orgasms was just part of the training, but worked along a Pavlovian response. Connecting the taste of pee with the pleasure of sex."
        scene d19s06mes-154 mc_mes_cl_cynthias_punishment with dissolve
        play voice3 cynthia_thinking_hmm4 noloop
        cl "I see."
        scene d19s06mes-155 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 min_surprised_huh1 noloop
        mes "Would you like to try?"
        scene d19s06mes-156 mc_mes_cl_cynthias_punishment with dissolve
        play voice3 cynthia_thinking_hmm1 noloop
        cl "You mean, as a punishment? For you to further humiliate me by pissing in my face."
        scene d19s06mes-157 mc_mes_cl_cynthias_punishment with dissolve
        play voice2 mc_no_no1 noloop
        mc "No, as a new sexual experience."
        scene d19s06mes-158 mc_mes_cl_cynthias_punishment with dissolve
        play voice3 min_happy_yeah noloop
        mes "To expose you to the pleasure of tasting the golden liquid."
        scene d19s06mes-159 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 cynthia_disappointed_oof noloop
        cl "I'm not sure..."
        scene d19s06mes-160 mc_mes_cl_cynthias_punishment with dissolve
        play voice3 min_surprised_ehh2 noloop
        mes "I could order you to do it - as a punishment - if you prefer."
        scene d19s06mes-161 mc_mes_cl_cynthias_punishment with dissolve
        play voice2 mc_no_no2 noloop
        mc "No. It should be her choice."
        scene d19s06mes-162 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 cynthia_disappointed_ehh noloop
        cl "I mean...{w} On the one hand, it's not something I'd ever want to try. On the other hand, there are probably tons of people with this fetish that get off on it."
        scene d19s06mes-163 mc_mes_cl_cynthias_punishment with dissolve
        play voice2 mc_yes_yeah6 noloop
        mc "You'll never know unless you try."
        scene d19s06mes-164 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 cynthia_sex_closedmoan2 noloop
        cl "Can you please do it as a humiliation? I think I could get off on that."
        scene d19s06mes-165 mc_mes_cl_cynthias_punishment with dissolve
        play voice2 mc_arrogant_huh1 noloop
        mc "Huh?"
        scene d19s06mes-166 mc_mes_cl_cynthias_punishment with dissolve
        play voice3 min_thinking_hmm3 noloop
        mes "I think she wants me to order her to do it."
        scene d19s06mes-167 mc_mes_cl_cynthias_punishment with dissolve
        play voice2 d2s12_emmm noloop volume 1.4
        mc "I'm not sure...{w} Now I'm confused."
        scene d19s06mes-168 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 cynthia_happy_mmm noloop
        cl "I don't want to consent to just getting peed on, but I will eagerly consent to the humiliation of being peed on as a punishment for my...{w} whatever excuse you come up with."
        scene d19s06mes-169 mc_mes_cl_cynthias_punishment with dissolve
        play voice2 mc_disappointed_ah2 noloop
        mc "Now my eyes have gone crossed.{w} I think there's a screw loose somewhere nearby."
        scene d19s06mes-170 mc_mes_cl_cynthias_punishment with dissolve
        play voice3 min_arrogant_huh1 noloop
        mes "Don't worry. I understand it.{w} Cynthia, I demand that you kneel down like the slut you are and let [mcname] piss in our mouths."
        scene d19s06mes-171 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 cynthia_yes_angry noloop
        cl "Yes, ma'am!"
        scene d19s06mes-172 mc_mes_cl_cynthias_punishment with dissolve
        pause
        play voice3 min_no_nonono noloop
        mes "No, no, no. That won't do at all.{w} Open your eyes and look at his magnificent penis."
        scene d19s06mes-173 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 cynthia_arrogant_hm noloop
        cl "It's going to pee on me. How is that magnificent?"
        scene d19s06mes-174 mc_mes_cl_cynthias_punishment with dissolve
        play voice3 min_disappointed_ehh3 noloop
        mes "He's not just going to pee on you. Open your mouth wide, now!"
        scene d19s06mes-a184-1_mc-mes-cl-piss-anim-184-1-00 with dissolve
        pause
        $ renpy.music.set_volume(0.8, 0.7, "music")
        play voice3 min_old_sinking fadein 1.0
        $ renpy.music.set_volume(0.2, 0.0, "sound2")
        $ renpy.music.set_volume(0.7, 0.0, "sound3")
        play sound2 sfx_piss_loop1 fadein 0.5
        play sound3 sfx_piss_loop2 fadein 0.5
        $ Lovense.vibrate(6)
        scene d19s06mes-a1_piss with Dissolve(0.8)
        pause
        play voice4 cynthia_scared_ah1 noloop
        cl "OMG! You're really doing it!"
        scene d19s06mes-a2_piss with dissolve
        pause
        play voice2 mc_hey_hey2 noloop
        mc "You're next, unless-"
        play voice3 cynthia_yes_happy noloop
        cl "Okay!"
        stop sound2 fadeout 1.0
        stop sound3 fadeout 1.0
        stop voice3 fadeout 1.0
        $ Lovense.vibrate(3)
        scene d19s06mes-a187-1_mc-mes-cl-piss-anim-187-1-00 with dissolve
        play voice3 cynthia_scared_ah3 noloop
        cl "I'm ready!!!"
        play sound2 sfx_piss_loop1 fadein 0.5
        play sound3 sfx_piss_loop2 fadein 0.5
        $ Lovense.vibrate(8)
        scene d19s06mes-a3_piss with Dissolve(0.8)
        play voice4 cynthia_sex_watersports
        cl "GAAHAHHHAHAHHAAH!!!"
        pause
        scene d19s06mes-a4_piss with dissolve
        pause
        play voice3 min_old_aww noloop volume 1.4
        mes "Doesn't that feel and taste amazing?!"
        stop sound2 fadeout 1.0
        stop sound3 fadeout 1.0
        $ Lovense.vibrate(2)
        scene d19s06mes-180 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 cynthia_disappointed_ahh noloop
        cl "I think I need more practice."
        scene d19s06mes-181 mc_mes_cl_cynthias_punishment with dissolve
        play voice2 mc_hey_hey5 noloop
        mc "Well, you're in luck."
        scene d19s06mes-182 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 cynthia_disgust_offf noloop
        cl "Oh fuck..."
        play voice4 cynthia_sex_watersports
        play sound2 sfx_piss_loop1
        play sound3 sfx_piss_loop2
        $ Lovense.vibrate(8)
        scene d19s06mes-a3_piss with dissolve
        pause
        scene d19s06mes-a4_piss with dissolve
        pause
        play voice3 min_old_disgusted noloop
        mes "Don't forget about me!"
        stop voice4 fadeout 1.0
        $ Lovense.vibrate(9)
        scene d19s06mes-a1_piss with dissolve
        play voice3 min_old_sinking fadein 1.0
        play voice4 cynthia_happy_relief noloop
        cl "Oh fuck yes."
        pause
        scene d19s06mes-a2_piss with dissolve
        pause
        play voice2 mc_yes_yeah8 noloop
        mc "You enjoy it?"
        play voice4 cynthia_disappointed_geh noloop
        cl "I don't think my nips and clit have ever been so hard."
        cl "I want it all over my face!"
        stop voice3 fadeout 1.0
        $ renpy.music.set_volume(0.6, 1.0, "sound2")
        $ renpy.music.set_volume(0.7, 1.0, "sound3")
        $ Lovense.vibrate(10)
        scene d19s06mes-a5_piss with dissolve
        play voice4 cynthia_sex_openmoans1
        cl "FUCK YES!{w} HUMILIATE ME LIKE THE DIRTY PISS WHORE I AM!!"
        pause
        scene d19s06mes-a6_piss with dissolve
        cl "NEXT TIME YOU NEED TO FILM THIS!!!"
        pause
        stop sound2 fadeout 1.0
        stop sound3 fadeout 1.0
        stop voice4 fadeout 1.0
        scene d19s06mes-190 mc_mes_cl_cynthias_punishment with dissolve
        $ Lovense.vibrate(2)
        play voice2 mc_arrogant_hm1 noloop
        $ renpy.music.set_volume(0.5, 0.7, "music")
        mc "That's all I've got. If you want more, you're going to have to provide it yourself."
        scene d19s06mes-191 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 cynthia_surprised_huh noloop
        cl "What do you mean?"
        scene d19s06mes-192 mc_mes_cl_cynthias_punishment with dissolve
        play voice3 min_arrogant_huh2 noloop
        mes "You know how I always carry a water bottle?"
        scene d19s06mes-193 mc_mes_cl_cynthias_punishment with dissolve
        play voice4 cynthia_no_calm noloop
        cl "No.{w}.. really?"
    else:
        play sound sfx_sextoy_uncuff1
        scene d19s06mes-134 mc_mes_cl_cynthias_punishment with dissolve
        pause
        scene d19s06mes-135 mc_mes_cl_cynthias_punishment with dissolve
        play sound sfx_sextoy_uncuff1
        play voice4 cynthia_disappointed_geh noloop
        cl "Thanks for all of this Min."
        scene d19s06mes-136 mc_mes_cl_cynthias_punishment with dissolve
        play voice3 min_yes_happy noloop
        mes "I enjoyed it a lot as well."

    scene d19s06mes-194 mc_mes_cl_cynthias_punishment with dissolve

    $ Lovense.stop()

    play voice3 min_thinking_hmm1 noloop
    mes "I haven't had that much fun since she went into the Pandora room."
    $ renpy.end_replay()
    $ unlock_gallery_slot("scene", "d19s06mes")

    jump d19s06_lewald
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
