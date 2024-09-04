label e14s02:

    scene black
    show screen scene_transistion(_("Some time later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    queue music caffee_theme_2
    hide screen scene_transistion
    $ renpy.music.set_volume(1.0, 0.0, "music2")
    $ renpy.music.set_volume(1.0, 0.0, "sound")
    $ renpy.music.set_volume(1.0, 0.0, "sound2")
    $ renpy.music.set_volume(1.0, 0.0, "sound3")
    $ renpy.music.set_volume(1.0, 0.0, "sound4")
    play sound4 sfx_seawaves_ambience2 fadein 2.0
    scene e14s02-01 noras-cafe-open_c1
    with Fade(0.5, 0.5, 0.9)
    pause
    $ renpy.music.set_volume(0.1, 1.0, "sound4")
    scene e14s02-02 nk-pouring-coffee-pw-excited-woo_c1 with dissolve
    play voice3 polly_wooh noloop
    pw "The first day of \"Nora's\"! Wooo!"
    scene e14s02-03 pw-hugs-nk-behind-ask-excited-nk-not-word_c1 with dissolve
    play voice3 polly_laughter noloop
    pw "Are you excited?"
    play voice4 nora_oh noloop
    nk "I don't think 'excited' is the word."
    scene e14s02-04 pw-asking-what-wrong-nk-hesitant_c1 with dissolve
    play voice3 polly_huh noloop
    pw "What's wrong, Nora?"
    play voice4 nora_mmm noloop volume 1.5
    nk "I..."
    play sound sfx_cup_slide1
    scene e14s02-05 nk-stops-what-if-mistake_c1 with dissolve
    play voice4 aaleyah_disappointed_eeh noloop
    nk "What if this was a mistake? I barely survived the last cafe. What if I dragged you two hundreds of miles from home-"
    nk "Only to fuck it all up."
    scene e14s02-06 pw-cups-chin-being-stupid-mc-never-met-better-coffee_c1 with dissolve
    play voice3 polly_angry noloop
    pw "Nora, I love you, but you're being stupid right now."
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah, I've never met someone who makes better coffee than you."
    pw "You don't have to worry. Plus this time you have us."
    play sound maria_kiss1
    scene e14s02-06 pw-kiss-nk-she-tells-overthinking-it_c1 with dissolve
    play voice4 nora_heh noloop
    nk "You're right. I'm overthinking it."
    play voice2 mc_yes_yes2 noloop
    mc "A little bit."
    scene e14s02-07 all-three-holding-coffee-nk-says-first-cup_c1 with dissolve
    play voice4 nora_nhey noloop
    nk "The first cup of joe poured at Nora's. Cheers!"
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "As an {i}almost{/i} business major graduate, I have to say that giving out free drinks is a bad business practice."
    scene e14s02-08 nk-suggest-that-so-smartass-ran-old-place-alone-years_c1 with dissolve
    play voice4 aaleyah_disappointed_mff noloop
    nk "Is that so smart ass?"
    nk "You know I ran the old place by myself for years without your help?"
    play sound sfx_door_slide4
    scene e14s02-09 pw-shut-it-customer-approaching_c1 with dissolve
    play voice3 stacy_hey_angry1 noloop
    pw "You two quit bickering, there's a customer!"
    scene e14s02-10 pw-welcomes-customer-ask-what-cu-answer-medium-coffee_c1 with dissolve
    play voice3 stacy_thinking_hmm2 noloop
    pw "Hi! Welcome to Nora's! What would you like?"
    play voice5 boy5_disappointed_ehh1 noloop
    "Customer" "Uhh, medium coffee?"
    scene e14s02-11 pw-first-customer-suggest-nicer-cu-wants-latte_c1 with dissolve
    play voice3 stacy_huh2 noloop
    pw "That's it? You're our first customer ever! Surely we can get you something a little nicer."
    play voice5 boy5_thinking_hmm1 noloop
    "Customer" "Fine, what about a latte?"
    scene e14s02-12 pw-latte-on-house-mc-cuts-in-not-on-house_c1 with dissolve
    play voice3 polly_aga noloop
    pw "Perfect! One latte on the house!"
    play voice2 d2s9_confused noloop volume 1.6
    mc "It's not on the house."
    scene e14s02-13 cu-not-in-rush-pw-nora-latte-die-for_c1 with dissolve
    play voice5 boy5_yes_aga noloop
    "Customer" "Whatever. I'm not really in a rush."
    play voice3 stacy_yes_yeah1 noloop
    pw "Good, because a latte from Nora is to die for."
    scene e14s02-14 nk-tells-customer-seven-bucks-cu-damn_c1 with dissolve
    play voice4 nora_aga noloop
    nk "That'll be 7 bucks."
    play voice5 boy5_arrogant_huh noloop
    "Customer" "Damn."
    play sound sfx_paper_slide1 volume 2.0
    scene e14s02-15 cu-leaves-money-reaches-for-coffee_c1 with dissolve
    pause
    play sound sfx_drink_slurp2
    scene e14s02-16 cu-drinks-coffee-surprised-face_c1 with dissolve
    pause
    scene e14s02-17 cu-again-damn-nk-worried-asking-what-wrong_c1 with dissolve
    play voice5 boy5_angry_dough noloop
    "Customer" "Hot damn!"
    play voice4 nora_huh noloop
    nk "Something wrong?"
    scene e14s02-18 cu-best-latte-ever-will-deff-come-back_c1 with dissolve
    play voice5 boy5_no_high noloop
    "Customer" "That's the best latte I've ever had."
    "Customer" "I'll definitely be back! I'm going to tell everyone at the beach about this place!"
    scene e14s02-19 cu-leaves-nk-joins-mc-pw_c1 with dissolve
    pause
    play sound sfx_skirt_off2
    scene e14s02-20 pw-jumps-hugs-nk-knew-would-do-great_c1 with dissolve
    play voice3 stacy_happy_yay3 noloop
    pw "I knew you'd do great!"
    play voice4 aaleyah_happy_laugh1 noloop
    nk "Polly, I've been making coffee for a long time."
    scene e14s02-21 pw-not-here-mc-joins-hug-either-way-million-more-coming_c1 with dissolve
    play voice3 polly_nouh noloop
    pw "Not here you haven't!"
    play voice2 mc_happy_yay2 noloop
    mc "Either way, first one down and a million to go!"
    scene e14s02-22 nk-two-are-insane-mc-ofc_c1 with dissolve
    play voice4 nora_pleasure noloop volume 1.4
    nk "You two are insane, you know that right?"
    play voice2 mc_yes_sure1 noloop
    mc "Of course we are. We're here aren't we?"
    scene e14s02-23 pw-jokes-talk-yourself-mc-reminds-her-labels_c1 with dissolve
    play voice3 polly_impressed noloop
    pw "Speak for yourself."
    play voice2 mc_yes_aga1 noloop
    mc "Says the woman who refuses to do labels."
    scene e14s02-24 pw-sits-counter-mc-impressed-pw-knows_c1 with dissolve
    play voice2 d2s9_mchey noloop
    mc "You know Polly, I'm impressed. That was one hell of a sales speech you gave that customer."
    play voice3 stacy_yes_yeah2 noloop
    pw "I know."
    scene e14s02-25 mc-future-marketing-pw-just-wait-nora-bar_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "It looks like you might have a future in marketing."
    play voice3 polly_laugh3 noloop
    pw "If you thought that was good, wait until we open \"Nora's Bar\" for the first time."
    scene e14s02-26 nk-looks-pw-cant-sit-counter-why_c1 with dissolve
    play voice4 aaleyah_disappointed_eh1 noloop
    nk "Polly, you can't sit on the counter."
    play voice3 polly_emmm noloop
    pw "Why?"
    scene e14s02-27 nk-health-code-violation-pw-no-inspector-here_c1 with dissolve
    play voice4 aaleyah_thinking_hmm2 noloop
    nk "It's a health code thing."
    play voice3 polly_hey noloop
    pw "There isn't a health inspector here."
    scene e14s02-28 pw-what-after-work-nk-reminds-just-opened_c1 with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    pw "What do you two want to do after work?"
    play voice4 aaleyah_disappointed_mff2 noloop
    nk "Polly, we just opened. There's still eight and a half hours to go."
    pw "I know, I'm just excited that we'll have some free time now!"
    scene e14s02-29 pw-just-excited-mc-free-time-nice_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Free time will be nice."
    scene e14s02-30 nk-two-not-owned-business-mc-what-mean-nk-no-free-time_c1 with dissolve
    play voice4 aaleyah_disappointed_oh1 noloop
    nk "You two haven't ever owned a business."
    play voice2 d1s2_hmm noloop volume 1.6
    mc "What do you mean?"
    nk "Ha, you don't have free time when you own a business."
    scene e14s02-31 pw-come-on-little-fun-nk-fine-go-somewhere-tonight_c1 with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    pw "Come on, Nora! You have to have at least a little bit of fun."
    play voice4 aaleyah_thinking_hmm3 noloop
    nk "Fine. Maybe we can go somewhere tonight."
    play voice3 stacy_happy_yay1 noloop
    scene e14s02-32 pw-yay-knows-place-check-mc-ask-where_c1 with dissolve
    pw "Yay! I actually heard of a place we can go check out."
    play voice2 mc_thinking_hmm4 noloop
    mc "Where?"
    scene e14s02-33 pw-nude-beach-five-mins-mct-how-much-lucky_c1 with dissolve
    play voice3 polly_laugh2 noloop
    pw "There's a nude beach really close by. Like a five minute walk."
    mct "Hell. Yes. How could I get so lucky?"
    scene e14s02-34 mc-sounds-great-nk-not-so-sure_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "That sounds super fun."
    play voice4 aaleyah_happy_mmm1 noloop
    nk "I don't know."
    scene e14s02-35 pw-ask-what-wrong-nk-not-crazy-about-public-stuff_c1 with dissolve
    play voice3 stacy_arrogant_huh2 noloop
    pw "What's wrong?"
    play voice4 aaleyah_disappointed_eeh2 noloop
    nk "I'm still not crazy about the public stuff."
    scene e14s02-36 pw-all-will-naked-nk-maybe-help-for-her_c1 with dissolve
    play voice3 stacy_arrogant_hmm3 noloop
    pw "Everyone will be naked though, that makes it better!"
    play voice4 aaleyah_yes_yes4 noloop
    nk "Maybe for you."
    scene e14s02-37 mc-suggest-blindfold-nk-agrees-helped-last-time_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Should we bring that blindfold again?"
    play voice4 nora_hmm noloop volume 1.8
    nk "... It did help last time."
    scene e14s02-38 pw-have-to-get-comfortable-no-blindfold-nk-agrees_c1 with dissolve
    play voice3 polly_mmmuhuh noloop
    pw "We should try to get you comfortable with being naked without the blindfold though."
    play voice4 aaleyah_happy_mmm2 noloop
    nk "Maybe."
    scene e14s02-39 pw-hugs-nk-behind-best-way-being-naked-nk-wont-let-go-till-beach_c1 with dissolve
    play voice3 stacy_thinking_hmm3 noloop
    pw "The best way to start getting comfy being naked, is being naked."
    play voice4 aaleyah_angry_cagh1 noloop
    nk "You're not going to let this go until we head to the beach, huh."
    scene e14s02-40 pw-nope-nk-agrees-fine_c1 with dissolve
    play voice3 stacy_no_nope4 noloop
    pw "Nope!"
    play voice4 aaleyah_disappointed_oof1 noloop
    nk "Ugghhhh, fine."
    play sound sfx_hair_scratch1
    scene e14s02-41 pw-hugs-nk-tight-superfun-mct-agrees_c1 with dissolve
    play voice3 stacy_happy_yay2 noloop
    pw "Awesome. This is going to be super fun."
    play voice2 mc_happy_yes1 noloop
    mc "Yes it is!"
    scene e14s02-42 pw-moves-mc-happy-all-here-mc-also_c1 with dissolve
    play voice3 polly_laugh1 noloop
    pw "I'm so happy we're all here."
    play voice2 mc_yes_yeah1 noloop
    mc "Me too."
    scene e14s02-43 pw-thanks-mc-ask-for-what-pw-explains-coming-with-them_c1 with dissolve
    play voice3 stacy_happy_hmm1 noloop
    pw "[mcname]... Thank you."
    play voice2 mc_thinking_mmm4 noloop
    mc "For what?"
    pw "For coming with us."
    play sound sfx_cloth_rustling4
    scene e14s02-44 pw-closer-mc-could-not-done-without-mc-would-be-fine-without-him_c1 with dissolve
    pw "I don't think we could have done this without you."
    play voice2 mc_arrogant_nah1 noloop
    mc "You two would have been fine without me."
    play voice3 polly_nono noloop
    pw "You are an integral part of what we have! I kind of hate to admit it but..."
    scene e14s02-45 pw-looks-back-nk-mc-smiles_c1 with dissolve
    play voice3 polly_breathing noloop
    pw "Without you, we wouldn't be together."
    play voice2 mc_arrogant_heh1 noloop
    mc "Sounds like you're being a little introspective."
    pw "A little bit. I guess..."
    play sound sfx_cloth_rustling1
    scene e14s02-46 mc-pw-sit-table-she-explains-flow-been-reflecting_c1 with dissolve
    play voice3 stacy_upset1 noloop
    pw "I love going with the flow, that's how I got here. I never would have guessed I would be here with you two."
    pw "It's made me reflect though. How I got here, what we're doing, where we're going..."
    scene e14s02-47 nk-walk-over-joking-pw-thinks-future-pw-agrees_c1 with dissolve
    play voice4 nora_huuuh noloop
    nk "Hold up. Are you telling me Polly Wilson is thinking about the future?"
    play voice3 polly_laugh noloop
    pw "Eventually you have to, right? \"If you don't think about the future, you cannot have one.\""
    scene e14s02-48 mc-pretty-deep-pw-someone-deep-not-the-point_c1 with dissolve
    play voice2 mc_surprised_wow1 noloop
    mc "Damn, that's pretty deep."
    play voice3 stacy_yes_ugu1 noloop
    pw "John Galsworthy was pretty deep. That's not the point though."
    scene e14s02-49 pw-loves-them-both-mc-tells-we-love-too_c1 with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    pw "I'm finally in a place where I kind of want to have a future. I love you two."
    play voice2 d9s2_mcyes noloop volume 2.4
    mc "And we love you."
    scene e14s02-50 nk-affirms-love-pw-deff-super-new_c1 with dissolve
    play voice4 aaleyah_yes_aga4 noloop
    nk "We do."
    play voice3 stacy_thinking_hm1 noloop
    pw "This is definitely super new to me."
    scene e14s02-51 nk-new-to-this-too-mc-jokes-about-it_c1 with dissolve
    play voice4 aaleyah_yes_yes1 noloop
    nk "I'd say the same."
    play voice2 mc_yes_yeah7 noloop
    mc "I can't say that I've ever been in a throuple starting a new business."
    scene e14s02-52 nk-glares-mc-calls-smartass-pw-must-think-really-thinking-future_c1 with dissolve
    play voice4 nora_heh noloop
    nk "Smart ass."
    play voice3 stacy_thinking_emm1 noloop
    pw "Everything too has made me think. One day maybe we'll get a house. Maybe I'll get pregnant. Maybe we'll all grow old having wild threesomes on the beach."
    nk "When you start thinking about the future, you really start thinking about the future."
    scene e14s02-53 pw-shrugs_c1 with dissolve
    play voice3 polly_aga noloop
    pw "A little bit. What can I say?"
    play voice4 nora_pleasure noloop
    nk "House, kids, threesomes?"
    play voice2 mc_hey_hey3 noloop
    mc "We don't have to wait too long for threesomes though."
    scene e14s02-54 pw-nk-both-look-mc_c1 with dissolve
    play voice4 aaleyah_disappointed_mff noloop
    nk "Can you only think about sex?"
    play voice2 mc_no_no2 noloop
    mc "... No?"
    nk "Of all the things she said, that's the only thing you heard."
    scene e14s02-55 mc-stands-up_c1 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "I heard the other stuff! I wasn't sure what to say. I was a bit surprised when you brought up kids."
    play voice3 polly_huh noloop
    pw "Why? Don't you think I'd make a good mom?"
    scene e14s02-56 mc-insist-he-do-has-agree-mc_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "I do! I just... I'm shocked that's something you'd want."
    play voice4 aaleyah_yes_yes2 noloop
    nk "I have to agree with [mcname], Polly. I'm also a little surprised by that."
    scene e14s02-57 pw-ask-what-surprise-nk-talk-about-labels-pw-doesnt-care-labels_c1 with dissolve
    play voice3 polly_impressed noloop
    pw "What's so surprising about it?"
    play voice4 aaleyah_thinking_hmm2 noloop
    nk "Usually 'free spirits' and 'children' don't really flow together."
    pw "Labels, labels, labels. I can be whatever I want, whenever I want."
    scene e14s02-58 pw-crosses-arms-no-need-fit-box-nk-knows_c1 with dissolve
    play voice3 min_arrogant_hm noloop
    pw "When will you two figure that out? I don't need to fit into some box."
    play voice4 aaleyah_disappointed_mff2 noloop
    nk "I know Polly, I know. We're just surprised."
    scene e14s02-59 mc-if-something-you-want-mct-wouldnt-mind-creampie-again_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "If that's something you want..."
    mct "... I wouldn't mind creampie-ing you again."
    scene e14s02-60 pw-ask-remember-time-fuck-pussy-mc-struggles-answers_c1 with dissolve
    play voice3 polly_angry noloop
    pw "You remembering the one time I let you fuck me in my pussy?"
    play voice2 d3s7_mcemm noloop volume 1.6
    mc "Uhhhh..."
    scene e14s02-61 pw-happy-totally-remember-havent-stopped-thinking-about-it-mc-no-words_c1 with dissolve
    play voice3 polly_laugh3 noloop
    pw "You totally are. You probably haven't stopped thinking about it since, have you?"
    play voice2 d1s5b_emmm noloop volume 1.4
    mc "I mean..."
    scene e14s02-62 pw-shows-how-tight-she-was-mc-shock_c1 with dissolve
    play voice3 min_disappointed_ehh1 noloop
    pw "Remember how I let you penetrate me, the first man in years to do so?"
    pw "How tight and wet it was? Oh, remember how my pussy just sucked you in, swallowing your dick."
    play voice2 mc_angry_huh2 noloop
    mc "Mmmm-"
    scene e14s02-63 nk-gets-hot-wants-calm-down-pw-good-mc-ugh_c1 with dissolve
    play voice4 nora_angrymoan noloop volume 1.8
    nk "Polly, calm down. You're getting me turned on."
    play voice3 polly_laugh noloop
    pw "Good. Gives you something to think about for the rest of the day."
    play voice2 mc_disgust_ooh1 noloop
    mc "Ugggh."
    scene e14s02-64 empty-cafe-mc-suggest-quicky-nk-customer-pw-points-cafe-empty_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "What about a quickie in the back?"
    play voice4 nora_oh noloop volume 1.3
    nk "What if a customer comes in? It's a bad look on your first day to disappear for twenty minutes."
    play voice3 min_disappointed_ehh3 noloop
    pw "There's no one-"
    scene e14s02-65 new-customer-walks-in_c1 with dissolve
    play voice4 nora_aga noloop
    nk "See what I mean? You never know when someone is going to walk in."
    scene e14s02-66 nk-goes-for-customer-tells-gang-be-professional_c1 with dissolve
    play voice4 aaleyah_thinking_hmm1 noloop
    nk "And Polly, keep that sexy ass off the counter."
    scene e14s02-67 pw-mc-fiiine-will-be-more-professional-end-scene_c1 with dissolve
    play voice3 stacy_yes_fine4 noloop
    pw "Fiiiiiiiine."
    stop music fadeout 3.0
    stop sound4 fadeout 3.0

    jump e14s03

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
