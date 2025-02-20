image e11s05-a42-1 = Movie(play = "images/E-11/s05/anim/e11s05-a42-1-2x-50fps.webm", start_image = "e11s05-a42-1 mc-fucking-dd-standing-anim-01")
image e11s05-a42-1-f = Movie(play = "images/E-11/s05/anim/e11s05-a42-1-2x-60fps.webm", start_image = "e11s05-a42-1 mc-fucking-dd-standing-anim-01")
image e11s05-a42-2 = Movie(play = "images/E-11/s05/anim/e11s05-a42-2-2x-50fps.webm", start_image = "e11s05-a42-2 mc-fucking-dd-standing-anim-01")
image e11s05-a42-2-f = Movie(play = "images/E-11/s05/anim/e11s05-a42-2-2x-60fps.webm", start_image = "e11s05-a42-2 mc-fucking-dd-standing-anim-01")
image e11s05-a42-3 = Movie(play = "images/E-11/s05/anim/e11s05-a42-3-2x-50fps.webm", start_image = "e11s05-a42-3 mc-fucking-dd-standing-anim-01")
image e11s05-a42-3-f = Movie(play = "images/E-11/s05/anim/e11s05-a42-3-2x-60fps.webm", start_image = "e11s05-a42-3 mc-fucking-dd-standing-anim-01")

image e11s05-a51-1 = Movie(play = "images/E-11/s05/anim/e11s05-a51-1-2x-50fps.webm", start_image = "e11s05-a51-1 dd-bj-mc-anim-01")
image e11s05-a51-1-f = Movie(play = "images/E-11/s05/anim/e11s05-a51-1-2x-60fps.webm", start_image = "e11s05-a51-1 dd-bj-mc-anim-01")
image e11s05-a51-2 = Movie(play = "images/E-11/s05/anim/e11s05-a51-2-2x-50fps.webm", start_image = "e11s05-a51-2 dd-bj-mc-anim-01")
image e11s05-a51-2-f = Movie(play = "images/E-11/s05/anim/e11s05-a51-2-2x-60fps.webm", start_image = "e11s05-a51-2 dd-bj-mc-anim-01")
image e11s05-a51-3 = Movie(play = "images/E-11/s05/anim/e11s05-a51-3-2x-50fps.webm", start_image = "e11s05-a51-3 dd-bj-mc-anim-01")
image e11s05-a51-3-f = Movie(play = "images/E-11/s05/anim/e11s05-a51-3-2x-60fps.webm", start_image = "e11s05-a51-3 dd-bj-mc-anim-01")

image e11s05-a65-1 = Movie(play = "images/E-11/s05/anim/e11s05-a65-1-2x-50fps.webm", start_image = "e11s05-a65-1 mc-fucks-dd-behind-naked-anim-01")
image e11s05-a65-1-f = Movie(play = "images/E-11/s05/anim/e11s05-a65-1-2x-60fps.webm", start_image = "e11s05-a65-1 mc-fucks-dd-behind-naked-anim-01")
image e11s05-a65-2 = Movie(play = "images/E-11/s05/anim/e11s05-a65-2-2x-50fps.webm", start_image = "e11s05-a65-2 mc-fucks-dd-behind-naked-anim-01")
image e11s05-a65-2-f = Movie(play = "images/E-11/s05/anim/e11s05-a65-2-2x-60fps.webm", start_image = "e11s05-a65-2 mc-fucks-dd-behind-naked-anim-01")
image e11s05-a65-3 = Movie(play = "images/E-11/s05/anim/e11s05-a65-3-2x-50fps.webm", start_image = "e11s05-a65-3 mc-fucks-dd-behind-naked-anim-01")
image e11s05-a65-3-f = Movie(play = "images/E-11/s05/anim/e11s05-a65-3-2x-60fps.webm", start_image = "e11s05-a65-3 mc-fucks-dd-behind-naked-anim-01")

image e11s05-a22-glam = Movie(play = "images/E-11/s05/anim/e11s05-a22-2x-50fps.webm", start_image = "e11s05-a22 dd-holding-cash-mct-she-really-going-to-do-it-glambot-22-000_i", image = "e11s05-a22 dd-holding-cash-mct-she-really-going-to-do-it-glambot-22-119_i", loop = False)
image e11s05-a34-glam = Movie(play = "images/E-11/s05/anim/e11s05-a34-2x-60fps.webm", start_image = "e11s05-a34 dd-screams-yes-croupier-announce-win-glambot-34-00_i", image = "e11s05-a34 dd-screams-yes-croupier-announce-win-glambot-34-77_i", loop = True)

