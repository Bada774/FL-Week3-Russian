image d21s05-a62-1 = Movie(play = "images/Day-21/s07/anim/d21s07-a62-01-1-2x-50fps.webm", start_image = "d21s07-a62-01-1 jdg-baf-mc-bj-two-01")
image d21s05-a62-1-f = Movie(play = "images/Day-21/s07/anim/d21s07-a62-01-1-2x-60fps.webm", start_image = "d21s07-a62-01-1 jdg-baf-mc-bj-two-01")
image d21s05-a62-2 = Movie(play = "images/Day-21/s07/anim/d21s07-a62-01-2-2x-50fps.webm", start_image = "d21s07-a62-01-2 jdg-baf-mc-bj-two-01")
image d21s05-a62-2-f = Movie(play = "images/Day-21/s07/anim/d21s07-a62-01-2-2x-60fps.webm", start_image = "d21s07-a62-01-2 jdg-baf-mc-bj-two-01")
image d21s05-a62-3 = Movie(play = "images/Day-21/s07/anim/d21s07-a62-01-3-2x-50fps.webm", start_image = "d21s07-a62-01-3 jdg-baf-mc-bj-two-01")
image d21s05-a62-3-f = Movie(play = "images/Day-21/s07/anim/d21s07-a62-01-3-2x-60fps.webm", start_image = "d21s07-a62-01-3 jdg-baf-mc-bj-two-01")
image d21s05-a62-4 = Movie(play = "images/Day-21/s07/anim/d21s07-a62-02-1-2x-50fps.webm", start_image = "d21s07-a62-02-1 jdg-baf-mc-bj-two-hard-01")
image d21s05-a62-4-f = Movie(play = "images/Day-21/s07/anim/d21s07-a62-02-1-2x-60fps.webm", start_image = "d21s07-a62-02-1 jdg-baf-mc-bj-two-hard-01")
image d21s05-a62-5 = Movie(play = "images/Day-21/s07/anim/d21s07-a62-02-2-2x-50fps.webm", start_image = "d21s07-a62-02-2 jdg-baf-mc-bj-two-hard-01")
image d21s05-a62-5-f = Movie(play = "images/Day-21/s07/anim/d21s07-a62-02-2-2x-60fps.webm", start_image = "d21s07-a62-02-2 jdg-baf-mc-bj-two-hard-01")
image d21s05-a62-6 = Movie(play = "images/Day-21/s07/anim/d21s07-a62-02-3-2x-50fps.webm", start_image = "d21s07-a62-02-3 jdg-baf-mc-bj-two-hard-01")
image d21s05-a62-6-f = Movie(play = "images/Day-21/s07/anim/d21s07-a62-02-3-2x-60fps.webm", start_image = "d21s07-a62-02-3 jdg-baf-mc-bj-two-hard-01")

