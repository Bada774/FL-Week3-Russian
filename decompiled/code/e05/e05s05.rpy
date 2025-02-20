image e05s05-a23-1 = Movie(play = "images/E-05/s05/anim/e05s05-a23-1-2x-50fps.webm", start_image = "e05s05-a23-1 mc-op-mh-sex-anim-01")
image e05s05-a23-1-f = Movie(play = "images/E-05/s05/anim/e05s05-a23-1-2x-60fps.webm", start_image = "e05s05-a23-1 mc-op-mh-sex-anim-01")
image e05s05-a23-2 = Movie(play = "images/E-05/s05/anim/e05s05-a23-2-2x-50fps.webm", start_image = "e05s05-a23-2 mc-op-mh-sex-anim-01")
image e05s05-a23-2-f = Movie(play = "images/E-05/s05/anim/e05s05-a23-2-2x-60fps.webm", start_image = "e05s05-a23-2 mc-op-mh-sex-anim-01")
image e05s05-a23-3 = Movie(play = "images/E-05/s05/anim/e05s05-a23-3-2x-50fps.webm", start_image = "e05s05-a23-3 mc-op-mh-sex-anim-01")
image e05s05-a23-3-f = Movie(play = "images/E-05/s05/anim/e05s05-a23-3-2x-60fps.webm", start_image = "e05s05-a23-3 mc-op-mh-sex-anim-01")

image e05s05-a26-1 = Movie(play = "images/E-05/s05/anim/e05s05-a26-1-2x-50fps.webm", start_image = "e05s05-a26-1 mc-op-mh-anim-01")
image e05s05-a26-1-f = Movie(play = "images/E-05/s05/anim/e05s05-a26-1-2x-60fps.webm", start_image = "e05s05-a26-1 mc-op-mh-anim-01")
image e05s05-a26-2 = Movie(play = "images/E-05/s05/anim/e05s05-a26-2-2x-50fps.webm", start_image = "e05s05-a26-2 mc-op-mh-anim-01")
image e05s05-a26-2-f = Movie(play = "images/E-05/s05/anim/e05s05-a26-2-2x-60fps.webm", start_image = "e05s05-a26-2 mc-op-mh-anim-01")
image e05s05-a26-3 = Movie(play = "images/E-05/s05/anim/e05s05-a26-3-2x-50fps.webm", start_image = "e05s05-a26-3 mc-op-mh-anim-01")
image e05s05-a26-3-f = Movie(play = "images/E-05/s05/anim/e05s05-a26-3-2x-60fps.webm", start_image = "e05s05-a26-3 mc-op-mh-anim-01")

image e05s05-a30-1 = Movie(play = "images/E-05/s05/anim/e05s05-a30-1-2x-50fps.webm", start_image = "e05s05-a30-1 mc-op-mh-anim-01")
image e05s05-a30-1-f = Movie(play = "images/E-05/s05/anim/e05s05-a30-1-2x-60fps.webm", start_image = "e05s05-a30-1 mc-op-mh-anim-01")
image e05s05-a30-2 = Movie(play = "images/E-05/s05/anim/e05s05-a30-2-2x-50fps.webm", start_image = "e05s05-a30-2 mc-op-mh-anim-01")
image e05s05-a30-2-f = Movie(play = "images/E-05/s05/anim/e05s05-a30-2-2x-60fps.webm", start_image = "e05s05-a30-2 mc-op-mh-anim-01")
image e05s05-a30-3 = Movie(play = "images/E-05/s05/anim/e05s05-a30-3-2x-50fps.webm", start_image = "e05s05-a30-3 mc-op-mh-anim-01")
image e05s05-a30-3-f = Movie(play = "images/E-05/s05/anim/e05s05-a30-3-2x-60fps.webm", start_image = "e05s05-a30-3 mc-op-mh-anim-01")

