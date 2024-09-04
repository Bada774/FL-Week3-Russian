image d18s11_glambot = Movie(play = "images/Day-18/s11/anim/d18s11-a32-4x-60fps.webm", start_image = "d18s12-a32 mc-ts-bar-binge-dialog-anim-32-00_i", image = "d18s12-a32 mc-ts-bar-binge-dialog-anim-32-48_i", loop = False)

label d18s11:

    if not hasattr(renpy.store, "d18s05_quartet_end"):
        $ d18s05_quartet_end = False

    $ d18s11_end_quartet = False
    $ d18s11_end_awvw = False
    $ d18s11_surprise_jdg = False
    $ d18s11_get_drunk = False

    $ renpy.music.set_volume(0.6, 0.0, "sound2")
    queue music truth_is_near
    play sound2 distanttraffic fadein 4.5
    scene d18s12-01 mc-walking-night-street_c1 with Fade(1.5, 1.5, 1.5)
    $ renpy.music.set_volume(0.7, 5.0, "music")
    pause
    scene d18s12-02 mc-walking-night-street_c2 with dissolve
    play voice2 d9s5_auch2 noloop
    mct "That bitch!{w} I still can't believe that she's been behind all this."
    mct "And she fucking gaslit me about it in the shower this morning."
    scene d18s12-03 mc-walking-night-street_c3 with dissolve
    play voice2 mc_angry_huh2 noloop
    if is_antagonist_mode is False:
        mct "Pretending like she knew nothing about Fetish Locator when she's running it!"
    elif True:
        mct "Pretending like she knew nothing about Fetish Locator when she's the fucker blackmailing me."
    mct "She was behind the whole damn thing!!!"
    play voice2 mc_pain_argh1 noloop
    play sound sfx_kick_monitor
    scene d18s12-04 mc-walking-night-street-hit_c4 with hpunch
    mc "Muther Fucker!!!"
    scene d18s12-05 mc-walking-night-street-hit_c4 with dissolve
    play voice2 mc_pain_mff5 noloop
    mct "Ow! Fuck!!!"
    mct "That hurt my hand more than the wall..."
    scene d18s12-06 mc-walking-night-street-hit_c5 with dissolve
    play voice2 mc_pain_auh6 noloop
    mct "And I don't feel any better."
    mc "Fucking bitch."
    scene d18s12-07 mc-walking-night-street_c5 with dissolve
    play voice2 mc_pain_rrrr noloop
    mct "Where the fuck am I?"
    scene d18s12-08 mc-walking-night-street_c6 with dissolve
    mct "Oh, there's a bar.{w} That seems like a good idea right now."
    scene d18s12-09 mc-walking-night-street_c7 with dissolve
    pause
label ending_12_return hide:
label ending_18_return hide:
    play sound sfx_car_approach1
    scene d18s12-10 mc-walking-night-street_c8 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mct "Fuck. Maybe I should just get the hell out of town for a while."
    scene d18s12-11 mc-walking-night-street-bus_c9 with dissolve
    mct "That's it. I'm either getting drunk or getting on that bus."
    call update_ending_variables from _call_update_ending_variables_10
    if is_extended_edition is True and d15s04_quartet_prep is True and d18s05_quartet_end is True:
        $ unlock_ending("18")
    if date_awvw is True:
        $ unlock_ending("12")
    menu:
        "Runaway with Dahlia, Samiya, and Pete"(hint="d18s11m01c01") if is_extended_edition is True and d15s04_quartet_prep is True and d18s05_quartet_end is True:
            $ d18s11_end_quartet = True
            stop sound2 fadeout 3.0
            stop sound fadeout 1.0
            jump ending_18

        "Runaway with Allison & Vanessa"(hint="d18s11m01c02") if date_awvw is True:
            $ d18s11_end_awvw = True
            stop sound2 fadeout 3.0
            stop sound fadeout 1.0
            jump ending_12

        "Surprise the Judge at Her House"(hint="d18s11m01c03") if is_extended_edition is True and date_jdg is True:
            $ d18s11_surprise_jdg = True
            stop sound2 fadeout 3.0
            stop sound fadeout 1.0
            stop music fadeout 4.0
            jump d18s11b_ext
        "Get Drunk in the Bar"(hint="d18s11m01c04"):

            $ d18s11_get_drunk = True
            stop sound2 fadeout 3.0
            stop sound fadeout 1.0
            jump d18s11_bar

