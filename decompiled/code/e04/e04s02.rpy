image e04s02-a41-1 = Movie(play = "images/E-04/s02/anim/e04s02-a41-1-2x-50fps.webm", start_image = "e04s02-a41-1 mc-lc-sex3-anim-01")
image e04s02-a41-1-f = Movie(play = "images/E-04/s02/anim/e04s02-a41-1-2x-60fps.webm", start_image = "e04s02-a41-1 mc-lc-sex3-anim-01")
image e04s02-a41-2 = Movie(play = "images/E-04/s02/anim/e04s02-a41-2-2x-50fps.webm", start_image = "e04s02-a41-2 mc-lc-sex3-anim-01")
image e04s02-a41-2-f = Movie(play = "images/E-04/s02/anim/e04s02-a41-2-2x-60fps.webm", start_image = "e04s02-a41-2 mc-lc-sex3-anim-01")
image e04s02-a41-3 = Movie(play = "images/E-04/s02/anim/e04s02-a41-3-2x-50fps.webm", start_image = "e04s02-a41-3 mc-lc-sex3-anim-01")
image e04s02-a41-3-f = Movie(play = "images/E-04/s02/anim/e04s02-a41-3-2x-60fps.webm", start_image = "e04s02-a41-3 mc-lc-sex3-anim-01")
image e04s02-a41-4 = Movie(play = "images/E-04/s02/anim/e04s02-a41-4-2x-50fps.webm", start_image = "e04s02-a41-4 mc-lc-sex3-anim-01")
image e04s02-a41-4-f = Movie(play = "images/E-04/s02/anim/e04s02-a41-4-2x-60fps.webm", start_image = "e04s02-a41-4 mc-lc-sex3-anim-01")

image e04s02-a50-1 = Movie(play = "images/E-04/s02/anim/e04s02-a50-1-2x-50fps.webm", start_image = "e04s02-a50-1 mc-lc-blowjob2-anim-01")
image e04s02-a50-1-f = Movie(play = "images/E-04/s02/anim/e04s02-a50-1-2x-60fps.webm", start_image = "e04s02-a50-1 mc-lc-blowjob2-anim-01")
image e04s02-a50-2 = Movie(play = "images/E-04/s02/anim/e04s02-a50-2-2x-50fps.webm", start_image = "e04s02-a50-2 mc-lc-blowjob2-anim-01")
image e04s02-a50-2-f = Movie(play = "images/E-04/s02/anim/e04s02-a50-2-2x-60fps.webm", start_image = "e04s02-a50-2 mc-lc-blowjob2-anim-01")
image e04s02-a50-3 = Movie(play = "images/E-04/s02/anim/e04s02-a50-3-2x-50fps.webm", start_image = "e04s02-a50-3 mc-lc-blowjob2-anim-01")
image e04s02-a50-3-f = Movie(play = "images/E-04/s02/anim/e04s02-a50-3-2x-60fps.webm", start_image = "e04s02-a50-3 mc-lc-blowjob2-anim-01")

image e04s02-a57-1 = Movie(play = "images/E-04/s02/anim/e04s02-a57-1-2x-50fps.webm", start_image = "e04s02-a57-1 mc-lc-sex1-anim-01")
image e04s02-a57-1-f = Movie(play = "images/E-04/s02/anim/e04s02-a57-1-2x-60fps.webm", start_image = "e04s02-a57-1 mc-lc-sex1-anim-01")
image e04s02-a57-2 = Movie(play = "images/E-04/s02/anim/e04s02-a57-2-2x-50fps.webm", start_image = "e04s02-a57-2 mc-lc-sex1-anim-01")
image e04s02-a57-2-f = Movie(play = "images/E-04/s02/anim/e04s02-a57-2-2x-60fps.webm", start_image = "e04s02-a57-2 mc-lc-sex1-anim-01")
image e04s02-a57-3 = Movie(play = "images/E-04/s02/anim/e04s02-a57-3-2x-50fps.webm", start_image = "e04s02-a57-3 mc-lc-sex1-anim-01")
image e04s02-a57-3-f = Movie(play = "images/E-04/s02/anim/e04s02-a57-3-2x-60fps.webm", start_image = "e04s02-a57-3 mc-lc-sex1-anim-01")

