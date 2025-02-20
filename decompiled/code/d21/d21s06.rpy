label d21s06:

    $ d21s06_is_fl_rebooted_available = date_sy and d20s04_pass_exam and d20s08_copy_files and date_hr and d21s01_bj
    $ d21s06_is_waterfall_available = date_mes and date_sy and date_cl and d15s07_more_watersports
    $ d21s06_reboot_fl = False
    $ d21s06_chose_waterfall = False
    $ fl_rebooted_name = None

    scene black
    show screen scene_transistion(_("One hour later\nOutside Stacy's place"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene d21s06-01 mc-arj-door1_c2
    with Fade(0.5, 0.5, 0.9)
    play voice3 amrose_arrogant_hmm2 noloop
    arj "So exactly how many fivesomes have you been a part of?"
    play sound knockknock
    scene d21s06-01 mc-arj-door1_c1 with dissolve
    play voice2 d1s5_mchappy noloop
    mc "Me, personally?"
    scene d21s06-02 mc-arj-door2_c2 with dissolve
    play voice3 amrose_arrogant_yeah1 noloop
    arj "Is there anyone else here?"
    scene d21s06-02 mc-arj-door2_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "There's you, and me, and the door here, and other doors, presumably people behind those doors..."
    scene d21s06-03 mc-arj-door3_c2 with dissolve
    play voice3 amrose_arrogant_huh3 noloop
    arj "So you're not going to tell me, in other words."
    scene d21s06-03 mc-arj-door3_c1 with dissolve
    play voice2 d2s9_confused noloop
    mc "I'm working that out."
    scene d21s06-04 mc-arj-door4_c1 with dissolve
    mc "No, I'm not trying to mess with you. When I tell you I don't remember, I mean it."
    scene d21s06-04 mc-arj-door4_c2 with dissolve
    play voice3 amrose_thinking_hmm3 noloop
    arj "You don't remember or you plead the fifth?"
    scene d21s06-04 mc-arj-door4_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "I don't remember."
    scene d21s06-05 mc-arj-door5_c2 with dissolve
    play voice3 amrose_arrogant_huh1 noloop
    arj "You don't remember, if you, [mcname], have been a part of any fivesomes."
    scene d21s06-05 mc-arj-door5_c1 with dissolve
    play voice2 d9s2_yeah noloop volume 1.8
    mc "That's right."
    scene d21s06-02 mc-arj-door2_c2 with dissolve
    play voice3 amrose_angry_ergh noloop
    arj "You're lying. Big fat liar."
    scene d21s06-02 mc-arj-door2_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "You're all I need, baby."
    play voice3 amrose_arrogant_pff noloop
    arj "Oh, quit it."
    play sound sfx_door_open3 volume 1.3
    $ renpy.music.set_volume(0.3, 3.0, "music" )
    play music casual_guitar_1
    scene d21s06-06 mc-arj-sy-entry1_c1 with dissolve
    pause
    scene d21s06-06 mc-arj-sy-entry1_c3 with dissolve
    play voice4 stacy_huh2 noloop
    sy "What are you guys, arguing?"
    scene d21s06-06 mc-arj-sy-entry1_c2 with dissolve
    play voice3 amrose_disappointed_oh3 noloop
    arj "Apparently, this fine man has the memory of a goldfish."
    scene d21s06-07 mc-arj-sy-entry2_c1 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Speaking of which, how did we get here? Where am I? Who are you?"
    scene d21s06-07 mc-arj-sy-entry2_c2 with dissolve
    play voice3 amrose_disappointed_ehh2 noloop
    arj "Here's hoping dementia doesn't run in the family."
    scene d21s06-07 mc-arj-sy-entry2_c3 with dissolve
    play voice4 stacy_laugh4 noloop
    sy "Idiot. Also, you know the door was open, right?"
    scene d21s06-08 mc-arj-sy-entry3_c1 with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "You keep your door unlocked?"
    scene d21s06-06 mc-arj-sy-entry1_c3 with dissolve
    play voice4 stacy_mmm1 noloop
    sy "Well, I knew you were coming, and I was in the shower, so yes. I mentioned it when I called you."
    scene d21s06-08 mc-arj-sy-entry3_c1 with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "What if we were burglars?"
    scene d21s06-08 mc-arj-sy-entry3_c3 with dissolve
    play voice4 stacy_angry noloop
    sy "Then I would have caught you already because you're still standing out in the hallway! So are you coming in or what?"
    scene d21s06-07 mc-arj-sy-entry2_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "AmRose, didn't we have somewhere else to be?"
    play sound sfx_kick_leg1
    play voice3 amrose_angry_errr noloop
    scene d21s06-09 mc-arj-sy-entry4_c2 with hpunch
    pause
    scene d21s06-09 mc-arj-sy-entry4_c3 with dissolve
    play voice4 stacy_hmm noloop
    sy "First, there's the business of your living situation."
    if d21s02_bring_sy is True:
        sy "You're fine with being here, right?"
        scene d21s06-09 mc-arj-sy-entry4_c1 with dissolve
        play voice2 mc_yes_yeah4 noloop
        mc "If you're okay with it, then I'm okay with it. I just have to bring my stuff."
        scene d21s06-09 mc-arj-sy-entry4_c3 with dissolve
        play voice4 stacy_mmm2 noloop
        sy "Are you going to remember where it is?"
        scene d21s06-09 mc-arj-sy-entry4_c1 with dissolve
        play voice2 d2s9_mchey noloop volume 1.4
        mc "Come on, give me a bit of credit, I came here, didn't I?"
        scene d21s06-10 mc-arj-sy-inside1_c1 with dissolve
        play voice4 stacy_yeahno noloop
        sy "Yeah, with AmRose."
        scene d21s06-10 mc-arj-sy-inside1_c2 with dissolve
        play voice3 amrose_happy_laugh1 noloop
        arj "I'm sure he'll be fine. He gets around."
    elif d21s02_bring_arj is True:
        scene d21s06-09 mc-arj-sy-entry4_c2 with dissolve
        play voice3 amrose_arrogant_huh2 noloop
        arj "You're living with me, right?"
        play voice2 mc_yes_yeah7 noloop
        mc "Right. You told me that on the way here."
        play voice3 amrose_no_angry1 noloop
        arj "No, I didn't."
        scene d21s06-09 mc-arj-sy-entry4_c1 with dissolve
        play voice2 mc_surprised_huh3 noloop
        mc "Really?"
        scene d21s06-09 mc-arj-sy-entry4_c3 with dissolve
        play voice4 stacy_mmm2 noloop
        sy "I'm scared, is he faking it or being serious?"
        scene d21s06-09 mc-arj-sy-entry4_c2 with dissolve
        play voice2 d3s11b_mcheh noloop volume 1.6
        mc "I'm just joking. Yeah, if AmRose will have me, I'll be glad to split the rent with her."
        play voice3 amrose_happy_woo noloop
        arj "Fantastic. Movie nights are coming back then."
        scene d21s06-10 mc-arj-sy-inside1_c1 with dissolve
        pause
    else:
        scene d21s06-09 mc-arj-sy-entry4_c1 with dissolve
        play voice2 mc_yes_yeah4 noloop
        mc "I'll take care of it."
        scene d21s06-09 mc-arj-sy-entry4_c3 with dissolve
        play voice4 stacy_mmm2 noloop
        sy "What do you mean, you'll take care of it?"
        sy "Did you come into a great deal of money in the past few days? Your credit went up for the first time?"
        scene d21s06-09 mc-arj-sy-entry4_c2 with dissolve
        play voice2 d1s5b_ehhh noloop volume 1.6
        mc "I'll get around."
        play voice3 amrose_surprised_huh2 noloop
        arj "Really, [mcname]? What, you're going to be homeless?"
        scene d21s06-09 mc-arj-sy-entry4_c1 with dissolve
        play voice2 d9s3_no noloop volume 1.5
        mc "I prefer the term 'transitory person' myself."
        mc "But no, I'll find a place. Can't be too hard to find."
        scene d21s06-10 mc-arj-sy-inside1_c1 with dissolve
        pause

    play sound sfx_door_closed1
    scene d21s06-10-2 mc-arj-sy-entry6_c3 with dissolve
    play voice4 polly_aga noloop
    sy "Fine, be sure that's taken care of then."
    scene d21s06-10-2 mc-arj-sy-entry6_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "I will. Thanks for your help."
    scene d21s06-12 mc-arj-sy-inside3_c2 with dissolve
    play voice4 stacy_huh noloop
    sy "Alright, good. How about you, AmRose? You ready to go?"
    play sound sfx_cloth_rustling1
    scene d21s06-12 mc-arj-sy-inside3_c3 with dissolve
    play voice3 amrose_yes_yeah1 noloop
    arj "Yeah."
    scene d21s06-15 mc-arj-sy-inside6_c3 with dissolve
    play voice4 polly_impressed noloop
    sy "Give me a moment, let me bring the clothes."
    if d21s05_fivesome is True:
        scene d21s06-13 mc-arj-sy-inside4_c1 with dissolve
        play voice2 mc_disappointed_meh1 noloop
        mc "It's also very hard to change into a suit right after a fivesome."
        scene d21s06-16 mc-arj-sy-inside7_c3 with dissolve
        play voice3 amrose_yes_ugu noloop
        arj "Or before one."
        scene d21s06-16 mc-arj-sy-inside7_c1 with dissolve
        play voice2 mc_yes_yeah5 noloop
        mc "Yeah, that has to be a kink, right? People wearing clothes to an orgy, what's the purpose other than for teasing and to elude imagination into fantasy?"
        play voice3 amrose_no_long noloop
        arj "No, I think it has more to do with social class."
        mc "And what social class are we in, wearing the same clothes and pants everyone else wears?"
        arj "Middle class."
    scene d21s06-18 mc-arj-sy-dressup2_c3 with fade
    play voice3 amrose_thinking_hmm1 noloop
    arj "What are you doing, exactly?"
    scene d21s06-19 mc-arj-sy-dressup3_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Taking off my clothes."
    scene d21s06-19 mc-arj-sy-dressup3_c3 with dissolve
    play voice3 amrose_yes_okay2 noloop
    arj "Alright."
    play sound [sfx_skirt_off2, sfx_shoes_off1]
    scene d21s06-22 mc-arj-sy-dressup6_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "You're not going to ask why?"
    scene d21s06-21 mc-arj-sy-dressup5_c3 with dissolve
    play voice3 amrose_no_uhuh noloop
    arj "I'm assuming you have a good reason."
    scene d21s06-23 mc-arj-sy-dressup7_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "It's a surprise."
    scene d21s06-24 mc-arj-sy-dressup8_c1 with dissolve
    play voice4 min_thinking_mhh noloop
    sy "And here are your clothes-"
    play voice2 mc_happy_yay3 noloop
    mc "Ta-da."
    scene d21s06-24 mc-arj-sy-dressup8_c3 with dissolve
    play voice4 min_happy_relief noloop
    sy "You know, if you encourage this, it's only gonna get worse."
    scene d21s06-24 mc-arj-sy-dressup8_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Have a taste."
    scene d21s06-24 mc-arj-sy-dressup8_c3 with dissolve
    play voice4 stacy_uhuh noloop
    sy "We're in an apartment right now."
    scene d21s06-24 mc-arj-sy-dressup8_c2 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "So what?"
    sy "My apartment. I don't want my neighbors to think I'm a pervert."
    scene d21s06-26-1 mc-arj-sy-overall1_c1 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "I think it's a bit too late for that."
    mc "What do they think about the cage?"
    scene d21s06-26-1 mc-arj-sy-overall1_c2 with dissolve
    play voice4 polly_mmmuhuh noloop
    sy "They never saw it."
    play voice2 mc_arrogant_huh1 noloop
    mc "You don't have neighbors over?"
    sy "Nope. I don't have neighbors over."
    scene d21s06-27 mc-arj-sy-overall2_c1 with dissolve
    play voice4 min_old_hmm noloop
    sy "Here, wear this in the meantime."
    scene d21s06-27 mc-arj-sy-overall2_c2 with dissolve
    play voice2 mc_angry_huh1 noloop
    mc "That? Really?"
    scene d21s06-27 mc-arj-sy-overall2_c1 with dissolve
    play voice4 stacy_huh2 noloop
    sy "Why not?"
    scene d21s06-27 mc-arj-sy-overall2_c2 with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "I thought you had a better sense of humor than that..."
    play voice4 polly_pollyangry noloop
    sy "Shut up and wear it!"
    play sound sfx_skirt_off1 volume 2.5
    scene d21s06-28 mc-arj-sy-overall1_c1 with fade
    play voice2 mc_disgust_meh4 noloop
    mc "I feel like Hugh Hefner in the Playboy mansion."
    scene d21s06-28 mc-arj-sy-overall1_c2 with dissolve
    play voice4 polly_angry noloop
    sy "Badboy, not Playboy! All that porn and you can't read anymore!"
    scene d21s06-28 mc-arj-sy-overall1_c1 with dissolve
    play voice2 mc_pain_ou1 noloop volume 1.3
    mc "Call a medic! We have progressing case of deteriorating sense of humor!"
    scene d21s06-30 mc-sy-arj-montage1_c2 with fade
    $ renpy.music.set_volume(1.0, 1.0, "sound3" )
    play sound sfx_pliers_loop1
    play sound3 [sfx_bag_fall1, sfx_cloth_rustling5] noloop
    play voice2 mc_angry_hm1 noloop
    mc "How are we taking this apart?"
    play voice3 amrose_thinking_hmm2 noloop
    arj "The inverse of how we put it together."
    scene d21s06-30 mc-sy-arj-montage2_c2 with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "I honestly don't remember how we put it together."
    play voice3 amrose_old_haha2 noloop volume 1.3
    arj "We did it the old-fashioned way. Since this thing prevents any wi-fi connection."
    play sound2 sfx_cloth_suitcase_ride1 noloop
    scene d21s06-30 mc-sy-arj-montage3_c2 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Doesn't it need to be turned on to do that?"
    play voice3 amrose_no_simple3 noloop
    arj "No, it does that on its own."
    play voice4 stacy_yeahno noloop
    sy "Yeah. My neighbor is getting suspicious because this entire area is a deadzone, meaning no connections get through one way or the other."
    sy "So I'm happy to get rid of it."
    stop sound2 fadeout 1.0
    play sound sfx_bed_slide4
    scene d21s06-30 mc-sy-arj-montage4_c2 with dissolve
    play voice3 amrose_thinking_emm noloop
    arj "Where are you going to keep it?"
    play voice4 stacy_hmm noloop
    sy "I figure we're going to keep it around."
    arj "You can put it in a storage unit."
    sy "I was looking into it, but they're kinda expensive. I certainly can't afford it."
    play sound sfx_bed_slide3
    scene d21s06-30 mc-sy-arj-montage5_c2 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "I can look into it."
    play voice4 stacy_mmm1 noloop
    sy "You? You don't even have a place to be at."
    mc "I thought I figured that out."
    play sound sfx_wrench_long1
    scene d21s06-30 mc-sy-arj-montage6_c2 with dissolve
    sy "You deferred it."
    play voice2 mc_disappointed_ehh1 noloop
    mc "I know a person who knows a person who can sublet his unit. Is that the term?"
    play voice3 amrose_happy_mmm noloop
    arj "Why do you want to keep it around anyway, Stacy? There's no use for it since the servers are down."
    scene d21s06-30 mc-sy-arj-montage7_c2 with dissolve
    play voice4 stacy_hey noloop
    sy "We'll need it if we should need to reboot the Fetish Locator program."
    play voice3 amrose_thinking_oh1 noloop
    arj "That's hilarious."
    sy "I'm kinda serious. I have it written down on my laptop."
    arj "Written what down?"
    sy "The plans for rebooting it."
    play sound2 sfx_cloth_suitcase_ride1 noloop
    play sound sfx_bed_slide4
    scene d21s06-30 mc-sy-arj-montage8_c2 with dissolve
    play voice3 amrose_yes_okay2 noloop
    arj "Okay, Stacy, I got your joke, you don't need to keep prolonging it."
    arj "Say it once and if no one responds, move on."
    play voice2 mc_arrogant_heh2 noloop volume 1.3
    mc "I don't think she's joking. She has that glimmer in her eye."
    arj "Next, you're going to tell me you're going to start a porn empire."
    stop sound2 fadeout 1.0
    play sound sfx_bed_slide2
    scene d21s06-30 mc-sy-arj-montage9_c1 with dissolve
    play voice4 polly_laughter noloop
    sy "And here are the plans to start a porn empire."
    play voice3 amrose_surprised_uh5 noloop
    arj "You're ridiculous, you know that?"
    play sound sfx_pliers_loop1
    scene d21s06-30 mc-sy-arj-montage10_c1 with dissolve
    play voice3 amrose_pain_ahh2 noloop
    arj "We came here to dismantle the whole thing, and now you just want to start it up again?"
    play voice4 stacy_oh noloop
    sy "Well, I know you have your concerns."
    play voice3 amrose_yes_yeah3 noloop
    arj "It's a little more serious than concerns. FL has been the source of many frustrations. Don't you forget it."
    sy "And I'm here to address them."
    sy "See, if we were to involve others in our circle of trust, people we really can trust..."
    arj "Yeah, Pete, Lydia, and how about we get all the professors on it, and get their blessing?"

    if d21s06_is_fl_rebooted_available is False:
        play sound sfx_wrench_long1
        scene d21s06-30 mc-sy-arj-montage11_c1 with dissolve
        play voice4 stacy_upset1 noloop
        sy "Sorry, I didn't know you weren't interested."
        play voice3 amrose_disappointed_ehh1 noloop
        arj "I thought you were just making conversation."
        play voice4 stacy_no1 noloop
        sy "I was kinda serious."
        sy "I can actually show you in this room now that the faraday cage is almost gone and the wi-fi is working."
        sy "Fetish Locator Redux! Rebooted, reloaded, and reanimated!"
        play voice3 amrose_disgust_argh noloop
        arj "Ugh."
        play sound sfx_bed_slide3
        scene d21s06-30 mc-sy-arj-montage12_c1 with dissolve
        play voice2 mc_hey_hey5 noloop
        mc "Come on, Stacy. She's not interested."
        play voice4 min_arrogant_hm noloop
        sy "I haven't explained it yet."
        play voice3 amrose_no_nah noloop
        arj "I don't want to hear it. Sorry."
        play sound sfx_cloth_hanger1
        scene d21s06-30 mc-sy-arj-montage13_c1 with dissolve
        play voice4 min_disappointed_mph noloop
        sy "And what about the spa idea?"
        play voice3 amrose_thinking_hmm5 noloop
        arj "What spa idea?"
        play voice2 mc_yes_yeah6 noloop
        mc "We had an idea with Min to start a wellness spa. It's not even worth going into."
        arj "Why not?"
        sy "Yeah, why not?"
        if d21s06_is_waterfall_available is False:
            mc "Because it's an idea in the ether. Nothing concrete, and certainly not anything we can hitch our wagon to."
        else:
            mc "Because we need Min for that conversation!"
        play sound sfx_throw_something1
        scene d21s06-30 mc-sy-arj-montage14_c1 with dissolve
        play voice4 amrose_old_psst noloop volume 1.4
        sy "*whispers* She doesn't need to know that."
        play voice2 mc_thinking_hmm5 noloop
        mc "Need to know what?"
        sy "That it's an idea."
        mc "Just drop the Fetish Locator thing. She'll never go for it."
        sy "We can try and make it work. And what's with you? We're trying to get people on board, not off. AmRose is too valuable to let go."
        mc "There's plenty of time to think of what we'll do. Let's just put it on the back burner for now. Alright?"
        if d21s06_is_waterfall_available is False:
            mc "Plus, I have a court date in a few weeks. It's not the ideal time for me to think about rebooting an app or landing a job at a wellness spa."
        else:
            mc "Plus, I had a different idea to talk about, but later."
        sy "You said you agreed with me when we discussed it!"
        mc "That was then, not now. Several interrogations later..."
        with hpunch
        play voice3 amrose_hey_happy4 noloop
        arj "What are you two doing?"
        play voice2 d2s12_emmm noloop volume 1.5
        mc "Nothing."
        play voice3 amrose_angry_ugh noloop
        arj "Well, stop doing nothing and help me out."
        play sound sfx_chair_slide1
        scene d21s06-30 mc-sy-arj-montage15_c1 with dissolve
        play voice3 amrose_happy_phew2 noloop
        arj "Need anything else?"
        play voice4 stacy_nono noloop
        sy "No, we were going to talk about something else, but... I've decided we can talk about it some other time."
        play voice3 amrose_arrogant_huh4 noloop
        arj "You coming, [mcname]?"
        play voice2 mc_yes_yeah2 noloop
        mc "Yeah."
        mc "We'll talk about it some other time. After the trial. I swear, Stacy."


        jump d21s06_no_fl
    else:

        play voice4 min_arrogant_hm noloop
        sy "What are you, a silent partner? Tell me if you're interested or if I'm just wasting my time."
        play voice2 mc_thinking_hmm5 noloop
        mc "Interested in rebooting Fetish Locator?"
        mc "I think you're putting the cart before the horse a little here."
        mc "What is the reason for doing so, exactly?"
        sy "Let me explain. Give me a second."
        play sound sfx_chair_slide1
        scene d21s06-31 mc-arj-sy-sit1_c2 with dissolve
        pause
        play voice3 amrose_hey_whisper noloop
        arj "Should we leave?"
        play voice2 mc_arrogant_huh3 noloop
        mc "The room?"
        arj "No, back to my place."
        scene d21s06-31 mc-arj-sy-sit1_c1 with dissolve
        play voice2 mc_happy_a1 noloop
        mc "Uh, I mean, we just got here."
        play sound sfx_cloth_rustling1
        scene d21s06-33 mc-arj-sy-sit3_c2 with dissolve
        play voice3 amrose_old_chmchm noloop
        arj "I don't want to listen to her sales pitch on rebooting Fetish Locator."
        scene d21s06-34 mc-arj-sy-stand_c1 with dissolve
        play voice2 mc_yes_yeah8 noloop
        mc "Why not?"
        scene d21s06-35 mc-arj-sy-laptop_c1 with dissolve
        play voice4 stacy_mmm2 noloop
        sy "Yeah, why not?"
        play voice3 amrose_disappointed_oh5 noloop
        arj "Should we sit down?"
        scene d21s06-35 mc-arj-sy-laptop_c3 with dissolve
        play voice4 polly_nouh noloop
        sy "No, keep standing. This should only take a minute or two."
        sy "Here are some pros and cons on why we should reboot Fetish Locator."
        play sound sfx_keyboard_enter1 volume 1.5
        scene d21s06-37 mc-arj-sy-laptop3_c1 with dissolve
        play voice2 mc_happy_yay2 noloop
        mc "But there's no cons in this chart, just a list of pros."
        play voice4 polly_aga noloop
        sy "Yeah, I lost that slide."
        sy "Okay, pros."
        sy "Helps men and women discover their sexual identities."
        scene d21s06-37 mc-arj-sy-laptop3_c3 with dissolve
        play voice3 amrose_arrogant_yeah2 noloop
        arj "Con, Fetish Locator exploits anyone who uses it."
        play sound sfx_keyboard_typing2 volume 2.0
        scene d21s06-38 mc-arj-sy-laptop4_c1 with dissolve
        play voice4 polly_impressed noloop
        sy "Pro, we would use the software for the good of its users, for beneficent ends."
        scene d21s06-38 mc-arj-sy-laptop4_c3 with dissolve
        play voice3 amrose_arrogant_hmm1 noloop
        arj "Con, all software developers promise one thing and then do another."
        scene d21s06-37 mc-arj-sy-laptop3_c1 with dissolve
        play voice4 stacy_hmm noloop
        sy "Pro, most people who used Fetish Locator had a good experience with them."
        play voice3 amrose_no_nope noloop
        arj "Con, people lie when polled."
        scene d21s06-37 mc-arj-sy-laptop3_c2 with dissolve
        play voice4 min_disappointed_ehh1 noloop
        sy "Pro, uh..."
        sy "We'd have our own server room? [mcname], help me out here!"
        play voice2 mc_happy_hah2 noloop
        mc "I'm enjoying watching this, it's like watching a ping pong match."
        scene d21s06-37 mc-arj-sy-laptop3_c3 with dissolve
        play voice3 amrose_surprised_huh3 noloop
        arj "Con, where are you going to put it? And do you know how expensive a server is? And maintaining it is going to be a pain."
        play voice4 min_surprised_ehh1 noloop
        sy "Can't we rent one?"
        play voice3 amrose_yes_confident1 noloop
        arj "And what if there's a data leak? Or when a hacker steals the data on the servers?"
        scene d21s06-38 mc-arj-sy-laptop4_c1 with dissolve
        play voice4 stacy_angryhuh noloop
        sy "You're being so negative."
        scene d21s06-39 mc-arj-sy-laptop5_c1 with dissolve
        play voice3 amrose_surprised_ahh1 noloop
        arj "How can I not be? It's like you're an amnesiac, forgetting why we're here, why we helped you take this cage apart in the first place."
        arj "It wasn't so we keep it around in case we need it, we did it so we get rid of it."
        arj "Same thing with the servers."
        arj "Right, [mcname]?"
        scene d21s06-39 mc-arj-sy-laptop5_c2 with dissolve
        play voice2 mc_arrogant_hm2 noloop volume 1.3
        mc "That's why I thought we came here."
        scene d21s06-40 mc-arj-sy-laptop6_c1 with dissolve
        play voice4 stacy_yay noloop
        sy "Me too, I just couldn't sleep last night because this came up in my mind."
        sy "Of course we can get rid of it, but we have the infrastructure, we have the experience, why don't we use it for something?"
        sy "Instead of just throwing it all away and leaving it behind as a bad memory?"
        play sound sfx_keyboard_typing1
        scene d21s06-39 mc-arj-sy-laptop5_c3 with dissolve
        play voice3 amrose_hey_happy2 noloop
        arj "It WAS a bad memory."
        play voice4 stacy_yeahno noloop
        sy "Not all of it."
        arj "Enough of it was."
        stop sound fadeout 1.0
        scene d21s06-41 mc-arj-sy-laptop7_c3 with dissolve
        play voice4 polly_hey noloop
        sy "[mcname], weigh in here."
        if date_arj_romance is False:
            scene d21s06-39 mc-arj-sy-laptop5_c1 with dissolve
            play voice2 mc_hey_hey2 noloop
            mc "What about our relationship, AmRose? Isn't it in the same circle?"
            mc "Not according to me, but to society."
            scene d21s06-39 mc-arj-sy-laptop5_c3 with dissolve
            play voice3 amrose_no_angry2 noloop
            if is_antagonist_mode is True:
                arj "No, because I chose to enter a relationship with you. With Fetish Locator, I didn't consent to its activities."
            else:
                arj "I chose to enter a relationship with you and I'm quite happy I did. I regret my involvement with Fetish Locator."
            arj "I did that because I trust you. If I didn't love you, then I wouldn't have entered into it, and maybe you wouldn't have either."
            scene d21s06-40 mc-arj-sy-laptop6_c3 with dissolve
            play voice4 min_thinking_hmm2 noloop
            sy "If you guys need a minute, I can leave the room."
            play voice3 amrose_no_simple1 noloop
            arj "No, you can stay because I'm getting to my real point, Fetish Locator is not something I'm interested in working with."
        else:
            scene d21s06-38 mc-arj-sy-laptop4_c2 with dissolve
            play voice2 mc_no_uhuh1 noloop
            mc "I'm just letting you guys talk because I don't really have much to add here. You want to do something with the Fetish Locator."
            scene d21s06-38 mc-arj-sy-laptop4_c1 with dissolve
            play voice4 min_yes_simple noloop
            sy "Yes, we would be partners, business partners, in making Fetish Locator and bringing it onto the market."
            sy "Under a new name of course."
            play voice2 mc_thinking_hmm3 noloop
            mc "And why are we doing that?"
            scene d21s06-42 mc-arj-sy-laptop8_c1 with dissolve
            play voice4 min_thinking_mhh noloop
            sy "Because as we saw, there's a huge demand for it."
            sy "I imagine we make it exclusive, invite-only for now, and open it up to more users as we make sure this is the road we want to go down."
            play voice2 mc_thinking_hmm1 noloop
            mc "And where is this road?"
            sy "I'm not sure. I haven't come up with a name yet."

        jump ending_09_return

label ending_09_return hide:
    scene d21s06-43 mc-arj-sy-laptop9_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, but do we have to talk about this now?"
    play voice3 amrose_no_questioning1 noloop
    arj "I don't."
    play voice4 stacy_upset1 noloop
    sy "It won't take that long, I promise."
    sy "I know how AmRose feels about this, but is this an idea you'd potentially be interested in, [mcname]?"
    call update_ending_variables from _call_update_ending_variables_11
    $ unlock_ending("09")
    menu:
        "Yes, I want to try to reboot Fetish Locator"(hint="d21s06m01c01"):
            $ d21s06_reboot_fl = True
            jump d21s06_reboot_fl
        "No, forget it"(hint="d21s06m01c02"):

            mc "No...?"
            jump d21s06_no_fl

label d21s06_reboot_fl:

    scene d21s06-43 mc-arj-sy-laptop9_c3 with dissolve
    play voice4 polly_wooh noloop
    sy "Great."
    play voice3 amrose_arrogant_huh4 noloop
    arj "Why do you want to hear it?"
    sy "Because he's a fan of good ideas."
    arj "Whatever."
    scene d21s06-51 mc-arj-sy-talk7_c3 with fade
    play voice3 min_disappointed_ehh1 noloop
    sy "So what do you think we should name it?"
    mc "Let's call it{w} {b}Fetish Locator Rebooted!{/b}"
    play voice4 stacy_yay noloop
    sy "I love it."
    scene d21s06-53 mc-arj-sy-talk9_c2 with dissolve
    play voice3 amrose_yes_confident2 noloop
    arj "It's perfect. On point and easy to understand."
    scene d21s06-51 mc-arj-sy-talk7_c1 with dissolve
    mc "And who should we invite?"
    scene d21s06-50 mc-arj-sy-talk6_c3 with dissolve
    play voice4 stacy_mmm1 noloop
    sy "Well, I was hoping AmRose would help with the coding."
    scene d21s06-50 mc-arj-sy-talk6_c2 with dissolve
    play voice3 amrose_no_questioning2 noloop
    arj "No, no thanks."
    play voice4 stacy_oh noloop
    sy "Oh, come on."
    arj "No, I really don't want to."
    arj "I came here to do one thing, I don't really have any interest in doing anything high-paced like that."
    scene d21s06-53 mc-arj-sy-talk9_c3 with dissolve
    play voice4 stacy_huh noloop
    sy "Didn't you major in it?"
    scene d21s06-50 mc-arj-sy-talk6_c2 with dissolve
    play voice3 amrose_thinking_emm noloop
    arj "A lot of my time is spent in solitude."
    scene d21s06-50 mc-arj-sy-talk6_c3 with dissolve
    play voice4 polly_impressed noloop
    sy "Alright, but hear me out."
    sy "You know how in some film productions, they have some 'intimacy advisor' on set to have coordination between the director and the actors?"
    sy "To keep them comfortable?"
    play voice3 amrose_yes_yeah2 noloop
    arj "I heard of it."
    sy "You would have a position like that in the company."
    scene d21s06-50 mc-arj-sy-talk6_c2 with dissolve
    play voice4 amrose_disappointed_ehh1 noloop
    arj "It's hard to make an ethically immoral product by design a moral one."
    scene d21s06-53 mc-arj-sy-talk9_c3 with dissolve
    play voice4 min_thinking_hmm3 noloop
    sy "Sure you can."
    sy "[mcname] is in business administration. There's such a thing as business ethics."
    arj "If you say so."
    scene d21s06-54 mc-arj-sy-talk10_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Business ethics does exist. It's just not exercised that often. Anyway, you don't sound convinced."
    scene d21s06-54 mc-arj-sy-talk10_c2 with dissolve
    play voice3 amrose_disappointed_oh4 noloop
    arj "I'm really not."
    scene d21s06-54 mc-arj-sy-talk10_c3 with dissolve
    play voice4 stacy_oh2 noloop
    sy "So what would convince you?"
    play voice3 amrose_arrogant_hmm2 noloop
    arj "I want final say."
    sy "Final say."
    scene d21s06-55 mc-arj-sy-talk11_c2 with dissolve
    play voice3 amrose_yes_yeah4 noloop
    arj "Yeah. If I'm unhappy with an idea, like, oh, I don't know, an app that spies on its users, I want to be able to say, no, don't do that."
    scene d21s06-55 mc-arj-sy-talk11_c3 with dissolve
    play voice4 stacy_angryhuh noloop
    sy "Where are we going to make our money if we don't sell their data?"
    sy "What? Everyone does it!"
    scene d21s06-56 mc-arj-sy-talk12_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "So you want veto power?"
    play voice3 amrose_yes_confident2 noloop
    arj "Yes."
    play voice2 mc_surprised_wow3 noloop
    mc "Wow, like the president."
    scene d21s06-56 mc-arj-sy-talk12_c2 with dissolve
    play voice3 amrose_yes_ugu noloop
    arj "If you have to put it like that, yes. I'll be the president."
    scene d21s06-56 mc-arj-sy-talk12_c3 with dissolve
    play voice4 stacy_laugh4 noloop
    sy "And what would we be?"
    scene d21s06-57 mc-arj-sy-talk13_c2 with dissolve
    play voice3 amrose_thinking_hmm2 noloop
    arj "Congress? Parliament?"
    scene d21s06-57 mc-arj-sy-talk13_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "I vote for being the senate chair."
    play voice4 min_thinking_hmm2 noloop
    sy "Hmm. Okay. So we would have to run things by you that are ethically bound."
    mc "That sounds fair."
    scene d21s06-57 mc-arj-sy-talk13_c3 with dissolve
    play voice4 stacy_yeahno noloop
    sy "Yeah, it does. If that's what you want, we'll give you the final word on these matters."
    sy "So to be clear, no spying, no advertising on fishy sites... man, sustaining this app is going to be a pain."
    scene d21s06-57 mc-arj-sy-talk13_c1 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Ahem... We'll make it work though."
    mc "Right, Stacy?"
    scene d21s06-55 mc-arj-sy-talk11_c3 with dissolve
    play voice4 stacy_yes noloop
    sy "Absolutely!"
    sy "I was joking about the spying. I swear."
    scene d21s06-56 mc-arj-sy-talk12_c1 with dissolve
    play voice2 d2s9_mchey noloop volume 1.5
    mc "AmRose, don't feel pressured. Don't do anything you don't want to do."
    scene d21s06-56 mc-arj-sy-talk12_c2 with dissolve
    play voice3 amrose_thinking_hmm4 noloop
    arj "I would be actively involved in the decision making process and have final say?"
    scene d21s06-53 mc-arj-sy-talk9_c3 with dissolve
    play voice4 stacy_huh2 noloop
    sy "Do you want it to be in writing?"
    scene d21s06-53 mc-arj-sy-talk9_c2 with dissolve
    play voice3 amrose_yes_okay2 noloop
    arj "Okay, okay. I don't think you guys have any ill will like Lydia."
    arj "However, there is one more thing, and this is serious."
    arj "If you were to be all in about this plan... you have to promise me, promise me nothing like what happened with Fetish Locator will happen again."
    scene d21s06-53 mc-arj-sy-talk9_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Well, she can certainly promise that..."
    scene d21s06-52 mc-arj-sy-talk8_c3 with dissolve
    play voice4 polly_mmmuhuh noloop
    sy "I don't think she meant it like that."
    sy "Can you be a little more specific? What don't you want to happen again?"
    scene d21s06-57 mc-arj-sy-talk13_c2 with dissolve
    play voice3 amrose_disappointed_ehh2 noloop
    arj "All the cons I stated. No lies. No deceit, and no manipulation."
    scene d21s06-58 mc-arj-sy-talk14_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "You have our word, AmRose. We would never do anything to break your strict confidence. I swear it."
    scene d21s06-58 mc-arj-sy-talk14_c3 with dissolve
    play voice4 polly_aga noloop
    sy "If we make any decisions that you find ethically... icky, and I mean any, you can talk to us about it and we'll listen."
    sy "We just want to do this right, and we can't do it without you. Like literally, we don't know any coders who aren't weirdos."
    sy "Please?"
    scene d21s06-59 mc-arj-sy-talk15_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mc "Plus, Ms. President is one hell of a title."
    scene d21s06-59 mc-arj-sy-talk15_c2 with dissolve
    play voice3 amrose_yes_okay1 noloop
    arj "Alright. Okay. I'll do it."
    arj "I'll go to hell."
    scene d21s06-59 mc-arj-sy-talk15_c3 with dissolve
    play voice4 stacy_impressed noloop
    sy "Really?"
    sy "You're the best!"
    play sound sfx_cloth_rustling4
    scene d21s06-60 mc-arj-sy-hug1_c2 with dissolve
    play voice3 amrose_happy_laugh3 noloop
    arj "I would never abandon you guys."
    scene d21s06-60 mc-arj-sy-hug1_c3 with dissolve
    play voice4 stacy_yay noloop
    sy "I didn't think you would."
    play sound sfx_cloth_rustling5
    scene d21s06-61 mc-arj-sy-hug2_c1 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Thank you, AmRose. For putting your faith in us."
    play voice3 amrose_disappointed_oh5 noloop
    arj "Oh, now you're going to make me blush."
    scene d21s06-61 mc-arj-sy-hug2_c2 with dissolve
    play voice4 stacy_hey noloop
    sy "Now, let's start putting together some of the finer details like who are the initial people we can bring in."
    scene d21s06-61 mc-arj-sy-hug2_c3 with dissolve
    play voice3 amrose_yes_yeah1 noloop
    arj "Before we do that, I have to make a phone call. I'll be in the hallway for a few minutes."
    play voice2 mc_yes_sure1 noloop
    mc "Take your time."
    scene d21s06-65 mc-arj-sy-leave1_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "So where should we get started first?"

    jump ending_09

label d21s06_no_fl:

    scene d21s06-49 mc-arj-sy-talk5_c2 with fade
    play voice3 amrose_surprised_uh3 noloop
    arj "See?"
    scene d21s06-49 mc-arj-sy-talk5_c3 with dissolve
    play voice4 stacy_mmm2 noloop
    sy "I know why you guys are a little hesitant on hearing it, but just give me one minute, and I'll tell you why it's a good idea."
    scene d21s06-50 mc-arj-sy-talk6_c2 with dissolve
    play voice3 amrose_disappointed_ehh1 noloop
    arj "You had more than a minute."
    arj "If you had something good, you would have said it by now."
    scene d21s06-53 mc-arj-sy-talk9_c3 with dissolve
    play voice4 stacy_oh2 noloop
    sy "Wow, you're so unnecessarily harsh."
    scene d21s06-56 mc-arj-sy-talk12_c2 with dissolve
    play voice3 amrose_no_long noloop
    arj "I'm not usually, but when it comes to this, I've made up my mind, sorry."
    arj "I have no interest in anything related to Fetish Locator, old or new."
    if date_arj_romance is False:
        arj "The only one I'm interested in is you."
        scene d21s06-54 mc-arj-sy-talk10_c3 with dissolve
        play voice4 stacy_huh noloop
        sy "Oh God, you're not going to start making out in front of me, are you?"
        scene d21s06-49 mc-arj-sy-talk5_c2 with dissolve
        play voice3 amrose_happy_laugh3 noloop
        arj "I know when you're baiting me."
    call buzz from _call_buzz_43
label d21s06_e15_start hide:
    if from_ending_menu is True:
        $ renpy.music.set_volume(0.3, 3.0, "music" )
        play music casual_guitar_1
    scene d21s06-65 mc-arj-sy-mobile-leave_c1 with dissolve
    play voice3 amrose_hey_whisper noloop
    arj "Hey guys. I have to go. Something came up."
    scene d21s06-65 mc-arj-sy-mobile-leave_c2 with dissolve
    play voice4 stacy_angry noloop
    sy "You just got here!"
    scene d21s06-65 mc-arj-sy-mobile-leave_c1 with dissolve
    play voice3 amrose_yes_yeah4 noloop
    arj "I know, I'm sorry. Next time we meet, we'll go out to a restaurant."
    play voice4 polly_impressed noloop
    sy "Alright."
    scene d21s06-65 mc-arj-sy-mobile-leave_c3 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Actually, AmRose, do you have a few minutes?"

    if d21s06_is_waterfall_available is True:
        jump d21s06_waterfall
    else:

        scene d21s06-74-1 mc-arj-sy-talk1_c3 with dissolve
        play voice3 amrose_yes_questioning noloop
        arj "If by few minutes, you mean one minute, then yes. I have a few minutes."
        scene d21s06-74-2 mc-arj-sy-phone1_c1 with dissolve
        play voice2 mc_thinking_hmm2 noloop
        mc "Well, that's not nearly enough time to explain it. It's a business proposal."
        play sound sfx_phone_tapping1 loop volume 3.0
        scene d21s06-74-2 mc-arj-sy-phone1_c3 with dissolve
        play voice3 amrose_disappointed_oh3 noloop
        arj "[mcname], like I said, I'm not interested in getting involved in starting any new businesses."
        arj "I want something a little slower paced."
        scene d21s06-74-3 mc-arj-sy-phone2_c1 with dissolve
        play voice2 mc_yes_yeah8 noloop
        mc "What are you thinking of doing?"
        play voice3 amrose_disappointed_pff noloop
        arj "You'll laugh."
        play voice2 mc_no_no2 noloop
        mc "No, I won't."
        scene d21s06-74-2 mc-arj-sy-phone1_c3 with dissolve
        play voice3 amrose_thinking_hmm1 noloop
        arj "I'm thinking of being on a farm."
        stop sound fadeout 3.0
        scene d21s06-74-3 mc-arj-sy-phone2_c2 with dissolve
        play voice4 stacy_laugh noloop
        sy "*laughs*"
        play voice3 amrose_hey_happy4 noloop
        arj "Hey!"
        sy "Really? A farm? What are you going to do there?"
        scene d21s06-74-3 mc-arj-sy-phone2_c3 with dissolve
        play voice3 amrose_arrogant_yeah1 noloop
        arj "Actually, I'm on my way to talk to someone about renting a plot of land."
        play voice4 stacy_huh2 noloop
        sy "What, right now?"
        play voice3 amrose_yes_yeah2 noloop
        arj "Yeah."
        scene d21s06-74-4 mc-arj-sy-phone3_c2 with dissolve
        play voice4 stacy_laugh4 noloop
        sy "And you think that's a better idea than starting a wellness spa?"
        scene d21s06-65 mc-arj-sy-mobile-leave_c1 with dissolve
        play voice3 amrose_no_nah noloop
        arj "I didn't really hear your idea. Well, it's been a minute, I have to go or I'll miss the train."
        arj "Bye, you two."
        scene d21s06-66 mc-arj-sy-leave2_c2 with dissolve
        play voice4 polly_angry noloop
        sy "Wow, that was some pitch."
        scene d21s06-66 mc-arj-sy-leave2_c1 with dissolve
        play voice2 d2s9_mchey noloop volume 1.3
        mc "Hey, you try selling this idea in one minute, it won't work."
        scene d21s06-72 mc-arj-sy-leave8_c1 with dissolve
        play voice2 mc_arrogant_hm1 noloop
        mc "I should call Min to say AmRose is out."
        scene d21s06-72 mc-arj-sy-leave8_c2 with dissolve
        play voice4 polly_aga noloop
        sy "Alright, well, I'll start putting the faraday cage parts up for auction."
        scene d21s06-73 mc-arj-sy-leave9_c1 with dissolve
        play voice2 mc_no_no4 noloop
        mc "You can't do that!"
        scene d21s06-73 mc-arj-sy-leave9_c2 with dissolve
        play voice4 stacy_hmm noloop
        sy "Well, what else am I going to do with them?"
        scene d21s06-73-2 mc-arj-sy-leave10_c1 with dissolve
        play voice2 mc_thinking_hmm4 noloop
        mc "Make sure the pieces are properly destroyed?"
        play sound sfx_keyboard_typing2 volume 3.0
        scene d21s06-73-2 mc-arj-sy-leave10_c2 with dissolve
        play voice4 stacy_angryhuh noloop
        sy "You're really out of practice, you know that? Business deals abound. Now, let's start listing them. A thousand for a 4x4 piece. That sounds about right."
        play voice2 mc_disappointed_ehh1 noloop
        mc "I'll let you handle that... I'm going to try and catch up with AmRose and start preparing for this trial."
        play voice4 stacy_mmm1 noloop
        sy "Keep me updated."
        play voice2 mc_arrogant_heh1 noloop
        mc "Or you can just read a newspaper."
        play voice4 stacy_uhuh noloop
        sy "Nope."
        scene d21s06-73-3 mc-arj-sy-leave11_c1 with dissolve
        pause

        jump d21s06_end

label d21s06_waterfall:

    scene d21s06-74-1 mc-arj-sy-talk1_c3 with dissolve
    play voice3 amrose_yes_yeah2 noloop
    arj "Well, if it's really quick."
    scene d21s06-74-4 mc-arj-sy-phone3_c2 with dissolve
    play sound sfx_phone_call1 volume 2.0
    play voice4 stacy_laugh4 noloop
    sy "Who are you calling?"
    scene d21s06-74-4 mc-arj-sy-phone3_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Min."
    $ renpy.music.set_volume(1.0, 1.0, "sound2" )
    play sound2 sfx_pool_ambience2 fadein 1.5
    scene d21s06-75 min-waterfall2_c1 with dissolve
    play voice3 min_hey_simple noloop
    mes "Hey."
    $ renpy.music.set_volume(0.0, 1.0, "sound2" )
    scene d21s06-74-10 mc-arj-sy-phone9_c1 with dissolve
    play voice2 d1s2_mchey noloop volume 1.4
    mc "Hey, Min. What are you up to?"
    $ renpy.music.set_volume(1.0, 1.0, "sound2" )
    scene d21s06-76 min-waterfall3_c1 with dissolve
    play voice3 min_happy_mmm noloop
    mes "Enjoying the sun."
    $ renpy.music.set_volume(0.0, 1.0, "sound2" )
    scene d21s06-74-7 mc-arj-sy-phone6_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Listen, I was calling about the watersports-business idea, do you have some free time?"
    $ renpy.music.set_volume(1.0, 1.0, "sound2" )
    play sound sfx_water_floatup1
    scene d21s06-77 min-waterfall6_c1 with dissolve
    play voice3 min_yes_yeah1 noloop
    mes "Yeah, it's going to have to be quick though."
    $ renpy.music.set_volume(0.0, 1.0, "sound2" )
    scene d21s06-74-11 mc-arj-sy-phone10_c2 with dissolve
    play voice4 stacy_hey noloop
    sy "Hey, Min! I'm here with [mcname] and AmRose!"
    $ unlock_gallery_slot("cg", "d21s06")
    play voice5 amrose_old_hey1 noloop volume 1.4
    arj "Hello."
    $ renpy.music.set_volume(1.0, 1.0, "sound2" )
    scene d21s06-78 min-waterfall4_c1 with dissolve
    play voice3 min_hey_greeting noloop
    mes "Hi, Stacy. Hi, AmRose."
    play voice4 stacy_phonetalk_huh noloop
    sy "So a watersports-business?"
    play voice3 min_yes_aga noloop
    mes "You might have noticed that [mcname] and I are into that type of stuff."
    $ renpy.music.set_volume(0.0, 1.0, "sound2" )
    scene d21s06-74-13 mc-arj-sy-phone12_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "And I think there isn't enough places for people to practice watersports."
    $ renpy.music.set_volume(1.0, 1.0, "sound2" )
label ending_15_return hide:
    scene d21s06-81 min-waterfall7_c1 with dissolve
    play voice3 min_arrogant_huh1 noloop
    mes "We were thinking about forming a wellness spa."
    play voice3 min_thinking_emm noloop
    mes "Before we go deeper, I want your opinion. Is this something that you really want to do, or not?"
    call update_ending_variables from _call_update_ending_variables_12
    $ unlock_ending("15")
    menu:
        "Yes, this is what I want to do."(hint="d21s06m02c01"):

            mc "Yes. I want to do this with you, Min."
            $ d21s06_chose_waterfall = True

            jump d21s06_wellness_spa

        "No, I have to give it more thought."(hint="d21s06m02c02") if from_ending_menu is False:
            $ d21s06_chose_waterfall = False

            scene d21s06-82 min-waterfall8_c1 with dissolve
            play voice3 min_disappointed_mph noloop
            mes "So I'm waiting for you call then. Now I'm going to drop out."
            mes "Bye."
            $ renpy.music.set_volume(0.0, 1.0, "sound2" )
            stop sound2 fadeout 1.0
            scene d21s06-74-1 mc-arj-sy-talk1_c2 with dissolve
            play voice4 polly_impressed noloop
            sy "Alright."
            scene d21s06-74-1 mc-arj-sy-talk1_c3 with dissolve
            play voice3 amrose_yes_okay1 noloop
            arj "Alright. That was more than a minute. But it was interesting... I'm intrigued. I have to go now too."
            scene d21s06-72 mc-arj-sy-leave8_c2 with dissolve
            play voice4 stacy_oh2 noloop
            sy "Now help me pick this stuff up, we're going to put it into storage."
            scene d21s06-72 mc-arj-sy-leave8_c1 with dissolve
            play voice2 mc_hey_hey5 noloop
            mc "Hey, that's a good idea, making a company to ship and move faraday cage components."
            scene d21s06-69 mc-arj-sy-leave5_c2 with dissolve
            play voice4 stacy_angryhuh noloop
            sy "That was actually my idea. I already copyrighted it."
            scene d21s06-70 mc-arj-sy-leave6_c1 with dissolve
            play voice2 mc_arrogant_nah1 noloop
            mc "You actually have to fill out forms to copyright something, you can't just claim something and not do anything."
            scene d21s06-70 mc-arj-sy-leave6_c2 with dissolve
            play voice4 stacy_angry noloop
            sy "How do you know I haven't?"
            scene d21s06-73 mc-arj-sy-leave9_c1 with dissolve
            play voice2 mc_arrogant_huh2 noloop
            mc "You know what, I don't. I admire your dedication."
            scene d21s06-73 mc-arj-sy-leave9_c2 with dissolve
            play voice4 stacy_laugh4 noloop
            sy "You want to go out for a drink? Or you want to stay here and play video games?"
            scene d21s06-73-2 mc-arj-sy-leave10_c1 with dissolve
            play voice2 mc_arrogant_heh3 noloop
            mc "Well, I mean I don't think I'm going outside dressed like this."
            play sound sfx_keyboard_typing2 volume 2.0
            scene d21s06-73-2 mc-arj-sy-leave10_c2 with dissolve
            mc "So let's do this."
            stop music fadeout 3.0

            jump d21s06_end

label d21s06_wellness_spa:

    $ renpy.music.set_volume(1.0, 1.0, "sound2" )
    scene d21s06-82 min-waterfall8_c1 with dissolve
    play voice3 min_yes_happy noloop
    mes "People are looking for an experience that will fulfill their sexual fantasies, and we're here to provide it to them."
    mes "It's a traditional spa."
    mes "But for those who know we will offer as much special service as they want."
    mes "Until they're satisfied."
    scene d21s06-77 min-waterfall6_c1 with dissolve
    play voice3 min_yes_simple noloop
    mes "It's one-of-a-kind. I figure it will draw in a lot of men and women."
    mes "To be both givers and recievers."
    mes "And the business will cater to the connoisseur of spas, watersports, relaxation and wellness centers."
    mes "And much more."
    scene d21s06-74-11 mc-arj-sy-phone10_c1 with dissolve
    play voice4 polly_aga noloop
    sy "It is a spa, just with a twist."
    play voice2 mc_thinking_mmm4 noloop
    mc "Lots of pee..."
    $ renpy.music.set_volume(1.0, 1.0, "sound2" )
    play sound sfx_water_dive1
    scene d21s06-75 min-waterfall2_c1 with dissolve
    play voice3 min_happy_yeah noloop
    mes "The name of the business is up for deliberation."
    mes "But our idea was the Waterfall."
    $ renpy.music.set_volume(0.0, 1.0, "sound2" )
    scene d21s06-74-11 mc-arj-sy-phone10_c2 with dissolve
    play voice5 amrose_thinking_hmm3 noloop
    arj "Hmm."
    play voice4 polly_laughter noloop
    sy "You're great with names, aren't you?"
    arj "Waterfall?"
    $ renpy.music.set_volume(1.0, 1.0, "sound2" )
    play sound sfx_water_floatup2
    scene d21s06-76 min-waterfall3_c1 with dissolve
    play voice3 min_disappointed_ehh1 noloop
    mes "It was either that or the Squirt Spa. That one might have been too obvious."
    $ renpy.music.set_volume(0.0, 1.0, "sound2" )
    scene d21s06-74-12 mc-arj-sy-phone11_c3 with dissolve
    play voice4 polly_hey noloop
    sy "And how are we funding this?"

    $ renpy.music.set_volume(1.0, 1.0, "sound2" )
    scene d21s06-78 min-waterfall4_c1 with dissolve
    play voice3 min_arrogant_huh2 noloop
    mes "We can make it work with an injection of capital. We know some people on campus who accomplished something similar. Loans and such."
    mes "That won't be the hard part. The hard part will be getting the building ready and building a customer base so we turn a profit."
    $ renpy.music.set_volume(0.0, 1.0, "sound2" )
    scene d21s06-74-11 mc-arj-sy-phone10_c3 with dissolve
    play voice4 stacy_upset1 noloop
    sy "Uh, sounds complicated."
    play voice5 amrose_yes_yeah3 noloop
    arj "It will be. I'm sorry [mcname], but I can't join you for this. At least not now."
    arj "I need to finish college."
    scene d21s06-79 min-waterfall5_c1 with dissolve
    play voice3 min_yes_yeah2 noloop
    mes "Understandable. But you're still in, right [mcname]?"
    scene d21s06-74-13 mc-arj-sy-phone12_c1 with dissolve
    play voice2 d9s2_mcyes noloop volume 1.7
    mc "Hell yeah."
    $ renpy.music.set_volume(1.0, 1.0, "sound2" )
    scene d21s06-81 min-waterfall7_c1 with dissolve
    play voice3 min_arrogant_heh2 noloop
    mes "Excellent. Then I'm going to continue on the planning."
    mes "You should come over and we can start working on the details."
    mc "I'll be right there."
    stop music fadeout 3.5
    stop sound2 fadeout 1.0

    jump ending_15

label d21s06_end:

    jump d21s07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
