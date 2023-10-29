

default persistent.ignore_mp_fail = False
default persistent.mp_info = ""

label splashscreen:

    if not renpy.loadable("images/Day-15/Scene-01/d15s01-01 mc-morning1.webp"):
        call screen patch_info()

    $ renpy.music.set_volume(volume=0.3, delay=0, channel="music" )
    $ renpy.music.set_volume(volume=0.3, delay=0, channel="music2")
    $ renpy.music.set_volume(volume=0.3, delay=0, channel="sound" )
    $ renpy.music.set_volume(volume=0.3, delay=0, channel="sound2")
    $ create_persistent_gallery_if_non_existent()
    play music config.main_menu_music
    scene black
    $ renpy.pause(0.5)
    show team-logo with Fade(0.6, 0.4, 0.6)
    $ renpy.pause(3.5)
    scene black
    show fl-loading-logo:
        xalign 0.5 yalign 0.5
    with Fade(0.6, 0.4, 0.6)
    $ renpy.pause(3.5)
    scene black
    show screen disclaimer()
    with Fade(0.6, 0.4, 0.6)
    pause
    hide screen disclaimer with dissolve
    if FLSS.mp is None or FLSS.is_inited is False:
        if persistent.ignore_mp_fail is False:
            jump failed_mp
    elif True:
        $ persistent.mp_info = ""
    if not persistent.chose_lang:
        call screen language_chooser_splash
    return



label start:

    stop music fadeout 2.0
    show screen fl_points_screen(0, False)

    jump prologue_fresh_start

label continue_from_previous_week:

    scene black
    stop music fadeout 1.0
    $ FLSS.mp_load(persistent.mp_slot)
    $ persistent.mp_slot = None
    show screen fl_points_screen(0, False)

    $ renpy.jump(FLSS.week.landing_label)

label end:

    $ quick_menu = False

    scene black with dissolve
    pause(0.5)

    $ check_finished_endings()

    jump end_credits

label failed_mp:

    scene black
    call screen mp_fail()
    with dissolve

    $ renpy.quit()



image fl_will_return = Text(_("The legendary Fetish Locator will return"), style="credit_start_text")

image after_credits_glambot_a1 = Movie(play = "images/Day-21/s25/anim/d21s25-a1-2x-50fps.webm", start_image = "d21s25-a1 sy-opening-anim-1", image = "d21s25-a1 sy-opening-anim-1-99", loop = False)
image after_credits_a116_1 = Movie(play = "images/Day-21/s25/anim/d21s25-a116-1-2x-50fps.webm", start_image = "d21s25-a116-1 sy-dd-zp-zp-1sm-jh-lw-talking-01")
image after_credits_a116_1_f = Movie(play = "images/Day-21/s25/anim/d21s25-a116-1-2x-60fps.webm", start_image = "d21s25-a116-1 sy-dd-zp-zp-1sm-jh-lw-talking-01")
image after_credits_a116_2 = Movie(play = "images/Day-21/s25/anim/d21s25-a116-2-2x-50fps.webm", start_image = "d21s25-a116-2 sy-dd-zp-zp-1sm-jh-lw-talking-01")
image after_credits_a116_2_f = Movie(play = "images/Day-21/s25/anim/d21s25-a116-2-2x-60fps.webm", start_image = "d21s25-a116-2 sy-dd-zp-zp-1sm-jh-lw-talking-01")
image after_credits_a116_3 = Movie(play = "images/Day-21/s25/anim/d21s25-a116-3-2x-50fps.webm", start_image = "d21s25-a116-3 sy-dd-zp-zp-1sm-jh-lw-talking-01")
image after_credits_a116_3_f = Movie(play = "images/Day-21/s25/anim/d21s25-a116-3-2x-60fps.webm", start_image = "d21s25-a116-3 sy-dd-zp-zp-1sm-jh-lw-talking-01")

