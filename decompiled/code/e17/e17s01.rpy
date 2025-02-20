image e17s01-a06-1 = Movie(play = "images/E-17/s01/anim/e17s01-a06-1-2x-50fps.webm", start_image = "e17s01-a06-1 when-in-rome-dw-talk-anim-01")
image e17s01-a06-1-f = Movie(play = "images/E-17/s01/anim/e17s01-a06-1-2x-60fps.webm", start_image = "e17s01-a06-1 when-in-rome-dw-talk-anim-01")
image e17s01-a06-2 = Movie(play = "images/E-17/s01/anim/e17s01-a06-2-2x-50fps.webm", start_image = "e17s01-a06-2 when-in-rome-dw-talk-anim-01")
image e17s01-a06-2-f = Movie(play = "images/E-17/s01/anim/e17s01-a06-2-2x-60fps.webm", start_image = "e17s01-a06-2 when-in-rome-dw-talk-anim-01")

image e17s01-a85-1 = Movie(play = "images/E-17/s01/anim/e17s01-a85-1-2x-50fps.webm", start_image = "e17s01-a85-1 when-in-rome-room-service-look-anim-01")
image e17s01-a85-1-f = Movie(play = "images/E-17/s01/anim/e17s01-a85-1-2x-60fps.webm", start_image = "e17s01-a85-1 when-in-rome-room-service-look-anim-01")
image e17s01-a85-2 = Movie(play = "images/E-17/s01/anim/e17s01-a85-2-2x-50fps.webm", start_image = "e17s01-a85-2 when-in-rome-room-service-look-anim-01")
image e17s01-a85-2-f = Movie(play = "images/E-17/s01/anim/e17s01-a85-2-2x-60fps.webm", start_image = "e17s01-a85-2 when-in-rome-room-service-look-anim-01")

image e17s01-a146-1 = Movie(play = "images/E-17/s01/anim/e17s01-a146-1-2x-50fps.webm", start_image = "e17s01-a146-1 when-in-rome-gotel-rs-grab-anim-01")
image e17s01-a146-1-f = Movie(play = "images/E-17/s01/anim/e17s01-a146-1-2x-60fps.webm", start_image = "e17s01-a146-1 when-in-rome-gotel-rs-grab-anim-01")
image e17s01-a146-2 = Movie(play = "images/E-17/s01/anim/e17s01-a146-2-2x-50fps.webm", start_image = "e17s01-a146-2 when-in-rome-gotel-rs-grab-anim-01")
image e17s01-a146-2-f = Movie(play = "images/E-17/s01/anim/e17s01-a146-2-2x-60fps.webm", start_image = "e17s01-a146-2 when-in-rome-gotel-rs-grab-anim-01")
image e17s01-a146-3 = Movie(play = "images/E-17/s01/anim/e17s01-a146-3-2x-50fps.webm", start_image = "e17s01-a146-3 when-in-rome-gotel-rs-grab-anim-01")
image e17s01-a146-3-f = Movie(play = "images/E-17/s01/anim/e17s01-a146-3-2x-60fps.webm", start_image = "e17s01-a146-3 when-in-rome-gotel-rs-grab-anim-01")

image e17s01-a17-glam = Movie(play = "images/E-17/s01/anim/e17s01-a17-2x-50fps.webm", start_image = "e17s01-a17 when_in_rome_glambot-17-00_i", image = "e17s01-a17 when_in_rome_glambot-17-89_i", loop = False)
image e17s01-a136-glam = Movie(play = "images/E-17/s01/anim/e17s01-a136-2x-50fps.webm", start_image = "e17s01-a136 when_in_rome_glambot-136-00_i", image = "e17s01-a136 when_in_rome_glambot-136-89_i", loop = False)

label e17_menu_jump:

    stop music fadeout 2.0
    call start_ending_from_menu from _call_start_ending_from_menu_8
    $ mcname = persistent.mcname
    $ mclogin = persistent.mclogin
    $ cage_ntr = persistent.cage_ntr
    $ stop_all_sound()
    call hide_fl_points_overlay from _call_hide_fl_points_overlay_20
    $ d19s04_dw_cum = False
    $ d15s04_quartet_prep = False

    $ renpy.music.set_volume(0.5, 3.0, "music")
    play music mystery_tension_extended fadein 1.5
    jump d19s04dw_after

