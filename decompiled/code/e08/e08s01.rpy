image e08s01-a110-1 = Movie(play = "images/E-08/s01/anim/e08s01-a110-1-2x-50fps.webm", start_image = "e08s01-a110-1 amr-mc-sex-sit-in-lap-01")
image e08s01-a110-1-f = Movie(play = "images/E-08/s01/anim/e08s01-a110-1-2x-60fps.webm", start_image = "e08s01-a110-1 amr-mc-sex-sit-in-lap-01")
image e08s01-a110-2 = Movie(play = "images/E-08/s01/anim/e08s01-a110-2-2x-50fps.webm", start_image = "e08s01-a110-2 amr-mc-sex-sit-in-lap-01")
image e08s01-a110-2-f = Movie(play = "images/E-08/s01/anim/e08s01-a110-2-2x-60fps.webm", start_image = "e08s01-a110-2 amr-mc-sex-sit-in-lap-01")
image e08s01-a110-3 = Movie(play = "images/E-08/s01/anim/e08s01-a110-3-2x-50fps.webm", start_image = "e08s01-a110-3 amr-mc-sex-sit-in-lap-01")
image e08s01-a110-3-f = Movie(play = "images/E-08/s01/anim/e08s01-a110-3-2x-60fps.webm", start_image = "e08s01-a110-3 amr-mc-sex-sit-in-lap-01")

image e08s01-a112-1 = Movie(play = "images/E-08/s01/anim/e08s01-a112-1-2x-50fps.webm", start_image = "e08s01-a112-1 arj-mc-sex-two-position-01")
image e08s01-a112-1-f = Movie(play = "images/E-08/s01/anim/e08s01-a112-1-2x-60fps.webm", start_image = "e08s01-a112-1 arj-mc-sex-two-position-01")
image e08s01-a112-2 = Movie(play = "images/E-08/s01/anim/e08s01-a112-2-2x-50fps.webm", start_image = "e08s01-a112-2 arj-mc-sex-two-position-01")
image e08s01-a112-2-f = Movie(play = "images/E-08/s01/anim/e08s01-a112-2-2x-60fps.webm", start_image = "e08s01-a112-2 arj-mc-sex-two-position-01")
image e08s01-a112-3 = Movie(play = "images/E-08/s01/anim/e08s01-a112-3-2x-50fps.webm", start_image = "e08s01-a112-3 arj-mc-sex-two-position-01")
image e08s01-a112-3-f = Movie(play = "images/E-08/s01/anim/e08s01-a112-3-2x-60fps.webm", start_image = "e08s01-a112-3 arj-mc-sex-two-position-01")

image e08s01-a114-1 = Movie(play = "images/E-08/s01/anim/e08s01-a114-1-2x-50fps.webm", start_image = "e08s01-a114-1 arj-mc-sex-three-position-01")
image e08s01-a114-1-f = Movie(play = "images/E-08/s01/anim/e08s01-a114-1-2x-60fps.webm", start_image = "e08s01-a114-1 arj-mc-sex-three-position-01")
image e08s01-a114-2 = Movie(play = "images/E-08/s01/anim/e08s01-a114-2-2x-50fps.webm", start_image = "e08s01-a114-2 arj-mc-sex-three-position-01")
image e08s01-a114-2-f = Movie(play = "images/E-08/s01/anim/e08s01-a114-2-2x-60fps.webm", start_image = "e08s01-a114-2 arj-mc-sex-three-position-01")
image e08s01-a114-3 = Movie(play = "images/E-08/s01/anim/e08s01-a114-3-2x-50fps.webm", start_image = "e08s01-a114-3 arj-mc-sex-three-position-01")
image e08s01-a114-3-f = Movie(play = "images/E-08/s01/anim/e08s01-a114-3-2x-60fps.webm", start_image = "e08s01-a114-3 arj-mc-sex-three-position-01")

image d08s01-a85-glambot-1 = Movie(play = "images/E-08/s01/anim/e8s01-a85-2x-50fps.webm", start_image = "e8s01-a85 amr-mc-rmy-cooking-talk-glambot-85-00_i", image = "e8s01-a85 amr-mc-rmy-cooking-talk-glambot-85-89_i", loop = False)

image d08s01-tv-sex-anim = Movie(play = "images/E-08/s01/anim/b01c06ss07-64-03-2x-50fps.webm", start_image = "b01c06ss07-64-03 mc-fucks-ffl-balls-deep-anim-64-03-01_i")

