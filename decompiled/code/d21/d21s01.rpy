image d21s01-a1 = Movie(play = "images/Day-21/s01/anim/d21s01-a40-03-1-2x-50fps.webm", start_image = "d21s01-a40-03-01 mc-hr-bj-anim-01")
image d21s01-a1-f = Movie(play = "images/Day-21/s01/anim/d21s01-a40-03-1-2x-60fps.webm", start_image = "d21s01-a40-03-01 mc-hr-bj-anim-01")

image d21s01-a2 = Movie(play = "images/Day-21/s01/anim/d21s01-a40-03-2-2x-50fps.webm", start_image = "d21s01-a40-03-02 mc-hr-bj-anim-01")
image d21s01-a2-f = Movie(play = "images/Day-21/s01/anim/d21s01-a40-03-2-2x-60fps.webm", start_image = "d21s01-a40-03-02 mc-hr-bj-anim-01")

image d21s01-a3 = Movie(play = "images/Day-21/s01/anim/d21s01-a40-06-1-2x-50fps.webm", start_image = "d21s01-a40-06-01 mc-hr-bj-anim-01")
image d21s01-a3-f = Movie(play = "images/Day-21/s01/anim/d21s01-a40-06-1-2x-60fps.webm", start_image = "d21s01-a40-06-01 mc-hr-bj-anim-01")

image d21s01-a4 = Movie(play = "images/Day-21/s01/anim/d21s01-a40-06-2-2x-50fps.webm", start_image = "d21s01-a40-06-02 mc-hr-bj-anim-01")
image d21s01-a4-f = Movie(play = "images/Day-21/s01/anim/d21s01-a40-06-2-2x-60fps.webm", start_image = "d21s01-a40-06-02 mc-hr-bj-anim-01")

image d21s01-glambot-1 = Movie(play = "images/Day-21/s01/anim/d21s01-a24-02-2x-50fps.webm", start_image = "d21s01-a24-02 mc-hr-talking-anim-24-02-00_i", image = "d21s01-a24-02 mc-hr-talking-anim-24-02-78_i", loop = False)

