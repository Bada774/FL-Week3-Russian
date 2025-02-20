image e17s05-a33-1 = Movie(play = "images/E-17/s05/anim/e17s05-a33-1-2x-50fps.webm", start_image = "e17s05-a33-1 mc-lick-dw-anim-01")
image e17s05-a33-1-f = Movie(play = "images/E-17/s05/anim/e17s05-a33-1-2x-60fps.webm", start_image = "e17s05-a33-1 mc-lick-dw-anim-01")
image e17s05-a33-2 = Movie(play = "images/E-17/s05/anim/e17s05-a33-2-2x-50fps.webm", start_image = "e17s05-a33-2 mc-lick-dw-anim-01")
image e17s05-a33-2-f = Movie(play = "images/E-17/s05/anim/e17s05-a33-2-2x-60fps.webm", start_image = "e17s05-a33-2 mc-lick-dw-anim-01")

image e17s05-a44-1 = Movie(play = "images/E-17/s05/anim/e17s05-a44-1-2x-50fps.webm", start_image = "e17s05-a44-1 mc-fucks-dw-gusto-anim-01")
image e17s05-a44-1-f = Movie(play = "images/E-17/s05/anim/e17s05-a44-1-2x-60fps.webm", start_image = "e17s05-a44-1 mc-fucks-dw-gusto-anim-01")
image e17s05-a44-2 = Movie(play = "images/E-17/s05/anim/e17s05-a44-2-2x-50fps.webm", start_image = "e17s05-a44-2 mc-fucks-dw-gusto-anim-01")
image e17s05-a44-2-f = Movie(play = "images/E-17/s05/anim/e17s05-a44-2-2x-60fps.webm", start_image = "e17s05-a44-2 mc-fucks-dw-gusto-anim-01")
image e17s05-a44-3 = Movie(play = "images/E-17/s05/anim/e17s05-a44-3-2x-50fps.webm", start_image = "e17s05-a44-3 mc-fucks-dw-gusto-anim-01")
image e17s05-a44-3-f = Movie(play = "images/E-17/s05/anim/e17s05-a44-3-2x-60fps.webm", start_image = "e17s05-a44-3 mc-fucks-dw-gusto-anim-01")

image e17s05-a55-1 = Movie(play = "images/E-17/s05/anim/e17s05-a55-1-2x-50fps.webm", start_image = "e17s05-a55-1 mc-fucks-dw-anal-cowgirl-anim-01")
image e17s05-a55-1-f = Movie(play = "images/E-17/s05/anim/e17s05-a55-1-2x-60fps.webm", start_image = "e17s05-a55-1 mc-fucks-dw-anal-cowgirl-anim-01")
image e17s05-a55-2 = Movie(play = "images/E-17/s05/anim/e17s05-a55-2-2x-50fps.webm", start_image = "e17s05-a55-2 mc-fucks-dw-anal-cowgirl-anim-01")
image e17s05-a55-2-f = Movie(play = "images/E-17/s05/anim/e17s05-a55-2-2x-60fps.webm", start_image = "e17s05-a55-2 mc-fucks-dw-anal-cowgirl-anim-01")
image e17s05-a55-3 = Movie(play = "images/E-17/s05/anim/e17s05-a55-3-2x-50fps.webm", start_image = "e17s05-a55-3 mc-fucks-dw-anal-cowgirl-anim-01")
image e17s05-a55-3-f = Movie(play = "images/E-17/s05/anim/e17s05-a55-3-2x-60fps.webm", start_image = "e17s05-a55-3 mc-fucks-dw-anal-cowgirl-anim-01")

image e17s05-a66-1 = Movie(play = "images/E-17/s05/anim/e17s05-a66-1-2x-50fps.webm", start_image = "e17s05-a66-1 mc-choking-dw-while-anal-anim-01")
image e17s05-a66-1-f = Movie(play = "images/E-17/s05/anim/e17s05-a66-1-2x-60fps.webm", start_image = "e17s05-a66-1 mc-choking-dw-while-anal-anim-01")
image e17s05-a66-2 = Movie(play = "images/E-17/s05/anim/e17s05-a66-2-2x-50fps.webm", start_image = "e17s05-a66-2 mc-choking-dw-while-anal-anim-01")
image e17s05-a66-2-f = Movie(play = "images/E-17/s05/anim/e17s05-a66-2-2x-60fps.webm", start_image = "e17s05-a66-2 mc-choking-dw-while-anal-anim-01")
image e17s05-a66-3 = Movie(play = "images/E-17/s05/anim/e17s05-a66-3-2x-50fps.webm", start_image = "e17s05-a66-3 mc-choking-dw-while-anal-anim-01")
image e17s05-a66-3-f = Movie(play = "images/E-17/s05/anim/e17s05-a66-3-2x-60fps.webm", start_image = "e17s05-a66-3 mc-choking-dw-while-anal-anim-01")