label e08_menu_jump:

    stop music fadeout 2.0
    call start_ending_from_menu from _call_start_ending_from_menu_1
    $ mcname = persistent.mcname
    $ mclogin = persistent.mclogin
    $ cage_ntr = persistent.cage_ntr
    $ d20s04_pass_exam = persistent.pass_exam
    $ d20s08_copy_files = persistent.copy_files
    $ stop_all_sound()
    call hide_fl_points_overlay from _call_hide_fl_points_overlay_13
    if persistent.finished_e08 is True:
        $ date_sy = False
        call screen e08_char_choice
    elif True:
        $ date_sy = persistent.date_sy

    jump e08s01

label e08s01:

    call hide_fl_points_overlay from _call_hide_fl_points_overlay_7
    scene black
    show screen scene_transistion(_("Ending #8\nMy Happy Ginger Family"))
    with Fade(0.9, 0.9, 0.9)
    pause
    hide screen scene_transistion
    scene black
    show screen scene_transistion(_("One year later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.5, 3.0, "sound2")
    $ renpy.music.set_volume(0.6, 3.0, "music")
    $ renpy.music.set_volume(1.0, 0.0, "sound")
    scene e8s01-01 establishing-shot-sign-for-farm
    play sound2 park fadein 5.0
    play music music_casual_farmingsim fadein 10.0
    with Fade(0.5, 0.5, 0.5)
    pause
    play sound sfx_handwork_shovel1 fadein 2.0
    scene e8s01-02 amr-establishing-shot with dissolve
    pause
    stop sound fadeout 2.5
    scene e8s01-03 mc-see-flowers with dissolve
    pause
    play sound sfx_handwork_flowerbreak1 volume 0.7
    scene e8s01-04 mc-pick-up-flower with dissolve
    pause
    scene e8s01-06 amr-mc-look-over with dissolve
    pause
    scene e8s01-07 amr-mc-stand-next-to with dissolve
    pause
    scene e8s01-07-02 amr-look-up with dissolve
    pause
    play voice3 amrose_thinking_hmm3 noloop
    $ renpy.music.set_volume(0.4, 10.0, "music")
    scene e8s01-08 amr-mc-stand-up with dissolve
    arj "What's this?"
    scene e8s01-09 amr-mc-give-flower with dissolve
    play voice2 mc_happy_a1 noloop
    mc "It's for you. My flower."
    scene e8s01-10 amr-mc-take-flower with dissolve
    play voice3 amrose_thinking_oh1 noloop
    arj "Aw. That's cute."
    scene e8s01-11 amr-mc-talk-hold-flower with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.8
    mc "Since there's no roses growing around here, this one I named after you."
    play sound sfx_cloth_rustling2
    scene e8s01-12 amr-mc-hug with dissolve
    pause
    scene e8s01-13 amr-mc-talk with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "I have an app on my phone that identifies the names of different flowers and stuff."
    mc "This one is called... don't kill me?"
    play voice3 amrose_arrogant_huh1 noloop
    arj "That's a weird name for a flower."
    play voice2 mc_no_no5 noloop
    mc "No. It's called Lydia."
    scene e8s01-20 amr-mc-talk-alt with dissolve
    play voice3 amrose_surprised_uh3 noloop
    arj "Lydia?"
    play voice2 mc_yes_ugu1 noloop
    mc "Yep."
    arj "Really?"
    scene e8s01-14 amr-mc-talk-alt with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah. I'm not even making that up. In French, it's called a fleur-de-Lydia."
    play voice3 amrose_disappointed_ehh2 noloop
    arj "Well, now I don't want it."
    mc "It's a good thing we don't live in France."
    scene e8s01-19 amr-mc-talk-close-view-alt with dissolve
    play voice3 amrose_happy_laugh1 noloop
    arj "I don't mind Lydia. Where do you think she's at now?"
    play voice2 mc_thinking_mmm5 noloop
    mc "Probably not on a farm, I can tell you that much."
    arj "Hope you don't mind that I'm all dirty."
    scene e8s01-15 amr-mc-talk-alt-2-close with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Of course I don't mind. Compared to the farm, you smell wonderful."
    play voice3 amrose_surprised_wow noloop
    arj "Wow, such a compliment."
    mc "Well, I mean, we switched to using fresh cow dung instead of composting with eggshells."
    scene e8s01-18 amr-mc-talk-amr-view with dissolve
    play voice3 amrose_happy_laugh3 noloop
    arj "It's more organic."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, I know."
    mc "Why is it that the most healthy stuff in nature always ends up smelling the worst?"
    scene e8s01-20 amr-mc-talk-alt with dissolve
    play voice3 amrose_arrogant_huh4 noloop
    arj "What do you mean?"
    play voice2 mc_thinking_hmm4 noloop
    mc "You know, like kale."
    arj "Kale, huh? You just mean lettuce in general, right?"
    scene e8s01-17 amr-mc-talk-3-alt with dissolve
    play voice2 mc_no_nono1 noloop
    mc "I meant health foods. Anything green."
    play voice3 amrose_thinking_hmm2 noloop
    arj "Well, it's mostly about preparation, isn't it? And what people are used to."
    arj "Some people never tasted raw milk, but for me, it tastes better coming straight from the source, than the supermarket sourced stuff."
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah. I guess I never did grow out of my habits. I'm still used to that MegaBucks coffee."
    scene e8s01-21 amr-mc-talk-alt-2 with dissolve
    play voice3 amrose_arrogant_hmm1 noloop
    arj "Well, you're just proving my point. Nora's coffee wasn't just off the shelf stuff. It's artisanal."
    arj "Anything can taste weird if you don't prepare it. And it's always nice to try new things as well."
    play voice2 mc_yes_yes1 noloop
    mc "I know. I never knew I would get used to this stuff."
    arj "It was a new beginning for both of us."
    scene e8s01-16 amr-mc-talk-2-close-alt with dissolve
    play voice2 d1s5_mchappy noloop volume 1.8
    mc "The only issue I have with it is that left in the barn, it could lead to an explosion."
    play voice3 amrose_surprised_huh3 noloop
    arj "Explosion?"
    mc "Yeah, if left in the barn, the nitrogen builds up and then the chemicals mix and match and it explodes."
    scene e8s01-22 amr-mc-far-view-talk with dissolve
    play voice3 amrose_arrogant_huh2 noloop
    arj "How would you know that?"
    play voice2 mc_thinking_hmm5 noloop
    mc "Basic chemistry."
    mc "You know, the number one leading cause of deaths on a farm is caused by random barn explosions."
    scene e8s01-24 amr-mc-far-view-talk-alt-2 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "That's why people don't compost."
    play voice3 amrose_no_nah noloop
    arj "I doubt it. How does a barn randomly explode?"
    mc "I don't know, that's why it's random."
    scene e8s01-23 amr-mc-far-view-talk-alt with dissolve
    play voice3 amrose_arrogant_pff noloop
    arj "Sure. Random."
    play voice2 mc_hey_hey3 noloop
    mc "I'm serious. There's a reason why people use feces for fuel."
    arj "What, so we need to be careful around poop?"
    scene e8s01-25 amr-mc-far-view-talk-alt-3 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "How we store it, yes."
    mc "Hey, I'm not as big of a dummy as you think I am."
    mc "I mean, sure, I'm not a hotshot engineer like you, but a business degree has its uses."
    scene e8s01-26 amr-mc-talk-upset with dissolve
    play voice3 amrose_arrogant_huh3 noloop
    arj "Engineering is an applied science, whereas business is not."
    arj "I don't think we need to advertise much for this job, anyway. The people come to us, not us to them."
    scene e8s01-27 amr-mc-talk-upset-alt with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "You're living in the past. Stuck in the mud. Embrace the electronic age, baby."
    mc "We should host some sort of farmer's market and get the word out, so people buy from us directly."
    scene e8s01-30 amr-mc-cf-notice-coming with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Speaking of which, farmers."
    play voice3 amrose_old_psst2 noloop
    arj "*Whispers* Plus I don't think you're a dummy. I picked you after all, didn't I?"
    mc "You made the right decision."
    play sound sfx_footsteps_grass1 fadein 3.0
    scene e8s01-31 amr-mc-cf-leave-barn with dissolve
    play voice4 boy5_thinking_hmm1 noloop volume 0.7
    pause
    stop sound fadeout 1.5
    scene e8s01-31-02 mc-amr-cf-wave-meet-up with dissolve
    play voice5 claudie_hey_happy2 noloop
    ac "Morning."
    scene e8s01-32 amr-mc-cf-group-talk-c4 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Hello, Mr. and Mrs. Cooper."
    scene e8s01-37 amr-mc-cf-group-talk-pov-c1-alt with dissolve
    play voice5 claudie_arrogant_ha1 noloop
    ac "Mrs. Cooper? That makes me sound so old. I would use your last name if I knew what it was."
    play voice2 mc_thinking_mmm4 noloop
    mc "Young."
    ac "That you are."
    scene e8s01-36 amr-mc-cf-group-talk-pov-c2-alt with dissolve
    play voice4 boy5_surprised_eeh1 noloop
    fc "How are things on the ginger farm?"
    play voice3 amrose_disappointed_oh3 noloop
    arj "Oh, the usual."
    scene e8s01-34 amr-mc-cf-group-talk-closer-c2 with dissolve
    play voice5 claudie_happy_mmm1 noloop
    ac "I like your hat."
    play voice3 amrose_happy_laugh2 noloop
    arj "[mcname] named it after me."
    scene e8s01-33 amr-mc-cf-group-talk-c3 with dissolve
    play voice5 claudie_disappointed_eeh noloop
    ac "That's romantic. Frank never does any of that for me."
    play voice4 boy5_hey_calm noloop
    fc "You never asked."
    fc "Really. She never asked."
    play voice5 claudie_arrogant_pff noloop
    ac "See what I live with?"
    scene e8s01-36 amr-mc-cf-group-talk-pov-c2-alt with dissolve
    play voice3 amrose_old_haha2 noloop volume 2.0
    arj "Did you folks need anything? Can I get you something to drink?"
    play voice4 boy5_no_high noloop
    fc "We won't be staying too long. I came over to ask if you had any more of that wire fencing."
    fc "The usual guy I get it from is at some auction, and I want to finish setting this up before the Vinovella versus Minerva Bay game."
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Is that tomorrow?"
    play voice4 boy5_yes_yeah noloop
    fc "Yeah. Don't you read the newspaper?"
    mc "Not much."
    fc "I'm making cheese curds."
    play voice5 claudie_happy_mmm2 noloop
    ac "Homemade cheese curds."
    scene e8s01-38 amr-mc-cf-group-talk-c2-question with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Do we have any more wire?"
    scene e8s01-35 amr-mc-cf-group-talk-pov-c2 with dissolve
    play voice3 amrose_yes_yap noloop
    arj "I think so."
    scene e8s01-40 amr-mc-cf-lets-go-barn with dissolve
    play voice3 amrose_old_hey1 noloop
    arj "Come with me, Frank."
    play sound sfx_footsteps_grass1 fadein 1.5
    scene e8s01-41 amr-mc-cf-head-barn with dissolve
    stop sound fadeout 3.5
    pause
    scene e8s01-50 mc-cf-fence-talk with dissolve
    play voice5 claudie_thinking_hmm2 noloop
    ac "So, what's a handsome, strapping fellow like you working on a farm like this?"
    scene e8s01-51 mc-cf-fence-talk-alt with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "You know me. Homegrown and ready for work."
    scene e8s01-52 mc-cf-fence-talk-alt-c2 with dissolve
    play voice5 claudie_arrogant_hm noloop
    ac "A young man like you ought to come over and do some work for me."
    ac "Maybe we can spend some time together."
    play sound sfx_cloth_rustling4
    scene e8s01-53 mc-cf-fence-talk-hand-over-hand with dissolve
    pause
    scene e8s01-54 mc-cf-fence-talk-smirk-response with dissolve
    play voice2 mc_happy_a1 noloop
    mc "If I wasn't naive, Mrs. Cooper, I would think you're hitting on me."
    scene e8s01-55 mc-cf-fence-talk-flirt with dissolve
    play voice5 claudie_thinking_oh noloop
    ac "Is that what I was doing?"
    ac "I was just talking."
    scene e8s01-54 mc-cf-fence-talk-smirk-response with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "So was I."
    scene e8s01-56 mc-cf-fence-hand-seed-packet with dissolve
    play voice5 claudie_thinking_hmm4 noloop
    ac "Give this to AmRose for me."
    scene e8s01-57 mc-cf-fence-look-at-seed-packet with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "What is it?"
    play voice5 claudie_arrogant_ha2 noloop
    ac "What does it look like?"
    scene e8s01-58 mc-cf-fence-sarcastic with dissolve
    play voice2 mc_no_no1 noloop
    mc "No, I mean, which seeds are they?"
    play voice5 claudie_hey_happy1 noloop
    ac "It's a surprise! You'll have to wait until they grow out to see what they are."
    scene e8s01-59 mc-cf-fence-talk-excited with dissolve
    play voice5 claudie_happy_laugh3 noloop
    ac "For all you know, they're magic seeds that can grow money trees."
    ac "Or they're just the regular money trees from China."
    play voice2 mc_arrogant_huh3 noloop
    mc "Sounds like a real gamble, but I think I might know which one it is."
    play sound sfx_door_slide2 volume 1.6
    scene e8s01-60 mc-amr-cf-leave-barn with dissolve
    play voice4 boy5_yes_yep noloop
    fc "I'll be heading off. Let's go."
    scene e8s01-61 mc-amr-cf-talk-walk with dissolve
    play voice4 boy5_hey_seeya noloop
    fc "Good seeing you guys. Say hi to the little lady for me. Where is she, anyway?"
    play voice2 mc_thinking_hmm2 noloop
    mc "Sleeping in the house."
    fc "I'll be sure to bring a treat for her next time I come over."
    play sound sfx_footsteps_grass1 fadein 3.0
    scene e8s01-62 mc-amr-cf-goodbye with dissolve
    stop sound fadeout 6.0
    play voice5 claudie_happy_laugh1 noloop
    ac "Well, you know where to find me."
    ac "Bye, AmRose."
    play voice3 amrose_yes_yeah2 noloop
    arj "See you later."
    scene e8s01-63 mc-amr-talk-teasing with dissolve
    play voice3 amrose_surprised_huh2 noloop
    arj "So what'd you guys talk about?"
    play voice2 mc_disappointed_ah2 noloop
    mc "Oh, she was teasing me as usual."
    arj "Teasing you?"
    scene e8s01-64 mc-amr-talk-response with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "You know. Mindless flirting, or least that's what I think it was."
    play voice3 amrose_thinking_hmm4 noloop
    arj "Do you find her attractive?"
    play voice2 d9s2_yeah noloop volume 2.2
    mc "Well, yeah."
    scene e8s01-68 mc-amr-talk-alt-over-shoulder with dissolve
    play voice3 amrose_arrogant_yeah1 noloop
    arj "So do I."
    play voice2 mc_angry_hm1 noloop
    mc "You say that with everyone."
    arj "Not everyone."
    scene e8s01-65 mc-amr-talk-wide-shot with dissolve
    play voice3 amrose_angry_ergh noloop
    arj "It's not my fault people around here are so attractive."
    arj "The old stereotype about rednecks isn't true. If only Hollywood came down here and saw people, they would move their production offices here."
    scene e8s01-67 mc-amr-talk-alt-shot with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "So I'm guessing Frank hit on you as well?"
    play voice3 amrose_no_simple3 noloop
    arj "No. We talked about which books we read."
    mc "What were you reading?"
    scene e8s01-66 mc-amr-talk-embarrassed with dissolve
    play voice3 amrose_thinking_hmm1 noloop
    arj "I recommended we both read Their Eyes Were Watching God."
    play voice2 mc_surprised_what1 noloop
    mc "What's that? Some religious book?"
    play voice3 amrose_no_simple2 noloop
    arj "No. It's about the life of a young black woman in the American South during the Civil War. Mostly about her life on the farm."
    arj "You'd like it."
    scene e8s01-69 mc-amr-talk-alt-over-shoulder with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Any exciting scenes?"
    play voice3 amrose_yes_yeah3 noloop
    arj "There's a lot of sex building, and lots of sexual tension throughout."
    arj "And a scene where there's a hurricane, though I'm not sure how realistic it is. The cows end up flying around."
    play voice2 mc_yes_okay2 noloop
    mc "I'll read it after you're done."
    scene e8s01-70 mc-amr-talk-alt-wideshot with dissolve
    play voice3 amrose_happy_phew2 noloop
    arj "When we were in college, I'd practically force you to read these books, and now you're doing it out of free will."
    play voice2 mc_no_nah2 noloop
    mc "I was never opposed to reading books, I just didn't have time to do it."
    mc "Now all we have is time."
    play sound sfx_cloth_rustling4
    scene e8s01-71 mc-amr-talk-close-together with dissolve
    play voice3 amrose_yes_ugu noloop
    arj "You're right."
    arj "You ever stop and wonder about the things we have now?"
    scene e8s01-72 mc-amr-talk-close-together-mc-response with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "All the time. Farm life is slow and dull, and it leaves for a lot of thinking to do."
    play voice3 amrose_thinking_hmm5 noloop
    arj "Did you mean it before, what you said? That you made the right decision?"
    mc "I do. I have no regrets being with you. I'm so glad I'm here with you now, here and forever."
    scene e8s01-73 mc-amr-talk-hug-i-love-you with dissolve
    play voice2 d1s5b_ehhh noloop
    mc "I love you."
    play voice3 amrose_angry_breath1 noloop
    arj "I love you too."
    scene e8s01-74 mc-amr-talk-finish-up with dissolve
    play voice3 amrose_yes_okay2 noloop
    arj "Let's finish up our work here and eat something."
    arj "I'm pooped."
    play voice2 mc_surprised_huh6 noloop
    mc "Hungry?"
    arj "A bit. We should feed our girl too."
    stop sound2 fadeout 2.5
    play sound sfx_door_closed2
    scene e8s01-75 amr-mc-rmy-enter-house with dissolve
    pause
    scene e8s01-76 amr-mc-rmy-change-clothes-table with dissolve
    play voice3 amrose_old_psst noloop volume 1.5
    arj "Remy's still sleeping."
    play sound sfx_cloth_dress_off1 volume 2.5
    scene e8s01-77 amr-rmy-put-hat-table with dissolve
    pause
    scene e8s01-78 amr-rmy-walk-back-naked with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "You want what we made yesterday? Still have some leftovers."
    play voice3 amrose_yes_yeah1 noloop
    arj "Alright."
    play sound sfx_cloth_dress_off3 volume 1.5
    scene e8s01-79 amr-rmy-hold-each-other with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "That reminds me, I need to go back out into the barn after lunch."
    play voice3 amrose_arrogant_huh3 noloop
    arj "What for?"
    scene e8s01-80 amr-rmy-hold-each-other-close-up with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Need to clean out the troughs. Forgot to do that."
    play voice3 amrose_disappointed_oh4 noloop
    arj "I thought you did that yesterday."
    mc "I did too. All shit out of luck."
    play sound sfx_hair_scratch1
    scene e8s01-81 amr-rmy-pat-remy with dissolve
    pause
    play voice3 amrose_happy_mmm noloop
    play sound dog_breath1 noloop
    scene e8s01-82 amr-rmy-hug-remy with dissolve
    stop sound fadeout 3.0
    pause
    scene e8s01-83 amr-rmy-leave-to-change with dissolve
    pause

    jump e08s01_arj_back

label e08s01_arj_back:

    $ renpy.music.set_volume(0.35, 0.0, "sound3")
    play sound3 sfx_dishes_fryingpan1 fadein 3.0
    scene e8s01-84 amr-rmy-come-back with Fade(0.4, 0.4, 0.4)
    play sound dog_moan2 fadein 1.0
    pause
    scene e8s01-85 amr-mc-rmy-cooking-talk with dissolve
    play voice3 stacy_smell noloop
    pause
    play sound sfx_camera_fly1
    scene d08s01-a85-glambot-1 with dissolve
    pause
    play voice3 amrose_thinking_emm noloop
    arj "Do you need any help?"
    scene e8s01-86 amr-mc-talk-alt-cooking with dissolve
    play voice2 mc_no_nope2 noloop
    mc "I am good."
    mc "I have a project in my mind. I'm thinking of expanding the barn a little more."
    scene e8s01-87 amr-mc-remy-talk-alt- with dissolve
    play voice3 amrose_surprised_oh4 noloop
    arj "Expanding the barn?"
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, you know, for the wintertime, so that we can store things a bit better there instead of leaving things out on the ground, on the snow."
    arj "Might be a bit difficult."
    scene e8s01-88 amr-mc-remy-talk-mc-pov with dissolve
    play voice2 mc_yes_yeah6 noloop
    mc "Yeah, I know. I'm taking my time with it."
    scene e8s01-89 amr-talk-close-up with dissolve
    play voice3 amrose_arrogant_huh1 noloop
    arj "Winter's just on the horizon."
    scene e8s01-88 amr-mc-remy-talk-mc-pov with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "I know. I noticed once the problems start, they never stop. They just keep piling on."
    mc "I should ask Frank or someone in the community about how to set it up. I know he worked on something like this."
    play sound sfx_coffee_machine volume 2.0
    scene e8s01-90 amr-talk-take-coffee with dissolve
    pause
    stop sound fadeout 1.0
    scene e8s01-91 amr-mc-talk-amr-pov with dissolve
    play voice3 amrose_yes_yeah4 noloop
    arj "Yeah, Frank's a smart guy. Did you know he used to be a musician?"
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Really? I've never seen him with an instrument."
    arj "He's a violinist."
    scene e8s01-92 mc-talk-close-up with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "Wow."
    play voice3 amrose_thinking_hmm2 noloop
    arj "And Ashley plays the cello."
    mc "Really? How do you know this and I don't?"
    scene e8s01-93 mc-talk-wide-shot with dissolve
    play voice3 amrose_old_haha2 noloop volume 1.5
    arj "They told me recently too. They were thinking about putting together a little folk ensemble and playing in public."
    play voice2 mc_thinking_mmm2 noloop
    mc "I'd be real curious to see Ashley on a cello."
    arj "That's a euphemism, I take it."
    scene e8s01-94 mc-talk-alt-mc with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "I mean, it's awesome to learn about something about a person we knew for a year and change. I mean, musicians, that's pretty huge, isn't it?"
    mc "Imagine if I didn't disclose that I went to college, no one would figure it out."
    mc "I mean technically, I didn't finish and get a degree, but I went, right, you never would guess looking at me."
    play voice3 amrose_happy_laugh4 noloop
    $ unlock_gallery_slot("cg", "e08s01")
    scene e8s01-95 amr-talk-alt-amr with dissolve
    arj "Is that a common thing, people thinking you didn't go to college?"
    play voice2 mc_arrogant_huh3 noloop
    mc "Only my parents think that."
    arj "Your parents didn't think you went to college?"
    play sound ["<silence 1.7>", sfx_drink_slurp2]
    scene e8s01-96 amr-mc-talk-drink-wide-shot with dissolve
    play voice2 mc_no_no2 noloop
    mc "No, they don't associate our college with sex, partying, and alcohol. It's more prestigious than that."
    play voice3 amrose_thinking_oh1 noloop
    arj "Oh, I see, so other people never saw you as an... {w}alcohol drinking, sex having, partygoing college student?"
    mc "That's right. All they see is a humble farmer."
    arj "You're ridiculous."
    scene e8s01-98 amr-tv-weather-talk-close-up with dissolve
    play voice3 amrose_old_wow noloop
    arj "Wow, it says on the news that there's a storm coming."
    scene e8s01-97 mc-amr-tv-weather with dissolve
    play voice3 amrose_surprised_oh1 noloop
    arj "I think we both need to go to the barn and board up the windows."
    scene e8s01-99 amr-mc-tv-weather-talk-mc-pov with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "Really?"
    mct "She's right, the mayor gave a speech about weatherproofing and about how we'd get fined if we didn't."
    mct "Just one more problem..."
    stop sound3 fadeout 2.0
    scene e8s01-100 amr-mc-bring-food with dissolve
    pause
    scene e8s01-101 amr-mc-remy-talk-remy with dissolve
    play voice2 mc_disappointed_meh1 noloop
    mc "See what I mean? Things piling up and up. Alright."
    mc "Remy, I need you, come on."
    play sound dog_snoring1 loop fadein 1.6
    scene e8s01-102 amr-mc-remy-scold-remy with dissolve
    pause
    scene e8s01-103 amr-mc-talk-sleep-more-than-me with dissolve
    play voice2 mc_arrogant_pff1 noloop volume 1.5
    mc "I swear, she sleeps more than I do."
    play voice3 amrose_no_uhuh noloop
    arj "That's impossible."
    stop sound fadeout 3.0
label replay_e08s01 hide:
    scene e8s01-104 amr-mc-hand-food with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.6
    mc "Here you go."
    play voice3 amrose_thinking_hmm3 noloop
    arj "Thanks."
    scene e8s01-105 amr-mc-show-seeds with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, before I forget, here."
    play voice3 amrose_arrogant_huh2 noloop
    arj "What's this?"
    mc "Some seeds."
    scene e8s01-106 amr-talk-take-seeds with dissolve
    play voice3 amrose_arrogant_hmm1 noloop
    arj "Which ones?"
    play voice2 d3s11b_mcheh noloop volume 1.6
    mc "Ashley gave me this when you were talking with Frank. Said they were money tree seeds as a joke."
    scene e8s01-107 amr-talk-alt with dissolve
    play voice3 amrose_yes_okay1 noloop
    arj "Alright, I mean, I could plant one in the backyard somewhere."
    play voice2 mc_happy_yay2 noloop
    mc "If we ever have kids, we'll tell them we planted it in their honor."
    arj "That's a nice thought."
    scene e8s01-108 amr-mc-lets-eat with dissolve
    play voice3 amrose_happy_laugh1 noloop
    arj "Let's eat before the food gets cold."
    play voice2 mc_thinking_hmm5 noloop
    mc "Want to watch something? A show maybe?"
    play voice3 amrose_yes_yeah3 noloop
    arj "Yeah. Not anything to do with farms, please."
    play sound sfx_tv_porn1 fadein 2.5
    scene black
    show d08s01-tv-sex-anim:
        zoom 0.265
        xanchor 0.5
        yanchor 0.5
        xalign 0.162
        yalign -0.13
        rotate 7
    show e8s01-109 amr-mc-tv-timepass
    with dissolve
    pause
    stop music fadeout 3.5
    stop sound fadeout 3.0
    scene black
    show screen scene_transistion(_("After watching tv for some time"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene e8s01-110-02 amr-mc-lean-in
    with Fade(0.5, 0.5, 0.9)
    $ renpy.music.set_volume(1.0, 10.0, "music")
    queue music music_new_grass
    play voice3 amrose_angry_breath2 noloop
    arj "You just got me in the mood."
    play sound maria_kiss1
    play voice3 amrose_old_upset noloop volume 1.6
    play voice2 mc_thinking_mmm1 noloop
    scene e8s01-110-03 amr-mc-kiss with dissolve
    pause
    play sound sfx_cloth_rustling1

    $ Lovense.stop()

    $ Lovense.vibrate(1)
    scene e8s01-110-04 amr-mc-sex-sit-in-lap with dissolve
    play voice3 amrose_disappointed_ehh2 noloop
    arj "When's the last time we really took the time to do this?"
    play voice2 mc_angry_huh2 noloop
    mc "Too long, baby."
    scene e8s01-111 amr-mc-sex-sit-in-lap-talk with dissolve
    play voice3 amrose_angry_ergh noloop
    arj "I can't wait anymore."
    scene e08s01-a110-1 amr-mc-sex-sit-in-lap-01 with dissolve
    pause
    play voice3 daisy_moaning
    play voice2 d7s4_mcbreathing fadein 3.0
    $ Lovense.pattern("5;8", 1700)
    scene e08s01-a110-1
    mc "You like the way that feels?"
    pause
    scene e08s01-a110-2 with dissolve
    pause
    scene e08s01-a110-3 with dissolve
    arj "It feels so good."
    pause
    $ Lovense.pattern("6;9", 900)
    scene e08s01-a110-1-f with dissolve
    arj "Keep going like that."
    pause
    scene e08s01-a110-2-f with dissolve
    pause
    scene e08s01-a110-3-f with dissolve
    arj "Right there."
    stop voice2 fadeout 1.0
    stop voice3 fadeout 1.0
    play sound sfx_cloth_rustling2
    $ Lovense.stop()
    $ Lovense.vibrate(3)
    scene e8s01-112 amr-mc-sex-2-position with dissolve
    pause
    scene e8s01-113 amr-mc-sex-2-position-talk with dissolve
    play voice3 amrose_angry_ehh noloop
    arj "I want you to fuck me hard this time."
    arj "Then I want you to come inside me."
    arj "I'm already yours."
    scene e08s01-a112-1 arj-mc-sex-two-position-01 with dissolve
    pause
    $ Lovense.pattern("6;9", 1700)
    play voice3 amrose_old_moaning
    play voice2 d7s4_mcbreathing
    scene e08s01-a112-1
    pause
    scene e08s01-a112-2 with dissolve
    arj "You make me feel so good, baby."
    pause
    scene e08s01-a112-3 with dissolve
    pause
    play voice3 amrose_old_moaning2
    $ Lovense.pattern("7;12", 900)
    scene e08s01-a112-1-f with dissolve
    pause
    scene e08s01-a112-2-f with dissolve
    arj "Fuck me just like that."
    pause
    scene e08s01-a112-3-f with dissolve
    pause
    $ Lovense.stop()
    $ Lovense.vibrate(5)
    play voice3 amrose_angry_breath2 noloop
    stop voice2 fadeout 1.0
    scene e8s01-116 amr-mc-sex-3-rest with dissolve
    pause
    scene e8s01-117 amr-mc-sex-3-rest-talk with dissolve
    pause
    scene e08s01-a114-1 arj-mc-sex-three-position-01 with dissolve
    pause
    $ Lovense.pattern("8;14", 1700)
    play voice3 amrose_old_orgasming
    play voice2 d7s4_mcbreathing
    scene e08s01-a114-1
    pause
    scene e08s01-a114-2 with dissolve
    pause
    scene e08s01-a114-3 with dissolve
    pause
    $ Lovense.pattern("8;14", 900)
    scene e08s01-a114-1-f with dissolve
    pause
    scene e08s01-a114-2-f with dissolve
    pause
    scene e08s01-a114-3-f with dissolve
    pause
    $ Lovense.pattern("18", 1700)
    play voice2 d1s5_orgasm2 noloop
    play voice3 amrose_sex_orgasm2 noloop
    scene e8s01-114 amr-mc-sex-3-position with vpunch
    arj "Ahhh! I am cumming!"
    play voice2 mc_angry_errr4 noloop
    scene e8s01-115 amr-mc-sex-3-cum with vpunch
    pause
    queue voice3 amrose_sex_orgasm3 noloop
    play sound ["<silence 0.3>", sfx_spitcum1] volume 0.4
    scene e8s01-115-02 amr-mc-sex-3-cum-drip with dissolve
    $ unlock_gallery_slot("scene", "e08s01")
    pause
    stop voice3 fadeout 1.0

    $ Lovense.stop()
    $ renpy.end_replay()

    stop music fadeout 4.5
    jump e08s02

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
