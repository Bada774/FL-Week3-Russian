label d16s05:

    $ d16s05_kiss_sy = False

    if date_sy is False:
        jump d16s06

    scene black
    show screen scene_transistion(_("After the class"))
    with Fade(0.9, 0.5, 0.5)
    pause
    play sound ["<silence 0.6>", sfx_door_open1]
    hide screen scene_transistion
    scene d16s05-01 mc-sy-entry1_c1
    with Fade(0.5, 0.5, 0.9)
    $ renpy.music.set_volume(0.6, 0.0, "music")
    play music stacy_time
    mct "Wonder what the thin—"
    scene d16s05-01 mc-sy-entry1_c2 with dissolve
    pause
    play sound sfx_door_closed1
    scene d16s05-01 mc-sy-entry1_c3 with dissolve
    play voice2 mc_scared_huh1 noloop
    mc "Shit, sorry."
    scene d16s05-02 mc-sy-entry2_c1 with dissolve
    play voice3 stacy_angry noloop
    sy "Oh please, like you haven't seen me naked before."
    scene d16s05-02 mc-sy-entry2_c2 with dissolve
    sy "Not to mention, if you really cared about privacy, you'd have knocked."
    scene d16s05-02 mc-sy-entry2_c3 with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "I did!"
    play voice3 ["<silence 0.1>", min_angry_argh1] noloop
    play sound sfx_throw_something1 volume 1.6
    scene d16s05-03 mc-sy-throw_c1 with dissolve
    pause
    scene d16s05-03 mc-sy-throw_c3 with dissolve
    pause
    scene d16s05-03 mc-sy-throw_c2 with dissolve
    pause
    play sound sfx_cloth_rustling2
    scene d16s05-03-2 mc-arj-room-talk3-2_c2 with dissolve
    play voice3 polly_angry noloop
    sy "And then came in right away!"
    scene d16s05-04 mc-sy-talk_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    if persistent.is_special is True:
        mc "I'm respecting your privacy by knocking but asserting my authority as your brother by coming in anyway."
    else:
        mc "I'm respecting your privacy by knocking but asserting my authority as your friend by coming in anyway."
    scene d16s05-04 mc-sy-talk_c2 with dissolve
    play voice3 stacy_angryhuh noloop
    sy "Knucklehead!"
    scene d16s05-04 mc-sy-talk_c3 with dissolve
    pause

    play sound sfx_bed_slide3 volume 0.3
    scene d16s05-05 mc-sy-talk2_c2 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "What are you dressing up for anyway?"
    scene d16s05-05 mc-sy-talk2_c1 with dissolve
    play voice3 stacy_hmm noloop
    sy "Job interview."
    scene d16s05-05 mc-sy-talk2_c2 with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "...Huh?"
    scene d16s05-05 mc-sy-talk2_c1 with dissolve
    play voice3 stacy_oh2 noloop
    sy "Oh, right. You see, a job is what you do to gain mon—"
    scene d16s05-05 mc-sy-talk2_c2 with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "I know what a job is, you sarcastic ass."
    mc "I'm just surprised."
    scene d16s05-06 mc-sy-talk3_c1 with dissolve
    play voice3 stacy_mmm2 noloop
    sy "About what?"
    mc "About you getting a job."
    scene d16s05-07 mc-sy-talk4_c1 with dissolve
    sy "Why is that surprising?"
    mc "...I dunno."
    mc "Feels like you're all grown up I guess."
    scene d16s05-07-2 mc-sy-talk5_c1 with dissolve
    play voice3 stacy_hey noloop
    sy "I {i}am{/i} all grown up."
    play voice2 mc_no_nah2 noloop
    mc "You're practically a fetus. Shut the fuck up."
    scene d16s05-06 mc-sy-talk3_c1 with dissolve
    play voice3 polly_impressed noloop
    sy "I'm gonna need to find a job sooner or later."
    scene d16s05-07 mc-sy-talk4_c1 with dissolve
    sy "Can't live that hot-girl life while broke."
    play voice2 d4s4_mclaugh noloop
    mc "*Chuckles* Right, right."
    scene d16s05-07-2 mc-sy-talk5_c1 with dissolve
    play voice3 stacy_mmm1 noloop
    sy "How do I look?"
    play voice2 mc_thinking_hmm2 noloop
    mc "Professional as fuck. Sleek and clean with a side of boss bitch."
    scene d16s05-07-3 mc-sy-talk6_c1 with dissolve
    play voice3 amrose_happy_yeah3 noloop
    sy "Fuck yeah, that's what I'm talking about."
    scene d16s05-07-3 mc-sy-talk6_c2 with dissolve
    play voice3 stacy_moan7 noloop
    sy "Ugh, I gotta piss. Knew I shouldn't have drunk that second cup of coffee."
    scene d16s05-08-1 mc-sy-toilet1_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "I'm seriously getting concerned about your caffeine intake."
    scene d16s05-08-1 mc-sy-toilet1_c2 with dissolve
    play voice3 stacy_yeahno noloop
    sy "It's that or cocaine, pick your poison."
    play sound sfx_door_open4 volume 4.0
    scene d16s05-08-2 mc-sy-toilet2_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Fair enough.{w} So what's this gig anyway?"
    play sound piss volume 0.4 fadein 2.6 loop
    scene d16s05-08-2 mc-sy-toilet2_c2 with dissolve
    play voice3 stacy_mmm1 noloop
    sy "Not sure, they weren't specific."
    sy "But I found a flyer saying that the CPD was looking for people with \"computer knowledge.\" Whatever that might mean."
    sy "Here's hoping it's a dev job or something."
    stop sound fadeout 1.0
    play sound3 sfx_toilet_flush1 noloop
    scene d16s05-09 mc-sy-out1_c1 with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "You're gonna work for the cops?"
    play voice3 polly_hey noloop
    sy "Hey, I'm not saying no to that government money."
    mc "Do you even know how much they're paying?"
    scene d16s05-09 mc-sy-out1_c2 with dissolve
    play voice3 polly_nouh noloop
    sy "Nope. But I'm sure I can sweet talk myself into a couple hundred grand."
    play voice2 mc_yes_yeah5 noloop
    mc "Right..."
    scene d16s05-10 mc-sy-out2_c1 with dissolve
    play voice3 stacy_angryhuh noloop
    sy "Alright. Uh... I think that's everything."
    scene d16s05-10 mc-sy-out2_c2 with dissolve
    sy "I'm ready to go."
    stop music fadeout 4.0

    $ renpy.music.set_volume(0.6, 0.0, "sound2")
    play sound2 subwaycar fadein 2.0
    scene d16s05-11 mc-sy-subway1_c2 with fade
    play voice3 stacy_impressed noloop
    sy "They literally had the audacity to just go \"{i}Somehow{/i} Palpatine returned.\" {b}Somehow!?{/b}, {i}{b}Somehow!?{/b}{/i}?"
    scene d16s05-11 mc-sy-subway1_c1 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Alright, well I admit that line was rough."
    scene d16s05-12 mc-sy-subway2_c1 with dissolve
    mc "But I dunno man, I still kinda liked it."
    scene d16s05-12 mc-sy-subway2_c2 with dissolve
    play voice3 polly_angry noloop
    sy "Well, your taste is trash and you should feel bad."
    sy "Ass."
    scene d16s05-13 mc-sy-subway3_c2 with dissolve
    play voice3 stacy_oh noloop
    sy "Oh! How's the uh...{i}situation{/i} by the way?"
    scene d16s05-13 mc-sy-subway3_c1 with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What—?"
    mc "Oh."

    if cockcage_released is True:
        scene d16s05-15 mc-sy-subway5_c1 with dissolve
        play voice2 mc_thinking_hmm1 noloop
        mc "I got out."
        scene d16s05-15 mc-sy-subway5_c2 with dissolve
        play voice3 stacy_yay noloop
        sy "What? That's great! How?"
        scene d16s05-16 mc-sy-subway6_c1 with dissolve
        play voice2 mc_thinking_oh1 noloop
        mc "Uh... It's a whole thing, to be honest."
        mc "Short version of it is that you get a special token if you do wild, fetishy shit which you can then use to skip/shorten certain challenges."
        scene d16s05-15 mc-sy-subway5_c1 with dissolve
        mc "I had enough of those tokens, so I got out."
        scene d16s05-16 mc-sy-subway6_c2 with dissolve
        play voice3 stacy_laugh4 noloop
        sy "Huh, well, that's great! You finally got your dick back."
        sy "Maybe we can put it to use later tonight."
    else:
        scene d16s05-15 mc-sy-subway5_c1 with dissolve
        play voice2 mc_disappointed_ehh3 noloop
        mc "Same ol', same ol'."
        scene d16s05-15 mc-sy-subway5_c2 with dissolve
        play voice3 stacy_upset1 noloop
        sy "Damn..."
        sy "Well... Maybe we try and see what we can do about that later tonight."

    scene d16s05-17 mc-sy-subway7_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "Stacy, stop. Not here."
    scene d16s05-17 mc-sy-subway7_c2 with dissolve
    play voice3 stacy_huh2 noloop
    sy "Why not?"
    scene d16s05-18 mc-sy-subway8_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "It's just..."
    mc "I know that we are...{i}more{/i} than we were before now."
    scene d16s05-17 mc-sy-subway7_c1 with dissolve
    mc "And it's exciting."
    mc "But at the same time, we need to take this one step at a time."

    if persistent.is_special is True:
        scene d16s05-17 mc-sy-subway7_c2 with dissolve
        play voice2 mc_thinking_mmm3 noloop
        mc "Society doesn't exactly take kindly to...what we're doing."
        mc "If someone finds out about us..."
        scene d16s05-18 mc-sy-subway8_c2 with dissolve
        play voice3 stacy_hey noloop
        sy "Who cares? Fuck 'em."
        sy "I care about you, and to the best of my knowledge, you care about me."
        scene d16s05-17 mc-sy-subway7_c2 with dissolve
        sy "That's all that matters."
        sy "People that can't keep to their fucking lane can go fuck themselves."
        play voice2 d3s11b_mcheh volume 2.0 noloop
        scene d16s05-16 mc-sy-subway6_c1 with dissolve
        mc "*Chuckles* I agree, but still."
    else:
        scene d16s05-18 mc-sy-subway8_c2 with dissolve
        play voice3 stacy_hey noloop
        sy "Why? Why can't we just jump in?"
        play voice2 mc_thinking_mmm3 noloop
        mc "Stacy, I care about you. I don't want to hurt you."
        scene d16s05-16 mc-sy-subway6_c1 with dissolve
        mc "I don't know what might happen, I just want us to be careful."
    scene d16s05-16 mc-sy-subway6_c2 with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    sy "*Sigh* I...get what you're trying to do."
    sy "Don't like it though. But I get it."

    menu:
        "Kiss her"(hint="d16s05m01c01"):

            $ d16s05_kiss_sy = True

            scene d16s05-18-2 mc-sy-subway9_c2 with dissolve
            sy "Hypocrite."
            scene d16s05-18-2 mc-sy-subway9_c1 with dissolve
            play voice2 mc_yes_yeah1 noloop
            mc "Rules for thee, but not for me."
            play sound maria_kiss1
            play voice3 stacy_suckmoan3 noloop
            scene d16s05-19-2 mc-sy-subway-kiss2_c1 with dissolve
            pause
            play sound maria_kiss2
            play voice3 stacy_suckmoan2 noloop
            play voice2 d1s1_mmm noloop
            scene d16s05-19-2 mc-sy-subway-kiss2_c3 with dissolve
            pause
            scene d16s05-18-2 mc-sy-subway9_c3 with dissolve
            play voice2 mc_arrogant_heh3 noloop
            mc "I'm kidding. Thank you. I'm happy you understand."
        "Don't"(hint="d16s05m01c02"):

            pass

    if is_extended_edition is True:
        play sound "<from 8.0>audio/freesound/extended/250516_389377-lq.ogg" fadein 1.0 noloop
    stop sound2 fadeout 2.5
    scene d16s05-19-3 mc-sy-subway-exit_c2 with fade
    play voice2 mc_yes_okay2 noloop
    mc "Looks like we're here."
    scene d16s05-19-3 mc-sy-subway-exit_c1 with dissolve
    play voice3 stacy_oh2 noloop
    sy "Oh boy."
    stop sound fadeout 3.0

    $ renpy.music.set_volume(0.2, 0.0, "sound3")
    play sound3 classroom fadein 3.0
    scene d16s05-21 mc-sy-station2_c2 with fade
    $ renpy.music.set_volume(0.1, 5.0, "sound3")
    play voice3 min_arrogant_pff noloop
    sy "Ugh, how much longer is this going to take?"
    scene d16s05-21 mc-sy-station2_c1 with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Our famous speedy government at work, ladies and gentlemen."
    scene d16s05-20 mc-sy-station1_c2 with dissolve
    sy "I feel like I'm aging years every second."
    scene d16s05-20 mc-sy-station1_c1 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Oh calm down, you drama queen. It's literally only been like 15 minutes."
    scene d16s05-22 mc-sy-station-talk1_c2 with dissolve
    play voice2 stacy_angry noloop
    sy "That's 15 minutes too much!"
    scene d16s05-23 mc-sy-station-talk2_c2 with dissolve
    sy "You know how much you could do in 15 minutes!?"
    scene d16s05-24 mc-sy-station-talk3_c2 with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    play music lofi4 fadein 1.5
    pause
    scene d16s05-24 mc-sy-station-talk3_c1 with dissolve
    play voice3 stacy_huh2 noloop
    pause
    play sound [sfx_vending_button, sfx_vending_cola]
    scene d16s05-25 mc-sy-station-vending_c2 with dissolve
    pause
    play sound sfx_vending_door1 volume 0.5
    scene d16s05-26 mc-sy-station-drink1_c2 with dissolve
    play voice2 d2s9_mchey noloop
    mc "Here, drink this. Apparently, it's harder to get anxious when you have something in your mouth."
    scene d16s05-26 mc-sy-station-drink1_c1 with dissolve
    play voice3 stacy_huh noloop
    sy "Is that an innuendo?"
    scene d16s05-27 mc-sy-station-drink2_c2 with dissolve
    play voice2 mc_yes_yeah6 noloop
    mc "Only if you make it one. Now drink up."
    scene d16s05-27 mc-sy-station-drink2_c1 with dissolve
    play voice3 polly_laughter noloop
    sy "Thank you."

    scene d16s05-28 mc-sy-station-drink3_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Why'd you apply to this anyway?"
    scene d16s05-28 mc-sy-station-drink3_c2 with dissolve
    play voice3 stacy_hmm noloop
    sy "What do you mean?"
    play sound [sfx_drink_slurp2, gulp] volume 0.5
    scene d16s05-29 mc-sy-station-drink4_c1 with dissolve
    play voice2 d2s9_confused noloop
    mc "I'm sure there must be plenty of other tech jobs, right? Even internships."
    mc "So why CPD?"
    play sound sfx_drink_loop1 loop
    scene d16s05-30 mc-sy-station-drink5_c2 with dissolve
    play voice3 stacy_upset1 noloop
    sy "I dunno. It's hard to explain."
    sy "It's like... I like tech, but I kinda hate the culture."
    scene d16s05-30 mc-sy-station-drink5_c1 with dissolve
    sy "So I wanted something that was related to tech, but far away from that whole bubble."
    sy "And then it's like I said. Saw the flyer, thought it might be something, and now here we are. Still waiting..."
    stop sound fadeout 1.0
    scene d16s05-28 mc-sy-station-drink3_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "*Chuckles* Well, is this what you want to do in the future as well?"
    scene d16s05-28 mc-sy-station-drink3_c2 with dissolve
    play voice3 stacy_no2 noloop
    sy "Fuck no! I'm going to start my own company. Make my own damn destiny instead of living under someone else's for 50 years and then dying."
    play voice2 mc_thinking_hmm3 noloop
    mc "So this is just a stepping stone then?"
    play sound sfx_drink_slurp2 volume 0.5
    scene d16s05-30 mc-sy-station-drink5_c1 with dissolve
    play voice3 polly_aga noloop
    sy "Pretty much."
    play sound sfx_drink_slurp1 volume 0.5
    scene d16s05-29 mc-sy-station-drink4_c2 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Hm. Good to know."
    $ renpy.music.set_volume(1.0, 1.0, "music")
    $ renpy.music.set_volume(0.4, 1.0, "sound3")
    scene d16s05-34 mc-sy-station-timelapse4_c1 with dissolve
    pause
    scene d16s05-31 mc-sy-station-timelapse1_c1 with dissolve
    pause
    scene d16s05-32 mc-sy-station-timelapse2_c1 with dissolve
    pause
    scene d16s05-33 mc-sy-station-timelapse3_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.2, 1.0, "sound3")
    $ renpy.music.set_volume(0.6, 1.5, "music")

    if persistent.is_special is True:
        scene d16s05-35 mc-sy-station-talk1_c1 with dissolve
        play voice2 mc_arrogant_hm2 noloop
        mc "I wonder if our...situation is going to be a problem."
        scene d16s05-35 mc-sy-station-talk1_c2 with dissolve
        play voice3 polly_impressed noloop
        sy "How would it be a problem?"
        scene d16s05-36 mc-sy-station-talk2_c1 with dissolve
        play voice2 mc_thinking_mmm4 noloop
        mc "Well, it's a federal job. They do background checks and all that shit."
        scene d16s05-36 mc-sy-station-talk2_c2 with dissolve
        play voice3 stacy_hmm noloop
        sy "Yeah, but it's not like we blast everything for everyone to see."
        sy "Literally like...only three people in the whole world know about us. Two of them being us.{w} I'm sure it'll be fine."
        scene d16s05-37 mc-sy-station-talk3_c1 with dissolve
        play voice2 mc_arrogant_heh2 noloop
        mc "Hm."

    if date_mh is True:
        scene d16s05-37 mc-sy-station-talk3_c2 with dissolve
        play voice3 stacy_oh2 noloop
        sy "Oh! How's Lyssa by the way?"
        scene d16s05-37 mc-sy-station-talk3_c1 with dissolve
        play voice2 mc_arrogant_huh3 noloop
        mc "Lyssa? Why are you asking about her all of a sudden?"
        scene d16s05-38 mc-sy-station-talk4_c2 with dissolve
        play voice3 stacy_laugh4 noloop
        sy "You two went on that date, right? The one I crashed."
        sy "How was it before that though? Are you two getting serious now? What's going on? Give me the deets."
        scene d16s05-38 mc-sy-station-talk4_c1 with dissolve
        play voice2 mc_disappointed_off2 noloop
        mc "Uh... Well, I guess? We're getting closer. And I want to continue seeing her."
        scene d16s05-39 mc-sy-station-talk5_c2 with dissolve
        play voice3 stacy_nono noloop
        sy "...That's like the driest answer ever."
        scene d16s05-39 mc-sy-station-talk5_c1 with dissolve
        play voice2 mc_thinking_oh1 noloop
        mc "Well what do you want from me!?"
        scene d16s05-35 mc-sy-station-talk1_c2 with dissolve
        play voice3 polly_hey noloop
        sy "I wanna know the spicy deets!"
        scene d16s05-35 mc-sy-station-talk1_c1 with dissolve
        play voice2 mc_no_uhuh1 noloop
        mc "Uh-uh, nope."
        scene d16s05-36 mc-sy-station-talk2_c2 with dissolve
        play voice3 stacy_suckmoan1 noloop
        sy "Come on! Please?"
        scene d16s05-36 mc-sy-station-talk2_c1 with dissolve
        play voice2 mc_thinking_mmm4 noloop
        mc "Why are you so interested in her anyway?"
        scene d16s05-37 mc-sy-station-talk3_c2 with dissolve
        play voice3 stacy_impressed noloop
        sy "Who wouldn't be interested in her? Have you {i}seen{/i} her?"
        sy "Plus, her caring dom vibes are immaculate."
        scene d16s05-37 mc-sy-station-talk3_c2 with dissolve
        if date_mh_bdsm is True:
            mct "*Chuckles* Dom, huh?"
        play voice2 mc_disappointed_ehh1 noloop
        mc "All I'll say is this, everything's going well."
        mc "Any spicy deets that may or may not exist will solely be known between her and me, and that's it."
        scene d16s05-38 mc-sy-station-talk4_c2 with dissolve
        play voice3 stacy_upset1 noloop
        sy "Aw. That's no—"

    scene d16s05-40 mc-sy-pm-station-talk1_c1 with dissolve
    play voice4 girl8_thinking_hmm2 noloop
    if persistent.is_special is True:
        "Woman" "Stacy Young? Do we have a Stacy Young in here?"
    else:
        "Woman" "Stacy Brawn? Do we have a Stacy Brawn in here?"
    scene d16s05-40 mc-sy-pm-station-talk1_c2 with dissolve
    play voice3 stacy_yes noloop
    sy "Oh shit. Uh, yes! That's me."
    scene d16s05-41 mc-sy-pm-station-talk2_c1 with dissolve
    play voice4 girl8_yes_aga noloop
    "Woman" "Great, come this way please."
    scene d16s05-41 mc-sy-pm-station-talk2_c3 with dissolve
    play voice3 polly_aga noloop
    sy "Of course."
    scene d16s05-42 mc-sy-pm-station-talk3_c2 with dissolve
    play voice3 stacy_mmm1 noloop
    sy "Oh my God, okay. I got this. Wish me luck."
    play voice2 mc_hey_hey5 noloop
    mc "Hey, I'm proud of you. You got this."
    scene d16s05-42 mc-sy-pm-station-talk3_c1 with dissolve
    play voice3 stacy_upset1 noloop
    sy "Uhm, thank you."
    play voice4 amrose_old_chmchm noloop
    "Woman" "*Coughs*"
    scene d16s05-42 mc-sy-pm-station-talk3_c3 with dissolve
    sy "Uh, okay, love you, byeee."

    scene d16s05-45 mc-station-timelapse3_c1 with dissolve
    pause
    play voice2 d7s6_moan1 noloop
    scene d16s05-43 mc-station-timelapse1_c1 with dissolve
    pause
    scene d16s05-44 mc-station-timelapse2_c1 with dissolve
    pause
    scene d16s05-46 mc-station-timelapse4_c1 with dissolve
    pause
    scene black
    show screen scene_transistion(_("30 minutes later"))
    with Fade(0.4, 0.4, 0.4)
    pause
    hide screen scene_transistion
    scene d16s05-47 mc-station-exit_c1
    with Fade(0.4, 0.4, 0.4)
    pause
    play voice2 d2s9_mchey noloop
    mc "Hey. How'd it go?"
    scene d16s05-47 mc-station-exit_c2 with dissolve
    play voice3 polly_angry noloop
    sy "Let's go."
    mct "Not well then..."
    stop sound3 fadeout 2.0

    $ renpy.music.set_volume(0.6, 0.0, "sound2")
    play sound2 subwaycar fadein 2.0
    scene d16s05-50 mc-sy-pm-subway-start1_c1 with fade
    play voice3 polly_pollyangry noloop
    sy "Like, seriously, who the fuck does drug tests these days!?"
    sy "Life is shit and we're all zooted out of our minds to cope anyway."
    sy "They can go fuck themselves with that drug test shit."
    scene d16s05-50 mc-sy-pm-subway-start1_c2 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah, it's kinda annoying."
    if fl_watersports is True:
        menu:
            "Ask her if she got any pictures"(hint="d16s05m02c01"):
                play voice2 mc_thinking_mmm2 noloop
                mc "Did you get any pictures though?"
                scene d16s05-52 mc-sy-pm-subway-phone_c1 with dissolve
                play voice3 stacy_hmm noloop
                sy "Oh, yeah actually."
                scene d16s05-52 mc-sy-pm-subway-phone_c2 with dissolve
                sy "Had to bend myself in 17 different angles to piss in the cup without pissing on myself in public."
                scene d16s05-62 sy-toilet1_c1 with dissolve
                pause
                scene d16s05-62 sy-toilet1_c2 with dissolve
                $ unlock_gallery_slot("cg", "d16s05p")
                pause
            "Don't"(hint="d16s05m02c02"):

                pass

    scene d16s05-53 mc-sy-pm-subway-talk1_c1 with dissolve
    play voice3 stacy_oh noloop
    sy "Oh, and a fucking polygraph test on top of all that!? For a fucking data entry position!?"
    sy "What do they think I'm going to do? Wikileaks 2: Electric Boogaloo?"
    scene d16s05-55 mc-sy-pm-subway-tongue_c2 with dissolve
    play voice2 d4s4_mclaugh noloop
    mc "*Chuckles*"
    scene d16s05-51 mc-sy-pm-subway-start2_c1 with dissolve
    play voice3 stacy_angry noloop
    sy "I swear to God, it was the dumbest shit ever."
    scene d16s05-51 mc-sy-pm-subway-start2_c2 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "I'm guessing you're gonna pass on the job then?"
    scene d16s05-54 mc-sy-pm-subway-talk2_c1 with dissolve
    play voice3 stacy_mmm2 noloop
    sy "Well... I dunno. It's a stable job and I can start whenever."
    sy "The pay is...alright I guess. Liveable."
    sy "I dunno. I'll have to sleep on it."
    scene d16s05-53 mc-sy-pm-subway-talk1_c1 with dissolve
    play voice3 stacy_upset1 noloop
    sy "Ugh, I can't wait until I have my own thing."
    sy "I can do whatever, whenever, and no one can tell me shit."
    scene d16s05-53 mc-sy-pm-subway-talk1_c2 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Welp, you gotta start somewhere."
    mc "I'm sure you'll be running the department by the end of the month."
    scene d16s05-54 mc-sy-pm-subway-talk2_c1 with dissolve
    play voice3 stacy_angryhuh noloop
    sy "Ugh, they don't tell you how exhausting interviews are."
    scene d16s05-54 mc-sy-pm-subway-talk2_c2 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yep. They're super draining."
    scene d16s05-55 mc-sy-pm-subway-tongue_c2 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Wanna go get ice cream before we go home?"
    scene d16s05-55 mc-sy-pm-subway-tongue_c1 with dissolve
    play voice3 stacy_hmm2 noloop
    sy "Yes!"

    if date_aw is True:
        call buzz from _call_buzz_20
        scene d16s05-57 mc-sy-subway-phone1_c1 with dissolve
        play voice2 mc_thinking_hmm5 noloop
        mct "Allison?"
        aw "Hey, are you busy?"
        scene d16s05-58 mc-sy-subway-phone2_c1 with dissolve
        play sound sfx_message_out1
        mct "Depends what's up?"
        play sound sfx_message_in1
        aw "Can you come over for a bit?"
        scene d16s05-59 mc-sy-subway-phone3_c1 with dissolve
        if date_awvw:
            mct "Hm, this might be my chance to talk to Allison about what went down at the party."
        menu:
            "I'll be over"(hint="d16s05m03c01"):
                play sound sfx_message_out1
                mct "Sure im with someone right now."
                scene d16s05-60 mc-sy-subway-phone4_c1 with dissolve
                play sound sfx_message_out1
                mct "I can be over in a bit tho."
                play sound sfx_message_in1
                aw "Great! Thank you."
            "I won't be able to come"(hint="d16s05m03c02"):


                $ d16_aw_reject = True

                play sound sfx_message_out1
                mct "Sorry im with someone rn."
                scene d16s05-60 mc-sy-subway-phone4_c1 with dissolve
                play sound sfx_message_in1
                aw "Oh, it's alright then."
                play sound sfx_message_in1
                aw "See you later."

        scene d16s05-61 mc-sy-subway-exit_c2 with dissolve
        play voice3 polly_hey noloop
        sy "Everything alright?"
        play voice2 mc_yes_yeah4 noloop
        mc "Yeah."
        play voice3 stacy_mmm1 noloop
        sy "Nice. You know, I really wanna try that cookie dough ice cream."
        scene d16s05-61 mc-sy-subway-exit_c1 with dissolve
        play voice2 mc_arrogant_heh1 noloop
        mc "Cookie dough? You're gonna get salmonella or something."
        play voice3 polly_laughter noloop
        sy "Worth it."
        $ unlock_gallery_slot("cg", "d16s05")

    stop sound2 fadeout 3.0
    stop music fadeout 3.5
    jump d16s06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
