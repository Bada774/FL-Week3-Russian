image d18s09-19-a1-f = Movie(play = "images/Day-18/s09/anim/d18s09-19-a1-2x-50fps.webm", start_image = "d18s09-19-a1 mc-hr-cf-bj-anim1-01_i")
image d18s09-19-a1 = Movie(play = "images/Day-18/s09/anim/d18s09-19-a1-4x-60fps.webm", start_image = "d18s09-19-a1 mc-hr-cf-bj-anim1-01_i")
image d18s09-19-a2-f = Movie(play = "images/Day-18/s09/anim/d18s09-19-a2-2x-50fps.webm", start_image = "d18s09-19-a2 mc-hr-cf-bj-anim2-01_i")
image d18s09-19-a2 = Movie(play = "images/Day-18/s09/anim/d18s09-19-a2-4x-60fps.webm", start_image = "d18s09-19-a2 mc-hr-cf-bj-anim2-01_i")
image d18s09-19-a3-f = Movie(play = "images/Day-18/s09/anim/d18s09-19-a3-2x-50fps.webm", start_image = "d18s09-19-a3 mc-hr-cf-bj-anim3-01_i")
image d18s09-19-a3 = Movie(play = "images/Day-18/s09/anim/d18s09-19-a3-4x-60fps.webm", start_image = "d18s09-19-a3 mc-hr-cf-bj-anim3-01_i")

image d18s09-a20-1-f = Movie(play = "images/Day-18/s09/anim/d18s09-a20-01-2x-50fps.webm", start_image = "d18s09-a20-01 mc-hr-cf-sex1-anim-20-01-00_i")
image d18s09-a20-1 = Movie(play = "images/Day-18/s09/anim/d18s09-a20-01-4x-60fps.webm", start_image = "d18s09-a20-01 mc-hr-cf-sex1-anim-20-01-00_i")
image d18s09-a20-2-f = Movie(play = "images/Day-18/s09/anim/d18s09-a20-02-2x-50fps.webm", start_image = "d18s09-a20-02 mc-hr-cf-sex1-anim-20-02-00_i")
image d18s09-a20-2 = Movie(play = "images/Day-18/s09/anim/d18s09-a20-02-4x-60fps.webm", start_image = "d18s09-a20-02 mc-hr-cf-sex1-anim-20-02-00_i")
image d18s09-a20-3-f = Movie(play = "images/Day-18/s09/anim/d18s09-a20-03-2x-50fps.webm", start_image = "d18s09-a20-03 mc-hr-cf-sex1-anim-20-03-00_i")
image d18s09-a20-3 = Movie(play = "images/Day-18/s09/anim/d18s09-a20-03-4x-60fps.webm", start_image = "d18s09-a20-03 mc-hr-cf-sex1-anim-20-03-00_i")
image d18s09-a21-1-f = Movie(play = "images/Day-18/s09/anim/d18s09-a21-01-2x-50fps.webm", start_image = "d18s09-a21-01 mc-hr-cf-sex2-anim-21-01-01_i")
image d18s09-a21-1 = Movie(play = "images/Day-18/s09/anim/d18s09-a21-01-4x-60fps.webm", start_image = "d18s09-a21-01 mc-hr-cf-sex2-anim-21-01-01_i")
image d18s09-a21-2-f = Movie(play = "images/Day-18/s09/anim/d18s09-a21-02-2x-50fps.webm", start_image = "d18s09-a21-02 mc-hr-cf-sex2-anim-21-02-01_i")
image d18s09-a21-2 = Movie(play = "images/Day-18/s09/anim/d18s09-a21-02-4x-60fps.webm", start_image = "d18s09-a21-02 mc-hr-cf-sex2-anim-21-02-01_i")
image d18s09-a21-3-f = Movie(play = "images/Day-18/s09/anim/d18s09-a21-03-2x-50fps.webm", start_image = "d18s09-a21-03 mc-hr-cf-sex2-anim-21-03-01_i")
image d18s09-a21-3 = Movie(play = "images/Day-18/s09/anim/d18s09-a21-03-4x-60fps.webm", start_image = "d18s09-a21-03 mc-hr-cf-sex2-anim-21-03-01_i")