label e11s05:

    scene black
    show screen scene_transistion(_("Next on the Bucket List"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.45, 3.0, "music")
    $ renpy.music.set_volume(0.5, 0.0, "sound5")
    play sound5 sfx_casino_ambience1 fadein 2.0
    scene e11s05-01 mc-dd-enter-casino_c1
    with Fade(0.5, 0.5, 0.9)
    queue music music_casino_cush
    pause
    scene e11s05-02 mc-makes-bond-joke-dd-comes-up-silly-name_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Young. [mcname] Young."
    play voice3 daisy_haha noloop
    dd "Does that make me Pussy von Topps?"
    scene e11s05-03 mc-thinks-dd-enough-bond-name-she-wants-ring-on-it_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "I think Daisy Diamond has a pleasant enough ring to it."
    play voice3 daisy_hmm1 noloop
    dd "If you like it then you better put a ring on it."
    scene e11s05-04 mc-lets-see-how-much-have-dd-always-be-with-him-mc-same_c1 with dissolve
    play voice2 d1s5_mchappy noloop
    mc "Let's see what I can afford after tonight."
    play voice3 daisy_thinking noloop
    dd "*Well, you should know I'll be with you no matter what fortune throws our way."
    scene e11s05-05 dd-asking-wouldnt-mc-change-he-unsure_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Same. I wouldn't change a thing."
    play voice3 lissa_thinking noloop
    dd "Wouldn't you?"
    mc "Well..."
    scene e11s05-06 mc-leads-dd-further-on-starts-lyrics-dd-rhyme-with-him_c1 with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "I wish that there were more than twenty-four hours in the day."
    play voice3 daisy_aga noloop
    dd "Even if there were forty more I wouldn't sleep a minute away."
    scene e11s05-07 mc-lists-all-games-casino-dd-tells-fortune-lost-anyway_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "There's black jack, poker, and the roulette wheel."
    mc "A fortune won and lost on every deal."
    scene e11s05-08 all-dd-needs-strong-heart-nerves-steel-mc-laughs-his-girl_c1 with dissolve
    play voice3 daisy_hey noloop
    dd "All I need is a strong heart and nerves of steel."
    play voice2 d4s4_mclaugh noloop volume 1.4
    mc "*laughs* That's my girl."
    scene e11s05-09 mc-dd-see-roulette-table_c1 with dissolve
    pause
    scene e11s05-10 dd-there-roulette-not-much-mc-just-numbers_c1 with dissolve
    play voice3 lissa_aga noloop
    dd "There it is. Doesn't look like much, does it?"
    play voice2 mc_happy_a1 noloop
    mc "It's just thirty-eight numbers."
    scene e11s05-11 dd-talks-payout-goes-towards-mc-ask-if-sure-she-absolutely_c1 with dissolve
    play voice3 lydia_thinking noloop
    dd "With a payout based on thirty-six."
    play voice2 d1s2_hmm noloop
    mc "You sure you want to do this?"
    dd "Absolutely."
    scene e11s05-12 mc-dd-join-table_c1 with dissolve
    pause
    scene e11s05-13 no-more-bets-mc-tells-missed-dd-wasnt-ready_c1 with dissolve
    play voice4 girl27_no_nouh noloop
    "Roulette Croupier" "No more bets!"
    play sound sfx_casino_roulette_start
    queue sound sfx_casino_roulette_loop loop
    play voice2 mc_disappointed_off1 noloop
    mc "I guess we won't get it on this spin."
    play voice3 daisy_uhuh noloop
    dd "I wasn't ready anyway."
    scene e11s05-14 croupier-announce-mc-tells-lot-of-money_c1 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "It is a lot of money..."
    play voice4 girl27_hey_short noloop
    "Roulette Croupier" "Double Zero!"
    scene e11s05-15 dd-all-about-timing-croupier-wants-bets-put-on-table_c1 with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    dd "It's not the money. It's the timing."
    play voice4 girl27_thinking_hmm3 noloop
    "Roulette Croupier" "Place your bets!"
    play voice2 mc_scared_oh4 noloop
    mc "How does this feel?"
    play voice3 dahlia_happy_hmm2 noloop
    dd "Wait for it."
    scene e11s05-16 sirdouchebag-appears-ask-dd-her-name-she-no_c1 with dissolve
    play voice5 boy5_hey_sexy noloop
    "Sir Douchebag" "You look so fine, you sweet thing. Tell me your name - I'm dying here."
    play voice3 dahlia_no_uhuh noloop
    dd "Uhh, no."
    scene e11s05-17 mc-right-there-douchebag-sorry_c1 with dissolve
    play voice2 mc_hey_hey4 noloop
    mc "Dude! I'm right here!"
    play voice5 boy5_surprised_oh1 noloop
    "Sir Douchebag" "Sorry brah, I didn't realize."
    scene e11s05-18 dd-ew-mc-still_c1 with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    dd "Ew."
    play voice2 mc_arrogant_hm3 noloop
    play sound sfx_casino_roulette_finish
    mc "Still."
    scene e11s05-19 croupier-announce-older-gambler-loses_c1 with dissolve
    play voice4 girl27_arrogant_ha noloop
    "Roulette Croupier" "Twenty-one, Red!"
    play voice5 boy5_angry_argh3 noloop
    "Elderly Gentleman" "Damn!"
    scene e11s05-20 dd-ask-mc-what-think-croupier-wants-bets-placed_c1 with dissolve
    play voice3 daisy_thinking noloop
    dd "What do you think, [mcname]?"
    play voice4 girl27_hey_sexy noloop
    "Roulette Croupier" "Place your bets!"
    scene e11s05-21 mc-only-one-chance-dd-tells-him-her-lucky-charm_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "You only get one chance at this. Are you sure?"
    play voice3 daisy_yes noloop
    dd "You're my lucky charm.{w} Luckier than any rabbit's foot."
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 1.5>", sfx_camera_fly1] volume 2.0 noloop
    scene e11s05-a22-glam with Dissolve(0.1)
    pause
    play voice2 mc_pain_mff1 noloop
    mct "She's really going to do it."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene e11s05-23 dd-places-big-bet-douchebag-surprised_c1 with dissolve
    play sound sfx_paper_rustl1 volume 1.5
    play voice3 dahlia_happy_hmm1 noloop
    if d19s04_dd_black is True:
        dd "Put it all on Black!"
    elif d19s04_dd_odd is True:
        dd "Put it all on Odd!"
    elif d19s04_dd_dozen is True:
        dd "Put it all on Second Dozen"
    elif d19s04_dd_corner is True:
        dd "Everything I've got on the corner bet - 17, 18, 20, and 21!"
    else:
        dd "I'm putting it all on Seventeen!"
    play voice5 boy5_surprised_geez noloop
    "Sir Douchebag" "Holy Shit!"
    scene e11s05-24 older-gambler-girl-gots-balls-dd-embarrased-thanks_c1 with dissolve
    play voice4 pete_angry_hmm2 noloop
    "Elderly Gentleman" "Damn.{w} She's got girl balls!"
    play voice3 daisy_laugh noloop
    dd "Uh, thank you, I think."
    scene e11s05-25 older-gambler-apologizes-mc-he-yesir_c1 with dissolve
    play voice4 pete_thinking_hmm1 noloop
    "Elderly Gentleman" "Excuse me, young man."
    play voice2 mc_yes_yes2 noloop
    mc "Yes? I mean, uh, yes sir?"
    scene e11s05-26 gambler-ask-mc-with-dd-he-confirms_c1 with dissolve
    play voice4 pete_thinking_emm2 noloop
    "Elderly Gentleman" "Did I hear correctly that you're attached to that lovely lady there?"
    play voice2 mc_yes_yes3 noloop
    mc "Yes, sir!"
    scene e11s05-27 gambler-doubles-bet-place-his-own-dd-wow-thanks_c1 with dissolve
    play voice4 pete_yes_ugu2 noloop
    "Elderly Gentleman" "Double her bet, and placing my own for the same."
    play voice3 daisy_impressed noloop volume 1.6
    dd "Woah! Thank you!!!"
    scene e11s05-28 mc-dont-have-do-that-gambler-buyng-something-want-mc-listen_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "You don't have to do that."
    play voice4 pete_happy_laugh1 noloop
    "Elderly Gentleman" "I'm buying something with that. I want you to listen to me, son."
    play voice2 mc_yes_okay1 noloop
    mc "Uh, okay."
    scene e11s05-29 gambler-dd-reminds-second-wife-couldnt-get-enough_c1 with dissolve
    play voice4 pete_thinking_mmf noloop
    "Elderly Gentleman" "She reminds me of my second? No... my third wife."
    "Elderly Gentleman" "She was a firecracker. I couldn't get enough of her.{w} Neither could anyone else."
    scene e11s05-30 gambler-storytime-afraid-losing-her-continues-story_c1 with dissolve
    play voice4 pete_thinking_eeh1 noloop
    "Elderly Gentleman" "I was so afraid of losing her that I drove her away."
    "Elderly Gentleman" "What I'm saying to you is this - when you find a woman like that..."
    scene e11s05-31 mc-finishes-sentence-not-let-go-gambler-agrees-totally_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    "Elderly Gentlemen" "Hold onto her as long as you can. Enjoy every moment you get with her. And when she's gone, remember her and the love you shared together."
    play voice4 pete_yes_simple1 noloop
    "Elderly Gentlemen" "Precisely, young man. I couldn't have said it better myself."
    mct "Poor guy doesn't realize how right he is."
    scene e11s05-32 mct-gambler-right-croupier-no-more-bets_c1 with dissolve
    play voice5 girl27_yes_aga3 noloop
    "Roulette Croupier" "No more bets!"
    scene e11s05-33 gambler-rooting-for-mc-he-thanks-mister_c1 with dissolve
    play voice4 pete_happy_mmm2 noloop
    "Elderly Gentlemen" "I'm rooting for you, kid."
    play voice2 mc_yes_aga2 noloop
    mc "Thank you, mister."
    play sound sfx_casino_roulette_start
    queue sound sfx_casino_roulette_loop loop volume 2.0
    scene e11s05-a34-glam with Dissolve(0.1)
    pause
    play sound sfx_casino_roulette_finish
    scene e11s05-34 dd-screams-yes-croupier-announce-win_c1 with dissolve
    play voice3 girl12_happy_woohoo1 noloop
    dd "YES!!!"
    play voice5 girl27_happy_yeah5 noloop
    "Roulette Croupier" "Seventeen, Black!"
    scene e11s05-35 mc-ask-we-won-dd-hugs-him-yes_c1 with dissolve
    play voice2 mc_surprised_huh3 noloop
    mc "We won?"
    play voice3 daisy_yay noloop
    dd "WE WON!!!"
    stop sound5 fadeout 3.0

label e11s05_later:

    scene black
    show screen scene_transistion(_("A short walk later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.6, 0.0, "sound4")
    play sound4 sfx_elevator_moving1 fadein 2.0
    scene e11s05-36 mc-dd-later-kissing-in-elevator_c1
    play sound dahlia_kiss_french1
    play voice2 d1s1_mmm noloop
    with Fade(0.5, 0.5, 0.5)
    pause
label replay_e11s05:
    if _in_replay:
        $ renpy.music.set_volume(0.6, 0.0, "sound4")
        play sound4 sfx_elevator_moving1 fadein 2.0
        $ renpy.music.set_volume(0.45, 0.0, "music")
        play music music_casino_cush
    scene e11s05-37 mc-backs-dd-against-wall-kissing-her_c1 with dissolve
    play sound maria_kiss2
    play voice3 dahlia_sex_closedmoan1 noloop
    pause
    scene e11s05-38 mc-loves-dd-she-no-underwear-mc-love-even-more_c1 with dissolve
    play voice2 d1s5b_ehhh noloop
    mc "I love you."
    play voice3 dahlia_thinking_hmm3 noloop
    dd "I'm not wearing any underwear."
    play voice2 mc_pain_rrrr noloop
    mc "And I thought I couldn't love you more!"
    scene e11s05-39 mc-hass-confession-dd-fuck-yes_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "I have a confession to make."
    play voice3 daisy_aah noloop
    dd "Fuck yes!"


    $ Lovense.stop()

    scene e11s05-40 mc-not-wearing-underwear-too-dd-noticed_c1 with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "I'm not wearing underwear either."
    play voice3 daisy_yes noloop
    dd "I noticed!!!"
    play sound sfx_fisting_fist1 volume 0.6
    $ Lovense.vibrate(5)
    scene e11s05-41 mc-puts-dick-inside-dd-pussy_c1 with dissolve
    pause
    scene e11s05-a42-1 mc-fucking-dd-standing-anim-01 with dissolve
    pause
    play voice2 d7s4_mcbreathing
    play voice3 daisy_moaning2
    play sound sfx_vagina_penetration1_fast loop volume 0.6
    $ Lovense.pattern("7;10", 1400)
    scene e11s05-a42-1
    pause
    scene e11s05-a42-2 with dissolve
    pause
    scene e11s05-a42-3 with dissolve
    pause
    scene e11s05-43 mc-tells-dd-tight-she-moans-needs-harder_c1 with dissolve
    mc "Oh fuck. You are so tight."
    dd "*moans* I think this elegant pussy just has you harder than ever."
    scene e11s05-44 mc-says-gorgeous-loves-pussy-dd-wants-elegant-pussy-fucked_c1 with dissolve
    mc "You are gorgeous, from head-to-toe. And yes I love your fucking elegant pussy."
    dd "Yes! Fuck my elegant pussy!"
    $ Lovense.pattern("7;10", 700)
    scene e11s05-a42-1-f with dissolve
    pause
    scene e11s05-a42-2-f with dissolve
    pause
    scene e11s05-a42-3-f with dissolve
    pause
    stop voice2 fadeout 1.0
    stop sound fadeout 1.0
    play voice3 daisy_scream7 noloop
    $ Lovense.stop()
    $ Lovense.vibrate(7)
    scene e11s05-45 dd-cums-while-mc-fucking-her-perfect-man_c1 with vpunch
    dd "Oh fuck! Mrrrm... ah.. oouh... ah!"
    queue voice3 daisy_scream3 noloop
    dd "You are my perfect man."
    play voice2 mc_thinking_mmm2 noloop
    mc "Thank you."
    scene e11s05-46 dd-stops-wait-mc-ask-what-she-wants-taste-her-juice_c1 with dissolve
    $ Lovense.vibrate(2)
    play voice3 daisy_oof noloop
    dd "Wait."
    play voice2 mc_thinking_hmm3 noloop
    mc "Why?"
    dd "I want to taste myself on you."
    play sound sfx_kick_leg1
    scene e11s05-47 dd-pushes-mc-against-wall_c1 with dissolve
    pause
    scene e11s05-48 dd-takes-off-dress_c1 with dissolve
    play voice3 daisy_hmm2 noloop
    pause
    play sound sfx_skirt_off2
    scene e11s05-49 mc-kneels-to-suck-mc-cock_c1 with dissolve
    pause
    scene e11s05-50 dd-puts-mc-dick-in-mouth_c1 with dissolve
    $ Lovense.vibrate(7)
    play voice3 daisy_dlick noloop volume 2.5
    pause
    scene e11s05-a51-1 dd-bj-mc-anim-01 with dissolve
    play voice3 daisy_sucking
    play voice2 d7s4_mcbreathing
    pause
    $ Lovense.pattern("7;10", 1400)
    scene e11s05-a51-1
    pause
    scene e11s05-a51-2 with dissolve
    pause
    scene e11s05-a51-3 with dissolve
    pause
    scene e11s05-52 mc-lets-dd-know-perfect-woman-beyond-perfect_c1 with dissolve
    mc "You should know - you aren't my perfect woman."
    mc "You are beyond perfect."
    scene e11s05-53 dd-slurping-sounds-mc-used-to-imagine-perfect-woman_c1 with dissolve
    dd "Wlrrrup... Mrllluhp..."
    mc "I used to imagine... I thought I knew what I wanted in a perfect woman."
    mc "You are so far beyond that."
    play voice3 aaleyah_sucking_deep
    $ Lovense.pattern("7;10", 700)
    scene e11s05-a51-1-f with dissolve
    pause
    scene e11s05-a51-2-f with dissolve
    pause
    scene e11s05-a51-3-f with dissolve
    pause
    scene e11s05-54 mc-couldnt-dream-woman-like-dd-doesnt-believe-his-luck_c1 with dissolve
    mc "I couldn't have dreamed of meeting a woman like you."
    mc "I can barely believe my luck to be with you."
    stop voice2 fadeout 1.0
    scene e11s05-55 mc-pov-dd-looks-up-mc-incredible-needs-fuck-now_c1 with dissolve
    $ Lovense.stop()
    $ Lovense.vibrate(5)
    play voice3 daisy_aah noloop
    dd "You are incredible."
    dd "I need you to fuck me now."
    scene e11s05-56 dd-bends-over-wall_c1 with dissolve
    pause
    stop sound4 fadeout 1.5
    play sound sfx_elevator_ding1
    $ renpy.music.set_volume(1.0, 0.0, "sound3")
    play sound3 sfx_elevator_door_closed1 noloop
    scene e11s05-57 mc-puts-dick-inside-dd-door-dings_c1 with dissolve
    play voice2 d1s5_orgasm noloop
    pause
    scene e11s05-58 door-opens-old-lady-sees-them-fucking_c1 with dissolve
    play voice4 girl27_scared_ah3 noloop
    "Little Old Lady" "Oh my!"
    play voice2 mc_pain_ou1 noloop
    mc "Oh, shit!"
    scene e11s05-59 dd-asking-mc-why-stop-old-lady-dont-stop_c1 with dissolve
    play voice3 dahlia_sex_closedmoan5 noloop
    dd "What is it? Why did you stop?"
    play voice4 girl27_arrogant_hm1 noloop
    "Little Old Lady" "Don't stop, young man. I've seen everything already."
    scene e11s05-60 mct-what-old-lady-wont-bother-them_c1 with dissolve
    play voice2 mc_pain_mff3 noloop
    mct "What?!"
    play voice4 girl27_disappointed_mmm noloop
    "Little Old Lady" "I'm just going to ride down with you two. Don't bother about me in the slightest."
    scene e11s05-61 dd-ask-if-serious-mc-suggest-they-get-dressed_c1 with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    dd "Are you serious? I mean..."
    play voice2 d2s12_emmm noloop
    mc "We should probably get dressed."
    scene e11s05-62 dd-wants-to-finish-mc-dont-mind_c1 with dissolve
    play voice3 daisy_uhuh noloop
    dd "I mean, she's okay with it. I'm okay with it. Finish."
    play voice2 mc_surprised_what1 noloop
    mc "Really? I mean, I don't mind having an audience."
    scene e11s05-63 dd-watched-mc-samiya-mc-ask-if-sure_c1 with dissolve
    play voice3 dahlia_yes_ugu noloop
    dd "I know - I watched you wrestle Samiya."
    play voice2 mc_scared_oh2 noloop
    mc "Are you sure?"
    play sound4 sfx_elevator_moving1 fadein 2.0
    play sound sfx_elevator_door_closed1
    scene e11s05-64 mc-lifts-dd-leg-starts-fucking-again_c1 with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    dd "I don't mind showing off a little."
    play voice2 mc_angry_errr4 noloop
    mc "Enough said!"
    scene e11s05-a65-1 mc-fucks-dd-behind-naked-anim-01 with dissolve
    pause
    play voice2 [mc_pain_mff1, "<silence 2.0>", mc_pain_mff2, "<silence 2.0>", mc_pain_mff4, "<silence 2.0>", mc_pain_mff3, "<silence 2.0>", mc_pain_mff5, "<silence 2.0>"]
    play voice3 daisy_sex_closedmoans1
    play sound sfx_vagina_penetration1_fast loop volume 0.6
    $ Lovense.pattern("7;12", 1400)
    scene e11s05-a65-1
    pause
    scene e11s05-a65-2 with dissolve
    pause
    scene e11s05-a65-3 with dissolve
    pause
    scene e11s05-66 dd-breathless-wants-it-mc-being-sucked-dd-pussy_c1 with dissolve
    play voice2 d7s4_mcbreathing
    play voice3 daisy_moaning2
    dd "*breathless* Come on. Give it to me baby!"
    mc "Daisy. Your pussy is sucking me so hard it almost hurts!"
    play voice2 [mc_pain_mff1, "<silence 2.0>", mc_pain_mff2, "<silence 2.0>", mc_pain_mff4, "<silence 2.0>", mc_pain_mff3, "<silence 2.0>", mc_pain_mff5, "<silence 2.0>"]
    play voice3 daisy_sex_closedmoans1
    $ Lovense.pattern("7;12", 700)
    scene e11s05-a65-1-f with dissolve
    pause
    scene e11s05-a65-2-f with dissolve
    pause
    scene e11s05-a65-3-f with dissolve
    pause
    play voice2 d7s4_mcbreathing
    play voice3 daisy_moaning2
    scene e11s05-67 dd-wants-keep-going-cant-talk-straight_c1 with dissolve
    dd "Yes! Keep going!! Give me your best shot!!!"
    dd "Ohurraaah! Fuck That Tight Twat!!"
    scene e11s05-67-01 old-lady-watching-mc-fuck-dd_c1 with dissolve
    pause
    scene e11s05-68 mc-cock-closeup-while-he-talks-with-ly_c1
    show memory-overlay
    with dissolve
    play voice4 girl28_surprised_what noloop
    ly "({i}Wait... are you saying that you and mom had sex while a little old lady watched?{/i})"
    play voice5 mc_yes_yeah5 noloop
    mct "Well, yeah."
    play voice4 girl28_disgust_oeagh2 noloop
    ly "({i}Why are you telling me this???{/i})"
    play voice5 mc_arrogant_huh2 noloop
    mct "You don't want to know how you were conceived?"
    play voice4 girl28_disgust_boeagh noloop
    ly "({i}What?! Ew, gross!{/i})"
    play voice5 mc_happy_hah1 noloop
    mct "I'm just kidding.{w} That was several months later."
    scene e11s05-69 old-lady-talks-about-her-husband-dd-about-to-orgasm_c1 with dissolve
    play voice4 girl27_thinking_mmm noloop
    "Little Old Lady" "Don't you worry about a thing, young couple."
    scene e11s05-69-01 old-lady-talks-about-her-husband-dd-about-to-orgasm-old-lady-pov_c1 with dissolve
    "Little Old Lady" "If my George was still alive - and we were forty years younger - we'd be right there slamming against the walls next to you."
    "Little Old Lady" "Although, George was fond of buggering, so he'd probably sodomize me..."
    stop sound4 fadeout 1.5
    play sound sfx_elevator_ding1
    play sound3 sfx_elevator_door_closed1 noloop volume 0.5
    scene e11s05-70 door-opens-old-lady-leaves_c1 with dissolve
    play voice5 sfx_elevator_lobbylevel noloop
    "Automated Voice" "Lobby Level"
    play voice4 girl27_happy_relief3 noloop
    "Little Old Lady" "Farewell, young couple."
    play voice3 jessie_cumming1 noloop
    play voice2 d1s5_orgasm2 noloop
    $ Lovense.stop()
    $ Lovense.vibrate(17)
    scene e11s05-71 dd-mc-both-cum-together_c1 with vpunch
    dd "ASKDJUHFBASDFASD!!!"
    $ Lovense.vibrate(18)
    play voice2 mc_angry_errr4 noloop
    with hpunch
    mc "FUUUCKKCKKKK YESSSSS!!!!"
    play sound sfx_spitcum1 volume 0.6
    scene e11s05-72 mc-drips-cum-from-dd-pussy_c1 with dissolve
    $ Lovense.vibrate(3)
    queue voice3 polly_breathing noloop
    dd "Best. Creampie. Ever."
    play voice2 mc_yes_yeah1 noloop
    mc "I couldn't agree more."
    $ unlock_gallery_slot("scene", "e11s05")
    scene e11s05-73 dd-looking-confused-old-lady-stole-her-dress_c1 with dissolve
    play voice3 daisy_thinking noloop
    dd "Hon-"
    play voice2 d9s2_mcyes noloop volume 2.5
    mc "Yes, Love?"
    play voice3 daisy_oof noloop
    dd "I think that little old lady stole my dress when she left."
    scene e11s05-74 mc-calls-her-bugger-dd-agrees_c1 with dissolve
    $ Lovense.vibrate(1)
    play voice2 mc_angry_errr2 noloop
    mc "That dirty old bugger."
    play voice3 dahlia_disappointed_hmm1 noloop
    dd "Yeah."
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "Well then, it's good that I held onto our winnings."
    scene e11s05-75 mc-dd-laugh-end-scene_c1 with dissolve
    play voice3 dahlia_happy_laugh3 noloop
    dd "*laughing* True, let's go shopping!"
    play voice2 d4s4_mclaugh noloop volume 1.7
    mc "*laughing* Let's go up to our room first."

    $ Lovense.stop()


    $ renpy.end_replay()

    stop music fadeout 3.0
    jump e11s06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