label after_credits:

    $ _skipping = True
    stop music fadeout 3.5
    scene black with dissolve
    pause(2.0)

    $ renpy.music.set_volume(1.0, 0.0, "music2")
    play music2 music_aftertitles_intro
    play sound sfx_camera_fly1 volume 1.5
    scene after_credits_glambot_a1 with dissolve
    pause
    play voice3 stacy_huh noloop
    scene d21s25-02 sy-opening with dissolve
    pause
    scene d21s25-03 sy-opening with dissolve
    pause
    play voice3 stacy_upset1 noloop
    scene d21s25-04 sy-where-am-i_c1 with dissolve
    pause
    scene d21s25-05 sy-summon-dd_c1 with dissolve
    play voice3 stacy_mmm1 noloop
    sy "What the...?"
    scene d21s25-05 sy-summon-dd_c2 with dissolve
    pause
    $ renpy.music.set_volume(0.5, 0.0, "music")
    play music music_aftertitles_daisy fadein 3.0
    stop music2 fadeout 4.0
    play sound sfx_magic_disappear2 volume 1.4
    scene d21s25-06 sy-summon-dd-2_c1 with image_dissolve_d21s25_01_3
    pause
    scene d21s25-07 sy-dd-talk-fl_c1 with dissolve
    play voice3 stacy_names_daisy_happy noloop
    sy "Daisy!"
    scene d21s25-07 sy-dd-talk-fl_c2 with dissolve
    play voice4 daisy_hey noloop
    dd "Heya! Nice to see ya!"
    scene d21s25-08 sy-dd-talk-fl-2_c1 with dissolve
    play voice3 stacy_laugh4 noloop
    sy "You're wearing our outfit!"
    scene d21s25-08 sy-dd-talk-fl-2_c2 with dissolve
    play voice4 daisy_aga noloop
    dd "Oh... Huh, I guess I am..."
    scene d21s25-09 sy-dd-talking with dissolve
    if persistent.finished_e01 is True:
        play voice4 daisy_hmm1 noloop
        dd "Which reminds me! Congrats on getting your ending!"
        scene d21s25-10 sy-dd-happy with dissolve
        play voice3 stacy_happy_yay1 noloop
        sy "Thank you! Honestly, I'm so happy I almost can't believe it!"
    elif True:
        play voice4 daisy_hmm1 noloop
        dd "Which reminds me! I haven't played your ending yet, is it good?"
        scene d21s25-12 sy-dd-surprised with dissolve
        play voice3 stacy_surprised_huh1 noloop
        sy "Whaaat!? Girl, you absolutely gotta get it ASAP. It's the best ending!"
        scene d21s25-13 sy-dd-talking with dissolve
        play voice4 daisy_haha noloop
        dd "Hm... I feel like you're being biased, but I don't know... *Laughs*"
        dd "Okay, okay, I will! Do you have any hints for me, though?"
        scene d21s25-14 sy-dd-talking with dissolve
        play voice3 stacy_no_uhuh4 noloop
        sy "Nuh-uh. You have to find out everything by yourself. I can't spoil it!"
        scene d21s25-15 sy-dd-talking with dissolve
        play voice3 amrose_old_psst2 noloop
        sy "But I'll say this, {i}you learn about some {b}very important{/b} things in it.{/i}"

    scene d21s25-16 sy-dd-anyway with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "Anyway, about your ending, though!"
    if persistent.finished_e11 is False:
        scene d21s25-17 sy-dd-sad with dissolve
        play voice4 daisy_oof noloop
        dd "Oh, well, I haven't seen it yet sadly."
        scene d21s25-28 sy-dd-talking with dissolve
        play voice3 stacy_disappointed_oh5 noloop
        sy "Aw, that's alright. Maybe we can experience it together then."
    elif True:
        scene d21s25-19 sy-dd-sad with dissolve
        play voice3 stacy_pain_au1 noloop
        sy "It is so sad! I thought you died."
        scene d21s25-20 sy-dd-crying with dissolve
        play voice3 allison_pain_sniff1 noloop
        sy "*sniffs*"
        play sound sfx_cloth_rustling4 volume 2.0
        scene d21s25-21 sy-dd-hugging with dissolve
        pause
        scene d21s25-22 sy-dd-talking with dissolve
        play voice4 daisy_oof noloop
        dd "Hey, it's okay. I'm healthy as a clam now."
        scene d21s25-24 sy-dd-wiping-tears with dissolve
        play voice3 stacy_angry_fuck1 noloop
        sy "*Sniffling* I know. *sniff* I'm glad you're okay."
        scene d21s25-25 sy-dd-smiling with dissolve
        play voice4 aaleyah_disappointed_mff2 noloop
        dd "Mmmhmm. Me too, Stacy."
        scene d21s25-26 sy-dd-smiling with dissolve
        if persistent.finished_e04 is True:
            play voice4 daisy_impressed noloop
            dd "And don't forget. There's is another ending with me!"
            scene d21s25-27 sy-dd-smiling with dissolve
            play voice3 stacy_oh2 noloop
            sy "Oh...right."
            play sound sfx_cloth_rustling2 volume 1.6
            scene d21s25-28 sy-dd-talking with dissolve
            play voice3 stacy_angry noloop
            sy "I almost forgot about the Sex Dungeon ending!"
        elif True:
            play voice4 daisy_impressed noloop
            dd "Don't forget about our other ending, Stacy. I get to be a hot, latex, sex doll in our own Sex Dungeon!"
            scene d21s25-27 sy-dd-smiling with dissolve
            play voice3 stacy_oh2 noloop
            sy "Yeah... That ending sounds like fun."
            play sound sfx_cloth_rustling2 volume 1.6
            scene d21s25-28 sy-dd-talking with dissolve
            play voice2 stacy_thinking_hm1 noloop
            sy "I can't wait to enjoy it with you."

    play sound sfx_memory_back4 volume 1.5
    scene d21s25-29 sy-dd-zp-enter with image_dissolve_d21s25_02_2
    pause
    scene d21s25-30 sy-dd-zp-talking with dissolve
    play voice5 postcredit_girl1_huh noloop
    zp "Ending?"
    scene d21s25-31 sy-dd-zp-talking with dissolve
    play voice4 daisy_hey noloop
    dd "Zemfira! Hey, girl!"
    scene d21s25-32 sy-dd-zp-talking with dissolve
    play voice3 stacy_thinking_hmm4 noloop volume 1.0
    sy "Wait, you know her?"
    scene d21s25-33 sy-dd-zp-talking with dissolve
    play voice4 daisy_yes noloop
    dd "Yeah, she is from Taboo University!"
    scene d21s25-34 sy-dd-zp-talking with dissolve
    play voice5 postcredit_girl1_yeah noloop
    zp "Uh, yeah. That's right."
    play sound sfx_magic_disappear1 volume 1.7
    scene d21s25-35 sy-dd-zp-sm-enter with image_dissolve_d21s25_03
    pause
    play voice6 postcredit_girl3_hey2 noloop
    sm "Me too!"
    scene d21s25-36 sy-dd-zp-sm-talking with dissolve
    play voice5 postcredit_girl1_surprised_ou noloop
    zp "Silvia? You're here as well?"
    scene d21s25-37 sy-dd-zp-sm-talking with dissolve
    play voice6 postcredit_girl3_yes_yap2 noloop
    sm "Of course!"
    scene d21s25-38 sy-dd-zp-sm-talking with dissolve
    play voice6 postcredit_girl3_hey noloop
    sm "Hey, nice to meet you all!"
    if persistent.finished_e01 is True:
        scene d21s25-39 sy-dd-zp-sm-congratulating with dissolve
        play voice6 postcredit_girl3_haha2 noloop
        sm "Congrats on finally opening up the S&M Studio, by the way!"
        scene d21s25-40 sy-dd-zp-sm-thanking with dissolve
        play voice3 stacy_happy_yay2 noloop
        sy "Thanks! I am {i}so{/i} looking forward to it!"
        scene d21s25-41 sy-dd-zp-sm-confused with dissolve
        play voice5 postcredit_girl1_angry_huh noloop
        zp "S and what? I haven't played that yet."
        scene d21s25-42 sy-dd-zp-sm-talking with dissolve
        play voice4 daisy_aah noloop
        dd "Well, looks like our little Stacy will get her own game! \"Fetish Locator: S&M Studio\""
        scene d21s25-43 sy-dd-zp-sm-impressed with dissolve
        play voice5 postcredit_girl1_surprised_wow1 noloop
        zp "Huh, that's pretty cool. I've always wanted my own game."
        scene d21s25-44 sy-dd-zp-sm-curious with dissolve
        zp "When's it coming out?"
        scene d21s25-45 sy-dd-zp-sm-talking with dissolve
        play voice3 stacy_thinking_well1 noloop
        sy "Not sure yet. Though the ViNovella team is already hard at work on it."
        sy "I've already had some sneak peaks of the stuff they planned for. It's gonna be amazing!"
        scene d21s25-46 sy-dd-zp-sm-talking with dissolve
        play voice6 postcredit_girl3_pff noloop
        sm "C'mon! You gotta share some of it with us!"
        scene d21s25-47 sy-dd-zp-sm-talking with dissolve
        play voice5 postcredit_girl1_yes_yeah2 noloop
        zp "Yeah."
        scene d21s25-48 sy-dd-zp-sm-unsure with dissolve
        play voice3 stacy_thinking_emm1 noloop
        sy "I-I promised not to tell anyone!"
        scene d21s25-49 sy-dd-zp-sm-convincing with dissolve
        play voice4 lissa_ha noloop
        dd "Well... I'm sure they won't be too mad if you share a {i}little{/i}."
        scene d21s25-50 sy-dd-zp-sm-convinced with dissolve
        play voice3 stacy_yes_fine3 noloop
        sy "*Sigh* Alright, alright. I've met some of the new characters..."
        stop music fadeout 4.0
        play sound ["<silence 0.2>", sfx_nondiegetic_transition_1]
        scene d21s25-50-02 sy-dd-zp-sm-convinced with image_dissolve_d21s25_04_2
        pause
        scene d21s25-51 sy-poof-to-studio with dissolve
        pause
        play sound sfx_light_podium_1
        play music2 "<silence 0.2>" noloop
        queue music2 music_aftertitles_showcase
        scene d21s25-51-02 sy-transition with dissolve
        pause
        play sound sfx_light_podium_2
        scene d21s25-51-03 sy-transition with dissolve
        pause
        play sound sfx_light_podium_3
        scene d21s25-51-04 sy-transition with dissolve
        pause
        play sound sfx_light_podium_2
        scene d21s25-51-05 sy-transition with dissolve
        pause
        play sound sfx_light_podium_1
        scene d21s25-51-06 sy-transition with dissolve
        pause
        play sound sfx_light_podium_3
        scene d21s25-51-07 sy-transition with dissolve
        pause
        scene d21s25-52 sy-happy with dissolve
        play voice3 stacy_arrogant_huh5 noloop
        sy "Here are some of our amazing girls!"
        scene d21s25-53 sy-introduction-time with dissolve
        play sound sfx_photocamera_flash2
        play voice3 stacy_happy_relief1 noloop
        sy "This is Arlene!"
        scene d21s25-54 sy-introduction-time with dissolve
        play sound sfx_photocamera_flash2
        pause
        scene d21s25-54-02 sy-introduction-time with dissolve
        pause
        scene d21s25-55 sy-introduction-time with dissolve
        play voice3 polly_aga noloop
        play sound sfx_photocamera_flash2
        sy "Here's Jenny!"
        scene d21s25-56 sy-introduction-time with dissolve
        play voice3 polly_laughter noloop
        sy "This is Elizabeth!"
        play sound sfx_photocamera_flash2
        scene d21s25-57 sy-introduction-time with dissolve
        pause
        scene d21s25-58 sy-introduction-time with dissolve
        pause
        scene d21s25-59 sy-introduction-time with dissolve
        play voice3 stacy_thinking_hmm1 noloop
        play sound sfx_photocamera_flash2
        sy "Here's Clare!"
        scene d21s25-60 sy-introduction-time with dissolve
        play voice3 stacy_thinking_hmm3 noloop
        sy "Meet Kellie!"
        scene d21s25-61 sy-introduction-time with dissolve
        play sound sfx_photocamera_flash2
        pause
        scene d21s25-62 sy-introduction-time with dissolve
        play voice3 stacy_happy_laugh3 noloop
        sy "And last - but not least - Eleonora!"
        scene d21s25-63 sy-introduction-time with dissolve
        play sound sfx_photocamera_flash2
        pause
        scene d21s25-64 sy-tossing-her-camera with dissolve
        pause
        play voice3 stacy_happy_wooh1 noloop
        scene d21s25-65 sy-tossing-her-camera with dissolve
        pause
        play sound sfx_photocamera_flash1 volume 1.5
        with Fade(0.25, 0.0, 0.7, color="#fff")
        play sound sfx_memory_in4
        scene d21s25-66 sy-dd-zp-sm-back-to-void with image_dissolve_2
        pause
        scene d21s25-67 sy-dd-zp-sm-camera-montage with dissolve
        pause
        play sound sfx_remote_button1 volume 3.0
        scene d21s25-67-02 sy-dd-zp-sm-camera-montage with dissolve
        pause
        play sound sfx_remote_button1 volume 3.0
        scene d21s25-67-03 sy-dd-zp-sm-camera-montage with dissolve
        pause
        play sound sfx_remote_button1 volume 3.0
        scene d21s25-67-04 sy-dd-zp-sm-camera-montage with dissolve
        pause
        play sound sfx_remote_button1 volume 3.0
        scene d21s25-67-05 sy-dd-zp-sm-camera-montage with dissolve
        pause
        play sound sfx_remote_button1 volume 3.0
        scene d21s25-68 sy-dd-zp-sm-camera-montage with dissolve
        pause
        $ renpy.music.set_volume(0.65, 2.5, "music2")
        scene d21s25-69 sy-dd-zp-sm-excited with dissolve
        play voice6 postcredit_girl3_surprised_wow1 noloop
        sm "Woah, so many already! I'm looking forward to meeting them all!"
        scene d21s25-70 sy-dd-zp-sm-excited with dissolve
        play voice3 stacy_yay noloop
        sy "I know! I can't wait to see what ViNovella has prepared for us next!"
        scene d21s25-71 sy-dd-zp-sm-excited with dissolve
        play voice4 daisy_hmm1 noloop
        dd "But what about Taboo University though?"
    elif True:
        scene d21s25-71 sy-dd-zp-sm-excited with dissolve
        play voice4 daisy_hey noloop
        dd "Hey, Nice to meet you too!"
        dd "How is Taboo University going? What's next?"
    scene d21s25-72 sy-dd-zp-sm-curious with dissolve
    play voice6 postcredit_girl3_surprised_ou noloop
    sm "Oh? Have you played TU?"
    scene d21s25-73 sy-dd-zp-sm-happy with dissolve
    play voice4 daisy_yay noloop
    dd "Yeah! I love it! Nia's story is my favorite. That group of hers seem so spooky..."
    scene d21s25-74 sy-dd-zp-sm-kidding with dissolve
    play voice5 postcredit_girl1_arrogant_hah noloop
    zp "Hah! Yeah. I wish I could fuck up that Andre prick though."
    scene d21s25-75 sy-dd-zp-sm-laughing with dissolve
    play voice6 postcredit_girl3_haha2 noloop
    sm "*Laughs*"
    scene d21s25-76 sy-dd-zp-sm-talking with dissolve
    play voice5 postcredit_girl1_geh noloop
    sm "Nia wanted to join us today as well, but she was busy because they are making her scenes right now."
    scene d21s25-77 sy-dd-zp-sm-talking with dissolve
    play voice4 daisy_oof noloop
    dd "Aw, I was dying to meet her!"
    if persistent.finished_e11 is True:
        scene d21s25-78 sy-dd-zp-sm-talking-ddending with dissolve
        dd "Literally."
        play voice3 stacy_happy_laugh4 noloop
        play voice6 postcredit_girl3_haha noloop
        play voice5 postcredit_girl1_happy_laugh3 noloop
        scene d21s25-79 sy-dd-zp-sm-laughing with dissolve
        pause
        scene d21s25-80 sy-dd-zp-sm-laughing with dissolve
        play voice3 stacy_happy_phew3 noloop
        sy "*Laughs* You {i}cannot{/i} joke about that. That's awful."
        scene d21s25-81 sy-dd-zp-sm-laughing with dissolve
        play voice4 daisy_laugh noloop volume 1.5
        dd "*Laughs* Sorry! Couldn't help myself."
    scene d21s25-82 sy-dd-zp-sm-talking with dissolve
    play voice3 stacy_hey_happy2 noloop
    sy "Do you two know when there'll be a finished version of TU available? I wanna binge it."
    scene d21s25-83 sy-dd-zp-sm-talking with dissolve
    play voice5 postcredit_girl1_thinking_hmm2 noloop
    zp "Well, I heard from the grapevine that Vi is planning to finish Book-1 during 2024, but there isn't anything concrete yet."
    scene d21s25-84 sy-dd-zp-sm-talking with dissolve
    play voice3 stacy_surprised_oh1 noloop
    sy "Oh? Wait, so is Book-1 like Week-1 in Fetish Locator?"
    scene d21s25-85 sy-dd-zp-sm-talking with dissolve
    play voice6 postcredit_girl3_ehh noloop
    sm "Close. Each TU book will be {i}much{/i} bigger than an FL Week."
    scene d21s25-86 sy-dd-zp-sm-talking with dissolve
    play voice3 stacy_arrogant_huh4 noloop
    sy "Woah, that sounds like it's gonna be something. I hope you guys do well!"
    sy "I definitely should {a=steam://openurl/https://store.steampowered.com/app/2459350/Taboo_University_Book_One/}{u}wishlist the game on Steam{/u}{/a} then!"
    play music sfx_music_shutdown1
    stop music2 fadeout 1.0
    scene d21s25-86-02 sy-dd-zp-sm-location-change with image_dissolve_d21s25_05
    queue music music_aftertitles_finish
    pause
    scene d21s25-87 sy-dd-zp-sm-bouldering-club with dissolve
    pause
    scene d21s25-88 sy-dd-zp-sm-jh-bouldering-club with dissolve
    pause
    scene d21s25-89 sy-dd-zp-sm-jh-talking with dissolve
    play voice4 postcredit_girl4_hey_happy1 noloop
    jh "Hey, guys!"
    scene d21s25-91 sy-dd-zp-sm-jh-landing with dissolve
    play voice5 postcredit_girl3_surprised_ou noloop
    sm "Oh! Hey, Josie!"
    play sound sfx_epic_kick2
    scene d21s25-90 sy-dd-zp-sm-jh-releasing-hang with dissolve
    pause
    play sound sfx_kick_leg1 volume 1.4
    scene d21s25-92 sy-dd-zp-sm-jh-everyone-shocked with vpunch
    pause
    play voice4 postcredit_girl4_happy_wooh1 noloop
    jh "Lara! Look who's here!"
    scene d21s25-93 sy-dd-zp-sm-jh-lw-peeking with dissolve
    play voice6 postcredit_girl5_hey_sexy1 noloop
    lw "Oh, hey."
    scene d21s25-94 sy-dd-zp-sm-jh-lw-peeking with dissolve
    play voice6 postcredit_girl5_angry_hmm1 noloop
    lw "I'm gonna jump! Clear out!"
    scene d21s25-95 sy-dd-zp-sm-jh-lw-talking with dissolve
    pause
    scene d21s25-96 sy-dd-zp-sm-jh-lw-talking with dissolve
    play voice4 postcredit_girl4_yes_aga2 noloop
    jh "You're good!"
    play sound sfx_epic_jump1
    scene d21s25-97 sy-dd-zp-sm-jh-lw-jumping with dissolve
    pause
    play sound sfx_epic_jump2
    scene d21s25-98 sy-dd-zp-sm-jh-lw-landing with vpunch
    pause
    scene d21s25-99 sy-dd-zp-sm-jh-lw-talking with dissolve
    play voice3 stacy_surprised_wow1 noloop
    sy "Wow! You're amazing!"
    scene d21s25-100 sy-dd-zp-sm-jh-lw-talking with dissolve
    play voice6 postcredit_girl5_happy_laugh8 noloop
    lw "Thank you. It's nice to meet you."
    scene d21s25-101 sy-dd-zp-sm-jh-lw-talking with dissolve
    play voice3 stacy_yes_yap1 noloop
    sy "Nice to meet you too. I'm Stacy!"
    scene d21s25-102 sy-dd-zp-sm-jh-lw-talking with dissolve
    play voice4 postcredit_girl4_arrogant_ha2 noloop
    jh "Lara's a huge fan of yours! You two remind me of each other sometimes *Laughs*"
    scene d21s25-103 sy-dd-zp-sm-jh-lw-looking-for-lyssa with dissolve
    play voice6 postcredit_girl5_arrogant_heh2 noloop
    lw "Is Lyssa here? Josie was gushing about her."
    scene d21s25-104 sy-dd-zp-sm-jh-lw-looking-for-lyssa with dissolve
    play voice4 postcredit_girl4_angry_argh1 noloop
    jh "Lara!"
    scene d21s25-105 sy-dd-zp-sm-jh-lw-blushing with dissolve
    play voice4 postcredit_girl4_yes_yeah2 noloop
    jh "Well, I mean, yes. I would've loved to meet Lyssa... She's just really cool!"
    play voice5 postcredit_girl1_geh noloop
    play voice6 postcredit_girl3_pff noloop
    scene d21s25-106 sy-dd-zp-sm-jh-lw-reacting with dissolve
    pause
    scene d21s25-107 sy-dd-zp-sm-jh-lw-reacting with dissolve
    play voice3 stacy_huh2 noloop
    sy "{size=25}What's their deal? Are they a part of the groups and whatnot?{/size}"
    scene d21s25-108 sy-dd-zp-sm-jh-lw-reacting with dissolve
    play voice4 daisy_thinking noloop volume 1.8
    dd "{size=25}Oh, they are the roommates of the main guy.{/size}"
    dd "{size=25}Josie had an old crush on him and that's now sparking up again, and Lara is very protective of Josie and not really trusting of the guy. But he's growing on her slowly.{/size}"
    dd "{size=25}Honestly, this love triangle is my favorite part of the game!{/size}"
    scene d21s25-109 sy-dd-zp-sm-jh-lw-reacting with dissolve
    play voice5 postcredit_girl1_hey_angry noloop
    zp "Hey!"
    scene d21s25-110 sy-dd-zp-sm-jh-lw-reacting with dissolve
    play voice4 daisy_yay2 noloop
    dd "Sorry! I love all the parts, but Josie and Lara are just so sweet!"
    play sound sfx_reminiscence_gone volume 1.4 fadein 2.3
    scene d21s25-110-02 sy-dd-location-changed with image_dissolve_d21s25_06_4
    pause
    scene d21s25-111 sy-dd-zp-sm-jh-lw-location-changed with dissolve
    pause
    scene d21s25-a116-1 sy-dd-zp-zp-1sm-jh-lw-talking-01 with dissolve
    pause
    play voice3 aaleyah_sucking_deep fadein 1.5
    scene after_credits_a116_1
    pause
    scene after_credits_a116_2 with dissolve
    pause
    scene after_credits_a116_3 with dissolve
    pause
    scene after_credits_a116_1_f with dissolve
    pause
    scene after_credits_a116_2_f with dissolve
    pause
    scene after_credits_a116_3_f with dissolve
    pause
    scene d21s25-112 sy-dd-zp-sm-jh-lw-talking with dissolve
    play voice5 postcredit_girl1_angry_huh noloop
    zp "Delphia?"
    stop voice3 fadeout 1.0
    scene d21s25-113 sy-dd-zp-1sm-jh-lw-reacting with dissolve
    play voice5 samiya_mfff3 noloop
    pause
    scene d21s25-114 sy-dd-zp-1sm-jh-lw-reacting with dissolve
    play voice6 postcredit_girl6_thinking_hm3 noloop
    dk "Hm? What are you doing here?"
    scene d21s25-115 sy-dd-zp-1sm-jh-lw-reacting with dissolve
    play voice4 postcredit_girl3_haha noloop
    sm "They just finished Fetish Locator! This is the post-credit scene!"
    sm "What are {i}you{/i} doing here?"
    scene d21s25-116 sy-dd-zp-1sm-jh-lw-talking with dissolve
    play voice5 samiya_mfff2 noloop
    edo "Mmgghhh-oo!"
    scene d21s25-117 sy-dd-zp-1sm-jh-lw-talking with dissolve
    play voice4 postcredit_girl6_thinking_oh noloop
    dk "Oh, whoops!"
    play sound sfx_spitcum1
    scene d21s25-118 sy-dd-zp-1sm-jh-lw-talking with dissolve
    play voice4 postcredit_girl6_arrogant_hm noloop
    dk "We were just uhm...preparing for the next scene."
    scene d21s25-119 sy-dd-zp-1sm-jh-lw-talking with dissolve
    play voice4 postcredit_girl6_happy_mmm noloop
    dk "Ezra needs to suck the Main Character's cock, but she's never sucked such a big dick. So I was just helping train her gag reflex!"
    scene d21s25-120 sy-dd-zp-1sm-jh-lw-talking with dissolve
    play voice5 girl8_happy_mmm1 noloop
    edo "I'm a big fan of your scenes, by the way! If I could take dick like you, I wouldn't have to train."
    scene d21s25-121 sy-dd-zp-1sm-jh-lw-talking with dissolve
    play voice3 stacy_yes2 noloop
    sy "Oh yeah! Daisy is a real expert at deep throating!"
    scene d21s25-122 sy-dd-zp-1sm-jh-lw-talking with dissolve
    play voice5 postcredit_girl7_yes_yeah5 noloop
    edo "Yeah! You are a star!"
    scene d21s25-123 sy-dd-zp-1sm-jh-lw-talking with dissolve
    play voice4 daisy_aga noloop
    dd "Thank you!"
    $ renpy.music.set_volume(0.0, 6.0, "music")
    $ renpy.music.set_volume(0.3, 0.0, "sound2")
    $ renpy.music.set_volume(0.35, 0.0, "sound3")
    play sound2 seabirds fadein 4.5
    play sound3 seawaves2 fadein 4.0
    play sound sfx_reminiscence_gone volume 1.6
    scene d21s25-124 sy-dd-zp-1sm-jh-lw-talking with image_dissolve_d21s25_07_5
    pause
    scene d21s25-125 sy-dd-talking with dissolve
    play voice4 daisy_oof noloop
    dd "Oh... I guess that's the end then."
    scene d21s25-126 sy-dd-talking with dissolve
    play voice3 stacy_hmm noloop
    sy "Well... We can still enjoy the sunset together."
    scene d21s25-127 sy-dd-smiling with dissolve
    play voice4 aaleyah_happy_mmm1 noloop
    dd "I'd like that very much."
    scene d21s25-128 sy-dd-sitting together with dissolve
    pause
    stop sound2
    stop sound3
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "sound2")
    $ renpy.music.set_volume(1.0, 3.0, "sound3")
    scene black
    show fl_will_return:
        xalign 0.5
        yalign 0.5
    with Fade(0.6, 0.6, 0.6)
    pause
    scene black with Fade(0.3, 0.3, 0.3)

    return