image d18s09-cum-anim:
    "d18s09-22 mc-hr-cf-cum1_c2"
    pause 0.1
    "d18s09-22 mc-hr-cf-cum2_c2" with hpunch
    pause 0.1
    "d18s09-22 mc-hr-cf-cum3_c2"
    pause 0.1
    "d18s09-22 mc-hr-cf-cum4_c2" with hpunch

label replay_d18s09:
label d18s09:

    $ d18s09_cf_cum = False

    scene d18s09-1 mc-hr-entry_c1 with Fade(0.6, 0.6, 0.6)
    play voice3 chloe_happy_hmm noloop
    hr "Good thing it isn't locked."
    play voice2 mc_arrogant_huh3 noloop
    mc "Don't you know how to pick locks?"
    scene d18s09-1 mc-hr-entry_c2 with dissolve
    play voice3 chloe_no_nope noloop
    hr "Nope."
    play sound sfx_door_open1
    scene d18s09-2 mc-hr-entry2_c3 with dissolve
    pause
    scene d18s09-3 mc-hr-entry3_c1 with dissolve
    play voice3 chloe_arrogant_heh1 noloop
    hr "I spent all my illicit skill points on hacking computers."
    scene d18s09-3 mc-hr-entry3_c2 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.5
    mc "I'd say you have quite a lot of sex skills as well."
    scene d18s09-4 mc-hr-entry4_c1 with dissolve
    play sound sfx_keyboard_typing1
    play voice3 chloe_arrogant_pff noloop
    hr "Anyone else said that I'd tear their nuts off{w}, but from you I guess that's a compliment."
    scene d18s09-4 mc-hr-entry4_c2 with dissolve
    hr "Besides, that's just immoral... not illicit."
    play music rich_bitch
    play sound d14s12_door_open
    pause
    play voice2 mc_scared_huh1 noloop
    scene d18s09-4 mc-hr-entry4_c3 with dissolve
    play voice3 chloe_angry_hm noloop
    hr "*whispers loudly* Quick! Hide!"
    play sound sfx_chair_slide1 volume 1.5
    scene d18s09-5 mc-hr-entry5_c1 with dissolve
    pause
    scene d18s09-5 mc-hr-entry5_c2 with dissolve
    pause
    scene d18s09-5 mc-hr-entry5_c3 with dissolve
    play voice2 d14s16_smell noloop
    mct "Just pretend like you belong here..."
    scene d18s09-6 mc-hr-cf-talk1_c1 with dissolve
    pause
    play sound sfx_door_closed7
    scene d18s09-6 mc-hr-cf-talk1-1_c2 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Ah, Professor Fulton."
    scene d18s09-6 mc-hr-cf-talk1-1_c3 with dissolve
    play voice3 claudie_hey_angry noloop
    cf "Who are you?"
    scene d18s09-7 mc-hr-cf-talk2_c3 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "I was hoping I could find you here."
    mct "Shit shit shit.{w} I hope this works."
    scene d18s09-7 mc-hr-cf-talk2_c2 with dissolve
    play voice3 claudie_thinking_emm noloop
    cf "Do I know you? Why are you in my office?"
    scene d18s09-8 mc-hr-cf-talk3_c3 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "I'm fairly certain you do. [mcname] Young."
    mct "C'mon lady, all I know about you is that you're somehow related to Fetish Locator."
    scene d18s09-8 mc-hr-cf-talk3_c2 with dissolve
    play voice3 claudie_thinking_hmm2 noloop
    cf "Sounds vaguely familiar."
    scene d18s09-9 mc-hr-cf-talk4_c3 with dissolve
    play voice2 d2s9_confused noloop volume 1.5
    mc "You might remember my online alias, [mclogin]."
    scene d18s09-9 mc-hr-cf-talk4_c2 with dissolve
    play voice3 claudie_surprised_oh noloop
    cf "Ah, yes. Someone showed me that video going around campus."
    scene d18s09-9 mc-hr-cf-talk4_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "Video? What video?"
    play voice3 claudie_arrogant_ha2 noloop
    cf "Is there something I can do for you?"
    scene d18s09-10 mc-hr-cf-talk5_c3 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "I think we both know why I'm here."
    scene d18s09-10 mc-hr-cf-talk5_c2 with dissolve
    play voice3 claudie_no_questioning noloop
    cf "No, not really."
    play voice3 claudie_scared_oof noloop
    play sound sfx_bed_fall1

    $ Lovense.stop()

    scene d18s09-12 mc-hr-cf-look_c1 with hpunch
    $ Lovense.vibrate(1)
    pause
    scene d18s09-12 mc-hr-cf-look_c3 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Let me clarify that."
    mc "I have an assignment we both can work on together."
    scene d18s09-12 mc-hr-cf-look_c2 with dissolve
    play voice3 claudie_surprised_huh2 noloop
    cf "Mr. Young, you're trying to seduce me?"
    scene d18s09-12 mc-hr-cf-look_c3 with dissolve
    play voice2 mc_no_no2 noloop
    mc "Of course not.{w} Would you like me to seduce you?"
    scene d18s09-12 mc-hr-cf-look_c2 with dissolve
    play voice3 claudie_surprised_what noloop
    cf "What??"
    scene d18s09-12 mc-hr-cf-look_c1 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Is that what you're trying to tell me?{w} Do you want me to seduce you?"
    play voice3 claudie_disappointed_oof noloop
    cf "Are we on camera right now? Is this some kind of prank?"
    play voice2 mc_no_no1 noloop
    mc "No cameras, no pranks. Just two consenting adults alone in a room together."
    mct "This is never going to work."
    scene d18s09-12 mc-hr-cf-look_c3 with dissolve
    play voice2 mc_disappointed_ehh4 noloop
    mc "Perhaps I've made a mistake."
    scene d18s09-12 mc-hr-cf-look_c2 with dissolve
    play voice3 claudie_no_simple noloop
    cf "No, no.{w}.. no mistake. I just...{w} you caught me by surprise."
    play voice2 mc_yes_ugu1 noloop
    mc "Go on."
    play voice3 claudie_sex_closedmoan1 noloop
    cf "You're right. We're both adults..."
    scene d18s09-12 mc-hr-cf-look_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "Consenting?"
    play voice3 claudie_yes_simple noloop
    cf "Yes.{w} I consent."
    scene d18s09-12 mc-hr-cf-look_c3 with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "Then what are we waiting for?"
    play voice3 claudie_sex_closedmoan3 noloop
    play voice2 d1s5_orgasm noloop
    play sound dahlia_kiss_french1
    scene d18s09-13 mc-hr-cf-kiss_c1 with dissolve
    pause
    mct "I can't believe this is working!"
    play voice3 claudie_sex_closedmoan4 noloop
    play sound maria_kiss1
    scene d18s09-13 mc-hr-cf-kiss_c2 with dissolve
    pause
    scene d18s09-13 mc-hr-cf-kiss_c3 with dissolve
    mct "I am a sex god!!!"
    play voice3 claudie_sex_openmoan1 noloop
    scene d18s09-12 mc-hr-cf-look_c1 with dissolve
    pause
    play sound sfx_cloth_planket2
    scene d18s09-14 mc-hr-cf-wait_c1 with Dissolve(0.4)
    play voice3 claudie_angry_eh noloop
    cf "Wait!"
    scene d18s09-14 mc-hr-cf-wait_c3 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course.{w} What is it."
    scene d18s09-14 mc-hr-cf-wait_c2 with dissolve
    play voice3 claudie_arrogant_ha3 noloop
    cf "Nothing in my ass, nothing in my eyes.{w} I love being choked, but hate being slapped."
    scene d18s09-15 mc-hr-cf-wait2_c3 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "Good to know."
    scene d18s09-15 mc-hr-cf-wait2_c2 with dissolve
    play voice3 claudie_thinking_hmm1 noloop
    cf "What about you? What are your limits?"
    scene d18s09-15 mc-hr-cf-wait2_c3 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "I haven't found any yet."
    scene d18s09-15 mc-hr-cf-wait2_c2 with dissolve
    play voice3 claudie_surprised_ohmy noloop
    cf "Oh my!"
    play sound2 sfx_cloth_rustling3 noloop
    play voice3 claudie_sex_closedmoan2 noloop
    play voice2 d1s1_mmm noloop
    play sound maria_kiss2
    $ Lovense.vibrate(2)
    scene d18s09-13 mc-hr-cf-kiss_c3 with hpunch
    pause
    mct "Okay, maybe I'm not a sex god."
    scene d18s09-13 mc-hr-cf-kiss_c2 with dissolve
    play sound maria_kiss3
    mct "Maybe she's just crazy!"
    scene d18s09-12 mc-hr-cf-look_c2 with dissolve
    play voice3 claudie_disappointed_eeh noloop
    cf "What are we waiting for then?"
    scene black with Fade(0.4, 0.4, 0.4)
    "Some time later"
    play sound sfx_keyboard_typing2 volume 0.5
    scene d18s09-20 mc-hr-cf-sex1_c1 with Fade(0.4, 0.4, 0.4)
    $ Lovense.vibrate(4)
    pause
    play voice3 claudie_sex_openmoans1
    play voice2 d7s4_mcbreathing
    $ Lovense.pattern("5;8", 1700)
    scene d18s09-a20-2-f with dissolve
    cf "Fuck me! Yeessss!"
    mc "I'm going to cum!"
    pause
    scene d18s09-a20-1-f with dissolve
    cf "Fill me up!!!{w} I'M BARREN!!!"
    mct "Wow. That's a hell of a way to tell that to someone."
    pause
    scene d18s09-a20-3-f with dissolve
    pause
    pause
    stop voice3 fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(14)
    scene d18s09-22 mc-hr-cf-cum1_c2 with dissolve
    play voice2 mc_pain_ffff noloop
    mc "I'MMMM CUMMMMINNNGGG!!!!"
    play sound mc_cum_sound1
    play voice3 claudie_sex_orgasming_end1 noloop
    play voice2 mc_pain_argh1 noloop
    $ Lovense.vibrate(16)
    scene d18s09-cum-anim
    pause
    $ Lovense.vibrate(2)
    scene d18s09-23 mc-hr-cf-code1_c2 with dissolve
    play voice2 mc_pain_mff2 noloop
    mct "I almost forgot why I am here.{w} How's Hana doing?"
    scene d18s09-23 mc-hr-cf-code1_c1 with dissolve
    mct "I hope that means she finished."
    play sound sfx_paper_rustl1
    scene d18s09-23 mc-hr-cf-code1_c3 with dissolve
    mct "She got the door code. 0-0-7-1.{w} Just gotta remember that."
    scene d18s09-24 mc-hr-cf-out_c1 with dissolve
    play voice2 d1s5_mcthinks noloop
    mct "Huh. She is gonna go out through the window."
    scene d18s09-24 mc-hr-cf-out_c2 with dissolve
    play voice3 claudie_sex_openmoan2 noloop
    cf "Don't tell me you're done already."
    scene d18s09-24 mc-hr-cf-out_c3 with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Hmm?"
    play sound sfx_door_slide2
    scene d18s09-24 mc-hr-cf-out_c2 with dissolve
    play voice3 claudie_sex_openmoan5 noloop
    cf "Please don't stop. I haven't come yet.{w} Please keep fucking me!"
    menu:
        "Keep Fucking"(hint="d18s09m01c01"):
            $ d18s09_cf_cum = True

            jump d18s09_continue
        "Leave Her Wanting More"(hint="d18s09m01c02"):

            jump d18s09_stop

