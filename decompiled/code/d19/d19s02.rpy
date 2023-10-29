label d19s02:

    $ d19s02_go_to_dd = False
    $ d19s02_go_to_dw = False

    scene black
    show screen scene_transistion(_("30 minutes later\nAt Stacy's apartment"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_door_open3
    scene d19s02-01 mc-arj-sy-entry1_c2
    with Fade(0.5, 0.5, 0.9)
    pause
    play sound4 sfx_keyboard_typing2 noloop
    scene d19s02-01 mc-arj-sy-entry1_c1 with dissolve
    pause
    play sound sfx_door_closed7
    scene d19s02-01-2 mc-j-nk-bar-entry2_c1 with dissolve
    $ renpy.music.set_volume(0.7, 1.5, "music")
    queue music lofi3
    play voice3 amrose_surprised_huh1 noloop
    arj "[mcname]?"
    arj "What happened to you? Are you alright? You weren't answering any of my calls!"
    scene d19s02-01-2 mc-j-nk-bar-entry2_c2 with dissolve
    play voice4 stacy_angry noloop
    sy "Yeah, what the fuck? You just vanished."
    scene d19s02-01-2 mc-j-nk-bar-entry2_c3 with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "Guys, I'm...well, not fine, but I'm alive at any rate."
    scene d19s02-01-3 mc-j-nk-bar-sit1_c1 with dissolve
    play voice4 stacy_huh noloop
    sy "What happened?"
    scene d19s02-01-3 mc-j-nk-bar-sit1_c2 with dissolve
    play voice2 mc_pain_mff5 noloop
    mc "We got the code. But Hana couldn't come with me.{w} I went into the server room alone."
    mc "I..."
    play sound sfx_memory_back4
    $ renpy.music.set_volume(2.5, 1.5, "music")
    if cage_ntr is True:


        $ Lovense.stop()

        play voice4 zbackground_mf_sex1_muffled fadein 2.5 volume 0.6
        scene d18s10-15-1 lc-fucking-pb_c1
        show memory-cloud
        with pixellate
        $ Lovense.vibrate(1)
        pause
        scene d18s10-15-2 mc-tries-to-get-better-look_c1
        show memory-cloud
        with fade
        pause
        play voice4 pete_sex_openmoans1
        play voice3 dahlia_sex_openmoans2
        $ Lovense.pattern("6;9", 1500)
        scene d18s10_a1_1
        show memory-cloud
        with fade
        pause
        scene d18s10_a2_1
        show memory-cloud
        with fade
        pause
        if d16s03_darkest_fantasy == "creampie":
            play voice4 pete_sex_orgasm2 noloop
            play voice3 lydia_orgasm1 noloop
            scene d18s10-16-05 lc-cumdrip_c1
            show memory-cloud
            with fade
            pause
            stop voice3 fadeout 1.5
            stop voice4 fadeout 1.5
        elif d16s03_darkest_fantasy == "anal":
            play voice3 dahlia_sex_openmoans2
            play voice4 pete_sex_openmoans2
            scene d18s10_a10
            show memory-cloud
            with fade
            pause
            stop voice3 fadeout 1.5
            stop voice4 fadeout 1.5
        elif d16s03_darkest_fantasy == "pissonher":
            $ renpy.music.set_volume(0.2, 0.0, "sound2")
            $ renpy.music.set_volume(0.7, 0.0, "sound4")
            play sound2 sfx_piss_loop1
            play sound4 sfx_piss_loop2
            play voice3 min_old_sinking
            play voice4 pete_sex_openmoans1
            $ Lovense.stop()
            $ Lovense.vibrate(5)
            scene d18s10_a11_2
            show memory-cloud
            with fade
            pause
            stop sound2 fadeout 1.5
            stop sound4 fadeout 1.5
            stop voice3 fadeout 1.5
            stop voice4 fadeout 1.5
        elif d16s03_darkest_fantasy == "gagging":
            play voice3 aaleyah_sucking_deep
            play voice4 pete_sex_openmoans2
            scene d18s10_a4
            show memory-cloud
            with fade
            pause
            stop voice3 fadeout 1.5
            stop voice4 fadeout 1.5
        elif d16s03_darkest_fantasy == "bdsm":
            play voice3 dahlia_sex_openmoans1
            play voice4 pete_sex_openmoans2
            scene d18s10_a6
            show memory-cloud
            with fade
            pause
            stop voice3 fadeout 1.5
            stop voice4 fadeout 1.5
        elif True:
            play voice4 pete_sex_openmoans1
            play voice3 dahlia_sex_openmoans2
            scene d18s10_a9
            show memory-cloud
            with fade
            pause
            stop voice3 fadeout 1.5
            stop voice4 fadeout 1.5
    elif True:

        scene d18s10-15-4 mc-sees-lc-clearly_c1
        show memory-cloud
        with pixellate
        pause
        scene d18s10-22-02 computer-doesnt-work_c1
        show memory-cloud
        with fade
        pause
        scene d18s10-22-03 lc-yelling-computer_c1
        show memory-cloud
        with fade
        play voice3 dahlia_angry_argh2 noloop
        pause
        scene d18s10-22-04 lc-yelling-closeup_c1
        show memory-cloud
        with fade
        play voice3 dahlia_angry_argh1 noloop
        pause
        scene d18s10-22-07 mc-thoughts-lc-tries-to-figure-bugs_c1
        show memory-cloud
        with fade
        pause
        scene d18s10-22-08 lc-sees-mc-leaving-on-camera_c1
        show memory-cloud
        with fade
        play voice3 lydia_huh2 noloop
        pause

    play sound sfx_memory_in4
    $ renpy.music.set_volume(0.8, 1.5, "music")


    $ Lovense.stop()

    scene d19s02-01-3 mc-j-nk-bar-sit1_c3 with pixellate
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "*Sigh* It was Lydia."
    scene d19s02-01-4 mc-j-nk-bar-sit2_c2 with dissolve
    play voice3 amrose_surprised_what noloop
    arj "...What?"
    scene d19s02-01-4 mc-j-nk-bar-sit2_c3 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "She was behind it all. She's the mastermind."
    scene d19s02-01-4 mc-j-nk-bar-sit2_c1 with dissolve
    play voice4 stacy_oh2 noloop
    sy "...Seriously? Fuck. Why would she...?"
    scene d19s02-05 mc-arj-sy-sit3_c3 with dissolve
    if cage_ntr is True:
        play voice3 amrose_angry_argh1 noloop
        arj "I'm going to kill that bitch."
        scene d19s02-03 mc-arj-sy-sit1_c2 with dissolve
        play voice2 mc_yes_yeah3 noloop
        mc "That would be the sweetest revenge. But it's not just her either."
        mc "Pete is working for her. Jerome too."
        scene d19s02-03 mc-arj-sy-sit1_c3 with dissolve
        play voice4 stacy_huh2 noloop
        sy "Pete? Wait, {i}your friend who you vouched for{/i} Pete?"
        scene d19s02-04 mc-arj-sy-sit2_c1 with dissolve
        play voice4 stacy_angryhuh noloop
        sy "I. Fucking. Knew. It."
        sy "That rat fucking bastard, oh my {i}{b}God{/b}{/i}."
        scene d19s02-05 mc-arj-sy-sit3_c3 with dissolve
        play voice3 amrose_disappointed_ehh2 noloop
        arj "Stacy."
        scene d19s02-04 mc-arj-sy-sit2_c3 with dissolve
        play voice4 polly_pollyangry noloop
        sy "I'm so angry right now. Fucking serenity now. Who's the other cunt?"
        scene d19s02-04 mc-arj-sy-sit2_c2 with dissolve
        play voice2 mc_arrogant_hm3 noloop
        mc "I thought he was just some asshole that tried to rape her during one of the FL parties."
        mc "But now, I...I don't even know. From what I gathered, he's her gimp."
        scene d19s02-04 mc-arj-sy-sit2_c1 with dissolve
        play voice3 amrose_surprised_uh5 noloop
        arj "Her {i}what{/i}?"
        scene d19s02-05 mc-arj-sy-sit3_c1 with dissolve
        play voice4 stacy_mmm2 noloop
        sy "What do you mean \"from what I gathered\", where were you?"
        scene d19s02-05 mc-arj-sy-sit3_c2 with dissolve
        play voice2 mc_arrogant_hm2 noloop volume 1.6
        mc "After I saw her in the server room, I just left."
        mc "I don't remember much about what happened but I got black out drunk, that's for sure."
        scene d19s02-06 mc-arj-sy-stand-talk1_c2 with dissolve
        mc "Next thing I know, I'm waking up in a sex dungeon looking up at Lydia."
        scene d19s02-06 mc-arj-sy-stand-talk1_c1 with dissolve
        play voice3 amrose_surprised_uh2 noloop
        arj "She kidnapped you!?"
        scene d19s02-08 mc-arj-sy-stand-talk3_c2 with dissolve
        play voice2 mc_yes_yeah1 noloop
        mc "I guess so."
        mc "She told me that she was my \"goddess\" and that she \"created\" me along with some other megalomaniacal bullshit."
        scene d19s02-08 mc-arj-sy-stand-talk3_c3 with dissolve
        play voice4 stacy_upset1 noloop volume 1.4
        sy "Jesus, she has really gone off the deep end."
        scene d19s02-08 mc-arj-sy-stand-talk3_c1 with dissolve
        play voice3 amrose_surprised_huh2 noloop
        arj "How did you get out?"
        play voice2 mc_thinking_mmm4 noloop
        mc "Managed to slip the bindings and deck Jerome before running as fast as I could."
        scene d19s02-09 mc-arj-sy-stand-talk4_c3 with dissolve
        play voice4 stacy_hmm noloop volume 1.5
        sy "Did you call the cops?"
        scene d19s02-09 mc-arj-sy-stand-talk4_c1 with dissolve
        play voice2 mc_yes_yes1 noloop
        mc "I did."
        scene d19s02-12 mc-arj-sy-laptop3_c1 with dissolve
        pause
        play sound sfx_keyboard_typing1
        scene d19s02-12 mc-arj-sy-laptop3_c2 with dissolve
        pause
        stop sound fadeout 1.5
        if d14s03_arj_kiss is True:
            scene d19s02-13 mc-arj-sy-laptop4_c1 with dissolve
            play voice3 amrose_pain_sobs1 noloop
            arj "God. I'm so sorry if I had just been there to protect you, I-I—"
            scene d19s02-14 mc-arj-sy-laptop5_c1 with dissolve
            play voice2 mc_hey_hey5 noloop
            mc "Hey, it's okay. I'm fine."
            scene d19s02-14 mc-arj-sy-laptop5_c2 with dissolve
            mc "You didn't do anything wrong."
            play sound dahlia_kiss_french1
            play voice3 amrose_happy_mmm noloop
            play voice2 d1s1_mmm noloop
            scene d19s02-15 mc-arj-sy-kiss_c2 with dissolve
            pause
            play sound maria_kiss2
            scene d19s02-15 mc-arj-sy-kiss_c1 with dissolve
            pause
            play sound maria_kiss1
            scene d19s02-15 mc-arj-sy-kiss_c3 with dissolve
            pause
        elif True:
            scene d19s02-13 mc-arj-sy-laptop4_c1 with dissolve
            play voice3 amrose_disappointed_ehh1 noloop
            arj "I knew we shouldn't have split up like that. If we were there we could've stopped them."
            scene d19s02-13 mc-arj-sy-laptop4_c2 with dissolve
            play voice2 mc_hey_hey5 noloop
            mc "It's alright. You all did amazingly. What happened, happened. It is what it is."
        scene d19s02-17 mc-arj-sy-talk2_c2 with fade
        play voice4 stacy_angry noloop
        sy "Bingo. Reported 207 at Lydia's place."
        sy "It says here that the \"suspect is detained.\" I'm gonna take a wild guess and say that's probably Lydia."
        scene d19s02-17 mc-arj-sy-talk2_c1 with dissolve
        play voice3 amrose_happy_phew2 noloop
        arj "Good. She can go rot."
    elif True:

        play voice3 amrose_surprised_huh2 noloop
        arj "What...? How could she... After {i}everything{/i}??"
        scene d19s02-03 mc-arj-sy-sit1_c2 with dissolve
        play voice2 mc_disappointed_ah2 noloop
        mc "I...I don't know."
        scene d19s02-03 mc-arj-sy-sit1_c1 with dissolve
        play voice3 amrose_thinking_hmm2 noloop
        arj "What do you mean?"
        play voice2 mc_arrogant_hm2 noloop volume 1.6
        mc "Look. I'm not saying that she's innocent. She is behind FL. But I don't think she meant to hurt anyone."
        scene d19s02-03 mc-arj-sy-sit1_c3 with dissolve
        play voice4 stacy_huh2 noloop
        sy "How does that make any sense?"
        scene d19s02-04 mc-arj-sy-sit2_c2 with dissolve
        play voice2 mc_thinking_mmm4 noloop
        mc "She wasn't alone. She told me that she only had the idea for the app, but someone else actually created it."
        play voice3 amrose_surprised_uh5 noloop
        arj "Who?"
        play voice2 mc_disappointed_ehh4 noloop
        mc "Jerome. But he's gone now."
        scene d19s02-04 mc-arj-sy-sit2_c3 with dissolve
        play voice4 stacy_hmm noloop volume 1.5
        sy "What do you mean \"gone\"?"
        scene d19s02-04 mc-arj-sy-sit2_c1 with dissolve
        play voice2 mc_arrogant_hm3 noloop
        mc "She told me that he vanished."
        play voice4 stacy_angryhuh noloop
        sy "Oh, what a load of horse shit. Of course he \"vanished.\" She's lying out of her teeth."
        play voice2 mc_disappointed_ah1 noloop
        mc "She handed herself in."
        scene d19s02-05 mc-arj-sy-sit3_c3 with dissolve
        play voice3 amrose_surprised_uh2 noloop
        arj "What?"
        scene d19s02-06 mc-arj-sy-stand-talk1_c2 with dissolve
        play voice2 mc_disappointed_meh1 noloop
        mc "When I found that she was behind it, I...uh, didn't take it all that well."
        scene d19s02-06 mc-arj-sy-stand-talk1_c1 with dissolve
        play voice3 amrose_surprised_ohmy noloop
        arj "What happened!? My God!"
        scene d19s02-08 mc-arj-sy-stand-talk3_c1 with dissolve
        play voice2 mc_arrogant_nah1 noloop
        mc "I'm alright. Just made some stupid decisions."
        mc "I drank myself ragged and ended up behind bars."
        mc "And when I woke up this morning, she was there. And we talked."
        scene d19s02-08 mc-arj-sy-stand-talk3_c2 with dissolve
        play voice2 mc_thinking_mmm5 noloop
        mc "She told me everything, got me out, and handed herself in."
        mc "I don't see why she would do all that if she was lying."

    if cage_ntr is False:
        scene d19s02-06 mc-arj-sy-stand-talk1_c3 with dissolve
    elif True:
        scene d19s02-18 mc-arj-sy-talk3_c2 with dissolve
    play voice4 stacy_oh noloop
    sy "Well... What now?"
    if cage_ntr is False:
        scene d19s02-06 mc-arj-sy-stand-talk1_c2 with dissolve
    elif True:
        scene d19s02-16 mc-arj-sy-talk1_c1 with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "I don't know."
    if cage_ntr is False:
        scene d19s02-06 mc-arj-sy-stand-talk1_c1 with dissolve
    elif True:
        scene d19s02-19 mc-arj-sy-talk4_c1 with dissolve
    play voice3 amrose_surprised_huh3 noloop
    arj "Can't we just turn off this damn app? We have access to the servers, right?"
    if cage_ntr is False:
        scene d19s02-08 mc-arj-sy-stand-talk3_c3 with dissolve
    play voice4 polly_aga noloop
    sy "Yeah, exactly."
    if cage_ntr is False:
        scene d19s02-08 mc-arj-sy-stand-talk3_c2 with dissolve
    elif True:
        scene d19s02-19 mc-arj-sy-talk4_c3 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Maybe.{w} But first things first, I need to prepare for the exam."
    mc "I can't let this fucking app destroy my life even more."
    if cage_ntr is False:
        scene d19s02-08 mc-arj-sy-stand-talk3_c1 with dissolve
    elif True:
        scene d19s02-19 mc-arj-sy-talk4_c2 with dissolve
    play voice3 amrose_thinking_emm noloop
    arj "What are you going to do? Exam's tomorrow, right?"
    if cage_ntr is False:
        scene d19s02-08 mc-arj-sy-stand-talk3_c2 with dissolve
    elif True:
        scene d19s02-17 mc-arj-sy-talk2_c2 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah. And knowing who's on the panel, I don't think I can pass this by just studying."
    if cage_ntr is False:
        scene d19s02-09 mc-arj-sy-stand-talk4_c3 with dissolve
    elif True:
        scene d19s02-19-2 mc-arj-sy-talk6_c1 with dissolve
    play voice4 stacy_huh2 noloop
    sy "What? Why?"
    if cage_ntr is False:
        scene d19s02-09 mc-arj-sy-stand-talk4_c2 with dissolve
    elif True:
        scene d19s02-20 mc-arj-sy-talk5_c3 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "The panel of judges are stacked against me. One hates me, one's a religious nutcase, and the other's a stickler."
    if study_points < 4:
        mc "And I didn't exactly get a lot of opportunities to study."
    if cage_ntr is False:
        scene d19s02-09 mc-arj-sy-stand-talk4_c1 with dissolve
    mc "So I need to figure out how to get them on my side."
    scene d19s02-18 mc-arj-sy-talk3_c2 with dissolve
    play voice4 stacy_mmm2 noloop
    sy "You're gonna bribe them?"
    scene d19s02-16 mc-arj-sy-talk1_c1 with dissolve
    play voice2 d9s2_mcyes noloop volume 2.5
    mc "Bribe, coerce, intimidate, whatever it takes."
    scene d19s02-16 mc-arj-sy-talk1_c2 with dissolve
    play voice4 stacy_angryhuh noloop
    sy "That's diabolical. Fuck yeah."
    scene d19s02-18 mc-arj-sy-talk3_c1 with dissolve
    play voice3 amrose_yes_okay1 noloop
    arj "Hm, okay. We can do this. Your judges were Lewald, Nordin, and Zarah, right?"
    scene d19s02-18 mc-arj-sy-talk3_c3 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah."
    scene d19s02-19 mc-arj-sy-talk4_c1 with dissolve
    play voice3 amrose_thinking_hmm4 noloop
    arj "Nordin's probably the easiest then. Man's an old perv. If we can get him in a precarious position with a student, he'd do anything to keep it secret."
    sy "A classic."
    scene d19s02-19 mc-arj-sy-talk4_c3 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sounds good to me, but finding someone that'd be willing to fuck around with Nordin will be the hardest part."
    scene d19s02-19 mc-arj-sy-talk4_c2 with dissolve
    play voice3 amrose_disappointed_oh5 noloop
    arj "And Lewald is just...I don't even know. I've met my fair share of religious nuts, but she's something else."
    arj "I feel like the best way to get to her would be to appeal to her religious side."
    play voice4 dahlia_arrogant_pff noloop
    sy "What, does [mcname] have to go molest a kid or something?"
    scene d19s02-16 mc-arj-sy-talk1_c3 with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "Jesus, Stacy."
    scene d19s02-19-2 mc-arj-sy-talk6_c1 with dissolve
    play voice4 stacy_laugh4 noloop
    sy "I kid, I kid."
    play voice3 amrose_thinking_hmm1 noloop
    arj "Well..."
    scene d19s02-17 mc-arj-sy-talk2_c2 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I would appreciate it if you didn't finish that thought."
    scene d19s02-19-2 mc-arj-sy-talk6_c2 with dissolve
    play voice3 amrose_no_simple3 noloop
    arj "No! Not that, it just makes me wonder if you could get to her through Cynthia."
    scene d19s02-20 mc-arj-sy-talk5_c3 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Hm. Might be something. I'll have to see."
    scene d19s02-20 mc-arj-sy-talk5_c1 with dissolve
    play voice3 amrose_yes_yeah1 noloop
    arj "Yeah. And Zarah... I got nothing for her."
    scene d19s02-19-2 mc-arj-sy-talk6_c3 with dissolve
    play voice2 mc_yes_yeah6 noloop
    mc "Yeah... I don't know what the fuck her problem is."
    mc "She practically hated me the moment she saw me."
    scene d19s02-20 mc-arj-sy-talk5_c2 with dissolve
    play voice4 stacy_mmm1 noloop
    sy "Have you tried talking with her? She seemed like a decent enough person to me."
    scene d19s02-20 mc-arj-sy-talk5_c3 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah... It seems like that's about all I can do to get her on my side."
    mc "So I doubt that's gonna happen. But it can't hurt to try, I guess."
    scene d19s02-18 mc-arj-sy-talk3_c3 with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "*Sigh* Welp, no rest for the wicked. I better get to it then."
    mc "I need to cram a semester's worth of knowledge into my head in a day."
    scene d19s02-19 mc-arj-sy-talk4_c3 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, by the way, do you still have the clothes I left here?"
    scene d19s02-19 mc-arj-sy-talk4_c1 with dissolve
    play voice4 stacy_yeahno noloop
    sy "Yeah. They should be in a drawer somewhere around here."
    scene d19s02-19 mc-arj-sy-talk4_c2 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Great. I wanna get out of these."
    play voice3 amrose_hey_whisper noloop
    arj "Hey, I'm sure you'll make it work. You always pull through."
    scene d19s02-20-1 mc-arj-sy-hug1_c3 with dissolve
    play voice4 polly_aga noloop
    sy "In the meantime, we'll try to see what we can do about Fetish Locator and Lydia."
    scene d19s02-21 mc-arj-sy-hug2_c1 with dissolve
    play voice4 stacy_suckmoan1 noloop
    sy "I'm sure we can get back in there and see if there's a way to shut it down or something."
    scene d19s02-21 mc-arj-sy-hug_c2 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "I don't know what I would do without you two."
    $ renpy.music.set_volume(2.0, 1.5, "music")
    scene d19s02-21 mc-arj-sy-hug_c1 with dissolve
    pause
    play voice4 stacy_suckmoan3 noloop
    scene d19s02-20-2 mc-arj-sy-hug2_c3 with dissolve
    pause
    play voice3 amrose_happy_mmm noloop
    scene d19s02-20-2 mc-arj-sy-hug2_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.8, 1.5, "music")
    if (date_dd is True or date_dw is True) and d17s06_choice_pn is False:
        scene black
        show screen scene_transistion(_("Some time later"))
        with Fade(0.9, 0.5, 0.5)
        pause
        $ renpy.music.set_volume(1.5, 1.5, "music")
        hide screen scene_transistion
        scene d19s02-25 mc-outside-talk1_c1
        with Fade(0.5, 0.5, 0.9)
        pause
        call buzz from _call_buzz_38
        scene d19s02-25 outside-talk5_c1 with dissolve
        if date_dd is True:
            play voice2 mc_thinking_hmm1 noloop
            mct "Daisy?"
            play sound sfx_message_in1
            dd "Hey dummy you busy?"
            scene d19s02-25 mc-outside-talk3_c1 with dissolve
            play sound sfx_message_out1
            mct "No whats up?"
            play sound sfx_message_in1
            dd "Can you come over?"
            scene d19s02-25 mc-outside-talk4_c1 with dissolve
            play sound sfx_message_out1
            mct "Is everything alright?"
            play sound sfx_message_in1
            dd "Everything is fine"
            play sound sfx_message_in1
            dd "I jus want you to come over"
            menu:
                "Go to her"(hint="d19s02m01c01") if True:
                    $ d19s02_go_to_dd = True
                    scene d19s02-25 mc-outside-talk2_c1 with dissolve
                    play sound sfx_message_out1
                    mct "I'll be there"
                    play sound sfx_message_in1
                    dd "*Sends a gif of a child doing a \"happy dance\"*"
                "Don't"(hint="d19s02m01c02") if True:

                    scene d19s02-25 mc-outside-talk2_c1 with dissolve
                    play sound sfx_message_out1
                    mct "Sorry i dont think i can make it today"
                    play sound sfx_message_out1
                    mct "Exams are tomorrow and I really need to catch up"
                    play sound sfx_message_in1
                    dd "Oh okay! Thats alright. Good luck with your exam!"
        elif True:

            play voice2 mc_thinking_hmm1 noloop
            mct "Dahlia?"
            play sound sfx_message_in1
            dw "Pet? Where are you?"
            scene d19s02-25 mc-outside-talk3_c1 with dissolve
            play sound sfx_message_out1
            mct "I'm out Mistress."
            play sound sfx_message_in1
            dw "Come to my dorm as soon as possible."
            play sound sfx_message_in1
            dw "I will be binding you today and incorporating ice.{w} I assume you're alright with this?"
            menu:
                "Go to her"(hint="d19s02m02c01") if True:
                    $ d19s02_go_to_dw = True
                    scene d19s02-25 mc-outside-talk4_c1 with dissolve
                    play sound sfx_message_out1
                    mct "Yes mistress"
                    play sound sfx_message_in1
                    dw "Good. Dont make me wait."
                "Don't"(hint="d19s02m02c02") if True:

                    scene d19s02-25 mc-outside-talk2_c1 with dissolve
                    play sound sfx_message_out1
                    mct "im sorry mistress i dont think i can make it today"
                    play sound sfx_message_in1
                    dw "Disappointing"

        scene d19s02-25 mc-outside-talk6_c1 with dissolve
        if is_extended_edition is True:
            mct "I forgot to ask AmRose while she is here."
        elif True:
            pause
        $ renpy.music.set_volume(0.8, 1.5, "music")

    jump d19s03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