label show_fl_points_overlay:

    show screen fl_points_screen(fl_points)
    return

label hide_fl_points_overlay:

    show screen fl_points_screen(fl_points, False)
    return

label add_points(points):

    $ fl_points += points
    call show_fl_points_overlay from _call_show_fl_points_overlay
    return

label update_ending_variables:

    if hasattr(renpy.store, "mcname"):
        $ persistent.mcname = mcname
    elif True:
        $ persistent.mcname = "Mike"
    if hasattr(renpy.store, "mclogin"):
        $ persistent.mclogin = mclogin
    elif True:
        $ persistent.mclogin = "Not_Mike"
    if hasattr(renpy.store, "cage_ntr"):
        $ persistent.cage_ntr = cage_ntr
    elif True:
        $ persistent.cage_ntr = False
    if hasattr(renpy.store, "fl_enema"):
        $ persistent.fl_enema = fl_enema
    elif True:
        $ persistent.fl_enema = False
    if hasattr(renpy.store, "fl_watersports"):
        $ persistent.fl_watersports = fl_watersports
        $ persistent.more_watersports = fl_watersports
    elif True:
        $ persistent.fl_watersports = False
        $ persistent.more_watersports = False
    if hasattr(renpy.store, "fl_footfetish"):
        $ persistent.fl_footfetish = fl_footfetish
    elif True:
        $ persistent.fl_footfetish = False
    if hasattr(renpy.store, "fl_cumgarnish"):
        $ persistent.fl_cumgarnish = fl_cumgarnish
    elif True:
        $ persistent.fl_cumgarnish = False
    if hasattr(renpy.store, "fl_fisting"):
        $ persistent.fl_fisting = fl_fisting
    elif True:
        $ persistent.fl_fisting = False
    if hasattr(renpy.store, "temp_pegging"):
        $ persistent.fl_pegging = temp_pegging
    elif True:
        $ persistent.fl_pegging = False
    if hasattr(renpy.store, "fl_trans"):
        $ persistent.fl_trans = fl_trans
    elif True:
        $ persistent.fl_trans = False
    if hasattr(renpy.store, "d20s08_copy_files"):
        $ persistent.copy_files = d20s08_copy_files
    elif True:
        $ persistent.copy_files = False
    if hasattr(renpy.store, "d20s04_pass_exam"):
        $ persistent.pass_exam = d20s04_pass_exam
    elif True:
        $ persistent.pass_exam = False
    if hasattr(renpy.store, "date_sy"):
        $ persistent.date_sy = date_sy
    elif True:
        $ persistent.date_sy = False
    if hasattr(renpy.store, "date_dd"):
        $ persistent.date_dd = date_dd
    elif True:
        $ persistent.date_dd = False
    if hasattr(renpy.store, "date_mh"):
        $ persistent.date_mh = date_mh
    elif True:
        $ persistent.date_mh = False
    if hasattr(renpy.store, "d12s05_stop"):
        $ persistent.fuck_nr = d12s05_stop
    elif True:
        $ persistent.fuck_nr = False
    if hasattr(renpy.store, "d20s03_sex"):
        $ persistent.d20s03_sex = d20s03_sex
    elif True:
        $ persistent.d20s03_sex = False
    if hasattr(renpy.store, "d15s05b_pegged"):
        $ persistent.nk_pegged = d15s05b_pegged
    elif True:
        $ persistent.nk_pegged = False
    return

