image e14s04-a80-1 = Movie(play = "images/E-14/s04/anim/e14s04-a80-1-2x-50fps.webm", start_image = "e14s04-a80-1 mc-nk-pw-1-anim-01")
image e14s04-a80-1-f = Movie(play = "images/E-14/s04/anim/e14s04-a80-1-2x-60fps.webm", start_image = "e14s04-a80-1 mc-nk-pw-1-anim-01")
image e14s04-a80-2 = Movie(play = "images/E-14/s04/anim/e14s04-a80-2-2x-50fps.webm", start_image = "e14s04-a80-2 mc-nk-pw-1-anim-01")
image e14s04-a80-2-f = Movie(play = "images/E-14/s04/anim/e14s04-a80-2-2x-60fps.webm", start_image = "e14s04-a80-2 mc-nk-pw-1-anim-01")
image e14s04-a85-1 = Movie(play = "images/E-14/s04/anim/e14s04-a85-1-2x-50fps.webm", start_image = "e14s04-a85-1 mc-nk-pw-2-anim-01")
image e14s04-a85-1-f = Movie(play = "images/E-14/s04/anim/e14s04-a85-1-2x-60fps.webm", start_image = "e14s04-a85-1 mc-nk-pw-2-anim-01")
image e14s04-a90-1 = Movie(play = "images/E-14/s04/anim/e14s04-a90-1-2x-50fps.webm", start_image = "e14s04-a90-1 mc-nk-pw-3-anim-01")
image e14s04-a90-1-f = Movie(play = "images/E-14/s04/anim/e14s04-a90-1-2x-60fps.webm", start_image = "e14s04-a90-1 mc-nk-pw-3-anim-01")
image e14s04-a90-2 = Movie(play = "images/E-14/s04/anim/e14s04-a90-2-2x-50fps.webm", start_image = "e14s04-a90-2 mc-nk-pw-3-anim-01")
image e14s04-a90-2-f = Movie(play = "images/E-14/s04/anim/e14s04-a90-2-2x-60fps.webm", start_image = "e14s04-a90-2 mc-nk-pw-3-anim-01")
image e14s04-a95-2 = Movie(play = "images/E-14/s04/anim/e14s04-a95-2-2x-50fps.webm", start_image = "e14s04-a95-2 mc-nk-pw-4-anim-01")
image e14s04-a95-2-f = Movie(play = "images/E-14/s04/anim/e14s04-a95-2-2x-60fps.webm", start_image = "e14s04-a95-2 mc-nk-pw-4-anim-01")
image e14s04-a100-2 = Movie(play = "images/E-14/s04/anim/e14s04-a100-2-2x-50fps.webm", start_image = "e14s04-a100-2 mc-nk-pw-5-anim-00")
image e14s04-a100-2-f = Movie(play = "images/E-14/s04/anim/e14s04-a100-2-2x-60fps.webm", start_image = "e14s04-a100-2 mc-nk-pw-5-anim-00")
image e14s04-a100-3 = Movie(play = "images/E-14/s04/anim/e14s04-a100-3-2x-50fps.webm", start_image = "e14s04-a100-3 mc-nk-pw-5-anim-00")
image e14s04-a100-3-f = Movie(play = "images/E-14/s04/anim/e14s04-a100-3-2x-60fps.webm", start_image = "e14s04-a100-3 mc-nk-pw-5-anim-00")

image e14s04-a61-glam = Movie(play = "images/E-14/s04/anim/e14s04-a61-2x-60fps.webm", start_image = "e14s04-a61 mc-nk-pw-cust4-glambot-61-000", image = "e14s04-a61 mc-nk-pw-cust4-glambot-61-119", loop = False)

