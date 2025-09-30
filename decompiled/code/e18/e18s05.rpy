image e18s05-a54-1 = Movie(play = "images/E-18/s05/anim/e18s05-a54-1-2x-50fps.webm", start_image = "e18s05-a54-1 mc-sb-anim-01")
image e18s05-a54-1-f = Movie(play = "images/E-18/s05/anim/e18s05-a54-1-2x-60fps.webm", start_image = "e18s05-a54-1 mc-sb-anim-01")
image e18s05-a54-2 = Movie(play = "images/E-18/s05/anim/e18s05-a54-2-2x-50fps.webm", start_image = "e18s05-a54-2 mc-sb-anim-01")
image e18s05-a54-2-f = Movie(play = "images/E-18/s05/anim/e18s05-a54-2-2x-60fps.webm", start_image = "e18s05-a54-2 mc-sb-anim-01")
image e18s05-a54-3 = Movie(play = "images/E-18/s05/anim/e18s05-a54-3-2x-50fps.webm", start_image = "e18s05-a54-3 mc-sb-anim-01")
image e18s05-a54-3-f = Movie(play = "images/E-18/s05/anim/e18s05-a54-3-2x-60fps.webm", start_image = "e18s05-a54-3 mc-sb-anim-01")

image e18s05-a59-1 = Movie(play = "images/E-18/s05/anim/e18s05-a59-1-2x-50fps.webm", start_image = "e18s05-a59-1 mc-sb-anim-01")
image e18s05-a59-1-f = Movie(play = "images/E-18/s05/anim/e18s05-a59-1-2x-60fps.webm", start_image = "e18s05-a59-1 mc-sb-anim-01")
image e18s05-a59-2 = Movie(play = "images/E-18/s05/anim/e18s05-a59-2-2x-50fps.webm", start_image = "e18s05-a59-2 mc-sb-anim-01")
image e18s05-a59-2-f = Movie(play = "images/E-18/s05/anim/e18s05-a59-2-2x-60fps.webm", start_image = "e18s05-a59-2 mc-sb-anim-01")
image e18s05-a59-3 = Movie(play = "images/E-18/s05/anim/e18s05-a59-3-2x-50fps.webm", start_image = "e18s05-a59-3 mc-sb-anim-01")
image e18s05-a59-3-f = Movie(play = "images/E-18/s05/anim/e18s05-a59-3-2x-60fps.webm", start_image = "e18s05-a59-3 mc-sb-anim-01")
image e18s05-a59-4 = Movie(play = "images/E-18/s05/anim/e18s05-a59-4-2x-50fps.webm", start_image = "e18s05-a59-4 mc-sb-anim-01")
image e18s05-a59-4-f = Movie(play = "images/E-18/s05/anim/e18s05-a59-4-2x-60fps.webm", start_image = "e18s05-a59-4 mc-sb-anim-01")

image e18s05-a64-1 = Movie(play = "images/E-18/s05/anim/e18s05-a64-1-2x-50fps.webm", start_image = "e18s05-a64-1 mc-sb-anim-01")
image e18s05-a64-1-f = Movie(play = "images/E-18/s05/anim/e18s05-a64-1-2x-60fps.webm", start_image = "e18s05-a64-1 mc-sb-anim-01")
image e18s05-a64-2 = Movie(play = "images/E-18/s05/anim/e18s05-a64-2-2x-50fps.webm", start_image = "e18s05-a64-2 mc-sb-anim-01")
image e18s05-a64-2-f = Movie(play = "images/E-18/s05/anim/e18s05-a64-2-2x-60fps.webm", start_image = "e18s05-a64-2 mc-sb-anim-01")
image e18s05-a64-3 = Movie(play = "images/E-18/s05/anim/e18s05-a64-3-2x-50fps.webm", start_image = "e18s05-a64-3 mc-sb-anim-01")
image e18s05-a64-3-f = Movie(play = "images/E-18/s05/anim/e18s05-a64-3-2x-60fps.webm", start_image = "e18s05-a64-3 mc-sb-anim-01")
image e18s05-a64-4 = Movie(play = "images/E-18/s05/anim/e18s05-a64-4-2x-50fps.webm", start_image = "e18s05-a64-4 mc-sb-anim-01")
image e18s05-a64-4-f = Movie(play = "images/E-18/s05/anim/e18s05-a64-4-2x-60fps.webm", start_image = "e18s05-a64-4 mc-sb-anim-01")