label d18s11_bar:

    $ renpy.music.set_volume(0.5, 0.0, "sound3")
    queue sound3 d12s2_cafe_crowd fadein 3.0
    scene d18s12-12 mc-bar-binge_c1 with Fade(0.5, 0.5, 0.5)
    pause
    scene d18s12-13 mc-bar-binge_c2 with dissolve
    play voice4 boy4_thinking_mmm2 noloop
    "Bartender" "What will you have?"
    scene d18s12-14 mc-bar-binge_c2 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "What's strong and cheap?"
    scene d18s12-15 mc-bar-binge_c3 with dissolve
    play voice4 boy4_thinking_oh1 noloop
    "Bartender" "Are you thinking Tequila or Lily?"
    scene d18s12-16 mc-bar-binge-dialog-bartender_c2 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "That depends. Who's Lily?"
    scene d18s12-17 mc-bar-binge-dialog-bartender_c4 with dissolve
    play voice4 boy4_disappointed_ehh1 noloop
    "Bartender" "Just a joke.{w} Tequila it is."
    scene d18s12-18 mc-bar-binge-dialog-bartender_c2 with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Okay, I'll take a bottle."
    scene d18s12-19 mc-bar-binge-dialog-bartender_c2 with dissolve
    play voice4 boy4_yes_yeah noloop
    "Bartender" "Okay. I need your keys."
    play voice2 mc_no_uhuh1 noloop
    mc "No keys. I don't drive."
    play sound sfx_bottle_pouring1
    scene d18s12-20 mc-bar-binge-dialog-bartender_c2 with dissolve
    pause
    scene d18s12-21 mc-bar-binge-dialog-bartender_c4 with dissolve
    play voice4 boy4_thinking_hmm1 noloop
    "Bartender" "You're good to go. Enjoy."
    scene d18s12-22 mc-bar-binge-dialog-bartender_c1 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "I doubt I'll be enjoying anything ever again."
    scene d18s12-23 mc-bar-binge-dialog-bartender_c3 with dissolve
    play voice4 boy4_sex_closedmoan1 noloop
    "Bartender" "Girl trouble?"
    scene d18s12-24 mc-bar-binge-dialog-bartender_c1 with dissolve
    play voice2 mc_angry_errr4 noloop
    mc "You could say that. She ruined my fucking life."
    scene d18s12-25 mc-bar-binge-dialog-bartender_c6 with dissolve
    play voice3 boy4_disappointed_oh noloop
    "Bartender" "Sounds rough. I've got some other customers, but I'll be back."
    play voice2 d9s2_yeah noloop volume 2.5
    mc "No worries."
    play sound gulp
    scene d18s12-26 mc-bar-binge-dialog-bartender_c7 with dissolve
    pause
    play sound sfx_plate_place1
    scene d18s12-26-5 mc-bar-binge-dialog-bartender_c7 with dissolve
    play voice2 mc_disgust_pfe1 noloop
    mc "Damn, this shit tastes like artificial sweetener mixed with fire."
    mc "Seems thematically appropriate to my evening."
    play sound gulp
    scene d18s12-26-1 mc-bar-binge-dialog-bartender_c7 with dissolve
    pause
    play sound sfx_plate_place1
    scene d18s12-26-2 mc-bar-binge-dialog-bartender_c7 with dissolve
    play voice2 mc_angry_huh1 noloop
    mct "Fucking bitch.{w} Ruined my fucking life."
    mct "Even before we met at that damn party, she must have been setting me up."
    play sound sfx_drink_loop1 volume 2.5 loop
    scene d18s12-26-3 mc-bar-binge-dialog-bartender_c8 with dissolve
    pause
    play sound sfx_cup_place1
    scene d18s12-26-4 mc-bar-binge-dialog-bartender_c7 with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    if cage_ntr is True:
        mc "Pete's definitely part of this shit. Talk about some betrayal."
    elif True:
        mc "Pete's probably part of this shit. Talk about some betrayal."
    mc "Fucking Kevin was the person who told me all about the app and got me signed up. I wonder how much he's involved."
    scene d18s12-31 mc-ts-bar-binge-dialog_c8 with dissolve
    play voice3 aaleyah_hey_hey4 noloop
    ts "Hey baby. I'm Tracey. What's your name?"
    play sound sfx_camera_fly1
    scene d18s11_glambot with dissolve
    pause
    scene d18s12-32 mc-ts-bar-binge-dialog_c8 with dissolve
    play voice3 aaleyah_thinking_hmm2 noloop
    ts "You come here often?{w} Maybe you're looking for a good time?"
    ts "Hello?{w} C'mon, help me out here kid."
    scene d18s12-33 mc-ts-bar-binge-dialog_c8 with dissolve
    play voice3 aaleyah_disappointed_mff noloop
    ts "All these fucking pigs think I'm a whore when really I'm just a horny bitch in heat."
    ts "They keep threatening me with solicitation.{w} I don't want money."
    scene d18s12-34 mc-ts-bar-binge-dialog_c9 with dissolve
    play voice3 aaleyah_closed_moan3 noloop
    ts "I just want a hot, hard man to fuck me senseless."
    ts "Hello?{w} No?{w} Fuck."
    scene d18s12-35 mc-ts-bar-binge-dialog_c9 with dissolve
    play voice3 aaleyah_angry_egh1 noloop
    ts "Look, if you want to fuck me - or even just want a blowjob - I'll be waiting in the mens room."
    scene d18s12-36 mc-ts-bar-binge-dialog_c9 with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "Can't trust anyone.{w} FUCK!"
    scene d18s12-37 mc-ts-bar-binge-dialog_c10 with dissolve
    play voice4 boy4_arrogant_mmm1 noloop
    "Stranger" "You alright, man?"
    scene d18s12-38 mc-ts-bar-binge-dialog_c11 with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah, whatever.{w} Just figuring out how many of my so-called \"friends\" have been fucking me in the ass."
    scene d18s12-39 mc-bar-binge-dialog-people1_c12 with dissolve
    play voice4 boy4_thinking_mmm1 noloop
    "Stranger" "Uhh... okay."
    scene d18s12-40 mc-bar-binge-dialog_c12 with dissolve
    play voice2 mc_pain_mff1 noloop
    mc "AmRose? Stacy? Can I fucking trust anyone right now?"
    scene d18s12-41 mc-bar-binge-dialog_c13 with dissolve
    play voice3 pete_thinking_hmm10 noloop
    "Stranger 2" "Is that guy just talking to himself?"
    scene d18s12-42 mc-bar-binge-dialog-people1_c14 with dissolve
    play voice4 boy4_yes_confident noloop
    "Stranger 1" "You see how much Tequila he's put down already? Just leave him alone."
    "Stranger 2" "Yeah, I guess."
    scene d18s12-43 mc-bar-binge-dialog-people1_c13 with dissolve
    play voice3 terrell_hmm1 noloop volume 1.5
    "Stranger 3" "Isn't this a cop bar? Shouldn't someone do something?"
    scene d18s12-44 mc-bar-binge-dialog-people_c14 with dissolve
    play voice4 boy4_yes_yeah noloop
    "Stranger 1" "Yeah, we are.{w} We're waiting until he's passive and then we'll let him sleep it off."
    scene d18s12-45 mc-bar-binge-dialog_c3 with dissolve
    play voice2 mc_disgust_ooh1 noloop
    mc "Fucking cops. I should call the fucking cops on her."
    mc "Manipulation, coercion, blackmail, fucking shit up..."
    scene d18s12-46 mc-bar-binge-dialog_c13 with dissolve
    play voice3 pete_disappointed_mmm1 noloop
    "Stranger 2" "Looks like he's almost done."
    scene d18s12-47 mc-bar-binge-dialog_c3 with dissolve
    play voice4 boy4_hey_attention noloop
    "Bartender" "Hey buddy, I'm back.{w} How you doing?"
    scene d18s12-30 mc-bar-binge-dialog-bartender_c7 with dissolve
    play voice2 mc_pain_ou1 noloop
    mc "Fucking cunts, man."
    play sound sfx_drink_loop1 volume 2.5 loop
    scene d18s12-28 mc-bar-binge-dialog-bartender_c8 with dissolve
    play voice4 boy4_disappointed_ehh2 noloop
    "Bartender" "You should know a lot of 5-0 frequent this bar."
    stop sound fadeout 1.0
    scene d18s12-29 mc-bar-binge-dialog-bartender_c7 with dissolve
    play voice2 mc_yes_yeah6 noloop
    mc "They're probably cunts too."
    scene d18s12-47 mc-bar-binge-dialog_c3 with dissolve
    play voice4 boy4_thinking_emm3 noloop
    "Bartender" "I wouldn't say that.{w} Look, you want me to call you a Taxi or something before they haul you into the drunk tank?"
    scene d18s12-27 mc-bar-binge-dialog-bartender_c7 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah.{w} I know exactly where I want to go."
    scene d18s12-48 mc-bar-binge-dialog-bartender_c6 with dissolve
    play voice4 boy4_yes_questioning noloop
    "Bartender" "Alright... where?"
    stop sound3 fadeout 3.0
    stop music fadeout 4.0

    jump d19s01

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