label e14s04:

    $ renpy.music.set_volume(0.45, 3.0, "music")
    queue music take_the_ride_calm
    scene e14s04-01 mc-nk-pw-blindfold1_c3 with Fade(0.5, 0.5, 0.9)
    play voice4 aaleyah_surprised_huh2 noloop
    nk "Should I be concerned about just how many different blindfolds you have?"
    scene e14s04-01 mc-nk-pw-blindfold1_c2 with dissolve
    play voice3 polly_laugh3 noloop
    pw "I think we know you like a little thrill now and then."
    scene e14s04-01 mc-nk-pw-blindfold1_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "You can say that again. Let's just make sure we don't scare off the customers."
    scene e14s04-02 mc-nk-pw-blindfold2_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "Our business is finally doing okayl."
    scene e14s04-02 mc-nk-pw-blindfold2_c3 with dissolve
    play voice4 aaleyah_no_nah noloop
    nk "Have no fear, I'll keep you two in check."
    scene e14s04-02 mc-nk-pw-blindfold2_c2 with dissolve
    play voice3 polly_laugh noloop
    pw "Haha. You can certainly try, sweet thang."
    play sound sfx_bandage_on1 volume 2.0
    scene e14s04-03 mc-nk-pw-blindfold3_c2 with dissolve
    play voice3 polly_aga noloop
    pw "There. All set."
    scene e14s04-03 mc-nk-pw-blindfold3_c3 with dissolve
    play voice4 aaleyah_yes_aga4 noloop
    nk "Okay."
    scene e14s04-04 mc-nk-pw-blindfold4_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "All good?"
    scene e14s04-04 mc-nk-pw-blindfold4_c3 with dissolve
    play voice4 aaleyah_yes_yep noloop
    nk "Let the games begin. Take off whatever you want. But slowly."
    scene e14s04-05 mc-nk-pw-undress1_c3 with dissolve
    play voice4 aaleyah_thinking_oh noloop
    nk "Oh, and what's the next drink order?"
    play sound sfx_paper_rustl1
    scene e14s04-06 mc-nk-pw-undress2_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "One piña colada."
    scene e14s04-06 mc-nk-pw-undress2_c3 with dissolve
    play voice4 aaleyah_thinking_hmm1 noloop
    nk "Alright, first step, I need the blender, rum and a measuring glass to start with."
    play sound sfx_glass_bottle_bonk volume 0.5
    scene e14s04-08 mc-nk-pw-drink1_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Got you covered."
    scene e14s04-09 mc-nk-pw-drink2_c3 with dissolve
    pause
    play sound sfx_bottle_pouring1
    scene e14s04-11 mc-nk-pw-make1_c2 with dissolve
    pause
    scene e14s04-11 mc-nk-pw-make1_c3 with dissolve
    play voice2 d1s1_mmm noloop
    mct "Incredible. She poured exactly two ounces."
    play voice4 nora_hmm noloop volume 2.4
    nk "How'd I do?"
    play voice2 mc_yes_yeah1 noloop
    mc "Perfect. You're amazing at this."
    scene e14s04-12 mc-nk-pw-make2_c3 with dissolve
    play voice4 nora_heh noloop
    nk "Just lots of practice, babe."
    play sound sfx_door_slide2 volume 2.0
    scene e14s04-13 mc-nk-pw-make3_c2 with dissolve
    play voice3 polly_hey noloop
    pause
    scene e14s04-18 mc-nk-pw-make8_c2 with dissolve
    pw "I'm Polly. What can I get you two?"
    play sound sfx_blender_mix1
    scene e14s04-13 mc-nk-pw-make3_c3 with dissolve
    play voice4 aaleyah_thinking_hmm2 noloop
    nk "Next we need one ounce of coconut cream and heavy cream. I think I saw them to your right."
    play sound sfx_door_slide6
    scene e14s04-15 mc-nk-pw-make5_c1 with dissolve
    play voice2 mc_yes_okay2 noloop volume 1.8
    mc "We're in business."
    play sound sfx_bottle_pouring1
    scene e14s04-15 mc-nk-pw-make5_c3 with dissolve
    play voice4 aaleyah_yes_yeah3 noloop
    nk "Thank you."
    scene e14s04-16 mc-nk-pw-make6_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Let's knock it up a notch. Heavy cream incoming."
    scene e14s04-16 mc-nk-pw-make6_c3 with dissolve
    play voice4 aaleyah_arrogant_heh noloop
    nk "Bring it."
    play sound sfx_throw_something1
    scene e14s04-17 mc-nk-pw-make7_c1 with hpunch
    play voice2 mc_arrogant_huh2 noloop
    mc "Catch."
    scene e14s04-17 mc-nk-pw-make7_c3 with dissolve
    play voice4 nora_huh noloop
    pause
    play voice4 aaleyah_happy_wooh noloop
    play sound sfx_sex_bodyslaps1_fast
    scene e14s04-18 mc-nk-pw-make8_c3 with hpunch
    stop sound fadeout 1.0
    nk "Woohoo."
    scene e14s04-19 mc-nk-pw-make9_c1 with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "How can you be blindfolded and still know exactly how to seduce me."
    scene e14s04-19 mc-nk-pw-make9_c3 with dissolve
    play voice4 aaleyah_happy_mmm1 noloop
    nk "It's a talent."
    play sound dahlia_kiss_french1
    scene e14s04-20 mc-nk-pw-kiss1_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    pause
    play sound maria_kiss2
    scene e14s04-20 mc-nk-pw-kiss1_c3 with dissolve
    play voice4 aaleyah_closed_moan1 noloop
    pause
    scene e14s04-21 mc-nk-pw-talk1_c3 with dissolve
    play voice4 nora_angrymoan noloop
    nk "But we can't get too distracted now. Last step. I need a can of pineapple juice and four ounces of ice."
    play sound sfx_ice_cubes1
    scene e14s04-22 mc-nk-pw-talk2_c3 with dissolve
    pause
    scene e14s04-25 mc-nk-pw-talk5_c3 with dissolve
    play voice3 polly_huh noloop volume 1.3
    pw "How's it going?"
    scene e14s04-25 mc-nk-pw-talk5_c2 with dissolve
    play voice4 nora_aga noloop
    nk "Just one more minute."
    scene e14s04-27 mc-nk-pw-pine2_c3 with dissolve
    play voice3 polly_laugh2 noloop
    pw "Almost forgot the pineapple slice."
    scene e14s04-28 mc-nk-pw-pine3_c2 with dissolve
    play voice4 aaleyah_no_uhuh noloop
    nk "I did not, I just wanted to get you close."
    scene e14s04-28 mc-nk-pw-pine3_c3 with dissolve
    pw "You're too good for me. Love you."
    scene e14s04-28 mc-nk-pw-pine3_c2 with dissolve
    play sound sfx_blender_mix2
    "*loud whirring*"
    play sound sfx_bottle_pouring1
    scene e14s04-32 mc-nk-pw-drink4_c1 with dissolve
    play voice4 aaleyah_happy_phew noloop
    nk "Voilà."
    scene e14s04-32 mc-nk-pw-drink4_c2 with dissolve
    play voice3 polly_wooh noloop
    pw "You're a real master even with a blindfold on."
    scene e14s04-39 mc-nk-pw-hug2_c1 with dissolve
    play voice2 d9s2_mcyes noloop volume 2.5
    mc "Yes she is."
    play voice3 polly_oh noloop
    pw "Alright. Well keep the blindfold on. That was just the drink I wanted."
    scene e14s04-39 mc-nk-pw-hug2_c2 with dissolve
    play voice4 aaleyah_angry_cagh1 noloop
    nk "Polly..."
    play voice3 polly_angry noloop
    pw "What? I need plenty of nutritious cocktails to keep me going during these work hours."
    scene e14s04-39 mc-nk-pw-hug2_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Nora's right. This isn't the time for messing around and drinking up our inventory."
    play voice4 aaleyah_angry_hm1 noloop
    nk "I'm sure we can punish her later."
    play voice2 mc_arrogant_heh3 noloop
    mc "Alright. Let's see if you can go two for two, gorgeous."
    scene e14s04-42 mc-nk-pw-talk_c2 with dissolve
    pause
    play sound sfx_cloth_rustling2
    scene e14s04-44 mc-nk-pw-undress1_c1 with dissolve
    play voice4 aaleyah_closed_moan2 noloop
    pause
    scene e14s04-44 mc-nk-pw-undress1_c2 with dissolve
    pause
    scene e14s04-45 mc-nk-pw-naked1_c1 with fade
    play voice2 mc_surprised_wow3 noloop
    mc "Looks like you're making progress."
    scene e14s04-45 mc-nk-pw-naked1_c2 with dissolve
    play voice4 nora_auh noloop
    nk "Did you ever doubt me, grasshopper?"
    scene e14s04-46 mc-nk-pw-naked2_c1 with dissolve
    play voice2 mc_no_no5 noloop
    mc "Not at all, my blind sensei. Ooooh, the Pina Colada Sensei, now there's a cool movie idea."
    scene e14s04-46 mc-nk-pw-naked2_c2 with dissolve
    play voice4 nora_aga noloop volume 1.5
    nk "She fights with the power of icy drinks."
    play sound sfx_hands_clap3
    scene e14s04-47 mc-nk-pw-naked3_c1 with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "And an ass that won't quit."
    scene e14s04-47 mc-nk-pw-naked3_c2 with dissolve
    play voice4 aaleyah_closed_moan3 noloop
    pause

    jump e14s04_later

