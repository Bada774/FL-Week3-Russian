image e04s06-a52-1 = Movie(play = "images/E-04/s06/anim/e04s06-a52-1-2x-50fps.webm", start_image = "e04s06-a52-1 lc-sucking-mc-anim-01")
image e04s06-a52-1-f = Movie(play = "images/E-04/s06/anim/e04s06-a52-1-2x-60fps.webm", start_image = "e04s06-a52-1 lc-sucking-mc-anim-01")
image e04s06-a52-2 = Movie(play = "images/E-04/s06/anim/e04s06-a52-2-2x-50fps.webm", start_image = "e04s06-a52-2 lc-sucking-mc-anim-01")
image e04s06-a52-2-f = Movie(play = "images/E-04/s06/anim/e04s06-a52-2-2x-60fps.webm", start_image = "e04s06-a52-2 lc-sucking-mc-anim-01")

image e04s06-a76-1 = Movie(play = "images/E-04/s06/anim/e04s06-a76-1-2x-50fps.webm", start_image = "e04s06-a76-1 mk-fuck-terell-anim-01")
image e04s06-a76-1-f = Movie(play = "images/E-04/s06/anim/e04s06-a76-1-2x-60fps.webm", start_image = "e04s06-a76-1 mk-fuck-terell-anim-01")
image e04s06-a76-2 = Movie(play = "images/E-04/s06/anim/e04s06-a76-2-2x-50fps.webm", start_image = "e04s06-a76-2 mk-fuck-terell-anim-01")
image e04s06-a76-2-f = Movie(play = "images/E-04/s06/anim/e04s06-a76-2-2x-60fps.webm", start_image = "e04s06-a76-2 mk-fuck-terell-anim-01")

image e04s06-a159-1 = Movie(play = "images/E-04/s06/anim/e04s06-a159-1-2x-50fps.webm", start_image = "e04s06-a159-1 lc-blowing-gloryhole-anim-01")
image e04s06-a159-1-f = Movie(play = "images/E-04/s06/anim/e04s06-a159-1-2x-60fps.webm", start_image = "e04s06-a159-1 lc-blowing-gloryhole-anim-01")
image e04s06-a159-2 = Movie(play = "images/E-04/s06/anim/e04s06-a159-2-2x-50fps.webm", start_image = "e04s06-a159-2 lc-blowing-gloryhole-anim-01")
image e04s06-a159-2-f = Movie(play = "images/E-04/s06/anim/e04s06-a159-2-2x-60fps.webm", start_image = "e04s06-a159-2 lc-blowing-gloryhole-anim-01")
image e04s06-a159-3 = Movie(play = "images/E-04/s06/anim/e04s06-a159-3-2x-50fps.webm", start_image = "e04s06-a159-3 lc-blowing-gloryhole-anim-01")
image e04s06-a159-3-f = Movie(play = "images/E-04/s06/anim/e04s06-a159-3-2x-60fps.webm", start_image = "e04s06-a159-3 lc-blowing-gloryhole-anim-01")

image e04s06-a72-glambot-1 = Movie(play = "images/E-04/s06/anim/e04s06-a72-2x-50fps.webm", start_image = "e04s06-a72 sy-realizing-glambot-72-000", image = "e04s06-a72 sy-realizing-glambot-72-149", loop = False)

