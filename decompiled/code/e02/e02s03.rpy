image e02s03-a60-1 = Movie(play = "images/E-02/s03/anims/e02s03-a60-1-2x-50fps.webm", start_image = "e02s03-a60-1 mc-mh-cowgirl-anim-01")
image e02s03-a60-1-f = Movie(play = "images/E-02/s03/anims/e02s03-a60-1-2x-60fps.webm", start_image = "e02s03-a60-1 mc-mh-cowgirl-anim-01")
image e02s03-a60-2 = Movie(play = "images/E-02/s03/anims/e02s03-a60-2-2x-50fps.webm", start_image = "e02s03-a60-2 mc-mh-cowgirl-anim-01")
image e02s03-a60-2-f = Movie(play = "images/E-02/s03/anims/e02s03-a60-2-2x-60fps.webm", start_image = "e02s03-a60-2 mc-mh-cowgirl-anim-01")
image e02s03-a60-3 = Movie(play = "images/E-02/s03/anims/e02s03-a60-3-2x-50fps.webm", start_image = "e02s03-a60-3 mc-mh-cowgirl-anim-01")
image e02s03-a60-3-f = Movie(play = "images/E-02/s03/anims/e02s03-a60-3-2x-60fps.webm", start_image = "e02s03-a60-3 mc-mh-cowgirl-anim-01")
image e02s03-a60-4 = Movie(play = "images/E-02/s03/anims/e02s03-a60-4-2x-50fps.webm", start_image = "e02s03-a60-4 mc-mh-cowgirl-anim-01")
image e02s03-a60-4-f = Movie(play = "images/E-02/s03/anims/e02s03-a60-4-2x-60fps.webm", start_image = "e02s03-a60-4 mc-mh-cowgirl-anim-01")

image e02s03-a61-1 = Movie(play = "images/E-02/s03/anims/e02s03-a61-1-2x-50fps.webm", start_image = "e02s03-a61-1 mc-mh-missionary-anim-01")
image e02s03-a61-1-f = Movie(play = "images/E-02/s03/anims/e02s03-a61-1-2x-60fps.webm", start_image = "e02s03-a61-1 mc-mh-missionary-anim-01")
image e02s03-a61-2 = Movie(play = "images/E-02/s03/anims/e02s03-a61-2-2x-50fps.webm", start_image = "e02s03-a61-2 mc-mh-missionary-anim-01")
image e02s03-a61-2-f = Movie(play = "images/E-02/s03/anims/e02s03-a61-2-2x-60fps.webm", start_image = "e02s03-a61-2 mc-mh-missionary-anim-01")
image e02s03-a61-3 = Movie(play = "images/E-02/s03/anims/e02s03-a61-3-2x-50fps.webm", start_image = "e02s03-a61-3 mc-mh-missionary-anim-01")
image e02s03-a61-3-f = Movie(play = "images/E-02/s03/anims/e02s03-a61-3-2x-60fps.webm", start_image = "e02s03-a61-3 mc-mh-missionary-anim-01")

image e02s03-a65-1 = Movie(play = "images/E-02/s03/anims/e02s03-a65-1-2x-50fps.webm", start_image = "e02s03-a65-1 mc-mh-rimming-anim-01")
image e02s03-a65-1-f = Movie(play = "images/E-02/s03/anims/e02s03-a65-1-2x-60fps.webm", start_image = "e02s03-a65-1 mc-mh-rimming-anim-01")
image e02s03-a65-2 = Movie(play = "images/E-02/s03/anims/e02s03-a65-2-2x-50fps.webm", start_image = "e02s03-a65-2 mc-mh-rimming-anim-01")
image e02s03-a65-2-f = Movie(play = "images/E-02/s03/anims/e02s03-a65-2-2x-60fps.webm", start_image = "e02s03-a65-2 mc-mh-rimming-anim-01")
image e02s03-a65-3 = Movie(play = "images/E-02/s03/anims/e02s03-a65-3-2x-50fps.webm", start_image = "e02s03-a65-3 mc-mh-rimming-anim-01")
image e02s03-a65-3-f = Movie(play = "images/E-02/s03/anims/e02s03-a65-3-2x-60fps.webm", start_image = "e02s03-a65-3 mc-mh-rimming-anim-01")