label e14s04_later:

    scene black
    show screen scene_transistion(_("One hour later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene e14s04-48 mc-nk-pw-naked4_c1
    with Fade(0.5, 0.5, 0.9)
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Are you sure about this?"
    scene e14s04-49 mc-nk-pw-naked5_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "If she takes off the blindfold and freaks out, Nora will probably get super embarrassed."
    mct "Not to mention it might put a damper on one of our best days yet."
    scene e14s04-48 mc-nk-pw-naked4_c2 with dissolve
    play voice4 aaleyah_yes_yes2 noloop
    nk "I'm ready."
    scene e14s04-50 mc-nk-pw-naked6_c3 with dissolve
    play voice3 polly_impressed noloop
    pw "You go girl. If you're good, drop it."
    play sound sfx_bandage_off1 volume 3.0
    scene e14s04-50 mc-nk-pw-uncover1_c2 with dissolve
    play voice4 nora_oh noloop volume 1.4
    nk "Oh..."
    scene e14s04-50 mc-nk-pw-uncover1_c1 with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "Everything alright?"
    scene e14s04-50 mc-nk-pw-uncover1_c2 with dissolve
    play voice4 aaleyah_disappointed_eeh noloop
    nk "No one is looking."
    scene e14s04-50 mc-nk-pw-uncover1_c3 with dissolve
    play voice3 polly_laugh3 noloop
    pw "Well except for me."
    pw "Mmm."
    play voice2 mc_thinking_mmm2 noloop
    mc "That makes two of us."
    scene e14s04-54 mc-nk-pw-uncover4_c2 with dissolve
    play voice4 aaleyah_disappointed_oof1 noloop
    nk "I guess it wasn't impossible after all. I... phew."
    nk "I can probably survive like this for an hour. Maybe two."
    scene e14s04-54 mc-nk-pw-uncover4_c3 with dissolve
    play voice3 polly_wooh noloop
    pw "That's the spirit! Just take it one step at a time."
    play sound sfx_cloth_rustling2
    scene e14s04-55 mc-nk-pw-hug1_c1 with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "And if you ever need to pull the plug, just signal to one of us and we'll help you."
    scene e14s04-55 mc-nk-pw-hug1_c2 with dissolve
    play voice4 allison_pain_sniff1 noloop
    nk "*sniff*"
    nk "What did I do to deserve the two of you?"
    scene e14s04-56 mc-nk-pw-hug2_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "In a crazy world, you've always been the kindest person I've known, Nora."
    scene e14s04-58 mc-nk-pw-cust1_c1 with dissolve
    play voice4 aaleyah_arrogant_heh noloop
    pw "What about me?"
    play voice2 mc_arrogant_heh1 noloop volume 1.3
    mc "Polly, you're the best at being a hellcat. I figured that went unsaid."
    play voice3 stacy_thinking_hm1 noloop
    pw "Every kitty likes to hear how good they are now and again, you dingus."
    play voice2 mc_arrogant_heh2 noloop
    mc "I usually 'say' it in other ways."
    pw "Meow."
    scene e14s04-58 mc-nk-pw-cust1_c3 with dissolve
    play voice5 boy5_thinking_huh noloop
    "Customer" "Uh. Hello? Can I get a drink?"
    scene e14s04-58 mc-nk-pw-cust1_c2 with dissolve
    play voice4 aaleyah_yes_yeah1 noloop
    nk "Of course."
    play sound sfx_pen_writing2 volume 2.0
    scene e14s04-59 mc-nk-pw-cust2_c2 with dissolve
    play voice4 aaleyah_happy_laugh2 noloop
    nk "Sorry for the wait. We can get a little wrapped up in our own stuff sometimes."
    scene e14s04-59 mc-nk-pw-cust2_c4 with dissolve
    play voice3 stacy_suckmoan3 noloop
    pw "I want to wrap my legs around her face while she eats out my little kitty."
    scene e14s04-60 mc-nk-pw-cust3_c1 with dissolve
    mct "I can't believe I'm going to say this."
    play voice2 mc_disappointed_off1 noloop
    mc "Come on Polly. Fun later, work now."
    scene e14s04-60 mc-nk-pw-cust3_c3 with dissolve
    play voice3 polly_yes1 noloop
    pw "Just promise me we'll make the most of our next break."
    play sound sfx_hands_clap4
    scene e14s04-61 mc-nk-pw-cust4_c2 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "I guarantee it."
    scene e14s04-61 mc-nk-pw-cust4_c1 with dissolve
    pause
    scene e14s04-a61 mc-nk-pw-cust4-glambot-61-000 with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.5
    scene e14s04-a61-glam
    pause
    stop sound fadeout 1.0
    scene e14s04-62 mc-nk-pw-cust5_c1 with dissolve
    pw "Here you go."
    queue sound sfx_drink_slurp2
    pause
    scene e14s04-62 mc-nk-pw-cust5_c3 with dissolve
    play voice5 girl27_surprised_wow1 noloop
    gt "Wow! This Mai Tai is absolutely incredible!"
    scene e14s04-62 mc-nk-pw-cust5_c2 with dissolve
    play voice3 polly_laugh1 noloop
    pw "Thanks. My girlfriend Nora is the best! She could give Moe a run for his money."
    pw "We're so glad you're enjoying our cafe."
    scene black
    show screen scene_transistion(_("A few drinks later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene e14s04-65 mc-nk-pw-sunset1_c3 with dissolve
    play voice5 girl27_happy_relief3 noloop
    gt "How long have you guys been doing this?"

    scene e14s04-68 mc-nk-pw-sunset4_c4 with dissolve
    pw "Hmm. It's actually been three months since we left Crowning."
    gt "Crazy. So you left everything behind to pursue this dream together."
    play voice4 boy5_arrogant_hm noloop
    hf "That's hardcore."
    play voice3 stacy_yes_ugu1 noloop
    pw "That's kind of our only speed."
    play sound sfx_cloth_rustling4

    scene e14s04-65 mc-nk-pw-sunset1_c4 with dissolve
    gt "Well Nora we're really loving your cafe. We're going to tell all our friends to stopy by next time they go to the beach."
    nk "Thanks so much, Gemma."
    play voice4 nora_hey noloop
    nk "But you gotta meet the final corner of our triangle."
    scene e14s04-66 mc-nk-pw-sunset2_c2 with dissolve
    nk "[mcname] this is Gemma and Harry."
    play voice2 mc_hey_hey5 noloop
    mc "Hey."
    scene e14s04-66 mc-nk-pw-sunset2_c1 with dissolve
    play voice5 boy5_surprised_wow1 noloop
    hf "Wow. You all match up so perfectly. How did you all meet?"
    scene e14s04-67 mc-nk-pw-sunset3_c4 with dissolve
    play voice3 polly_emmm noloop
    pw "Our college ran a couple of blind dating events. There was a... mixup and we three got grouped up."
    mct "Well that's one way to put it."
    scene e14s04-68 mc-nk-pw-sunset4_c3 with dissolve
    play voice4 aaleyah_thinking_hmm3 noloop
    nk "We had some bumps along the way, but eventually, each of us found something in each other that we fell in love with."
    scene e14s04-69 mc-nk-pw-sunset5_c2 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "And being together, all three of us, well it just made sense."
    scene e14s04-67 mc-nk-pw-sunset3_c1 with dissolve
    play voice5 girl27_happy_yeah2 noloop
    gt "That's incredible."
    scene e14s04-69 mc-nk-pw-sunset5_c1 with dissolve
    gt "You three should totally set up like some kind of blind date event here. Just think about it. People might come here, find someone special and then they can walk down to the beach together."
    scene e14s04-70 mc-nk-pw-idea1_c4 with dissolve
    play voice2 boy5_thinking_hmm3 noloop
    hf "That sounds perfect. It's much easier to break the ice at a cafe instead of meeting someone right on the beach."
    scene e14s04-69 mc-nk-pw-sunset5_c3 with dissolve
    play voice3 stacy_thinking_hmm3 noloop
    pw "That's a wonderful idea."
    play voice4 aaleyah_disappointed_eeh2 noloop
    nk "The nude bar isn't enough?"
    scene e14s04-68 mc-nk-pw-sunset4_c1 with dissolve
    play voice5 girl27_no_nonono4 noloop
    gt "The bar is great, but wouldn't it be nice helping others to find something magical like you, Polly and [mcname] have?"
    scene e14s04-67 mc-nk-pw-sunset3_c4 with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    pw "Huh. I never thought about it like that."
    pw "We can certainly brainstorm the idea."
    scene e14s04-69 mc-nk-pw-sunset5_c2 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Thanks Gemma."
    scene e14s04-70 mc-nk-pw-idea1_c1 with dissolve
    play voice5 girl27_yes_yap3 noloop
    gt "Anytime."
    scene e14s04-69 mc-nk-pw-sunset5_c2 with dissolve
    mc "It was great meeting you both, but we should get back to it."
    hf "Totally."

    jump e14s04_sex

label e14s04_sex:

    scene black
    show screen scene_transistion(_("A little later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
label replay_e14s04:

    if _in_replay:
        $ renpy.music.set_volume(0.45, 3.0, "music")
        play music take_the_ride_calm

    scene e14s04-72 mc-nk-pw-idea3_c2 with dissolve
    play voice4 aaleyah_happy_mmm2 noloop
    nk "Gemma's idea actually sounds like a lot of fun."
    scene e14s04-71 mc-nk-pw-idea2_c3 with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    pw "I think other people can handle their own love life. Do we really want to play matchmaker for a bunch of strangers?"
    scene e14s04-71 mc-nk-pw-idea2_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Well, without me playing assistant, who knows if you and Nora would have ever clicked."
    scene e14s04-71 mc-nk-pw-idea2_c2 with dissolve
    play voice4 aaleyah_yes_yep noloop
    nk "Exactly. Sometimes, people need a little push. And of course, if [mcname] didn't help you, the three of us wouldn't be here."
    scene e14s04-73 mc-nk-pw-idea4_c3 with dissolve
    play voice3 polly_laughter noloop
    pw "Alright, you two twisted my arm."
    scene e14s04-73 mc-nk-pw-idea4_c1 with dissolve
    play voice2 mc_yes_okay3 noloop
    mc "Cool, we can figure out the details later."
    scene e14s04-74 mc-nk-pw-idea5_c3 with dissolve
    play voice3 polly_laugh2 noloop
    pw "You certainly seemed to have hit your stride my dear."
    pw "The day started and you were all nervous about strutting your stuff in front of everyone."
    scene e14s04-74 mc-nk-pw-idea5_c2 with dissolve
    play voice4 nora_aga noloop
    nk "Thanks. But don't be surprised if I keep my apron on a few hours each shift."
    nk "But I'm definitely over the most of it. I think"
    scene e14s04-75 mc-nk-pw-idea6_c1 with dissolve
    play voice4 nora_pleasure noloop volume 2.5
    nk "I really believe that with you two as support, I could tackle anything."
    play voice2 mc_yes_yeah8 noloop
    mc "Do you mean 'anything' anything?"
    play voice3 polly_oh noloop
    pw "Like having some ball-slapping sex right here in front of our customers."
    scene e14s04-76 mc-nk-pw-idea7_c1 with hpunch
    play voice4 aaleyah_closed_moan5 noloop
    nk "Well... I'm sure more than a few have already caught you eye-fucking us both tonight. And we 'are' close to closing."
    play voice2 mc_happy_a1 noloop
    mc "I can't think of a better way to finish out the night."
    play voice3 polly_yes1 noloop
    pw "Hell yes!"
    scene e14s04-75 mc-nk-pw-idea6_c2 with dissolve
    pause
    play sound sfx_bottle_pouring1
    scene e14s04-76-2 mc-nk-pw-tequila1_c2 with dissolve
    play voice4 nora_hmm noloop volume 2.5
    nk "I don't know about you two, but I need a drink to relax."
    scene e14s04-76-2 mc-nk-pw-tequila1_c3 with dissolve
    play voice3 polly_aga noloop
    pw "Go for it. Pour one for me and [mcname] too!"
    scene e14s04-76-2 mc-nk-pw-tequila1_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "I thought we were trying to be more frugal."
    scene e14s04-76-3 mc-nk-pw-tequila2_c2 with dissolve
    play voice4 aaleyah_no_nah noloop
    nk "No worries. Some rich college kids paid for the whole thing. They made it through one round of shots and then left for the beach."
    scene e14s04-76-3 mc-nk-pw-tequila2_c3 with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    pw "Sweet!"
    play sound sfx_drinking_passionately noloop
    scene e14s04-76-4 mc-nk-pw-tequila3_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "*whispers* Sounds good."
    mct "She really is a pink-haired devil. I fucking love it."
    scene e14s04-76-4 mc-nk-pw-tequila3_c2 with dissolve
    play voice4 nora_mmm noloop volume 2.5
    nk "Hmmm."
    mct "Nora might play things cooler than Polly and I, but I can tell she's just as horny."
    pause
    play sound sfx_bottle_pouring1
    scene e14s04-76-5 mc-nk-pw-tequila4_c2 with dissolve
    play voice3 polly_wooh noloop
    pw "Woooh! That will put hair on your puss."

    scene e14s04-76-5 mc-nk-pw-tequila4_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mct "Sneaky sneak-sneak."


    $ Lovense.stop()

    scene e14s04-78 mc-nk-pw-new_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "I knew it! She's wetter than Niagra Falls."
    $ Lovense.vibrate(6)
    scene e14s04-77 mc-nk-pw-cust_c1 with hpunch
    play voice2 mc_sex_sucking_slow1 noloop
    play voice4 nora_auh noloop
    mc "*slurping*"
    queue voice4 nora_moans1 volume 2.0
    nk "*gasps* Oh hello!"
    mct "Damn she tastes so good."
    scene e14s04-77 mc-nk-pw-cust_c2 with dissolve
    nk "What can I get you?"
    play voice5 boy4_disappointed_oh noloop
    "Customer" "I hear you make a mean Mai Tai."
    scene e14s04-80 mc-nk-pw-animation1_c1 with dissolve
    play sound sfx_ice_cubes1
    play voice2 mc_sex_sucking_slow1
    nk "*moans* Oooh. Only the best."
    scene e14s04-80 mc-nk-pw-animation1_c2 with dissolve
    mct "Watch and learn ladies and gentleman."
    $ Lovense.pattern("7;10", 1400)
    scene e14s04-a80-1 with dissolve
    pause
    scene e14s04-80 mc-nk-pw-animation1_c3 with dissolve
    play voice3 polly_breathing noloop
    pw "One Mai Tain will be eight dollars."
    scene e14s04-a80-2 with dissolve
    play sound sfx_vagina_penetration1_fast loop
    play voice3 stacy_fmoans5 volume 0.8
    pause
    scene e14s04-80 mc-nk-pw-animation1_c3 with dissolve
    play voice5 boy4_yes_yeah noloop
    "Customer" "Cool."
    $ Lovense.pattern("7;10", 700)
    scene e14s04-a80-1-f with dissolve
    pause
    nk "Your drink is nearly ready. Thank you for your patience."
    scene e14s04-a80-2-f with dissolve
    pause
    play voice3 stacy_thinking_hmm4 noloop
    pw "Trust me, everything she does is worth the wait."
    stop voice2 fadeout 1.0
    stop sound fadeout 1.0
    stop voice3 fadeout 1.0
    scene e14s04-80 mc-nk-pw-animation1_c1 with dissolve
    play voice4 nora_orgasm2 noloop
    nk "Oh god! Sorry... Gets a little hot in here sometimes."
    $ Lovense.stop()
    $ Lovense.vibrate(3)
    scene e14s04-80-2 mc-nk-pw-new1_c1 with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "I better pull my weight a little bit."


    scene e14s04-81 mc-nk-pw-drink1_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Here you go man. Enjoy the drink."
    play voice5 boy4_happy_relief1 noloop
    "Customer" "Thanks. Keep the change."
    scene e14s04-81 mc-nk-pw-drink1_c2 with dissolve
    pause
    scene e14s04-82 mc-nk-pw-drink2_c2 with dissolve
    play voice3 polly_laugh3 noloop
    pw "*whispers* Such a deliciously naughty girl."
    play voice4 aaleyah_thinking_hmm2 noloop
    nk "Babe, another customer is waiting at table three."
    play sound sfx_cloth_rustling1
    scene e14s04-82 mc-nk-pw-drink2_c3 with dissolve
    play voice3 stacy_suckmoan2 noloop
    pw "I got it covered."
    scene e14s04-83 mc-nk-pw-drink3_c3 with dissolve
    play voice3 polly_hey noloop
    pw "What can I get for you?"
    scene e14s04-83 mc-nk-pw-drink3_c1 with dissolve
    play voice2 mc_happy_hah2 noloop
    mct "Polly looks like she needs an assist."
    mct "An {i}anal{/i} assist."
    scene e14s04-84 mc-nk-pw-drink4_c1 with dissolve
    $ Lovense.vibrate(6)
    play voice3 polly_orgasm3 noloop
    pw "*squeaks* Sweet jeebus!"
    scene e14s04-84 mc-nk-pw-drink4_c3 with dissolve
    play voice5 girl28_hey_active noloop
    "Customer" "Hello. We wanted to hear about your specials."
    play voice2 d2s9_confused noloop volume 1.5
    mc "You're too far away, let me help you out."
    play sound sfx_bed_slide1
    scene e14s04-85 mc-nk-pw-animation2_c1 with hpunch
    play voice3 polly_moans
    play voice2 d7s4_mcbreathing
    pw "*hitched breathing* Specials. Yes. YES! We have half-off on penis. I mean. Half-off on Piña Coladas and Daiquiris."
    play sound sfx_vagina_penetration1_fast loop volume 0.5
    $ Lovense.pattern("7;10", 1400)
    scene e14s04-a85-1 with dissolve
    pause
    scene e14s04-85 mc-nk-pw-animation2_c3 with dissolve
    play voice5 girl28_happy_mmm1 noloop
    "Customer" "Mmm. They both sound great."
    $ Lovense.pattern("7;10", 700)
    scene e14s04-a85-1-f with dissolve
    pause
    play voice3 stacy_fmoans3 volume 0.7
    mc "*whispers* Too hot for you to handle?"
    pw "*whispers* No fucking way. You haven't even hit my sweet spot."
    mc "*whispers* So why are you moaning so much?"
    pw "*whispers* I never said your cock wasn't useful, dummy."
    pw "Uhhowwoohow! [mcname]! You're pulverizing my asshole!!"
    stop voice2 fadeout 1.5
    stop voice3 fadeout 1.5
    $ Lovense.stop()
    $ Lovense.vibrate(3)
    scene e14s04-87 mc-nk-pw-drinks_c1 with dissolve
    pw "Mmm."
    scene e14s04-86 mc-nk-pw-kiss_c1 with dissolve
    play sound dahlia_kiss_french1
    stop voice2 fadeout 1.0
    play voice3 stacy_suckmoan1 noloop
    pw "Mrrrmmm-wrmmm-hmmm."
    scene e14s04-86 mc-nk-pw-kiss_c2 with dissolve
    play sound maria_kiss2
    pause
    scene e14s04-83 mc-nk-pw-drink3_c2 with dissolve
    play voice4 nora_hey noloop
    nk "Hey you crazy kids, what do we need?"
    pw "*panting* Two daiquiris and a shot of tequila."
    play sound sfx_blender_mix1
    play voice4 aaleyah_yes_aga1 noloop
    nk "On it!"
    scene e14s04-86 mc-nk-pw-kiss_c4 with dissolve
    pause
    scene e14s04-87 mc-nk-pw-drinks_c4 with dissolve
    pause
    stop voice2 fadeout 1.0
    scene e14s04-87 mc-nk-pw-drinks_c2 with dissolve
    play voice3 polly_breathing noloop
    pw "*panting*Such a fucking wildman, pounding my ass in front of those two."
    play voice2 mc_thinking_mmm2 noloop
    mc "Don't pretend like you didn't love it."
    play voice3 stacy_thinking_hmm1 noloop
    pw "Being with you and Nora has certainly had me thinking about cock and cock-associated things for a while now."
    scene e14s04-87 mc-nk-pw-drinks_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh really. Care to elaborate."
    play voice3 stacy_no_nope4 noloop
    pw "Nope."
    scene e14s04-87-2 mc-nk-pw-drinks2_c3 with dissolve
    pause
    scene e14s04-88-3 mc-nk-pw-blindfold3_c3 with dissolve
    play voice4 aaleyah_disappointed_mff noloop
    nk "Can we try something new on [mcname]?"
    play voice2 d1s2_hmm noloop volume 1.7
    mc "What's on your mind?"
    nk "Well... you've been with us a few times now."
    scene e14s04-88-3 mc-nk-pw-blindfold3_c2 with dissolve
    play voice3 polly_impressed noloop
    pw "Forty-two times to be exact."
    scene e14s04-88-3 mc-nk-pw-blindfold3_c1 with dissolve
    play voice4 aaleyah_thinking_hmm3 noloop
    nk "You must be... very familiar with how- how we both {i}feel{/i}, if you get what I mean."
    play voice3 stacy_happy_relief1 noloop
    pw "Ooh. This is going to be fun. Let's see if [mcname] can guess who's pussy or mouth he's playing with without looking."
    play sound sfx_hair_scratch1
    scene e14s04-88-4 mc-nk-pw-blindfold4_c1 with dissolve
    pause
    scene e14s04-88-4 mc-nk-pw-blindfold4_c2 with dissolve
    pause
    play sound maria_kiss1
    scene e14s04-88-5 mc-nk-pw-blindfold5_c1 with dissolve
    play voice3 stacy_suckmoan2 noloop
    pause
    play sound maria_kiss3
    scene e14s04-88-5 mc-nk-pw-blindfold5_c2 with dissolve
    play voice4 aaleyah_closed_moan2 noloop
    nk "Mowah."
    scene e14s04-88-6 mc-nk-pw-blindfold6_c1 with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Ohwah-oh."
    play voice3 polly_angry noloop
    pw "If you can't tell who is who, you're sleeping with the crabs tonight, big boy."
    mct "Oh boy. Shit just got real."
    scene e14s04-88-6 mc-nk-pw-blindfold6_c2 with dissolve
    play voice3 polly_laugh1 noloop
    pw "Just lie down and relax."
    scene e14s04-88-7 mc-nk-pw-table_c1 with dissolve
    play voice4 nora_pleasure noloop volume 1.5
    nk "Your audience is already looking quite impressed."
    scene e14s04-88-7 mc-nk-pw-table_c2 with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    pw "Get ready."
    play sound sfx_cloth_rustling4
    scene e14s04-89 mc-nk-pw-table_c1 with dissolve
    pause
    scene e14s04-89 mc-nk-pw-table_c2 with dissolve
    play voice4 nora_heh noloop
    nk "After we've had our fun, you'll have to guess."
    scene e14s04-89 mc-nk-pw-table_c3 with dissolve
    play voice3 stacy_yes_yap1 noloop
    pw "Yup, so for now, get busy licking on that pussy hanging right above your tongue."
    $ renpy.music.set_pan(-0.75, 0.0, "voice5")
    $ Lovense.pattern("7;10", 1400)
    scene e14s04-a90-1 with dissolve
    play voice5 girl28_happy_woohoo1 noloop
    play voice3 polly_moans
    play voice2 mc_sex_sucking_slow1
    play voice4 nora_sucks_mouth

    gt "Woohoo!"

    scene e14s04-a90-2 with dissolve
    pw "Good boy. That looks like it feels... really good."
    $ renpy.music.set_pan(0.0, 1.0, "voice5")
    $ Lovense.pattern("7;12", 700)
    scene e14s04-a90-1-f with dissolve
    pause
    scene e14s04-a90-2-f with dissolve
    pause
    $ Lovense.pattern("7;10", 1400)
    scene e14s04-a95-2 with dissolve
    play voice2 d7s4_mcbreathing
    nk "So good."
    "???" "*slurping*"
    "???" "*moaning*"
    $ Lovense.pattern("7;12", 700)
    scene e14s04-a95-2-f with dissolve
    pw "You can lick harder. No need to be gentle."
    nk "Mmmhmm."
    $ Lovense.pattern("7;10", 1400)
    scene e14s04-a90-1 with dissolve
    play voice2 mc_sex_sucking_slow1
    play voice3 stacy_fmoans2
    mct "Well this pussy is certainly extremely wet."
    mct "It's easy to slide my tongue inside too, but the moment I get in there, her walls squeeze onto me like a bear trap."
    scene e14s04-a90-2 with dissolve
    mc "*hungry slurping*"
    pw "Yes. Oh that's good. Really good. Mraaah."
    $ Lovense.pattern("7;12", 700)
    scene e14s04-a90-1-f with dissolve
    pause
    scene e14s04-a90-2-f with dissolve
    pause
    mct "Well, Nora isn't talking much, so I must be eating out Polly's delicious cookie. She always is the greedy one out of all three of us."
    mct "Fuck me, it feels like Nora is going to suck my soul out of my balls!"
    $ Lovense.pattern("7;11", 1400)
    scene e14s04-a100-2 with dissolve
    play voice2 d7s4_mcbreathing
    nk "Time to change things up."
    nk "Mrrrwaaah."
    scene e14s04-a100-3 with dissolve
    pause
    play voice4 aaleyah_open_moans1
    pw "Go for it, slugger. Pound that hot snatch!"
    nk "Yes. I think it's begging for your thick, hot cock!"
    scene e14s04-a100-2-f with dissolve
    mct "Alright, this breadbox is way tighter. They must have switched places."
    mc "Can I guess yet?"
    scene e14s04-a100-3-f with dissolve
    pw "*moaning loudly* What's... Mraah... what's the rush?"
    nk "Yes. Just keep going. Please [mcname]!"
    scene e14s04-a100-2-f with dissolve
    nk "Yes! Right there. I mean... Oh fuck!"
    mct "Well that clinches it."
    play voice4 nora_sucks_mouth
    scene e14s04-a95-2 with dissolve
    mc "Sounds like I'm porking Nora and Nora... you're making Polly's pussy drool with your fingers."
    pw "Annngh! Total miss. It's her tongue."
    pw "*panting* Her fucking amazing tongue."
    nk "Thank you, Polly. Oh god. [mcname], I'm c-cumming. Cumming!"
    play voice4 aaleyah_open_moans1
    scene e14s04-a100-3-f with dissolve
    nk "*delirious moans*"
    pw "Too much?"
    nk "No. Just right. Mmm. You're so gorgeous."
    pw "I know right."
    pw "Alright sailor. You guessed right, so you deserve a prize."
    pw "My special harbor is open. Why don't you 'come' home?"
    scene e14s04-a100-2-f with dissolve
    mc "Happy to. Bring that pussy right here!"
    pw "Ooooh."

    nk "Cum all over us, [mcname]!"
    pw "I'm still cumming!"
    pw "Oh, you fuckeruaaah!"
    play voice2 d1s5_orgasm2 noloop
    play voice4 aaleyah_orgasm_shortmoan1 noloop
    $ Lovense.stop()
    $ Lovense.vibrate(17)
    scene e14s04-102 mc-nk-pw-cum2_c1 with vpunch
    pause
    play voice3 polly_orgasming2 noloop
    $ Lovense.vibrate(16)
    scene e14s04-103 mc-nk-pw-cum3_c2 with vpunch
    pw "Wooouwwaaahah!"
    nk "Amazing."
    $ Lovense.vibrate(3)
    scene e14s04-104 mc-nk-pw-cum4_c3 with dissolve
    play voice2 mc_angry_errr4 noloop
    mc "I'm not done yet."
    play voice2 mc_pain_argh1 noloop
    play voice3 polly_orgasm2 noloop
    $ Lovense.vibrate(18)
    scene e14s04-104 mc-nk-pw-cum4_c2 with vpunch
    pw "My ass!"
    play voice2 mc_angry_errr3 noloop
    play voice3 polly_orgasm3 noloop
    $ Lovense.vibrate(19)
    scene e14s04-104 mc-nk-pw-cum4_c1 with vpunch
    mc "*grunts*"
    scene e14s04-102 mc-nk-pw-cum2_c2 with dissolve
    $ Lovense.vibrate(3)
    nk "It's dripping onto my flesh. Mmm. You okay, Polly?"
    play voice3 polly_breathing noloop
    pw "Better than okay."
    pw "Mrmmm."
    scene e14s04-106 mc-nk-pw-k2_c2 with dissolve
    play voice3 polly_laugh2 noloop
    pw "Nothing like having a stud worship your body and give you exactly what you're craving."
    play voice4 aaleyah_yes_aga4 noloop
    nk "*moans approvingly*"
    scene e14s04-106 mc-nk-pw-k2_c1 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Mmrrm. That got a little wild. Even for you."
    play sound sfx_cloth_wiping1 volume 2.5
    scene e14s04-107 mc-nk-pw-wipe_c2 with dissolve
    play voice3 polly_laugh noloop
    pw "Hah. You ain't seen nothing yet."
    scene e14s04-107 mc-nk-pw-wipe_c3 with dissolve
    pause
    stop sound fadeout 1.0
    scene e14s04-108 mc-nk-pw-kiss_c2 with dissolve
    play voice3 polly_licking
    play voice4 nora_sucks_mouth
    pause
    scene e14s04-108 mc-nk-pw-kiss_c3 with dissolve
    pause
    play voice2 mc_thinking_mmm2 noloop
    scene e14s04-108-2 mc-nk-pw-kiss2_c1 with dissolve
    queue voice2 d3s8_sucking2
    pause
    scene e14s04-108-2 mc-nk-pw-kiss2_c2 with dissolve
    pause
    scene e14s04-108-2 mc-nk-pw-kiss2_c3 with dissolve
    pause
    play voice5 girl27_surprised_wow1 noloop
    gt "*cheers* Woah. A drink and a show. I think I need to skip the beach and get drilled myself after watching that."
    play voice5 boy5_happy_laugh1 noloop
    hf "I'll drink to that."

    $ Lovense.stop()


    $ renpy.end_replay()
    $ unlock_gallery_slot("scene", "e14s04")
    stop voice2 fadeout 1.0
    stop voice3 fadeout 1.0
    stop voice4 fadeout 1.0
    scene e14s04-109-2 mc-nk-pw-talk2_c1 with fade
    play voice2 mc_thinking_emm1 noloop
    mc "You sure you're good. Normally you're not so into me firing off inside of you."
    play voice3 polly_nouh noloop
    pw "It was nothing. I just wanted to make you go beast-mode on me."
    scene e14s04-109-2 mc-nk-pw-talk2_c2 with dissolve
    play voice4 aaleyah_disappointed_mff noloop
    nk "You certainly started humping her like you wanted nothing more than to pump a baby inside of her."
    scene e14s04-109-2 mc-nk-pw-talk2_c3 with dissolve
    play voice3 aaleyah_disappointed_mff noloop
    pw "*giggling* Yeah. You're such a man, [mcname]. Never change."
    scene e14s04-110 mc-nk-pw-end1_c3 with dissolve
    play voice3 polly_impressed noloop
    pw "But now, we need to get ready to close up shop."
    play sound sfx_cleaning_floor2
    scene e14s04-110 mc-nk-pw-end1_c1 with dissolve
    stop sound fadeout 3.5
    play voice4 aaleyah_yes_yes1 noloop
    nk "Right! How about you clean up here while we clean up the bar and kitchen?"
    play voice2 mc_happy_hah2 noloop
    mc "On it. But then you two might have to clean me up one more time after we're done."
    play voice4 aaleyah_disappointed_oof1 noloop
    nk "Ooooh, I love the way you think, [mcname]."
    stop music fadeout 3.0

    jump e14s05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