label e18s05:

    $ e18s05_not_dork = False
    $ e18s05_sb_deserves_it = False
    $ e18s05_oogle_sb = False
    $ e18s05_mc_dom = False

    scene black
    show screen scene_transistion(_("A few days later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(1.0, 3.0, "music")
    $ renpy.music.set_volume(0.0, 0.0, "music2")
    $ renpy.music.play(audio.music_lofispers, "music" , True, None, True, 0.0)
    $ renpy.music.play(audio.music_lofispers_reverbed, "music2", True, None, True, 0.0)
    play sound ["<silence 1.2>", knockknock]
    play sound2 sfx_door_open1 noloop
    scene e18s05-1 mc-sb-walk1_c1
    with Fade(0.5, 0.5, 0.9)
    pause
    scene e18s05-1 mc-sb-walk1_c2 with dissolve
    play sound sfx_phone_tapping1 loop volume 2.0
    pause
    play sound2 sfx_heels_steps2 fadein 1.0
    scene e18s05-2 mc-sb-walk2_c1 with dissolve
    play voice2 d2s9_mchey noloop
    mc "Hey, Samiya. Everything okay?"
    stop sound2 fadeout 1.0
    play sound sfx_cloth_rustling2
    scene e18s05-2 mc-sb-walk2_c2 with dissolve
    play voice3 samiya_hmm1 noloop
    sb "Why so curious, [mcname]?"
    mct "How does she look so good without even trying?"
    mct "Get a hold of yourself man."
    scene e18s05-3 mc-sb-phone_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "Uh, Mistress just wanted me to see how you were doing."
    mc "We haven't seen you since breakfast."
    play sound sfx_phone_tapping1 loop volume 2.0
    scene e18s05-3 mc-sb-phone_c2 with dissolve
    play voice3 samiya_laughing1 noloop
    sb "Mistress. Hahaha."
    sb "You really buy that hook, line, and sinker, don't you?"
    stop sound fadeout 1.0
    scene e18s05-4 mc-sb-phone2_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "I like Dahlia's games a lot more than I liked Lydia's."
    play sound2 sfx_cloth_rustling3 noloop
    scene e18s05-4 mc-sb-phone2_c2 with dissolve
    play sound sfx_phone_tapping1 loop
    play voice3 girl35_thinking_hmm5 noloop
    sb "You don't talk about Lydia much, do you?"
    stop sound fadeout 1.0
    scene e18s05-5 mc-sb-stand_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "What is there to talk about?"
    play sound sfx_phone_tapping1 loop
    scene e18s05-5 mc-sb-stand_c2 with dissolve
    play voice3 girl35_yes_yeah1 noloop
    sb "Yeah. I figured as much."
    stop sound fadeout 1.0
    scene e18s05-5 mc-sb-stand_c3 with dissolve
    play voice3 girl35_thinking_eem6 noloop
    sb "Tell Dahlia she doesn't have to worry about me. I'm fine."
    scene e18s05-7 mc-sb-phone_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "It would probably go a lot further if that came from you."
    play sound2 sfx_cloth_rustling4 noloop
    scene e18s05-7 mc-sb-phone_c2 with dissolve
    play sound sfx_phone_tapping1 loop
    play voice3 samiya_hah1 noloop
    sb "Heh. Scared of our girlfriend, are we?"
    stop sound fadeout 1.0
    scene e18s05-8 mc-sb-chuckles_c1 with dissolve
    play voice2 mc_no_no6 noloop
    mc "No. But I know what she likes and doesn't like."
    scene e18s05-8 mc-sb-chuckles_c2 with dissolve
    play voice3 samiya_hm1 noloop volume 1.7
    sb "Go downstairs and get the car ready, [mcname]."
    play sound sfx_cloth_rustling5
    scene e18s05-9 mc-sb-stand_c1 with dissolve
    play voice2 mc_surprised_why3 noloop
    mc "Okay. Uh... why?"
    scene e18s05-9 mc-sb-stand_c2 with dissolve
    play voice3 samiya_geh noloop volume 1.5
    sb "Since you're {i}so{/i} worried about me, then it's high time I got treated to a day where we get to do everything I want to do."
    scene e18s05-10 mc-sb-stand2_c1 with dissolve
    play voice2 d1s1_mmm noloop volume 1.6
    mct "Why am I suddenly a little scared?"

    jump e18s05_car

label e18s05_car:

    play sound3 sfx_car_inside_ride1 fadein 1.0
    play sound4 sfx_car_drive1 volume 0.15
    scene e18s05-11 mc-sb-car_c2 with Fade(0.5, 0.5, 0.5)
    play voice3 girl35_yes_aga9 noloop
    sb "First, we're going to find a salon so I can get a manicure."
    scene e18s05-11 mc-sb-car_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Your nails look fine."
    scene e18s05-12 mc-sb-talk_c2 with dissolve
    play voice3 girl35_no_laughing noloop
    sb "It's been weeks since we got here, and I've been doing my nails on my own."
    sb "I {b}want{/b} my manicure, [mcname]."
    scene e18s05-12 mc-sb-talk_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay okay. A manicure."
    scene e18s05-13 mc-sb-talk2_c2 with dissolve
    play voice3 girl35_thinking_hm2 noloop
    sb "And then you're taking me out to lunch. Your treat."
    scene e18s05-13 mc-sb-talk2_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hey, you know you're not supposed to boss me around."
    scene e18s05-14 mc-sb-talk3_c1 with dissolve
    play voice2 mc_disgust_meh4 noloop
    mc "Dahlia does enough of that."
    scene e18s05-14 mc-sb-talk3_c2 with dissolve
    play voice3 samiya_eeem1 noloop volume 1.4
    if d14s14_mc_wins is True:
        sb "Consider it payback for when you pounded me after mud wrestling!"
    else:
        sb "Come on [mcname], I know you got thick skin."
    sb "Besides, you can't say you don't enjoy a little teasing now and then."
    scene e18s05-15 mc-sb-talk4_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure, I like you teasing me as much as you like me dominating you."
    scene e18s05-15 mc-sb-talk4_c2 with dissolve
    play voice3 samiya_mmm3 noloop volume 1.4
    sb "..."
    scene e18s05-16 mc-sb-talk5_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "What's wrong? Worried about being in a stolen car?"
    scene e18s05-16 mc-sb-talk5_c2 with dissolve
    play voice3 samiya_no1 noloop volume 1.5
    sb "No. We've had it parked at the car wash for a few days now."
    sb "If it was reported stolen, the cops would have returned by this point."
    scene e18s05-17 mc-sb-look_c1 with dissolve
    play voice3 girl35_happy_laugh2 noloop
    sb "And if we do get in trouble, I'll just put on my best damsel act. You'll be the one in trouble."
    scene e18s05-17 mc-sb-look_c2 with dissolve
    play voice2 mc_angry_off noloop
    mc "I hope that is more of your teasing, Samiya."
    play voice3 girl35_happy_mmm4 noloop
    sb "Maybe."
    stop sound4 fadeout 1.5
    stop sound3 fadeout 2.0

    jump e18s05_shopping

label e18s05_shopping:

    $ renpy.music.set_volume(1.6, 3.5, "music")
    scene black
    show screen scene_transistion(_("After Samiya's manicure\n&\nAn expensive lunch"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.0, 1.5, "music")
    $ renpy.music.set_volume(1.0, 1.0, "music2")
    play sound sfx_door_closed7
    scene e18s05-18 mc-sb-walk_c1
    with Fade(0.5, 0.5, 0.9)
    mc "What is this place?"
    scene e18s05-18 mc-sb-walk_c2 with dissolve
    sb "This is the BDSM shop Dahlia and I found. I want to check out the dresses."
    mc "Fine."
    play voice3 samiya_huh4 noloop
    sb "Why are you acting so stiff, [mcname]?"
    scene e18s05-18 mc-sb-walk_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "Well, you were worried about the car earlier, and now we've parked it in plain sight again."
    mc "Just feels a little risky I guess."
    play sound sfx_cloth_rustling3
    scene e18s05-19 mc-sb-talk_c2 with dissolve
    play voice3 samiya_yes2 noloop
    sb "Yeah, but {i}you{/i} like risky, don't you? There is no adventure without a little risk."
    sb "There is no need to worry. Like I said, if a problem was going to happen it would have happened already."
    scene e18s05-20 mc-sb-talk2_c1 with dissolve
    play voice3 girl35_arrogant_hm2 noloop
    sb "So relax, dork."
    menu:
        "I'm no dork."(hint="e18s05m01c01"):
            $ e18s05_not_dork = True
            $ e18_mc_cocky_points += 1
            play sound sfx_cloth_rustling1
            scene e18s05-21 mc-sb-talk3_c1 with dissolve
            play voice2 mc_disappointed_ehh1 noloop
            mc "I'm no dork, Samiya."
            scene e18s05-21 mc-sb-talk3_c2 with dissolve
            play voice3 girl35_disappointed_oh3 noloop
            sb "I guess you're right. I'd never let a dork do all the stuff you've done to me."
            sb "Mmm. You know, you're the only dork that's ever gotten into my pants."
            play sound sfx_heels_steps1 loop
            scene e18s05-22 mc-sb-talk4_c1 with dissolve
            play voice2 mc_yes_aga2 noloop
            mc "Multiple times, too."
            scene e18s05-22 mc-sb-talk4_c2 with dissolve
            play voice3 girl35_happy_laugh4 noloop
            sb "Haha. Don't remind me."
            stop sound fadeout 1.0
            scene e18s05-24 mc-sb-wave_c2 with dissolve
            play voice3 girl35_happy_mmm3 noloop
            sb "Come on, time to watch me ogle some dresses. That's a win if I ever heard one."
        "You love teasing me."(hint="e18s05m01c02"):

            play sound sfx_cloth_rustling1
            scene e18s05-23 mc-sb-talk5_c1 with dissolve
            play voice2 mc_surprised_uh1 noloop
            mc "You love teasing me, don't you?"
            scene e18s05-23 mc-sb-talk5_c2 with dissolve
            play voice3 girl35_disappointed_oh3 noloop
            sb "I tease you, and one time you stuck your cock inside me and spanked me when you were supposed to be my plaything."
            sb "Let's call it even, dork. Maybe I'll even let you have some fun with me later."
            play sound sfx_heels_steps1 loop
            scene e18s05-25 mc-sb-walk_c2 with dissolve
            play voice3 girl35_happy_laugh4 noloop
            sb "Haha just kidding. I don't know what you're mad about."
            sb "Dork is miles above 'worm', haha."
            stop sound fadeout 1.0
            scene e18s05-26 mc-sb-talk_c1 with dissolve
            play voice2 mc_yes_aga2 noloop
            mc "I guess so."
            scene e18s05-26 mc-sb-talk_c2 with dissolve
            play voice3 girl35_happy_mmm3 noloop
            sb "Come on, don't give me that long face. I'm going to let you watch me try on some dresses."
            sb "So you're still coming out ahead today."

    scene e18s05-27 mc-sb-look_c1 with dissolve
    play sound sfx_cloth_rustling2
    pause
    scene e18s05-27 mc-sb-look_c2 with dissolve
    play voice3 girl35_surprised_wow5 noloop
    sb "Woah. Elegant has never looked so sexy."
    play sound sfx_cloth_rustling5
    scene e18s05-28 mc-sb-dress_c2 with dissolve
    play voice3 girl35_thinking_eem5 noloop
    sb "It's a nice dress, but I probably wouldn't wear something like this at the car wash."
    scene e18s05-31 mc-sb-dress_c1 with dissolve
    sb "What do you think?"
    play voice2 mc_thinking_mmm2 noloop
    mc "Very hot. Could be nice for a night out at some club."
    scene e18s05-31 mc-sb-dress_c2 with dissolve
    play voice3 girl35_disappointed_geh3 noloop
    sb "Gah. Clubs are just expensive, noisy bars with more room to dance and no food." id e18s05_shopping_55b56984
    play sound sfx_cloth_dress_off2
    scene e18s05-32 mc-sb-dress2_c2 with dissolve
    play voice3 samiya_hm2 noloop
    sb "Speaking of expensive..."
    scene e18s05-33 mc-sb-sad_c2 with dissolve
    play voice3 samiya_ou2 noloop
    sb "Damn. I can't buy this. Dahlia would absolutely kill me for spending a chunk of our change on a dress."
    scene e18s05-30 mc-sb-talk_c2 with dissolve
    play voice3 girl35_thinking_hmf3 noloop
    sb "I'm sure you eventually want to live in a place that is bigger than a shoebox."
    menu:
        "You deserve it."(hint="e18s05m02c01"):
            $ e18s05_sb_deserves_it = True
            scene e18s05-34 mc-sb-talk_c1 with dissolve
            play voice2 mc_happy_a1 noloop
            mc "You deserve it."
            scene e18s05-34 mc-sb-talk_c2 with dissolve
            play voice3 girl35_arrogant_pff3 noloop
            sb "Shut up."
            scene e18s05-35 mc-sb-talk2_c1 with dissolve
            play voice2 mc_happy_yay2 noloop
            mc "Come on. You deserve a reward now and then, Samiya."
            jump e18s05_ogling_menu
        "Yes, please."(hint="e18s05m02c02"):

            scene e18s05-30 mc-sb-talk_c1 with dissolve
            play voice2 mc_yes_yes6 noloop volume 0.8
            mc "Yes, please. Most nights I'm always sharing a bed with Dahlia."
            mc "But when I'm not, and I have to bunk with Pete, he steals all the damn covers."
            scene e18s05-29 mc-sb-dress2_c2 with dissolve
            play voice3 girl35_happy_laugh5 noloop
            sb "Well then I'll do my best to spare you such a humiliating fate."
            scene e18s05-32 mc-sb-dress2_c2 with dissolve
            play voice3 girl35_thinking_hmm1 noloop
            sb "Still, I guess it wouldn't hurt to try it on."
            jump e18s05_dressing_room

label e18s05_ogling_menu:

    scene e18s05-35 mc-sb-talk2_c2 with dissolve
    play voice3 samiya_yes1 noloop
    sb "That's what I call playing with you and Pete."
    scene e18s05-36 mc-sb-talk3_c1 with dissolve
    play voice2 d9s2_yeah noloop volume 2.0
    mc "Yeah, but this would be just for you, Samiya."
    scene e18s05-36 mc-sb-talk3_c2 with dissolve
    play voice3 girl35_disgust_oof2 noloop
    sb "Oooh? You wouldn't be checking me out all the time if I wore this?"
    menu:
        "Totally."(hint="e18s05m03c01"):
            $ e18_mc_cocky_points += 1
            $ e18s05_oogle_sb = True
            scene e18s05-37 mc-sb-talk4_c1 with dissolve
            play voice2 d9s2_mcyes noloop volume 2.0
            mc "Totally. It would give me one more reason to enjoy that ass."
            scene e18s05-37 mc-sb-talk4_c2 with dissolve
            play voice3 girl35_happy_laugh1 noloop
            sb "Even in another country, you are such a perve, [mcname]."
            scene e18s05-39 mc-sb-talk6_c1 with dissolve
            play voice2 mc_arrogant_heh3 noloop
            mc "I swear it's just this island fever."
            scene e18s05-39 mc-sb-talk6_c2 with dissolve
            play voice3 girl35_arrogant_laugh noloop
            sb "Hahah. We better not fix you too soon, then. I guess at the very least, I can try it on."
        "Nah, but I want you to be happy."(hint="e18s05m03c02"):

            scene e18s05-40 mc-sb-talk7_c1 with dissolve
            play voice2 mc_no_nah2 noloop
            mc "Nah, but I want you to be happy. And if that dress would make you happy, you should at least try it on."
            scene e18s05-40 mc-sb-talk7_c2 with dissolve
            play voice3 girl35_arrogant_hm1 noloop
            sb "Can't argue with that."

    jump e18s05_dressing_room

label replay_e18s05:

    scene black with fade
    menu:
        "Do you want to dominate Samiya?"
        "Yes":
            $ e18_mc_cocky_points = 3
        "No":

            $ e18_mc_cocky_points = 0

label e18s05_dressing_room:

    if _in_replay:
        $ renpy.music.set_volume(0.0, 0.0, "music")
        $ renpy.music.set_volume(1.0, 0.0, "music2")
        $ renpy.music.play(audio.music_lofispers, "music" , True, None, True, 0.0)
        $ renpy.music.play(audio.music_lofispers_reverbed, "music2", True, None, True, 0.0)
    scene e18s05-41 mc-sb-walk_c1 with dissolve
    pause
    play sound sfx_locker_open1
    scene e18s05-41 mc-sb-walk_c2 with dissolve
    pause
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    scene e18s05-42 mc-sb-dress_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "What is taking her so long?"
    $ renpy.music.set_volume(1.0, 3.0, "music")
    scene e18s05-42 mc-sb-dress_c2 with dissolve
    queue music music_sexyfunkytime
    play voice3 girl35_hey_fun3 noloop
    sb "Hey [mcname]. Get in here, Dahlia is calling me but I've got my hands full."
    play sound sfx_door_locked1
    scene e18s05-43 mc-sb-inside_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "Samiya... I don't see your phone."
    scene e18s05-43 mc-sb-inside_c2 with dissolve
    play voice3 girl35_arrogant_pff4 noloop
    sb "Don't be so dull, [mcname]."
    scene e18s05-44 mc-sb-ask_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.5
    mc "What are you doing?"
    if e18_mc_cocky_points >= 2:
        scene e18s05-44 mc-sb-ask_c2 with dissolve
        play voice3 girl35_disappointed_geh5 noloop
        sb "Come on, dummy. Don't make me say it."
        scene e18s05-43 mc-sb-inside_c1 with dissolve
        play voice2 mc_thinking_hm noloop
        mct "Say what? What does she want me to make her say?"
        mct "She does look kind of horny. Wait. That's it."
        jump e18s05_cocky_menu
    else:
        play sound sfx_cloth_rustling4
        scene e18s05-49-4 mc-sb-talk3_c2 with dissolve
        play voice3 samiya_mmm2 noloop
        sb "Get closer. We don't want the manager to know exactly what we're doing."
        scene e18s05-49-4 mc-sb-talk3_c1 with dissolve
        play voice2 mc_angry_huh1 noloop
        mc "What are we doing?"
        play sound sfx_cloth_rustling1
        scene e18s05-49-5 mc-sb-talk4_c1 with dissolve
        play voice3 samiya_cagh noloop
        sb "Maybe Pete is sharper than you, [mcname]."
        scene e18s05-49-5 mc-sb-talk4_c2 with dissolve
        play voice3 girl35_disappointed_mmm1 noloop
        sb "You've been a great help to me on this... adventure."
        scene e18s05-49-6 mc-sb-talk5_c1 with dissolve
        play voice3 samiya_huh noloop
        sb "And now I want you to fuck my brains out. Without any other distractions."
        scene e18s05-49-6 mc-sb-talk5_c2 with dissolve
        play voice2 mc_thinking_oh1 noloop
        mc "I'm on the case."
        scene e18s05-49-7 mc-sb-talk6_c1 with dissolve
        play voice3 samiya_laughing1 noloop
        sb "Haha. See, no matter what, you're still a dork."
        scene e18s05-49-7 mc-sb-talk6_c2 with dissolve
        play voice2 mc_yes_yeah1 noloop
        mc "A dork with that big Dee you want!"
        scene e18s05-49-8 mc-sb-talk7_c2 with dissolve
        play voice3 girl35_surprised_ohmy2 noloop
        sb "Oh my god."
        jump e18s05_sb_sex

label e18s05_cocky_menu:

    play sound sfx_cloth_rustling4
    scene e18s05-45 mc-sb-beg_c2 with dissolve
    play voice2 mc_thinking_hmm6 noloop
    mct "Samiya wants me to fuck her. Nice."
    menu:
        "Make her say it."(hint="e18s05m04c01"):
            $ e18s05_mc_dom = True
            scene e18s05-45 mc-sb-beg_c1 with dissolve
            play voice2 mc_thinking_hmm2 noloop
            mc "Say it. I want you to say it."
            scene e18s05-45 mc-sb-beg_c2 with dissolve
            play voice3 samiya_kghhh noloop
            sb "You're so mean."
            sb "A big dumb meanie."
            scene e18s05-46 mc-sb-beg2_c1 with dissolve
            play voice2 mc_happy_hah2 noloop
            mc "And you want my big dumb cock, Samiya. Say it. Or no cock for you."
            play voice3 girl35_disappointed_mff1 noloop
            sb "..."
            mc "I know you want to, slut."
            play sound sfx_leg_kick8 volume 0.5
            scene e18s05-46 mc-sb-beg2_c2 with dissolve
            play voice3 samiya_yes3 noloop
            sb "I do. I really do."
            play sound sfx_cloth_rustling3
            scene e18s05-48 mc-sb-throat_c1 with dissolve
            play voice2 mc_arrogant_huh3 noloop
            mc "So say it."
            scene e18s05-48 mc-sb-throat_c2 with dissolve
            play voice3 samiya_mmm2 noloop
            sb "I want you to fuck me up with your big cock, [mcname]."
            sb "Make me scream. Do whatever you want."
            play sound sfx_cloth_rustling2
            scene e18s05-49 mc-sb-throat2_c1 with dissolve
            play voice2 mc_angry_errr6 noloop
            mc "Perfect."
        "I don't understand."(hint="e18s05m04c02"):

            scene e18s05-49-4 mc-sb-talk3_c1 with dissolve
            play voice2 mc_angry_huh1 noloop
            mc "And what exactly am I 'making' you say?"
            scene e18s05-49-4 mc-sb-talk3_c2 with dissolve
            play voice3 samiya_cagh noloop
            sb "Come on..."
            mc "..."
            play sound sfx_cloth_rustling2
            scene e18s05-49-5 mc-sb-talk4_c1 with dissolve
            play voice3 samiya_huh3 noloop
            sb "Seriously?"
            scene e18s05-49-5 mc-sb-talk4_c2 with dissolve
            play voice2 mc_disappointed_off1 noloop
            mc "I seriously don't know what you want."
            scene e18s05-49-6 mc-sb-talk5_c1 with dissolve
            play voice3 samiya_grrr noloop volume 1.4
            sb "*sighs* Fine. I want you to fuck me. Got it?"
            scene e18s05-49-6 mc-sb-talk5_c2 with dissolve
            play voice2 mc_thinking_mmm3 noloop volume 1.6
            mc "Who are you, and where did you put Samiya?"
            scene e18s05-49-7 mc-sb-talk6_c1 with dissolve
            play voice3 samiya_hm3 noloop volume 1.4
            sb "It's still me, or at least the 'me' after you fucked my brains out the first time."
            sb "So, are you staying or not?"
            scene e18s05-49-8 mc-sb-talk7_c1 with dissolve
            play voice2 mc_yes_yes4 noloop
            mc "Of course."

    jump e18s05_sb_sex

label e18s05_sb_sex:


    $ Lovense.stop()

    play sound sfx_skirt_off3
    scene e18s05-49-9 mc-sb-undress_c2 with dissolve
    $ Lovense.vibrate(1)
    pause
    play sound sfx_jeans_on1
    scene e18s05-50 mc-sb-room1_c1 with dissolve
    pause
    play sound sfx_skirt_off1
    scene e18s05-50 mc-sb-room1_c2 with dissolve
    pause
    if e18s05_mc_dom is True:
        scene e18s05-51 mc-sb-order_c1 with dissolve
        play voice2 mc_thinking_hmm1 noloop
        mc "Get down on your knees."
        scene e18s05-51 mc-sb-order_c2 with dissolve
        play voice3 girl35_yes_simple2 noloop
        sb "Yes, [mcname]."
    play sound sfx_cloth_rustling2
    scene e18s05-52 mc-sb-knee_c1 with dissolve
    pause
    play sound sfx_hair_scratch1
    scene e18s05-53 mc-sb-knee2_c2 with dissolve
    play voice2 d9s2_ugu noloop volume 1.8
    mc "Open wide."
    scene e18s05-53 mc-sb-knee2_c1 with dissolve
    play voice3 girl35_happy_mmm1 noloop
    if e18s05_mc_dom is True:
        sb "Give it to me. I want every inch shoved down my throat."
    else:
        sb "Enjoy my throat. Dahlia would never let you do this."
        scene e18s05-54 mc-sb-animation_c2 with dissolve
        play voice2 mc_yes_yes1 noloop
        mc "Yes, but let's forget about her for a bit."
    $ Lovense.vibrate(6)
    play sound sfx_spitcum1
    scene e18s05-a54-1 mc-sb-anim-01 with dissolve
    play voice3 samiya_mfff noloop
    sb "Mrrrmaah..."
    play sound mc_sex_sucking_fast2 loop volume 0.6
    $ Lovense.pattern("7;12", 1400)
    scene e18s05-a54-1
    play voice2 mc_sex_openmoans1
    play voice3 samiya_moans6
    mct "Man, she's really sucking me in there. I don't think I've ever felt her body like this."
    sb "Lrrrmphaa..."
    sb "Mrrrah-hurr-phrfff."
    scene e18s05-a54-2 with dissolve

    if e18s05_mc_dom is True:
        mc "That's it, Samiya. You're my good cock-sucking slut today."
        mc "Right?"
        sb "Mrrrhmm!"
    else:
        mct "Oh fuck. Her tongue is going everywhere."
    pause
    scene e18s05-a54-3 with dissolve

    sb "*muffled moaning*"
    mc "Let's got a little deeper."
    pause
    $ Lovense.pattern("7;12", 700)
    scene e18s05-a54-1-f with dissolve
    sb "Mrrrf-pahua-blrfff."
    pause
    scene e18s05-a54-2-f with dissolve
    pause
    scene e18s05-a54-3-f with dissolve
    pause

    stop voice2 fadeout 1.0
    play sound sfx_hair_scratch1
    $ Lovense.stop()
    $ Lovense.vibrate(4)
    scene e18s05-55 mc-sb-stand_c1 with dissolve
    play voice3 polly_breathing noloop
    pause
    if e18s05_mc_dom is True:
        scene e18s05-55 mc-sb-stand_c2 with dissolve
        play voice2 mc_thinking_mmm6 noloop
        mc "Good girl. But we're just getting started."
        play sound sfx_cloth_rustling5
        scene e18s05-56 mc-sb-spank_c1 with dissolve
        play voice2 mc_arrogant_tsktsk noloop
        mc "I still think you're holding back."
        play voice2 mc_angry_errr8 noloop
        play voice3 samiya_pain2 noloop
        play sound sfx_whip_slap1
        $ Lovense.vibrate(8)
        scene e18s05-57 mc-sb-spank2_c2 with hpunch
        sb "Nrrrhhhh... Oouhaah..."
        scene e18s05-58 mc-sb-look_c1 with dissolve
        $ Lovense.vibrate(3)
        play voice2 mc_angry_oof noloop
        mc "Look at you, getting off on being spanked."
        mc "My perfect sex addict toy."
        scene e18s05-58 mc-sb-look_c2 with dissolve
        play voice3 girl35_yes_confident1 noloop
        sb "Yes, [mcname]."
    else:
        play sound sfx_cloth_rustling5
        scene e18s05-56 mc-sb-spank_c1 with dissolve
        play voice3 girl35_disappointed_mmm4 noloop
        sb "I want you to spank me."
        scene e18s05-56 mc-sb-spank_c2 with dissolve
        play voice2 mc_thinking_wait1 noloop
        mc "Wait, what about trying to keep the volume down?"
        scene e18s05-57 mc-sb-spank2_c1 with dissolve
        play voice3 samiya_hah1 noloop
        sb "Spank me or I'll run screaming from this room."
        sb "You can take your chances."
        play voice2 mc_angry_errr8 noloop
        play voice3 samiya_pain2 noloop
        play sound sfx_whip_slap1
        $ Lovense.vibrate(8)
        scene e18s05-57 mc-sb-spank2_c2 with hpunch
        mc "You always have to be such a bitch, don't you."
        scene e18s05-58 mc-sb-look_c2 with dissolve
        $ Lovense.vibrate(3)
        play voice3 girl35_yes_angry2 noloop
        sb "Yes. Now... fuck me while you spank me."
        scene e18s05-58 mc-sb-look_c1 with dissolve
        play voice2 mc_angry_errr2 noloop
        mc "Fucking bitch."
    scene e18s05-a59-1 mc-sb-anim-01 with dissolve
    $ Lovense.pattern("7;12", 1400)
    scene e18s05-a59-1
    play voice2 mc_sex_openmoans2
    play voice3 samiya_moans1
    play sound sfx_vagina_penetration1_fast loop volume 0.6
    sb "Right there. Nrraaah."
    pause
    scene e18s05-a59-2 with dissolve
    if e18s05_mc_dom is True:
        sb "Yes. Fuck me, daddy. Have all the fun you want with your little slut."
    else:
        sb "At least I know you won't just stick it in and cum like Pete."

    sb "Oh fuck. You really like being nasty with me."
    pause
    scene e18s05-a59-3 with dissolve
    sb "Ouhaah... that's it... keep spanking me, [mcname]."
    if e18s05_mc_dom is True:
        sb "It feels so gooduaha-huraah..."
    else:
        sb "Shit like this is all your good for."
        mc "There are worse jobs out there."
        sb "Hah."
    pause
    scene e18s05-a59-4 with dissolve


    sb "Oouhaah. Right there. Ohua-fuck! I'm going to have to keep my ass hidden for days."
    sb "Yes... Oh fuck. Fuck! Fuuhaak-huah me!"
    pause
    $ Lovense.pattern("7;12", 700)
    scene e18s05-a59-1-f with dissolve
    pause
    scene e18s05-a59-2-f with dissolve

    mc "We should have fucked in a dressing room a long time ago."
    pause
    scene e18s05-a59-3-f with dissolve
    sb "*panting heavily* Just. Keep. Fucking. Me."
    pause
    scene e18s05-a59-4-f with dissolve
    pause

    stop voice2 fadeout 1.0
    play sound sfx_cloth_rustling2
    $ Lovense.stop()
    $ Lovense.vibrate(3)
    scene e18s05-60 mc-sb-pick_c2 with dissolve
    play voice3 samiya_mmm2 noloop
    sb "Now... fuaha... now what are you doing."
    scene e18s05-60 mc-sb-pick_c1 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "Just trust me. You're going to love it."
    scene e18s05-61 mc-sb-chest_c2 with dissolve
    play voice3 girl35_disappointed_mff2 noloop
    sb "Okay. I'm... phew... I'm too tired to resist anyhow."
    play sound sfx_fisting_fist1
    $ Lovense.vibrate(6)
    scene e18s05-62 mc-sb-back_c1 with dissolve
    play voice3 samiya_orgasm4 noloop
    play voice2 mc_angry_errr4 noloop
    pause
    scene e18s05-62 mc-sb-back_c2 with dissolve
    pause
    scene e18s05-a64-1 mc-sb-anim-01 with dissolve
    scene e18s05-a64-1
    $ Lovense.pattern("7;12", 1400)
    play voice2 mc_sex_openmoans2
    play voice3 samiya_moans1
    play sound sfx_vagina_penetration1_fast loop volume 0.6
    sb "Shituaah... Could have warned me a little."
    pause
    scene e18s05-a64-2 with dissolve
    if e18s05_mc_dom is True:
        mc "You're all mine, remember?"
        sb "Yeah... still, this fucking big cock keeps fucking up my thoughts."
        mc "Just relax, Samiya. I got you..."
        sb "Mrmm.... I... I know, [mcname]."
    else:
        mc "Sorry, Samiya."
        mc "Forget my own cock-strength sometimes."
        sb "It's fine. Now... get that motor running again. I don't have all day."
    pause
    scene e18s05-a64-3 with dissolve
    play voice3 samiya_moans3
    mc "Alright, time to heat things up."
    sb "Yes. Keep going. Hammer my poor little pussy."
    sb "P-pound... pound me..."
    pause
    scene e18s05-a64-4 with dissolve
    sb "Make it cream all over your cock."
    mct "Fuck. She's getting so nasty. I love it."
    mct "But she's going to make me cum soon with all this dirty talk, and the way her pussy's squeezing me."
    pause
    $ Lovense.pattern("7;14", 700)
    scene e18s05-a64-1-f with dissolve
    sb "[mcname]. Nraah... Your cock is getting so big."
    sb "Heh. I guess it can't be helped. I'm the best pussy you've ever had."
    pause
    scene e18s05-a64-2-f with dissolve

    mc "Hah. Maybe. Even if that's true, we'll keep it between us."
    sb "Smart. Fuahak... Nrrrnnn. If you say that around Dahlia, she might attack us both."

    pause
    scene e18s05-a64-3-f with dissolve
    mc "Haha. Wouldn't want that."
    sb "No... sir... muruah-huaah. I'm getting so close!"
    pause
    scene e18s05-a64-4-f with dissolve


    pause
    sb "Inside... cum inside me, [mcname]."
    play voice2 mc_sex_orgasm4 noloop
    play voice3 samiya_orgasm2 noloop
    play sound mc_cum_sound1
    $ Lovense.stop()
    $ Lovense.vibrate(18)
    scene e18s05-65 mc-sb-cum_c3 with vpunch
    mc "*groaning*"
    sb "Oh my goduhaa-huaaa-ffuuaah."
    play sound mc_cum_sound1
    scene e18s05-66 mc-sb-cum2_c2 with dissolve
    $ Lovense.vibrate(3)
    pause
    scene e18s05-65 mc-sb-cum_c2 with dissolve
    play voice3 polly_breathing noloop
    sb "Fuhuaah... You absolutely wrecked my pussy. That cock of yours can be a real monster."
    play voice2 mc_thinking_mmm4 noloop
    mc "Mmm. Quit complaining."
    if e18s05_mc_dom is True:
        scene e18s05-67 mc-sb-stand_c1 with dissolve
        play voice2 mc_angry_hm1 noloop
        mc "You were the one who begged to get fucked."
        scene e18s05-67 mc-sb-stand_c2 with dissolve
        play voice3 girl35_arrogant_hehe noloop
        sb "Pretty sure you were imagining things."
    play sound sfx_sex_fingering_slow1 volume 0.6
    $ Lovense.vibrate(8)
    scene e18s05-68 mc-sb-cum_c2 with dissolve
    play voice3 samiya_moans1 noloop
    sb "Oohuaah. What... oouahh-ahh..."
    play sound sfx_spitcum1
    scene e18s05-69 mc-sb-cum2_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    play voice3 samiya_mfff noloop
    $ Lovense.vibrate(10)
    mc "A little snack."
    scene e18s05-69 mc-sb-cum2_c2 with dissolve
    play voice3 samiya_mfff2 noloop
    sb "Mrrmmm."
    play sound sfx_locker_open1
    scene e18s05-70 mc-sb-outside_c2 with fade

    $ Lovense.stop()


    play voice3 samiya_geh noloop
    sb "Shame I have to say goodbye to the dress for now."
    sb "Probably for the best, though."
    play sound sfx_heels_steps1 loop
    scene e18s05-71 mc-sb-walk_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "You go get the car ready. I need to use the restroom."
    scene e18s05-71 mc-sb-walk_c2 with dissolve
    play voice3 samiya_hm2 noloop
    sb "Okay."
    stop sound fadeout 1.5
    if _in_replay:
        stop music fadeout 3.0
    $ renpy.end_replay()

    jump e18s06_end

label e18s06_end:

    $ renpy.music.set_volume(0.6, 3.0, "music")
    play sound3 sfx_car_inside_ride1 fadein 1.0
    play sound4 sfx_supercar_drive1 volume 0.05
    scene e18s05-72 mc-sb-car_c2 with Fade(0.5, 0.5, 0.5)
    pause
    scene e18s05-72 mc-sb-car_c2-2 with dissolve
    play voice3 girl35_thinking_hm noloop
    sb "What is that bag for?"
    scene e18s05-73 mc-sb-car2_c1 with dissolve
    $ unlock_gallery_slot("scene", "e18s05")
    play voice3 samiya_huh5 noloop
    sb "Did you grab something?"
    mc "..."
    scene e18s05-73 mc-sb-car2_c2 with dissolve
    play voice3 samiya_huh4 noloop
    sb "[mcname]?"
    scene e18s05-74 mc-sb-talk_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "You liked the dress so much. I decided to get it."
    scene e18s05-74 mc-sb-talk_c2 with dissolve
    play voice3 girl35_surprised_what5 noloop
    sb "Where did you get the money?"
    scene e18s05-75 mc-sb-talk2_c1 with dissolve
    play voice2 mc_happy_laugh2 noloop
    mc "It was on five-finger discount."
    scene e18s05-75 mc-sb-talk2_c2 with dissolve
    play voice3 girl35_scared_huh4 noloop
    sb "Don't be cute. Oh my god. We're here, probably driving a stolen car, and then you go and steal a dress to make me-"
    sb "Fuck."
    scene e18s05-76 mc-sb-angry_c2 with dissolve
    play voice3 samiya_youu noloop
    sb "You didn't even have the brains to hide it in the trunk?!"
    scene e18s05-77 mc-sb-talk_c1 with dissolve
    play voice2 mc_yes_yeah9 noloop
    mc "Yeah, the trunk is still busted."
    scene e18s05-78 mc-sb-point_c2 with dissolve
    play voice3 girl35_angry_ergh1 noloop
    sb "I'm going to bust you if I end up in a Santa Domina jail!"
    sb "First thing you do when we get home is fix the trunk."
    play sound sfx_car_skid1 volume 0.6
    stop sound3 fadeout 1.0
    stop sound4 fadeout 1.0
    scene e18s05-79 mc-sb-talk_c1 with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Shouldn't we go back and uh 'return' the dress?"
    scene e18s05-79 mc-sb-talk_c2 with dissolve
    play voice3 girl35_angry_hm1 noloop
    sb "Who said anything about returning my dress?"
    $ renpy.music.set_volume(1.0, 3.0, "music")
    play sound sfx_car_door_closed1
    play sound2 sfx_heels_steps1
    scene e18s05-80 mc-sb-walk_c2 with dissolve
    pause
    stop sound2 fadeout 1.0
    play sound sfx_pliers_loop1 volume 0.6
    scene e18s05-80 mc-sb-trunk_c1 with dissolve
    play voice2 mc_angry_errr7 noloop
    pause
    play sound sfx_car_trunk_squeak5
    play sound2 sfx_kick_metal1 noloop volume 0.4
    scene e18s05-80 mc-sb-trunk_c2 with dissolve
    play voice2 mc_pain_argh1 noloop
    mc "Come on you piece of junk."
    scene e18s05-80 mc-sb-walk_c1 with dissolve
    play voice2 mc_disappointed_meh1 noloop
    mc "Screw this. I'll fix it tomorrow."
    play sound sfx_heels_steps2 loop
    scene e18s05-81 mc-sb-walk_c1 with dissolve
    pause
    stop sound fadeout 1.0

    stop music fadeout 3.0
    jump e18s06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