label e17s05:

    scene black
    show screen scene_transistion(_("Many Days Later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_jail_door_open1
    scene e17s05-01 dw-looking-camera-warden-voice-calls-her_c1
    queue music music_viola_loss
    with Fade(0.5, 0.5, 0.9)
    pause
    play voice5 boy5_hey_angry noloop
    "Warden" "Prisoner Two-One-One-Nine-Zero-Nine-Zero-Five!"
    scene e17s05-02 dw-cuffed-wrists_c1 with dissolve
    play voice3 dahlia_yes_questioning noloop
    dw "Yes, Warden?"
    play sound sfx_sextoy_uncuff1
    scene e17s05-03 dw-confused-wants-know-what-this-about-fade_c1 with dissolve
    play voice5 boy5_arrogant_hm noloop
    "Warden" "Convict! Welcome to the visitation area. Also known as the conjugal trailer."
    play voice3 dahlia_surprised_huh2 noloop
    dw "Warden? What am I doing here?"
    play voice5 boy5_arrogant_huh noloop
    "Warden" "Convict! You will have a VISITOR! Make Yourself Ready!!!"
    scene e17s05-04 dw-cuffs-gone-will-have-visitor_c1 with dissolve
    play voice3 dahlia_surprised_huh1 noloop
    dw "A visitor? In the conjugal trailer?"
    dw "What the hell is this about?"

    jump e17s05_sex

label replay_e17s05:
label e17s05_sex:

    if _in_replay:
        $ renpy.music.set_volume(0.5, 0.0, "music")
        play music music_viola_loss
    scene e17s05-05 mc-enters-hello-mistress-dw-surprised_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "Hey, Mistress."
    play voice3 dahlia_pain_ah2 noloop
    dw "[mcname]?"
    scene e17s05-06 mc-dw-kiss-middle-room_c1 with dissolve
    play sound dahlia_kiss_french1
    play voice2 d1s1_mmm noloop
    mct "They said I was in that coma for the last four months."
    scene e17s05-07 dw-tears-running-down_c1 with dissolve
    play voice3 girl12_pain_sobs2 noloop
    mct "I can only imagine the hell she's been through during that time."
    scene e17s05-08 dw-wipes-tears-asking-if-here-mc-confirms_c1 with dissolve
    queue voice3 girl12_pain_sobs4 noloop
    dw "You're here?{w} Am I dreaming?"
    play voice2 mc_no_no5 noloop
    mc "This is real. I'm here.{w} I would never leave you like that."
    scene e17s05-09 dw-tell-mc-were-dead-mc-inform-mix-paperwork_c1 with dissolve
    play voice3 dahlia_pain_sobs noloop
    dw "But you were dead? I was convicted of your murder."
    play voice2 mc_yes_yeah5 noloop
    mc "They told me about that. Some mix up in the paperwork."
    scene e17s05-10 dw-insist-he-was-dead-mc-shrugs-it-off_c1 with dissolve
    play voice3 dahlia_pain_ah3 noloop
    dw "But I killed you? You weren't breathing. You were dead!"
    play voice2 mc_arrogant_nah1 noloop
    mc "*shrug* I got better."
    scene e17s05-11 dw-turns-away-calls-mc-ass-he-asks-be-punished_c1 with dissolve
    play voice3 dahlia_happy_laugh2 noloop
    dw "*chuckles* You ass."
    play voice2 mc_yes_yeah1 noloop
    mc "I know. You should punish me for that one."
    scene e17s05-12 dw-turns-towards-mc-never-again-mc-dont-understand_c1 with dissolve
    play voice3 dahlia_no_serious noloop
    dw "No.{w} Never again."
    play voice2 mc_thinking_mmm4 noloop
    mc "I don't understand."
    scene e17s05-13 dw-gets-serious-loves-him-never-hurt-him-again_c1 with dissolve
    play voice3 dahlia_old_upset noloop
    dw "I've missed you.{w} I love you."
    dw "I never want to hurt you ever again."
    scene e17s05-14 mc-ask-if-he-wants-dw-cant-find-words-confused_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "What if I want it?"
    play voice3 dahlia_disappointed_ehh3 noloop
    dw "I..."
    dw "I don't know.{w} I'm so confused right now."
    play sound sfx_cloth_rustling4
    scene e17s05-15 dw-presses-mc-chest-can-hear-him-ask-again-if-alive_c1 with dissolve
    play voice3 dahlia_happy_phew noloop
    dw "I can't believe it. I can even feel your heartbeat."
    dw "You're alive?"
    scene e17s05-16 mc-confirms-alive-dw-has-one-thing-please_c1 with dissolve
    play voice2 d9s2_mcyes noloop volume 2.2
    mc "I am, Mistress."
    play voice3 dahlia_disappointed_hmm2 noloop
    dw "Please?"
    mc "Anything."
    scene e17s05-17 dw-closeup-wants-called-by-name-mc-calls-her-dahlia_c1 with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    dw "Call me by my name."
    play voice2 d1s5b_ehhh noloop
    mc "Dahlia."
    scene e17s05-18 mc-comfirms-all-real-loves-dw_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "I'm alive. I'm standing here with you. This is real."
    mc "Dahlia, I love you."
    scene e17s05-19 dw-dreamt-moment-thought-was-awake_c1 with dissolve
    play voice3 dahlia_sex_closedmoan3 noloop
    dw "I've dreamed about this so many times."
    dw "Some of those times I even thought I was wide awake."
    scene e17s05-20 dw-steps-away-mc-he-ask-what-next-she-two-guesses_c1 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Well then, in those dreams, what happens next?"
    stop music fadeout 3.0
    play voice3 dahlia_arrogant_ha noloop
    dw "Two guesses..."


    $ Lovense.stop()

    play sound sfx_skirt_off2
    scene e17s05-21 dw-drops-top-on-floor_c1 with dissolve
    play music music_horny_forgiveness
    pause
    scene e17s05-22 dw-topless-second-guess-doesnt-count_c1 with dissolve
    $ Lovense.vibrate(1)
    play voice3 dahlia_disappointed_hmm1 noloop
    dw "And the second one doesn't count."
    play sound sfx_cloth_rustling5
    scene e17s05-23 mc-pushes-dw-on-bed_c1 with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "I think I know how this goes."
    mc "I've been dreaming about this for months."
    scene e17s05-24 dw-didnt-expect-this-mc-ask-what-did-expect_c1 with dissolve
    play voice3 dahlia_surprised_oh noloop
    dw "[mcname]? This isn't what I expected."
    play voice2 mc_surprised_what1 noloop
    mc "What did you think?"
    scene e17s05-25 dw-wants-mc-cock-all-he-thinks-her-pleasure_c1 with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    dw "I dreamed of your hard cock deep inside me."
    play voice2 mc_happy_yay2 noloop
    mc "Maybe this is my dream, because all I can think about right now is your pleasure."
    scene e17s05-26 dw-calls-mc-name-c-looks-up-wants-dw-hold-his-head_c1 with dissolve
    play voice3 dahlia_pain_ah1 noloop
    dw "Oh, [mcname]!"
    play voice2 mc_thinking_hmm2 noloop
    mc "Grab my head."
    scene e17s05-27 dw-surprised-what-mc-her-possession-thinks-about-it-since-woke-up_c1 with dissolve
    play voice3 dahlia_surprised_what noloop
    dw "What?"
    play voice2 mc_disappointed_off1 noloop
    mc "I deserve this. I'm your possession."
    mct "I've been thinking about this ever since I woke up."
    scene e17s05-28 dw-what-if-dont-want-to-mc-surprised_c1 with dissolve
    play voice3 dahlia_pain_argh noloop
    dw "But [mcname], what if I don't want to?"
    play voice2 mc_surprised_huh6 noloop
    mc "Huh?"
    scene e17s05-29 dw-loves-him-not-wanting-do-anything-mc-wants-to_c1 with dissolve
    play voice3 dahlia_angry_oof noloop
    dw "I love you. I don't want to make you do anything."
    play voice2 mc_thinking_mmm5 noloop
    mc "But I want you to."
    scene e17s05-30 dw-asking-what-if-hurt-again-mc-promises-wont_c1 with dissolve
    play voice3 dahlia_old_argh2 noloop
    dw "What if I hurt you again?"
    play voice2 mc_no_no4 noloop
    mc "You won't."
    scene e17s05-31 mc-wont-hurt-if-mutual-pleasure-wants-be-used-sexual-plaything_c1 with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    dw "What?"
    play voice2 mc_disappointed_ehh3 noloop
    mc "If you don't want to hurt me, then do it for our mutual pleasure."
    mc "Grab my head and use me as your sexual plaything."
    play voice2 d3s8_licking3 noloop
    scene e17s05-32 mc-starts-licking-dw_c1 with dissolve
    $ Lovense.vibrate(3)
    play voice3 dahlia_old_moan3 noloop
    dw "Oh, [mcname]!"
    scene e17s05-a33-1 with dissolve
    play voice2 mc_sex_sucking_slow1
    play voice3 dahlia_sex_openmoans2
    pause
    dw "Keep licking! *moans* You have the best tongue!"
    scene e17s05-a33-2 with dissolve
    dw "Ohhhhhh, fuck me."
    dw "Fuck me, [mcname]!"
    pause
    $ Lovense.vibrate(5)
    scene e17s05-a33-1-f with dissolve
    dw "Damn it. You really do your best work when I lead you by the nose."
    pause
    scene e17s05-a33-2-f with dissolve
    dw "That's it. Please me. Please your Mistress!"
    pause
    stop voice2 fadeout 1.0
    stop voice3 fadeout 1.0
    $ Lovense.vibrate(3)
    scene e17s05-37 mc-stops-licking-her-transition-missionary_c1 with dissolve
    pause
    play sound sfx_cloth_rustling4
    scene e17s05-38 mc-dw-lay-missionary-position_c1 with dissolve
    play voice3 dahlia_sex_closedmoan5 noloop
    dw "Fuck me, I've missed your cock."
    play voice2 mc_angry_errr4 noloop
    mc "I've been missing every inch of your body. And my cock has definitely been missing this."
    scene e17s05-39 mc-prepares-enter-dw-wait-mc-asking-what_c1 with dissolve
    play voice3 dahlia_old_uh noloop
    dw "[mcname], wait!"
    play voice2 mc_yes_yeah8 noloop
    mc "What is it, Mistress?"
    scene e17s05-40 dw-neverminds-mc-ask-sure-she-tell-him-later_c1 with dissolve
    play voice3 dahlia_happy_relief noloop
    dw "Never mind."
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "You're sure?"
    dw "I will tell you later."
    play sound sfx_fisting_fist2
    scene e17s05-41 mc-enters-dw-better-not-be-std-dw-tell-would-deserve-it_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "It better not be an S.T.D."
    play voice3 dahlia_old_laugh1 noloop
    dw "You would deserve that. Wouldn't you, my little worm?"
    scene e17s05-42 mc-okay-if-from-her-pauses-ask-if-really-std_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "As long as it came from you."
    mc "It's not... is it?"
    scene e17s05-43 dw-loves-mc-squirm-not-std-he-happy-with-it_c1 with dissolve
    play voice3 dahlia_thinking_oh noloop
    dw "Oh I've missed seeing you squirm. No. It's nothing like that. You aren't going to catch anything."
    play voice2 mc_happy_oof3 noloop
    mc "Oh, good."
    scene e17s05-a44-1 mc-fucks-dw-gusto-anim-01 with dissolve
    pause
    scene e17s05-a44-1
    play sound2 sfx_vagina_penetration1_fast volume 0.5
    play voice3 dahlia_sex_openmoans1
    play voice2 d7s4_mcbreathing
    $ Lovense.pattern("7;10", 1400)
    dw "Oh fuck. FUCK!"
    pause
    scene e17s05-a44-2 with dissolve
    dw "I've never been so full!"
    pause
    scene e17s05-a44-3 with dissolve
    mc "You like that?!"
    dw "YES!"
    pause
    play sound3 sfx_sex_bodyslaps1
    $ Lovense.pattern("7;10", 700)
    scene e17s05-a44-1-f with dissolve
    mc "You love it?!"
    dw "You have no idea!!"
    pause
    play sound3 sfx_sex_bodyslaps1
    scene e17s05-a44-2-f with dissolve
    mc "Christ! It's like your pussy is sucking me in!!!"
    pause
    play sound3 sfx_sex_bodyslaps1
    scene e17s05-a44-3-f with dissolve
    dw "*breathless* [mcname]. Oh... Slave! STOP!"
    play voice3 dahlia_angry_argh1 noloop
    dw "Remove that pitiful cock from my pussy right now!"
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene e17s05-49 mc-stops-surprised-ask-what-dw-ask-mc-forget-yourself_c1 with dissolve
    $ Lovense.stop()
    $ Lovense.vibrate(3)
    play voice2 mc_surprised_what3 noloop
    mc "What? Why?"
    play voice3 dahlia_angry_ah1 noloop
    dw "Do you forget yourself?!"
    play voice2 mc_angry_errr2 noloop
    mc "What? No, I mean...{w} Why, Mistress?"
    scene e17s05-50 dw-gets-evil-her-ass-needs-attention_c1 with dissolve
    play voice3 dahlia_arrogant_heh noloop
    dw "Because...{w} My ass needs your cock's attention!"
    scene e17s05-51 mc-wide-smile-gladly-mistress_c1 with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "GLADLY, MISTRESS!!!"
    scene e17s05-52 dw-top-mc-facing-him-told-him-call-her-dahlia_c1 with dissolve
    play voice3 dahlia_angry_argh2 noloop
    dw "I told you to call me Dahlia."
    play voice2 d2s12_emmm noloop
    mc "Of course, but-"
    scene e17s05-53 dw-aligns-cock-ass-dahlia-quiet-mistress-during-sex-mc-of-course_c1 with dissolve
    play voice3 dahlia_old_moan2 noloop
    dw "I know. Dahlia when... when it's quiet. *moans* Mistress during sex."
    play voice2 mc_yes_yes2 noloop
    mc "Of course, Mistress!"
    scene e17s05-a55-1 mc-fucks-dw-anal-cowgirl-anim-01 with dissolve
    pause
    $ Lovense.pattern("7;12", 1400)
    scene e17s05-a55-1
    play sound2 sfx_vagina_penetration1_fast volume 0.5
    play voice3 dahlia_sex_openmoans2
    play voice2 d7s4_mcbreathing
    pause
    scene e17s05-a55-2 with dissolve
    dw "Do you like my tight ass wrapped around your pathetic cock, my sweet?"
    pause
    scene e17s05-a55-3 with dissolve
    mc "I love it-"
    pause
    play sound3 sfx_sex_bodyslaps1
    $ Lovense.pattern("7;12", 1400)
    scene e17s05-a55-1-f with dissolve
    pause
    play sound3 sfx_sex_bodyslaps1
    scene e17s05-a55-2-f with dissolve
    pause
    play sound3 sfx_sex_bodyslaps1
    scene e17s05-a55-3-f with dissolve
    pause
    stop voice2 fadeout 1.0
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene e17s05-57 dw-asking-know-what-want-mc-suggest-choking-him_c1 with dissolve
    $ Lovense.stop()
    $ Lovense.vibrate(3)
    play voice3 dahlia_angry_hm2 noloop
    dw "Do you know what I want to do with you right now?"
    play voice2 mc_yes_yeah7 noloop
    mc "Do you want to choke me, Mistress?"
    scene e17s05-58 dw-stops-second-unsure-doesnt-want-lose-control-again_c1 with dissolve
    play voice3 dahlia_no_high3 noloop
    dw "No."
    dw "No, [mcname]. I'm afraid I would lose control again."
    scene e17s05-59 mc-has-faint-dw-she-knows-she-doesnt-but-have-trust-mc_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "I have complete faith in you."
    play voice3 dahlia_yes_yeah4 noloop
    dw "I know you do. I don't."
    dw "But I've realized something. I should trust you more."
    scene e17s05-60 mc-not-sure-dw-could-learn-lot-mc-guess-true_c1 with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    dw "You have the self control that I lack. I could learn a lot from you about that."
    play voice2 mc_disappointed_off2 noloop
    mc "Oh, well. I guess that's true."
    scene e17s05-61 dw-wants-do-something-mc-anything_c1 with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    dw "So, I want you to do something for me."
    play voice2 mc_yes_sure1 noloop
    mc "Anything."
    scene e17s05-62 dw-takes-mc-hand-wants-be-choked-mc-not-getting-it_c1 with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    dw "I want you to choke me."
    play voice2 mc_angry_huh1 noloop
    mc "Mistress?"
    scene e17s05-63 dw-puts-mc-hand-on-throat-wants-be-chocked_c1 with dissolve
    play voice3 dahlia_sex_closedmoan4 noloop
    dw "Choke me, [mcname]. I want to feel what you feel."
    dw "I want to experience that ecstasy and little death that you find so pleasurable."
    scene e17s05-64 mct-dahlia-desperate-agrees-dw-just-like-that_c1 with dissolve
    mct "She is so desperate for redemption. It's strange."
    play voice2 mc_angry_huh2 noloop
    mc "Of course I will do what you ask."
    play voice3 dahlia_old_moan2 noloop
    dw "Yes. Just like that."
    scene e17s05-65 mct-hold-neck-no-squeeze-mc-obeys-mistress_c1 with dissolve
    mct "I can do this. I'll hold her neck, but no squeezing."
    play voice2 mc_yes_okay2 noloop
    mc "Okay, Dahlia.{w} I mean, \"Yes, Mistress\"."
    scene e17s05-a66-1 mc-choking-dw-while-anal-anim-01 with dissolve
    pause
    $ Lovense.pattern("7;10", 1400)
    scene e17s05-a66-1
    play sound2 sfx_vagina_penetration1_fast volume 0.5
    play voice2 d7s4_mcbreathing
    play voice3 dahlia_sex_openmoans1
    pause
    scene e17s05-a66-2 with dissolve
    pause
    dw "Mrraah... Yes... I can feel it..."
    scene e17s05-a66-3 with dissolve
    pause
    mc "Yes, Mistress."
    mct "Mistress, I've missed you fucking me."
    play sound3 sfx_sex_bodyslaps1
    $ Lovense.pattern("7;14", 700)
    scene e17s05-a66-1-f with dissolve
    pause
    dw "Don't you dare cum before I do!"
    mc "I wouldn't dream of it."
    play sound3 sfx_sex_bodyslaps1
    scene e17s05-a66-2-f with dissolve
    play voice3 dahlia_sex_orgasming2
    dw "ALMOST-"
    mct "Just a little pressure for her orgasm..."
    play sound3 sfx_sex_bodyslaps1
    scene e17s05-a66-3-f with dissolve
    dw "GWAK!!!"
    mct "And let go for the climax"
    play voice3 girl12_angry_breath noloop
    stop voice2 fadeout 1.0
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(17)
    scene e17s05-70 dw-hard-orgasm_c1 with vpunch
    dw "GAAAHHAHAHHHHHAAAHH YESSSSS!!"
    queue voice3 dahlia_old_angry noloop
    dw "*breathless*Fucking. Amazing."
    dw "It seems... a coma hasn't completely robbed your usefulness."
    scene e17s05-71 dw-climbs-off-mc-happy-satisfy-her-she-tells-mc-deserves-reward_c1 with dissolve
    $ Lovense.vibrate(3)
    play voice2 mc_scared_oh4 noloop
    mc "I'm glad you're satisfied, Mistress."
    play voice3 dahlia_old_moan1 noloop
    dw "Very. You deserve something special."
    scene e17s05-72 dw-gets-knees-mc-ask-rewards-she-allow-him-cum-tits_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.8
    mc "I do?"
    play voice3 dahlia_happy_hmm2 noloop
    dw "You may cum on my tits."
    scene e17s05-73 mc-starts-jerking-off-dw-warns-aim-well-mc-ofcourse_c1 with dissolve
    $ Lovense.pattern("7;10", 700)
    play voice3 dahlia_angry_hm1 noloop
    play sound sfx_handjob_cream1 loop
    play voice2 d7s4_mcbreathing
    dw "Just be sure to aim well, Worm, or I'll break your balls."
    mc "Yes, Mistress."
    play voice3 dahlia_thinking_hmm4 noloop
    dw "If you get so much as a drop-"
    play voice2 d1s5_orgasm2 noloop
    play voice3 dahlia_pain_ah1 noloop
    play sound mc_cum_sound1
    $ Lovense.stop()
    $ Lovense.vibrate(16)
    scene e17s05-74 dw-cant-finish-mc-cums-on-tits_c1 with vpunch
    pause
    scene e17s05-75 dw-cum-all-over-tits-good-boy-wants-mc-clean-up_c1 with dissolve
    $ Lovense.vibrate(3)
    play voice3 dahlia_arrogant_yeah noloop
    dw "Good boy."
    dw "Now clean me up."

    $ Lovense.stop()


    $ renpy.end_replay()

    jump e17s05_end

label e17s05_end:

    scene e17s05-76 mc-dw-cuddle-bed_c1 with Fade(0.5, 0.5, 0.5)
    play voice3 dahlia_happy_hmm1 noloop
    dw "Those first few days, I just sat there. I couldn't move. All I could think of was you and what I did to you."
    dw "Then came the trial. I wasn't ready to face anyone, but had to tell the judge what happened."
    scene e17s05-77 dw-not-remembering-what-said-enough-for-jail_c1 with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    dw "I don't even remember what I said."
    dw "I guess it was enough to put me here."
    scene e17s05-78 dw-mumbles-mc-ask-what-is-it_c1 with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    dw "Then here... well..."
    play voice2 d1s5_mcthinks noloop volume 1.7
    mc "What is it?"
    scene e17s05-79 dw-puts-mc-hand-belly-talks_c1 with dissolve
    play voice3 dahlia_sex_closedmoan1 noloop
    dw "I don't know how to tell you this."
    dw "They do random drug tests and last month..."
    dw "... they found something unexpected."
    scene e17s05-80 mc-afraid-someone-drugged-her-she-says-no-he-thinks-confused_c1 with dissolve
    play voice2 mc_surprised_huh3 noloop
    mc "Someone drugged you?"
    play voice3 dahlia_no_simple noloop
    dw "No. Nothing like that."
    mct "I'm confused..."
    scene e17s05-81 dw-turns-mc-tells-she-pregnant_c1 with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    dw "We're pregnant."
    $ unlock_gallery_slot("scene", "e17s05")
    scene e17s05-82 mc-blank-expression-wow-dw-what-that-means_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh... wow."
    play voice3 dahlia_disappointed_hmm1 noloop
    dw "What does that mean?"
    play voice2 mc_thinking_hmm4 noloop
    mc "I'm thinking... this is a lot to process."
    scene e17s05-83 dw-nervous-ask-mc-upset-he-not-even-slightly_c1 with dissolve
    play voice3 dahlia_old_oh noloop
    dw "You're upset?"
    play voice2 mc_no_no3 noloop
    mc "No! Not in the slightest!"
    scene e17s05-84 mc-looks-dw-explains-she-not-want-raise-child-jail_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "I'm elated. I'm glad. I literally couldn't be happier."
    mc "This is just... unexpected."
    play voice3 dahlia_happy_hmm1 noloop
    dw "I know. This isn't where I wanted to raise a child."
    scene e17s05-85 mc-tells-dw-love-her-she-replies-cool_c1 with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Dahlia, I love you.{w} I love us - you, me, and our unborn child."
    mc "We'll make it work."
    play voice3 dahlia_yes_yeah4 noloop
    dw "Cool."
    scene e17s05-86 mc-thinks-what-means-tells-dw-no-need-do-this_c1 with dissolve
    mct "Cool? What does that mean?"
    mct "Oh, I think I get it."
    play voice2 mc_hey_hey1 noloop
    mc "You don't have to do that, hon."
    scene e17s05-87 dw-what-talking-about-mc-tells-deflecting-emotions_c1 with dissolve
    play voice3 dahlia_surprised_huh2 noloop
    dw "What are you talking about?"
    play voice2 mc_thinking_hmm5 noloop
    mc "You deflect your emotions. You retreat from admitting your thoughts or feelings."
    scene e17s05-88 mc-reiterates-no-nee-dw-must-trust-mc_c1 with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "You don't have to do that with me."
    mc "You can trust me."
    scene e17s05-89 dw-looks-at-cieling-talks-not-knowing-what-feeling-now_c1 with dissolve
    play voice3 dahlia_old_argh2 noloop
    dw "I know. I know that I can trust you."
    dw "It's just habit. I don't even let myself..."
    dw "I don't even know what I'm thinking or feeling right now."
    scene e17s05-90 dw-mc-lock-eyes-mc-wants-try-she-overwhelmed_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Try. For me."
    play voice3 dahlia_disappointed_hmm2 noloop
    dw "I guess I'm overwhelmed."
    scene e17s05-91 dw-prison-diff-country-mc-somehow-alive_c1 with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    dw "I'm in prison in a strange country. I don't even know the laws here, but murder is murder."
    dw "And yet somehow... you're alive.{w} You've come back to me."
    scene e17s05-92 somehow-raise-child-dw-loves-mc-beyond-words_c1 with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    dw "Somehow we're going to raise our child together, but I don't know how that could possibly work."
    dw "I love you beyond words."
    scene e17s05-93 dw-nevertheless-overwhelmed-mc-thanks-her_c1 with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    dw "But I'm overwhelmed."
    play voice2 mc_thinking_mmm5 noloop
    mc "Thank you."
    scene e17s05-94 distant-shot-mc-having-same-thought-will-figure-out_c1 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "To be honest, I'm having the same thoughts."
    mc "But I believe in us. We'll find some way-"
    scene e17s05-95 mc-dw-look-at-camera-war-ask-interupting_c1 with dissolve
    play voice5 boy5_arrogant_huh noloop
    "Warden" "*chuckles* Am I interrupting anything?"
    play sound sfx_cloth_planket2
    scene e17s05-96 dw-stands-up-no-warden-he-can-watch_c1 with dissolve
    play voice3 dahlia_pain_ah2 noloop
    dw "NO, WARDEN!"
    play voice5 boy5_thinking_hmm1 noloop
    "Warden" "Because I would be happy to wait and watch."
    scene e17s05-97 dw-unsure-mc-says-not-necessary_c1 with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    dw "Uh..."
    play voice2 d3s7_mcemm noloop
    mc "That won't be necessary."
    scene e17s05-98 dw-instictively-answers-warden-he-smart-girl_c1 with dissolve
    play voice3 dahlia_no_high2 noloop
    dw "THAT WON'T BE NECESSARY, WARDEN!"
    play voice5 boy5_thinking_hmm3 noloop
    "Warden" "Smart girl. Well, if you are finished..."
    scene e17s05-99 dw-yes-warden-he-tells-get-out-prison_c1 with dissolve
    play voice3 dahlia_yes_angry noloop
    dw "YES, WARDEN!"
    play voice5 boy5_angry_argh4 noloop
    "Warden" "THEN GET THE HELL OUT OF MY PRISON!!!"
    scene e17s05-100 mc-dw-exchange-confused-looks_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Me?"
    play voice5 boy5_angry_argh1 noloop
    "Warden" "Both of you."
    play voice3 dahlia_old_upset noloop
    dw "I don't understand..."
    scene e17s05-101 mc-looking-camera_c1 with dissolve
    play voice5 boy5_angry_errr2 noloop
    "Warden" "Don't be dim, fools."
    "Warden" "You didn't kill him. He isn't dead. You're not a convict anymore."
    play voice2 mc_thinking_emm1 noloop
    mc "I don't think it works that way... does it?"
    scene e17s05-102 war-ton-paperwork-get-naked-asses-out_c1 with dissolve
    play voice5 boy5_arrogant_yeah noloop
    "Warden" "Of course not. There was a ton of paperwork, but the judge signed off on it."
    "Warden" "Now get your naked asses out of my prison before I charge you with trespassing!!"
    scene e17s05-103 mc-dw-both-elated-thank-warden_c1 with dissolve
    play voice3 dahlia_pain_sobs noloop
    dw "YES, WARDEN!"
    play voice2 mc_happy_wooh3 noloop
    mc "Thank you!"
    play voice3 dahlia_sex_closedmoan5 noloop
    play sound dahlia_kiss_french1
    play sound2 sfx_sand_jump1 volume 2.0 noloop
    scene e17s05-104 dw-jump-mc-embrace-they-kiss-end-scene_c1 with dissolve
    play voice5 boy5_disappointed_ehh1 noloop
    "Warden" "Nice. Looks like I missed a passionate show."
    "Warden" "That's enough of that. Collect your belongings and get the fuck out."

    stop music fadeout 3.0
    jump e17s06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