image e04s02-a63-glambot-1 = Movie(play = "images/E-04/s02/anim/e04s02-a63-2x-50fps.webm", start_image = "e04s02-a63 mc-lc-end1-glambot-63-000_i", image = "e04s02-a63 mc-lc-end1-glambot-63-119_i", loop = False)

label e04s02:

    $ alt_mcname = None
    $ e04s02_change_name = False

    scene black
    show screen scene_transistion(_("Some time later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_jail_door_open1
    scene e04s02-01 mc-lc-entry1_c1
    with Fade(0.5, 0.5, 0.5)
    $ renpy.music.set_volume(0.7, 6.0, "music")
    play sound2 sfx_heels_steps2
    queue music music_bdsm_sentenced
    pause
    scene e04s02-02 mc-lc-entry2_c1 with dissolve
    pause
    stop sound2 fadeout 1.0
    scene e04s02-04 mc-lc-talk1_c1 with dissolve
    play sound sfx_cloth_rustling2
    play voice2 mc_thinking_oh1 noloop
    mc "This is a nice throne."
    mc "Super uncomfortable though."
    scene e04s02-04 mc-lc-talk1_c2 with dissolve
    play voice3 dahlia_angry_oof noloop
    lc "You don't deserve to sit on it."
    scene e04s02-05 mc-lc-talk2_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "And you do?"
    scene e04s02-05 mc-lc-talk2_c2 with dissolve
    play voice3 dahlia_yes_yeah4 noloop
    lc "Of course."
    scene e04s02-06 mc-lc-talk3_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Kneel."
    scene e04s02-06 mc-lc-talk3_c2 with dissolve
    play voice3 dahlia_no_serious noloop
    lc "No."
    scene e04s02-07 mc-lc-talk4_c1 with dissolve
    play voice2 mc_arrogant_tsktsk noloop
    mc "Tsk, tsk. Eventually, you'll learn."
    scene e04s02-07 mc-lc-talk4_c2 with dissolve
    play voice3 lydia_thinking noloop volume 1.7
    lc "Why did you bring me down here?"
    scene e04s02-08 mc-lc-talk5_c1 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "To start your re-education."
    scene e04s02-08 mc-lc-talk5_c2 with dissolve
    play voice3 dahlia_arrogant_pff noloop
    lc "You won't break me."
    play sound sfx_cloth_rustling1
    play sound2 sfx_heels_steps1 noloop
    scene e04s02-09 mc-lc-walk1_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Before we get into that, there are so me rules we need to go over."
    stop sound2 fadeout 1.0
    scene e04s02-10 mc-lc-near1_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "You're free to return to prison whenever you want. All you need to do is press this button."
    play sound sfx_sextoy_cuff2
    scene e04s02-11 mc-lc-neck1_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Of course, then everyone will know that I broke you."
    scene e04s02-11 mc-lc-neck1_c2 with dissolve
    play voice3 dahlia_angry_oh noloop
    lc "I'll never press it."
    scene e04s02-12 mc-lc-talk1_c1 with dissolve
    play voice2 d9s2_yeah noloop volume 2.6
    mc "We'll see about that."
    scene e04s02-13 mc-lc-talk2_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "If you plan on staying then, there are some rules."
    mc "The next rule - from now on, I want you to call me..."
    menu:
        "[mcname]"(hint="e04s02m01c01"):
            scene e04s02-14 mc-lc-talk3_c1 with dissolve
            play voice2 mc_thinking_hmm4 noloop
            mc "Actually, I think I'm going to have you call me [mcname]. For now."
            $ alt_mcname = mcname
        "Warden"(hint="e04s02m01c02"):

            $ e04s02_change_name = True
            $ alt_mcname = "Warden"
            scene e04s02-14 mc-lc-talk3_c1 with dissolve
            play voice2 mc_thinking_hmm1 noloop
            mc "You'll only refer to me as Warden from here on out. It is my proper title after all."
        "Enter your own"(hint="e04s02m01c03"):

            $ e04s02_change_name = True
            python:
                alt_mcname = renpy.input(_("What do you want Lydia to call you?"), default=__("")).strip().title()
                if not alt_mcname:
                    alt_mcname = mcname
            scene e04s02-14 mc-lc-talk3_c1 with dissolve
            play voice2 mc_thinking_hmm1 noloop
            mc "Hmm, from now on you'll call me [alt_mcname]."

    scene e04s02-12 mc-lc-talk1_c2 with dissolve
    play voice3 dahlia_arrogant_hm noloop
    lc "If I don't?"
    play sound sfx_cloth_rustling1
    scene e04s02-15 mc-lc-talk4_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop volume 1.5
    mc "We'll get to that."
    mc "Third rule; what I say is law. Every word is a directive, every sentence a commandment."
    mc "Disobeying me will result in a punishment."
    scene e04s02-13 mc-lc-talk2_c2 with dissolve
    play voice3 dahlia_disgust_yah noloop
    lc "You're a pathetic loser."
    scene e04s02-16 mc-lc-talk5_c1 with dissolve
    play voice2 mc_thinking_hmm3 noloop volume 1.4
    mc "We'll call this one rule four; I can punish you for any reason I want. Because that's why you're here; to be punished."
    scene e04s02-14 mc-lc-talk3_c2 with dissolve
    play voice3 dahlia_old_argh2 noloop
    lc "You couldn't punish me even if you tried."
    scene e04s02-17 mc-lc-near1_c1 with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Have you already forgotten about the pool?"
    scene e04s02-17 mc-lc-near1_c2 with dissolve
    play voice3 lydia_moan1 noloop
    lc "You..."
    scene e04s02-18 mc-lc-face1_c1 with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "I know. While you're under this roof, you'll have a bed."
    mc "You'll get food... Whenever I feel like it. You can make small requests for books and whatnot. If you behave."
    scene e04s02-18 mc-lc-face1_c2 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "During your imprisonment, you'll need to wear something more... Appropriate."
    play sound sfx_heels_steps1 volume 1.5
    scene e04s02-19 mc-lc-goback1_c1 with dissolve
    pause
    play sound sfx_paper_bag_1
    scene e04s02-20 mc-lc-throne_c1 with dissolve
    pause
    scene e04s02-20 mc-lc-throne_c2 with dissolve
    pause

    jump e04s02_sex

label replay_e04s02:
label e04s02_sex:

    if _in_replay:
        $ renpy.music.set_volume(0.7, 0.0, "music")
        play music music_bdsm_sentenced
    play sound sfx_paper_bag_2
    scene e04s02-21 mc-lc-beg1_c1 with dissolve
    play voice2 mc_happy_hah1 noloop
    mc "Now, time to begin your training. Strip."
    scene e04s02-21 mc-lc-beg1_c2 with dissolve
    play voice3 dahlia_surprised_huh2 noloop
    lc "Why."
    scene e04s02-22 mc-lc-beg2_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.6
    mc "Because you need to put on your new prison uniform."
    scene e04s02-22 mc-lc-beg2_c2 with dissolve
    play voice3 dahlia_angry_argh2 noloop
    lc "And if I decline?"
    scene e04s02-23 mc-lc-lookaway1_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "There are plenty of options for punishments. Maybe we'll take away some privileges. No books, maybe a week in complete darkness."
    mc "Amongst some of the more creative options. So strip or..."
    scene e04s02-23 mc-lc-lookaway1_c2 with dissolve
    play voice3 dahlia_pain_mmh noloop
    lc "You're a pig."
    scene e04s02-24 mc-lc-near1_c2 with dissolve
    play voice3 dahlia_surprised_huh1 noloop
    lc "How do you expect me to strip with these on?"
    play sound sfx_sextoy_uncuff1
    scene e04s02-25 mc-lc-handcuff1_c1 with dissolve
    play voice2 d2s9_confused noloop
    pause
    play sound sfx_sextoy_uncuff1
    scene e04s02-25 mc-lc-handcuff1_c2 with dissolve
    pause
    play sound sfx_skirt_off2
    scene e04s02-25-1 mc-lc-undress1_c2 with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    lc "You don't deserve to see me like this."
    play sound sfx_cloth_rustling1
    scene e04s02-26 mc-lc-nude1_c2 with dissolve
    lc "Happy."
    scene e04s02-26 mc-lc-nude1_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.5
    mc "Not even trying to cover yourself."
    scene e04s02-27 mc-lc-nude2_c2 with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    lc "I have nothing to be ashamed of."
    play sound sfx_cloth_rustling2
    scene e04s02-28 mc-lc-talk1_c1 with dissolve
    play voice2 d9s2_ugu noloop volume 1.7
    mc "Here's your uniform. Put it on."
    play sound sfx_cloth_rustling1
    scene e04s02-29 mc-lc-talk2_c2 with dissolve
    pause
    play sound sfx_paper_bag_1
    scene e04s02-30 mc-lc-look beg1_c2 with dissolve
    pause
    stop sound fadeout 1.0
    scene e04s02-32 mc-lc-talk1_c2 with dissolve
    play voice3 dahlia_no_nah noloop
    lc "Kinky, but I am {i}not{/i} wearing this."
    lc "Why would I wear something like this for someone as pathetic as you?"
    scene e04s02-31 mc-lc-look beg2_c1 with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Have I not been clear? Refuse a command, and you will be punished."
    scene e04s02-33 mc-lc-back1_c1 with dissolve
    play voice3 dahlia_angry_oof noloop
    lc "Ooooh, I'm shaking."
    play sound sfx_cloth_rustling1
    scene e04s02-34 mc-lc-back2_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "I'm curious. What's the worst you think I could do?"
    play sound sfx_cloth_rustling3
    scene e04s02-35 mc-lc-back3_c1 with dissolve
    pause
    scene e04s02-36 mc-lc-back4_c2 with dissolve
    play voice3 lydia_haha noloop volume 1.7
    lc "Nothing that will break me."
    scene e04s02-36 mc-lc-back4_c1 with dissolve
    play voice3 lydia_hmmmm noloop volume 1.7
    lc "Whatever you think you've got, your secret weapon. It won't be enough."
    play voice2 mc_scared_oh4 noloop
    mc "Oh, I got a better idea than that."
    play sound sfx_hair_scratch1
    scene e04s02-37 mc-lc-force1_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    if d17s01_arj_assfuck is True:
        mc "Remember how you made me fuck AmRose in the ass, with no lube?"
        mc "You seemed to really like watching that. Maybe it's your turn to know what that feels like."
    else:
        mc "Remember how you tried to use Fetish Locator to get me to fuck AmRose in the ass with no lube?"
        mc "Maybe I should show you just how rough anal can be, especially without lube."
    scene e04s02-37 mc-lc-force1_c2 with dissolve
    play voice3 dahlia_arrogant_heh noloop
    lc "Like your dick is really going to do anything to me."
    scene e04s02-38 mc-lc-force2_c2 with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    lc "Try all you want, I won't be like those other women who just seem to magically worship your dick after one fuck."
    scene e04s02-38 mc-lc-force2_c1 with dissolve
    play voice2 mc_happy_thatsgood noloop
    mc "Good thing I'll have enough time to fuck you more than once."
    play sound sfx_jeans_on1 volume 1.5
    $ renpy.music.set_volume(0.85, 3.0, "music")


    $ Lovense.stop()

    scene e04s02-39 mc-lc-sex1_c1 with dissolve
    pause

    $ Lovense.vibrate(5)

    play voice2 mc_angry_errr4 noloop
    play sound sfx_fisting_fist2
    scene e04s02-a41-1 mc-lc-sex3-anim-01 with dissolve
    play voice3 lydia_ah noloop
    lc "SWEET MOTHER OF GOD!"
    $ Lovense.pattern("5;10", 1400)
    scene e04s02-a41-1
    play sound sfx_vagina_penetration1_fast loop
    play voice2 mc_happy_laugh1 noloop
    queue voice2 d7s4_mcbreathing
    play voice3 dahlia_sex_openmoans2
    mc "Yeah, it feels greeeat when you don't have lube, right?"
    play voice3 dahlia_angry_argh1 noloop
    queue voice3 dahlia_sex_openmoans2
    lc "FUCK. YOU."
    play voice2 mc_no_nono1 noloop
    queue voice2 d7s4_mcbreathing
    mc "No, no. I'm fucking you."
    pause
    scene e04s02-a41-2 with dissolve
    pause
    lc "FUCK. FUCK. FUCK."
    lc "COULD you {i}PLEASE{/i} slow down!?"
    mc "How do you ask?"
    lc "FUCK, I said {i}please!{/i}"
    scene e04s02-a41-3 with dissolve
    mc "How do you ask {i}me?{/i}"
    lc "Nuh uh!"
    mc "Wrong answer."
    pause
    scene e04s02-a41-4 with dissolve
    lc "JESUS, fine!"
    lc "Please, [alt_mcname], can you slow down!?"
    pause
    play voice3 dahlia_sex_openmoans2
    $ Lovense.pattern("7;11", 700)
    scene e04s02-a41-1-f with dissolve
    pause
    mc "Nope."
    lc "FUCK! I DID WHAT YOU SAID!"
    scene e04s02-a41-2-f with dissolve
    mc "And?"
    lc "YOU ASSHOLE!"
    pause
    scene e04s02-a41-3-f with dissolve
    mc "Hmm, that sure is a lot of back talk."
    lc "OH FUCK!"
    pause
    scene e04s02-a41-4-f with dissolve
    mc "Do you remember rule number four?"
    lc "Eat a dick!"
    pause
    stop voice3 fadeout 1.0
    play sound sfx_hair_scratch1 volume 1.5
    $ Lovense.stop()
    $ Lovense.vibrate(3)
    scene e04s02-42 mc-lc-sex4_c1 with dissolve
    play voice2 mc_scared_oh3 noloop
    mc "You know, you've given me an idea for your next punishment."
    scene e04s02-42 mc-lc-sex4_c2 with dissolve
    pause
    scene e04s02-43 mc-lc-walk1_c1 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Open wide."
    scene e04s02-43 mc-lc-walk1_c2 with dissolve
    play voice3 dahlia_no_high1 noloop
    lc "No."
    scene e04s02-44 mc-lc-front1_c1 with dissolve
    $ Lovense.vibrate(2)
    play voice2 mc_arrogant_huh3 noloop
    mc "Still feeling feisty, huh."
    scene e04s02-44 mc-lc-front1_c2 with dissolve
    play voice3 dahlia_sex_closedmoan1 noloop
    lc "I won't be your plaything."
    play sound sfx_cloth_rustling1
    scene e04s02-45 mc-lc-grab1_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Open."
    scene e04s02-45 mc-lc-grab1_c2 with dissolve
    play voice3 dahlia_angry_hm1 noloop
    lc "Hell no."
    scene e04s02-46 mc-lc-grab2_c1 with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "How about now?"
    play voice3 lydia_ah noloop
    play voice2 sfx_biologic_spit1 noloop volume 2.5
    play sound sfx_hands_clap1
    scene e04s02-46 mc-lc-grab2_c2 with hpunch
    pause
    scene e04s02-47 mc-lc-stand1_c2 with dissolve
    play voice2 mc_angry_errr3 noloop
    mc "It will only get worse."
    mc "I looked through your toys. Do you know what I found?"
    play voice3 lydia_huh2 noloop volume 1.4
    lc "No! You wouldn't!"
    scene e04s02-47 mc-lc-stand1_c1 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "That's right. That little metal device for prying someone's mouth open and keeping it that way."
    scene e04s02-48 mc-lc-stand2_c2 with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    lc "Fine..."
    scene e04s02-48 mc-lc-stand2_c1 with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Good girl. You're learning."
    $ Lovense.vibrate(4)
    scene e04s02-49 mc-lc-blowjob1_c1 with dissolve
    play voice2 mc_yes_yes1 noloop
    play voice3 samiya_mfff noloop
    mc "This is what eating a dick feels like!"
    mc "And about being an asshole-"
    scene e04s02-49 mc-lc-blowjob1_c2 with dissolve
    play voice2 mc_thinking_mmm1 noloop volume 1.3
    play voice3 samiya_mfff3 noloop
    mc "How does it feel to have the taste of your ass shoved down your throat?"
    mc "Hopefully you've kept it clean!"
    scene e04s02-a50-1 mc-lc-blowjob2-anim-01 with dissolve
    pause
    play voice2 d7s4_mcbreathing
    play voice3 aaleyah_sucking_deep
    $ Lovense.pattern("7;10", 1400)
    scene e04s02-a50-1
    mc "And if you are what you eat-"
    mc "-are you a shithead, or a cocksucker?"
    pause
    scene e04s02-a50-2 with dissolve
    pause
    scene e04s02-a50-3 with dissolve
    pause
    $ Lovense.pattern("7;11", 700)
    scene e04s02-a50-1-f with dissolve
    pause
    scene e04s02-a50-2-f with dissolve
    pause
    scene e04s02-a50-3-f with dissolve
    mc "How long do you think you can hold your breath?"
    lc "Mmmng?"
    pause
    play voice2 d1s5_orgasm2 noloop
    play voice3 samiya_mfff3 noloop
    $ Lovense.stop()
    $ Lovense.vibrate(15)
    scene e04s02-51 mc-lc-blowjob3_c1 with hpunch
    mc "1...{w} 2...{w} 3...{w} 4...{w} 5..."
    play voice2 d1s5_orgasm noloop
    scene e04s02-51 mc-lc-blowjob3_c2 with dissolve
    play voice3 samiya_mfff2 noloop
    mc "6...{w} 7...{w} 8...{w} 9...{w} 10."
    play sound sfx_spitcum1
    $ Lovense.vibrate(3)
    scene e04s02-52 mc-lc-blowjob4_c1 with dissolve
    play voice2 mc_surprised_wow2 noloop
    play voice3 polly_breathing noloop
    mc "Wow, look at you. Good girl."
    scene e04s02-52 mc-lc-blowjob4_c2 with dissolve
    play voice3 dahlia_pain_sobs noloop
    lc "Fuck... You..."
    play sound sfx_hands_clap2
    scene e04s02-53 mc-lc-blowjob5_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "You will. There's so much left to do."
    scene e04s02-53 mc-lc-blowjob5_c2 with dissolve
    play voice3 dahlia_sex_closedmoan2 noloop
    lc "You're... A... Bastard..."
    $ Lovense.vibrate(2)
    scene e04s02-54 mc-lc-goback1_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "This can stop, any time. All you have to do is press that little button on your collar."
    play voice3 dahlia_no_high3 noloop
    lc "...No..."
    play sound sfx_hair_scratch1
    scene e04s02-55 mc-lc-back1_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "Just you wait."
    scene e04s02-55 mc-lc-back1_c2 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "If you keep breaking the rules, the punishments will get worse and worse."
    scene e04s02-56 mc-lc-back2_c1 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Maybe you'll be able to fight it. Maybe you'll be able to resist the urge to be my little cum dumpster."
    scene e04s02-56 mc-lc-back2_c2 with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "At least for a little bit."
    play voice2 mc_angry_errr4 noloop
    play voice3 dahlia_pain_argh noloop
    play sound sfx_fisting_fist2
    $ Lovense.vibrate(5)
    scene e04s02-a57-1 mc-lc-sex1-anim-01 with dissolve
    pause
    play voice2 d7s4_mcbreathing
    play voice3 dahlia_sex_openmoans2
    play sound sfx_vagina_penetration1_fast loop
    $ Lovense.pattern("7;12", 1400)
    scene e04s02-a57-1
    lc "OW, JESUS!"
    mc "Hey you lubed up my dick real nice this time around!"
    pause
    scene e04s02-a57-2 with dissolve
    play voice3 dahlia_pain_ouch2 noloop
    queue voice3 dahlia_sex_openmoans2
    lc "It's still sore from before!"
    mc "Good! Maybe you'll learn your lesson then."
    mc "There's- Oh, fuck- I'm getting close."
    pause
    scene e04s02-a57-3 with dissolve
    lc "Don't- mmph- don't you dare cum in my ass! I will, nnng, I will shove it down your throat!"
    mc "What was that? Was that a little moan?"
    lc "Mmm- no! Fuck- No!"
    pause
    $ Lovense.pattern("7;14", 700)
    scene e04s02-a57-1-f with dissolve
    mc "I think that someone is starting to like this!"
    lc "No, no, no, no- Fuck!"
    pause
    scene e04s02-a57-2-f with dissolve
    mc "Fuuuuhuck, I'm just about to cum!"
    lc "Wait, wait, just a little-"
    pause
    scene e04s02-a57-3-f with dissolve
    mc "Fuck, I'm going to fill your ass with my cum!"
    lc "Just a little-"
    mc "Nnnnnng!"
    pause
    play voice3 lydia_orgasm1 noloop
    play voice2 d1s5_orgasm2 noloop
    play sound mc_cum_sound1
    $ Lovense.stop()
    $ Lovense.vibrate(17)
    scene e04s02-58-3 mc-lc-cum_c1 with vpunch
    lc "No, no, no!"
    pause
    play voice2 d1s5_orgasm noloop
    play voice3 lydia_oops noloop
    scene e04s02-58-3 mc-lc-cum_c2 with hpunch
    pause
    $ Lovense.vibrate(2)
    scene e04s02-59 mc-lc-stand1_c2 with dissolve
    pause
    $ renpy.music.set_volume(0.6, 3.0, "music")
    scene e04s02-60 mc-lc-stand2_c1 with dissolve
    play voice3 dahlia_angry_oh noloop
    lc "*Whispers* Fuck... I was so close. You bastard."
    play voice2 mc_no_nah2 noloop
    mc "You'll be allowed to cum when you start acting like a good girl. But for now-"

    $ Lovense.stop()


    play sound sfx_jeans_on1
    scene e04s02-61 mc-lc-stand3_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "-You exist for my pleasure."
    play sound sfx_sextoy_cuff1
    scene e04s02-62 mc-lc-handcuff1_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I'll give you a moment. Then I want you to clean up the mess you made."
    play sound sfx_sextoy_cuff2
    scene e04s02-62 mc-lc-handcuff1_c2 with dissolve
    pause
    $ renpy.end_replay()
    $ unlock_gallery_slot("scene", "e04s02")
    play sound sfx_cloth_rustling2
    scene e04s02-63 mc-lc-end1_c1 with dissolve
    play sound2 sfx_heels_steps2
    play voice2 mc_thinking_hmm4 noloop
    mc "While you handle that, I need to get your cell prepared."
    stop sound2 fadeout 3.0
    play sound ["<silence 0.4>", sfx_camera_fly1] volume 2.5
    scene e04s02-a63-glambot-1 with dissolve
    pause
    stop sound fadeout 1.0
    scene e04s02-63 mc-lc-end1_c2 with dissolve
    play voice3 dahlia_angry_argh1 noloop
    lc "What an... Idiot. I... I could escape... Right now..."
    play sound sfx_cloth_planket2
    scene e04s02-65 mc-lc-end3_c1 with dissolve
    play voice3 dahlia_pain_mmh noloop
    lc "But then... You'd think you've won... I... Had you wrapped around my finger...{w} Once..."
    play sound sfx_cloth_rustling2 volume 1.5
    scene e04s02-66 mc-lc-end4_c1 with dissolve
    play voice3 dahlia_sex_closedmoan2 noloop
    lc "I'll... Do it... Again..."
    stop music fadeout 3.0

    jump e04s03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
