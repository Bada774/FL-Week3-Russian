image e07s06-a163-1 = Movie(play = "images/E-07/s06/anim/e07s06-a163-1-2x-50fps.webm", start_image = "e07s06-a163-1 final-challenge-lc-bj-anim-00")
image e07s06-a163-1-f = Movie(play = "images/E-07/s06/anim/e07s06-a163-1-2x-60fps.webm", start_image = "e07s06-a163-1 final-challenge-lc-bj-anim-00")
image e07s06-a163-2 = Movie(play = "images/E-07/s06/anim/e07s06-a163-2-2x-50fps.webm", start_image = "e07s06-a163-2 final-challenge-lc-bj-anim-00")
image e07s06-a163-2-f = Movie(play = "images/E-07/s06/anim/e07s06-a163-2-2x-60fps.webm", start_image = "e07s06-a163-2 final-challenge-lc-bj-anim-00")

image e07s06-a184-1 = Movie(play = "images/E-07/s06/anim/e07s06-a184-1-2x-50fps.webm", start_image = "e07s06-a184-1 final-challenge-mc-bj-anim-00")
image e07s06-a184-1-f = Movie(play = "images/E-07/s06/anim/e07s06-a184-1-2x-60fps.webm", start_image = "e07s06-a184-1 final-challenge-mc-bj-anim-00")
image e07s06-a184-2 = Movie(play = "images/E-07/s06/anim/e07s06-a184-2-2x-50fps.webm", start_image = "e07s06-a184-2 final-challenge-mc-bj-anim-00")
image e07s06-a184-2-f = Movie(play = "images/E-07/s06/anim/e07s06-a184-2-2x-60fps.webm", start_image = "e07s06-a184-2 final-challenge-mc-bj-anim-00")

image e07s06-a200-1 = Movie(play = "images/E-07/s06/anim/e07s06-a200-1-2x-50fps.webm", start_image = "e07s06-a200-1 final-challenge-arj-handjob-anim-01")
image e07s06-a200-1-f = Movie(play = "images/E-07/s06/anim/e07s06-a200-1-2x-60fps.webm", start_image = "e07s06-a200-1 final-challenge-arj-handjob-anim-01")
image e07s06-a200-2 = Movie(play = "images/E-07/s06/anim/e07s06-a200-2-2x-50fps.webm", start_image = "e07s06-a200-2 final-challenge-arj-handjob-anim-01")
image e07s06-a200-2-f = Movie(play = "images/E-07/s06/anim/e07s06-a200-2-2x-60fps.webm", start_image = "e07s06-a200-2 final-challenge-arj-handjob-anim-01")
image e07s06-a200-3 = Movie(play = "images/E-07/s06/anim/e07s06-a200-3-2x-50fps.webm", start_image = "e07s06-a200-3 final-challenge-arj-handjob-anim-01")
image e07s06-a200-3-f = Movie(play = "images/E-07/s06/anim/e07s06-a200-3-2x-60fps.webm", start_image = "e07s06-a200-3 final-challenge-arj-handjob-anim-01")