label e04s06:

    if not hasattr(renpy.store, "e04s06_mk_available"):
        if d15s05_rescue is False and d15s05_leave is False:
            $ e04s06_mk_available = True
        elif True:
            $ e04s06_mk_available = False
    $ e04s06_lc_suck = False

    scene black
    show screen scene_transistion(_("Some time later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
label replay_e04s06 hide:
    $ renpy.music.set_volume(0.5, 1.0, "sound4")
    play sound4 park fadein 2.0
    play sound2 sfx_weather_arctic_wind noloop volume 0.1 fadein 3.0
    scene e04s06-01-mc-sy-lc-feeling-the-sunlight
    with Fade(0.5, 0.5, 0.5)
    stop sound2 fadeout 3.0
    pause
    play voice4 lydia_moan1 noloop
    lc "Sunlight! I never thought I would feel it on my face again."
    scene e04s06-02-mc-sy-lc-feeling-the-sunlight with dissolve
    play voice4 dahlia_thinking_hmm3 noloop
    lc "I missed this so much."
    scene e04s06-03-mc-sy-lc-curious with dissolve
    play voice4 dahlia_disappointed_ehh3 noloop
    lc "What is this? Exercise in the prison yard?"
    scene e04s06-04-mc-commanding with dissolve
    play voice2 mc_no_no5 noloop
    mc "No. Get down on your hands and knees."
    scene e04s06-05-lc-accepting-the-order with dissolve
    play voice4 dahlia_thinking_mmm1 noloop
    lc "Whatever... Fine. Let's see what you have planned this time."
    play sound sfx_cloth_rustling2
    scene e04s06-06-lc-down-on-her-knees with dissolve
    pause
    scene e04s06-07-mc-asking with dissolve
    play voice2 d2s9_mchey noloop
    mc "Stacy, are we live?"
    scene e04s06-08-sy-streaming with dissolve
    play music music_funky_horn
    play voice3 stacy_thinking_hmm4 noloop
    sy "Streaming and recording for later. No users in chat yet."
    $ renpy.music.set_volume(0.5, 10.0, "music" )
    scene e04s06-09-mc-ly-asking with dissolve
    play voice4 dahlia_surprised_huh1 noloop
    lc "What's going on?"
    play voice2 mc_thinking_hmm5 noloop
    mc "Get a good close-up on us, then. I'm about to explain it to our new puppy."
    scene e04s06-11-lc-curious with dissolve
    play voice4 dahlia_surprised_what noloop
    lc "What?"
    scene e04s06-12-mc-talking with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "I got permission from the Judge to take our doggo out for a walk in the park today."
    scene e04s06-14-mc-explaining with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "You might recognize our little bitch here."
    mc "She was Lydia Cox, daughter of famous parents, starting to build her own social media presence and singing career. Then she was convicted and became my prisoner."
    scene e04s06-15-mc-lc-sy-get-a-close-up with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Today, she's just a fuckable piece of dogmeat who is going for walkies."
    scene e04s06-17-lc-angry with vpunch
    play voice4 lydia_ah noloop
    lc "What?! You can't do this!! People will see me!!!"
    scene e04s06-18-mc-explaining with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "First, I can do this. I have explicit permission."
    mc "Second, don't worry. There shouldn't be that many people in the park. It's a weekday."
    scene e04s06-19-sy-talking with dissolve
    play voice3 stacy_happy_yay1 noloop
    sy "We now have five viewers in chat."
    play sound sfx_cloth_rustling1
    scene e04s06-20-mc-talking with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Third, that's why Stacy is livestreaming this. By the end of the day hopefully thousands of people all over the world will have seen you."
    scene e04s06-21-sy-talking with dissolve
    play voice3 stacy_happy_laugh4 noloop
    sy "And maybe some locals will catch the livestream and join us in the park."
    scene e04s06-23-lc-mad with dissolve
    play voice4 dahlia_no_high1 noloop
    lc "No, no, no, no, no, no, no."
    lc "This cannot be happening."
    play sound sfx_heels_steps1 loop volume 1.5
    scene e04s06-24-mc-yelling with dissolve
    play voice2 mc_pain_argh1 noloop
    mc "Lydia, HEEL!"
    scene e04s06-25-mc-lc-heeling with dissolve
    play voice2 mc_angry_errr4 noloop
    mc "Lydia, I said \"HEEL\"! You know what happens if you disobey me."
    play sound sfx_barefoot_steps1 volume 3.0
    scene e04s06-26-lc-complaining with dissolve
    play voice4 dahlia_pain_sobs noloop
    lc "Fuck.{w} Coming!"
    scene e04s06-27-sy-lc-mc-asking with dissolve
    play voice3 stacy_thinking_emm2 noloop
    sy "Shouldn't she be barking and whimpering?"
    scene e04s06-28-mc-answering with dissolve
    play voice2 mc_no_nah2 noloop
    mc "I prefer hearing her anguish and humiliation given a voice."
    scene e04s06-29-sy-happy with dissolve
    play voice3 stacy_surprised_oh1 noloop
    sy "Oh, we're up to ten viewers in chat!"
    stop sound fadeout 1.0
    scene e04s06-30-lc-requesting with fade
    play sound sfx_heels_steps1 loop
    pause
    scene e04s06-31-lc-requesting with dissolve
    play voice4 dahlia_pain_ah2 noloop
    lc "Please stop this. I'll be good. I'll be good."
    scene e04s06-32-mc-being-smart with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "You can stop this if you want to - just press the button."
    scene e04s06-33-lc-helpless with dissolve
    play voice4 dahlia_pain_ah3 noloop
    lc "I can't... but... people can see me."
    scene e04s06-34-mc-talking-to-himself with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Indeed. They can. Speaking of which..."
    mc "Stacy, how's the livestream going?"
    scene e04s06-35-sy-answering with dissolve
    play voice3 stacy_happy_relief1 noloop
    sy "Really well. Much better than we expected."
    scene e04s06-36-sy-shout-out with dissolve
    play voice3 stacy_hey_attention1 noloop
    sy "Shout out to those of you who live in Crowning."
    sy "If you look at the video carefully you should know where we are."
    sy "You can probably guess where we are going if we can get through the Tier Three and Tier Four Tip Goals."
    stop sound fadeout 1.0
    scene e04s06-37-sy-mc-talking with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "Very nice. Are we exceeding expectations in terms of viewers as well as in tips?"
    play voice3 stacy_yes_simple1 noloop
    sy "Yep. As matter of fact..."
    sy "Hold on just a second..."
    scene e04s06-38-sy-excited with dissolve
    play voice3 stacy_surprised_wow1 noloop
    sy "Yes! We passed our Tier Three Goal for Tips!"
    scene e04s06-39-sy-excited with dissolve
    play voice3 stacy_laugh noloop
    sy "You know what that means?!"
    scene e04s06-40-mc-talking with dissolve
    play voice2 d9s2_mcyes noloop volume 2.5
    mc "I do.{w} Lydia gets a hot dog."
    scene e04s06-41-lc-misunderstanding with dissolve
    play voice4 dahlia_disgust_yah noloop
    lc "Ugh, no thanks.{w} I'm already nauseous."
    scene e04s06-42-sy-talking with dissolve
    play voice3 stacy_uhuh noloop
    sy "No choice. Chat has spoken!"
    scene e04s06-43-mc-talking with dissolve
    play voice2 d1s5_mchappy noloop volume 1.67
    mc "Besides, it's not that kind of hot dog."
    scene e04s06-44-lc-understanding with dissolve
    play voice4 dahlia_old_upset noloop
    lc "You wouldn't. Not here."
    scene e04s06-45-mc-talking with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "I would.{w} Lydia, kneel."
    mc "I told you. Be a good little bitch and kneel for your master."
    scene e04s06-46-lc-kneeling with dissolve
    play voice2 d9s2_ugu noloop volume 2.2
    mc "Good girl. You deserve a treat."
    play voice4 dahlia_angry_oof noloop
    lc "I really might puke."
    scene e04s06-47-mc-praising with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Do you know what people do when they give their dog a treat?"


    $ Lovense.stop()

    play sound sfx_jeans_fly1 volume 2.0
    scene e04s06-48-mc-treating with dissolve
    $ Lovense.vibrate(1)
    play voice2 mc_happy_a1 noloop
    mc "They put it on the doggie's nose and the dog does a little trick..."
    scene e04s06-49-lc-treating with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "... where they put the treat in their mouth without dropping it."
    mc "Go on, girl. I'm sure you can do it."
    scene e04s06-50-lc-doing-the-trick with dissolve
    pause
    play voice4 daisy_dlick noloop volume 2.7
    $ Lovense.vibrate(3)
    scene e04s06-51-lc-doing-the-trick with dissolve
    pause
    scene e04s06-a52-1 lc-sucking-mc-anim-01 with dissolve
    pause
    scene e04s06-a52-1
    $ Lovense.pattern("5;10", 1700)
    play sound mc_sex_sucking_slow2 loop
    play voice4 daisy_sucking
    pause
    scene e04s06-53-mc-happy with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Good girl. Enjoy that hot, hard shaft of meat."
    scene e04s06-54-sy-joking with dissolve
    play voice3 stacy_happy_laugh2 noloop
    sy "Just don't bite it. *laughing*"
    scene e04s06-55-mc-happy with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "She knows better than that."
    scene e04s06-a52-2 with dissolve
    mc "Remind me, what was the Tier Four tip goal?"
    pause
    scene e04s06-57-sy-talking with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "You take her to the ladies' water closet."
    scene e04s06-56-mc-pleasure with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Really? I thought that was going to be Tier Five."
    scene e04s06-58-sy-talking with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "It was, but then we couldn't think up a good Tier Four."
    sy "So, Tier Five became Tier Four, but I left the required amount of tips the same as Tier Five would have been.."
    scene e04s06-59-mc-talking with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Speaking of which, how are we doing on tips now?"
    scene e04s06-57-sy-talking with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "Really well. Plus we have a competition going on in chat."
    scene e04s06-55-mc-happy with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "I didn't know we could do that."
    play voice3 stacy_no_simple3 noloop
    sy "No, but there are two groups that are promising massive tips if we do what they want."
    scene e04s06-58-sy-talking with dissolve
    play voice3 stacy_thinking_hmm3 noloop
    sy "One group wants you to cum all over her face and not let her clean herself up."
    play sound mc_sex_sucking_fast2 loop
    $ Lovense.pattern("5;10", 800)
    scene e04s06-a52-1-f with dissolve
    sy "The other group is in the lead, though. They want you to shove your cock all the way down her throat and cum in her stomach."
    pause
    scene e04s06-a52-2-f with dissolve
    pause
    scene e04s06-61-mc-pov with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "I like the sound of that."
    play sound sfx_hair_scratch1
    scene e04s06-62-mc-lc-lets-fill-you with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "I really like that thought. She can get plenty cum on her face later."
    mc "But right now-"
    play sound sfx_fisting_fist2
    $ Lovense.stop()
    $ Lovense.vibrate(15)
    scene e04s06-63-mc-lc-deepthroat with hpunch
    play voice2 d1s5_orgasm2 noloop
    play voice4 samiya_mfff noloop
    mc "Fucck..."
    scene e04s06-64-mc-lc-deepthroat-extreme with dissolve
    play voice2 d1s5_orgasm noloop
    play voice4 samiya_mfff2 noloop
    mc "I'm about to-"
    $ Lovense.vibrate(16)
    with hpunch
    play voice2 mc_pain_argh1 noloop
    play voice4 samiya_mfff3 noloop
    mc "FFFUuuuuuccccccckkkkkiiiiiinnnngggg"
    $ Lovense.vibrate(17)
    with hpunch
    play voice2 mc_pain_rrrr noloop
    mc "CUuuuuuuUUUuuuuuummmm."
    $ Lovense.vibrate(3)
    scene e04s06-65-lc-coughing with dissolve
    play voice4 daisy_cough noloop
    lc "*cough* *cough*"
    scene e04s06-54-sy-joking with dissolve
    play voice3 stacy_happy_yay3 noloop
    sy "That was fucking awesome! And I got it all on stream!"
    scene e04s06-66-lc-licking with dissolve
    play voice2 d7s4_mcbreathing
    play voice4 daisy_sucking
    mc "*panting* Lydia, you missed a spot. Clean me up."
    mc "Good girl. *panting* I assume that chat liked that?"
    scene e04s06-67-sy-recording with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "Chat LOVED that. We just broke our Tier Four Goal."
    mc "Excellent."
    stop voice4 fadeout 1.0
    play sound sfx_heels_steps1 loop
    $ Lovense.vibrate(1)
    scene e04s06-68-mc-lc-heeling with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Lydia, heel."
    mc "Let's see if you can guess where we are going."
    play sound sfx_door_openclosed1
    stop sound4 fadeout 2.0
    scene e04s06-69-mc-lc-sy-inside-the-loo with fade
    play voice2 mc_thinking_hmm1 noloop
    mc "Here we are. Do you know what this place is?"
    scene e04s06-70-lc-curious with dissolve
    play voice4 dahlia_surprised_ah2 noloop
    lc "The women's restroom in a park?"
    scene e04s06-71-mc-talking with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Yes. Do you know why we're here?"
    scene e04s06-70-lc-curious with dissolve
    play voice4 dahlia_angry_oh noloop
    lc "Oh, god. You're going to make me drink toilet water?"
    scene e04s06-a72 sy-realizing-glambot-72-000 with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.5
    play sound2 ["<silence 2.5>", sfx_camera_fly1] volume 1.5 noloop
    scene e04s06-a72-glambot-1
    pause
    play voice3 stacy_disappointed_oh2 noloop
    sy "That should have been the Tier Four Goal!"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene e04s06-71-mc-talking with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.7
    mc "Good thinking, but no.{w} You can stand up now."
    scene e04s06-73-sy-talking with dissolve
    play voice3 stacy_happy_laugh1 noloop
    sy "Chat figured it out a while ago. Several local guys said they were running for the men's room."
    scene e04s06-74-lc-standing with dissolve
    play voice4 dahlia_disappointed_ehh2 noloop
    lc "I don't understand."
    scene e04s06-75-mc-talking with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "The answer will be obvious to you in a moment."
    play sound sfx_locker_open1
    if e04s06_mk_available is True:
        scene e04s06-a76-1 mk-fuck-terell-anim-01 with dissolve
        play voice3 stacy_thinking_emm3 noloop
        sy "Uh, [mcname]? It seems to be already occupied."
        $ Lovense.pattern("5;10", 1700)
        scene e04s06-a76-1
        play voice5 maria_orgasming
        mk "Oh, hi."
        scene e04s06-a76-2 with dissolve
        pause
        scene e04s06-81-sy-surprised with dissolve
        play voice3 stacy_hey_happy2 noloop
        sy "We're doing a little livestream. There are a few thousand people watching."
        $ Lovense.pattern("5;10", 900)
        scene e04s06-a76-1-f with dissolve
        sy "I'll keep the camera pointed away from you. You can slip out of here silently."
        pause
        scene e04s06-a76-2-f with dissolve
        pause
        sy "And I can edit you out of the video before we upload-"
        scene e04s06-78-mk-hi with dissolve
        $ Lovense.stop()
        $ Lovense.vibrate(4)
        play voice5 maria_argh noloop
        if d15s05_leave is True:
            mk "Meh, this is what I do."
        elif True:
            mk "It's fine. I've done a few livestreams here already."
        scene e04s06-79-sy-hi-back with dissolve
        play voice3 stacy_arrogant_huh1 noloop
        sy "You don't care?"
        scene e04s06-80-mk-talking with dissolve
        play voice5 maria_yes noloop
        mk "Go ahead and film me. It might get more guys to the hole."
        scene e04s06-81-sy-surprised with dissolve
        play voice3 stacy_yes_fine4 noloop
        sy "Okay. If that's what you want."
        scene e04s06-82-mc-waving with dissolve
        play voice2 mc_hey_hey5 noloop
        mc "Hi Maria. How's it going?"
        scene e04s06-83-mk-mc-talking with dissolve
        play voice5 min_old_breathing noloop
        if d15s05_leave is True:
            mk "I'm a fuckhole. This is what I do."
        elif True:
            mk "Couldn't be happier. After you put me here, I realized just how much I love this."
        mk "I'm not a fan of men. Their bodies, their hands all over me, just ew."
        scene e04s06-84-mk-happy with dissolve
        play voice5 maria_laughing noloop
        mk "But their cocks? And their cum? There's nothing better."
        scene e04s06-85-mc-talking with dissolve
        play voice2 d1s5_mchappy noloop
        mc "Well, good, I guess. If that's what you want - more power to you."
        mc "It seems like you found a nicer spot than that gloryhole on campus."
        play sound sfx_likes_starfall loop
        scene e04s06-86-mk-talking with dissolve
        play voice5 min_old_moans
        mk "I can take a little break if you need to use it. Just let me finish up with Terrell here."
        play voice2 mc_yes_yeah1 noloop
        mc "That would be great. Lydia here would love to take the next few dicks."
        stop sound fadeout 1.0
        scene e04s06-87-sy-curious with dissolve
        play voice3 stacy_surprised_huh1 noloop
        sy "Wait. How do you know who's cock that is?"
        scene e04s06-80-mk-talking with dissolve
        mk "I've gotten to recognizing the regulars."
        mk "Besides, he-"
        play voice5 min_old_orgasm1 noloop
        $ Lovense.pattern("9;14", 600)
        scene e04s06-88-mk-ahegao with hpunch
        mk "Ohhhhh, that's the good stuff."
        play voice5 min_old_orgasm3 noloop
        play sound mc_cum_sound1
        $ Lovense.stop()
        $ Lovense.vibrate(15)
        scene e04s06-89-mk-cumming with hpunch
        pause
        scene e04s06-90-mk-view-at-the-hole with dissolve
        $ Lovense.vibrate(3)
        play voice5 min_happy_mmm noloop
        mk "MMmmm. I feel so full.{w} My ass is going to be dripping for hours after that."
        scene e04s06-91-mk-talking with dissolve
        play voice5 min_thinking_hmm2 noloop
        mk "Just let me clean him up and I'll step aside."
        mk "I hope you don't mind if I stay and watch."
        scene e04s06-87-sy-curious with dissolve
        play voice3 stacy_yes_yeah1 noloop
        sy "Uh, yeah..."
        scene e04s06-85-mc-talking with dissolve
        play voice2 mc_yes_sure1 noloop
        mc "Sure. That's fine with me."
    elif True:
        scene e04s06-92-mk-view-at-the-empty-hole with dissolve
        pause
        scene e04s06-93-lc-sy-in-the-stall with dissolve
        play voice4 lydia_huh2 noloop
        play voice2 d4s4_mclaugh noloop volume 1.7
        mc "Welcome to the gloryhole."
        mc "I guess this is your first time."
    scene e04s06-95-sy-talking with dissolve
    $ Lovense.vibrate(1)
    play voice3 stacy_laugh4 noloop
    sy "A few guys in chat say they are lining up on the other side of the wall, waiting for you."
    scene e04s06-94-lc-surprised with dissolve
    play voice4 lydia_moan1 noloop
    lc "Oh fuck."
    scene e04s06-98-sy-talking with dissolve
    play voice3 stacy_huh2 noloop
    sy "Do you know a guy named Zack Olsen?"
    scene e04s06-96-lc-talking with dissolve
    play voice4 lydia_hmmmm noloop
    lc "Sure, we've been friends since-"
    scene e04s06-95-sy-talking with dissolve
    play voice3 stacy_arrogant_ha2 noloop
    sy "Seems like he just paid off every person in line ahead of him so that he can be first."
    scene e04s06-94-lc-surprised with dissolve
    play voice4 lydia_ah noloop
    lc "Zack???"
    scene e04s06-97-lc-surprised with dissolve
    play voice4 dahlia_old_upset noloop
    lc "That's Zack's penis?"
    scene e04s06-98-sy-talking with dissolve
    play voice3 stacy_yes_yap1 noloop
    sy "He's in chat texting that he's \"always wanted to fuck your sweet ass\"."
    sy "But that \"right now I want to feel those soft lips wrapped around my cock\"."
    scene e04s06-99-lc-digusted with dissolve
    play voice4 dahlia_angry_argh1 noloop
    lc "That dick! I thought we were friends!"
    scene e04s06-100-lc-panicing with dissolve
    play voice4 dahlia_sex_closedmoan2 noloop
    lc "I can't do this. Fucking hell. I can't do this."
    play sound sfx_cloth_rustling1
    scene e04s06-101-lc-panicing with dissolve
    play voice4 dahlia_sex_closedmoan3 noloop
    lc "Please, just get that camera out of my face for a second. I can't fucking deal."
    play voice4 dahlia_pain_sobs noloop
    lc "Get a grip, Lydia. You've dealt with worse situations than this."
    lc "Fuck! No, I haven't."
    lc "Whatever. I can do this. I can do this. I can do this."
    scene e04s06-102-lc-asking with dissolve
    play voice4 dahlia_no_high2 noloop
    lc "Don't make me do this."
    lc "There's a way out of this, right?"
    lc "I just have to-"
    scene e04s06-103-lc-asking with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "This is one of those key moments, Lydia."
    mc "Either press the damn button or get over there and start sucking cock."
    if is_antagonist_mode is True:
        play sound sfx_knob_tapping1 loop
        scene e04s06-104-lc-pressing-the-button with hpunch
        play voice4 dahlia_old_angry noloop
        lc "That's it. You win."
        with hpunch
        queue voice4 dahlia_pain_argh noloop
        lc "I give up."
        scene e04s06-105-mc-talking with dissolve
        play voice2 mc_surprised_huh6 noloop
        mc "What do you think you're doing?"
        scene e04s06-106-lc-confused with dissolve
        play voice4 dahlia_pain_ah2 noloop
        lc "I'm pressing the button."
        scene e04s06-107-mc-talking with dissolve
        play voice2 mc_yes_yeah8 noloop
        mc "And what do you think that will do?"
        stop sound fadeout 1.0
        scene e04s06-108-lc-confused with dissolve
        play voice4 lydia_oof noloop
        lc "I...{w} I don't know."
        lc "Let's the Judge or someone know that I've had enough?"
        play voice2 mc_yes_yeah7 noloop
        mc "And what do you think that would accomplish?"
        play voice4 dahlia_disappointed_hmm2 noloop
        lc "Someone would come and take me back to prison."
        lc "I don't care. I'll serve my full sentence. I just can't take it anymore."
        scene e04s06-107-mc-talking with dissolve
        play voice2 mc_no_nah1 noloop
        mc "It doesn't do anything like that. It just signals to me that you've given up."
        mc "You wanted to break me. You wanted to make me your slave."
        mc "Instead, I've broken you."
        play voice2 mc_arrogant_heh1 noloop
        mc "I've won, bitch."
        play sound sfx_knob_tapping1 volume 0.5
        scene e04s06-106-lc-confused with dissolve
        play voice4 dahlia_pain_ah1 noloop
        lc "I can't go back to prison? I'm stuck here with you?"
        play voice2 mc_yes_yes2 noloop
        mc "Exactly."
        stop sound fadeout 1.0
        scene e04s06-100-lc-panicing with dissolve
    elif True:
        scene e04s06-109-lc-asking with dissolve
    play voice4 lydia_morningoh noloop
    lc "What's next?"
    scene e04s06-110-mc-confused with dissolve
    play voice2 d1s2_hmm noloop volume 1.5
    mc "What do you mean?"
    play sound sfx_likes_starfall loop
    scene e04s06-111-lc-looking-at-the-camera with dissolve
    play voice4 dahlia_happy_hmm1 noloop
    lc "You've humiliated me in public. You've spread my humiliation across the internet."
    lc "You've brought me to a gloryhole and are going to livestream me servicing random cocks."
    lc "What's next? Are you going to drag me naked to the courthouse steps and punish me for all to see?"
    stop sound fadeout 1.0
    scene e04s06-112-mc-lc-talking with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "I was thinking about setting up a pillory in front of city hall."
    scene e04s06-113-mc-lc-smiling with dissolve
    play voice2 mc_happy_a1 noloop
    mc "The mayor's office is considering it. They're currently unsure of how it would affect his reelection campaign."
    scene e04s06-109-lc-asking with dissolve
    play voice4 lydia_aga noloop
    lc "Okay."
    lc "I understand."
    if e04s06_mk_available is True:
        scene e04s06-114-mc-mk-confused with dissolve
        play voice5 maria_what noloop
        mk "I'm sorry, what is that? What's going on here?"
        scene e04s06-115-mc-mk-talking with dissolve
        play voice2 mc_thinking_oh1 noloop
        mc "Oh, I can explain."
        scene e04s06-116-mk-talking with dissolve
        play voice5 maria_argh noloop
        mk "Now that I think about it... Shouldn't she be in prison?"
        scene e04s06-117-mc-talking with dissolve
        play voice2 mc_no_no2 noloop
        mc "Like I said, I can explain."
        scene e04s06-118-mk-happy with dissolve
        play voice5 min_old_laugh noloop
        mk "Well, go on then. I can't wait to hear this."
        scene e04s06-119-mc-confused with fade
        play voice2 mc_yes_yeah5 noloop
        mc "So, that's pretty much it. Lydia is a prisoner. I am her warden."
        scene e04s06-120-mc-happy with dissolve
        play voice2 mc_thinking_hmm3 noloop
        mc "I have a few guards working for me. There are also some voluntary prisoners and/or slaves."
        mc "My job is to punish Lydia, but it's turning into a whole kind of sex harem thing."
        scene e04s06-121-mk-excited with dissolve
        play voice5 maria_aah noloop
        mk "Fascinating. How much do your voluntary prisoners have to pay for the experience?"
        scene e04s06-120-mc-happy with dissolve
        play voice2 mc_surprised_what1 noloop
        mc "Excuse me?"
        scene e04s06-118-mk-happy with dissolve
        play voice5 min_surprised_ehh1 noloop
        mk "How much would I need to pay? I've made a good bit working these gloryholes."
        scene e04s06-119-mc-confused with dissolve
        play voice2 mc_thinking_emm1 noloop
        mc "Umm... okay."
        mc "Can you call me tomorrow? We can work out the details."
        scene e04s06-121-mk-excited with dissolve
        play voice5 maria_yes noloop
        mk "Terrific. Looking forward to it."
    scene e04s06-122-lc-take-it-off with dissolve
    play voice4 lydia_lydiahey noloop
    lc "You can take this off me. I don't need it anymore."
    scene e04s06-123-mc-curious with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "Tell me why."
    scene e04s06-124-lc-accepting-defeat with dissolve
    play voice4 dahlia_disappointed_ehh2 noloop
    if is_antagonist_mode is True:
        lc "It's useless. But there's more to it than that."
    lc "I don't need it anymore."
    lc "I've accepted my place. Do whatever you want with me.{w} And I'll do whatever you tell me to do."
    scene e04s06-125-lc-accepting-defeat with dissolve
    play voice4 lydia_moan1 noloop
    lc "I don't need it anymore. It's over."
    lc "I am yours."
    scene e04s06-126-mc-happy with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "I'm glad to hear you say that. It saves me a lot of trouble."
    mc "Still, I think I will continue to have you wear it."
    scene e04s06-127-lc-lemme-do-it with dissolve
    play voice4 lydia_oof noloop
    lc "Why?"
    play voice2 mc_thinking_hmm1 noloop
    mc "As a reminder, but mostly because I like the way it looks on you."
    if e04s06_mk_available is True:
        scene e04s06-128-mk-observing with dissolve
        pause
    play voice4 dahlia_thinking_hmm4 noloop
    lc "Well, I better get in there and start sucking cocks."
    menu:
        "I want to see that."(hint="e04s06m01c01"):
            $ e04s06_lc_suck = True
            jump e04s06_ntr
        "No need. I proved my point."(hint="e04s06m01c02"):

            $ e04s06_lc_suck = False
            jump e04s06_no_ntr

label e04s06_no_ntr:

    scene e04s06-129-mc-talking with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Don't bother."
    scene e04s06-130-lc-talking with dissolve
    play voice4 dahlia_surprised_huh2 noloop
    lc "Why not? Isn't that what you want me to do?"
    scene e04s06-131-mc-sad with dissolve
    play voice2 mc_no_uhuh1 noloop
    mc "I never wanted to see you do that."
    mc "I thought it was necessary, but after what you just said..."
    mc "Forget it. Let's get you back to your cage."
    play sound sfx_skirt_off2
    scene e04s06-132-mc-lc-comforting with dissolve
    play voice4 lydia_oops noloop
    lc "Okay.{w} Are you still planning on uploading the video of all this online?"
    play voice2 mc_yes_yeah2 noloop
    mc "Yup."
    scene e04s06-133-lc-asking with dissolve
    play voice4 dahlia_thinking_mmm2 noloop
    lc "So when I'm ninety years old there will still be guys jerking off to my humiliation today?"
    scene e04s06-135-sy-telling with dissolve
    play voice3 stacy_happy_laugh1 noloop
    sy "Not just guys."
    scene e04s06-134-mc-telling with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.5
    mc "I'm sure you'll be very popular at the retirement home."
    scene e04s06-137-mc-lc-walking-away with dissolve
    play voice4 dahlia_arrogant_heh noloop
    lc "*sarcastically* Terrific. Wonderful. Something to look forward to..."
    if e04s06_mk_available is True:
        scene e04s06-138-mk-aww with dissolve
        play voice5 min_disappointed_ehh2 noloop
        mk "That was kinda sweet."
        mk "Still, I can't help thinking I should feel offended."
        scene e04s06-139-mk-more-cocks with dissolve
        play voice5 min_surprised_oh noloop
        mk "Oh, well. More for me!"
        $ Lovense.vibrate(6)
        scene e04s06-140-mk-sucking-it with dissolve
        play voice5 aaleyah_sucking_deep
        pause
        stop voice5 fadeout 2.0
        scene e04s06-141-zo-wtf with dissolve
        play voice6 boy5_angry_breathing noloop
        pause
    elif True:
        scene e04s06-141-zo-wtf with dissolve
        play voice6 boy5_hey_angry noloop
        zo "Hello?"
        zo "I'm still waiting here..."
        zo "Goddammit."

    stop music fadeout 4.0

    $ Lovense.stop()


    $ renpy.end_replay()
    jump e04s07

label e04s06_ntr:

    scene e04s06-142-mc-talking with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "There's no time like the present."
    scene e04s06-127-lc-lemme-do-it with dissolve
    play voice4 dahlia_disappointed_hmm2 noloop
    lc "Yeah."
    scene e04s06-145-mc-talking with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "And listen to Stacy."
    scene e04s06-143-sy-talking with dissolve
    play voice3 stacy_oh2 noloop
    sy "Oh?"
    play voice2 mc_thinking_hmm4 noloop
    mc "We want to make sure this looks as good as possible for the camera."
    sy "Oh, right."
    if e04s06_mk_available is True:
        scene e04s06-144-mk-talking with dissolve
        play voice5 min_arrogant_huh1 noloop
        mk "Sounds like you've got this covered for a while."
        play voice2 d9s2_yeah noloop volume 2.0
        mc "Yeah. I only plan to keep her here for an hour or two, but we'll see how it goes."
        mk "Cool. Then I'm going to get some lunch."
        play sound sfx_barefoot_steps1 loop volume 2.0
        scene e04s06-146-mk-walking-out with dissolve
        play voice2 d1s1_mmm noloop volume 2.0
        mct "Is that a tramp stamp? \"One Size Fits All\"?"
        mct "*sarcastically* Classy."
        scene e04s06-147-mc-asking with dissolve
        play voice2 mc_happy_yay2 noloop
        mc "Forgetting something?{w} Don't you need your clothes?"
        scene e04s06-148-mk-talking with dissolve
        play voice5 min_no_nah noloop
        mk "Nah, I'm good. See you in about forty-five minutes."
        stop sound fadeout 1.0
    scene e04s06-149-sy-talking with dissolve
    pause
    scene e04s06-150-sy-talking with dissolve
    play voice3 stacy_yes_yap3 noloop
    sy "That's perfect."
    sy "Hold that pose while I get the camera into position."
    scene e04s06-151-sy-talking with dissolve
    play voice3 stacy_yes_ugu1 noloop
    sy "Just a moment longer."
    sy "Breathe in through your nose and really capture the scent of this place and the penis in front of you."
    scene e04s06-152-sy-asking-pov with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "Tell me what it feels like right now."
    play voice4 dahlia_disappointed_hmm1 noloop
    lc "It's disgusting. He has a heavy masculine scent, but something else. I think he didn't clean himself up after jerking off earlier."
    play voice3 stacy_disappointed_oh7 noloop
    sy "You should get used to that."
    scene e04s06-153-lc-grossed-out with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    sy "I imagine most of the guys waiting over there came at least once watching this livestream earlier today."
    play voice4 dahlia_disappointed_ehh3 noloop
    lc "The room itself smells worse. Sour milk, urine, yet the strong undercurrent of some cleaner. Bleach?"
    play voice3 stacy_hey_attention1 noloop
    sy "That's good. Why don't you give Zack's cock a little kiss to get started?"
    scene e04s06-154-lc-kissing-it with dissolve
    play sound maria_kiss1
    pause
    scene e04s06-155-sy-talking with dissolve
    $ Lovense.vibrate(2)
    play voice3 stacy_happy_relief1 noloop
    sy "This place could use another round of bleach. Maybe after we leave."
    sy "That sour milk smell is dried cum, by the way."
    sy "That's a nice kiss. Why don't you use your tongue a bit as well?"
    scene e04s06-156-lc-licking-it with dissolve
    play voice4 daisy_dlick noloop volume 1.5
    play voice3 stacy_thinking_hmm2 noloop
    $ Lovense.vibrate(3)
    sy "Beautiful. You've clearly done this before."
    scene e04s06-157-sy-encouraging-it with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "Giving head, I mean. I have no doubt this is your first experience working in a gloryhole."
    sy "It's a shame the wall is there. I would love to see you licking his balls."
    scene e04s06-158-lc-sucking with dissolve
    $ Lovense.vibrate(5)
    play voice4 daisy_sucking
    play voice3 stacy_thinking_oh2 noloop
    sy "Very nice. I didn't know you could do that."
    play voice2 mc_scared_oh3 noloop
    mc "She's very talented."
    sy "That's enough foreplay. You may start slowly sucking that dick now."
    scene e04s06-159-lc-blowing with dissolve
    play voice3 stacy_moan6 noloop
    sy "Oh baby, you really are talented."
    sy "I thought I was good, but that looks really good."
    sy "I should watch this video later so I can take notes."
    sy "How about you show off your deepthroat skills. Can you kiss the wall around his cock?"
    scene e04s06-a159-1 lc-blowing-gloryhole-anim-01 with dissolve
    pause
    play voice4 aaleyah_sucking_deep
    $ Lovense.pattern("8;11", 1400)
    scene e04s06-a159-1
    play voice3 stacy_surprised_wow1 noloop
    sy "Amazing! You were born for this."
    scene e04s06-a159-2 with dissolve
    play voice3 stacy_yay noloop
    sy "Just look at those luscious lips kissing that dirty-ass gloryhole wall!"
    scene e04s06-a159-3 with dissolve
    sy "Okay, you can suck him off properly anytime that you want."
    pause
    $ Lovense.pattern("8;12", 700)
    scene e04s06-a159-1-f with dissolve
    pause
    scene e04s06-a159-2-f with dissolve
    pause
    scene e04s06-a159-3-f with dissolve
    pause
    scene e04s06-162-lc-talking with dissolve
    $ Lovense.stop()
    $ Lovense.vibrate(5)
    play voice4 daisy_sucking
    pause
    scene e04s06-163-lc-licking with dissolve
    play voice3 stacy_happy_phew3 noloop
    sy "Damn, girl. That looks very professional."
    sy "Are you sure you hadn't done this before? Maybe some amateur porn films?"
    play voice4 daisy_dlick noloop
    play sound sfx_handjob_cream1 volume 2.5 loop
    scene e04s06-164-lc-pumping with dissolve
    sy "Do you teach classes?"
    play sound2 sfx_likes_starfall
    scene e04s06-165-lc-looking-at-the-cam with dissolve
    play voice3 stacy_surprised_oh1 noloop
    sy "Oh, is he getting close?"
    stop sound2 fadeout 1.0
    scene e04s06-163-lc-licking with dissolve
    play voice4 daisy_sucking
    lc "*mumbles* Yesh."
    stop sound fadeout 1.0
    $ Lovense.pattern("8;12", 1400)
    scene e04s06-160-lc-blowing with dissolve
    play voice4 aaleyah_sucking_deep
    play voice3 stacy_yes_fine2 noloop
    sy "Good, good. But don't talk with your mouth full."
    sy "We'll change it up every time, but for this first dick I want you to spray it all over your face."
    scene e04s06-161-lc-blowing with dissolve
    play voice3 stacy_thinking_emm4 noloop
    sy "Don't accidentally get it in your mouth.{w} What am I saying - you're clearly a pro at this."
    sy "Aim for your eyes and nostrils, if you can."
    sy "The audience at home would love to see that."
    play sound2 sfx_likes_starfall
    $ Lovense.stop()
    $ Lovense.vibrate(8)
    scene e04s06-165-lc-looking-at-the-cam with dissolve
    play voice4 dahlia_disappointed_hmm2 noloop
    play voice3 stacy_yes_okay1 noloop
    sy "That's great, but can you look directly at the camera?"
    sy "Turn your head a bit. I want to capture this moment perfectly."
    stop sound2 fadeout 1.0
    play sound sfx_handjob_cream1 volume 2.5 loop
    scene e04s06-166-lc-zo-cumming with dissolve
    play voice3 stacy_disappointed_oh3 noloop
    sy "That's gorgeous."
    sy "You..."
    play sound mc_cum_sound1
    $ Lovense.vibrate(15)
    scene e04s06-167-lc-zo-cumming with hpunch
    play voice3 stacy_happy_hmm1 noloop
    sy "... Are..."
    play voice4 lydia_ah noloop
    $ Lovense.vibrate(16)
    scene e04s06-168-lc-zo-cumming with hpunch
    sy "... So..."
    scene e04s06-169-lc-looking-at-the-camera-again with dissolve
    $ Lovense.vibrate(3)
    play voice3 stacy_disappointed_mmm1 noloop
    play voice4 lydia_moan1 noloop
    sy "... Pretty."
    sy "Gorgeous. Absolutely perfect."
    sy "You wear that so well."
    sy "But don't forget about your little friend there. Give him a kiss."
    scene e04s06-170-lc-kissing-it with dissolve
    play sound maria_kiss1
    play voice3 stacy_yes_yap2 noloop
    sy "Lovely. Now let's see that tongue clean him up."
    scene e04s06-171-lc-licking-it with dissolve
    play voice4 daisy_sucking
    play voice3 stacy_arrogant_hmm3 noloop
    sy "Wonderful. Tell me, how does being covered in cum make you feel?"
    scene e04s06-172-lc-talking with dissolve
    play voice4 lydia_haha noloop volume 1.5
    lc "It is what [alt_mcname] wants. That is my purpose."
    play sound sfx_likes_starfall loop
    scene e04s06-173-sy-pov with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "Okay, good answer. Ummm...{w} How does this make you feel, Lydia?"
    play voice4 dahlia_thinking_mmm2 noloop
    lc "I love it. I am serving [alt_mcname]. I want nothing else."
    $ unlock_gallery_slot("scene", "e04s06")
    stop sound fadeout 1.0
    scene e04s06-174-mc-pov with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "Huh. Interesting."
    sy "Do you have anything you want to say to the audience at home?"
    play sound sfx_likes_starfall loop
    scene e04s06-173-sy-pov with dissolve
    play voice4 lydia_lydyes noloop
    lc "Yes, I think I do."
    stop sound fadeout 1.0
    scene e04s06-175-tr-close-up with dissolve
    pause
    scene e04s06-176-lc-close-up with dissolve
    play voice4 lydia_laugh noloop
    lc "Get in line."
    stop music fadeout 4.0

    $ Lovense.stop()


    $ renpy.end_replay()

    jump e04s07

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