label start_ending_from_menu:

    $ from_ending_menu = True

    if not has_persistent("mcname"):
        $ persistent.mcname = "Mike"
    if not has_persistent("mclogin"):
        $ persistent.mclogin = "Not_Mike"
    if not has_persistent("cage_ntr"):
        $ persistent.cage_ntr = False
    if not has_persistent("fl_enema"):
        $ persistent.fl_enema = False
    if not has_persistent("fl_watersports"):
        $ persistent.fl_watersports = False
        $ persistent.more_watersports = False
    if not has_persistent("fl_footfetish"):
        $ persistent.fl_footfetish = False
    if not has_persistent("fl_cumgarnish"):
        $ persistent.fl_cumgarnish = False
    if not has_persistent("fl_fisting"):
        $ persistent.fl_fisting = False
    if not has_persistent("fl_pegging"):
        $ persistent.fl_pegging = False
    if not has_persistent("fl_trans"):
        $ persistent.fl_trans = False
    if not has_persistent("d20s08_copy_files"):
        $ persistent.copy_files = False
    if not has_persistent("d20s04_pass_exam"):
        $ persistent.pass_exam = False
    if not has_persistent("date_sy"):
        $ persistent.date_sy = False
    if not has_persistent("date_dd"):
        $ persistent.date_dd = False
    if not has_persistent("date_mh"):
        $ persistent.date_mh = False
    if not has_persistent("fuck_nr"):
        $ persistent.fuck_nr = False
    if not has_persistent("d20s03_sex"):
        $ persistent.d20s03_sex = False
    if not has_persistent("d15s05b_pegged"):
        $ persistent.nk_pegged = False
    return

label after_load:

    $ _preferences.show_empty_window = False
    $ FLSS.savename = FLSS.savename_temp
    $ save_name = FLSS.savename
    call update_ending_variables from _call_update_ending_variables_15
    return

label add_gold_star:

    show fl_goldstar at fl_goldstar_anim
    play sound get_goldstar
    pause 3.0
    $ fl_goldstars += 1
    pause
    return

label end_game_text(txt):

    scene black
    show screen game_end_text(txt)
    with Fade(1.0, 0.5, 1.0)
    pause
    hide screen game_end_text
    return



label buzz:

    play sound buzz
    "Bzzzzz" with hpunch
    return

label knock:

    play sound2 knockknock noloop
    "*knock knock*"
    return

label metalknock1:

    play sound2 sfx_metaldoor_knock1 noloop
    "*knock knock*"
    return

label metalknock2:

    play sound2 sfx_metaldoor_knock2 noloop
    "*knock knock*"
    return

label drink:

    play sound ["<silence .3>", audio.gulp, "<silence .5>", audio.gulp, "<silence .3>", audio.gulp, "<silence .7>", audio.gulp, "<silence .4>", audio.gulp] loop
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