label e07s06:

    $ e07s06_cheat = False
    $ e07s06_suck_dick = False

    scene black
    show screen scene_transistion(_("A couple days later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_door_closed1
label replay_e07s06 hide:
    scene e07s06-00 final_challenge_walkingn_lc_smug
    with Fade(0.5, 0.5, 0.5)
    $ renpy.music.set_volume(0.8, 1.0, "music")
    play music thinking_music_3
    pause
    scene e07s06-01 final_challenge_walkingn_lc_talk_turn with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    lc "You have come a long way."
    if e07_mc_wins == 1:
        scene e07s06-02 final_challenge_walkingn_lc_talk_displeased with dissolve
        play voice3 dahlia_angry_oh noloop
        lc "You have disappointed me, [e07_mcname!t], but I'd like to give you one more chance to prove you are something special."
        scene e07s06-03 final_challenge_walkingn_lc_talk_scratch with dissolve
        play voice3 dahlia_angry_hm2 noloop
        lc "God help you if you fail me again."
        lc "Understood?"
        scene e07s06-04 final_challenge_walkingn_mc_talk with dissolve
        play voice2 d9s2_mcyes2 noloop volume 2.3
        mc "Yes..."
        scene e07s06-05 final_challenge_walkingn_lc_talk_pleased with dissolve
        play voice3 dahlia_thinking_hmm1 noloop
        lc "Good."
    elif e07_mc_wins == 2:
        scene e07s06-06 final_challenge_walking_2_winsn_lc_talk with dissolve
        play voice3 dahlia_disappointed_ehh3 noloop
        lc "Tell me something, [e07_mcname!t]."
        scene e07s06-07 final_challenge_walking_2_winsn_mc_talk with dissolve
        play voice2 mc_yes_yes2 noloop
        mc "Yes?"
        scene e07s06-08 final_challenge_walking_2_winsn_lc_talk with dissolve
        play voice3 dahlia_thinking_hmm1 noloop
        lc "Is \"mediocre\" a word you'd use to describe yourself?"
        scene e07s06-09 final_challenge_walking_2_winsn_mc_talk_resiliant with dissolve
        play voice2 mc_no_no2 noloop
        mc "No, of course not."
        scene e07s06-10 final_challenge_walking_2_winsn_lc_talk_disgust with dissolve
        play voice3 dahlia_angry_hm2 noloop
        lc "Then why have you only won two of the challenges?"
        scene e07s06-11 final_challenge_walking_2_winsn_mc_talk_down with dissolve
        play voice2 d2s12_emmm noloop
        mc "I have no excuse."
        scene e07s06-12 final_challenge_walking_2_winsn_lc_stare with dissolve
        lc "..."
        scene e07s06-13 final_challenge_walking_2_winsn_lc_talk_cross_arm_smile with dissolve
        play voice3 dahlia_angry_oh noloop
        lc "Lucky for you, I believe in second chances."
        scene e07s06-14 final_challenge_walking_2_winsn_mc_talk with dissolve
        play voice2 mc_happy_a1 noloop
        mc "Thank you."
        scene e07s06-15 final_challenge_walking_2_winsn_lc_talk_stroke_chin with dissolve
        play voice3 dahlia_happy_laugh4 noloop
        lc "*chuckles* Save it. You haven't won yet. But maybe I'll let you {i}thank me{/i} if you survive this round."
    if e07_mc_wins == 3:
        scene e07s06-16 final_challenge_walking_3_winsn_lc_talkmpressed with dissolve
        play voice3 lydia_lydwow noloop
        lc "You've really outdone yourself, [e07_mcname!t]. When you accepted your role, I thought you might lose some of that gung-ho spirit you had weeks ago."
        lc "I stand corrected. Your determination for my affection is... flatterting."
        scene e07s06-17 final_challenge_walking_3_winsn_mc_talk_proud with dissolve
        play voice2 mc_happy_a1 noloop
        mc "Thank you, [e07_lcname!t]. That means a lot, coming from you."
        scene e07s06-18 final_challenge_walking_lc_talk_fold_arm with dissolve
        play voice3 dahlia_angry_hm2 noloop
        lc "Of course it does."
    lc "But now we've arrived at my final challenge for you."
    lc "Are you both up to the task?"
    scene e07s06-19 final_challenge_walking_pb_talk_fist with dissolve
    play voice3 pete_yes_yeah noloop
    pb "I'm ready for anything."
    scene e07s06-20 final_challenge_mc_talk_determined with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Just tell me what to do."
    mct "You're going down, Pete. Lydia belongs to me."
    scene e07s06-21 final_challenge_lc_talk_arj with dissolve
    play voice3 lydia_hmmmm noloop volume 1.6
    lc "[e07_arjname!t], be a good little toy and remove their blindfolds."
    play sound sfx_sextoy_uncuff1
    scene e07s06-22 final_challenge_arj_remove_blindfold with dissolve
    pause
    scene e07s06-23 final_challenge_arj_talk_sad with dissolve
    play voice4 amrose_hey_whisper noloop
    arj "Are you okay, [mcname]?"
    scene e07s06-24 final_challenge_mc_talk with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Don't worry, I got this."
    scene e07s06-25 final_challenge_arj_to_pete with dissolve
    pause
    play sound sfx_cloth_rustling2
    scene e07s06-26 final_challenge_arj_stroke_chest with dissolve
    pause
    play sound sfx_sextoy_uncuff1
    scene e07s06-27 final_challenge_arj_pull_mask with dissolve
    pause
    scene e07s06-28 final_challenge_pb_talk with dissolve
    play voice5 pete_hey_sexy noloop
    pb "Hey, Red."
    scene e07s06-29 final_challenge_lc_talk_arj_move_away with dissolve
    play voice3 dahlia_angry_argh2 noloop
    lc "Don't get distracted you two."
    play voice3 dahlia_arrogant_ha noloop
    lc "The only holes I want you thinking about are these holes."
    scene e07s06-31 final_challenge_lc_runs_hand_down with dissolve
    play voice3 dahlia_sex_closedmoan1 noloop
    play voice2 mc_thinking_mmm2 noloop
    mct "Okay. I think I like where this challenge is going."
    scene e07s06-32 final_challenge_mc_thought_runs_hand_down with dissolve
    play voice3 dahlia_sex_closedmoan4 noloop
    lc "Mrmm."
    scene e07s06-30 final_challenge_lc_talk with dissolve
    lc "I hope you two are ready."
    scene e07s06-33 final_challenge_mc_thought_hands_off_point_gloryhole with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "Huh?"
    scene e07s06-34 final_challenge_mc_talk with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Ah. You meant those holes."
    scene e07s06-35 final_challenge_lc_talk_smile with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    lc "Don't sound so disappointed, [e07_mcname!t]."
    scene e07s06-36 final_challenge_lc_talk_walkover with dissolve
    play voice3 dahlia_happy_laugh2 noloop
    lc "I promise that you're going to enjoy this."
    scene e07s06-37 final_challenge_lc_talk_look_arj with dissolve
    play voice3 dahlia_hey_angry noloop
    lc "You can go now."
    scene e07s06-38 final_challenge_look_down_arj with dissolve
    play voice4 amrose_yes_ugu noloop
    pause
    play sound sfx_heels_steps2
    scene e07s06-39 final_challenge_lc_talk_arj_walk_out with dissolve
    pause
    play sound sfx_door_closed2
    scene e07s06-40 final_challenge_lc_talk_arms_on_both with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    lc "Mmmm."
    lc "Listen closely."
    scene e07s06-41 final_challenge_lc_talk_pb with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    lc "Both of you."
    lc "Behind that wall is a group of horny sluts."
    scene e07s06-42 final_challenge_lc_talk_ahead with dissolve
    lc "Since Fetish Locator started, I've seen a lot of girls desperate to get back at daddy or to find out their limits."
    lc "But these girls put the rest to shame."
    scene e07s06-43 final_challenge_lc_talk_lick_lips with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    lc "And..."
    scene e07s06-44 final_challenge_lc_talk with dissolve
    play voice3 lydia_moan1 noloop
    lc "They are truly hungry to enjoy your cocks."
    scene e07s06-45 final_challenge_lc_talk_step_side with dissolve
    play voice3 dahlia_yes_yeah3 noloop
    lc "So the rules of this challenge are simple."
    lc "Stick your dick in the hole. And survive."
    scene e07s06-46 final_challenge_pb_talk with dissolve
    play voice5 pete_disappointed_oof1 noloop
    pb "Uhhh..."
    scene e07s06-47 final_challenge_mc_talk with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Survive?"
    scene e07s06-48 final_challenge_lc_talk_smile with dissolve
    play voice3 dahlia_arrogant_heh noloop
    lc "Step One. Stick your dick in the hole."
    lc "Step Two. Allow my newest pets to salivate and drool all over your flesh while they milk you."
    scene e07s06-49 final_challenge_lc_talk_suck_finger with dissolve
    play voice3 daisy_dlick noloop volume 1.7
    lc "After you cum, we've hit Step Three."
    lc "Pull out your cock and show me you've still got some mojo."
    scene e07s06-50 final_challenge_lc_talk_sharper_expression with dissolve
    play voice3 dahlia_thinking_oh noloop
    lc "But if you take out your cock and it's limp city."
    lc "Buzz! Game over."
    scene e07s06-51 final_challenge_mc_talk_nod with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "I understand, [e07_lcname!t]."
    scene e07s06-52 final_challenge_pb_talk_grin with dissolve
    play voice5 pete_yes_simple2 noloop
    pb "Got it."
    scene e07s06-53 final_challenge_lc_talk_smile with dissolve
    play voice3 dahlia_yes_aga noloop
    lc "Good. Now get in position."
    scene e07s06-54 final_challenge_pb_hole with dissolve
    pause
    scene e07s06-55 final_challenge_mc_lookdown with dissolve
    play voice2 d2s9_confused noloop
    mc "Uh. [e07_lcname!t]."
    scene e07s06-56 final_challenge_lc_laugh with dissolve
    play voice3 dahlia_happy_laugh6 noloop
    lc "Of course. I almost forgot."
    scene e07s06-57 final_challenge_lc_touch with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    lc "Mrmmm."
    lc "You were so good when you put this on the first time. A fun little puppy."
    lc "I knew that you'd make the right decision when the moment came."


    $ Lovense.stop()

    scene e07s06-58 final_challenge_mc_talk_mc_happy with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "You did?"
    play sound cockcage_lock_off
    $ Lovense.vibrate(1)
    scene e07s06-59 final_challenge_lc_talk_mc_remove_cage with dissolve
    play voice3 lydia_lydyes noloop
    lc "A woman can always tell..."
    scene e07s06-60 final_challenge_pb_talk_bothn_hole with dissolve
    play voice5 pete_hey_happy noloop
    pb "Best of luck, [mcname]."
    scene e07s06-61 final_challenge_mc_talk_bothn_hole with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Don't need it. Never had it."
    scene e07s06-62 final_challenge_mc_talk_pete_amused with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "How long do we have until-"
    scene e07s06-63 final_challenge_mc_thought_awkward_look with dissolve
    play sound2 mc_sex_sucking_slow2 volume 0.5
    play voice2 mc_pain_mff2 noloop
    queue voice2 d7s4_mcbreathing
    $ Lovense.pattern("7;10", 1400)
    mct "Not long it turns out."
    scene e07s06-64 final_challenge_pb_talk with dissolve
    play voice5 pete_happy_relief2 noloop
    queue voice5 pete_sex_openmoans2
    pb "Wohoo. And we're off."
    scene e07s06-65 final_challenge_mc_talk with dissolve
    play voice2 mc_disappointed_off2 noloop
    queue voice2 d7s4_mcbreathing
    mc "Woah."
    scene e07s06-66 final_challenge_pb_talk with dissolve
    play voice5 pete_happy_laugh6 noloop
    queue voice5 pete_sex_openmoans2
    pb "Haha, you already in trouble, partner?"
    scene e07s06-67 final_challenge_mc_talk with dissolve
    play voice2 mc_no_no3 noloop
    queue voice2 d7s4_mcbreathing
    mc "No. I'm fine."
    scene e07s06-66 final_challenge_pb_talk with dissolve
    play voice5 pete_happy_laugh1 noloop
    queue voice5 pete_sex_openmoans2
    pb "Hah. Whatever you say."
    scene e07s06-68 final_challenge_mc_thought_losing_control with dissolve
    $ Lovense.pattern("7;10", 700)
    mct "I'm fine. I'm fine. I'm- Jeez, who sucks cock this good?"
    mc "Fuuah... Nrrnn... can't..."
    scene e07s06-69 final_challenge_pb_talk with dissolve
    pb "That's it, girl. Have some fun with that dick."
    scene e07s06-70 final_challenge_lc_talk_barks with dissolve
    play voice3 dahlia_angry_ah2 noloop
    lc "Less peanut gallery, Bull."
    scene e07s06-71 final_challenge_pb_talk with dissolve
    pause
    scene e07s06-72 final_challenge_mc_thought_bite_lip with dissolve
    mct "Baseball. Just think about baseball and old things"
    mct "Shit. Oh no. I can't cum first! I have to-"
    $ Lovense.stop()
    $ Lovense.vibrate(14)
    scene e07s06-73 final_challenge_mc_talk_cum with hpunch
    play voice2 d1s5_orgasm2 noloop
    mc "Fuck-huah."
    scene e07s06-74 final_challenge_pb_talk with dissolve
    play voice5 pete_happy_laugh4 noloop
    pb "Haha. Good thing this wasn't a timed course."
    $ Lovense.vibrate(15)
    scene e07s06-75 final_challenge_pb_talk_cum with dissolve
    play voice5 pete_sex_orgasm2 noloop
    pb "Fuck me. That tognuaa-hurah."
    stop sound2 fadeout 1.0
    scene e07s06-76 final_challenge_pb_talk_goofy with dissolve
    $ Lovense.vibrate(3)
    play voice5 pete_happy_phew2 noloop
    pb "Phew. One to One."
    scene e07s06-77 final_challenge_lc_talk_forward with dissolve
    play voice3 dahlia_hey_active2 noloop
    lc "I can keep score just fine. Extract your cocks."
    scene e07s06-78 final_challenge_lc_talk_both_pullout_limp with dissolve
    play voice3 dahlia_disgust_yah noloop
    lc "You have thirty seconds to get hard again, and get back into the trenches."
    scene e07s06-79 final_challenge_pb_talk with dissolve
    play voice5 pete_surprised_huh1 noloop
    pb "Thirty seconds?"
    scene e07s06-80 final_challenge_lc_talk with dissolve
    play voice3 dahlia_angry_hm1 noloop
    lc "Unless you're throwing in the towel?"
    scene e07s06-81 final_challenge_mc_talk_jerking with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "I'm ready for round two, [e07_lcname!t]."
    scene e07s06-82 final_challenge_pb_talk_both_jerking with dissolve
    play voice5 pete_angry_argh1 noloop
    pb "Shit."
    scene e07s06-83 final_challenge_lc_talk_smile with dissolve
    play voice3 dahlia_happy_laugh3 noloop
    lc "I had no idea how fun this would be."
    scene e07s06-84 final_challenge_lc_talk_point with dissolve
    play voice3 dahlia_old_moan1 noloop
    lc "Alright, you know the drill."
    scene e07s06-85 final_challenge_mc_talk_both_fun with dissolve
    play sound2 mc_sex_sucking_slow2 volume 0.5
    play voice2 mc_happy_oof1 noloop
    queue voice2 d7s4_mcbreathing
    $ Lovense.pattern("7;10", 1400)
    mc "Fuck, fuck, fuck!"
    scene e07s06-86 final_challenge_pb_talk_both_struggling with dissolve
    play voice5 pete_angry_ergh3 noloop
    queue voice5 pete_sex_openmoans2
    pb "Nrraaaahhhhh!"
    scene e07s06-87 final_challenge_mc_talk_both_struggling with dissolve
    mc "This must be a trick. It can't feel this good."
    mc "Right?"
    scene e07s06-88 final_challenge_pb_talk_focus with dissolve
    pb "Yeah. I mean. No..."
    pb "I'm a hard man-"
    play voice5 pete_sex_orgasm1 noloop
    pb "Oh chimichangas!"
    scene e07s06-89 final_challenge_mc_talk_look_over with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Liar!"
    scene e07s06-90 final_challenge_pb_talk_look with dissolve
    play voice5 pete_arrogant_huh2 noloop
    pb "Liar? Takes one to know one!"
    scene e07s06-91 final_challenge_both_close with dissolve
    play voice2 d7s4_mcbreathing
    play voice5 pete_sex_closedmoans1
    pause
    scene e07s06-92 final_challenge_both_talk with dissolve
    play voice2 d9s5_auch2 noloop
    play voice5 pete_sex_orgasm3 noloop
    $ Lovense.stop()
    $ Lovense.vibrate(16)
    "Both" "Fuuuuuuuuccccccckkkk"
    scene e07s06-93 final_challenge_lc_talk with dissolve
    play voice3 dahlia_yes_happy noloop
    lc "Alright. Dicks up!"
    stop sound2 fadeout 1.0
    $ Lovense.vibrate(3)
    scene e07s06-94 final_challenge_mc_fine with dissolve
    play voice2 mc_thinking_mmm1 noloop
    pause
    scene e07s06-95 final_challenge_both_fine_lc_talk with dissolve
    mc "..."
    play voice3 dahlia_surprised_huh1 noloop
    lc "Hmmph. Looks like we still have an even match."
    lc "CONTINUE!"
    scene e07s06-96 final_challenge_both_fine_lc_talk_look_each_other with dissolve
    play voice2 mc_angry_hm2 noloop
    pause
    scene e07s06-97 final_challenge_both_fine_pb_mc_talk_backn with dissolve
    $ Lovense.pattern("7;10", 1400)
    play sound2 mc_sex_sucking_slow2 volume 0.5
    play voice5 pete_angry_ergh5 noloop
    queue voice5 pete_sex_openmoans1
    pb "Hurah!"
    play voice2 mc_pain_rrrr noloop
    queue voice2 d7s4_mcbreathing
    mc "Euuuagh!"
    scene e07s06-98 final_challenge_both_fine_pb_mc_thought_cums with dissolve
    mct "Oh God. It feels like this chick is sucking the marrow out of my bones."
    scene e07s06-99 final_challenge_pb_talk with dissolve
    pb "You've got it easy. I've got King Boo on the other end!"
    scene e07s06-100 final_challenge_mc_talk_heavy_breathing with dissolve
    mc "*heavy breathing* Come on, is... is that all you got?"
    scene e07s06-101 final_challenge_mc_talk_pound_fist with dissolve
    $ Lovense.pattern("7;13", 700)
    play sound sfx_toiletroom_shaking volume 0.6
    play voice2 mc_pain_ou1 noloop
    queue voice2 d7s4_mcbreathing
    mc "Oh shit."
    scene e07s06-102 final_challenge_mc_talk_off_gaurd with dissolve
    mct "She's trying to suck me through the hole."
    scene e07s06-103 final_challenge_mc_thoult_hand_wall_panicking with dissolve
    mct "I have to do something. There must be some way to defeat Pete."
    scene e07s06-104 final_challenge_mc_thought_eureka with dissolve
    mct "His ass! Dahlia once said Pete's weak in the ass!"
    mct "She played with his asshole one time, and he went off like a firecracker."
    scene e07s06-105 final_challenge_mc_talk_close_cum with dissolve
    play voice2 d4s8_scared noloop volume 2.0
    queue voice2 d7s4_mcbreathing
    mc "Oh fuck... huraah... where did [e07_lcname!t] find these girls?"
    mct "Got to focus. If I can... If I can hit him in the right spot, I can make him go off like a bomb."
    scene e07s06-106 final_challenge_mc_thought_focus with dissolve
    mct "And he'll be down for the count."
    mct "Oh sweet fluffy lord, do I really want to try that?"
    scene e07s06-107 final_challenge_mc_look_lc with dissolve
    mct "It might be my best shot. It might be my only shot to win."
    menu:
        "Cheat with a sneak attack"(hint="e07s06m01c01"):
            $ e07s06_cheat = True
            $ e07_mc_wins += 1
            jump e07s06_sneak_attack
        "Don't cheat"(hint="e07s06m01c02"):

            $ e07s06_cheat = False
            jump e07s06_no_cheating

label e07s06_sneak_attack:

    scene e07s06-108 final_challenge_menu_cheat_mc_thought with dissolve
    mct "Here goes nothing!"
    scene e07s06-109 final_challenge_menu_cheat_mc_thought with dissolve
    mct "I want to close my eyes... but then I might miss."
    mct "Fuck it."
    play sound sfx_fisting_fist1
    $ Lovense.stop()
    $ Lovense.vibrate(15)
    scene e07s06-110 final_challenge_menu_cheat_pb_focus with dissolve
    play voice5 pete_sex_closedmoans1
    pause
    scene e07s06-111 final_challenge_menu_cheat_pb_talk_suddenly with dissolve
    play voice5 pete_surprised_what3 noloop
    pb "What in the-"
    scene e07s06-112 final_challenge_menu_cheat_pb_talk_cum_lean_wall with dissolve
    $ Lovense.vibrate(18)
    play voice5 pete_sex_orgasm2 noloop
    pb "Shiiituuaaah!"
    scene e07s06-113 final_challenge_menu_cheat_mc_thought_pullback_remembers with dissolve
    $ Lovense.pattern("7;10", 1400)
    play voice2 mc_disgust_fu1 noloop
    mct "Gross, gross, gross!"
    queue voice2 d7s4_mcbreathing
    mct "But... now I can relax. There is no way Pete recovers from that"
    scene e07s06-114 final_challenge_menu_cheat_mc_lean_cum with dissolve
    $ Lovense.stop()
    $ Lovense.vibrate(16)
    play voice2 d1s5_orgasm2 noloop
    pause
    stop sound2 fadeout 1.0
    scene e07s06-115 final_challenge_menu_cheat_mc_talk_relieved with dissolve
    $ Lovense.vibrate(3)
    play voice2 mc_happy_oof3 noloop
    mc "Phew."
    scene e07s06-116 final_challenge_menu_cheat_lc_talk_stand_near with dissolve
    play voice3 dahlia_arrogant_yeah noloop
    lc "Sounds like it's time for an inspection again."
    scene e07s06-117 final_challenge_menu_cheat_lc_talk_mc_hard_pb_limp with dissolve
    pause
    scene e07s06-118 final_challenge_menu_cheat_lc_talk_disgust with dissolve
    play voice3 dahlia_arrogant_pff noloop
    lc "Really. You could only give me three shots?"
    scene e07s06-119 final_challenge_menu_cheat_pb_talk with dissolve
    play voice5 pete_angry_ehh1 noloop
    pb "I would if someone didn't-"
    scene e07s06-120 final_challenge_menu_cheat_lc_talk_nomood with dissolve
    play voice3 dahlia_yes_angry noloop
    lc "Put a lid on it. You're done."
    scene e07s06-121 final_challenge_menu_cheat_lc_talk_proud with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    lc "Mrmmm. You outdid yourself today, [e07_mcname!t]."
    play sound sfx_handjob_cream1 loop
    scene e07s06-122 final_challenge_menu_cheat_mc_talk_grab_cock with dissolve
    $ Lovense.vibrate(6)
    play voice2 mc_scared_huuuh1 noloop
    mc "Eeep!"
    scene e07s06-123 final_challenge_menu_cheat_lc_talk_grab_cock with dissolve
    play voice3 dahlia_arrogant_huh noloop
    lc "Problem?"
    scene e07s06-124 final_challenge_menu_cheat_mc_talk with dissolve
    play voice2 mc_no_no2 noloop
    mc "No, [e07_lcname!t]. Just still a little sensitive."
    scene e07s06-125 final_challenge_menu_cheat_lc_talk with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    lc "Ah... Would a kiss make it better?"
    play sound sfx_cloth_rustling2
    scene e07s06-126 final_challenge_menu_cheat_lc_talk_on_knees with dissolve
    play voice3 dahlia_old_moan1 noloop
    lc "Watching you get sucked dry through that hole got me a little wet, [e07_mcname!t]."

    jump e07s06_bonus_challange

label e07s06_no_cheating:

    scene e07s06-127 final_challenge_menu_dont_cheat_mc_talk_worried with dissolve
    play voice2 mc_no_no5 noloop
    queue voice2 d7s4_mcbreathing
    mct "No. I'm not sticking my finger up some guy's ass."
    mct "I just have to win the old-fashioned way."
    scene e07s06-102 final_challenge_mc_talk_off_gaurd with dissolve
    mct "I just have to-"
    $ Lovense.stop()
    $ Lovense.vibrate(16)
    play voice2 mc_pain_argh1 noloop
    with hpunch
    mc "*groaning* Huah... fuck."
    scene e07s06-103 final_challenge_mc_thoult_hand_wall_panicking with dissolve
    $ Lovense.vibrate(3)
    play voice2 d7s4_mcbreathing noloop
    mc "*panting*"
    scene e07s06-105 final_challenge_mc_talk_close_cum with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Oh no. Oh shit. God that felt so good. But I-"
    scene e07s06-128 final_challenge_menu_dont_cheat_lc_talk_pullout with dissolve
    play voice3 dahlia_angry_ah1 noloop
    lc "Alright, pull out, [e07_mcname!t]."
    scene e07s06-129 final_challenge_menu_dont_cheat_pullout_pb_cumming with dissolve
    play voice5 pete_sex_orgasm4 noloop
    pause
    stop sound2 fadeout 1.0
    scene e07s06-130 final_challenge_menu_dont_cheat_mc_jerking with dissolve
    play voice2 mc_thinking_mmm3 noloop
    pause
    scene e07s06-131 final_challenge_menu_dont_cheat_lc_talk with dissolve
    play voice3 dahlia_angry_oof noloop
    lc "Hands off, [e07_mcname!t]."
    scene e07s06-132 final_challenge_menu_dont_cheat_mc_talk with dissolve
    play voice2 d9s2_mcyes2 noloop volume 2.5
    mc "Yes..."
    scene e07s06-133 final_challenge_menu_dont_cheat_lc_talk_dick_limp with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    lc "Ahhh, poor little guy."
    play sound sfx_horror_message1
    scene e07s06-134 final_challenge_menu_dont_cheat_lc_talk_look_phone with dissolve
    play voice3 dahlia_yes_ugu noloop
    lc "Time's up."
    scene e07s06-135 final_challenge_menu_dont_cheat_lc_talk_look_pb_erect with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    lc "Mrmmmm."
    scene e07s06-136 final_challenge_menu_dont_cheat_pb_talk_look_pb_touch with dissolve
    play voice5 pete_angry_hmm2 noloop
    pb "Nrrrnnn..."
    scene e07s06-137 final_challenge_menu_dont_cheat_lc_talk with dissolve
    play voice3 dahlia_happy_laugh1 noloop
    lc "Haha. Looks like you're the only one left, [e07_pbname!t]."
    scene e07s06-138 final_challenge_menu_dont_cheat_pb_talk with dissolve
    play voice5 pete_yes_simple3 noloop
    pb "Yes, [e07_lcname!t]."
    scene e07s06-139 final_challenge_menu_dont_cheat_lc_smile with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    lc "Well it is very obvious, we have a winner. I really thought you'd do better, [e07_mcname!t]."
    if e07_mc_wins == 4:
        scene e07s06-140 final_challenge_menu_dont_cheat_lc_talk with dissolve
        play voice3 dahlia_disappointed_ehh2 noloop
        lc "Well if it makes you feel better, you're still doing quite well in our little competition here."
        play voice2 mc_yes_ugu1 noloop
        mc "Thank you, [e07_lcname!t]."
    elif e07_mc_wins == 3:
        scene e07s06-141 final_challenge_menu_dont_cheat_one_loss_lc_talk_nice with dissolve
        play voice3 dahlia_disappointed_ehh2 noloop
        lc "You really need to think about putting in more of an effort."
        lc "Or maybe you're tired of trying to win my favor."
        scene e07s06-142 final_challenge_menu_dont_cheat_one_loss_mc_talk_nice with dissolve
        play voice2 mc_no_no4 noloop
        mc "Not at all, [e07_lcname!t]. I love you and I'll do anything to be with you."
        scene e07s06-145 final_challenge_menu_dont_cheat_two_loss_mc_talk_holes with dissolve
        play voice2 mc_happy_oof2 noloop
        mc "But the girl I was dealing with, she had the throat of a succubus."
        scene e07s06-146 final_challenge_menu_dont_cheat_two_loss_lc_talk_amused with dissolve
        lc "..."
    elif True:
        scene e07s06-147 final_challenge_menu_dont_cheat_three_loss_lc_talk_angry with dissolve
        play voice3 dahlia_disappointed_ehh2 noloop
        lc "Well..."
        scene e07s06-144 final_challenge_menu_dont_cheat_two_loss_mc_talk_determined with dissolve
        play voice2 mc_yes_yes2 noloop
        mc "Yes?"
        scene e07s06-143 final_challenge_menu_dont_cheat_two_loss_lc_talk_bored with dissolve
        play voice3 dahlia_angry_hm1 noloop
        lc "That was your third loss. What do you have to say for yourself?"
        scene e07s06-148 final_challenge_menu_dont_cheat_three_loss_mc_talk_confused with dissolve
        play voice2 d3s7_mcemm noloop
        mc "I... I don't know. Usually I have no problem going longer."
        mc "But that last girl... it felt like she was draining my soul."
        scene e07s06-149 final_challenge_menu_dont_cheat_three_loss_lc_talk with dissolve
        play voice3 dahlia_thinking_oh noloop
        lc "I'll be sure to pass along your compliments."
        lc "But that's a real shame. I thought you wanted to give your soul and your love to me."
        scene e07s06-150 final_challenge_menu_dont_cheat_three_loss_mc_talk_tired_sad with dissolve
        play voice2 mc_disappointed_ah2 noloop
        mc "I did - I mean I do. I'll do better, I promise."
        scene e07s06-151 final_challenge_menu_dont_cheat_three_loss_lc_talk_amused with dissolve
        play voice3 dahlia_thinking_mmm2 noloop
        lc "Hmmmph."

    jump e07s06_bonus_challange

label e07s06_bonus_challange:

    play sound sfx_message_in1
    scene e07s06-152 final_challenge_menu_dont_bonus_challenge_lc_talk_look_phone with dissolve
    $ Lovense.vibrate(1)
    play voice3 dahlia_disappointed_hmm1 noloop
    lc "Hmmm."
    scene e07s06-153 final_challenge_menu_dont_bonus_challenge_lc_talkf_mc_won_lost with dissolve
    play voice3 lydia_lydiahey noloop
    if e07s06_cheat is True:
        lc "It looks like you have a chance to get an extra point."
        lc "If you're interested, [e07_mcname!t]."
    elif True:
        lc "Well, it seems like fortune smiles on you, [e07_mcname!t]."
        lc "There is a chance for you to make up the point you lost."
    scene e07s06-154 final_challenge_menu_dont_bonus_challenge_mc_talk_curious_arj_retrun with dissolve
    play voice2 mc_surprised_huh3 noloop
    mc "What would I have to do?"
    scene e07s06-155 final_challenge_menu_dont_bonus_challenge_lc_talk_smiles with dissolve
    play voice3 lydia_haha noloop volume 1.5
    pause
    play sound sfx_message_out1
    scene e07s06-156 final_challenge_menu_dont_bonus_challenge_lc_talk_send_text with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    lc "Watch."
    play sound sfx_cloth_rustling1
    scene e07s06-157 final_challenge_menu_dont_bonus_challenge_mc_talk_look_hole with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "That's definitely not a gopher."
    scene e07s06-158 final_challenge_menu_dont_bonus_challenge_lc_talk_smile with dissolve
    play voice3 dahlia_happy_laugh5 noloop
    lc "Haha. No, it's not."
    scene e07s06-159 final_challenge_menu_dont_bonus_challenge_lc_moves_mc_watch with dissolve
    pause
    scene e07s06-160 final_challenge_menu_dont_bonus_challenge_lc_talk_on_knees with dissolve
    play voice3 dahlia_disgust_oeah noloop
    lc "Ooooh, someone is excited."
    scene e07s06-161 final_challenge_menu_dont_bonus_challenge_lc_open_mouth with dissolve
    pause
    scene e07s06-162 final_challenge_menu_dont_bonus_challenge_mc_look_unhappy with dissolve
    pause
    scene e07s06-a163-1 final-challenge-lc-bj-anim-00 with dissolve
    pause
    scene e07s06-a163-1
    play voice3 daisy_fsucking
    play sound mc_sex_sucking_fast2 loop
    $ Lovense.pattern("7;10", 1400)
    lc "Glrrrphh... mrrrhpphh..."
    pause
    scene e07s06-a163-2 with dissolve
    pause
    scene e07s06-164 final_challenge_menu_dont_bonus_challenge_mc_thought with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "[e07_lcname!t]. You're so hot... but... do you really have to do this to me?"
    $ Lovense.pattern("7;10", 700)
    scene e07s06-a163-1-f with dissolve
    lc "*lewd sucking*"
    pause
    scene e07s06-a163-2-f with dissolve
    pause
    scene e07s06-166 final_challenge_menu_dont_bonus_challenge_mc_thought with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "Fuck. This is getting worse and worse!"
    $ Lovense.stop()
    $ Lovense.vibrate(3)
    stop sound fadeout 1.0
    scene e07s06-167 final_challenge_menu_dont_bonus_challenge_lc_pullsout with dissolve
    play voice3 dahlia_happy_relief noloop
    pause
    scene e07s06-168 final_challenge_menu_dont_bonus_challenge_lc_talk_stand_wipe with dissolve
    play voice3 dahlia_hey_angry noloop
    lc "Now it's your turn, [e07_mcname!t]."
    scene e07s06-169 final_challenge_menu_dont_bonus_challenge_mc_talk with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    scene e07s06-170 final_challenge_menu_dont_bonus_challenge_lc_talk_win_lose with dissolve
    play voice3 dahlia_arrogant_ha noloop
    if e07s06_cheat is True:
        lc "Relieve them, and I'll give you an extra point."
    elif True:
        lc "Service our new friend, and you can make up for your earlier loss."
    scene e07s06-171 final_challenge_menu_dont_bonus_challenge_lc_talk_hand_hips with dissolve
    play voice3 dahlia_arrogant_pff noloop
    lc "Is that clear enough for you?"
    scene e07s06-172 final_challenge_menu_dont_bonus_challenge_mc_talk with dissolve
    play voice2 d2s12_emmm noloop
    mc "Can I use my hands?"
    scene e07s06-173 final_challenge_menu_dont_bonus_challenge_lc_talk_nope with dissolve
    play voice3 dahlia_no_nope noloop
    lc "Nope. I want to see those lovely lips of yours working that meat."
    scene e07s06-174 final_challenge_menu_dont_bonus_challenge_mc_talk with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "Why?"
    scene e07s06-175 final_challenge_menu_dont_bonus_challenge_lc_talkrritated with dissolve
    play voice3 dahlia_angry_argh1 noloop
    lc "Your place isn't to question, [e07_mcname!t]. I'm sure you've gotten horny watching me have fun with other girls."
    scene e07s06-176 final_challenge_menu_dont_bonus_challenge_lc_talk_bored with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    lc "But if you're not interested in my little bonus challenge, just say so."
    lc "Still, can you afford to pass up the chance?"
    menu:
        "Suck the dick for Lydia"(hint="e07s06m02c01"):
            $ e07s06_suck_dick = True
            $ e07_mc_wins += 1
            jump e07s06_suck_dick
        "Don't suck the dick"(hint="e07s06m02c02"):

            $ e07s06_suck_dick = False
            jump e07s06_no_bj

label e07s06_suck_dick:

    scene e07s06-177 final_challenge_menu_suck_for_lydia_mc_talk with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Alright. All's fair in love and war."
    mct "I can't believe I'm doing this. But if it gets me closer to getting [e07_lcname!t] at the end of all this, it will be worth it."
    scene e07s06-178 final_challenge_menu_dont_bonus_challenge_lc_talk_surprised with dissolve
    play voice3 dahlia_yes_simple noloop
    lc "Yes, show me just how deep your love for me goes."
    scene e07s06-179 final_challenge_menu_dont_bonus_challenge_mc_kneel with dissolve
    pause
    scene e07s06-180 final_challenge_menu_dont_bonus_challenge_mc_thought_torn with dissolve
    play voice2 d14s16_smell noloop
    mct "Really wish I could use my hands."
    scene e07s06-181 final_challenge_menu_dont_bonus_challenge_mc_closes_eyes with dissolve
    play voice2 mc_thinking_mmm5 noloop
    pause
    scene e07s06-182 final_challenge_menu_dont_bonus_challenge_mc_thought_mouth with dissolve
    $ Lovense.vibrate(7)
    play sound mc_sex_sucking_slow2 loop
    play voice2 d1s5_orgasm noloop
    mct "Okay I did it. I actually have a cock in my mouth."
    mct "Holy fuck."
    scene e07s06-183 final_challenge_menu_dont_bonus_challenge_mc_open_eyes with dissolve
    play voice2 mc_pain_mff2 noloop
    mct "Okay, shouldnt' have opened my eyes."
    mct "That doesn't help at all!"
    scene e07s06-a184-1 final-challenge-mc-bj-anim-00 with dissolve
    pause
    $ Lovense.pattern("7;10", 1400)
    scene e07s06-a184-1
    pause
    scene e07s06-a184-2 with dissolve
    play voice4 mc_pain_mff5 noloop
    play voice2 mc_sex_sucking_slow2
    mc "Mrrllphh... phrrrmhh..."
    pause
    scene e07s06-185 final_challenge_menu_dont_bonus_challenge_mc_bj_lc_smile with dissolve
    play voice3 dahlia_old_moan1 noloop
    lc "Mrmmm...."
    scene e07s06-186 final_challenge_menu_dont_bonus_challenge_mc_bj_lc_talk with dissolve
    play voice3 dahlia_happy_phew noloop
    lc "There is really isn't a line you won't cross for me."
    lc "It's truly inspiring."
    $ Lovense.pattern("7;12", 700)
    scene e07s06-a184-1-f with dissolve
    pause
    scene e07s06-a184-2-f with dissolve
    pause
    scene e07s06-187 final_challenge_menu_dont_bonus_challenge_mc_bj_mc_thought with dissolve
    $ Lovense.stop()
    $ Lovense.vibrate(15)
    play voice2 mc_pain_mff4 noloop
    mct "Oh shit. They're getting close."
    stop sound fadeout 1.0
    scene e07s06-188 final_challenge_menu_dont_bonus_challenge_mc_talk_pulls_back with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "They're going to cum."
    mc "Can I-"
    $ Lovense.vibrate(17)
    play sound mc_cum_sound1
    scene e07s06-189 final_challenge_menu_dont_bonus_challenge_cum with hpunch
    pause
    scene e07s06-190 final_challenge_menu_dont_bonus_challenge_mc_talk_chin with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "Huh..."
    pause
    scene e07s06-191 final_challenge_menu_dont_bonus_challenge_lc_talk_cock_pullback with dissolve
    $ Lovense.vibrate(2)
    play voice3 dahlia_happy_laugh6 noloop
    lc "Well done, [e07_mcname!t]. Full marks."
    lc "Hahaha."
    scene e07s06-192 final_challenge_menu_dont_bonus_challenge_lc_talk_motion_arj with dissolve
    play voice3 dahlia_hey_greeting noloop
    lc "[e07_arjname!t], clean him up, and give him a happy ending."
    lc "[e07_mcname!t] deserves it."
    play sound sfx_cloth_wiping1
    scene e07s06-193 final_challenge_menu_dont_bonus_challenge_arj_talk_wipe with dissolve
    play voice4 amrose_thinking_emm noloop
    arj "Are you okay?"
    scene e07s06-194 final_challenge_menu_dont_bonus_challenge_mc_talk_wipe with dissolve
    play voice2 d9s2_yeah noloop volume 2.4
    mc "Yeah. It's just uh... well I didn't know I'd ever do that."
    mc "Before I met her..."
    stop sound fadeout 1.0
    scene e07s06-195 final_challenge_menu_dont_bonus_challenge_arj_talk_frowns with dissolve
    play voice4 amrose_happy_mmm noloop
    arj "..."
    scene e07s06-196 final_challenge_menu_dont_bonus_challenge_lc_talk with dissolve
    play voice3 dahlia_angry_argh1 noloop
    lc "What's keeping you. Come on, [e07_arjname!t]."
    scene e07s06-197 final_challenge_menu_dont_bonus_challenge_arj_drop_towel_reach with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Ahuaah..."
    scene e07s06-a200-1 final-challenge-arj-handjob-anim-01 with dissolve
    pause
    $ Lovense.pattern("5;8", 1400)
    scene e07s06-a200-1
    play voice2 d7s4_mcbreathing
    play sound sfx_handjob_cream1 loop
    play voice4 daisy_moaning
    pause
    arj "*light panting*"
    scene e07s06-a200-2 with dissolve
    mct "Mrmmm. Feels good having AmRose's hands on me."
    pause
    scene e07s06-a200-3 with dissolve
    mct "Those other girls were fucking ravenous."
    pause
    $ Lovense.pattern("5;8", 700)
    scene e07s06-a200-1-f with dissolve
    pause
    scene e07s06-a200-2-f with dissolve
    pause
    scene e07s06-a200-3-f with dissolve
    pause
    stop voice4 fadeout 1.0
    scene e07s06-202 final_challenge_menu_dont_bonus_challenge_mc_talk with dissolve
    $ Lovense.stop()
    $ Lovense.vibrate(5)
    mc "..."
    play voice2 d2s9_confused noloop
    mc "Uh, is something wrong?"
    scene e07s06-203 final_challenge_menu_dont_bonus_challenge_arj_talk with dissolve
    play voice4 amrose_no_simple1 noloop
    arj "No. Why would anything be wrong?"
    scene e07s06-204 final_challenge_menu_dont_bonus_challenge_mc_talk with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "I don't know. Just... feels different."
    scene e07s06-205 final_challenge_menu_dont_bonus_challenge_lc_talk with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    lc "Hmmm."
    scene e07s06-206 final_challenge_menu_dont_bonus_challenge_arj_talk with dissolve
    play voice4 amrose_no_nah noloop
    arj "It must be your imagination."
    scene e07s06-207 final_challenge_menu_dont_bonus_challenge_lc_talk_step_forward with dissolve
    play voice3 dahlia_no_serious noloop
    lc "No, it's not his imagination, [e07_arjname!t]. A blind monkey could jerk him off better than that."
    stop sound fadeout 1.0
    scene e07s06-208 final_challenge_menu_dont_bonus_challenge_arj_talk with dissolve
    play voice4 amrose_disappointed_ehh2 noloop
    arj "I guess I'm not in the mood."
    scene e07s06-209 final_challenge_menu_dont_bonus_challenge_lc_shove_aside_arj with dissolve
    play voice3 dahlia_angry_ah2 noloop
    lc "I will deal with you later."
    $ Lovense.vibrate(8)
    play sound maria_kiss1
    play sound2 sfx_cloth_rustling2 noloop
    scene e07s06-210 final_challenge_menu_dont_bonus_challenge_lc_talk_mc_lay with dissolve
    play sound sfx_handjob_cream1 loop
    play voice3 dahlia_thinking_mmm2 noloop
    lc "*lewd kissing* Let me kiss it and make it better."
    scene e07s06-211 final_challenge_menu_dont_bonus_challenge_mc_talk with dissolve
    play voice2 mc_scared_oh4 noloop
    mct "Oh my god. This is perfect after everything today"
    scene e07s06-212 final_challenge_menu_dont_bonus_challenge_lc_balls_mc_thought with dissolve
    play voice2 d7s4_mcbreathing
    mct "All these challenges, I must be doing something right."
    stop sound fadeout 1.0
    scene e07s06-213 final_challenge_menu_dont_bonus_challenge_lc_lick_mc_thought with dissolve
    play voice3 mc_sex_sucking_slow1
    mct "[e07_lcname!t] must be finally ready to truly accept me."
    scene e07s06-214 final_challenge_menu_dont_bonus_challenge_lc_lick_mc_talk_cumming with dissolve
    $ Lovense.vibrate(14)
    play voice2 mc_happy_oof2 noloop
    queue voice2 d7s4_mcbreathing
    mc "[e07_lcname!t]. I'm... I'm going to-"
    stop voice3 fadeout 1.0
    scene e07s06-215 final_challenge_menu_dont_bonus_challenge_lc_tongue_back_mc_thought with dissolve
    $ Lovense.vibrate(1)
    play voice2 mc_angry_hm2 noloop
    mct "Huh?"
    play sound sfx_sextoy_cuff1
    $ Lovense.vibrate(16)
    scene e07s06-216 final_challenge_menu_dont_bonus_challenge_lc_latch_mc_thought with dissolve
    pause
    $ Lovense.vibrate(1)
    scene e07s06-217 final_challenge_menu_dont_bonus_challenge_lc_talk with dissolve
    play voice3 mc_arrogant_tsktsk noloop
    lc "Tsk, tsk, tsk. I don't think so, [e07_mcname!t]."
    scene e07s06-218 final_challenge_menu_dont_bonus_challenge_mc_talk_surprised with dissolve
    play voice2 mc_pain_mff5 noloop
    mc "Mrrrhhaaa-huaak."
    mc "Why?"
    play sound sfx_cloth_rustling1
    scene e07s06-219 final_challenge_menu_dont_bonus_challenge_lc_talk_stands with dissolve
    play voice3 dahlia_arrogant_heh noloop
    lc "I never said if you sucked cock that you'd get to cum, [e07_mcname!t]."
    if e07_mc_wins >= 3:
        scene e07s06-220 final_challenge_menu_dont_bonus_challenge_lc_talk_leans_forward with dissolve
        play voice3 dahlia_happy_hmm2 noloop
        lc "But, don't worry."
        play sound sfx_hair_scratch1
        scene e07s06-221 final_challenge_menu_dont_bonus_challenge_lc_talk_stroke_chin with dissolve
        play voice3 dahlia_old_argh2 noloop
        lc "Your {i}reward{/i} is coming. Have no fear about that."
        scene e07s06-222 final_challenge_menu_dontf_false_mc_talk_stroke_chin with dissolve
        play voice2 mc_yes_okay2 noloop
        mc "Okay... That's... that's good, at least."
    scene e07s06-223 final_challenge_menu_dontf_false_lc_talk_stroke_chin with dissolve
    play voice3 dahlia_disgust_oof noloop
    lc "Now, come along. I have a busy evening planned, and it doesn't involve staying in this stinking space any longer."
    $ unlock_gallery_slot("scene", "e07s06")
    play sound sfx_heels_steps1
    scene e07s06-224 final_challenge_menu_dontf_false_leave_area with dissolve
    pause
    stop sound fadeout 1.0

    jump e07s06_end

label e07s06_no_bj:

    scene e07s06-225 final_challenge_menu_dont_suck_dick_lc_talk_disappointed with dissolve
    play voice3 dahlia_old_upset noloop
    lc "I thought you'd want the extra point."
    $ unlock_gallery_slot("scene", "e07s06")
    scene e07s06-226 final_challenge_menu_dont_suck_dick_mc_talk_disappointed with dissolve
    play voice2 mc_no_no5 noloop
    mc "Not that badly."
    scene e07s06-227 final_challenge_menu_dont_suck_dick_lc_talk_shrugs with dissolve
    play voice3 dahlia_angry_oh noloop
    lc "Suit yourself."
    scene e07s06-228 final_challenge_menu_dont_suck_dick_lc_talk_gestures with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    lc "Come along, my studs. We're done playing with the holes."

    jump e07s06_end

label e07s06_end:

    $ Lovense.stop()


    $ renpy.end_replay()
    stop music fadeout 3.0
    jump e07s07

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
