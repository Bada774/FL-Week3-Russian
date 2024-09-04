image e07s01-a49-1 = Movie(play = "images/E-07/s01/anim/e07s01-a49-1-2x-50fps.webm", start_image = "e07s01-a49-1 mc-lc-arj-sex-anim-01")
image e07s01-a49-1-f = Movie(play = "images/E-07/s01/anim/e07s01-a49-1-2x-60fps.webm", start_image = "e07s01-a49-1 mc-lc-arj-sex-anim-01")
image e07s01-a49-2 = Movie(play = "images/E-07/s01/anim/e07s01-a49-2-2x-50fps.webm", start_image = "e07s01-a49-2 mc-lc-arj-sex-anim-01")
image e07s01-a49-2-f = Movie(play = "images/E-07/s01/anim/e07s01-a49-2-2x-60fps.webm", start_image = "e07s01-a49-2 mc-lc-arj-sex-anim-01")
image e07s01-a49-3 = Movie(play = "images/E-07/s01/anim/e07s01-a49-3-2x-50fps.webm", start_image = "e07s01-a49-3 mc-lc-arj-sex-anim-01")
image e07s01-a49-3-f = Movie(play = "images/E-07/s01/anim/e07s01-a49-3-2x-60fps.webm", start_image = "e07s01-a49-3 mc-lc-arj-sex-anim-01")

image e07s01-a06-glambot-1 = Movie(play = "images/E-07/s01/anim/e07s01-a06-2x-50fps.webm", start_image = "e07s01-a06 mc-lc-arj-stand1-glambot-06-000", image = "e07s01-a06 mc-lc-arj-stand1-glambot-06-149", loop = False)

label e07_menu_jump:

    stop music fadeout 2.0
    call start_ending_from_menu from _call_start_ending_from_menu_11
    $ mcname = persistent.mcname
    $ date_arj_romance = persistent.arj_romance
    $ stop_all_sound()
    call hide_fl_points_overlay from _call_hide_fl_points_overlay_26

    jump e07_start_label

