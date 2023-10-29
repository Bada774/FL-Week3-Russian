image e06s07-a15-glambot-1 = Movie(play = "images/E-06/s07/anim/e06s07-a15-2x-50fps.webm", start_image = "e06s07-a15 wedding-ceremony-begins-glambot-15-000", image = "e06s07-a15 wedding-ceremony-begins-glambot-15-238", loop = False)

label e06s07:

    scene black
    show screen scene_transistion(_("Two Weeks Later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.5, 0.0, "music2" )
    play music2 music_prewedding_melody_muffled fadein 1.5
    scene e06s07-01 sy-mc-preparing-lc-bathroom_c1
    with Fade(0.5, 0.5, 0.9)
    pause
    play sound sfx_cloth_rustling5
    scene e06s07-02 mc-asking-what-sy-doing-she-final-touches_c1 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "What are you doing?"
    play voice3 stacy_mmm2 noloop
    sy "Just the final touches. I've got to make sure you're perfectly dressed or else."
    mc "You sound nervous. Is Lydia giving you a hard time?"
    scene e06s07-03 sy-havent-seen-lc-yet-mes-gives-her-trouble_c1 with dissolve
    play voice3 stacy_upset1 noloop
    sy "I haven't seen her yet. It's Min."
    scene e06s07-04 mc-explains-mes-perfectionist-interupterd-by-sy_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Ah, that makes sense. Min is the ultimate perfectionist."
    sy "Can you believe she-?"
    scene e06s07-05 sy-says-enough-about-mes-how-mc-feeling_c1 with dissolve
    play voice3 stacy_hmm noloop
    sy "Nevermind. How about you? Are you nervous?"
    scene e06s07-06 mc-not-nervours-delegated-everything-sy_c1 with dissolve
    play voice2 d9s3_no noloop volume 2.2
    mc "Not in the slightest. That's your job."
    play voice3 stacy_angry noloop
    sy "This is probably the biggest day of your life - how are you not nervous?"
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "Easy. I delegated all that to you."
    mc "Don't get me wrong - Lydia and I have been nervous as hell for weeks and scrambling to make today perfect."
    scene e06s07-07 mc-will-enjoy-relax-while-sy-mes-do-work_c1 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Today we're just going to enjoy ourselves and leave all the stress to you and Min."
    play voice3 stacy_oh2 noloop
    sy "That explains a lot."
    mc "I told you that when you volunteered to be my best \"man\"."
    scene e06s07-08 sy-didnt-realize-mh-delegete-mes-stress-her_c1 with dissolve
    play voice3 stacy_yeahno noloop
    sy "True, but I didn't realize Lydia would delegate all her stress onto Min... who would then stress me out about every little detail!"
    play voice2 d2s9_confused noloop volume 1.5
    mc "Are you finally done fussing over my appearance yet?"
    sy "It's as good as it is going to get."
    scene e06s07-09 leans-next-sy-probably-should-get-dressed_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Good. The ceremony is going to start soon. You should probably get dressed."
    play voice3 stacy_huh2 noloop
    sy "What are you talking about? I am dressed."
    play voice2 mc_angry_hm1 noloop
    mc "That's what you're wearing to my wedding?"
    scene e06s07-10 sy-suit-practical-tactical-sexy-easy-come-off-mc-catches-drift_c1 with dissolve
    play voice3 stacy_yes2 noloop
    sy "It's tactical. It's practical. It's fancy. And it's sexy."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh."
    sy "Besides, it will come off easily afterwards."
    mc "I suppose there is that..."
    scene e06s07-11 mc-asks-sy-convinced-other-wear-mission-outfits_c1 with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "You didn't manage to convince anyone else to wear their mission outfits today, did you?"
    scene e06s07-12 sy-head-towards-door-as-explaining-mc-why-not_c1 with dissolve
    play voice3 stacy_no1 noloop
    sy "Sadly, no. I tried, but AmRose already had a dress and Hana wouldn't come."
    sy "I think she hates your intended bride."
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah, I haven't seen her since the trial. Que sera, sera."
    scene e06s07-13 sy-at-door-asks-mc-last-regrets-pov_c1 with dissolve
    play voice3 stacy_mmm1 noloop
    sy "Any last minute reservations?"
    play voice2 mc_no_nah2 noloop
    mc "None. I've never been more certain of anything before in my life."
    play voice3 polly_aga noloop
    sy "Alright. Let's get out there."
    scene e06s07-14 mc-reminds-sy-not-forget-rings-as-walks-out_c1 with dissolve
    play voice2 d2s9_mchey noloop volume 1.3
    mc "Don't forget the rings."
    stop music2 fadeout 5.4
    play sound sfx_door_open3

    jump e06s07_ceremony

label e06s07_ceremony hide:

    scene black
    show screen scene_transistion(_("15 minutes later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.5, 1.0, "sound3" )
    play sound3 park fadein 3.0
    if e06s05_dd_harem is True:
        scene e06s07-a15 wedding-ceremony-begins-glambot-15-000
        with Fade(0.5, 0.5, 0.5)
        pause
        $ renpy.music.set_volume(1.0, 0.0, "sound2")
        play sound [sfx_camera_fly1, sfx_camera_fly1] volume 1.5
        play sound2 ["<silence 2.5>", sfx_camera_fly1] noloop
        scene e06s07-a15-glambot-1
        pause
    elif True:
        scene e06s07-15 wedding-ceremony-begins_c1 with dissolve
        pause
    stop sound fadeout 1.0
    queue music music_wedding_ceremony
    scene e06s07-16 mh-whispers-mc-lc_c1 with dissolve
    play voice4 amrose_old_psst2 noloop
    mh "*whisper* You both look gorgeous."
    scene e06s07-17 mc-lc-both-happy_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.4
    mc "*whisper* Uh, thanks."
    play voice3 lydia_haha noloop
    lc "*whisper* Thank you. I've never felt better in my life."
    play voice2 mc_yes_yeah1 noloop
    mc "*whisper* What she said."
    scene e06s07-16 mh-whispers-mc-lc_c1 with dissolve
    play voice4 lissa_ugu2 noloop
    mh "*whisper* Let's start the show."
    scene e06s07-18 mh-begins-ceremony_c1 with dissolve
    play voice4 lissa_thinking noloop
    if e06s06_mh_harem is True:
        mh "Dearly Beloved - and by that I mean all of us here today..."
    elif True:
        mh "Dearly Beloved - and by that I mean all of you here today..."
    mh "... we are gathered here to celebrate the lawful union and bonds of matrimony between Lydia Cox and [mcname] Young."
    mh "The couple selected their own vows, which they will now read."
    scene e06s07-19 lc-asks-she-begins-mh-go-ahead_c1 with dissolve
    play voice3 lydia_hmmmm noloop
    lc "Should I go first?"
    play voice4 lissa_yes noloop volume 0.6
    mh "Yes. Go ahead."
    scene e06s07-20 lc-starts-her-vow_c1 with dissolve
    play voice3 lydia_oof noloop
    lc "Without doubt or question, I promise to love you, honor you, and submit myself to you in all things."
    lc "You were the first man I ever touched in an intimate way."
    lc "You were the first man I ever performed oral sex upon."
    scene e06s07-21 lc-continues-vow_c1 with dissolve
    play voice3 lydia_moan1 noloop
    lc "I give you my heart, my soul, and my virginity."
    lc "So long as we both shall live, you are the only man I shall enjoy being with sexually - unless you specifically order me to do otherwise."
    scene e06s07-22 mes-listens-lc-vow_c1 with dissolve
    play voice4 min_happy_mmm noloop
    lc "As Queen of your Harem, I join a proud sisterhood."
    lc "I will care for my new sisters as I would care for myself."
    scene e06s07-23 arj-listens-lc-vow_c1 with dissolve
    play voice4 amrose_happy_mmm noloop
    lc "I will ensure no strife between us comes to your attention."
    lc "I will ensure that each of us is available to sooth your mind and satisfy your body to the best of our abilities."
    scene e06s07-20 lc-starts-her-vow_c1 with dissolve
    play voice3 lydia_morningoh noloop
    lc "Should I or one of my sisters fail you, I shall present my body for your just punishment."
    lc "This I pledge, until death do us part."
    scene e06s07-27 mh-surprised-reaction-aswell_c1 with dissolve
    play voice4 lissa_oh2 noloop
    mh "Wow. I mean-"
    scene e06s07-26 mc-shocked-by-lc-vow_c1 with dissolve
    play voice2 d2s12_emmm noloop volume 1.5
    mc "I know we said we were going to write our own vows, but-"
    mc "Are you sure about all of that?"
    scene e06s07-28 mc-asking-if-lc-sure-lc-confirms_c1 with dissolve
    play voice3 lydia_lydyes noloop
    lc "I am."
    lc "That is to say, I do."
    scene e06s07-29 mh-reminds-mc-now-time-his-vow_c1 with dissolve
    play voice4 lissa_moan1 noloop
    mh "[mcname], I believe it is your turn to declare your vows."
    play voice2 mc_yes_yeah4 noloop
    mc "Um, yeah. This might seem a little unimpressive by comparison, but..."
    scene e06s07-30 focus-mc-starts-vow_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "Lydia, you are my sunlight in the morning, my favorite part of every day, and my favorite snuggle buddy at night."
    mc "Being with you is the best part of my existence."
    scene e06s07-31 mc-pledges-life-to-lc_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "I love you beyond measure, and vow to continue to do so even after the sun burns out."
    mc "I pledge my life, my heart, and my entire being to you for all eternity."
    scene e06s07-25 sy-listens-lc-vow_c1 with dissolve
    play voice4 stacy_hmm noloop
    mc "Every sexual conquest I experience, I will share with you."
    if e06s05_dd_harem is True:
        scene e06s07-24 dd-listens-to-vows_c1 with dissolve
    mc "Every breath I take, I will do for you."
    scene e06s07-32-01 no-dd-mc-ends-vow-wide-view_c1
    if e06s05_dd_harem is True:
        play voice4 daisy_impressed noloop
        show e06s07-32 mc-ends-vow-wide-view_c1
    with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "I am yours for all eternity."
    scene e06s07-33 lc-touched-by-vow_c1 with dissolve
    pause
    scene e06s07-34 mh-asking-if-that-all-mc-cant-think-of-anything-else_c1 with dissolve
    play voice4 dahlia_disappointed_hmm2 noloop
    mh "Is that it?"
    play voice2 mc_yes_yeah7 noloop
    mc "Um, yes. Did I forget anything?"
    scene e06s07-35-01 no-dd-mc-sees-harem-mh-reminds-him-tell-about-harem_c1
    if e06s05_dd_harem is True:
        show e06s07-35 mc-sees-harem-mh-reminds-him-tell-about-harem_c1
    with dissolve
    play voice4 lissa_laugh2 noloop
    mh "Did you want to say anything about your Harem?"
    play voice2 mc_scared_oh4 noloop
    mc "Oh! Um, give me a minute."
    scene e06s07-36 mc-tries-talk-harem-cant-find-words_c1 with dissolve
    play voice2 d14s16_smell noloop
    mc "Lydia, I accept you as Queen of my Harem."
    mc "I will -"
    play voice2 d1s5b_emmm noloop
    mc "Um, I will..."
    scene e06s07-37 arj-raises-hand_c1 with dissolve
    play voice3 amrose_thinking_emm noloop
    arj "May I help?"
    scene e06s07-38-01 no-dd-arj-offers-to-help-mc-agrees_c1
    if e06s05_dd_harem is True:
        show e06s07-38 arj-offers-to-help-mc-agrees_c1
    with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Yes, please."
    play voice4 lissa_aga noloop
    mh "Go ahead."
    scene e06s07-39 arj-steps-up-whispers-something-mc_c1 with dissolve
    play voice3 amrose_happy_laugh3 noloop
    arj "*whispers* You might want to..."
    scene e06s07-40 mc-eyes-widen-he-agrees_c1 with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "That sounds good to me. Let me see how much of that I remember."
    scene e06s07-41 mc-starts-repeating-arj-advice_c1 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "I pledge to use my Queen and my Harem to fulfill my sexual needs."
    mc "To see to their contentment and satisfy their sexual needs - either by myself or using members of my Harem."
    scene e06s07-42 lc-lovely-smile-as-mc-closes-vow_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.6
    mc "To assist Lydia in the management of my Harem."
    mc "And to love and care for each member of the Harem so long as they are useful to me."
    scene e06s07-43 arj-back-at-harem-give-thumbs-up_c1 with dissolve
    play voice3 amrose_happy_woo noloop
    arj "Perfect, [mcname]"
    scene e06s07-44 mh-agrees-mc-did-good-lc-has-more-to-say_c1 with dissolve
    play voice4 lissa_ugu noloop
    if e06s06_mh_harem is True:
        mh "I agree.{w} At this time I believe our Queen has additional vows on behalf of the Harem."
    elif True:
        mh "I agree.{w} At this time I believe the Queen has additional vows on behalf of the Harem."
    scene e06s07-45 lc-thanks-ly-begins-harem-vow_c1 with dissolve
    play voice3 lydia_aga noloop
    lc "Thank you, Lyssa. Yes, on behalf of the Harem I pledge the following:"
    scene e06s07-46 lc-looking-harem-as-they-recite-vow_c1 with dissolve
    play voice3 lydia_moan1 noloop
    lc "We pledge our bodies to [mcname]'s carnal pleasure."
    lc "We pledge our wombs to [mcname]'s offspring."
    scene e06s07-47 lc-finishes-vow-to-serve-mc-best-their-abilities_c1 with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    lc "We pledge our hearts to [mcname]'s tender care."
    lc "We will follow the guidance of our Queen and serve [mcname] to the best of our abilities."
    scene e06s07-48 mes-confrims-i-do_c1 with dissolve
    play voice4 min_yes_simple noloop
    mes "I do."
    scene e06s07-49 sy-says-i-do_c1 with dissolve
    play voice5 stacy_yes2 noloop
    sy "I do."
    scene e06s07-50 arj-also-confirms_c1 with dissolve
    play voice3 amrose_yes_confident1 noloop
    arj "Without question, I do."
    if e06s05_dd_harem is True:
        scene e06s07-51 dd-say-all-agree_c1 with dissolve
        play voice5 daisy_yay noloop
        dd "So say we all."
    if e06s06_mh_harem is True:
        scene e06s07-52 mh-agrees-as-well_c1 with dissolve
        play voice4 lissa_moan2 noloop
        mh "I whole-heartedly concur."
    scene e06s07-53 mh-asks-anyone-has-something-say-mc-says-i-do_c1 with dissolve
    mh "Is there anything else either of you would like to say before we continue?"
    play voice2 mc_yes_yes3 noloop
    mc "I do."
    mh "Go ahead."
    scene e06s07-54 mc-explains-he-meant-to-say-i-do_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "That was it. I just felt like I should say, \"I do\"."
    scene e06s07-55 mh-lc-share-smile_c1 with dissolve
    play voice4 lissa_shyoh noloop
    mh "Very well. Do you have the rings?"
    scene e06s07-56 mh-asks-rings-mc-wants-them-from-sy_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Um, Stacy?"
    scene e06s07-57 sy-steps-ahead-searching-jacket-mc-not-happy_c1 with dissolve
    play voice5 stacy_oh2 noloop
    sy "Oh, right. Just a second."
    play voice2 d1s1_mmm noloop
    mc "*whispers* You had one job."
    scene e06s07-58 sy-gives-mc-rings_c1 with dissolve
    play voice5 polly_aga noloop
    sy "Here they are!"
    play voice2 mc_happy_oof3 noloop
    mc "Thank you."
    play sound sfx_cloth_rustling2
    scene e06s07-59 lc-hand-engagement-ring-only_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Lydia, with this band I thee wed."
    scene e06s07-60 lc-so-happy-she-could-burst_c1 with dissolve
    play voice3 lydia_ah noloop
    lc "Oh, [mcname]. I'm so happy I could burst."
    play sound sfx_handjob_cream1 volume 2.0
    scene e06s07-61 lc-puts-finger-mc-hand_c1 with dissolve
    stop sound fadeout 0.3
    play voice3 lydia_oof noloop
    lc "[mcname], my King, my Love, my Master in all things. With this band I thee wed."
    scene e06s07-62 lc-mh-hold-hands-as-mh-forgot-detail_c1 with dissolve
    play voice4 lissa_oh2 noloop
    mh "Oops. I forgot one little detail."
    scene e06s07-63-01 no-dd-harem-has-no-objections_c1
    if e06s05_dd_harem is True:
        show e06s07-63 harem-has-no-objections_c1
    with dissolve
    mh "If there is anyone present who has cause why these two should not be wed, speak now or forever hold your peace."
    scene e06s07-64 mh-pronounce-mc-lc-married_c1 with dissolve
    play voice4 daisy_hey noloop
    mh "Then by the power invested in me by the State I now declare you man, wife, and harem."
    scene e06s07-65 mh-tells-mc-can-kiss-bride_c1 with dissolve
    play voice4 lissa_haha noloop
    mh "You may kiss the bride!"
    play sound dahlia_kiss_french1
    play voice2 mc_pain_mff1 noloop
    play voice3 dahlia_sex_closedmoan1 noloop
    $ renpy.music.set_volume(1.0, 0.0, "sound2")
    play sound2 sfx_cloth_planket2 noloop
    scene e06s07-66 mc-kiss-lc-passionately_c1 with dissolve
    pause
    play voice4 amrose_happy_woohoo noloop
    play voice5 min_happy_yay noloop
    play voice6 stacy_greetings noloop
    play sound sfx_wineglass_ding1
    scene e06s07-67-01 no-dd-harem-happy-reaction_c1
    if e06s05_dd_harem is True:
        play voice2 daisy_yay2 noloop
        show e06s07-67 harem-happy-reaction_c1
    with dissolve
    pause
    $ unlock_gallery_slot("cg", "e06s07")
    scene e06s07-68-01 overview-wedding-ceremony-complete-no-dd_c1
    if e06s05_dd_harem is True:
        show e06s07-68 overview-wedding-ceremony-complete_c1
    with dissolve
    pause

    $ renpy.music.set_volume(0.0, 2.0, "sound3" )
    jump e06s08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