label d18s09_continue:

    scene d18s09-25 mc-cf-talk1_c3 with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "Don't worry, Professor.{w} I have a reputation to maintain."
    scene d18s09-24 mc-hr-cf-out_c2 with dissolve
    play voice3 claudie_yes_aga noloop
    cf "I bet!"
    play voice2 mc_thinking_emm1 noloop
    mc "But I need you to do something to get me to full hard-on."
    scene d18s09-17 mc-hr-cf-bj-talk2_c1 with dissolve
    play voice3 claudie_disappointed_mmm noloop
    cf "I can imagine."
    $ Lovense.vibrate(4)
    scene d18s09-19-a3 mc-hr-cf-bj-anim3-01_i with dissolve
    pause
    play voice3 claudie_sex_sucking3
    play voice2 d7s4_mcbreathing noloop
    $ Lovense.pattern("5;8", 1700)
    scene d18s09-19-a3
    pause
    mc "While you suck on that...{w} do you mind if I ask you a few questions?"
    play voice4 claudie_sex_closedmoan6 noloop
    cf "Mmffffmmmmm."
    scene d18s09-19-a2 with dissolve
    mc "Excellent.{w} What video are you talking about?"
    stop voice2 fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(3)
    scene d18s09-17 mc-hr-cf-bj-talk2_c1 with dissolve
    play voice3 claudie_surprised_huh1 noloop
    cf "You don't know?"
    scene d18s09-17 mc-hr-cf-bj-talk2_c2 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Well, I guess I should say \"Which video\" since there are probably a lot."
    scene d18s09-17 mc-hr-cf-bj-talk2_c3 with dissolve
    play voice3 claudie_sex_openmoan1 noloop
    cf "The chair. Spinning. Fountain of cum. Everywhere."
    play voice3 claudie_sex_sucking2
    play voice2 d7s4_mcbreathing noloop
    $ Lovense.pattern("5;8", 1700)
    scene d18s09-19-a1 with dissolve
    mct "The spinning chair?{w} At AmRose's house?"
    mct "I guess I came a lot and that impressed her."
    if is_antagonist_mode is False:
        mct "Although, this might be the person behind Fetish Locator and the VIP Program."
    else:
        mct "Although, this might be the bitch behind Fetish Locator and the Retention Program."
    mc "You like the taste?"
    cf "Mmmfffffmmm."
    $ Lovense.pattern("5;8", 900)
    scene d18s09-19-a3-f with dissolve
    mc "You like the taste of your own pussy on my cock?"
    cf "*continues sucking*"
    scene d18s09-19-a1-f with dissolve
    mct "I guess that's my answer."
    scene d18s09-19-a2-f with dissolve
    mc "Tell me what you know about Fetish Locator."
    play voice3 claudie_surprised_huh2 noloop
    stop voice2 fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(3)
    scene d18s09-17 mc-hr-cf-bj-talk2_c1 with dissolve
    cf "Huh?"
    scene d18s09-17 mc-hr-cf-bj-talk2_c2 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh look.{w} I'm hard enough to pound that pussy again."
    scene d18s09-17 mc-hr-cf-bj-talk2_c3 with dissolve
    play voice3 claudie_yes_happy noloop
    cf "YES!!!"
    $ Lovense.vibrate(4)
    scene d18s09-a20-01 mc-hr-cf-sex1-anim-20-01-00_i with fade
    play voice2 mc_pain_rrrr noloop
    mc "Tell me."
    play voice2 d7s4_mcbreathing
    play voice3 claudie_sex_openmoans1
    $ Lovense.pattern("7;10", 2000)
    scene d18s09-a20-1
    cf "Anything!"
    pause
    mc "What do you know?!"
    scene d18s09-a20-2 with dissolve
    cf "Anything you want!!!"
    mc "About Fetish Locator!!!"
    cf "JUST KEEP FUCKING ME!!!"
    pause
    $ Lovense.pattern("7;10", 1000)
    scene d18s09-a20-1-f with dissolve
    mc "TELL ME!!!"
    pause
    scene d18s09-a20-2-f with dissolve
    cf "WHATEVER YOU WANT!!!"
    pause
    scene d18s09-a20-3-f with dissolve
    mct "Is Wayne Brady gonna have to actually choke a bitch?!"
    play voice3 claudie_sex_harder_faster noloop
    queue voice3 claudie_sex_openmoans1
    cf "HARDER! FASTER!! STRONGER!!!"
    pause
    stop voice3 fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(4)
    scene d18s09-a21-03 mc-hr-cf-sex2-anim-21-03-01_i with dissolve
    play voice2 mc_angry_errr4 noloop
    mc "TELL ME WHAT YOU KNOW ABOUT FETISH LOCATOR!!!"
    play voice3 claudie_sex_orgasming1
    play voice2 d7s4_mcbreathing
    $ Lovense.pattern("7;11", 2000)
    scene d18s09-a21-3-f
    cf "NOTHING!!!"
    pause
    scene d18s09-a21-2-f with dissolve
    mct "FUCK!!!"
    with vpunch
    cf "I'M CUMMMINNGGGGG!!!"
    mct "Son of a Bitch!!!"
    mc "I'M GONNA CUM TOO!!!"
    scene d18s09-a21-1-f with dissolve
    cf "FILL MY BARREN CUNTHOLE WITH YOUR SEED!!!"
    mct "..."
    play voice2 d9s5_auch2 noloop
    play voice3 claudie_sex_orgasming_end1 noloop
    $ Lovense.stop()
    $ Lovense.vibrate(17)
    scene d18s09-a21-01 mc-hr-cf-sex2-anim-21-01-01_i with vpunch
    with vpunch
    mc "AGAGGAAHHHAAAHAHAAAAA!!!"
    $ renpy.music.set_volume(0.35, 5.0, "music")
    $ renpy.end_replay()
    scene d18s09-25 mc-cf-talk1_c1 with Fade(0.4, 0.4, 0.4)
    $ Lovense.vibrate(1)
    play voice2 mc_thinking_hmm5 noloop
    mc "Huh?"
    play voice3 claudie_sex_fuck noloop
    cf "Fuck."
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah."
    scene d18s09-25 mc-cf-talk1_c2 with dissolve
    play voice3 claudie_disappointed_geh noloop
    cf "Don't get me wrong - you were amazing."
    scene d18s09-25 mc-cf-talk1_c3 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "But-?"
    scene d18s09-26 mc-cf-talk2_c1 with dissolve
    play voice3 claudie_disappointed_eeh noloop
    cf "But I'm a professor and you are a student."
    play voice2 d9s2_yeah noloop volume 3.0
    mc "I'm not one of your students."
    scene d18s09-26 mc-cf-talk2_c2 with dissolve
    play voice3 claudie_disappointed_eh noloop
    cf "Still."
    scene d18s09-26 mc-cf-talk2_c3 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "I should dress up."
    cf "Yeah."

    $ Lovense.stop()

    scene d18s09-27 cf-speak1_c1 with dissolve
    play voice3 claudie_disappointed_oof noloop
    cf "This was a mistake."
    play voice2 mc_yes_aga1 noloop
    mc "Probably. Mind if I ask you a question?"
    scene d18s09-28 cf-speak2_c1 with dissolve
    play voice3 claudie_thinking_hmm4 noloop
    cf "You know if you mention this to anyone I'll lose my job."
    play voice2 mc_yes_okay2 noloop
    mc "In that case, I suggest you answer my question as honestly as possible."
    scene d18s09-29 cf-speak3_c1 with dissolve
    play voice3 claudie_arrogant_pff noloop
    cf "Fuck. What do you want?"
    play voice2 mc_thinking_hmm3 noloop
    mc "What do you know about Fetish Locator?"
    scene d18s09-30 cf-speak4_c1 with dissolve
    play voice3 claudie_thinking_hmm3 noloop
    cf "That app?{w} It seems to be popular around campus."
    mc "You gave access to someone to run it from the campus servers."
    scene d18s09-31 cf-speak5_c1 with dissolve
    play voice3 claudie_surprised_huh1 noloop
    cf "I did?{w} I don't remember anything like that."
    play voice2 d2s9_confused noloop volume 1.7
    mc "How else would they have gotten access?"
    scene d18s09-29 cf-speak3_c1 with dissolve
    play voice3 claudie_surprised_eem noloop
    cf "I mean, I don't know. The previous professor?"
    play voice2 mc_arrogant_huh2 noloop
    mc "You're telling me you don't know who has access to the campus servers?"
    play voice3 claudie_arrogant_yeah noloop
    cf "My job is like the Defense Against the Dark Arts teacher at Hogwarts."
    mc "I don't understand."
    scene d18s09-27 cf-speak1_c1 with dissolve
    play voice3 claudie_arrogant_ha3 noloop
    cf "It changes every year.{w} This year it changed twice."
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "So you're not the mastermind behind the Fetish Locator app?"
    play voice3 claudie_no_uhuh noloop
    cf "I barely even have a job here.{w} I haven't even taught a course yet."
    mc "Okay, sorry to bother you."
    scene d18s09-35 cf-speak9_c1 with dissolve
    play voice3 claudie_disgust_neeh noloop
    cf "You're not going to mention this-"
    play voice2 mc_no_no1 noloop
    mc "No.{w} Definitely not.{w} I would never-"
    scene d18s09-38 cf-speak10_c1 with dissolve
    play voice3 claudie_happy_phew noloop
    cf "Okay. Thanks."
    mc "Was it good for you?"
    scene d18s09-32 cf-speak6_c1 with dissolve
    play voice3 claudie_happy_laugh3 noloop
    cf "I think so.{w} Right now I'm kinda terrified that I've ruined my life."
    play voice2 mc_happy_yay2 noloop
    mc "Honestly, I won't say anything.{w} It might be on Fetish Locator, but I don't think..."
    if is_antagonist_mode is False:
        mc "Well, I hope the app won't identify you or give any information that could."
    else:
        mc "Well, I hope the app won't demand anything of you."
    scene d18s09-33 cf-speak7_c1 with dissolve
    play voice3 claudie_hey_simple noloop
    cf "Hey, [mcname]...{w} I've never been fucked like that in my life."
    cf "You should know that."
    play voice2 d3s11b_mcheh noloop
    mc "I'm... glad?{w} You deserve it."
    scene d18s09-34 cf-speak8_c1 with dissolve
    play voice3 claudie_arrogant_ha1 noloop
    cf "Heh. At least you don't have to worry about having my kid."
    play voice2 mc_arrogant_heh3 noloop
    mc "Heh... yeah. There's that, I guess."
    scene d18s09-32 cf-speak6_c1 with dissolve
    play voice3 claudie_thinking_hm noloop
    cf "This got kinda awkward, didn't it?"
    play voice2 mc_thinking_hmm1 noloop
    mc "Well, it was nice meeting you."
    mc "Good luck in your career here."
    scene d18s09-33 cf-speak7_c1 with dissolve
    play voice3 claudie_yes_yeah1 noloop
    cf "Yeah, thanks.{w} Good luck on your final exams, if you haven't had them yet."
    mc "Thanks.{w}.. I'm gonna go."
    cf "Okay."
    play sound sfx_jeans_on1
    scene d18s09-39 cf-out1_c2 with fade
    play voice3 claudie_hey_happy2 noloop
    cf "Wait!"
    scene d18s09-39 cf-out1_c1 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yes, Professor?"
    scene d18s09-40 cf-out2_c2 with dissolve
    play voice3 claudie_happy_mmm1 noloop
    cf "I just want you to know what an incredible specimen you are."
    scene d18s09-40 cf-out2_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Huh?"
    scene d18s09-39 cf-out1_c2 with dissolve
    play voice3 claudie_sex_closedmoan1 noloop
    cf "I've never seen a man cum like you did."
    cf "And I've never felt a man fill me up as much as you did{w} - and you did it twice."
    scene d18s09-39 cf-out1_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "Um.{w}.. thanks?"
    scene d18s09-40 cf-out2_c2 with dissolve
    play voice3 claudie_sex_openmoan1 noloop
    cf "I just wanted you to know that you're really special."
    scene d18s09-40 cf-out2_c1 with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Okay.{w} Take care of yourself."
    cf "You too."
    play sound sfx_door_closed10
    $ unlock_gallery_slot("scene", "d18s09")

    stop music fadeout 3.5
    jump d18s10