label e07s01:

    $ e07_challange_count = 5
    $ e07_mc_wins = 0

    $ e07_lcname = _("Queen")
    $ e07_mcname = _("Limpdick")
    $ e07_pbname = _("Neanderthal")
    $ e07_trname = _("Cocksucker")
    $ e07_ahname = _("Cuntlicker")
    $ e07_arjname = _("Skank")

    $ e07s01_face_arj = False
    $ e07s01_convince_arj = False

    $ renpy.music.set_volume(1.0, 1.0, "sound")
    $ renpy.music.set_volume(1.0, 1.0, "sound2")
    $ renpy.music.set_volume(1.0, 1.0, "sound3")
    $ renpy.music.set_volume(1.0, 1.0, "sound4")
    $ renpy.music.set_volume(1.0, 1.0, "sound5")
    $ renpy.music.set_volume(1.0, 1.0, "voice2")
    $ renpy.music.set_volume(1.0, 1.0, "voice3")
    $ renpy.music.set_volume(1.0, 1.0, "voice4")
    $ renpy.music.set_volume(1.0, 1.0, "voice5")
    $ renpy.music.set_volume(1.0, 1.0, "voice6")
    scene black
    show screen scene_transistion(_("Ending #7\nA New Chair"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene black
    show screen scene_transistion(_("Some time later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene e07s01-01 mc-lc-arj-entry1_c1
    with Fade(0.5, 0.5, 0.5)
    $ renpy.music.set_volume(0.6, 1.0, "music")
    play music assey
    pause
    play sound sfx_double_door1
    scene e07s01-01 mc-lc-arj-entry1_c2 with dissolve
    play voice4 amrose_surprised_huh1 noloop
    arj "Why is he tied up?!"
    play sound sfx_sand_run1 loop
    scene e07s01-02 mc-lc-arj-entry2_c1 with dissolve
    play voice3 dahlia_disgust_oof noloop
    lc "Oopsie. I guess I forgot to tell someone to unbind him."
    scene e07s01-02 mc-lc-arj-entry2_c2 with dissolve
    play voice3 lydia_hmmmm noloop volume 2.0
    lc "Feel free to untie him, but..."
    play sound sfx_skirt_off2
    scene e07s01-03 mc-lc-arj-untying1_c2 with dissolve
    pause
    scene e07s01-03 mc-lc-arj-untying1_c1 with dissolve
    pause
    play sound sfx_skirt_off3 volume 1.6
    scene e07s01-04 mc-lc-arj-wakeup1_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "Huh? What's happening?"
    play voice3 dahlia_disappointed_hmm2 noloop
    lc "... I expect it won't do much good."
    scene e07s01-04 mc-lc-arj-wakeup1_c2 with dissolve
    play voice4 amrose_surprised_uh2 noloop
    arj "What is this?! What have you done to him?! Is he drugged?!"
    scene e07s01-04 mc-lc-arj-wakeup1_c3 with dissolve
    play voice3 dahlia_no_nonono noloop
    lc "Drugged? Heaven's no. He's probably just dehydrated from drinking too much last night."
    scene e07s01-05 mc-lc-arj-walk1_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 2.0
    mc "AmRose? What are you doing here?"
    play voice4 amrose_surprised_ahh1 noloop
    arj "I don't know. I can't remember what happened."
    play sound sfx_heels_steps1 loop
    scene e07s01-05 mc-lc-arj-walk1_c2 with dissolve
    play voice3 dahlia_arrogant_ha noloop
    lc "Anyway, as I was saying. [mcname], if you can stand, stand. If not, then crawl out of that chair."
    play sound sfx_cloth_rustling2 volume 1.6
    scene e07s01-06 mc-lc-arj-stand1_c1 with dissolve
    play voice4 amrose_hey_scared noloop
    arj "*whispers* [mcname], let's get out of here. We can overpower this bitch or make a run for it."
    play voice2 mc_no_no5 noloop
    mc "No. *whispers* No. I'll explain it to you later. I want to be here."
    arj "*whispers* But we can go."
    scene e07s01-a06 mc-lc-arj-stand1-glambot-06-000 with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    lc "I hope bindings won't be necessary again."
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.5>", sfx_camera_fly1] volume 2.0 noloop
    scene e07s01-a06-glambot-1
    pause
    stop sound2 fadeout 1.0
    play sound sfx_cloth_rustling1 volume 1.6
    scene e07s01-07 mc-lc-arj-sit1_c1 with dissolve
    play voice3 dahlia_arrogant_heh noloop
    lc "Unless you prefer to be bound."
    lc "Many of my pets find pleasure in being tied up."
    scene e07s01-07 mc-lc-arj-sit1_c2 with dissolve
    play voice3 dahlia_thinking_oh noloop
    lc "Speaking of which, why don't you two untie my light fixtures."
    lc "[e07_trname!t] and [e07_ahname!t] could be useful in other ways soon."
    scene e07s01-08 mc-lc-arj-look1_c2 with dissolve
    play voice4 amrose_surprised_huh3 noloop
    arj "*whispers* Huh? What is she talking about."
    scene e07s01-08 mc-lc-arj-look1_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "*whispers* Terrell and his girlfriend, Aaleyah. We should let them out."
    scene e07s01-09 mc-lc-arj-talk1_c2 with dissolve
    play voice4 amrose_surprised_oh4 noloop
    arj "*whispers* Oh, okay."
    scene e07s01-10 mc-lc-arj-unbinding1_c1 with dissolve
    pause
    play sound sfx_cloth_rustling2
    scene e07s01-10 mc-lc-arj-unbinding1_c2 with dissolve
    play voice4 amrose_arrogant_huh4 noloop
    arj "You can't actually want to be here like this."
    play voice5 aaleyah_closed_moan6 noloop
    ah "*mumbles*"
    play sound sfx_sextoy_cuff2
    scene e07s01-11 mc-lc-arj-unbinding2_c2 with dissolve
    play voice4 amrose_disappointed_oh4 noloop
    arj "Oh, right. Don't try to speak yet."
    play sound sfx_spitcum1
    scene e07s01-11 mc-lc-arj-unbinding2_c1 with dissolve
    pause
    scene e07s01-12 mc-lc-arj-unbinding3_c1 with dissolve
    play voice6 terrell_hey2 noloop
    tr "I don't actually suck cock, just so you know."
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    play sound sfx_sextoy_uncuff1
    scene e07s01-12 mc-lc-arj-unbinding3_c2 with dissolve
    play voice6 terrell_relief noloop
    tr "My name. She calls me [e07_trname!t]. But I'm not a cocksucker."
    tr "I mean - sure, I do what she tells me to. But I don't enjoy it."
    scene e07s01-13 mc-lc-arj-talk1_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop volume 1.4
    mc "I didn't ask."
    mc "That said, if I wanted to get my dick sucked..."
    scene e07s01-13-1 mc-lc-arj-talk2_c2 with dissolve
    play voice6 terrell_oof noloop volume 1.5
    tr "Oh, I wouldn't worry about that if I were you."
    scene e07s01-13-1 mc-lc-arj-talk2_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "No? Have you got some idea of what she has planned for me?"
    scene e07s01-13-2 mc-lc-arj-talk3_c2 with dissolve
    play voice6 terrell_yes noloop volume 1.4
    tr "I know enough. You definitely don't need to worry about draining your balls anytime soon."
    scene e07s01-13-2 mc-lc-arj-talk3_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "Uh, okay..."
    scene e07s01-13-1 mc-lc-arj-talk2_c2 with dissolve
    play voice6 terrell_huh1 noloop
    tr "If I was you-"
    scene e07s01-15 mc-lc-arj-talk3_c2 with dissolve
    play voice3 dahlia_hey_angry noloop
    lc "You know the wonderful thing about the acoustics of this room?"
    lc "From my throne here I can hear everything you are saying. Even the whispers."
    scene e07s01-15 mc-lc-arj-talk3_c1 with dissolve
    play voice4 amrose_old_psst2 noloop
    arj "*whispers* We'll talk later."
    play voice5 aaleyah_disappointed_eeh noloop
    ah "*whispers* You really weren't listening, were you?"
    scene e07s01-16 mc-lc-arj-talk4_c2 with dissolve
    play voice3 dahlia_angry_argh2 noloop
    lc "That's enough. Put her in the chair."
    scene e07s01-16 mc-lc-arj-talk4_c1 with dissolve
    play voice4 amrose_surprised_huh2 noloop
    arj "Me?"
    scene e07s01-17 mc-lc-arj-talk5_c2 with dissolve
    play voice3 dahlia_angry_oh noloop
    lc "Did I stutter? [e07_trname!t], [e07_ahname!t], you may use force if she resists."
    scene e07s01-18 mc-lc-arj-talk6_c2 with dissolve
    play voice4 amrose_thinking_emm noloop
    arj "I'll..."
    arj "I will sit.{w} You don't need to force me."
    scene e07s01-19 mc-lc-arj-sit1_c1 with dissolve
    play voice3 dahlia_yes_simple noloop
    lc "Oh good. Let's chat. Just us gals."
    play sound sfx_cloth_rustling2
    scene e07s01-19 mc-lc-arj-sit1_c2 with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    lc "That includes [mcname], of course. Stand next to her, dear boy."
    scene e07s01-19 mc-lc-arj-sit1_c3 with dissolve
    play voice4 amrose_surprised_what noloop
    arj "What?!"
    scene e07s01-20 mc-lc-arj-sit2_c1 with dissolve
    play voice3 dahlia_arrogant_yeah noloop
    lc "[mcname]. One of us girls."
    lc "His claims to manhood might as well be worthless."
    scene e07s01-20 mc-lc-arj-sit2_c3 with dissolve
    play voice4 amrose_surprised_uh5 noloop
    arj "What are you talking about? You know as well as I do-"
    scene e07s01-22 mc-lc-arj-stand1_c2 with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    lc "Poor girl. He's a loser. Always has been. Always will be."
    lc "He's not worthy of me. He's not even worthy enough to lick my feet."
    lc "Even a redheaded cunt like you could do much better."
    scene e07s01-21 mc-lc-arj-walk1_c1 with dissolve
    play voice4 amrose_surprised_ahh2 noloop
    arj "Bitch!"
    scene e07s01-20 mc-lc-arj-sit2_c2 with dissolve
    play voice3 dahlia_disgust_yah noloop
    lc "Pish, posh, whatever."
    lc "If you're done acting out, let's talk."
    scene e07s01-22 mc-lc-arj-stand1_c1 with dissolve
    play voice4 amrose_angry_ehh noloop
    arj "Fine. What do you want to talk about?"
    scene e07s01-30 mc-lc-arj-talk5_c2 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "You know that she's behind Fetish Locator, right?"
    scene e07s01-23 mc-lc-arj-stand2_c2 with dissolve
    play voice4 amrose_yes_confident1 noloop
    arj "She told me."
    if is_antagonist_mode is True:
        arj "She's the one that has been blackmailing me for weeks."
        scene e07s01-23 mc-lc-arj-stand2_c1 with dissolve
        play voice4 amrose_angry_ugh noloop
        arj "She's the one that has copies of the photos and videos..."
        arj "Files I wouldn't want exposed anywhere."
    elif True:
        arj "She's the one who's been offering the reward."
        scene e07s01-23 mc-lc-arj-stand2_c1 with dissolve
        play voice4 amrose_angry_ugh noloop
        arj "And saw my photos and videos..."
        arj "Photos and videos I... Wish I had never posted..."
    scene e07s01-27 mc-lc-arj-talk2_c1 with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "Did she tell you that... This was the end game?"
    mc "Lydia wanted to build a harem of submissives and slaves. She was using Fetish Locator to find the people who would be best suited for her servitude."
    if is_antagonist_mode is True:
        mc "Which is why she was blackmailing us."
        scene e07s01-27 mc-lc-arj-talk2_c2 with dissolve
        play voice4 amrose_disappointed_ehh2 noloop
        arj "She was never going to stop blackmailing us. We were never going to be free."
        scene e07s01-24 mc-lc-arj-stand3_c2 with dissolve
        play voice3 dahlia_hey_greeting noloop
        lc "On the contrary, I was going to let you be the most free you've ever been."
        scene e07s01-24 mc-lc-arj-stand3_c1 with dissolve
        play voice4 amrose_angry_argh3 noloop
        arj "Bullshit!"
        scene e07s01-25 mc-lc-arj-sit_c2 with dissolve
        play voice3 dahlia_no_simple noloop
        lc "No, AmRose. It might not be what you imagined what freedom looks like."
        lc "But I'm creating a place where you can be entirely yourself. Where you don't need to hide those fetishes that you dare not let the world see."
        scene e07s01-32 mc-lc-arj-talk7_c2 with dissolve
        play voice3 girl12_arrogant_cough1 noloop
    elif True:
        mc "Which is why she offered the reward. It was a trick to see who would do the most depraved things."
        scene e07s01-27 mc-lc-arj-talk2_c2 with dissolve
        play voice4 amrose_disappointed_ehh2 noloop
        arj "She was never going to give us a reward. There was no money..."
        scene e07s01-24 mc-lc-arj-stand3_c2 with dissolve
        play voice3 dahlia_hey_greeting noloop
        lc "On the contrary, I have every intention of making sure you see every cent of the prize."
        scene e07s01-24 mc-lc-arj-stand3_c1 with dissolve
        play voice4 amrose_angry_argh3 noloop
        arj "Bullshit!"
        scene e07s01-25 mc-lc-arj-sit_c2 with dissolve
        play voice3 dahlia_no_simple noloop
        lc "No, AmRose. It might not be what you imagined the prize looks like."
        lc "But if we start looking at how much room and board costs, utilities, the cost of this house, the little \"activities\" I have planned for you."
        scene e07s01-32 mc-lc-arj-talk7_c2 with dissolve
        play voice3 girl12_arrogant_cough1 noloop
        lc "The cost adds up pretty quick. You'll have a life worth a million, if not more."
    lc "He hasn't gotten to the best part yet. Go on, [mcname]."
    scene e07s01-27 mc-lc-arj-talk2_c2 with dissolve
    play voice4 amrose_surprised_uh4 noloop
    arj "What? [mcname], tell me what's going on."
    play voice2 d2s12_emmm noloop volume 1.4
    mc "I... I've decided to stay."
    play voice4 amrose_surprised_ahh3 noloop
    arj "WHAT!?"
    scene e07s01-28 mc-lc-arj-talk3_c1 with dissolve
    play voice3 dahlia_angry_oof noloop
    lc "Oh come on, [e07_mcname!t]. Now is not the time to be bashful."
    scene e07s01-23 mc-lc-arj-stand2_c1 with dissolve
    play voice2 d3s7_mcemm noloop volume 1.7
    mc "I... Love Lydia."
    play voice4 amrose_pain_ahh2 noloop
    arj "Even after everything she's done to you!?"
    play voice2 d9s2_mcyes2 noloop volume 2.5
    mc "...Yes."
    scene e07s01-25 mc-lc-arj-sit_c2 with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    lc "Which brings me to why you are here, AmRose. As another participant in my little program, you're afforded the same choice as [e07_mcname!t]."
    if is_antagonist_mode is True:
        lc "You can finally be as free as you want, and stay here in my dungeon."
    elif True:
        lc "You can collect your winnings and stay here in my dungeon."
    lc "Otherwise, you're released from the program. You get nothing, you will receive nothing. Just my word that it's over."
    play sound sfx_cloth_planket2
    scene e07s01-25 mc-lc-arj-sit_c1 with dissolve
    play voice4 amrose_angry_breath1 noloop
    arj "If [mcname] is staying, so am I!"
    scene e07s01-29 mc-lc-arj-talk4_c1 with dissolve
    play voice3 dahlia_surprised_wow noloop
    lc "Oh wow, I did not see that coming. [e07_mcname!t], would you like to share your feelings on that?"
    menu:
        "Try and Convince AmRose to Leave"(hint="e07s01m01c01"):
            $ e07s01_convince_arj = True
            scene e07s01-30 mc-lc-arj-talk5_c2 with dissolve
            play voice2 mc_hey_hey1 noloop
            mc "AmRose... You should leave."
            scene e07s01-30 mc-lc-arj-talk5_c1 with dissolve
            play voice4 amrose_no_long noloop
            arj "No. I'm with you. I'll always be with you, [mcname]."
            scene e07s01-22 mc-lc-arj-stand1_c2 with dissolve
            play voice3 lydia_thinking noloop volume 1.7
            lc "Mmmm, how delectably sweet."
        "Stay Quiet"(hint="e07s01m01c02"):

            scene e07s01-23 mc-lc-arj-stand2_c1 with dissolve
            play voice2 mc_angry_hm2 noloop
            pause
            scene e07s01-22 mc-lc-arj-stand1_c2 with dissolve
            play voice3 dahlia_yes_yeah2 noloop
            lc "Good boy."

    lc "There are conditions for staying here. First of all, you shall address me from here on out as [e07_lcname!t]."
    scene e07s01-28 mc-lc-arj-talk3_c1 with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    lc "Secondly, you will follow every direction I give. Without question."
    lc "That's it, if you can do those two simple things we'll have no problems. Understood?"
    scene e07s01-29 mc-lc-arj-talk4_c2 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Yes, [e07_lcname!t]."
    scene e07s01-33 mc-lc-arj-talk8_c1 with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    lc "[e07_mcname!t], tell her to comply. Or else."
    scene e07s01-33 mc-lc-arj-talk8_c2 with dissolve
    play voice4 amrose_yes_confident2 noloop
    arj "Fine. [e07_lcname!t]. As long as I get to stay with [mcname]."
    scene e07s01-38 mc-lc-arj-walk1_c2 with dissolve
    play voice3 dahlia_yes_ugu noloop
    lc "Good, now face me."
    menu:
        "Continue Facing AmRose"(hint="e07s01m02c01"):
            $ e07s01_face_arj = True
            if e07s01_convince_arj is True:
                $ e07_mcname = _("Loverboy")
                $ e07_arjname = _("Fuckmeat")
            scene e07s01-30 mc-lc-arj-talk5_c1 with dissolve
            play voice2 mc_thinking_mmm3 noloop
            play voice4 amrose_happy_mmm noloop
            pause
            scene e07s01-32 mc-lc-arj-talk7_c1 with dissolve
            play voice3 dahlia_disgust_oeah noloop
            lc "I see how it is then."
            lc "You'll be [e07_arjname!t], with your little [e07_mcname!t]."
        "Turn to Face Lydia's Throne"(hint="e07s01m02c02"):

            scene e07s01-31 mc-lc-arj-talk6_c1 with dissolve
            play voice2 mc_thinking_mmm3 noloop
            play voice4 amrose_happy_mmm noloop
            pause
            scene e07s01-31 mc-lc-arj-talk6_c2 with dissolve
            play voice3 dahlia_happy_yay noloop
            lc "Very good, [e07_mcname!t]. You still have to learn your new place in the world, [e07_arjname!t]."

    jump e07s01_after_choice

label e07s01_after_choice:

    scene e07s01-36-4 mc-lc-arj-talk14_c1 with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    lc "Say it."
    scene e07s01-36-4 mc-lc-arj-talk14_c2 with dissolve
    play voice4 amrose_disappointed_oh5 noloop
    arj "I... submit. I am your...{w} slave. I'll do whatever you require..."
    scene e07s01-37 mc-lc-arj-bow_c3 with dissolve
    arj "[e07_lcname!t]."
    scene e07s01-37 mc-lc-arj-bow_c2 with dissolve
    pause
    scene e07s01-37 mc-lc-arj-bow_c1 with dissolve
    play voice3 dahlia_yes_happy noloop
    lc "Good. [e07_trname!t], take [e07_mcname!t] for his... Little gift. [e07_ahname!t], get [e07_arjname!t] into her \"outfit\"."
    scene e07s01-38 mc-lc-arj-walk1_c1 with dissolve
    pause
    scene e07s01-38 mc-lc-arj-walk1_c3 with dissolve
    pause
label replay_e07s01 hide:
    if _in_replay:
        $ renpy.music.set_volume(0.6, 0.0, "music")
        play music assey
    scene e07s01-39 mc-lc-arj-kneel1_c2 with Fade(0.5, 0.5, 0.5)
    play voice2 d1s1_mmm noloop
    mct "When Lydia said she had a surprise for me, I didn't think she meant this cock cage again..."
    scene e07s01-39 mc-lc-arj-kneel1_c1 with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    lc "Your a fan of old films. I'm a fan of old music. I'm sure you've heard this song before."
    lc "\"Face Down. Ass Up. That's the way we like to fuck\"."
    scene e07s01-40 mc-lc-arj-kneel2_c1 with dissolve
    play voice3 dahlia_no_questioning noloop
    lc "No? Doesn't ring a bell. Oh well."
    lc "Well, I want you to keep your face towards me. I don't want you looking at me - you may look at my throne."
    scene e07s01-40 mc-lc-arj-kneel2_c2 with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    lc "You may even look at my feet."
    lc "Keep that ass up, I want to see every expression on your face."
    scene e07s01-41 mc-lc-arj-kneel3_c1 with dissolve
    play voice3 dahlia_disgust_meh noloop
    lc "Show me every moment of blissful humiliation as your precious little [e07_arjname!t] plunders your booty."
    scene e07s01-41 mc-lc-arj-kneel3_c2 with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "...?!"
    scene e07s01-41-2 mc-lc-arj-kneel3_c1 with dissolve
    play voice3 dahlia_thinking_oh noloop
    lc "Oh, do you want to say something about that? You have my permission to speak."
    scene e07s01-41-2 mc-lc-arj-kneel3_c2 with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "[e07_lcname!t], with all respect, I don't... This is..."
    mct "I don't think she wants to harm me, and I definitely don't want to leave."
    mc "I'm just afraid. I would ask you to change your mind. Isn't there something else-"
    play sound sfx_double_door1
    scene e07s01-41-3 mc-lc-arj-kneel_c1 with dissolve
    play voice3 dahlia_angry_ah2 noloop
    lc "Feel free to keep talking if you want to leave... No?{w} Ah, there she is."
    scene e07s01-43 mc-lc-arj-point_c1 with dissolve
    play voice3 dahlia_happy_laugh3 noloop
    lc "Can you hear me, [e07_arjname!t]? The {u}love of your life{/u} is f-f-f-frightened. *chuckle*"
    scene e07s01-43 mc-lc-arj-point_c2 with dissolve
    play voice3 dahlia_no_nah noloop
    lc "Don't say a word. I'll tell MY worthless [e07_mcname!t] why this is happening."
    scene e07s01-42 mc-lc-arj-kneel4_c1 with dissolve
    play voice3 dahlia_angry_hm1 noloop
    lc "Let's go over the basics. You want to impress me. You want to give me pleasure. That is your purpose."
    lc "If I let him finish his request for leniency, it would show a lack of devotion. I would have no choice but to order him to leave."
    scene e07s01-44 mc-lc-arj-stand_c1 with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    lc "I think you, [e07_arjname!t], know what you have in those delicious holes of yours."
    lc "Those toys inside you are remote controlled. You will be brought to the heights of ecstasy at my whim."
    scene e07s01-45 mc-lc-arj-talk1_c1 with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    lc "So long as you ravage your poor [e07_mcname!t] so hard that it makes him cum."
    play sound sfx_heels_steps1 loop
    scene e07s01-46 mc-lc-arj-walk1_c1 with dissolve
    play voice3 dahlia_arrogant_ha noloop
    lc "Metaphorically speaking, of course. Bonus points if you can actually make him cum from fucking his ass."
    scene e07s01-46 mc-lc-arj-walk1_c2 with dissolve
    pause
    stop sound fadeout 0.5
    scene e07s01-47 mc-lc-arj-walk2_c1 with dissolve
    play voice3 dahlia_happy_wooh noloop
    lc "Let the games begin!"
    scene e07s01-47 mc-lc-arj-walk2_c2 with dissolve
    play voice3 dahlia_angry_argh1 noloop
    lc "I said, \"Begin\"!"
    scene e07s01-47 mc-lc-arj-walk2_c3 with dissolve
    pause
    scene e07s01-48 mc-lc-arj-sit_c1 with dissolve
    play voice4 amrose_disappointed_oh1 noloop
    arj "I'm sorry, [mcname]. I'm not allowed to use any lube."
    arj "I can't even spit on it or your asshole."


    $ Lovense.stop()

    scene e07s01-48 mc-lc-arj-sit_c2 with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Just. Do. It."
    play sound sfx_fisting_fist2
    $ Lovense.vibrate(5)
    scene e07s01-49 mc-lc-arj-sex1_c2 with hpunch
    play voice2 mc_pain_argh1 noloop
    mc "GAAAAAAHHHHHHHHHH!!!!!"
    scene e07s01-51 mc-lc-arj-sex3_c2 with dissolve
    play voice3 dahlia_hey_active1 noloop
    lc "Silence! I did not permit you to scream!!"
    lc "Actually, I love it when he screams in pain. It's just even more fun when he isn't permitted to do so."
    lc "That's a good start. Let's give her some additional motivation."
    scene e07s01-a49-1 with dissolve
    play sound2 sfx_sextoy_vibrator1 volume 1.5
    play sound sfx_vagina_penetration1_fast loop
    play voice4 amrose_surprised_ohmy noloop
    queue voice4 amrose_old_moaning2
    play voice2 d7s4_mcbreathing
    $ Lovense.pattern("6;10", 1400)
    arj "OH MY GODD!!!"
    scene e07s01-51 mc-lc-arj-sex3_c2 with dissolve
    play voice3 dahlia_happy_laugh1 noloop
    lc "I didn't give you permission to speak."
    lc "For now, anyway. I'm sure I'll punish you for that later."
    scene e07s01-50 mc-lc-arj-sex2_c3 with dissolve
    lc "This is delightful. Seeing [mcname]'s humiliation will never get old."
    lc "Still..."
    lc "I know this music.{w} Let's change the beat."
    scene e07s01-50 mc-lc-arj-sex2_c2 with dissolve
    play voice2 mc_pain_rrrr noloop
    queue voice2 d7s4_mcbreathing
    mct "Oh fuck... as if this literal pain in the ass wasn't humiliating enough..."
    scene e07s01-a49-2 with dissolve
    pause
    scene e07s01-a49-3 with dissolve
    pause
    play sound3 mc_cum_sound1 noloop
    $ Lovense.stop()
    $ Lovense.vibrate(16)
    scene e07s01-50 mc-lc-arj-sex2_c1 with hpunch
    play voice2 d1s5_orgasm2 noloop
    queue voice2 d7s4_mcbreathing
    mct "... some fucked up part of me is getting off on this."
    scene e07s01-51 mc-lc-arj-sex3_c1 with dissolve
    $ Lovense.pattern("6;10", 1400)
    play voice3 dahlia_disgust_oof noloop
    lc "Pathetic."
    scene e07s01-51 mc-lc-arj-sex3_c3 with dissolve
    play voice4 amrose_old_orgasming
    arj "FUUuuuuuuckkkkking again!!"
    scene e07s01-52 mc-lc-arj-talk1_c3 with dissolve
    play voice3 dahlia_happy_laugh2 noloop
    lc "Look at this slut. Grabbing her tits. Twisting her nips."
    lc "She's forgotten all about the love of her life while she pounds harder, and harder and causes him more, and more pain."
    scene e07s01-51 mc-lc-arj-sex3_c2 with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    lc "And for what? Because of the bliss of lust? Look at her - she's cum drunk."
    lc "She doesn't care about anyone or anything except her next orgasm.{w} This will be too easy."
    scene e07s01-52 mc-lc-arj-talk1_c2 with dissolve
    play voice5 pete_surprised_huh1 noloop
    pb "What will be too easy, [e07_lcname!t]?"
    scene e07s01-52 mc-lc-arj-talk1_c1 with dissolve
    play voice3 dahlia_arrogant_pff noloop
    lc "I wasn't talking to you, [e07_pbname!t]. But since you ask."
    lc "I will make her fall out of love and forget all about [mcname]."
    scene e07s01-54 mc-lc-arj-talk3_c2 with dissolve
    play voice5 pete_thinking_emm1 noloop
    pb "I'm uncertain, [e07_lcname!t]. She seems to be as devoted to him as I am to you."
    scene e07s01-53 mc-lc-arj-talk2_c1 with dissolve
    play voice3 dahlia_angry_ah2 noloop
    lc "Go away, [e07_pbname!t]. You're ruining the mood."
    scene e07s01-53 mc-lc-arj-talk2_c3 with dissolve
    play voice5 pete_yes_simple1 noloop
    pb "Yes, [e07_lcname!t].{w} My apologies, [e07_lcname!t]."
    scene e07s01-53 mc-lc-arj-talk2_c2 with dissolve
    play voice2 d9s5_auch2 noloop
    queue voice2 d7s4_mcbreathing
    mc "GRrrrrraaaahhhh!"
    $ Lovense.pattern("6;10", 700)
    scene e07s01-a49-2-f with dissolve
    mct "Make this stop. Make this stop. Please please make this stop."
    pause
    scene e07s01-a49-3-f with dissolve
    arj "Ohhhhhh close.... so close.... please..."
    pause
    scene e07s01-a49-1-f with dissolve
    pause
    play voice4 amrose_sex_orgasm1 noloop
    play voice2 mc_pain_mff5 noloop
    stop sound fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(17)
    scene e07s01-55 mc-lc-arj-talk4_c1 with hpunch
    arj "FUUUUCKKKKING HEELLLLLLLLLLL!!!"
    play voice4 amrose_sex_orgasm3 noloop
    play voice2 mc_pain_mff4 noloop
    scene e07s01-55 mc-lc-arj-talk4_c2 with vpunch
    arj "OH MY FUCKING GOD YESSSSS!!!"
    stop sound2 fadeout 1.0
    scene e07s01-56 mc-lc-arj-talk5_c1 with dissolve
    $ Lovense.vibrate(3)
    play voice4 amrose_angry_breath2 noloop
    arj "I've never felt anything like that-"
    play voice2 mc_angry_errr3 noloop
    mct "I hope I never feel anything like this ever again..."
    scene e07s01-56 mc-lc-arj-talk5_c2 with dissolve
    play voice3 dahlia_happy_phew noloop
    lc "Well, I guess that was mildly stimulating."
    scene e07s01-56 mc-lc-arj-talk5_c3 with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    lc "Still, I suppose they proved their devotion.{w}.. for now."
    $ unlock_gallery_slot("scene", "e07s01")
    play sound sfx_hands_clap3
    play sound2 ["<silence 0.2>", sfx_hands_clap4] noloop
    scene e07s01-57 mc-lc-arj-end1_c1 with dissolve
    play voice3 dahlia_arrogant_hm noloop
    lc "Slaves! Those of you still awake!"
    lc "Clean up this mess."
    scene e07s01-57 mc-lc-arj-end1_c2 with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    lc "I'll be in my bedroom - alone - for the rest of the night."
    lc "I shall not be disturbed."
    play sound sfx_heels_steps2
    scene e07s01-58 mc-lc-arj-end2_c1 with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    lc "See that these two are prepared to attend to my needs in the morning."
    play sound sfx_cloth_rustling1
    scene e07s01-58 mc-lc-arj-end2_c2 with dissolve
    play voice5 terrell_hey1 noloop
    pause

    $ Lovense.stop()


    $ renpy.end_replay()

    stop music fadeout 3.0
    jump e07s02

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