image e05s05-a34-1 = Movie(play = "images/E-05/s05/anim/e05s05-a34-1-2x-50fps.webm", start_image = "e05s05-a34-1 mc-op-mh-anim-01")
image e05s05-a34-1-f = Movie(play = "images/E-05/s05/anim/e05s05-a34-1-2x-60fps.webm", start_image = "e05s05-a34-1 mc-op-mh-anim-01")
image e05s05-a34-2 = Movie(play = "images/E-05/s05/anim/e05s05-a34-2-2x-50fps.webm", start_image = "e05s05-a34-2 mc-op-mh-anim-01")
image e05s05-a34-2-f = Movie(play = "images/E-05/s05/anim/e05s05-a34-2-2x-60fps.webm", start_image = "e05s05-a34-2 mc-op-mh-anim-01")
image e05s05-a34-3 = Movie(play = "images/E-05/s05/anim/e05s05-a34-3-2x-50fps.webm", start_image = "e05s05-a34-3 mc-op-mh-anim-01")
image e05s05-a34-3-f = Movie(play = "images/E-05/s05/anim/e05s05-a34-3-2x-60fps.webm", start_image = "e05s05-a34-3 mc-op-mh-anim-01")

label e05s05:

    scene black
    show screen scene_transistion(_("The next day in the office"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene e05s05-01 mc-op-mh-office1_c3
    with Fade(0.5, 0.5, 0.5)
    $ renpy.music.set_volume(0.6, 0.0, "music")
    $ renpy.music.set_volume(0.0, 0.0, "music2")
    $ renpy.music.play(audio.music_nowhere_tobe, "music" , True, None, True, 1.0)
    $ renpy.music.play(audio.music_nowhere_tobe_reverbed, "music2", True, None, True, 1.0)
    play voice3 dahlia_disappointed_hmm1 noloop
    mh "Have you thought about what you're going to wear?"
    play voice4 oliver_surprised_what4 noloop
    op "Wear for what?"
    mh "Our first day in court."
    scene e05s05-01 mc-op-mh-office1_c2 with dissolve
    play voice4 oliver_thinking_huh5 noloop
    op "I... Haven't even thought about that yet..."
    play voice3 lissa_aga noloop
    mh "You should. A nice suit always leaves a good impression on the jury."
    scene e05s05-03 mc-op-mh-office3_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "'The suit maketh the man.'"
    scene e05s05-03 mc-op-mh-office3_c2 with dissolve
    play voice4 oliver_surprised_what5 noloop
    op "What?"
    play sound sfx_cloth_rustling2
    scene e05s05-04 mc-op-mh-office4_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "You know, 'the suit maketh the man.'{w} You didn't see that movie?"
    play voice4 oliver_no6 noloop
    op "No?..."
    play voice2 mc_thinking_hmm2 noloop
    mc "Well, a good suit is important."
    scene e05s05-04 mc-op-mh-office4_c2 with dissolve
    play voice4 oliver_thinking_eem noloop
    op "I... Don't really own a suit..."
    scene e05s05-04 mc-op-mh-office4_c3 with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop volume 0.7
    mh "Well that simply won't do."
    play sound sfx_cloth_rustling1
    scene e05s05-05 mc-op-mh-office5_c3 with dissolve
    play voice3 nora_hey noloop
    mh "[mcname]."
    scene e05s05-06 mc-op-mh-office6_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Incoming."
    play sound sfx_heels_steps2 loop
    scene e05s05-07 mc-op-mh-office7_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Come on, Ollie."
    play voice3 oliver_thinking_huuh noloop
    op "Where are we going?"
    mc "To get you a suit!"
    scene e05s05-07 mc-op-mh-office7_c2 with dissolve
    play voice4 oliver_angry_oh1 noloop
    op "Wha-wait!"
    stop sound fadeout 1.0
    $ renpy.music.set_volume(1.0, 2.0, "music")
    scene black
    show screen scene_transistion(_("In the Suit Store"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.0, 2.0, "music")
    $ renpy.music.set_volume(1.5, 2.0, "music2")
    scene e05s05-08 mc-op-mh-store1_c1
    with Fade(0.5, 0.5, 0.5)
    play voice2 mc_thinking_mmm7 noloop
    mc "Oooh, nice suit. Jon Philip - London. I have two myself."
    scene e05s05-08 mc-op-mh-store1_c2 with dissolve
    play voice3 oliver_thinking_huh1 noloop
    op "You have two of these?"
    play voice2 mc_no_nah1 noloop
    mc "I wish. Just something I heard once."
    play sound sfx_heels_steps2
    scene e05s05-08 mc-op-mh-store1_c3 with dissolve
    play voice4 boy5_hey_simple noloop
    "Tailor" "Hello, gentleman. Can I be of any help today?"
    stop sound fadeout 1.0
    scene e05s05-09 mc-op-mh-store2_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Yes! Looking for a two piece, two button, single breasted charcoal gray suit. European cut."
    play voice4 boy5_thinking_hmm3 noloop
    "Tailor" "Yes, sir. Right away."
    scene e05s05-09 mc-op-mh-store2_c2 with dissolve
    play voice3 oliver_surprised_why2 noloop
    op "Why do you know so much about suits?"
    play voice2 mc_arrogant_heh1 noloop
    mc "I used to steal Pete's suit magazine when I was bored. Very informative."
    play voice3 oliver_thinking_huh2 noloop
    op "Huh..."
    play sound sfx_cloth_rustling4
    scene e05s05-10 mc-op-mh-store3_c3 with dissolve
    pause
    scene e05s05-09 mc-op-mh-store2_c3 with dissolve
    play voice4 boy5_thinking_huh noloop
    "Tailor" "I had the suit placed in our fitting room."
    play sound sfx_heels_steps1 loop
    scene e05s05-12 mc-op-mh-store5_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Thank you! After you, Mr. Parra."
    play sound2 sfx_heels_steps2
    scene e05s05-12 mc-op-mh-store5_c2 with dissolve
    pause
    scene e05s05-12 mc-op-mh-store5_c3 with dissolve
    pause
    stop sound fadeout 2.0
    stop sound2 fadeout 2.50
    scene e05s05-17-2 mc-op-mh-talk4_c1 with fade
    play voice2 mc_hey_hey7 noloop
    mc "How's it going in there?"
    play voice3 oliver_emm2 noloop
    op "I... I don't know..."
    play voice2 mc_surprised_uh2 noloop
    mc "Why don't you know?"
    play voice3 oliver_ehh1 noloop
    op "I'm just... Not used to seeing myself... Dressed like this."
    play voice2 mc_disappointed_off1 noloop
    mc "Oh, come on. Let's see it, yeah? I bet you look great."
    play sound sfx_door_open3 volume 1.5
    scene e05s05-13 mc-op-mh-walk1_c2 with dissolve
    play sound2 sfx_heels_steps1
    pause
    play voice3 oliver_disappointed_moan3 noloop
    op "So...{w} What do you think?"
    stop sound2 fadeout 1.0
    scene e05s05-14 mc-op-mh-stand1_c1 with dissolve
    play voice2 mc_scared_huuuh3 noloop
    pause
    scene e05s05-14 mc-op-mh-stand1_c2 with dissolve
    play voice3 oliver_surprised_eh noloop
    op "[mcname]?"
    op "Come on, say something. You're making me nervous..."
    scene e05s05-15 mc-op-mh-talk1_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "A man must look his best when he's getting married, or bur- going to stand up in court for the first time as a lawyer."
    scene e05s05-15 mc-op-mh-talk1_c2 with dissolve
    play voice3 oliver_huh5 noloop
    op "You... You think I look good?"
    scene e05s05-16 mc-op-mh-talk2_c1 with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "I think you look {i}fucking great!{/i}"
    scene e05s05-14 mc-op-mh-stand1_c2 with dissolve
    play voice3 oliver_surprised_huh1 noloop
    op "R-really?"
    play sound sfx_cloth_rustling2
    scene e05s05-15 mc-op-mh-talk1_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Really really."
    play sound sfx_hair_scratch1
    scene e05s05-15 mc-op-mh-talk1_c2 with dissolve
    play voice3 oliver_happy_laugh1 noloop
    op "Well, I-... Thanks, [mcname]."
    scene e05s05-16 mc-op-mh-talk2_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course, Ollie. You just need to be confident, like the car ride."
    scene e05s05-16 mc-op-mh-talk2_c2 with dissolve
    play voice3 oliver_happy_relief noloop
    op "That was... Well, that was because of Lyssa."
    scene e05s05-17 mc-op-mh-talk3_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "That guy is still inside of you, Ollie. You can be that confident, strong guy, whenever you want."
    scene e05s05-17 mc-op-mh-talk3_c2 with dissolve
    play voice3 oliver_no_nervous4 noloop
    op "I... I don't think I can..."
    op "Lyssa... I just don't want to disappoint Lyssa."
    play sound sfx_cloth_rustling2
    scene e05s05-18 mc-op-mh-sit1_c1 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "I don't think you could."
    op "I just..."
    scene e05s05-18 mc-op-mh-sit1_c2 with dissolve
    play voice3 oliver_disappointed_geh noloop
    op "I have... Imposter's syndrome. Lyssa is just so... Perfect. Compared to her, I'm..."
    op "I'm not as good as her. I don't think I'll ever be as good as her..."
    op "As a friend, a lawyer... A lover..."
    scene e05s05-19 mc-op-mh-ask1_c1 with dissolve
    play voice2 mc_surprised_wow1 noloop
    mc "Woah, woah. What's this about being a lover?"
    scene e05s05-19 mc-op-mh-ask1_c2 with dissolve
    play voice3 oliver_disappointed_eh noloop
    op "I... {w} Sometimes...{w} Sometimes I think you're only with me because of Lyssa..."
    scene e05s05-19-1 mc-op-mh-look_c1 with dissolve
    play voice2 mc_surprised_what5 noloop
    mc "You... What!?"
    play voice3 oliver_ah2 noloop
    op "I-"
    play voice2 mc_angry_cough1 noloop
    mc "Oliver Parra. Stop."
    scene e05s05-19-1 mc-op-mh-look_c2 with dissolve
    play voice3 oliver_emm1 noloop
    op "But-"
    play voice2 mc_no_no6 noloop
    mc "No, look at me."
    play sound sfx_cloth_rustling4
    scene e05s05-19-2 mc-op-mh-shoulder_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I'm with you, because of you. Not Lyssa, not anything. You. Because of who you are."
    scene e05s05-19-2 mc-op-mh-shoulder_c2 with dissolve
    play voice3 ["<silence 0.5>", oliver_sex_closedmoan1] noloop
    mc "The strong, confident man I know you are. Smart, capable, fun. I love you, {i}for you{/i}, Oliver-"

    jump e05s05_sex

label replay_e05s05:
label e05s05_sex:

    if _in_replay:
        $ renpy.music.set_volume(0.0, 2.0, "music")
        $ renpy.music.set_volume(1.5, 2.0, "music2")
        $ renpy.music.play(audio.music_nowhere_tobe, "music" , True, None, True, 1.0)
        $ renpy.music.play(audio.music_nowhere_tobe_reverbed, "music2", True, None, True, 1.0)
    scene e05s05-19-3 mc-op-mh-kiss_c1 with dissolve
    play voice3 oliver_sex_closedmoan2 noloop
    play voice2 mc_thinking_mmm1 noloop
    play sound maria_kiss2
    pause
    scene e05s05-19-3 mc-op-mh-kiss_c2 with dissolve
    play voice3 oliver_sex_closedmoan3 noloop
    play sound maria_kiss3
    pause
    play sound sfx_cloth_rustling1
    scene e05s05-19-4 mc-op-mh-thigh_c1 with dissolve
    play voice2 mc_surprised_wow4 noloop
    mc "What was that for?"
    scene e05s05-19-4 mc-op-mh-thigh_c2 with dissolve
    play voice2 oliver_disappointed_moan2 noloop
    op "I love you too, [mcname]."
    op "I guess... I just get in my head sometimes and..."
    scene e05s05-19-5 mc-op-mh-thigh2_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "In your defense, we haven't had a lot of me and you time lately. The case has taken up a lot of our free time."
    scene e05s05-19-5 mc-op-mh-thigh2_c2 with dissolve
    play voice2 oliver_arrogant_hmf noloop
    op "Speaking of, did you find that guy?"
    scene e05s05-19-6 mc-op-mh-look_c1 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "I think so. I still need to track him down, but - wait, we're not talking about work right now."
    mc "We're talking about me and you."
    mc "And us time."
    scene e05s05-19-6 mc-op-mh-look_c2 with dissolve
    play voice3 oliver_heh1 noloop volume 1.5
    op "Us?"
    scene e05s05-19-5 mc-op-mh-thigh2_c1 with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "I think the tailor is leaving us alone..."
    scene e05s05-19-4 mc-op-mh-thigh_c2 with dissolve
    play voice3 oliver_surprised_huh2 noloop
    op "[mcname]! This is super public."
    scene e05s05-19-4 mc-op-mh-thigh_c1 with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "It's just like the movie theater, but this time we won't get caught..."
    scene e05s05-19-5 mc-op-mh-thigh2_c2 with dissolve
    play voice3 oliver_oh1 noloop
    op "I mean, when you put it that way..."
    scene e05s05-19-6 mc-op-mh-look_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "After you, Mr. Parra."
    scene e05s05-19-6 mc-op-mh-look_c2 with dissolve
    play voice3 oliver_happy_laugh3 noloop
    op "Why thank you, Mr. Young."
    play sound sfx_door_open3 volume 1.5
    play sound2 sfx_jeans_on1 noloop
    scene e05s05-19-7 mc-op-mh-cloth_c1 with fade
    play voice2 mc_disappointed_ehh5 noloop
    mc "That is a very nice suit, Mr. Para... It would be a shame to ruin it."
    scene e05s05-19-7 mc-op-mh-cloth_c2 with dissolve
    play voice3 oliver_yes_yeah noloop
    op "You've got a good point."
    scene e05s05-20 mc-op-mh-sex1_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "It's a shame you can't wear this suit to court. I think you look quite dashing in it."
    scene e05s05-20 mc-op-mh-sex1_c2 with dissolve
    play voice3 oliver_um1 noloop
    op "My birthday suit?"
    play voice2 d9s2_ugu noloop
    mc "Mmhmmmm."


    $ Lovense.stop()

    scene e05s05-21 mc-op-mh-sex2_c1 with dissolve
    $ Lovense.vibrate(1)
    play voice2 mc_thinking_hmm8 noloop
    mc "You ready to have a little fun?"
    play voice3 oliver_yes_questioning noloop
    op "Always, [mcname]."
    play voice2 mc_arrogant_heh2 noloop
    mc "Good."
    scene e05s05-21 mc-op-mh-sex2_c2 with dissolve
    play voice3 oliver_surprised_what6 noloop
    op "What are you-"
    play voice3 oliver_scared_ah1 noloop volume 2.0
    play sound sfx_fall_mud1 volume 0.4
    play sound2 sfx_epic_kick2 noloop
    play sound3 sfx_leg_kick6 noloop volume 0.4
    scene e05s05-22 mc-op-mh-sex3_c1 with vpunch
    op "-Doing!?"
    play voice2 mc_happy_laugh2 noloop
    mc "Having fun."
    scene e05s05-22 mc-op-mh-sex3_c2 with dissolve
    pause
    $ renpy.music.set_volume(0.8, 2.0, "music")
    $ renpy.music.set_volume(0.0, 5.0, "music2")
    scene e05s05-a23-1 mc-op-mh-sex-anim-01 with dissolve
    pause
    $ Lovense.pattern("7;12", 1400)
    scene e05s05-a23-1
    play voice2 mc_sex_closedmoans1
    play sound mc_sex_sucking_slow2 loop
    play voice3 oliver_angry_oh2 noloop
    queue voice3 oliver_sex_sucking1
    op "Oooohhh, mmmmm."
    pause
    scene e05s05-a23-2 with dissolve
    mc "Glllck, glllck!"
    op "Ouuuach, ouuuuach!!"
    pause
    scene e05s05-a23-3 with dissolve
    op "Mmmphouach! Mmmmphouach!!"
    mc "Nnphcckkk! Nnnnnphckkk!"
    pause
    $ Lovense.pattern("7;12", 700)
    scene e05s05-a23-1-f with dissolve
    op "Ouach, ouach, ouach, ouach!"
    pause
    scene e05s05-a23-2-f with dissolve
    mc "Mmmmmmmm! Glck, glck!"
    pause
    scene e05s05-a23-3-f with dissolve
    op "Ohhhhppphmmmm!!!!"
    pause
    stop voice3 fadeout 1.0
    play sound2 sfx_epic_kick2 noloop
    play sound ["<silence 0.3>", sfx_leg_kick8] volume 0.7
    $ Lovense.stop()
    $ Lovense.vibrate(2)
    scene e05s05-24 mc-op-mh-sex5_c1 with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "Fuck, that was a workout!"
    scene e05s05-24 mc-op-mh-sex5_c2 with dissolve
    play voice3 oliver_surprised_wow4 noloop
    op "I didn't think you were that strong..."
    play sound sfx_cloth_rustling1
    scene e05s05-25 mc-op-mh-sit1_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "There's still a few things you don't know about me, Ollie."
    scene e05s05-25 mc-op-mh-sit1_c2 with dissolve
    play voice3 oliver_thinking_huh4 noloop volume 1.4
    op "Like?"
    scene e05s05-25 mc-op-mh-sit1_c1 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Like, that I'm a giver."
    scene e05s05-a26-1 mc-op-mh-anim-01 with dissolve
    scene e05s05-a26-1
    play voice2 mc_sex_closedmoans1
    play sound mc_sex_sucking_slow2 loop
    play voice3 oliver_scared_ah2 noloop
    queue voice3 oliver_sex_openmoans2
    $ Lovense.pattern("7;10", 1400)
    op "[mcname]!"
    pause
    scene e05s05-a26-2 with dissolve
    op "O-oh my g-goodness!"
    op "This is- this is-"
    mc "Gllllccck, gllllck!"
    pause
    scene e05s05-a26-3 with dissolve
    op "I-I feel your finger against my pr-prostate, and-"
    mc "Glllllcck, gllllck!!"
    pause
    $ Lovense.pattern("7;10", 700)
    scene e05s05-a26-1-f with dissolve
    play voice3 oliver_sex_openmoans3
    op "I don't - mygooodnesss - don't know how long I can last."
    pause
    scene e05s05-a26-2-f with dissolve
    op "Oh yes, yes! Just like that, [mcname]. Oh my, oh my!"
    pause
    scene e05s05-a26-3-f with dissolve
    op "Oh my God, [mcname], I'm going to - I'm going to-!"
    pause
    play sound mc_cum_sound1
    scene e05s05-a26-3 mc-op-mh-anim-01
    $ Lovense.stop()
    $ Lovense.vibrate(14)
    play voice3 oliver_pain_aar2 noloop volume 1.4
    play voice2 mc_angry_errr8 noloop
    with hpunch
    op "Cummm!"
    scene e05s05-27 mc-op-mh-stand_c2 with dissolve
    $ Lovense.vibrate(2)
    play voice3 oliver_angry_breathing noloop
    op "Oh my, [mcname], I- That was-! You're so {i}good at that!{/i}"
    scene e05s05-27 mc-op-mh-stand_c1 with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "Anything for my lover."
    scene e05s05-27 mc-op-mh-stand_c2 with dissolve
    play voice3 oliver_ehh2 noloop volume 1.5
    op "I..."
    op "Come over here and fuck me, [mcname]."
    scene e05s05-28 mc-op-mh-stand2_c1 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "You don't need to ask me twice."
    scene e05s05-28 mc-op-mh-stand2_c2 with dissolve
    pause
    scene e05s05-a30-1 mc-op-mh-anim-01 with dissolve
    pause
    $ Lovense.pattern("7;14", 1400)
    scene e05s05-a30-1
    play sound sfx_vagina_penetration1_fast loop
    play voice3 oliver_sex_openmoans2
    play voice2 mc_sex_openmoans2
    op "Oh, goodness, [mcname] - I always forget how big your dick is."
    pause
    scene e05s05-a30-2 with dissolve
    op "It feeeels sooo good!"
    mc "I feel the same way, counselor!"
    pause
    scene e05s05-a30-3 with dissolve
    op "Good, yes, right there. Mmmm, I can feel your dick pushing so far into meeee. This is- this is a great angle to fuck in!"
    op "Fuh - mmmmm - Fuck me, [mcname]!"
    mc "Ollie, I think I hear - Fuuuuh - I hear the tailor coming back."
    op "Not right-"
    pause
    $ renpy.music.set_volume(0.4, 1.0, "voice2")
    $ renpy.music.set_volume(0.4, 1.0, "voice3")
    $ renpy.music.set_volume(0.4, 1.0, "sound")
    scene e05s05-36 mc-op-mh-door_c3 with dissolve
    play voice5 boy5_surprised_eeh1 noloop
    "Tailor" "Sir, how's everything fitting so far?"
    $ renpy.music.set_volume(1.0, 1.0, "voice2")
    $ renpy.music.set_volume(1.0, 1.0, "voice3")
    $ renpy.music.set_volume(1.0, 1.0, "sound")
    $ Lovense.pattern("7;14", 700)
    scene e05s05-a30-1-f with dissolve
    play voice3 oliver_arrogant_yeah1 noloop
    queue voice3 oliver_sex_openmoans2
    op "G-good! It fits {i}perfectly!{/i}"
    play voice5 boy4_thinking_mmm2_muffled noloop
    "Tailor" "Are you in need of any assistance?"
    play voice3 oliver_pain_aar1 noloop volume 1.5
    queue voice3 oliver_sex_openmoans2
    op "N-no! I think I can manage this on my own!"
    pause
    $ renpy.music.set_volume(0.4, 1.0, "voice2")
    $ renpy.music.set_volume(0.4, 1.0, "voice3")
    $ renpy.music.set_volume(0.4, 1.0, "sound")
    scene e05s05-36 mc-op-mh-door_c3 with dissolve
    play voice5 boy5_thinking_hmm2 noloop
    "Tailor" "And the crotch? When you gave us your measurements, we weren't quite sure how those bottoms would fit you."
    $ renpy.music.set_volume(1.0, 1.0, "voice2")
    $ renpy.music.set_volume(1.0, 1.0, "voice3")
    $ renpy.music.set_volume(1.0, 1.0, "sound")
    scene e05s05-a30-2-f with dissolve
    play voice3 oliver_ohgod noloop
    queue voice3 oliver_sex_openmoans2
    op "Oh believe me, I'm the perfect bottom."
    play voice5 boy5_thinking_hmm1_muffled noloop
    "Tailor" "Sir?"
    op "I, uhm, meant that the crotch fits {i}exactly{/i} and the bottom is {i}terrific{/i}."
    "Tailor" "If you say so, sir..."
    pause
    $ renpy.music.set_volume(0.4, 1.0, "voice2")
    $ renpy.music.set_volume(0.4, 1.0, "voice3")
    $ renpy.music.set_volume(0.4, 1.0, "sound")
    scene e05s05-36 mc-op-mh-door_c3 with dissolve
    play voice5 boy5_yes_yeah noloop
    "Tailor" "If you need anything, I will just be outside. Call if you require me."
    $ renpy.music.set_volume(1.0, 1.0, "voice2")
    $ renpy.music.set_volume(1.0, 1.0, "voice3")
    $ renpy.music.set_volume(1.0, 1.0, "sound")
    scene e05s05-a30-3-f with dissolve
    play voice3 oliver_sex_openmoans3
    op "Oh, oh! I, uhm, I will!"
    pause
    stop sound fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(2)
    scene e05s05-29 mc-op-mh-animation2_c1 with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Think he's actually gone?"
    scene e05s05-32 mc-op-mh-stand4_c2 with dissolve
    play voice3 oliver_angry_ergh1 noloop
    op "Uhm..."
    op "I actually don't care... Just come over here and fuck me until I can't walk straight."
    scene e05s05-32 mc-op-mh-stand4_c1 with dissolve
    play voice2 mc_surprised_ohmy noloop
    mc "My, my. Sweet little Oliver, what has gotten into you?"
    scene e05s05-33 mc-op-mh-stand5_c2 with dissolve
    play voice3 oliver_yes_aga2 noloop
    op "You have. That's what. I understand why Lyssa has to keep that bottle of lube on her desk now."
    scene e05s05-33 mc-op-mh-stand5_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.4
    mc "Love will make you do crazy things."
    play voice3 oliver_yes_unhappy noloop
    op "It will. Like fucking my brains out in this dressing room."
    play voice2 mc_thinking_hm noloop
    mc "Well, when you ask so nicely..."
    scene e05s05-33 mc-op-mh-stand5_c2 with dissolve
    play voice3 oliver_disappointed_off noloop
    op "And, uhm... [mcname]?"
    play voice2 mc_yes_ugu1 noloop
    mc "Uh huh?"
    op "Can you... Pick me up like you did earlier?"
    play sound sfx_cloth_rustling2
    scene e05s05-34 mc-op-mh-animation4_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Absolutely I can."
    scene e05s05-a34-1 mc-op-mh-anim-01 with dissolve
    pause
    $ Lovense.pattern("7;14", 1400)
    scene e05s05-a34-1
    play voice3 oliver_sexphrase_fuck noloop volume 1.5
    queue voice3 oliver_sex_openmoans2
    play voice2 d7s4_mcbreathing
    play sound sfx_vagina_penetration1_fast loop
    op "F-fuck! [mcname], you're so strong!"
    mc "I've been working out a bit."
    pause
    scene e05s05-a34-2 with dissolve
    op "Whatever you've been doing, keep doing it! I want you to fuck me like this {i}every time.{/i}"
    mc "Fuhhh - Ollie, you, you gotta keep it down. The tailor is just outside."
    op "I-I don't care. This is incredible! {i}You{/i} are incredible!"
    pause
    scene e05s05-a34-3 with dissolve
    op "Fuck, I love having every inch of you inside of me!"
    op "Fuck me, [mcname]! Fuck me!"
    pause
    $ Lovense.pattern("7;14", 700)
    scene e05s05-a34-1-f with dissolve
    play voice2 mc_sex_openmoans3
    play voice3 oliver_sex_openmoans3
    mc "Jeesus, Ollie! We have really turned you into a little slut, haven't we?"
    op "N-no! You just made me confident."
    pause
    scene e05s05-a34-2-f with dissolve
    op "I know, fuhck - fuhck! I know what I want now!"
    op "I want you. And Lyssa. Always."
    op "I love you."
    pause
    scene e05s05-a34-3-f with dissolve
    mc "And I love you toooo - fuck, I'm about to cum!"
    op "Yes, yes, YES! Cum in me! You're going to make mee-"
    pause
    $ renpy.music.set_volume(0.4, 1.0, "voice2")
    $ renpy.music.set_volume(0.4, 1.0, "voice3")
    $ renpy.music.set_volume(0.4, 1.0, "sound")
    scene e05s05-36 mc-op-mh-door_c3 with dissolve
    play voice5 boy4_angry_cough3 noloop
    "Tailor" "Sir, is everything all right in here?"
    play voice3 oliver_angry_kghh noloop
    play voice2 d1s5_orgasm2 noloop
    $ renpy.music.set_volume(1.0, 0.5, "voice2")
    $ renpy.music.set_volume(1.0, 0.5, "voice3")
    $ renpy.music.set_volume(1.0, 0.5, "sound")
    stop sound fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(18)
    scene e05s05-35 mc-op-mh-chin_c1 with vpunch
    pause
    play voice5 boy4_thinking_mmm2_muffled noloop
    "Tailor" "Sir? Are you still in there?"
    $ renpy.music.set_volume(0.0, 5.0, "music")
    $ renpy.music.set_volume(1.5, 5.0, "music2")
    scene e05s05-36 mc-op-mh-door_c1 with dissolve
    $ Lovense.vibrate(1)
    play voice3 oliver_angry_breathing noloop
    op "Uh huh... I'm... {i}Great{/i}..."
    scene e05s05-36 mc-op-mh-door_c3 with dissolve
    play voice5 boy5_arrogant_huh noloop
    "Tailor" "You've... Taken a long time in there, sir. Are you sure you're all right?"
    scene e05s05-36 mc-op-mh-door_c1 with dissolve
    play voice3 oliver_yep1 noloop
    op "Yep... Just wanted to make sure it was the {i}perfect fit{/i}."
    op "We'll take it."
    scene e05s05-36 mc-op-mh-door_c2 with dissolve
    play voice5 boy5_surprised_oh1_muffled noloop
    "Tailor" "Of course, sir. Well... Bring it up to the front when you're ready."
    play voice3 oliver_yes_okay4 noloop
    op "We'll be right there."
    scene e05s05-38 mc-op-mh-end2_c1 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "I think he's gone."
    mc "See? Just like the movie theater, but without getting caught."
    scene e05s05-38 mc-op-mh-end2_c2 with dissolve
    play voice3 oliver_happy_relief noloop
    op "It was perfect. But I think we should go, before the tailor gets any more suspicious."
    $ unlock_gallery_slot("scene", "e05s05")
    play voice3 oliver_scared_oof1 noloop
    play sound sfx_fall_mud1
    play sound2 sfx_leg_kick6 noloop
    scene e05s05-37 mc-op-mh-end1_c2 with hpunch
    op "Oh goodness!"
    scene e05s05-37 mc-op-mh-end1_c1 with dissolve
    play voice3 oliver_huh6 noloop
    op "Seems, uhm... I can't walk straight."
    play voice2 mc_surprised_uh1 noloop
    mc "Isn't that what you told me to do? Fuck you until you couldn't walk straight?"
    op "I did say something like that, didn't I."
    play sound sfx_cloth_rustling1
    scene e05s05-38 mc-op-mh-end2_c2 with dissolve
    play voice3 oliver_disappointed_moan3 noloop
    op "Well, seeing as I'm... Incapacitated, mind helping me get dressed and checked out?"
    scene e05s05-38 mc-op-mh-end2_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Anything for my lover."
    stop music fadeout 3.0
    stop music2 fadeout 3.0

    $ Lovense.stop()


    $ renpy.end_replay()

    jump e05s06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