label e17s01:

    call hide_fl_points_overlay from _call_hide_fl_points_overlay_21
    scene black
    show screen scene_transistion(_("Ending #17\nNot Guilty"))
    with Fade(0.9, 0.9, 0.9)
    pause
    hide screen scene_transistion
    scene black
    show screen scene_transistion(_("Some time later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_court_whispering fadein 2.5 volume 0.7 loop
    scene black
    with Fade(0.5, 0.5, 0.5)
    $ renpy.music.set_volume(1.0, 0.0, "music")
    $ renpy.music.set_volume(1.0, 0.0, "music2")
    $ renpy.music.set_volume(1.0, 0.0, "sound")
    $ renpy.music.set_volume(1.0, 0.0, "sound2")
    $ renpy.music.set_volume(1.0, 0.0, "sound3")
    $ renpy.music.set_volume(1.0, 0.0, "sound4")
    $ renpy.music.set_volume(1.0, 0.0, "sound5")
    play voice4 dahlia_reverbed_disappointed_hmm2 noloop
    dw "{i}How much do you want to know? I mean - I'm here, right?{/i}"
    dw "{i}You don't end up in a place like this unless something really fucked up happened.{/i}"
    dw "{i}In my case, well...{/i}"
    dw "{i}I guess I should start at the beginning. We met... well, there was this app... anyway, that's not important.{/i}"
    stop sound fadeout 1.5
    play sound3 sfx_plane_flyloop fadein 7.0
    play sound2 sfx_plane_takeoff fadein 1.0 noloop
    dw "{i}We hit it off - in our own way. During the summer we decided to take a tour of Europe together.{/i}"


    $ Lovense.stop()

    scene e17s01_00 with Fade(0.5, 0.5, 0.5)
    $ Lovense.pattern("7;10", 1400)
    play voice2 d7s4_mcbreathing
    play voice3 dahlia_sex_openmoans2
    play sound sfx_sex_bodyslaps1_fast loop
    dw "{i}At first, we were like any other couple. Boyfriend and girlfriend.{/i}"
    dw "{i}It was... sweet.{w} I hated it, of course. Too banal. Too pedestrian. Too normal.{/i}"
label replay_e17s01a:

    if _in_replay:
        $ renpy.music.set_volume(1.0, 0.0, "sound")
        $ renpy.music.set_volume(1.0, 0.0, "sound2")
        $ renpy.music.set_volume(1.0, 0.0, "sound3")
        play voice2 d7s4_mcbreathing
        play voice3 dahlia_sex_openmoans2
        play sound sfx_sex_bodyslaps1_fast loop
        play sound3 sfx_plane_flyloop fadein 7.0
        play sound2 sfx_plane_takeoff fadein 1.0 noloop
    scene e17s01_01_mc_talk with dissolve
    play voice2 mc_happy_oof1 noloop
    queue voice2 d7s4_mcbreathing
    mc "I hope nobody saw us come in here."
    scene e17s01_02_dw_talk with dissolve
    dw "I'm sure they did."
    scene e17s01_03_mc_talk with dissolve
    mc "Fuck. We're going to get caught."
    scene e17s01_04_dw_talk with dissolve
    dw "That's half the fun."
    scene e17s01_05_mc_talk with dissolve
    mc "Fuck! You're right."
    scene e17s01-a06-1 when-in-rome-dw-talk-anim-01 with dissolve
    dw "Hurry up - and don't you dare cum before I do."
    play sound sfx_vagina_penetration1_fast loop
    $ Lovense.pattern("7;10", 2000)
    scene e17s01-a06-1
    pause
    scene e17s01-a06-2 with dissolve
    pause
    $ Lovense.pattern("7;10", 1000)
    scene e17s01-a06-1-f with dissolve
    pause
    scene e17s01-a06-2-f with dissolve
    pause
    stop voice2 fadeout 3.5
    stop voice3 fadeout 3.5
    stop sound fadeout 3.0
    stop sound3 fadeout 3.0
    stop sound2 fadeout 1.0
    stop sound4 fadeout 2.0
    $ renpy.end_replay()
    play sound5 sfx_venice_channel fadein 2.0
    scene e17s01_07_venice with Fade(0.5, 0.5, 0.5)
    $ Lovense.stop()
    $ renpy.music.set_volume(0.45, 0.0, "music")
    play music "<silence 2.0>" noloop
    queue music music_frenchy_mood
    play voice4 dahlia_reverbed_angry_oh noloop
    dw "{i}He seemed to be loving every minute of it, but inside I was dying.{/i}"
    dw "{i}Maybe if he was a jock. Maybe if he were muscles on muscles and able to break me in two with his cock...{/i}"
    dw "{i}I knew he was a naturally-born submissive. I'm a naturally-born dominatrix.{/i}"
    dw "{i}The boyfriend-girlfriend relationship was wearing thin. We both needed something different.{/i}"
    scene e17s01_08_venice_mc_talk with dissolve
    play voice2 mc_happy_yay3 noloop
    mc "This is terrific. I've never been to a place like this before."
    $ unlock_gallery_slot("scene", "e17s01a")
    scene e17s01_09_venice_dw_talk with dissolve
    play voice3 dahlia_disgust_meh noloop
    dw "Meh."
    scene e17s01_10_venice_mc_talk with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "How can you say \"meh\" to this?"
    scene e17s01_11_venice_dw_talk with dissolve
    play voice3 dahlia_disgust_yah noloop
    dw "It seemed more fun last time I was here."
    scene e17s01_12_venice_mc_talk with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "When was that?"
    scene e17s01_13_venice_dw_talk with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    dw "Daisy and I came here just after high school."
    scene e17s01_14_venice_dw_smirk_mc_talk with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Oh."
    scene e17s01_15_venice_dw_smirk_dw_talk with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    dw "We were eighteen. It seemed like an undiscovered country."
    dw "It's all touristy now."
    scene e17s01_16_venice_dw_smirk_dw_talk with dissolve
    pause
    stop sound5 fadeout 3.0

    jump e17s01_hotel_lobby

label e17s01_hotel_lobby:

    play sound2 d12s2_cafe_crowd fadein 3.0 volume 0.5
    $ renpy.music.set_volume(0.35, 10.0, "music")
    scene e17s01-a17 when_in_rome_glambot-17-00_i
    show memory-overlay
    with Fade(0.5, 0.5, 0.5)
    play voice4 dahlia_reverbed_thinking_hmm1 noloop
    dw "({i}We were sitting in a hotel lobby when I decided to change things up.{/i})"
    play sound sfx_camera_fly1 volume 2.0
    scene e17s01-a17-glam
    pause
    stop sound fadeout 1.0
    scene e17s01_18_hotel_lobby_mc_talk with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "This is wonderful. I'd never been overseas before and now we get to -"
    scene e17s01_19_hotel_lobby_dw_talk with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    dw "This isn't working for me."
    scene e17s01_20_hotel_lobby_mc_talk with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "Wha-?"
    scene e17s01_21_hotel_lobby_dw_talk with dissolve
    play voice3 dahlia_angry_oof noloop
    dw "The balance is wrong."
    scene e17s01_22_hotel_lobby_mc_talk with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "What? I don't understand. I'm paying my share."
    scene e17s01_23_hotel_lobby_dw_talk with dissolve
    play voice3 dahlia_no_serious noloop
    dw "You don't get it. This isn't how it is supposed to be between us."
    scene e17s01_24_hotel_lobby_mc_talk with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "Huh?"
    scene e17s01_25_hotel_lobby_dw_talk with dissolve
    play voice3 dahlia_old_moan1 noloop
    dw "You're mine, Worm. Don't you get that?"
    scene e17s01_26_hotel_lobby_mc_talk with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Of course, in private-"
    scene e17s01_27_hotel_lobby_dw_talk with dissolve
    play voice3 dahlia_angry_hm2 noloop
    dw "NOT just in private. You are mine. My property. My servant. My slave."
    scene e17s01_28_hotel_lobby_mc_talk with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Yes, of course, dear."
    scene e17s01_29_hotel_lobby_dw_talk with dissolve
    play voice3 dahlia_arrogant_heh noloop
    dw "Say it, Worm."
    scene e17s01_30_hotel_lobby_mc_talk with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "I'm yours, dearest."
    scene e17s01_31_hotel_lobby_dw_talk with dissolve
    play voice3 dahlia_old_argh3 noloop
    dw "Try again, you filthy piece of shit."
    scene e17s01_32_hotel_lobby_mc_talk with dissolve
    play voice2 d2s12_emmm noloop
    mc "I am yours. Always."
    scene e17s01_33_hotel_lobby_dw_talk with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    dw "..."
    scene e17s01_34_hotel_lobby_mc_talk with dissolve
    play voice2 d3s7_mcemm noloop
    mc "I am your ssssl..."
    mc "I am your slave."
    scene e17s01_35_hotel_lobby_dw_talk with dissolve
    play voice3 dahlia_arrogant_yeah noloop
    dw "Even in public."
    scene e17s01_36_hotel_lobby_mc_talk with dissolve
    play voice2 d9s2_mcyes2 noloop volume 2.5
    mc "Yes, even in public."
    scene e17s01_37_hotel_lobby_dw_talk with dissolve
    play voice3 dahlia_old_argh noloop
    dw "Then assume the position, Worm."
    scene e17s01_38_hotel_lobby_mc_talk with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "What? I don't understand."
    scene e17s01_39_hotel_lobby_dw_talk with dissolve
    play voice3 dahlia_angry_hm1 noloop
    dw "Get on your knees and kneel at my feet, bitch."
    play sound sfx_cloth_rustling1
    scene e17s01_40_hotel_lobby_mc_talk_crawl with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Yes, Mistress."
    scene e17s01_41_hotel_lobby_dw_talk_kneeling with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    dw "This is how we should have been doing things since the beginning."
    dw "You shouldn't have to worry about *chuckles* paying your share."
    scene e17s01_42_hotel_lobby_dw_talk_feeding with dissolve
    play voice3 dahlia_old_laugh1 noloop
    dw "I'll take care of you."
    dw "And you'll pay your way by submitting to my whims."
    play voice2 mc_eating_mmm noloop
    scene e17s01_43_hotel_lobby_dw_talk_eating with dissolve
    dw "Isn't that easier?"
    play voice3 dahlia_thinking_oh noloop
    dw "Oh, dear me. You still have your mouth full."
    dw "I'll wait."
    scene e17s01_44_hotel_lobby_mc_talk_red with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Yes, Mistress."
    scene e17s01_45_hotel_lobby_dw_talk_red with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    dw "Yes to what? You took so long eating I forgot."
    scene e17s01_46_hotel_lobby_mc_talk_red with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Yes, Mistress. It is my duty to submit to your whims."
    scene e17s01_47_hotel_lobby_dw_talk_red with dissolve
    play voice3 dahlia_yes_yeah3 noloop
    dw "Very good."
    dw "I've decided that there are three ways we can do this relationship thing."
    scene e17s01_48_hotel_lobby_mc_talk_red with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Yes, Mistress?"
    scene e17s01_49_hotel_lobby_dw_talk_red with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    dw "We can pretend to be boyfriend and girlfriend. That clearly isn't working."
    scene e17s01_50_hotel_lobby_mc_talk_red with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, Mistress."
    scene e17s01_51_hotel_lobby_dw_talk_red with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    dw "The other two ways require accepting that I am your Mistress and you are my slave."
    scene e17s01_52_hotel_lobby_mc_talk_red with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course, Mistress."
    scene e17s01_53_hotel_lobby_dw_talk_red with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    dw "So, now I'm left wondering about your goal. Is it merely to keep from embarrassing us?"
    scene e17s01_54_hotel_lobby_mc_talk_red with dissolve
    play voice2 mc_no_no3 noloop
    mc "I would never want to embarrass you, Mistress."
    scene e17s01_55_hotel_lobby_dw_talk_red with dissolve
    play voice3 dahlia_arrogant_huh noloop
    dw "Or are you capable of actually making me look good?"
    scene e17s01_56_hotel_lobby_mc_talk_red with dissolve
    play voice2 d2s12_emmm noloop
    mc "Do I not do that, Mistress?"
    scene e17s01_57_hotel_lobby_dw_talk_red with dissolve
    play voice3 dahlia_no_serious noloop
    dw "No, you do not."
    dw "The highest purpose of any man is to make their woman look good."
    scene e17s01_58_hotel_lobby_mc_talk_choice with dissolve
    play voice2 d9s2_yeah noloop volume 1.7
    if persistent.is_special is True:
        mc "My sister often said that, Mistress."
    else:
        mc "I believe that is true, Mistress."
    scene e17s01_59_hotel_lobby_dw_talk with dissolve
    play voice3 dahlia_old_upset noloop volume 1.4
    dw "Sadly, I just don't think you're up to it."
    scene e17s01_60_hotel_lobby_mc_talk with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "I'm sorry, Mistress."
    scene e17s01_61_hotel_lobby_dw_talk with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    dw "For the meantime, try not to embarrass us. Try not to embarrass me."
    scene e17s01_62_hotel_lobby_mc_talk with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Yes, Mistress."
    scene e17s01_63_hotel_lobby_dw_talk with dissolve
    play voice3 dahlia_arrogant_hm noloop
    dw "Well, what are you waiting for?"
    scene e17s01_64_hotel_lobby_mc_talk with dissolve
    play voice2 d2s9_confused noloop
    mc "Mistress?"
    play voice3 dahlia_arrogant_pff noloop
    dw "Idiot."
    play sound sfx_metal_chain1
    scene e17s01_65_hotel_lobby_dw_talk_pullout_leash with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    dw "I've got something for you."
    dw "Let me put this on you properly."
    scene e17s01_66_hotel_lobby_mc_talk_pullout_leash with dissolve
    play voice2 d3s7_mcemm noloop
    mc "...?!"
    scene e17s01_67_hotel_lobby_dw_talk_pullout_leash with dissolve
    play voice3 dahlia_angry_argh2 noloop
    dw "I'm sorry, did you have something to say about this?"
    scene e17s01_68_hotel_lobby_mc_talk_pullout_leash with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "...{w} No, Mistress."
    stop sound2 fadeout 3.0

    jump e17s01_hotel_bedroom

label replay_e17s01:
label e17s01_hotel_bedroom:

    if _in_replay:
        $ renpy.music.set_volume(0.35, 0.0, "music")
        play music music_frenchy_mood
    scene e17s01_69_hotel_bedroom_dw_talk with Fade(0.5, 0.5, 0.5)
    $ Lovense.vibrate(1)
    play voice3 dahlia_thinking_mmm2 noloop
    dw "I ordered room service. They should be here soon."
    scene e17s01_70_hotel_bedroom_mc_talk with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Should I dress? A towel at least?"
    scene e17s01_71_hotel_bedroom_dw_talk with dissolve
    play voice3 dahlia_no_simple noloop
    dw "No. You shall receive them as is, and I shall sign for the bill and the tip."
    scene e17s01_72_hotel_bedroom_mc_talk with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Yes, Mistress."
    play sound knockknock
    scene e17s01_73_hotel_bedroom_knock_mc_thought with dissolve
    "*knocking at the door*"
    play voice2 d1s1_mmm noloop
    mct "Fuck me. I hope it's a woman on the other side of this door."
    scene e17s01_74_hotel_bedroom_knock_mc_thought_walk with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "Wait, fuck! If it's a woman I'll probably get arrested. Maybe I want it to be a guy?"
    scene e17s01_75_hotel_bedroom_knock_mc_thought_stand_by_door with dissolve
    mct "Too late. I'm fucked either way."
    scene e17s01_76_hotel_bedroom_knock_dw_talk with dissolve
    play voice3 dahlia_angry_argh1 noloop
    dw "Just open the fucking door, jerkoff. I'm losing my patience."
    scene e17s01_77_hotel_bedroom_knock_mc_talk with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Yes, Mistress."
    scene e17s01_78_hotel_bedroom_open_door with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "Just open the fucking door."
    play sound sfx_door_open6
    scene e17s01_79_hotel_bedroom_rs_talk with dissolve
    play voice4 girl27_hey_sexy noloop
    rs "Room Service! Where would you like-{w} Oh!?"
    scene e17s01_80_hotel_bedroom_dw_talk with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    dw "Forgive my slave. He's just following orders."
    scene e17s01_81_hotel_bedroom_rs_talk with dissolve
    play voice4 girl27_thinking_oh2 noloop
    rs "Oh, I don't mind."
    scene e17s01_82_hotel_bedroom_dw_talk with dissolve
    play voice3 dahlia_arrogant_ha noloop
    dw "Really?{w} Please bring the food over here. I'll sign for it."
    scene e17s01_83_hotel_bedroom_rs_talk with dissolve
    play voice4 girl27_happy_laugh6 noloop
    rs "It just caught me off guard. You wouldn't believe some of the things I've seen here."
    scene e17s01_84_hotel_bedroom_dw_talk with dissolve
    play voice3 dahlia_old_moan1 noloop
    dw "In that case, would you mind if I suggest something more..."
    dw "Sorry, do you mind if he locks the door?"
    scene e17s01-a85-1 when-in-rome-room-service-look-anim-01 with dissolve
    play voice4 girl27_thinking_emm5 noloop
    rs "I assume you're going to ask me something inappropriate?"
    play sound sfx_handjob_cream1 loop
    play voice2 d7s4_mcbreathing
    $ Lovense.pattern("4;7", 1400)
    scene e17s01-a85-1 with dissolve
    pause
    scene e17s01-a85-2 with dissolve
    play voice4 girl27_disappointed_ehh2 noloop
    rs "But I have the choice whether to participate or leave?"
    pause
    $ Lovense.pattern("4;7", 700)
    scene e17s01-a85-1-f with dissolve
    pause
    scene e17s01-a85-2-f with dissolve
    play voice3 dahlia_yes_yeah2 noloop
    dw "Indeed."
    pause
    stop sound fadeout 1.0
    stop voice2 fadeout 1.0
    scene e17s01_89_hotel_bedroom_turn_rs_talk with dissolve
    $ Lovense.stop()
    $ Lovense.vibrate(3)
    play voice4 girl27_arrogant_hah noloop
    rs "You heard your, Mistress. You may close the door... slave."
    play sound sfx_wheeltable_move
    scene e17s01_90_hotel_bedroom_rs_talk with dissolve
    play voice4 girl27_thinking_hmm3 noloop
    rs "I hope I used the correct pronouns, Miss, and didn't overstep my boundaries."
    scene e17s01_91_hotel_bedroom_dw_talk with dissolve
    play voice3 dahlia_happy_laugh4 noloop
    dw "That was perfect. So, as to your tip."
    scene e17s01_92_hotel_bedroom_rs_talk with dissolve
    play voice4 girl27_yes_unsure noloop
    rs "Yes, Miss?"
    scene e17s01_93_hotel_bedroom_dw_talk with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    dw "I'm American. We have a rule - always tip 20%%."
    scene e17s01_94_hotel_bedroom_rs_talk with dissolve
    play voice4 girl27_happy_relief2 noloop volume 0.8
    rs "I wish more Americans were aware of that rule."
    scene e17s01_95_hotel_bedroom_dw_talk with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    dw "However, I'm willing to make a wager with you."
    scene e17s01_96_hotel_bedroom_rs_talk with dissolve
    play voice4 girl27_thinking_oh noloop
    rs "I have to win to keep the 20%%?"
    scene e17s01_97_hotel_bedroom_dw_talk with dissolve
    play voice3 dahlia_no_uhuh noloop
    dw "No. The 20%% is what you get if you lose. I'll add a zero to that if you win."
    scene e17s01_98_hotel_bedroom_rs_talk with dissolve
    play voice4 girl27_surprised_huh noloop
    rs "200%% tip?!"
    scene e17s01_99_hotel_bedroom_dw_talk with dissolve
    play voice3 dahlia_yes_simple noloop
    dw "Exactly."
    scene e17s01_100_hotel_bedroom_rs_talk_skeptical with dissolve
    play voice4 girl27_surprised_wow1 noloop
    rs "What do I have to do?"
    scene e17s01_101_hotel_bedroom_dw_talk_skeptical with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    dw "Quite simple. My slave - as you might have noticed - is under orders to edge, but not cum."
    scene e17s01_102_hotel_bedroom_rs_talk_skeptical with dissolve
    play voice4 girl27_thinking_oh3 noloop
    rs "My English is not... Do you mean that he has to jerk off without ejaculating?"
    scene e17s01_103_hotel_bedroom_dw_talk_skeptical with dissolve
    play voice3 dahlia_yes_yeah1 noloop
    dw "Precisely."
    scene e17s01_104_hotel_bedroom_rs_talk_skeptical with dissolve
    play voice4 girl27_disappointed_mmm noloop
    rs "How long has he been doing that?"
    scene e17s01_105_hotel_bedroom_dw_talk_skeptical with dissolve
    play voice3 dahlia_disgust_oeah noloop
    dw "Slave, tell her."
    scene e17s01_106_hotel_bedroom_mc_talk_skeptical with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "One hour seventeen minutes so far, today."
    scene e17s01_107_hotel_bedroom_rs_talk_skeptical with dissolve
    play voice4 girl27_surprised_ohmy2 noloop
    rs "Oh my! Is that impressive or horrifying?"
    scene e17s01_108_hotel_bedroom_dw_talk_skeptical with dissolve
    play voice3 dahlia_no_nah noloop
    dw "Neither. His record is just over two hours."
    scene e17s01_109_hotel_bedroom_mc_talk_skeptical with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Two hours thirty four minutes, Mistress."
    scene e17s01_110_hotel_bedroom_dw_talk_skeptical with dissolve
    play voice3 dahlia_surprised_ah2 noloop
    dw "Did I ask you to clarify or correct me, Worm?"
    scene e17s01_111_hotel_bedroom_mc_talk_skeptical with dissolve
    play voice2 mc_no_no2 noloop
    mc "No, Mistress. I'm sorry, Mistress."
    scene e17s01_112_hotel_bedroom_dw_talk_skeptical with dissolve
    play voice3 dahlia_old_argh2 noloop
    dw "I'll add that to your list of punishments for later."
    scene e17s01_113_hotel_bedroom_mc_talk_skeptical with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Of course, Mistress."
    scene e17s01_114_hotel_bedroom_rs_talk_skeptical with dissolve
    play voice4 girl27_arrogant_hm5 noloop
    rs "So, the wager."
    scene e17s01_115_hotel_bedroom_dw_talk_skeptical with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    dw "You simply have to make him cum - that is, ejaculate - before his current record."
    scene e17s01_116_hotel_bedroom_rs_talk_skeptical with dissolve
    play voice4 girl27_surprised_huh3 noloop
    rs "I have over an hour to make him cum? In exchange for a 200%% tip on this order?"
    scene e17s01_117_hotel_bedroom_dw_talk_skeptical with dissolve
    play voice3 dahlia_thinking_oh noloop
    dw "Is it not enough? Shall I make it a 250%% tip?"
    scene e17s01_118_hotel_bedroom_rs_talk_skeptical with dissolve
    play voice4 girl27_happy_hmm1 noloop
    rs "What are my limitations?"
    scene e17s01_119_hotel_bedroom_dw_talk_skeptical with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    dw "No permanent damage."
    scene e17s01_120_hotel_bedroom_rs_talk_hesitant with dissolve
    play voice4 girl27_thinking_hmm6 noloop
    rs "So, I could simply wait to see if he jerks himself off in time, or I could even let him fuck me... anything so long as it results in his ejaculating?"
    scene e17s01_121_hotel_bedroom_dw_talk_hesitant with dissolve
    play voice3 dahlia_yes_questioning noloop
    dw "Essentially, yes."
    scene e17s01_122_hotel_bedroom_rs_talk_hesitant with dissolve
    play voice4 girl27_scared_oh2 noloop
    rs "And if I lose, I still get a 20%% tip."
    scene e17s01_123_hotel_bedroom_dw_talk_hesitant with dissolve
    play voice3 dahlia_yes_yeah4 noloop
    dw "Correct."
    scene e17s01_118_hotel_bedroom_rs_talk_skeptical with dissolve
    play voice4 girl27_thinking_mmm noloop
    rs "And if I win, I get-"
    scene e17s01_119_hotel_bedroom_dw_talk_skeptical with dissolve
    play voice3 dahlia_yes_aga noloop
    dw "Ten times that."
    scene e17s01_124_hotel_bedroom_rs_talk_maniacal with dissolve
    play voice4 girl27_happy_nice1 noloop
    rs "Very well, I accept."
    scene e17s01_125_hotel_bedroom_dw_talk_maniacal with dissolve
    play voice3 dahlia_arrogant_heh noloop
    dw "You heard her, slave. And just to make it more fun - [mcname], if you cum, I'll cut your balls off."
    scene e17s01_126_hotel_bedroom_mc_talk_maniacal with dissolve
    play voice2 mc_scared_huuuh3 noloop
    mc "Mistress?!"
    scene e17s01_127_hotel_bedroom_dw_talk_maniacal with dissolve
    play voice3 dahlia_happy_laugh3 noloop
    dw "I'm kidding. You'll be punished - brutally - if you let her win."
    scene e17s01_128_hotel_bedroom_mc_talk_maniacal with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "*sigh* Yes, Mistress."
    scene e17s01_127_hotel_bedroom_dw_talk_maniacal with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    dw "Although I might have you go to a backstreet doctor and get a vasectomy."
    scene e17s01_126_hotel_bedroom_mc_talk_maniacal with dissolve
    play voice2 mc_pain_mff3 noloop
    mct "She wouldn't?! Would she?!"
    mc "Understood, Mistress."
    scene e17s01_130_hotel_bedroom_dw_talk_panicked with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    dw "Very well, you may begin whenever you are ready."
    scene e17s01_131_hotel_bedroom_rs_talk_panicked with dissolve
    play voice4 girl27_yes_yap2 noloop
    rs "Thank you, Miss."
    scene e17s01_132_hotel_bedroom_rs_talk_hair_pull with dissolve
    pause

    jump e17s01_sex

label e17s01_sex:

    play sound sfx_hair_scratch1
    scene e17s01_133_hotel_bedroom_rs_talk_hair_pull with dissolve
    play voice4 girl27_thinking_hmm5 noloop
    rs "Tell me, slave, do you like your Mistress's feet?"
    scene e17s01_134_hotel_bedroom_mc_talk_hair_pull with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yes... ma'am?"
    scene e17s01_135_hotel_bedroom_rs_talk_hair_pull with dissolve
    play voice4 girl27_disgust_mff noloop
    rs "Call me...{w} Goddess."
    scene e17s01-a136 when_in_rome_glambot-136-00_i with dissolve
    play voice4 girl27_thinking_emm4 noloop
    rs "Is that acceptable, Miss?"
    play voice3 dahlia_yes_angry noloop
    dw "It is. For the next hour, slave, this is your Goddess."
    play sound sfx_camera_fly1 volume 2.0
    scene e17s01-a136-glam
    pause
    stop sound fadeout 1.0
    scene e17s01_137_hotel_bedroom_mc_talk_look_at_dw with dissolve
    play voice2 d9s2_mcyes noloop volume 2.5
    mc "Yes, Mistress. Thank you, Goddess."
    scene e17s01_138_hotel_bedroom_rs_talk_look_at_dw with dissolve
    play voice4 girl27_angry_mmm noloop
    rs "Lick them. Lick the soles of your Mistress's feet."
    scene e17s01_139_hotel_bedroom_mc_talk_licking with dissolve
    play voice2 mc_sex_sucking_slow1
    play voice3 dahlia_old_moan1 noloop
    pause
    queue voice3 dahlia_old_moan2 noloop
    scene e17s01_140_hotel_bedroom_rs_talk_touch_ass with dissolve
    play voice4 girl27_yes_ya noloop
    rs "Very good, slave."
    rs "Very good. He hasn't even stopped - what did you call it? Edging?"
    scene e17s01_141_hotel_bedroom_dw_talk_touch_ass with dissolve
    play voice3 dahlia_yes_yeah3 noloop
    dw "Edging. Correct."
    scene e17s01_142_hotel_bedroom_rs_talk_touch_ass with dissolve
    play voice4 girl27_happy_laugh4 noloop
    rs "He seems very well trained. And in good shape."
    rs "I wonder how he'll respond to this?"
    play sound sfx_fisting_fist1
    $ Lovense.vibrate(8)
    scene e17s01_143_hotel_bedroom_mc_talk_grab_balls with dissolve
    play voice2 mc_pain_rrrr noloop
    mc "MMMmmmppphhh!"
    scene e17s01_144_hotel_bedroom_dw_talk_grab_balls with dissolve
    play voice3 dahlia_surprised_huh1 noloop
    dw "I hope you're not doing any permanent damage."
    play sound sfx_fisting_fist2
    scene e17s01_145_hotel_bedroom_mc_talk_grab_balls_twist with dissolve
    play voice2 d9s5_auch2 noloop
    mc "MMMMmmmmMMppphhhh!!!"
    play voice2 mc_sex_sucking_slow1
    play voice3 jessie_moans volume 0.7
    play voice4 hana_moans
    play sound sfx_handjob_cream1 loop
    play sound2 sfx_vagina_penetration1_fast volume 0.5
    $ Lovense.pattern("7;10", 1400)
    scene e17s01-a146-1 with dissolve
    pause
    play voice4 girl27_no_nonono2 noloop
    queue voice4 hana_moans
    rs "Nothing that won't heal. Has he cleaned his ass yet today?"
    scene e17s01-a146-2 with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    queue voice3 jessie_moans
    dw "He was to have his enema after I finished my meal."
    pause
    scene e17s01-a146-3 with dissolve
    play voice4 girl27_disgust_ohh3 noloop
    queue voice4 hana_moans
    rs "Oh dear. After he ejaculates, please order him to clean my fingers."
    play voice3 dahlia_yes_aga noloop
    queue voice3 jessie_moans
    dw "Of course."
    pause
    $ Lovense.pattern("7;10", 700)
    scene e17s01-a146-1-f with dissolve
    pause
    play voice2 d7s4_mcbreathing
    play sound mc_sex_sucking_slow1 loop
    mc "Ohhhoohhooohhhhhoooo... no..."
    scene e17s01-a146-2-f with dissolve
    pause
    scene e17s01-a146-3-f with dissolve
    play voice4 girl27_hey_sexy noloop
    rs "He's almost there. I've always wanted to try this."
    pause
    play voice4 girl27_angry_err3 noloop
    play sound sfx_whip_slap1
    play voice2 d1s5_orgasm2 noloop volume 1.7
    play sound2 mc_cum_sound1 noloop
    stop voice3 fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(16)
    scene e17s01_152_hotel_bedroom_cum with hpunch
    pause
    scene e17s01_153_hotel_bedroom_cum_dw_talk with dissolve
    $ Lovense.vibrate(3)
    play voice3 dahlia_arrogant_huh noloop
    dw "Slave, did you just cum?"
    scene e17s01_154_hotel_bedroom_cum_mc_talk with dissolve
    play voice2 d2s12_emmm noloop
    mc "Yes, Mistress. I'm sorry, Mistress."
    scene e17s01_155_hotel_bedroom_step_back_dw_talk with dissolve
    play voice3 dahlia_angry_ah1 noloop
    dw "DID YOU CUM WITHOUT PERMISSION?!"
    scene e17s01_156_hotel_bedroom_step_back_mc_talk with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yes, Mistress. I'm so sorry... I'm so very very sorry..."
    scene e17s01_157_hotel_bedroom_rs_stand_dw_talk with dissolve
    play voice3 dahlia_angry_argh1 noloop
    dw "You cost me money, bitch. The least you can do is turn around and suck her fingers clean."
    scene e17s01_158_hotel_bedroom_rs_stand_mc_talk with dissolve
    play voice2 d9s2_mcyes2 noloop volume 2.6
    mc "Yes, Mistress"
    $ unlock_gallery_slot("scene", "e17s01")
    scene e17s01_159_hotel_bedroom_fingers_dw_talk with dissolve
    play voice2 mc_sex_sucking_fast1
    play voice3 dahlia_disgust_oof noloop
    dw "After that, slave, you can clean up your cum from wherever it landed."
    dw "Lick it up, suck it up, use your mouth to make sure there isn't a drop left. I'll check with the blacklight later."
    play sound sfx_pen_writing2
    scene e17s01_160_hotel_bedroom_writing_paper_dw_talk with dissolve
    play voice3 dahlia_arrogant_hm noloop
    dw "As for you, what did we agree on? 500%% tip?"
    scene e17s01_161_hotel_bedroom_writing_paper_rs_talk with dissolve
    play voice4 girl27_no_nonono1 noloop
    rs "I believe it was 200%%, Miss."
    scene e17s01_162_hotel_bedroom_writing_paper_dw_talk with dissolve
    play voice3 dahlia_arrogant_heh noloop
    dw "Honest too. Good for you."
    play sound sfx_paper_slide1 volume 1.5
    scene e17s01_163_hotel_bedroom_hand_paper_dw_talk_mc_lick with dissolve
    play voice2 mc_sex_sucking_slow1
    dw "If you had tried to cheat me, well... you wouldn't have enjoyed it. Although I would have."
    dw "Now get out of here, you earned every cent of what I wrote down."
    scene e17s01_164_hotel_bedroom_rs_leaves_dw_talk with dissolve
    play voice3 dahlia_angry_hm1 noloop
    dw "Take your time, [mcname]. I have to invent new punishments for you now."
    stop voice2 fadeout 2.0

    $ Lovense.stop()


    $ renpy.end_replay()

    stop music fadeout 3.0
    jump e17s02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
