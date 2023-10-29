image d16s01_sy_mc_catch = Movie(play = "images/Day-16/Scene-01/anim/d16s01-a1-2x-50fps.webm", start_image = "d16s01-63-a1 mc-tosses-flli-to-sy-glambot-1-000_i", image = "d16s01-63-a1 mc-tosses-flli-to-sy-glambot-1-196_i", loop = False)

label d16s01:

    $ cockcage_released = False

    scene black
    show screen scene_transistion(_("Tuesday\nDay-16"))
    with Fade(0.9, 0.5, 0.5)
    pause
    $ renpy.music.set_volume(0.05, 0.0, "sound2")
    play sound2 park fadein 3.0
    play voice2 d7s6_snoring fadein 3.0
    hide screen scene_transistion
    scene d16s01-01-mc-groggily-blinks
    with Fade(0.5, 0.5, 0.9)
    pause
    $ renpy.music.set_pan(0.8, 0.0, "voice3")
    $ renpy.music.set_pan(0.8, 0.0, "sound")
    play voice3 stacy_oh2 noloop
    play sound sfx_keyboard_enter1
    sy "Oh shit, it compiled on the first try! That doesn't bode well..."
    $ renpy.music.set_volume(0.01, 2.0, "sound2")
    $ renpy.music.set_volume(0.2, 2.0, "voice2")
    scene black with Fade(0.5, 0.5, 0.5)
    "..."
    $ renpy.music.set_volume(0.05, 2.0, "sound2")
    $ renpy.music.set_volume(1.0, 2.0, "voice2")
    scene d16s01-02-mc-groggily-blinks with Fade(0.5, 0.5, 0.5)
    pause
    $ renpy.music.set_pan(0.7, 0.0, "voice3")
    play voice3 stacy_angryhuh noloop
    play sound sfx_keyboard_typing2
    sy "99 dastardly bugs in the code, 99 dastardly bugs. Take one down, patch it around, 110 dastardly bugs in the code..."
    stop sound fadeout 2.0
    $ renpy.music.set_volume(0.01, 2.0, "sound2")
    $ renpy.music.set_volume(0.2, 2.0, "voice2")
    scene black with Fade(0.5, 0.5, 0.5)
    "..."
    $ renpy.music.set_volume(0.05, 2.0, "sound2")
    $ renpy.music.set_volume(1.0, 2.0, "voice2")
    scene d16s01-03-mc-groggily-blinks with Fade(0.5, 0.5, 0.5)
    pause
    play voice3 amrose_angry_breath1 noloop
    play sound sfx_keyboard_typing1
    sy "God, I need this to not shit the bed right now."
    stop sound fadeout 2.0
    $ renpy.music.set_volume(0.01, 2.0, "sound2")
    $ renpy.music.set_volume(0.2, 2.0, "voice2")
    scene black with Fade(0.5, 0.5, 0.5)
    "..."
    if d14s03_arj_kiss is True:
        $ renpy.music.set_volume(0.05, 2.0, "sound2")
        $ renpy.music.set_volume(1.0, 2.0, "voice2")
        scene d16s01-02-mc-groggily-blinks with Fade(0.5, 0.5, 0.5)
        pause
        $ renpy.music.set_pan(0.5, 0.0, "voice3")
        $ renpy.music.set_pan(0.5, 0.0, "voice4")
        play voice3 amrose_old_psst2 noloop
        play sound sfx_keyboard_typing2
        arj "Hey, we should try to keep it down a bit. [mcname] is sleeping still."
        play voice4 stacy_hmm noloop
        sy "Oop, right."
        stop sound fadeout 2.0
        $ renpy.music.set_volume(0.01, 2.0, "sound2")
        $ renpy.music.set_volume(0.2, 2.0, "voice2")
        scene black with Fade(0.5, 0.5, 0.5)
        "..."
        $ renpy.music.set_volume(0.05, 2.0, "sound2")
        $ renpy.music.set_volume(1.0, 2.0, "voice2")
        scene d16s01-03-mc-groggily-blinks with Fade(0.5, 0.5, 0.5)
        pause
    $ renpy.music.set_volume(0.05, 2.0, "sound2")
    $ renpy.music.set_volume(1.0, 2.0, "voice2")
    play voice3 stacy_yay noloop
    sy "Hallelujah, I think it's finally working."
    $ renpy.music.set_pan(0.0, 0.0, "sound")
    play sound sfx_cloth_rustling1
    play voice2 ["<silence 0.3>", d7s6_moan1] noloop
    scene d16s01-04-mc-wakes-up with fade
    pause
    play sound sfx_cloth_rustling2
    scene d16s01-05-arj-sy-looking-at-mc with dissolve
    $ renpy.music.set_volume(0.7, 0.0, "music")
    stop sound2 fadeout 6.0
    play music lofi_morning
    pause
    $ renpy.music.set_pan(0.0, 0.0, "voice3")
    $ renpy.music.set_pan(0.0, 0.0, "voice4")
    play voice3 stacy_hey noloop
    scene d16s01-06-sy-talking-with-mc with dissolve
    sy "Oh, would you look at that. The man of the hour is awake as well. Perfect timing."
    play voice2 d7s6_moan2 noloop
    scene d16s01-07-mc-yawns-and-stretches
    if cage_ntr is False:
        show d16s01-07-mc-yawns-and-stretches-2
    with dissolve
    pause
    scene d16s01-08-mc-looking-at-arj-sy with dissolve
    pause
    play voice3 aaleyah_disappointed_mff2 noloop
    play voice4 dahlia_disappointed_ehh3 noloop
    scene d16s01-09-sy-arj-yawns with dissolve
    sy "**Yawns**"
    scene d16s01-10-mc-talking-with-arj-sy with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "You two didn't get a lick of sleep last night, did you?"
    scene d16s01-11-sy-talking-with-mc with dissolve
    play voice3 stacy_yes noloop
    sy "Yes we did!"
    scene d16s01-12-arj-talking-with-mc with dissolve
    play voice4 amrose_yes_yeah2 noloop
    arj "We were too hyped up to sleep. So we decided to put that energy to use and keep working on the thing."
    scene d16s01-13-sy-talking-with-mc with dissolve
    play voice3 stacy_laugh4 noloop
    sy "Working title: {b}Fetish-Locator-Locator-Inator™{/b}."
    scene d16s01-14-arj-talking-with-mc with dissolve
    play voice4 amrose_thinking_emm noloop
    arj "...We need some more R&D on that one."
    scene d16s01-15-mc-comes-closer with dissolve
    play sound sfx_keyboard_typing2
    arj "The hardware side of things is finally done."
    scene d16s01-16-arj-talking-with-mc with dissolve
    arj "Fixed up the power drain issue and hacked together some lithium-ions as the power supply."
    scene d16s01-18-arj-looking-at-sy with dissolve
    play voice4 amrose_arrogant_hmm2 noloop
    arj "This thing can probably last for a week on one charge {i}and{/i} you don't need to lug around huge batteries."
    scene d16s01-17-sy-talking-with-mc
    if cage_ntr is False:
        show d16s01-17-sy-talking-with-mc-2
    with dissolve
    play voice3 stacy_yay noloop
    sy "With only a 36.72%% chance of blowing up in your face!"
    scene d16s01-19-arj-talking-with-mc with dissolve
    play voice4 amrose_yes_yap noloop
    arj "I'm pretty proud of it if I do say so myself."
    scene d16s01-20-mc-talking-with-arj with dissolve
    play voice2 mc_surprised_wow2 noloop
    mc "Woah, you should be. This is great!"
    scene d16s01-21-mc-talking-with-arj with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Maybe we can even make these on a commercial scale after we take care of Fetish Locator."
    scene d16s01-22-arj-talking-with-mc with dissolve
    play voice4 amrose_thinking_hmm1 noloop
    arj "Hm... Maybe, but that's only one half of the puzzle."
    scene d16s01-23-sy-talking-with-mc
    if cage_ntr is False:
        show d16s01-23-sy-talking-with-mc-2
    with dissolve
    play voice3 stacy_hmm noloop
    sy "Right."
    scene d16s01-24-sy-talking-with-mc with dissolve
    sy "The magic sauce is right here."
    scene d16s01-25-sy-talking-with-mc with dissolve
    sy "This baby will allow the Fetish-Locator-Locator-Inator™ to masquerade as a legitimate network."
    scene d16s01-26-sy-talking-with-mc with dissolve
    play voice3 stacy_mmm1 noloop
    sy "Give me your phone."
    scene d16s01-29-mc-talking-with-sy with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Are you sure that it is ready?"
    scene d16s01-28-sy-talking-with-mc with dissolve
    play voice3 stacy_laugh3 noloop
    sy "Let's find out."
    play sound sfx_phone_tapping1 volume 4.2
    scene d16s01-27-sy-fiddles-around-on-the-phone with dissolve
    pause
    scene d16s01-28-sy-talking-with-mc with dissolve
    play voice3 stacy_mmm2 noloop
    sy "Alright, it's done."
    scene d16s01-29-mc-talking-with-sy with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "What did you do?"
    scene d16s01-30-sy-talking-with-mc with dissolve
    play voice3 stacy_hmm noloop
    sy "I connected your phone to the Fetish-Locator-Locator-Inator™ network."
    sy "Basically, Fetish-Locator-Locator-Inator™ allows you to use and connect to the internet, but all traffic that you send and receive gets logged into it."
    scene d16s01-31-sy-talking-with-mc-arj with dissolve
    sy "Meaning that when Fetish Locator sends anything to you or receives anything from you, the Fetish-Locator-Locator-Inator™ secretly writes all that info down."
    sy "And Fetish Locator is none-the-wiser because, from its perspective, it's just a normal network. Nothing weird going on here."
    scene d16s01-32-mc-talking-with-sy with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "That's great. So all I have to do is just connect to Fetish Locator and we'll get its location?"
    scene d16s01-33-sy-talking-with-mc with dissolve
    play voice3 stacy_upset1 noloop
    sy "Well... It's a bit more complicated than that."
    scene d16s01-34-arj-talking-with-mc with dissolve
    play voice4 amrose_yes_ugu noloop
    arj "We tried it out last night on my phone.{w} It didn't work."
    scene d16s01-35-mc-talking-with-arj with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "What do you mean?"
    scene d16s01-36-arj-talking-with-mc with dissolve
    play voice4 amrose_arrogant_hmm2 noloop
    arj "All of Fetish Locator's network packets are encrypted."
    scene d16s01-37-mc-talking-with-arj with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Shit."
    scene d16s01-38-sy-talking-with-mc with dissolve
    sy "Yeep."
    scene d16s01-39-mc-talking-with-sy with dissolve
    mc "They must've {i}really{/i} not wanted anyone snooping around."
    scene d16s01-40-sy-talking-with-mc with dissolve
    play voice3 stacy_angry noloop
    sy "Well, I don't know if it was intentional or not. They could've just been following modern networking standards as well. But anyway, that's not important."
    scene d16s01-41-mc-talking-with-sy with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Still, what do we do about that then? Or are we just dead in the water?"
    scene d16s01-42-sy-talking-with-mc with dissolve
    play voice3 amrose_arrogant_pff noloop
    sy "Pish, have at least a {i}little{/i} confidence in us, [mcname]."
    sy "This is what I was working on all night long."
    scene d16s01-38-sy-talking-with-mc with dissolve
    sy "Basically, along with logging all incoming and outgoing data from Fetish Locator, Fetish-Locator-Locator-Inator™ also tries to decrypt the data."
    scene d16s01-40-sy-talking-with-mc with dissolve
    play voice3 stacy_mmm2 noloop
    sy "The problem, however, is that we're trying to brute-force our way in and uh... It's not fast, to say the least."
    scene d16s01-43-mc-talking-with-sy with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What do you mean?"
    scene d16s01-44-arj-talking-with-mc with dissolve
    play voice4 amrose_arrogant_huh3 noloop
    arj "What she's saying is that we need a lot of data from Fetish Locator and an unknown amount of time to crack the encryption."
    scene d16s01-45-mc-talking-with-arj with dissolve
    play voice2 mc_scared_oh3 noloop
    mc "\"Unknown\"?"
    scene d16s01-46-sy-talking-with-mc with dissolve
    play voice3 stacy_hmm noloop
    sy "Bruteforcing these sorts of encryptions take a lot of time. And we can't really predict how long it'll take."
    sy "It could work the moment you open FL, it could take months..."
    scene d16s01-47-arj-talking-with-mc with dissolve
    play voice4 amrose_thinking_hmm2 noloop
    arj "Still, this is our best chance."
    scene d16s01-48-sy-talking-with-mc with dissolve
    sy "Yeah. And I don't necessarily think that it'll take a super long time to crack."
    sy "But the uncertainty sucks."
    scene d16s01-49-mc-talking-with-sy with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "There's no point getting dejected."
    mc "We got something that might actually work here."
    scene d16s01-51-mc-talking-with-sy with dissolve
    mc "So we should try to give it as much as we can first."
    play voice2 mc_arrogant_huh1 noloop
    mc "Speaking of which. What kind of data do we need to give it?"
    scene d16s01-50-mc-talking-with-sy with dissolve
    mc "I'm guessing I can't just open and close the app a bunch of times and be done with it?"
    scene d16s01-52-sy-talking-with-mc with dissolve
    play voice3 stacy_yeahno noloop
    sy "Yeah, no. You need different kinds of data."
    sy "The same stuff over and over again won't help."
    scene d16s01-53-arj-talking-with-mc with dissolve
    play voice4 amrose_yes_yap noloop
    arj "So, complete challenges, buy stuff, and just interact with Fetish Locator as much as you can I suppose."
    arj "More points equal more chances to decrypt it."
    scene d16s01-55-mc-talking-with-arj-sj
    if cage_ntr is False:
        show d16s01-55-mc-talking-with-arj-sj-2
    with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Alright. Well, that doesn't sound all that bad."
    mc "I have to do that regardless."
    mc "Would be a hell of a lot easier if I didn't have to lug a cock cage around though."
    scene d16s01-56-sy-talking-with-mc with dissolve
    play voice3 stacy_laugh4 noloop
    sy "I'm sure you have plenty of other...{i}instruments{/i} that you can use to make it work."
    scene d16s01-58-arj-talking-with-mc with dissolve
    play voice4 amrose_yes_yeah1 noloop
    arj "Yeah. So we can just have that running in the background and try to figure out if we have any other options when it comes to Fetish Locator as well."
    scene d16s01-62-arj-talking-with-mc with dissolve
    play voice4 amrose_surprised_ahh2 noloop
    arj "Crap."
    scene d16s01-54-mc-talking-with-arj with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "Everything alright?"
    scene d16s01-57-arj-talking-with-mc with dissolve
    play voice4 amrose_yes_yeah3 noloop
    arj "Yeah, but I should really get going. I need to get to class."
    scene d16s01-59-mc-talking-with-arj with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "Right, fuck. Me too."
    mc "I need to wash up first though. Can you wait for me?"
    scene d16s01-60-arj-talking-with-mc with dissolve
    play voice4 amrose_yes_okay1 noloop
    if d14s03_arj_kiss is True:
        arj "Of course!"
    elif True:
        arj "Sure."
    scene d16s01-63-a1 mc-tosses-flli-to-sy-glambot-1-000_i with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Stacy, catch!"
    $ renpy.music.set_volume(1.0, 0.0, "sound2")
    play sound ["<silence 1.0>", sfx_camera_fly1]
    play sound2 ["<silence 3.0>", sfx_camera_fly1] noloop
    play voice3 ["<silence 3.2>", stacy_impressed] noloop
    scene d16s01_sy_mc_catch with dissolve
    pause
    scene d16s01-64-sy-talking-with-mc with dissolve
    play voice3 stacy_hey noloop
    sy "Hey! Be careful!"
    scene d16s01-65-mc-talking-with-arj with dissolve
    play voice2 mc_happy_hah1 noloop
    mc "I knew you'd catch it."
    mc "I'll be out in a bit!"
    scene d16s01-67-sy-talking-with-mc with dissolve
    play voice3 polly_angry noloop
    sy "Jackass."

    jump d16s02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