label d21s07:

    $ d21s07_sex_dungeon = False
    $ d21s07_fuck_judge = False
    $ ntr_lc_guilty = False
    $ lc_lc_guilty = False
    $ d21s07_engagement = False
    $ d21s07_still_dating = False
    $ d21s07_from_ending = False
    $ d21s07_last_menu = None

    if cage_ntr is True:
        $ ntr_lc_guilty = True
    elif d21s03_statement_2 is True:
        $ lc_lc_guilty = True

    $ d21s07_is_dungeon_available = date_dd and date_sy and cage_ntr is True and date_arj_romance is False and d21s03_statement_1 and d21s07_from_ending is False
    $ d21s07_is_harem_available = date_sy and date_mes and cage_ntr is False and d20s09_lc_love > 2 and d21s03_statement_2 is False and (d19s01lc_kiss is True or d19s01lc_talk_nice is True) and d21s07_from_ending is False
    $ d21s07_is_stacy_available = d21s02_bring_sy and date_sy and d21s07_from_ending is False

    $ d21s07_arj_points = d14s03_arj_kiss + d16s02_arj_eatout + (d16s03_lie_to_lc is False) + (d16s03_arj_watch is False or d16s03_refuse_lc) + d16s10_talk_future
    $ d21s07_is_amrose_available = d21s02_bring_arj and date_arj_romance and d21s07_arj_points >= 3 and d21s07_from_ending is False

    scene black
    show screen scene_transistion(_("Several Weeks Later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.35, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 5.0, "sound2" )
    play music vidala_en_verde fadein 3.0
    scene d21s07-01 jdg-def-p-lc-hr-baf-start1_c3
    with Fade(0.5, 0.5, 0.9)
    play voice3 lydia_hmmmm noloop
    lc "That was when my boyfriend-"
    scene d21s07-01 jdg-def-p-lc-hr-baf-start1_c2 with dissolve
    play voice4 claudie_thinking_hmm2 noloop
    "Defense Attorney" "That would be [mcname] Young?"

    $ fl_achievement_unlock("d21s07n01")
    $ unlock_gallery_slot("extra", "d21s07n01")

    scene d21s07-02 jdg-def-p-lc-hr-baf-mc-start2_c3 with dissolve
    play voice3 lydia_lydyes noloop
    lc "Yes, we were taking a shower together and [mcname] Young told me-"
    play sound sfx_door_open5
    scene d21s07-02 jdg-def-p-lc-hr-baf-mc-start2_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Um, sorry."
    scene d21s07-06 jdg-def-p-lc-hr-baf-mc-talk1_c2 with dissolve
    play voice4 claudie_yes_unsure noloop
    "Defense Attorney" "Please continue, Miss Cox."
    scene d21s07-03 jdg-def-p-lc-hr-baf-mc-entry1_c3 with dissolve
    play voice3 lydia_aga noloop
    lc "Yes, of course. That was [mcname] Young told me about Fetish Locator's dark secret."
    scene d21s07-02 jdg-def-p-lc-hr-baf-mc-start2_c2 with dissolve
    play voice4 claudie_thinking_hmm1 noloop
    "Defense Attorney" "And what was that secret, in your opinion?"
    scene d21s07-04 jdg-def-p-lc-hr-baf-mc-entry2_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "*whispers* Sorry I'm late. What did I miss?"
    scene d21s07-04 jdg-def-p-lc-hr-baf-mc-entry2_c5 with dissolve
    play voice3 hana_hmm noloop
    hr "*whispers* Your girlfriend is up there crying crocodile tears. A jury might have bought it, but the judge won't fall for that."
    play sound sfx_cloth_rustling1
    scene d21s07-05 jdg-def-p-lc-hr-baf-mc-entry3_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    if cage_ntr is True:
        mc "*whispers* I think we broke up. If we were ever really dating..."
    else:
        mc "*whispers* Did it ever occur to you that she might be telling the truth - from her point of view."
    scene d21s07-05 jdg-def-p-lc-hr-baf-mc-entry3_c5 with dissolve
    play voice3 hana_argh noloop
    hr "*whispers* Whatever."
    scene d21s07-01 jdg-def-p-lc-hr-baf-start1_c4 with dissolve
    play voice4 aaleyah_thinking_hmm1 noloop
    jdg "I will ask once for silence in this courtroom. If I have to ask again I will have the bailiff remove the audience."
    scene d21s07-21 jdg-def-p-lc-hr-baf-mc-grill12_c4 with dissolve
    play voice5 boy4_angry_cough3 noloop
    "Bailiff" "SILENCE IN THE COURTROOM."
    scene d21s07-02 jdg-def-p-lc-hr-baf-mc-start2_c4 with dissolve
    play voice4 nora_aga noloop
    jdg "Thank you. Please continue."
    scene d21s07-08 jdg-def-p-lc-hr-baf-mc-talk3_c2 with dissolve
    play voice5 claudie_arrogant_hm noloop
    "Defense Attorney" "I think that is sufficient. No further questions, your honor."
    scene d21s07-08 jdg-def-p-lc-hr-baf-mc-talk3_c3 with dissolve
    play voice3 lydia_moan1 noloop
    lc "Does that mean I can leave?"
    scene d21s07-08 jdg-def-p-lc-hr-baf-mc-talk3_c4 with dissolve
    play voice4 aaleyah_no_no3 noloop
    jdg "Remain seated.{w} Prosecutor, would you like to cross examine the witness?"
    play sound sfx_chair_slide1
    scene d21s07-09 jdg-def-p-lc-hr-baf-mc-talk4_c2 with dissolve
    pause
    scene d21s07-10 jdg-def-p-lc-hr-baf-mc-grill1_c2 with dissolve
    play voice5 pete_yes_yeah noloop
    "Prosecutor" "I would, your honor.{w} Miss Cox, you testified that you did not know what Mister Skinner was doing."
    scene d21s07-10 jdg-def-p-lc-hr-baf-mc-grill1_c3 with dissolve
    play voice3 dahlia_surprised_huh2 noloop
    lc "Who?"
    scene d21s07-12 jdg-def-p-lc-hr-baf-mc-grill3_c2 with dissolve
    play voice5 pete_thinking_hmm10 noloop
    "Prosecutor" "Jerome Skinner. Your co-defendant and the man you claim was the mastermind behind \"Fetish Locator\"."
    scene d21s07-12 jdg-def-p-lc-hr-baf-mc-grill3_c3 with dissolve
    play voice3 dahlia_surprised_oh noloop
    lc "Oh, correct. He created and controlled that horrible app without my knowledge or consent."
    scene d21s07-14 jdg-def-p-lc-hr-baf-mc-grill5_c2 with dissolve
    play voice5 pete_yes_ugu2 noloop
    "Prosecutor" "So, you had no reason to be in the campus server room which happened to administer that app?"
    scene d21s07-14 jdg-def-p-lc-hr-baf-mc-grill5_c3 with dissolve
    play voice3 dahlia_no_high3 noloop
    lc "No, of course not.{w} I'm a music major."
    scene d21s07-15 jdg-def-p-lc-hr-baf-mc-grill6_c2 with dissolve
    play voice5 pete_thinking_hmm7 noloop
    "Prosecutor" "So, you did not gain the access codes to that room a semester prior to the \"app's\" launch - as a prior witness testified?"
    scene d21s07-07 jdg-def-p-lc-hr-baf-mc-talk2_c3 with dissolve
    play voice3 lydia_uhuh noloop
    lc "I have no recollection of that."
    scene d21s07-12 jdg-def-p-lc-hr-baf-mc-grill3_c2 with dissolve
    play voice5 pete_thinking_eeh1 noloop
    "Prosecutor" "And on that day when Mister Young informed you - in the shower - about Fetish Locator's nefarious actions...{w} You were not present in the server room as another witness has testified?"
    scene d21s07-10 jdg-def-p-lc-hr-baf-mc-grill1_c3 with dissolve
    play voice3 dahlia_no_high1 noloop
    lc "No, sir."
    scene d21s07-14 jdg-def-p-lc-hr-baf-mc-grill5_c2 with dissolve
    play voice5 pete_happy_mmm1 noloop
    "Prosecutor" "And after the server room was sealed by investigators you did not enter the server room and delete evidence?"
    scene d21s07-14 jdg-def-p-lc-hr-baf-mc-grill5_c3 with dissolve
    play voice3 dahlia_no_serious noloop
    lc "Of course not!"
    scene d21s07-15 jdg-def-p-lc-hr-baf-mc-grill6_c2 with dissolve
    play voice5 pete_arrogant_heh1 noloop
    "Prosecutor" "Your fingerprints were found throughout the administrator section of that server room by investigators. How do you explain that?"
    scene d21s07-15 jdg-def-p-lc-hr-baf-mc-grill6_c3 with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    lc "They were?"
    scene d21s07-15 jdg-def-p-lc-hr-baf-mc-grill6_c1 with dissolve
    play voice5 claudie_hey_angry noloop
    "Defense Attorney" "Objection, your honor! Defense was not made aware of any fingerprints."
    scene d21s07-15 jdg-def-p-lc-hr-baf-mc-grill6_c4 with dissolve
    play voice4 nora_angrymoan noloop volume 2.0
    jdg "Overruled. They were entered into evidence and made available to you during discovery."
    scene d21s07-14 jdg-def-p-lc-hr-baf-mc-grill5_c1 with dissolve
    play voice5 claudie_surprised_huh2 noloop
    "Defense Attorney" "I never saw anything about this!"
    scene d21s07-16 jdg-def-p-lc-hr-baf-mc-grill7_c4 with dissolve
    play voice4 nora_hmm noloop volume 1.6
    jdg "Did you sleep through the testimony by the fingerprint expert?{w} OVERRULED."
    scene d21s07-19 jdg-def-p-lc-hr-baf-mc-grill10_c2 with dissolve
    play voice5 pete_thinking_mmf noloop
    "Prosecutor" "As I was saying, Miss Cox. How do you explain your fingerprints in that server room?"
    scene d21s07-12 jdg-def-p-lc-hr-baf-mc-grill3_c3 with dissolve
    play voice3 lydia_oops noloop
    lc "I...{w} Alright, I was there, but it wasn't what you think!"
    if cage_ntr is True:
        lc "Pete would take me there to have sex. I didn't realize it was the same room."
        scene d21s07-15 jdg-def-p-lc-hr-baf-mc-grill6_c2 with dissolve
        play voice5 pete_yes_simple1 noloop
        "Prosecutor" "We are well aware of Mister Butler's involvement. He has already plead guilty and testified against both of you."
        "Prosecutor" "But that doesn't explain why your fingerprints were found on the server administrator's keyboard."
        scene d21s07-14 jdg-def-p-lc-hr-baf-mc-grill5_c3 with dissolve
        play voice3 dahlia_disappointed_ehh3 noloop
        lc "Um...{w} Oh! Sometimes we watched videos while getting intimate. That's probably how my fingerprints got on that keyboard."
    else:
        lc "I did go to that room, but only after [mcname] told me about it. I was trying to shut it down!"
    scene d21s07-12 jdg-def-p-lc-hr-baf-mc-grill3_c2 with dissolve
    play voice5 pete_no_uhuh noloop
    "Prosecutor" "Uh huh. So, when you said you never went to that room... were you lying then or are you lying now?"
    scene d21s07-13 jdg-def-p-lc-hr-baf-mc-grill4_c3 with dissolve
    play voice3 lydia_oof noloop
    lc "I...{w} I made a mistake."
    scene d21s07-15 jdg-def-p-lc-hr-baf-mc-grill6_c2 with dissolve
    play voice5 pete_thinking_hmm8 noloop
    "Prosecutor" "Would you have continued lying to this court if you hadn't been aware of the fingerprint evidence?"
    scene d21s07-15 jdg-def-p-lc-hr-baf-mc-grill6_c1 with dissolve
    play voice4 claudie_angry_eh noloop
    "Defense Attorney" "Objection!"
    scene d21s07-19 jdg-def-p-lc-hr-baf-mc-grill10_c2 with dissolve
    play voice5 pete_arrogant_hm2 noloop
    "Prosecutor" "Withdrawn. No further questions."
    scene d21s07-18 jdg-def-p-lc-hr-baf-mc-grill9_c4 with dissolve
    play voice4 aaleyah_thinking_hmm2 noloop
    jdg "Defense, redirect?"
    scene d21s07-14 jdg-def-p-lc-hr-baf-mc-grill5_c1 with dissolve
    play voice5 claudie_no_simple noloop
    "Defense Attorney" "No, your honor.{w} No further questions for this witness."
    scene d21s07-20 jdg-def-p-lc-hr-baf-mc-grill11_c4 with dissolve
    play voice4 aaleyah_disappointed_mff noloop
    jdg "You may step down, Miss Cox. In fact, would a guard please escort this defendant someplace where she can wash her face?"
    scene d21s07-19 jdg-def-p-lc-hr-baf-mc-grill10_c3 with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    lc "Thank you, your honor."
    if cage_ntr is False and date_jdg is False:
        scene d21s07-30 jdg-p-baf-mc-talk1_c4 with dissolve
        play voice4 aaleyah_yes_aga4 noloop
        jdg "We are going to take a 1 hour recess, then return for closing arguments."
        play sound sfx_court_hammer1
        scene d21s07-72 jdg-def-p-lc-hr-baf-mc-closing3_c5 with dissolve
        play voice3 hana_argh2 noloop
        hr "I'm so excited to see that bitch hang. I hope the judge throws the book at her."
        scene d21s07-72 jdg-def-p-lc-hr-baf-mc-closing3_c1 with dissolve
        play voice2 d2s9_mchey noloop
        mc "Watch it. That's my girlfriend you're talking about."
        scene d21s07-73 jdg-def-p-lc-hr-baf-mc-closing4_c5 with dissolve
        play voice3 hana_hmm2 noloop
        hr "So, you don't want to find someplace to have a quickie during this break?"
        scene d21s07-73 jdg-def-p-lc-hr-baf-mc-closing4_c1 with dissolve
        play voice2 mc_no_no5 noloop
        if lc_lc_guilty is True:
            mc "No, I'm too nauseous. I feel like I betrayed her."
        else:
            mc "No, I'm too worried about the verdict. I hope she's not guilty."
        scene d21s07-74 jdg-def-p-lc-hr-baf-mc-closing5_c5 with dissolve
        play voice3 hana_yeah2 noloop
        hr "Really? After what she did to you? All those people that she hurt."
        scene d21s07-75 jdg-def-p-lc-hr-baf-mc-closing6_c1 with dissolve
        play voice2 mc_hey_hey2 noloop
        mc "She wasn't the app. Jerome was behind all that awful shit."
        scene d21s07-76 jdg-def-p-lc-hr-baf-mc-closing7_c5 with dissolve
        play voice3 hana_argh noloop
        hr "Disagree.{w} We'll just have to see how the judge feels about that."
        scene d21s07-76 jdg-def-p-lc-hr-baf-mc-closing7_c1 with dissolve
        play voice2 mc_yes_aga1 noloop
        mc "That's what I'm worried about."

        jump d21s07_closing
    else:

        scene d21s07-30 jdg-p-baf-mc-talk1_c4 with dissolve
        play voice4 aaleyah_happy_mmm2 noloop
        jdg "Is Mr [mcname] Young in attendance?"
        scene d21s07-23 jdg-def-p-lc-hr-baf-mc-speak2_c5 with dissolve
        play voice2 mc_yes_yes3 noloop
        mc "Yes, your honor."
        scene d21s07-18 jdg-def-p-lc-hr-baf-mc-grill9_c4 with dissolve
        play voice4 aaleyah_yes_aga4 noloop
        jdg "We are going to take a 1 hour recess, then return for closing arguments."
        if d21s07_is_dungeon_available is True:
            jdg "[mcname] Young, please remain. Prosecutor, please remain as well."
        else:
            jdg "[mcname] Young, please remain."
        jdg "Bailiff, please escort everyone else out."
        play sound sfx_court_hammer1
        scene d21s07-22 jdg-def-p-lc-hr-baf-mc-speak1_c4 with dissolve
        play voice5 boy4_angry_cough4 noloop
        "Bailiff" "You heard the Judge!{w} EVERYBODY MOVE!!!"
        if d21s07_is_dungeon_available is True:
            jump d21s07_offer
        elif is_extended_edition is True and d18s11_surprise_jdg is True:
            jump d21s07_jdg_quickie
        else:
            scene d21s07-46 jdg-p-baf-mc-talk16_c2 with fade
            play voice2 mc_yes_yeah8 noloop
            mc "Yes, your honor? You wanted to see me?"
            scene d21s07-46 jdg-p-baf-mc-talk16_c4 with dissolve
            play voice4 nora_heh noloop
            jdg "I just wanted you to know that if things were slightly different there right now we'd be talking about a very interesting offer."
            scene d21s07-50 jdg-mc-l1_c2 with dissolve
            play voice2 mc_arrogant_huh1 noloop
            mc "If things were different?"
            scene d21s07-50 jdg-mc-l1_c4 with dissolve
            play voice4 aaleyah_yes_yes4 noloop
            jdg "Yes. Have you heard of indentured servitude?"
            scene d21s07-52 jdg-mc-l2_c2 with dissolve
            play voice2 mc_arrogant_heh3 noloop
            mc "You mean slavery?"
            scene d21s07-52 jdg-mc-l2_c4 with dissolve
            play voice4 aaleyah_yes_yep noloop
            jdg "Similar concept, but slavery is illegal and immoral."
            jdg "The prosecutor extended an offer to Miss Cox to serve her time under house arrest with a personal warden. Someone to oversee her punishments."
            jdg "Miss Cox said she would only agree if you were assigned as the warden."
            scene d21s07-53 jdg-mc-l3_c2 with dissolve
            play voice2 mc_surprised_what2 noloop
            mc "What? Really?"
            scene d21s07-52 jdg-mc-l2_c4 with dissolve
            play voice4 aaleyah_yes_yes1 noloop
            jdg "Yes, but the investigation into your background was disappointing..."
            play voice2 mc_pain_ou1 noloop
            mc "Oh, shit. Am I in trouble?"
            jdg "Quite the opposite. The prosecutor decided you were too nice of a person."
            scene d21s07-50 jdg-mc-l1_c2 with dissolve
            play voice2 d1s2_hmm noloop volume 1.6
            mc "Too... nice?"
            play voice4 aaleyah_disappointed_mff2 noloop
            jdg "You were not found suitable to administer a private prison."
            mc "Oh, so... is there anything I could do?"
            scene d21s07-50 jdg-mc-l1_c4 with dissolve
            play voice4 nora_pleasure noloop
            jdg "Maybe next time. Your next life, maybe. Who knows? That's the way things go."
            play voice2 mc_angry_hm2 noloop
            mct "Did she just quote the Matrix?{w} Whoa."
            scene d21s07-46 jdg-p-baf-mc-talk16_c4 with dissolve
            play voice4 aaleyah_happy_mmm1 noloop
            jdg "Anyway, you can go. I just wanted you to know that it was close."
            play voice2 mc_arrogant_heh2 noloop
            mc "You just wanted me to know... about a missed opportunity that I can't do anything about now?"
            jdg "Exactly."
            mc "Uh, okay."

            jump d21s07_closing

label d21s07_offer:

    scene d21s07-30 jdg-p-baf-mc-talk1_c4 with fade
    play voice4 aaleyah_thinking_hmm1 noloop
    jdg "Prosecutor, Mr. Young, please approach the bench."
    scene d21s07-30 jdg-p-baf-mc-talk1_c2 with dissolve
    play voice5 pete_yes_ugu1 noloop
    "Prosecutor" "Of course, your honor."
    play sound sfx_heels_steps1
    scene d21s07-32 jdg-p-baf-mc-talk2_c2 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Um, sure... What's this about?"
    scene d21s07-32 jdg-p-baf-mc-talk2_c4 with dissolve
    play voice4 aaleyah_disappointed_mff2 noloop
    jdg "I'll let the Prosecutor explain."
    scene d21s07-33 jdg-p-baf-mc-talk3_c2 with dissolve
    play voice5 pete_thinking_hmm11 noloop
    "Prosecutor" "You've been watching the trial. You have some idea about how the case is going for your girlfriend."
    "Prosecutor" "I have offered Miss Cox an unconventional alternative to prison."
    "Prosecutor" "I'm sure you have heard of private prisons."
    play voice2 mc_no_uhuh1 noloop
    mc "Uh huh."
    scene d21s07-33 jdg-p-baf-mc-talk3_c4 with dissolve
    play voice5 pete_happy_mmm2 noloop
    "Prosecutor" "And I'm sure you've heard of house arrest."
    play voice2 mc_yes_sure1 noloop
    mc "Well, sure."
    stop sound fadeout 1.0
    scene d21s07-34 jdg-p-baf-mc-talk4_c2 with dissolve
    play voice5 pete_happy_relief1 noloop
    "Prosecutor" "Well, in rare cases such as this we have the opportunity for a combination thereof."
    play voice2 mc_angry_hm1 noloop
    mc "I don't understand."
    scene d21s07-37 jdg-p-baf-mc-talk7_c4 with dissolve
    play voice4 nora_pleasure noloop
    jdg "The basic concept is that Lydia Cox would be placed in a private prison in her own home, but with you as the warden."
    scene d21s07-37 jdg-p-baf-mc-talk7_c5 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "I'm sorry, what?!"
    scene d21s07-38 jdg-p-baf-mc-talk8_c2 with dissolve
    play voice5 pete_arrogant_heh2 noloop
    "Prosecutor" "As one of the aggrieved victims of her malfeasance you are eligible to serve as warden of her house arrest."
    play voice2 d2s9_confused noloop volume 1.5
    mc "So, I would be responsible for keeping her fed and making sure she stays within the property limits?"
    play voice5 pete_happy_laugh1 noloop
    "Prosecutor" "*chuckle* Have you seen what private prisons feed their inmates? You could let her starve if you want."
    scene d21s07-37 jdg-p-baf-mc-talk7_c4 with dissolve
    play voice4 aaleyah_happy_mmm1 noloop
    jdg "There would be an electronic implant - much better than those old ankle bracelets - to ensure she stayed within her property limits."
    scene d21s07-38 jdg-p-baf-mc-talk8_c2 with dissolve
    play voice5 pete_surprised_ah noloop
    "Prosecutor" "She would remain responsible for paying any bills associated with her incarceration. You'd basically get to live there, get paid for it, and punish her however you see fit."
    "Prosecutor" "It's a reasonable deal. She would only serve 8 years. She'll be 30 when you are done with her."
    scene d21s07-38 jdg-p-baf-mc-talk8_c5 with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "Wait! So, you're going to find her guilty?"
    scene d21s07-39 jdg-p-baf-mc-talk9_c4 with dissolve
    play voice4 nora_angrymoan noloop
    jdg "I can't say what the verdict will be until it is public and official. Besides, I still haven't heard the closing arguments."
    scene d21s07-38 jdg-p-baf-mc-talk8_c5 with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "I can't believe this! Why me?"
    scene d21s07-39 jdg-p-baf-mc-talk9_c2 with dissolve
    play voice5 pete_thinking_hmm2 noloop
    "Prosecutor" "Well, there are three types of victims in this case."
    "Prosecutor" "One group of victims actually liked what happened to them, which makes them unacceptable to me."
    "Prosecutor" "Another group of victims want vengeance - preferably aggressive & violent."
    scene d21s07-36 jdg-p-baf-mc-talk6_c5 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Are those unacceptable to you as well?"
    scene d21s07-38 jdg-p-baf-mc-talk8_c2 with dissolve
    play voice5 pete_happy_laugh2 noloop
    "Prosecutor" "*chuckle* Heavens No, but there's no way to convince her to choose that over jail."
    play voice2 mc_thinking_emm1 noloop
    mc "I assume there's a third group."
    "Prosecutor" "The third group is just you."
    scene d21s07-41 jdg-p-baf-mc-talk11_c2 with dissolve
    play voice5 pete_arrogant_hm1 noloop
    "Prosecutor" "Miss Cox has already signed the paperwork for the plea deal on the condition that you are her warden."
    "Prosecutor" "She believes that she can manipulate you, but I'm willing to bet you'll turn the tables on her."
    scene d21s07-42 jdg-p-baf-mc-talk12_c2 with dissolve
    play voice2 mc_angry_huh1 noloop
    mc "This is insane."
    scene d21s07-37 jdg-p-baf-mc-talk7_c4 with dissolve
    play voice4 aaleyah_no_no1 noloop
    jdg "I can assure you that the offer is completely legal."
    scene d21s07-45 jdg-p-baf-mc-talk15_c5 with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "You're asking me to devote the next 8 years of my life to being her warden?"
    scene d21s07-38 jdg-p-baf-mc-talk8_c2 with dissolve
    play voice5 pete_hey_attention noloop
    "Prosecutor" "Living rent free, getting paid for it, and otherwise doing whatever you want."
    scene d21s07-38 jdg-p-baf-mc-talk8_c4 with dissolve
    play voice4 aaleyah_yes_yeah3 noloop
    jdg "Of course, there will be health & wellness checks every 6 months, but you'll be allowed to schedule those whenever it is convenient."
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "What you're asking is immoral, unethical, and completely wrong in every possible way."
    play voice5 pete_thinking_oh2 noloop
    "Prosecutor" "Perhaps, but consider the alternative."
    if is_antagonist_mode is True:
        "Prosecutor" "Women's prisons are few and far between - and massively overcrowded."
        "Prosecutor" "If she's lucky enough to get into a women's prison she'll be in gen pop with everyone from insider stock traders to convicted mass murderers."
        "Prosecutor" "More likely, she'll be assigned to either a women's wing or a coed wing of a minimum security prison."
        "Prosecutor" "Sure, she won't be side-by-side with murderers, but she's a pretty girl and... you know how it is."
    scene d21s07-38 jdg-p-baf-mc-talk8_c2 with dissolve
    play voice2 d3s7_mcemm noloop
    mc "I need a few minutes to think about it."
    scene d21s07-39 jdg-p-baf-mc-talk9_c4 with dissolve
    play voice4 aaleyah_yes_aga1 noloop
    jdg "Take your time, but I recommend that you don't leave the room."
    play voice5 pete_disappointed_mmm1 noloop
    "Prosecutor" "If you are going to take advantage of this offer, I need your signature on these papers before the end of the recess."
    scene d21s07-36 jdg-p-baf-mc-talk6_c5 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Recess? Makes me feel like a kid again."
    scene d21s07-41 jdg-p-baf-mc-talk11_c4 with dissolve
    play voice4 aaleyah_disappointed_eeh noloop
    jdg "Mr Prosecutor... Phil, would you be so kind as to leave the paperwork and exit. I would like to have a conversation with this Young man."
    scene d21s07-45 jdg-p-baf-mc-talk15_c2 with dissolve
    play voice5 pete_yes_simple1 noloop
    "Prosecutor" "Of course, your honor."
    scene d21s07-45 jdg-p-baf-mc-talk15_c4 with dissolve
    play voice4 aaleyah_hey_hey1 noloop
    jdg "Don't worry about the bailiff. They're completely loyal to me."
    jdg "*chuckle* I could murder you and they'd clean up the body and the mess before court resumes."
    scene d21s07-46 jdg-p-baf-mc-talk16_c2 with dissolve
    play voice2 mc_scared_oh2 noloop
    mc "That's terrifying."
    scene d21s07-46 jdg-p-baf-mc-talk16_c4 with dissolve
    play voice4 aaleyah_happy_laugh2 noloop
    jdg "Relax. I only want to tell you something you shouldn't know."
    scene d21s07-50 jdg-mc-l1_c2 with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Okay."
    scene d21s07-50 jdg-mc-l1_c4 with dissolve
    play voice4 aaleyah_disappointed_eh1 noloop
    jdg "Lydia is going away for a long, long time. Jerome too."
    jdg "Jerome is a piece of shit, but if you want to... well, sign the papers."
    scene d21s07-52 jdg-mc-l2_c2 with dissolve
    play voice2 mc_surprised_wow1 noloop
    mc "Wow. That's..."
    scene d21s07-52 jdg-mc-l2_c4 with dissolve
    play voice4 aaleyah_angry_hm1 noloop
    jdg "I'm sorry, did you hear something?"
    play voice5 boy5_no_angry noloop
    "Bailiff" "No, your honor. Just a fly on the wall."
    scene d21s07-53 jdg-mc-l3_c2 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "When it says that I can perform any punishments that I see fit..."
    scene d21s07-53 jdg-mc-l3_c4 with dissolve
    play voice4 aaleyah_yes_yeah1 noloop
    jdg "Use your imagination."
    if is_extended_edition is True and d18s11_surprise_jdg is True:
        jdg "While you decide...{w} don't mind me."
        jump d21s07_jdg_quickie
    else:
        jump d21s07_offer_p2

label replay_d21s07:
label d21s07_jdg_quickie:

    play sound sfx_skirt_off2
    if _in_replay:
        $ renpy.music.set_volume(0.35, 3.0, "music" )
    play music vidala_en_verde fadein 3.0
    scene d21s07-55 jdg-mc-talk1_c1 with fade
    play voice4 aaleyah_closed_moan3 noloop
    jdg "I'm just going to take a moment for myself."
    scene d21s07-56 jdg-mc-talk2_c2 with dissolve
    play voice4 nora_heh noloop
    jdg "Do you ever think about it? The people who stand trial here before me?"
    jdg "The defendants. Most confessed for a plea deal, but every once in a while I get a real case like this one."
    play sound sfx_skirt_off1
    scene d21s07-57 jdg-mc-talk3_c2 with dissolve
    play voice4 nora_oh noloop
    jdg "Their fear and anxiety? While some justice of the peace holds their fate in their hands?"
    jdg "Sure, I don't get to actually see the punishments. I have to stay impartial."
    jdg "But sometimes - late at night - I can't help jilling myself off to fantasies."
    scene d21s07-58 jdg-mc-talk4_c2 with dissolve
    play voice4 aaleyah_closed_moan1 noloop
    jdg "Come over here. I want you to shove your cock down my throat."
    scene d21s07-58 jdg-mc-talk4_c1 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "You want me to pretend to rape you right here on the defense table?"
    scene d21s07-58 jdg-mc-talk4_c2 with dissolve
    play voice4 aaleyah_no_uhuh noloop
    jdg "Just my mouth. We don't have time for more."
    scene d21s07-58 jdg-mc-talk4_c1 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "You're just going to watch?"
    play voice5 boy5_arrogant_yeah noloop
    "Bailiff" "Pretend I'm not even here."
    menu:
        "Facefuck the Judge During Recess"(hint="d21s07m01c01"):
            $ d21s07_fuck_judge = True

            play voice2 mc_yes_okay2 noloop
            mc "Okay then."
            scene d21s07-58 jdg-mc-talk4_c2 with dissolve
            play voice4 aaleyah_disappointed_eeh2 noloop
            jdg "It's such a shame we don't have time for more."
            play voice2 d1s5_mcthinks noloop volume 1.7
            mc "You're the judge. I'm pretty sure recess doesn't end until you say so."
            play voice4 aaleyah_closed_moan5 noloop
            jdg "True.{w} Now, show me that hard cock."
            scene d21s07-60 jdg-baf-mc-blowjob_c1 with dissolve
            play voice4 aaleyah_closed_moan4 noloop
            jdg "God damn. I've never really taken the time to admire your manhood before."
            jdg "Impressive. You must have women lining up to fuck your magnificent cock."
            scene d21s07-60 jdg-baf-mc-blowjob_c2 with dissolve
            play voice2 mc_arrogant_nah1 noloop
            mc "Well, kinda."
            mc "Anyway, I think it's time you shut up now."
            play voice4 samiya_mfff noloop
            scene d21s07-a62-02-3 jdg-baf-mc-bj-two-hard-01 with dissolve
            play voice2 mc_happy_oof1 noloop
            mc "Damn. There is something to be said for an experienced woman."
            $ renpy.music.set_volume(0.75, 3.0, "music" )
            play voice4 aaleyah_sucking_soft
            play voice2 d7s4_mcbreathing
            scene d21s05-a62-6
            pause
            scene d21s05-a62-4 with dissolve
            pause
            scene d21s05-a62-2 with dissolve
            pause
            scene d21s05-a62-1 with dissolve
            pause
            scene d21s05-a62-3 with dissolve
            mc "I'm going to cummm so far down your throat!"
            pause
            scene d21s05-a62-5 with dissolve
            pause
            play voice4 aaleyah_sucking_deep
            scene d21s05-a62-6-f with dissolve
            pause
            scene d21s05-a62-4-f with dissolve
            pause
            scene d21s05-a62-2-f with dissolve
            pause
            scene d21s05-a62-1-f with dissolve
            pause
            play voice2 mc_happy_laugh1 noloop
            scene d21s05-a62-3-f with dissolve
            queue voice2 d7s4_mcbreathing
            mc "FUCK YES YOU PSYCHOPATHIC BITCH!!!"
            pause
            scene d21s05-a62-5-f with dissolve
            pause
            play voice2 mc_pain_argh1 noloop
            play voice4 aaleyah_closed_moan6 noloop
            scene d21s07-62 jdg-baf-mc-blowjob2_c4 with hpunch
            mc "FUCCKCKCKCKCCKKCCKCKCKCKKK"
            play voice4 samiya_mfff3 noloop
            with hpunch
            scene d21s07-60 jdg-baf-mc-blowjob_c4 with dissolve
            play voice2 mc_happy_oof2 noloop
            mc "Hell yes.{w} I could do this all day."
            scene d21s07-60 jdg-baf-mc-blowjob_c2 with dissolve
            play voice5 boy5_thinking_hmm1 noloop
            "Bailiff" "You might want to let her breathe.{w} So I don't have to shoot you."
            $ renpy.music.set_volume(0.35, 3.0, "music" )
            scene d21s07-57 jdg-mc-talk3_c2 with dissolve
            play voice4 aaleyah_surprised_ohmy noloop
            jdg "So close...{w} I was so close..."
            scene d21s07-58 jdg-mc-talk4_c1 with dissolve
            play voice2 mc_arrogant_huh1 noloop
            mc "To an orgasm?"
            play voice4 aaleyah_angry_cagh1 noloop
            jdg "I was either going to cum or pass out."
            play voice5 boy5_disappointed_oh1 noloop
            "Bailiff" "Apologies for interrupting, your honor."

            $ fl_achievement_unlock("d21s07n02")
            $ unlock_gallery_slot("extra", "d21s07n02")

            scene d21s07-57 jdg-mc-talk3_c2 with dissolve
            play voice4 aaleyah_closed_moan2 noloop
            jdg "Either way, thank you."
            jdg "Thank you both."
            $ unlock_gallery_slot("scene", "d21s07")
        "Refuse Her Request"(hint="d21s07m01c02"):

            scene d21s07-57 jdg-mc-talk3_c1 with dissolve
            play voice2 mc_no_no5 noloop
            mc "No thanks, I'm good."
            scene d21s07-57 jdg-mc-talk3_c2 with dissolve
            play voice4 aaleyah_closed_moan5 noloop
            jdg "Well, I hope you don't mind if I continue solo..."
            scene d21s07-55 jdg-mc-talk1_c4 with dissolve
            play voice2 mc_yes_yeah4 noloop
            mc "Go right ahead."
            mct "How did a psychopathic bitch like her get to be a judge?"

    $ renpy.end_replay()

    if d21s07_is_dungeon_available is True:
        jump d21s07_offer_p2
    else:
        jump d21s07_closing

label ending_04_return hide:
label d21s07_offer_p2:

    scene d21s07-50 jdg-mc-l1_c4 with fade
    play voice4 aaleyah_thinking_hmm3 noloop
    jdg "Recess is almost over. You only have another minute or two to sign those papers... if that's what you want to do."
    scene d21s07-52 jdg-mc-l2_c2 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Alright, well. I've decided."
    call update_ending_variables from _call_update_ending_variables_3
    $ unlock_ending("04")
    menu:
        "Enslave Lydia in Her Own Dungeon"(hint="d21s07m02c01"):
            $ d21s07_sex_dungeon = True

            play voice2 mc_yes_yeah1 noloop
            mc "I'm sure this is in everyone's best interest."
        "Reject the Offer"(hint="d21s07m02c02"):

            $ d21s07_sex_dungeon = False

            play voice2 mc_no_no1 noloop
            mc "No.{w} As Hartigan famously said, \"There's wrong, and there's wrong, and there's *this*\"."
            mc "I won't sign it."

    scene d21s07-52 jdg-mc-l2_c4 with dissolve
    play voice4 aaleyah_surprised_oh noloop
    jdg "Well, I can't say that I would have done the same, but... Good Choice."
    jdg "Please return to your seat in the audience."

    jump d21s07_closing

label d21s07_closing:

    if from_ending_menu is True:
        $ renpy.music.set_volume(0.35, 3.0, "music" )
        play music vidala_en_verde fadein 3.0
    play sound sfx_court_hammer1
    scene d21s07-21 jdg-def-p-lc-hr-baf-mc-grill12_c4 with Fade(0.5, 0.5, 0.5)
    play voice5 boy5_hey_angry noloop
    "Bailiff" "All Rise!{w} The People v. Lydia Cox and Jerome Skinner will now resume."
    "Bailiff" "Be seated."
    if d21s07_sex_dungeon is True:
        scene d21s07-70 jdg-baf-mc-closing1_c4 with dissolve
        play voice4 aaleyah_thinking_hmm1 noloop
        jdg "Lydia Cox, I have before me signed documents for your plea agreement."
        scene d21s07-70 jdg-baf-mc-closing1_c5 with dissolve
        play voice3 lydia_moan1 noloop
        lc "You do, your honor?"
        scene d21s07-72 jdg-def-p-lc-hr-baf-mc-closing3_c4 with dissolve
        play voice4 aaleyah_yes_yes2 noloop
        jdg "I do. [mcname] Young has accepted responsibility for your punishments for a duration of 8 years."
        jdg "During this time you will be under house arrest and required to perform and endure whatever punishments he determines appropriate."
        jdg "You will effectively be a felon without rights and an indentured servant with [mcname] Young as your master."
        jdg "Do you agree to this?"
        scene d21s07-76 jdg-def-p-lc-hr-baf-mc-closing7_c2 with dissolve
        play voice5 claudie_yes_unsure noloop
        "Defense Attorney" "She does, your honor. Her signature is already-"
        scene d21s07-75 jdg-def-p-lc-hr-baf-mc-closing6_c4 with hpunch
        play voice4 aaleyah_angry_grrr1 noloop
        jdg "Shut up.{w} You are her attorney, but I need to hear it from her."
        scene d21s07-74 jdg-def-p-lc-hr-baf-mc-closing5_c2 with dissolve
        play voice3 daisy_ugu noloop
        lc "I do, your honor."
        scene d21s07-74 jdg-def-p-lc-hr-baf-mc-closing5_c4 with dissolve
        play voice4 nora_hmm noloop volume 1.4
        jdg "In that case, how do you plead?"
        scene d21s07-70 jdg-baf-mc-closing1_c5 with dissolve
        play voice3 dahlia_disappointed_ehh2 noloop
        lc "I plead guilty, your honor. According to the terms of my plea deal."
        scene d21s07-76 jdg-def-p-lc-hr-baf-mc-closing7_c4 with dissolve
        play voice4 dahlia_arrogant_hm noloop
        jdg "Mr. [mcname] Young, please approach the podium."
        scene d21s07-80 jdg-def-p-lc-hr-baf-mc-podium1_c2 with dissolve
        play voice2 mc_yes_yes2 noloop
        mc "Um, yes...{w} That is me, your honor."
        scene d21s07-80 jdg-def-p-lc-hr-baf-mc-podium1_c4 with dissolve
        play voice4 aaleyah_thinking_hmm2 noloop
        jdg "Are you certain?"
        scene d21s07-81 jdg-def-p-lc-hr-baf-mc-podium2_c2 with dissolve
        play voice2 mc_yes_yes1 noloop
        mc "Yes, your honor. I am [mcname] Young.{w} My signature is on those documents."
        scene d21s07-81 jdg-def-p-lc-hr-baf-mc-podium2_c4 with dissolve
        play voice4 nora_aga noloop
        jdg "You agree to the terms of this agreement as well?"
        scene d21s07-82 jdg-def-p-lc-hr-baf-mc-podium3_c2 with dissolve
        play voice2 mc_yes_yeah2 noloop
        mc "I do, your honor."
        scene d21s07-82 jdg-def-p-lc-hr-baf-mc-podium3_c4 with dissolve
        play voice4 aaleyah_thinking_hmm3 noloop
        jdg "Very well. Please be at Miss Cox's house tomorrow afternoon at 3pm for delivery."
        scene d21s07-83 jdg-def-p-lc-hr-baf-mc-podium4_c2 with dissolve
        play voice2 mc_thinking_hmm5 noloop
        mc "Delivery, your honor?"
        scene d21s07-83 jdg-def-p-lc-hr-baf-mc-podium4_c4 with dissolve
        play voice4 aaleyah_disappointed_mff noloop
        jdg "Miss Cox will be stripped, shackled, and prepared for your tender loving care."
        scene d21s07-84 jdg-def-p-lc-hr-baf-mc-podium5_c2 with dissolve
        play voice2 mc_thinking_oh1 noloop
        mc "Oh, wow. Thank you, your honor."
        scene d21s07-84 jdg-def-p-lc-hr-baf-mc-podium5_c4 with dissolve
        play voice4 aaleyah_angry_hm1 noloop
        jdg "We will resume Jerome Skinner's case tomorrow at 9am."
        scene d21s07-84 jdg-def-p-lc-hr-baf-mc-podium5_c1 with dissolve
        play voice3 boy4_surprised_huh5 noloop
        js "Wait! Can I get a plea deal too?!"
        scene d21s07-88 lc-mc-queen3_c1 with dissolve
        play voice4 aaleyah_thinking_hmm2 noloop
        jdg "Mister Prosecutor?"
        scene d21s07-70 jdg-baf-mc-closing1_c2 with dissolve
        play voice5 pete_no_simple3 noloop
        "Prosecutor" "No, thanks. I believe he will be better served in a traditional prison."
        play voice3 boy4_pain_sobs2 noloop
        pause 0.1
        stop voice3 fadeout 3.0
        js "Nooooooo!"
        play sound sfx_court_hammer1
        stop music fadeout 3.0

        jump ending_04

    scene d21s07-84 jdg-def-p-lc-hr-baf-mc-podium5_c4 with dissolve
    play voice4 aaleyah_thinking_hmm1 noloop
    jdg "We will now hear closing arguments. Prosecutor, you may go first."
    scene d21s07-15 jdg-def-p-lc-hr-baf-mc-grill6_c2 with dissolve
    play voice5 pete_thinking_mmf noloop
    "Prosecutor" "Thank you, your honor.{w} Ladies and gentlemen of the jury..."
    scene d21s07-15 jdg-def-p-lc-hr-baf-mc-grill6_c4 with dissolve
    play voice4 aaleyah_angry_cagh1 noloop
    jdg "Ahem.{w} Do I need to remind you that the defendants waived their right to a jury of their peers?"
    scene d21s07-16 jdg-def-p-lc-hr-baf-mc-grill7_c2 with dissolve
    play voice5 pete_thinking_oh1 noloop
    "Prosecutor" "Right, right. Sorry, your honor. Force of habit."
    jdg "You may continue."
    "Prosecutor" "Thank you, your honor..."
    scene d21s07-72 jdg-def-p-lc-hr-baf-mc-closing3_c5 with Fade(0.4, 0.4, 0.4)
    play voice4 chloe_hey_whisper noloop
    hr "*whispers* Hey! [mcname]! Wake up!"
    scene d21s07-73 jdg-def-p-lc-hr-baf-mc-closing4_c1 with dissolve
    play voice2 mc_scared_huh2 noloop
    mc "Huh? What? Oh.{w}.. sorry, was I snoring?"
    scene d21s07-73 jdg-def-p-lc-hr-baf-mc-closing4_c5 with dissolve
    play voice4 fshhh noloop
    hr "*whispers* Shut up and listen. The Judge is about to announce the verdict."
    scene d21s07-74 jdg-def-p-lc-hr-baf-mc-closing5_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "*whisper* Thanks for waking me."
    if ntr_lc_guilty is True:
        scene d21s07-97 lc-mc-queen11_c1 with dissolve
        play voice4 aaleyah_angry_hm1 noloop
        jdg "Lydia Cox and Jerome Skinner I find you both guilty on all charges."
        jdg "In light of your youth and that this is the first offense for either of you I am inclined to be lenient."
        scene d21s07-100 lc-mc-queen14_c1 with dissolve
        play voice4 aaleyah_thinking_hmm2 noloop
        jdg "However, due to the malicious nature of your offenses I am inclined to throw the book at you."
        jdg "Therefore, I sentence you both to 15 years each."
        scene d21s07-102 lc-mc-queen16_c1 with dissolve
        play voice4 aaleyah_disappointed_mff noloop
        jdg "Further, I recommend your sentence be carried out in general population at a labor camp."
        jdg "May God have mercy on your anuses."
        play sound sfx_court_hammer1
        scene d21s07-73 jdg-def-p-lc-hr-baf-mc-closing4_c5 with dissolve
        play voice5 chloe_happy_yeah2 noloop
        hr "Ah ha! TAKE THAT YOU POND SCUM!"
        scene d21s07-76 jdg-def-p-lc-hr-baf-mc-closing7_c1 with dissolve
        play voice2 mc_happy_a1 noloop volume 1.2
        mc "I didn't think I would feel good about anything today, but I was wrong."
        mc "They are getting exactly what they deserve."
        jump d21s07_endings
    elif lc_lc_guilty is True:
        scene d21s07-97 lc-mc-queen11_c1 with dissolve
        play voice4 aaleyah_angry_hm1 noloop
        jdg "Lydia Cox and Jerome Skinner I find you both guilty on all charges."
        jdg "However, I sentence Lydia Cox to 2 years in prison and suspend the sentence."
        scene d21s07-70 jdg-baf-mc-closing1_c5 with dissolve
        play voice3 dahlia_surprised_ah2 noloop
        lc "Your honor? What does that mean?"
        scene d21s07-100 lc-mc-queen14_c1 with dissolve
        play voice4 aaleyah_disappointed_mff noloop
        jdg "You will be on parole for no less than 2 years. If you complete the conditions of your parole you will not need to serve any time."
        jdg "If you fail to comply with the conditions of your parole, you will serve the entire time as required."
        scene d21s07-74 jdg-def-p-lc-hr-baf-mc-closing5_c2 with dissolve
        play voice3 dahlia_surprised_oh noloop
        lc "Oh!{w} Thank you, your honor!"
        scene d21s07-102 lc-mc-queen16_c1 with dissolve
        play voice4 aaleyah_angry_egh1 noloop
        jdg "As for Jerome Skinner, I sentence you to 15 years manual labor."
        play voice3 boy4_pain_sobs2 noloop
        pause 0.1
        stop voice3 fadeout 3.0
        js "Nooooooo!"
        play sound sfx_court_hammer1
        scene d21s07-72 jdg-def-p-lc-hr-baf-mc-closing3_c5 with dissolve
        play voice4 chloe_surprised_huh1 noloop
        hr "She only got 2 years? I think I'm going to throw up."
        scene d21s07-73 jdg-def-p-lc-hr-baf-mc-closing4_c1 with dissolve
        play voice2 mc_happy_a1 noloop
        mc "Overall, I feel quite good about the sentences."
        scene d21s07-73 jdg-def-p-lc-hr-baf-mc-closing4_c5 with dissolve
        play voice4 chloe_disgust_boeah2 noloop
        hr "I am never fucking you again."
        scene d21s07-74 jdg-def-p-lc-hr-baf-mc-closing5_c1 with dissolve
        play voice2 d9s2_yeah noloop volume 2.0
        mc "Fair enough."
    else:
        scene d21s07-97 lc-mc-queen11_c1 with dissolve
        play voice4 aaleyah_angry_hm1 noloop
        jdg "Jerome Skinner, I find you Guilty on all charges."
        jdg "I sentence you to 15 years manual labor. May God have mercy on your anus."
        scene d21s07-74 jdg-def-p-lc-hr-baf-mc-closing5_c2 with dissolve
        play voice3 dahlia_pain_ah2 noloop
        lc "Oh my goodness! That's horrible!"
        scene d21s07-100 lc-mc-queen14_c1 with dissolve
        play voice4 nora_arghh noloop
        jdg "BE SILENT. As for you, Miss Cox..."
        play voice3 gulp volume 0.2 noloop
        lc "*gulp*"
        play voice4 aaleyah_thinking_hmm3 noloop
        jdg "Lydia Cox, I find you Not Guilty on all charges."
        scene d21s07-70 jdg-baf-mc-closing1_c5 with dissolve
        play voice3 lydia_ah noloop
        lc "I'm... what?!"
        play voice4 nora_heh noloop
        jdg "You are free to go."
        play voice3 girl8_scared_ah3 noloop
        lc "OMG! W00T!!!"
        play sound sfx_court_hammer1
        scene d21s07-72 jdg-def-p-lc-hr-baf-mc-closing3_c5 with dissolve
        play voice4 chloe_arrogant_heh1 noloop
        hr "Did she just fucking say W-zero-zero-T?"
        scene d21s07-73 jdg-def-p-lc-hr-baf-mc-closing4_c1 with dissolve
        play voice2 mc_yes_yeah5 noloop
        mc "And she said O-M-G."
        scene d21s07-73 jdg-def-p-lc-hr-baf-mc-closing4_c5 with dissolve
        play voice4 chloe_angry_argh4 noloop
        hr "I fucking hate the universe and everything in it."
        scene d21s07-74 jdg-def-p-lc-hr-baf-mc-closing5_c1 with dissolve
        play voice2 mc_thinking_mmm5 noloop
        mc "At least an innocent woman was set free."
        scene d21s07-74 jdg-def-p-lc-hr-baf-mc-closing5_c5 with dissolve
        play voice4 chloe_surprised_huh1 noloop
        hr "Innocent?{w} I am never fucking you again."
        scene d21s07-75 jdg-def-p-lc-hr-baf-mc-closing6_c1 with dissolve
        play voice2 mc_thinking_emm1 noloop
        mc "Did we fuck before?"
        play voice4 chloe_surprised_what noloop
        hr "Are you shitting me?"
        play voice2 d2s9_confused noloop volume 1.4
        mc "Sorry, there was so much excitement during the weeks Fetish Locator was running... I kinda forgot who I've been with and who I haven't."
        scene d21s07-74 jdg-def-p-lc-hr-baf-mc-closing5_c5 with dissolve
        play voice4 chloe_angry_argh1 noloop
        hr "You are so...{w} NEVER AGAIN."
    if d21s07_is_harem_available is True:
        jump d21s07_harem_end
    else:
        jump d21s07_endings

label d21s07_harem_end hide:

    if from_ending_menu is True:
        $ renpy.music.set_volume(0.35, 3.0, "music" )
        play music vidala_en_verde fadein 3.0
    scene d21s07-05 jdg-def-p-lc-hr-baf-mc-entry3_c5 with dissolve
    play voice4 chloe_angry_hm noloop
    hr "That twisted cunt caused all this and got off?"
    scene d21s07-05 jdg-def-p-lc-hr-baf-mc-entry3_c1 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Hey, at least Jerome is going away for-"
    scene d21s07-74 jdg-def-p-lc-hr-baf-mc-closing5_c5 with dissolve
    play voice4 chloe_angry_breath noloop
    hr "Screw this.{w} I'm outta here."
    scene d21s07-87 lc-mc-queen2_c1 with dissolve
    pause
    play sound sfx_heels_run2
    scene d21s07-87 lc-mc-queen2_c4 with dissolve
    play voice2 mc_surprised_wow1 noloop
    mc "Whoa! What the-?"
    play voice3 lydia_orgasm2 noloop
    lc "I'm free! I'm Free!! I'M FREE!!!"
    play voice2 mc_pain_mff2 noloop
    play voice3 dahlia_sex_closedmoan4 noloop
    play sound dahlia_kiss_french1
    scene d21s07-90 lc-mc-kiss_c4 with vpunch
    pause
    play sound maria_kiss1
    scene d21s07-90 lc-mc-kiss_c2 with dissolve
    pause
    scene d21s07-92 lc-mc-queen6_c4 with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    lc "I've never been so happy. And I love you so much!"
    scene d21s07-92 lc-mc-queen6_c2 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mc "I never had any doubt that the court would find you innocent."
    scene d21s07-92 lc-mc-queen6_c4 with dissolve
    play voice3 dahlia_sex_closedmoan1 noloop
    lc "Innocent, eh? Let me tell you something about that."
    lc "*whisper* If there weren't so many people here I'd tell you to throw me over that table and have your way with me right now."
    scene d21s07-92 lc-mc-queen6_c2 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Hmm..."
    if from_ending_menu is True:
        jump d21s07_marry_lc
    call update_ending_variables from _call_update_ending_variables_4
    $ unlock_ending("06")
    menu:
        "Propose Marriage to Lydia"(hint="d21s07m03c01"):
            $ d21s07_engagement = True
            $ d21s07_last_menu = 01
            jump d21s07_marry_lc

        "Let Lydia Down Gently for AmRose"(hint="d21s07m03c02") if d21s07_is_amrose_available is True:
            $ d21s07_last_menu = 02
            jump d21s07_breakup

        "Let Lydia Down Gently for Stacy"(hint="d21s07m03c03") if d21s07_is_stacy_available is True:
            $ d21s07_last_menu = 03
            jump d21s07_breakup

        "Let Lydia Down"(hint="d21s07m03c04") if d21s02_bring_sy is True and date_sy is False:
            $ d21s07_last_menu = 04
            jump d21s07_breakup

label d21s07_marry_lc hide:

    scene d21s07-94 lc-mc-queen8_c2 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "*whisper* Ignore them. Let's do it anyway."
    scene d21s07-94 lc-mc-queen8_c4 with dissolve
    play voice3 lydia_laugh noloop
    lc "*laughing* You're incorrigible."
    scene d21s07-95 lc-mc-queen9_c2 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Don't tell that to the judge."
    mc "As long as the judge is here, why don't you marry me?"
    scene d21s07-94 lc-mc-queen8_c4 with dissolve
    play voice3 lydia_ah noloop
    lc "Are you serious?"
    scene d21s07-94 lc-mc-queen8_c2 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Maybe I am."
    play voice3 lydia_moan1 noloop
    lc "Ask me. I'll say, \"yes\". We can do it right now."
    play voice2 mc_yes_okay2 noloop
    mc "I was going to wait for a more opportune moment, but..."
    scene d21s07-94 lc-mc-queen8_c4 with dissolve
    play voice3 dahlia_surprised_huh2 noloop
    lc "You're kidding me! Really?!"
    play sound sfx_powder_latch_closed
    scene d21s07-95 lc-mc-queen9_c3 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "I guess now is as good a time as any."
    mc "Lydia Cox, will you be my wife?"
    play voice3 lydia_orgasm1 noloop
    scene d21s07-95 lc-mc-queen9_c4 with hpunch
    lc "O-M-G!!!"
    scene d21s07-95 lc-mc-queen9_c1 with dissolve
    play voice4 aaleyah_disappointed_oh1 noloop
    jdg "Oh, hell. I hate when this happens."
    jdg "Alright, if you want to get married here, now, then let's hurry this up-"
    scene d21s07-95 lc-mc-queen9_c4 with dissolve
    play voice3 dahlia_surprised_huh1 noloop
    lc "Wait! No!"
    scene d21s07-96 lc-mc-queen10_c2 with dissolve
    play voice2 mc_surprised_huh3 noloop
    mc "No?!"
    play sound sfx_powder_latch_closed
    scene d21s07-96 lc-mc-queen10_c4 with dissolve
    play voice3 dahlia_happy_laugh3 noloop
    lc "Not that, silly. Of course I'll marry you. I'm the happiest woman in the world right now!"
    scene d21s07-96 lc-mc-queen10_c3 with dissolve
    play voice2 d2s12_emmm noloop volume 1.5
    mc "Then what did you mean, \"No\"?"
    play sound sfx_cloth_rustling4
    scene d21s07-97 lc-mc-queen11_c2 with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    lc "I don't want to get married to you right here, right now. We don't even have a marriage license."
    scene d21s07-97 lc-mc-queen11_c3 with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Okay..."
    scene d21s07-97 lc-mc-queen11_c4 with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    lc "*whispers* Besides, I've got a better idea."
    scene d21s07-97 lc-mc-queen11_c3 with dissolve
    play voice3 amrose_old_psst2 noloop
    "*Lydia whispers softly into [mcname]'s ear*"
    scene d21s07-98 lc-mc-queen12_c2 with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "Oh you dirty bitch. I love you so much right now."
    scene d21s07-94 lc-mc-queen8_c4 with dissolve
    play voice3 lydia_haha noloop volume 1.5
    lc "Ditto, baby. I love you too."
    stop music fadeout 3.5

    jump ending_06

label d21s07_breakup:

    $ d21s07_still_dating = False

    scene d21s07-92 lc-mc-queen6_c4 with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Hon, I really don't want to ruin your moment, but-"
    play voice3 lydia_morningoh noloop
    lc "Oh..."
    play voice2 mc_yes_yeah5 noloop volume 0.7
    mc "Yeah. I'm sorry. I'm really really sorry."
    play voice3 daisy_ugu noloop
    lc "But there's someone else..."
    scene d21s07-91 lc-mc-queen5_c2 with dissolve
    play voice2 d1s5b_ehhh noloop
    mc "I mean, I hope we can still be friends... and you know I'll always be around for the fun times."
    scene d21s07-91 lc-mc-queen5_c4 with dissolve
    play voice3 lydia_hmmmm noloop
    if d21s07_is_amrose_available is True:
        lc "Is it AmRose?"
    elif d21s07_is_stacy_available is True:
        lc "Is it Stacy?"
    else:
        jump d21s07_endings

    scene d21s07-102 lc-mc-queen16_c2 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Yeah. Is it that obvious?"
    scene d21s07-102 lc-mc-queen16_c4 with dissolve
    play voice3 lydia_oof noloop
    lc "I could tell. I kinda knew that ever since she came with you to visit me in that holding cell."
    scene d21s07-102 lc-mc-queen16_c2 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "I didn't mean to get your hopes up, but I didn't want to-"
    scene d21s07-102 lc-mc-queen16_c4 with dissolve
    play voice3 lydia_lydiahey noloop
    lc "Thank you, for that. Not crushing my hopes sooner."
    lc "That didn't come out right. I really want to thank you."
    lc "Sometimes the fantasy about us together was all that got me through my time in jail."
    scene d21s07-101 lc-mc-queen15_c2 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "I'll always love you. I hope you know that."
    scene d21s07-101 lc-mc-queen15_c4 with dissolve
    play voice3 lydia_lydyes noloop
    lc "Same. You are now, and ever shall be, my friend. One of my favorite people."
    play voice2 mc_yes_yeah1 noloop
    mc "Exactly."

    jump d21s07_endings

label d21s07_endings:

    stop music fadeout 3.5
    call update_ending_variables from _call_update_ending_variables_5
    if d21s07_is_amrose_available is True:
        $ unlock_ending("08")
        jump ending_08
    elif d21s07_is_stacy_available is True:
        $ unlock_ending("01")
        jump ending_01
    else:
        jump d21s99
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