label d18s09_stop:

    scene d18s09-25 mc-cf-talk1_c3 with dissolve
    play voice2 mc_surprised_huh3 noloop
    mc "Oh my - is that the time?"
    scene d18s09-41 cf-out-fast1_c1 with fade

    $ Lovense.stop()

    play voice2 d1s5b_emmm noloop
    mc "I'm sorry, but I need to-"
    scene d18s09-41 cf-out-fast1_c2 with dissolve
    play voice3 claudie_angry_argh2 noloop
    cf "Are you serious?"
    play voice2 mc_thinking_mmm3 noloop
    mc "Can you finish yourself off?"
    play voice3 claudie_no_rude noloop
    cf "No. I can't.{w} I can't climax by myself."
    scene d18s09-41 cf-out-fast1_c1 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Oh, well. I'll come back and finish later."
    mc "It was nice meeting you."
    play voice3 claudie_yes_happy noloop
    cf "Terrific. Just leave me with a great big set of blue ladyballs."
    play sound sfx_jeans_on1
    scene d18s09-41 cf-out-fast2_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "I'm sorry, but I really need to go."
    scene d18s09-41 cf-out-fast2_c2 with dissolve
    play voice3 claudie_arrogant_pff noloop
    cf "Fuck."
    play sound sfx_door_closed10
    $ renpy.end_replay()

    stop music fadeout 3.5
    jump d18s10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