label e02s03:

    $ e02s03_cum_again = False

    scene black
    show screen scene_transistion(_("Later that evening"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    queue music languid_love
    scene e02s03-09 mc-mh-eat9_c1
    with Fade(0.5, 0.5, 0.9)
    play voice2 d1s5_mchappy noloop
    mc "I forgot to congratulate you."
    scene e02s03-09 mc-mh-eat9_c2 with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    mh "For what?"
    scene e02s03-09 mc-mh-eat9_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "For that whooping you gave me at chess after we got back from the slopes."
    scene e02s03-09 mc-mh-eat9_c2 with dissolve
    play voice3 dahlia_arrogant_heh noloop
    mh "Haha. Thank you. In all fairness to you, I think you were a little distracted."
    play voice2 mc_thinking_mmm4 noloop
    mc "Mmmhmmm. Hard to concentrate on an empty stomach."
    if d17s05_mh_op is True or d17s05_mh_sy is True:
        play sound sfx_cup_slide1
        scene e02s03-10 mc-mh-eat10_c1 with dissolve
        play voice2 mc_happy_a1 noloop
        mc "Even though I lost, I still enjoyed it. When we played Cards against Humans, that was one of those moments where I really got to know you, Lyssa."
        play voice3 lissa_yes noloop
        mh "Yes, it was a wonderful moment. You know it is a shame we did not pack the deck."
        mh "It would have been a lovely way to break the ice with the other guests."
    elif True:
        play sound sfx_cup_slide1
        scene e02s03-10 mc-mh-eat10_c1 with dissolve
        play voice3 lissa_haha2 noloop
        mh "I thought you were going to talk of how difficult it is to strategize when you sit across from me."
        play voice2 mc_happy_hah2 noloop
        mc "Haha. Well I figured that went without saying."
        mh "We should have brought a board game along. It would be the perfect strategy to help break the ice with the other guests."
    play voice3 daisy_dlick volume 1.5 noloop
    scene e02s03-11 mc-mh-eat11_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Totally. But you know me. I make friends easily."
    scene e02s03-10 mc-mh-eat10_c2 with dissolve
    play voice3 lissa_aga noloop
    mh "Yes, but games always help. You did not forget that without Secret Oral Santa, we might never have met."
    play voice2 mc_thinking_mmm3 noloop
    mc "Mmm. I don't think so."
    scene e02s03-11 mc-mh-eat11_c2 with dissolve
    play voice3 lissa_oh2 noloop
    mh "Oh? And why is that?"
    play sound sfx_plate_place1
    scene e02s03-12 mc-mh-eat12_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "I think we would have connected somehow... somewhere."
    scene e02s03-12 mc-mh-eat12_c2 with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    mh "Mmm, like we were meant to be."
    scene e02s03-18 mc-mh-ac-fc-eat18_c2 with dissolve
    mh "That's very sweet, [mcname]."
    play sound sfx_plate_place1
    scene e02s03-18-1 mc-mh-ac-fc-eat19_c2 with dissolve
    play voice3 lissa_ugu noloop
    mh "I think we would have found one another as well."
    scene e02s03-18-2 mc-mh-ac-fc-eat20_c2 with dissolve
    mh "Speaking of finding people."
    play sound sfx_cup_place1
    scene e02s03-19 mc-mh-ac-fc-talk1_c2 with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    mh "We should introduce ourselves to the other guests."
    scene e02s03-19 mc-mh-ac-fc-talk1_c1 with dissolve
    play voice2 d1s5_mcthinks noloop
    mct "Is that the couple we heard arguing earlier?"
    scene e02s03-19 mc-mh-ac-fc-talk1_c3 with dissolve
    pause
    scene e02s03-20 mc-mh-ac-fc-talk2_c2 with dissolve
    play voice4 claudie_disappointed_geh noloop
    ac "Honey, we're still not ready."
    scene e02s03-20 mc-mh-ac-fc-talk2_c1 with dissolve
    play voice5 boy5_no_nah noloop
    fc "I'm sure we can make it work."
    scene e02s03-21 mc-mh-ac-fc-talk3_c2 with dissolve
    play voice4 claudie_disappointed_eeh noloop
    ac "Frank, this is our first vacation in years. We barely have time for ourselves..."
    ac "Raising a child is a huge responsibility."
    scene e02s03-21 mc-mh-ac-fc-talk3_c1 with dissolve
    play voice5 boy5_yes_active noloop
    fc "So we'll get some helpers. I can ask Bill if he knows anyone who's looking for work."
    play sound sfx_bottle_chponk1
    scene e02s03-22 mc-mh-ac-fc-talk4_c2 with dissolve
    play voice4 claudie_arrogant_ha3 noloop
    ac "How are we going to afford that?"
    scene e02s03-22 mc-mh-ac-fc-talk4_c1 with dissolve
    play voice5 boy5_thinking_emm noloop
    fc "We'll... oh. Um well we will figure it out."
    play sound sfx_bottle_pouring1
    scene e02s03-23 mc-mh-ac-fc-talk5_c2 with dissolve
    play voice4 claudie_disappointed_eh noloop
    ac "I love you, but we can't just do something like this and hope it will all work out."
    scene e02s03-25 mc-mh-ac-fc-talk6_c2 with dissolve
    play voice4 claudie_disappointed_mmm noloop
    ac "Listen, let's just try to enjoy our time here."
    play sound sfx_bottle_pouring1 volume 1.6
    scene e02s03-25 mc-mh-ac-fc-talk6_c1 with dissolve
    play voice5 boy5_yes_yeah noloop
    fc "Alright, Ashley. I can do that."
    scene e02s03-26 mc-mh-ac-fc-hey_c1 with dissolve
    pause
    scene e02s03-26 mc-mh-ac-fc-hey_c2 with dissolve
    play voice5 boy5_hey_calm noloop
    fc "Hey, there!"
    fc "How's it going?"
    play sound sfx_plates_moving1
    scene e02s03-28 mc-mh-ac-fc-greet_c1 with dissolve
    stop sound fadeout 1.0
    play voice2 mc_arrogant_nah1 noloop
    mc "Not bad. You're not actually staff are you?"
    scene e02s03-28 mc-mh-ac-fc-greet_c2 with dissolve
    play voice5 boy5_happy_laugh1 noloop
    fc "Haha. Nope. Just serving up some drinks for me and the wife."
    fc "I'm Frank Cooper. Nice to meet you."
    play sound sfx_cloth_rustling1
    scene e02s03-29 mc-mh-ac-fc-handshake1_c2 with dissolve
    play voice4 claudie_happy_mmm1 noloop
    ac "Ashley."
    scene e02s03-29 mc-mh-ac-fc-handshake1_c1 with dissolve
    play voice3 lissa_ugu2 noloop
    mh "Lyssa. This is my boyfriend, [mcname]"
    play sound sfx_hands_clap3 volume 0.4
    scene e02s03-29-2 mc-mh-ac-fc-handshake2_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Nice to meet you."
    scene e02s03-29-2 mc-mh-ac-fc-handshake2_c2 with dissolve
    play voice4 claudie_thinking_hmm2 noloop
    ac "The pleasure is all mine."
    play sound sfx_kick3 volume 0.5
    scene e02s03-29-3 mc-mh-ac-fc-handshake3_c2 with dissolve
    play voice5 boy5_arrogant_hm noloop
    fc "So is this a pre-engagement trip? Or are you two here for the sessions?"
    scene e02s03-29-3 mc-mh-ac-fc-handshake3_c1 with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "It's our first big trip together. It's been amazing."
    play voice3 lissa_ugu noloop
    mh "Mmhmm."
    scene e02s03-30 mc-mh-ac-fc-talk1_c2 with dissolve
    play voice5 boy5_disappointed_oh2 noloop
    fc "Ah, my mistake. I can see it now, that glow on you both."
    fc "Well I'm still happy to meet you, we came up here for-"
    scene e02s03-30 mc-mh-ac-fc-talk1_c1 with dissolve
    play voice4 claudie_angry_eh noloop
    ac "Frank!"
    ac "Don't bore our new friends."
    play voice5 boy5_disappointed_hmm noloop
    fc "I'm just saying, they're very cozy. I figured they didn't come up for the couples' therapy."
    scene e02s03-32 mc-mh-ac-fc-talk3_c1 with dissolve
    play voice3 lissa_thinking noloop volume 1.4
    mh "Therapy?"
    play voice4 claudie_yes_simple noloop
    ac "Ahem.. yes. It's the main part of why we came here."
    scene e02s03-32 mc-mh-ac-fc-talk3_c2 with dissolve
    play voice5 boy5_arrogant_yeah noloop
    fc "Yeah but it's not really true therapy. The therapist got hurt so it's unlikely they'll make it here."
    fc "But we talked to the other couples and have still been trying to... I don't know, to share and figure out solutions."
    scene e02s03-32 mc-mh-ac-fc-talk3_c1 with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    mh "Interesting."
    scene e02s03-33 mc-mh-ac-fc-talk4_c1 with dissolve
    play voice4 claudie_thinking_hmm1 noloop
    ac "You two are welcome to join us. We set another meeting for two days from now."
    play voice2 d1s1_mmm noloop
    mct "I don't know if we should get involved."
    scene e02s03-34 mc-mh-ac-fc-talk5_c1 with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    mh "Are you sure we wouldn't be imposing?"
    play voice2 mc_angry_huh2 noloop
    mct "Hmmm."
    scene e02s03-34 mc-mh-ac-fc-talk5_c2 with dissolve
    play voice5 boy5_no_high noloop
    fc "That's kind of you, but I think it would be fine. Especially if you met the other couples."
    fc "It's all been very casual, no stress."
    scene e02s03-35 mc-mh-ac-fc-talk6_c1 with dissolve
    play voice4 claudie_yes_yeah2 noloop
    ac "Except for the stress that we haven't made any progress because we don't actually know what we're doing."
    play voice5 boy5_thinking_huh noloop
    fc "Well, we gotta get points for trying."
    play voice3 dahlia_thinking_mmm1 noloop
    mh "What do you talk about there?"
    scene e02s03-35 mc-mh-ac-fc-talk6_c2 with dissolve
    play voice5 boy5_arrogant_hah noloop
    fc "Anything that comes to mind, really."
    scene e02s03-36 mc-mh-ac-fc-talk7_c2 with dissolve
    play voice4 claudie_thinking_emm noloop
    ac "We try to focus on our problems, but well... then sometimes we only focus on those, instead of solutions."
    scene e02s03-36 mc-mh-ac-fc-talk7_c1 with dissolve
    play voice5 lissa_aga noloop
    mh "Well, if you really don't mind, we will think about stopping by."
    play voice2 d2s9_confused noloop
    mct "We will? I didn't picture Lyssa as a people watcher."
    scene e02s03-38 mc-mh-ac-fc-wink_c2 with dissolve
    play voice4 claudie_happy_yay noloop
    ac "Excellent."
    mct "Huh? Did Ashley just wink at me?"
    play sound sfx_heels_steps1 loop
    play sound3 sfx_heels_steps1
    scene e02s03-39 mc-mh-ac-fc-exit_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "*Whispers* Well this should be interesting."
    play voice3 lissa_laugh2 noloop
    mh "*Whispers* I was thinking the same thing."
    scene e02s03-39 mc-mh-ac-fc-exit_c2 with dissolve
    mh "*Whispers* Overall, I'm sure we'll just end up hanging out with them to help make their stay better since the therapist couldn't make it."
    mct "Even on a trip, Lyssa still likes to help people in need."
    play voice2 mc_yes_yes3 noloop
    mc "Sounds like a plan, gorgeous."
    stop sound fadeout 1.0
    stop sound3 fadeout 1.0

    jump e02s03_lodge

label e02s03_lodge:

    scene black
    show screen scene_transistion(_("In the lodge"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_door_open2 volume 1.6
    scene e02s03-40 mc-mh-talk1_c1
    with Fade(0.5, 0.5, 0.5)
    play voice2 mc_thinking_hmm1 noloop
    mc "Hmmm. I know you have your rules, but you might want to consider breaking them."
    play sound sfx_cloth_rustling2 volume 1.7
    scene e02s03-40 mc-mh-talk1_c2 with dissolve
    play voice3 lissa_haha noloop
    mh "Haha. I'm going wireless this trip. No beeps or vibrations. Just moans and gasps."
    play sound sfx_shoes_off1
    scene e02s03-41 mc-mh-mobile1_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "I love the sound of that, but these texts, well they're starting to pile up."
    scene e02s03-41 mc-mh-mobile1_c2 with dissolve
    play voice3 lissa_thinking noloop volume 1.4
    mh "I'm sure it can be handled. After our vacation has concluded."
    scene e02s03-42 mc-mh-mobile2_c2 with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    mh "Oliver can handle things. I think his anxiety is just acting up because I left him alone in the office."
    mh "When we get back, I'll be sure to thank him for all the extra work he did."
    scene e02s03-43 mc-mh-mobile3_c2 with dissolve
    play voice3 dahlia_disgust_meh noloop
    mh "You know, after all that wine, I'm feeling a little..."
    play sound sfx_throw_something1
    scene e02s03-44 mc-mh-mobile4_c1 with dissolve
    play voice2 d2s12_emmm noloop volume 1.4
    mc "Dizzy?"
    scene e02s03-44 mc-mh-mobile4_c2 with dissolve
    play voice3 dahlia_arrogant_hm noloop
    mh "Frisky, actually."
    play voice2 mc_scared_huuuh3 noloop
    scene e02s03-45 mc-mh-mobile5_c1 with dissolve
    pause
    scene e02s03-45 mc-mh-mobile5_c2 with dissolve
    pause
    play sound sfx_phone_fall1
    scene e02s03-46 mc-mh-mobile6_c3 with vpunch
    pause

label replay_e02s03 hide:
    if _in_replay:
        play music languid_love
    scene e02s03-46 mc-mh-mobile6_c2 with dissolve
    play voice3 lissa_laugh noloop
    mh "Would you be a gentleman and help me undress?"
    scene e02s03-47 mc-mh-undress1_c2 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "You know, I might have accepted my defeat too rashly."
    scene e02s03-47-2 mc-mh-undress2_c1 with dissolve
    play voice3 lissa_oh2 noloop
    mh "Oh, how do you figure?"
    play sound sfx_cloth_rustling3
    scene e02s03-47-2 mc-mh-undress2_c2 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "I mean, everything is going to be decided here. During the final round."
    play sound sfx_skirt_off2
    scene e02s03-48 mc-mh-talk1_c1 with dissolve
    mc "Are you ready?"
    scene e02s03-48 mc-mh-talk1_c2 with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    mh "Oh, how romantic. And I about to be dominated... like a beast in wild?"
    play sound sfx_jeans_on1
    scene e02s03-49 mc-mh-talk2_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.7
    mc "Haha. I am not some lowly beast. I'm the king of romance, like Cyrano de Bergerac. That's why you're with me."
    scene e02s03-49 mc-mh-talk2_c2 with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    mh "Mmm. That might be part of it. But you're so much more than a hopeless romantic, [mcname]"
    scene e02s03-50 mc-mh-talk3_c1 with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "You think I'm hopeless?"
    scene e02s03-50 mc-mh-talk3_c2 with dissolve
    play voice3 lissa_haha noloop
    mh "Hehe. I think you might have been before we met."
    play sound sfx_cloth_rustling4
    scene e02s03-51 mc-mh-bed_c2 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "I can live with that. Now come here..."

    $ Lovense.stop()

    $ renpy.music.set_volume(1.0, 3.0, "music" )
    play sound dahlia_kiss_french1
    scene e02s03-55 mc-mh-kiss_c1 with dissolve
    $ Lovense.vibrate(1)
    pause
    scene e02s03-55 mc-mh-kiss_c2 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "I love you."
    scene e02s03-56 mc-mh-kiss2_c1 with dissolve
    play voice3 lissa_moan2 noloop
    mh "I adore you, [mcname]"
    scene e02s03-56 mc-mh-kiss2_c2 with dissolve
    play voice3 lissa_moan3 noloop
    mh "*Moans softly* Your fingers are like little candles tickling my body."
    play voice2 d14s16_smell noloop
    mc "You smell so good."
    mh "Slip it in... I cannot wait any longer..."
    play sound sfx_cloth_rustling2
    scene e02s03-59 mc-mh-bed1_c1 with dissolve
    $ Lovense.vibrate(2)
    play voice2 d1s5_mcthinks noloop volume 1.7
    mc "Hmmm, what exactly am I supposed to be slipping inside of you?"
    play voice3 lissa_mmm1 noloop
    mh "That big... {i}throbbing{/i} cock of yours, Mr. de Bergerac."
    scene e02s03-a60-1 mc-mh-cowgirl-anim-01 with dissolve
    play voice3 lissa_moan1 noloop
    mh "Go slow."
    play voice3 [lissa_moan2, "<silence 1.0>", lissa_moan3, "<silence 1.0>", lissa_moan4, "<silence 1.0>", lissa_moan5, "<silence 1.0>", lissa_moan1, "<silence 1.0>"]
    play voice2 d7s4_mcbreathing
    play sound sfx_handjob_cream1 loop volume 2.0
    $ renpy.music.set_volume(0.5, 0.0, "sound4" )
    $ Lovense.pattern("7;11", 1700)
    play sound4 sfx_vagina_penetration1 fadein 1.0
    scene e02s03-a60-1
    pause
    scene e02s03-a60-2 with dissolve
    pause
    scene e02s03-a60-3 with dissolve
    mh "Make love to me. Make me yours."
    pause
    scene e02s03-a60-4 with dissolve
    pause
    queue voice3 [lissa_moan2, "<silence 0.7>", lissa_moan3, "<silence 0.7>", lissa_moan4, "<silence 0.7>", lissa_moan5, "<silence 0.4>", lissa_moan1, "<silence 0.5>"]
    play sound4 sfx_vagina_penetration1_fast fadein 1.0
    $ Lovense.pattern("7;11", 900)
    scene e02s03-a60-1-f with dissolve
    pause
    mc "You look so beautiful."
    scene e02s03-a60-2-f with dissolve
    pause
    scene e02s03-a60-3-f with dissolve
    pause
    mh "And you're my treasure. I was so afraid you wouldn't come with me. I wouldn't know what I'd do if you said no..."
    mc "I never want to disappoint you, Lyssa. You're my world..."
    scene e02s03-a60-4-f with dissolve
    pause
    stop sound4 fadeout 1.0
    stop voice2 fadeout 1.0
    stop voice3 fadeout 1.0
    stop sound fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(2)
    scene e02s03-a61-1 mc-mh-missionary-anim-01 with dissolve
    pause
    play voice3 [lissa_moan2, "<silence 1.0>", lissa_moan3, "<silence 1.0>", lissa_moan4, "<silence 1.0>", lissa_moan5, "<silence 1.0>", lissa_moan1, "<silence 1.0>"]
    play voice2 d7s4_mcbreathing
    play sound4 sfx_vagina_penetration1 fadein 1.0
    $ Lovense.pattern("8;12", 1700)
    scene e02s03-a61-1
    mh "You can go a little faster, Baby..."
    scene e02s03-a61-2 with dissolve
    mc "It's fine, Lyssa. I want this moment to last forever."
    mh "Mhmm."
    scene e02s03-a61-3 with dissolve
    mc "You're so warm and tight."
    mh "Yes... I love having you inside me."
    mh "Hold onto me."
    play voice3 [lissa_moan7, "<silence 0.7>", lissa_moan2, "<silence 0.7>", lissa_moan3, "<silence 0.7>", lissa_moan4, "<silence 0.4>", lissa_moan5, "<silence 0.5>", lissa_moan8, "<silence 0.5>"]
    play sound4 sfx_vagina_penetration1_fast fadein 1.0
    $ Lovense.pattern("10;14", 900)
    scene e02s03-a61-1-f with dissolve
    mc "I can't get enough of you. Your face, your hair, the color of your eyes."
    mc "The way you feel, how you smell, the taste of your mouth."
    mc "And your amazing little cock."
    scene e02s03-a61-2-f with dissolve
    mh "I would say it is pretty far from little."
    mc "Fair point."
    mh "Hold me. Don't ever let me go."
    scene e02s03-a61-3-f with dissolve
    mh "Ahh."
    mh "Yes! Finish... inside me... I want it all, darling..."
    mc "Ah, I'm close."
    scene e02s03-a61-1-f with dissolve
    mh "Do it, cum, cum inside me."
    $ Lovense.stop()
    $ Lovense.vibrate(18)
    play voice3 lissa_moan9 noloop
    stop sound4 fadeout 1.0
    scene e02s03-61mc-mh-missionary_c1
    play voice2 d1s5_orgasm2 noloop
    with hpunch
    mc "Ah!"
    scene e02s03-66 mc-mh-cum2_c2 with dissolve
    $ Lovense.vibrate(3)
    play voice2 mc_disappointed_ah2 noloop
    mc "Fuck. I made a mess out of you."
    scene e02s03-66 mc-mh-cum2_c3 with dissolve
    play voice3 lissa_moan2 noloop
    mh "You did."
    menu:
        "I think I can make you cum again"(hint="e02s03m01c01"):
            $ e02s03_cum_again = True
            jump e02s03_cum_again
        "That was amazing"(hint="e02s03m01c02"):

            jump e02s03_end

label e02s03_cum_again:

    scene e02s03-a65-1 mc-mh-rimming-anim-01 with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    mh "Woah."
    play sound mc_sex_sucking_slow1 loop
    play voice3 [lissa_moan2, "<silence 0.7>", lissa_moan3, "<silence 0.7>", lissa_moan4, "<silence 0.7>", lissa_moan5, "<silence 0.4>", lissa_moan1, "<silence 0.5>"]
    $ Lovense.vibrate(6)
    scene e02s03-a65-1
    pause
    scene e02s03-a65-2 with dissolve
    play sound mc_sex_sucking_slow1 loop
    play voice2 mc_thinking_mmm1 noloop
    mc "Mmm. Sorry to surprise you..."
    pause
    scene e02s03-a65-3 with dissolve
    mh "It's o-okay... but this is just... oh my god..."
    pause
    scene e02s03-a65-1-f with dissolve
    play voice2 mc_sex_sucking_fast1
    mc "*Hungry licking*"
    pause
    scene e02s03-a65-2-f with dissolve
    play voice3 dahlia_sex_openmoans1
    mh "It feels {b}SO{/b} good. It’s blowing my mind."
    mh "Your tongue is going so keep. You're getting so good at that!"
    scene e02s03-a65-3-f with dissolve
    mh "Ahh. Keep going."
    pause
    play voice3 lissa_moan10 noloop
    stop voice2 fadeout 1.0
    scene e02s03-65 mc-mh-cum1_c4
    with vpunch
    stop sound fadeout 1.0
    mh "Ahhhhhhhh!!!"
    play voice2 d3s8_licking3 noloop
    scene e02s03-68 mc-mh-lick_c2 with dissolve
    pause
    play sound dahlia_kiss_french1
    stop voice2 fadeout 0.5
    scene e02s03-70 mc-mh-kiss_c2 with dissolve
    play voice3 nora_sucking1 noloop
    mh "Now what are you doing, wildman?"
    scene e02s03-70 mc-mh-kiss_c1 with dissolve
    play voice3 nora_pleasure noloop
    pause
    $ Lovense.vibrate(3)
    scene e02s03-70 mc-mh-kiss_c2 with dissolve
    play voice3 lissa_moan2 noloop
    mh "I... I must admit... that was one of the kinkiest things I have done."
    play voice2 mc_thinking_mmm2 noloop
    mc "Mmm... give me time, I'm sure I'll top that."
    mh "I'm looking forward to it."

    jump e02s03_end

label e02s03_end:

    $ renpy.music.set_volume(0.7, 3.0, "music" )
    $ Lovense.vibrate(1)
    scene e02s03-71 mc-mh-sleep1_c2 with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "Sweet dreams, my dear."
    $ unlock_gallery_slot("scene", "e02s03")
    scene e02s03-71 mc-mh-sleep1_c1 with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    mh "Mmm. After that, I'm sure I'll be dreaming of you, my love..."

    $ Lovense.stop()

    $ renpy.end_replay()

    stop music fadeout 3.5
    jump e02s04

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