label d21s01:

    $ d21s01_bj = False
    $ d21s01_roleplay = False
    $ d21s01_join_shower = False

    scene black
    show screen scene_transistion(_("Sunday\nDay-21"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.05, 0, "sound2" )
    $ renpy.music.set_volume(0.5, 0, "voice2" )
    $ renpy.music.set_volume(0.1, 0, "voice3" )
    play sound2 park
    play voice2 d7s6_snoring fadein 3.0
    play voice3 [chloe_disappointed_snoring, "<silence 3.0>"] fadein 5.0
    scene d21s01-01 mc-sleeping
    with Fade(0.4, 0.5, 0.5)
    pause
    $ renpy.music.set_volume(1.0, 1.5, "voice2" )
    scene d21s01-02 mc-opening-eyes with dissolve
    pause
    play voice2 d7s6_awake noloop
    scene d21s01-02-02 mc-opening-eyes with dissolve
    pause
    scene d21s01-03 mc-hr-her-sleeping with dissolve
    pause
    $ renpy.music.set_volume(0.4, 1.5, "voice3" )
    play sound sfx_cloth_planket2
    scene d21s01-03-02 mc-hr-her-sleeping with dissolve
    stop sound fadeout 1.0
    pause
    $ renpy.music.set_volume(0.2, 1.5, "voice3" )
    play sound sfx_cloth_rustling1
    scene d21s01-04 mc-hr-standing with dissolve
    play voice2 mc_thinking_mmm4 noloop volume 0.6
    pause
    $ renpy.music.set_volume(0.4, 1.5, "voice3" )
    play sound sfx_cloth_rustling4
    scene d21s01-05 mc-hr-pulling-down-the-duvet with dissolve
    pause
    play sound sfx_cloth_dress_off2
    scene d21s01-06 mc-hr-grabbing-her-arm with dissolve
    pause
    scene d21s01-06-02 mc-hr-grabbing-her-arm with dissolve
    pause
    play sound sfx_cloth_dress_off1 volume 3.0
    scene d21s01-06-03 mc-hr-grabbing-her-arm with dissolve
    pause
    play voice2 mc_thinking_hmm5 noloop volume 0.7
    $ renpy.music.set_volume(0.1, 1.5, "voice3" )
    scene d21s01-07 mc-sighing with dissolve
    pause
    play sound sfx_barefoot_steps1 volume 0.3
    scene d21s01-08 mc-going-to-desk with dissolve
    pause
    play sound sfx_chair_slide1
    queue sound sfx_phone_button1
    scene d21s01-09 mc-sitting-down with dissolve
    $ renpy.music.set_volume(0.0, 0, "music" )
    $ renpy.music.set_volume(1.0, 0, "music2")
    $ renpy.music.play(audio.calm_guitar_1, "music" , True, None, True, 1.0)
    $ renpy.music.play(audio.calm_guitar_1_muffled, "music2", True, None, True, 4.0)
    pause
    scene d21s01-10 mc-listehning-to-music with dissolve
    play voice2 d1s5b_ehhh noloop
    pause
    scene d21s01-10-02 mc-still-listehning-to-music with fade
    $ renpy.music.set_volume(0.6, 15.0, "music" )
    $ renpy.music.set_volume(0.0, 15.0, "music2")
    pause
    $ renpy.music.set_volume(1.0, 1.5, "voice3" )
    play voice3 chloe_disappointed_oh noloop
    scene d21s01-11 hr-waking-up with dissolve
    pause
    play sound sfx_cloth_rustling3
    scene d21s01-12 mc-hr-talking with dissolve
    pause
    scene d21s01-12-02 mc-hr-talking with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Good morning."
    scene d21s01-13 mc-hr-talking with dissolve
    play voice3 chloe_disappointed_ehh7 noloop
    hr "Morning."
    scene d21s01-13-02 mc-hr-talking with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Sounds like you were sleeping well."
    mc "You were snoring and everything."
    scene d21s01-14 mc-hr-talking with dissolve
    play voice3 chloe_surprised_huh3 noloop
    hr "Was I? What time is it?"
    scene d21s01-14-02 mc-hr-talking with dissolve
    play voice2 mc_happy_a1 noloop
    mc "It's eight."
    mc "You looked cute when you were sleeping."
    scene d21s01-13 mc-hr-talking with dissolve
    play voice3 hana_argh noloop
    hr "You weren't watching me. Only a pervert would do that."
    play voice2 mc_thinking_emm1 noloop
    mc "It's not like I was spying on you."
    hr "It's the definition of spying. Watching someone while they're most vulnerable."
    play voice2 mc_disappointed_ehh3 noloop
    scene d21s01-14-02 mc-hr-talking with dissolve
    mc "Ah, you'll get over it. I did."
    mc "Is this when you usually get up?"
    play sound sfx_cloth_rustling5
    scene d21s01-15 hr-getting-up with dissolve
    play voice3 chloe_no_simple noloop
    hr "No. I couldn't fall asleep at night. Something about sleeping in a foreign bed."
    scene d21s01-15-02 hr-getting-up with dissolve
    play voice3 hana_argh2 noloop
    hr "Shut it."
    scene d21s01-15-03 mc-hr-shrugging with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Wasn't going to make a joke."
    mc "I was curious about your schedule, is all."
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    scene d21s01-16 hr-grabbing-her-phone with dissolve
    pause
    scene d21s01-16-01 hr-grabbing-her-phone with dissolve
    pause
    play sound sfx_cloth_planket2
    scene d21s01-16-02 hr-grabbing-her-phone with dissolve
    pause
    scene d21s01-16-03 hr-grabbing-her-phone with dissolve
    pause
    play sound sfx_bandage_on1 volume 3.0
    scene d21s01-16-04 hr-grabbing-her-phone with dissolve
    pause
    play sound sfx_cloth_hanger1
    scene d21s01-16-05 hr-grabbing-her-phone with dissolve
    pause
    play sound sfx_door_closed8 volume 1.8
    scene d21s01-16-06 hr-grabbing-her-phone with dissolve
    pause
    stop sound2 fadeout 4.0
    $ renpy.music.set_volume(0.6, 3.0, "music" )
    scene d21s01-17 mc-hr-back with Fade(0.5, 0.5, 0.5)
    pause
    scene d21s01-17-01 mc-hr-back with dissolve
    play voice3 chloe_happy_hmm noloop
    hr "What, you want a day in the life of? I shower first, then I put some coffee on."
    scene d21s01-17-02 mc-hr-talking with dissolve
    hr "What do you do?"
    play voice2 mc_thinking_hmm4 noloop
    mc "You know what? I do the same thing. But to say I had a regular schedule the past few weeks is pushing it."
    scene d21s01-18 mc-hr-talking with dissolve
    play voice3 chloe_yes_yeah2 noloop
    hr "Yeah, I suppose."
    hr "Seeing as how you blew up the servers, I assume you'll be sleeping a lot better now."
    scene d21s01-18-02 mc-hr-talking with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Maybe..."
    mc "Did you tell Iona?"
    scene d21s01-18-03 hr-talking with dissolve
    play voice3 hana_emm noloop
    hr "Tell her what?"
    scene d21s01-18-05 mc-hr-talking with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "You know."
    scene d21s01-18-04 hr-talking with dissolve
    play voice3 chloe_disappointed_ehh4 noloop
    hr "Not yet. First thing I'm doing when I'm leaving is to go to our place."
    hr "Hey, do you think if I stuff a bag with whiskey, anyone would recognize it? I guess the glass clinking would give it away."
    scene d21s01-18-02 mc-hr-talking with dissolve
    play voice2 d1s5_mchappy noloop volume 2.3
    mc "Are you guys really that close?"
    scene d21s01-18-06 mc-hr-talking with dissolve
    play voice3 chloe_arrogant_pff noloop
    hr "Take a guess. Are you really that close to Pete?"
    if cage_ntr is True:
        scene d21s01-19-02 mc-hr-talking-ntr with dissolve
        play voice2 mc_angry_errr1 noloop
        mc "Pete's an asshole."
    else:
        scene d21s01-19 mc-hr-talking with dissolve
        play voice2 mc_no_nah1 noloop
        mc "Not really."
    scene d21s01-20 mc-hr-talking with dissolve
    play voice3 hana_hmm noloop
    hr "What do you get someone that really knows her drinks? Maybe I'll get her some sparkling wine instead..."
    scene d21s01-20-02 mc-hr-talking with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, I get it now."
    mc "You miss her? It's only been what, a day?"
    scene d21s01-21 mc-hr-sorrowful talk with dissolve
    play voice3 chloe_disappointed_mff noloop
    hr "Well, I want to tell her what happened. She'd love hearing about Jerome getting his ass beat."
    scene d21s01-21-02 mc-hr-talking with dissolve
    play voice2 d2s9_mchey noloop
    mc "Does she even know who Jerome is?"
    scene d21s01-21-03 mc-hr-talking with dissolve
    play voice3 chloe_arrogant_heh1 noloop
    hr "Do you?"
    scene d21s01-21-04 mc-hr-talking with dissolve
    play voice2 mc_no_no2 noloop
    mc "Not especially. I enjoyed hitting him though. His face is the definition of punchable."
    play voice3 chloe_angry_argh4 noloop
    scene d21s01-21-05 mc-hr-talking with dissolve
    hr "He has really the face of someone only a mother would love. Like nobody ever told him he was an unlikable piece of shit."
    hr "He pulled some shit with Iona at the bar."
    scene d21s01-21-06 mc-hr-talking with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "I vaguely remember that."
    play voice3 chloe_angry_breath noloop
    scene d21s01-22 mc-hr-angry-duck with dissolve
    pause
    scene d21s01-22-02 mc-hr-angry-duck with dissolve
    pause
    play voice3 chloe_angry_argh5 noloop
    play sound sfx_epic_kick2
    scene d21s01-22-03 mc-hr-angry-duck with hpunch
    hr "She told me about it and it got my blood boiling."
    scene d21s01-22-04 mc-hr-angry-duck with dissolve
    hr "I hope you kicked his teeth out. Scumbag."
    play sound sfx_epic_jump1
    scene d21s01-22-05 mc-hr-angry-duck with dissolve
    play voice2 mc_surprised_huh5 noloop
    mc "I wanted to do a lot more than that, believe me."
    scene d21s01-23 mc-hr-talking with dissolve
    play voice3 chloe_disappointed_ehh2 noloop
    hr "Lydia too. But I didn't know her like you did. To me, she's just another trifling bitch. We have a lot of those."
    hr "Knowing what she did though."
    hr "I wouldn't hit her. Mush her, maybe."
    scene d21s01-23-02 mc-hr-talking with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "Mush?"
    scene d21s01-23-03 mc-hr-talking with dissolve
    play voice3 chloe_happy_hmm noloop
    hr "It's not hitting a person, it's a specialized technique of placing your hand on someone's face to push them away."
    scene d21s01-23-04 mc-hr-talking with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "I'll have to remember that when I see her."
    scene d21s01-a24-02 mc-hr-talking-anim-24-02-00_i with dissolve
    play voice3 hana_hmm2 noloop
    hr "What happened to Pete?"
    play sound sfx_camera_fly1 volume 1.6
    scene d21s01-glambot-1
    pause
    if cage_ntr is True:
        play voice2 mc_scared_oh4 noloop
        mc "AmRose tased his balls off."
        play voice3 chloe_arrogant_huh noloop
        scene d21s01-24-03 mc-hr-talking with dissolve
        hr "What?"
        scene d21s01-25 mc-hr-talking with dissolve
        play voice2 mc_yes_yeah4 noloop
        mc "He's going to prison. Also, he's probably afraid of redheads and the color yellow."
        scene d21s01-24-03 mc-hr-talking with dissolve
        play voice3 chloe_arrogant_heh2 noloop
        hr "Ha!"
    else:
        play voice2 mc_arrogant_hm3 noloop
        mc "He's probably spending the summer on a sunny beach with a high priced escort."
        scene d21s01-24-05 mc-hr-talking with dissolve
        play voice3 hana_huh noloop
        hr "Huh? Sounds like there's a story there."
        scene d21s01-25 mc-hr-talking with dissolve
        play voice2 mc_yes_yeah4 noloop
        mc "Yeah. I'm pretty glad he turned out to be innocent."
        scene d21s01-25-03 mc-hr-talking with dissolve
        pause
        scene d21s01-25-04 mc-hr-talking with dissolve
        play voice3 chloe_disappointed_off noloop
        hr "I guess. That just means I sucked his cock for no reason."
    scene d21s01-25-05 mc-hr-talking with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Anyway.{w}.. why don't you call her?"
    scene d21s01-25-02 mc-hr-talking with dissolve
    play voice3 chloe_angry_hm noloop
    hr "Call who?"
    scene d21s01-25-05 mc-hr-talking with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Iona."
    play voice3 chloe_disappointed_ehh3 noloop
    scene d21s01-25-07 mc-hr-talking with dissolve
    hr "I don't think she's up yet. Iona is more of a spiritual person, she lets nature and the alignments of the stars, and of the universe, and the shapes of the moon dictate when she wakes up."
    hr "I wake up when the alarm goes off."
    scene d21s01-25-08 mc-hr-talking with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "Think you forgot to set one."
    scene d21s01-25-09 mc-hr-talking with dissolve
    play voice3 chloe_happy_mmm noloop
    hr "Phone's not charged."
    hr "I figured you'd wake me up with a nice surprise."
    scene d21s01-25-10 mc-hr-talking with dissolve
    play voice2 mc_disappointed_ehh4 noloop
    mc "Come on, what do you take me as, some kind of person who would jump at the opportunity of having sex?"
    scene d21s01-25-11 mc-hr-talking with dissolve
    play voice3 chloe_yes_aga2 noloop
    hr "Rhetorical question."
    scene d21s01-25-12 mc-hr-talking with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "I was psyching myself up a little bit with some music. Thinking about what I'll say to Lydia. I mean, what possibly can she say? There's nothing."
    scene d21s01-25-06 mc-hr-talking with dissolve
    play voice3 chloe_arrogant_heh1 noloop
    hr "Nothing?"
    scene d21s01-25 mc-hr-talking with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "If there is a reason to destroy someone's ability to make their own choices and have free will, I'd love to hear it."
    scene d21s01-25-04 mc-hr-talking with dissolve
    play voice3 chloe_disappointed_ehh1 noloop
    hr "I don't know if we're all bound by our choices. Sometimes choices are made for us, we have no say in it."
    scene d21s01-25-05 mc-hr-talking with dissolve
    play voice2 mc_disappointed_meh1 noloop volume 1.4
    mc "That's too easy. Absolves people of their responsibility."
    scene d21s01-25-11 mc-hr-talking with dissolve
    play voice3 chloe_disappointed_ehh5 noloop
    hr "I mean, I didn't have a choice being born into my family, no one did either."
    play voice3 chloe_disappointed_ehh6 noloop
    scene d21s01-26 mc-hr-talking with dissolve
    pause
    scene d21s01-27 mc-hr-talking with dissolve
    hr "You know what, it is too early for a philosophical debate."
    play sound sfx_hair_scratch1
    hr "I need a shower."
    scene d21s01-27-02 mc-hr-talking with dissolve
    pause
    play sound sfx_bandage_off1
    scene d21s01-27-03 mc-hr-talking with dissolve
    pause
    scene d21s01-27-04 mc-hr-talking with dissolve
    pause
    scene d21s01-27-05 mc-hr-talking with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Wait."
    scene d21s01-27-06 mc-hr-talking with dissolve
    mc "I wanted to talk about something."
    scene d21s01-27-07 mc-hr-talking with dissolve
    play voice3 chloe_surprised_huh2 noloop
    hr "Thought we just did."
    scene d21s01-27-08 mc-hr-talking with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Did you come to the dorm {i}just{/i} to pick up the mic?"
    scene d21s01-27-09 mc-hr-talking with dissolve
    play voice3 chloe_yes_simple noloop
    hr "Of course."
    scene d21s01-27-10 mc-hr-talking with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "But you told me the mic was a dud."
    scene d21s01-27-09 mc-hr-talking with dissolve
    play voice3 chloe_yes_yeah1 noloop
    hr "It was a dud."
    scene d21s01-27-08 mc-hr-talking with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "So why are you really here?"
    mc "Were you secretly hoping I was still in here?"
    scene d21s01-27-07 mc-hr-talking with dissolve
    play voice3 chloe_arrogant_heh3 noloop
    hr "That's funny."
    hr "Listen, [mcname]. It's like what you said yesterday. I'm not really interested in being here. Or being in a relationship at the moment."
    hr "I have a lot of things going on in my life. And you do as well, with Lydia."
    scene d21s01-27-10 mc-hr-talking with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "So that's it?"
    hr "That's it."
    scene d21s01-28 mc-hr-talking with dissolve
    play voice3 chloe_disappointed_oh noloop
    hr "Aw, you look so sad. Was I leading you on?"
    scene d21s01-28-01 mc-hr-talking with dissolve
    hr "You know what my favorite journalist wrote, that we were always selling others out. In the end, you got what you wanted, and so did I."
    play voice2 mc_yes_yeah3 noloop
    mc "Quid pro quo."
    mc "So what, you ride off into the sunset with Iona?"
    scene d21s01-28-02 mc-hr-talking with dissolve
    play voice3 chloe_disappointed_ehh7 noloop
    hr "Dunno. That's up to us to decide."
    play voice2 d1s5_mcthinks noloop volume 1.5
    mc "Would we ever see each other again?"
    scene d21s01-28-03 mc-hr-talking with dissolve
    play voice3 hana_emm noloop
    hr "Do you want to?"
    scene d21s01-28-04 mc-hr-talking with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Of course I do."
    play sound sfx_cloth_rustling2
    scene d21s01-29 mc-hr-talking with dissolve
    play voice3 chloe_happy_mmm noloop
    hr "Well, I'm sure that can be arranged. I'm sure we won't be strangers after this."
    scene d21s01-29-01 mc-hr-talking with dissolve
    pause
    scene d21s01-29-02 mc-hr-talking with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    hr "Was that all?"
    play voice2 mc_no_no5 noloop
    mc "No, not exactly. We still have a bit of unfinished business."
    scene d21s01-29-03 mc-hr-talking with dissolve
    pause
    scene d21s01-29-04 mc-hr-talking with dissolve
    play voice3 hana_argh noloop
    hr "Here I was thinking that it was just morning wood."
    play voice2 mc_pain_mff2 noloop
    mc "It's dangerous for an erection to last this long. I need a release."
    scene d21s01-29-05 mc-hr-talking with dissolve
    play voice3 hana_yeah2 noloop
    hr "So jerk off. There's the computer. Or to the posters in the room."
    scene d21s01-29-06 mc-hr-talking with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "I'd rather have you suck my cock."
    scene d21s01-29-07 mc-hr-talking with dissolve
    play voice3 chloe_surprised_oh noloop
    hr "Oh, really?"
    hr "Well, that's a lot of things I want, doesn't mean we get it."
    scene d21s01-29-08 mc-hr-talking with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "You promised."
    scene d21s01-29-09 mc-hr-talking with dissolve
    play voice3 chloe_yes_yeah3 noloop
    hr "I promised a lot of things."
    scene d21s01-29-08 mc-hr-talking with dissolve
    play voice2 mc_arrogant_hm2 noloop volume 1.7
    mc "You don't want to?"
    scene d21s01-29-10 mc-hr-talking with dissolve
    play voice3 chloe_disappointed_ehh4 noloop
    hr "I don't want to send a confusing message, like we're in some sort of relationship together. We're fuck buddies. That's it."
    hr "No more dates, or buying me gifts, or any of that dumb stuff."
    scene d21s01-29-11 mc-hr-talking with dissolve
    play voice2 mc_yes_okay2 noloop volume 1.6
    mc "Okay, so we're not exclusive. Got it."
    mc "You don't want to suck some dick from time to time?"
    scene d21s01-30-03 mc-hr-talking with dissolve
    play voice3 chloe_yes_unsure noloop
    hr "You're right though. I am feeling a bit frisky. Maybe it's because of the lack of sleep. Or because of being in this room."
    hr "I guess we have time for a quick blowie."
    scene d21s01-30-04 mc-hr-talking with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "No sex?"
    scene d21s01-29-09 mc-hr-talking with dissolve
    play voice3 chloe_hey_whisper noloop
    hr "Hey, I just came in here to get this and leave. Come get it while the offer's good."
    menu:
        "Suck my cock."(hint="d21s01m01c01"):
            $ d21s01_bj = True
            jump d21s01_bj
        "No thanks."(hint="d21s01m01c02"):

            jump d21s01_no_bj

label replay_d21s01:
label d21s01_bj:

    if _in_replay:
        play music calm_guitar_1
    play sound sfx_skirt_off1
    scene d21s01-31 mc-hr-the-start with dissolve
    play voice2 mc_angry_hm2 noloop
    mc "Let's not talk any more about families, or school, or relationships. Let's just do it."
    play voice3 chloe_no_questioning noloop
    hr "Do it? No foreplay? No calling me daddy?"
    scene d21s01-32 mc-hr-the-start with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Do you want that?"
    scene d21s01-33 mc-hr-the-start with dissolve
    play voice3 chloe_happy_hmm noloop
    hr "...{w}do you want it?"
    menu:
        "I do"(hint="d21s01m02c01"):
            $ d21s01_roleplay = True
            play voice2 d9s2_mcyes noloop volume 2.5
            mc "Yes. I do."
        "I don't"(hint="d21s01m02c02"):

            play voice2 mc_no_nah2 noloop
            mc "No. I don't."

    scene d21s01-31 mc-hr-the-start with dissolve
    mc "Get on the side of the bed. I want to take some of my stress out on you."
    play voice3 chloe_angry_breath noloop
    if d21s01_roleplay is True:
        hr "You make it sound so violent, daddy."
    else:
        hr "You make it sound so violent, [mcname]."
    hr "The threat is over. It's gone. We're in the languor stage of things."
    scene d21s01-32 mc-hr-the-start with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "What are you talking about?"
    hr "Did you take that women's studies course?"
    mc "No?"
    hr "I didn't either."
    scene d21s01-33 mc-hr-the-start with dissolve
    play voice3 chloe_disappointed_ehh5 noloop
    hr "It's just something I heard from Iona. We're in that period right before things will change for the better or worse. It's like going through a tunnel. We don't know what's on the other end."
    play voice2 mc_thinking_mmm2 noloop
    mc "I think I have an idea."
    play sound sfx_cloth_rustling1
    scene d21s01-34 mc-hr-the-start with dissolve
    pause
    scene d21s01-35 mc-hr-the-start with dissolve
    pause
    play voice2 mc_pain_rrrr noloop
    stop music fadeout 6.0
    play music2 "<silence 6.0>"
    play sound sfx_skirt_off2 volume 1.3
    scene d21s01-35-02 mc-hr-the-start with vpunch
    play voice3 chloe_arrogant_heh4 noloop
    $ renpy.music.set_volume(0.55, 0, "music2")
    queue music2 music_dad_island
    hr "Oh, so aggressive."
    play voice2 mc_thinking_mmm4 noloop
    mc "I remember you liking it rough."
    hr "I do."
    hr "But, to be honest. I don't think you fit the role."
    mc "What do you mean?"
    scene d21s01-35-05 mc-hr-the-start with dissolve
    play voice3 chloe_arrogant_heh2 noloop
    hr "I mean, I don't want to be the bearer of bad news, but you're kinda too soft."
    hr "Nothing wrong with being soft."
    scene d21s01-35-02 mc-hr-the-start with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "That's not how you felt last time."
    play voice3 chloe_arrogant_yeah1 noloop
    hr "Yeah, but that was easy. Out on a boat in the middle of the ocean. It was an away team disadvantage for me."
    mc "And now, you're on home territory."
    hr "You've been here too, nothing you haven't seen before."
    play sound sfx_spitcum1
    scene d21s01-35-03 mc-hr-the-start with hpunch
    play voice3 chloe_scared_oh2 noloop
    hr "Guh?!?"
    play voice2 mc_happy_hah1 noloop
    mc "What's wrong? You don't want to have a relationship with me right?"
    mc "So I'm guessing you want to be treated like a worthless, ugly, used-up whore."
    scene d21s01-35 mc-hr-the-start with dissolve
    play voice3 chloe_angry_argh2 noloop
    hr "Get away from me."
    hr "Ugly? I think you're describing your dick."
    hr "Who'd want to suck on that thing?"
    play voice3 chloe_angry_argh6 noloop
    play sound sfx_spitcum1 volume 1.5
    scene d21s01-35-04 mc-hr-the-start with hpunch
    play voice2 mc_happy_yay2 noloop
    mc "You know you're lying."
    scene d21s01-35-06 mc-hr-the-start with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Here, give it a taste."
    play voice3 chloe_angry_argh4 noloop
    scene d21s01-35-07 mc-hr-the-start with dissolve
    pause
    play sound sfx_jeans_on1
    scene d21s01-35-08 mc-hr-the-start with dissolve
    play voice2 d1s2_hmm noloop volume 2.0
    mc "Am I wrong about you wanting it?"
    play voice3 chloe_arrogant_pff noloop
    hr "I'm not a whore."
    scene d21s01-35-09 mc-hr-the-start with dissolve
    play voice2 mc_no_uhuh1 noloop
    if persistent.is_special is True:
        mc "You may have fooled your father with that innocent girl act, but I know who you are."
    else:
        mc "You may have fooled the Senator with that innocent girl act, but I know who you are."
        mc "You're just a little teeny slut, aren't you?"
    scene d21s01-36 mc-hr-blowjob with dissolve
    pause
    scene d21s01-36-02 mc-hr-blowjob with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "Take your clothes off."
    scene d21s01-36-03 mc-hr-blowjob with dissolve
    play voice3 hana_hmm noloop
    hr "Why don't you make me?"
    scene d21s01-37 mc-hr-blowjob with dissolve
    play voice3 chloe_happy_mmm noloop
    hr "Or what, you're just going to stare at me like the last time I was in here."
    scene d21s01-37-02 mc-hr-blowjob with dissolve
    hr "All your pretending doesn't mean anything, you're just a scared little baby boy."
    play sound spank3
    play voice2 mc_pain_mff3 noloop volume 1.6
    scene d21s01-38 mc-hr-slap with hpunch
    pause
    play sound sfx_epic_jump1
    scene d21s01-38-02 mc-hr-slap with dissolve
    pause
    play sound spank1
    play voice3 chloe_scared_oh1 noloop
    scene d21s01-38-04 mc-hr-slap with hpunch
    pause
    play voice2 d14s16_smell noloop
    scene d21s01-39 mc-hr-more-slaps with dissolve
    pause
    scene d21s01-39-02 mc-hr-more-slaps with dissolve
    play voice3 chloe_angry_argh3 noloop
    hr "Slap me again."
    hr "Fucker."
    scene d21s01-39-04 mc-hr-more-slaps with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "Bitch."
    play sound spank2 volume 1.5
    play voice3 chloe_angry_argh2 noloop
    scene d21s01-39-03 mc-hr-more-slaps with hpunch
    hr "Harder, stop being such a limp dick pussy and slap me harder. What, you're not man enough?"
    scene d21s01-38-05 mc-hr-slap with dissolve
    play voice3 chloe_angry_argh1 noloop
    hr "You always were a little crybaby bitch."
    play sound spank1 volume 2.0
    scene d21s01-38-04 mc-hr-slap with hpunch
    play voice3 chloe_angry_argh5 noloop
    hr "Afraid I'd turn into another Lydia?"
    hr "That's the only reason you got any pussy anyway. So why are you so angry at her? I'd thank her for turning you into a man."
    play voice2 mc_pain_ffff noloop
    scene d21s01-39 mc-hr-more-slaps with dissolve
    pause
    play sound spank3 volume 2.0
    play voice3 chloe_scared_ah2 noloop
    scene d21s01-39-06 mc-hr-more-slaps with vpunch
    pause
    play voice3 chloe_angry_breath noloop
    scene d21s01-39-07 mc-hr-more-slaps with dissolve
    pause
    scene d21s01-39-08 mc-hr-more-slaps with dissolve
    play voice3 chloe_yes_simple noloop
    if d21s01_roleplay is True:
        hr "That's how I like it, daddy."
    else:
        hr "That's how I like it, [mcname]"
    scene d21s01-39-04 mc-hr-more-slaps with dissolve
    play voice2 d9s5_auch2 noloop
    mc "Have you been a bad girl?"
    play voice3 chloe_yes_unsure noloop
    hr "Yes."
    play voice2 mc_disappointed_off2 noloop
    mc "Well, I don't believe in punishment for my beautiful little girl, so I'm going to give her an incentive to be nicer to me."
    scene d21s01-39-09 mc-hr-more-slaps with dissolve
    pause
    play sound sfx_cloth_tear1
    scene d21s01-39-10 mc-hr-more-slaps with dissolve
    pause
    play sound sfx_cloth_planket2 volume 1.7
    play voice3 chloe_scared_ah1 noloop
    scene d21s01-39-11 mc-hr-more-slaps with vpunch
    pause
    scene d21s01-39-12 mc-hr-more-slaps with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Close your eyes, and open your mouth."
    $ Lovense.stop()

    play voice3 hana_argh2 noloop
    $ Lovense.stop()
    scene d21s01-39-13 mc-hr-more-slaps with dissolve
    pause
    play voice2 d3s8_sucking volume 2.0
    play voice3 chloe_old_softmoans
    $ Lovense.vibrate(1)
    scene d21s01-39-14 mc-hr-more-slaps with dissolve
    pause
    scene d21s01-39-16 mc-hr-more-slaps with dissolve
    pause
    play voice2 d14s19_lc_licking
    scene d21s01-39-17 mc-hr-more-slaps with dissolve
    pause
    scene d21s01-39-18 mc-hr-more-slaps with dissolve
    $ Lovense.vibrate(1)
    pause
    stop voice2 fadeout 1.0
    $ Lovense.stop()
    scene d21s01-39-19 mc-hr-more-slaps with dissolve
    play voice3 hana_moans noloop
    hr "Ahh."
    scene d21s01-39-20 mc-hr-more-slaps with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Your mouth is watering."
    scene d21s01-39-21 mc-hr-more-slaps with dissolve
    play voice3 chloe_angry_breath noloop
    if d21s01_roleplay is True:
        hr "Yes, daddy."
    else:
        hr "Yes, [mcname]."
    scene d21s01-39-22 mc-hr-more-slaps with dissolve
    play voice2 d3s11b_mcheh noloop volume 2.5
    mc "Beg for it."
    scene d21s01-39-23 mc-hr-more-slaps with dissolve
    play voice3 chloe_old_yes noloop
    hr "I want your dick."
    play voice2 mc_surprised_huh6 noloop
    mc "What was that?"
    hr "I want your dick so bad. I want to suck your cock and milk it with my mouth, use my mouth like a toy, fuck me, abuse me, choke me, slap me."
    play voice3 chloe_old_sucking1
    $ Lovense.vibrate(4)
    scene d21s01-40 mc-hr-bj with dissolve
    pause
    $ Lovense.pump(1)
    scene d21s01-a40-03-01 mc-hr-bj-anim-01 with dissolve
    pause
    $ Lovense.pattern("10;7", 1700)
    play voice2 d7s4_mcbreathing
    scene d21s01-a1
    pause
    scene d21s01-a2 with dissolve
    pause
    $ Lovense.pattern("14;10", 1000)
    scene d21s01-a1-f with dissolve
    pause
    $ Lovense.pattern("14;10", 1000)
    scene d21s01-a2-f with dissolve
    pause
    stop voice2 fadeout 1.0
    stop voice3 fadeout 1.0
    $ Lovense.stop()
    scene d21s01-40-03 mc-hr-bj with dissolve
    pause
    scene d21s01-40-04 mc-hr-bj with dissolve
    play voice2 mc_pain_argh1 noloop
    mc "No fucking teeth, you fucking whore."
    scene d21s01-40-05 mc-hr-bj with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "Here, you want to use your teeth? I'm going to use your throat."
    $ Lovense.vibrate(18)
    play voice3 samiya_mfff3 noloop
    scene d21s01-40-06 mc-hr-bj with hpunch
    pause
    scene d21s01-40-07 mc-hr-bj with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "What, you can't breathe?"
    scene d21s01-a40-06-01 mc-hr-bj-anim-01 with dissolve
    pause
    play voice3 mc_sex_sucking_slow2
    play voice2 d7s4_mcbreathing fadein 3.0
    $ Lovense.pattern("13;10", 1700)
    scene d21s01-a3
    pause
    scene d21s01-a4 with dissolve
    pause
    play voice4 chloe_old_sucking1
    play voice3 mc_sex_sucking_fast2
    $ Lovense.pattern("17;13", 1000)
    scene d21s01-a3-f with dissolve
    pause
    scene d21s01-a4-f with dissolve
    pause
    play voice3 chloe_old_scream1 noloop
    stop voice4 fadeout 0.3
    play voice2 mc_angry_errr4 noloop
    $ Lovense.pattern("19")
    scene d21s01-41 mc-hr-cumming with vpunch
    pause
    play voice2 d1s5_orgasm2 noloop volume 1.6
    $ Lovense.pattern("19")
    scene d21s01-41-02 mc-hr-cumming with vpunch
    pause
    $ renpy.music.set_volume(0.15, 3.0, "music2" )
    scene d21s01-41-03 mc-hr-collapsing with fade

    $ Lovense.stop()
    play sound sfx_bed_fall1
    play voice2 d1s5b_ehhh noloop volume 1.4
    pause
    scene d21s01-41-04 mc-hr-collapsing with dissolve
    play voice3 hana_emm noloop
    hr "That was..."
    scene d21s01-41-05 mc-hr-collapsing with dissolve
    play voice2 d1s5_mchappy noloop volume 1.8
    mc "Amazing?"
    scene d21s01-41-06 mc-hr-collapsing with dissolve
    play voice3 chloe_happy_yeah4 noloop
    hr "Yeah. Please tell me you recorded that on your computer or something."
    play voice2 d1s2_hmm noloop volume 1.8
    mc "Should I have?"
    hr "Definitely."
    $ renpy.end_replay()
    $ unlock_gallery_slot("scene", "d21s01")
    scene d21s01-41-03 mc-hr-collapsing with dissolve
    play voice2 d2s9_confused noloop volume 1.8
    mc "So did you mean anything you said?"
    scene d21s01-41-04 mc-hr-collapsing with dissolve
    play voice3 chloe_surprised_huh3 noloop
    hr "What, about you being a bitch?"
    scene d21s01-41-05 mc-hr-collapsing with dissolve
    play voice2 d9s3_no noloop volume 2.5
    mc "No, about how Lydia and the Fetish Locator was the only reason I got laid."
    scene d21s01-41-06 mc-hr-collapsing with dissolve
    play voice3 chloe_no_nah noloop
    hr "Nah. Just came out at the spur of the moment, you know?"
    scene d21s01-41-05 mc-hr-collapsing with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah. For the record, I don't think you're a worthless slut."
    scene d21s01-41-04 mc-hr-collapsing with dissolve
    play voice3 chloe_happy_hmm noloop
    hr "I'm glad."
    hr "I didn't want to expose you publicly for what you really are."
    play sound sfx_jeans_on1
    scene d21s01-21-04 mc-hr-talking with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "And what am I?"
    scene d21s01-20 mc-hr-talking with dissolve
    play voice3 chloe_arrogant_heh4 noloop
    hr "I'll tell you in the shower."
    menu:
        "Join her"(hint="d21s01m03c01"):
            $ d21s01_join_shower = True
            scene d21s01-21-06 mc-hr-talking with dissolve
            play voice2 mc_yes_yeah5 noloop
            mc "Yeah, you're right. I'm filthy."
            scene d21s01-23-03 mc-hr-talking with dissolve
            play voice3 chloe_yes_aga2 noloop
            hr "Come on then. And no funny business."
            scene d21s01-23-04 mc-hr-talking with dissolve
            play voice2 mc_arrogant_heh1 noloop
            mc "Is anal out of the question?"
            scene d21s01-20 mc-hr-talking with dissolve
            play voice3 chloe_disappointed_off noloop
            hr "We'll talk..."
        "Don't join her."(hint="d21s01m03c02"):

            scene d21s01-21-06 mc-hr-talking with dissolve
            play voice2 mc_thinking_mmm5 noloop
            mc "I'll shower later. I have some things to do."
            scene d21s01-23-03 mc-hr-talking with dissolve
            play voice3 chloe_surprised_huh1 noloop
            hr "After all that, you're not going to join me?"
            scene d21s01-23-04 mc-hr-talking with dissolve
            play voice2 mc_yes_yeah6 noloop
            mc "Sorry."
            scene d21s01-20 mc-hr-talking with dissolve
            play voice3 chloe_disappointed_mff noloop
            hr "Whatever. I'll try not to use up all the hot water."

    jump d21s01_end

label d21s01_no_bj:

    scene d21s01-30-04 mc-hr-talking with dissolve
    play voice2 mc_no_uhuh1 noloop
    mc "No. I think I want a little more than a blowjob."
    scene d21s01-29-12 mc-hr-talking with dissolve
    play voice3 chloe_disgust_meh noloop
    hr "That's a shame. I wanted to show off some of my skills to you."
    hr "You would have came so hard."
    scene d21s01-30 mc-hr-talking with dissolve
    play voice2 d2s9_confused noloop volume 1.8
    mc "Isn't this what you wanted? No relationship?"
    scene d21s01-29-04 mc-hr-talking with dissolve
    play voice3 chloe_arrogant_yeah2 noloop
    hr "Yeah. I still want some dick though."
    scene d21s01-29-03 mc-hr-talking with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Well, I'm around."
    mc "Not here, in this dorm, but I'll be around."
    play sound sfx_cloth_rustling3
    scene d21s01-29-02 mc-hr-talking with dissolve
    play voice3 chloe_angry_breath noloop
    hr "We'll definitely see each other again. I can feel it."
    hr "Call it instinct."
    play sound maria_kiss1
    scene d21s01-41-07 mc-hr-collapsing with dissolve
    pause
    play sound sfx_skirt_off1
    scene d21s01-41-08 mc-hr-leaving with dissolve
    play voice3 hana_argh noloop
    hr "Bye, [mcname]."
    play voice2 mc_yes_yeah2 noloop
    mc "Later, Hana."

    jump d21s01_end

label d21s01_end:

    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop sound2 fadeout 3.0

    jump d21s02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
