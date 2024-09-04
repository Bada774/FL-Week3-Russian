image e17s06-a41-1 = Movie(play = "images/E-17/s06/anim/e17s06-a41-1-2x-50fps.webm", start_image = "e17s06-a41-1 mc-fingers-dw-suck-tit-anim-01")
image e17s06-a41-1-f = Movie(play = "images/E-17/s06/anim/e17s06-a41-1-2x-60fps.webm", start_image = "e17s06-a41-1 mc-fingers-dw-suck-tit-anim-01")
image e17s06-a41-2 = Movie(play = "images/E-17/s06/anim/e17s06-a41-2-2x-50fps.webm", start_image = "e17s06-a41-2 mc-fingers-dw-suck-tit-anim-01")
image e17s06-a41-2-f = Movie(play = "images/E-17/s06/anim/e17s06-a41-2-2x-60fps.webm", start_image = "e17s06-a41-2 mc-fingers-dw-suck-tit-anim-01")
image e17s06-a41-3 = Movie(play = "images/E-17/s06/anim/e17s06-a41-3-2x-50fps.webm", start_image = "e17s06-a41-3 mc-fingers-dw-suck-tit-anim-01")
image e17s06-a41-3-f = Movie(play = "images/E-17/s06/anim/e17s06-a41-3-2x-60fps.webm", start_image = "e17s06-a41-3 mc-fingers-dw-suck-tit-anim-01")

image e17s06-a63-1 = Movie(play = "images/E-17/s06/anim/e17s06-a63-1-2x-50fps.webm", start_image = "e17s06-a63-1 mc-mask-anal-anim-01")
image e17s06-a63-1-f = Movie(play = "images/E-17/s06/anim/e17s06-a63-1-2x-60fps.webm", start_image = "e17s06-a63-1 mc-mask-anal-anim-01")
image e17s06-a63-2 = Movie(play = "images/E-17/s06/anim/e17s06-a63-2-2x-50fps.webm", start_image = "e17s06-a63-2 mc-mask-anal-anim-01")
image e17s06-a63-2-f = Movie(play = "images/E-17/s06/anim/e17s06-a63-2-2x-60fps.webm", start_image = "e17s06-a63-2 mc-mask-anal-anim-01")
image e17s06-a63-3 = Movie(play = "images/E-17/s06/anim/e17s06-a63-3-2x-50fps.webm", start_image = "e17s06-a63-3 mc-mask-anal-anim-01")
image e17s06-a63-3-f = Movie(play = "images/E-17/s06/anim/e17s06-a63-3-2x-60fps.webm", start_image = "e17s06-a63-3 mc-mask-anal-anim-01")

image e17s06-a78-1 = Movie(play = "images/E-17/s06/anim/e17s06-a78-1-2x-50fps.webm", start_image = "e17s06-a78-1 dw-mc-sixty-nine-anim-01")
image e17s06-a78-1-f = Movie(play = "images/E-17/s06/anim/e17s06-a78-1-2x-60fps.webm", start_image = "e17s06-a78-1 dw-mc-sixty-nine-anim-01")
image e17s06-a78-2 = Movie(play = "images/E-17/s06/anim/e17s06-a78-2-2x-50fps.webm", start_image = "e17s06-a78-2 dw-mc-sixty-nine-anim-01")
image e17s06-a78-2-f = Movie(play = "images/E-17/s06/anim/e17s06-a78-2-2x-60fps.webm", start_image = "e17s06-a78-2 dw-mc-sixty-nine-anim-01")

image e17s06-a84-1 = Movie(play = "images/E-17/s06/anim/e17s06-a84-1-2x-50fps.webm", start_image = "e17s06-a84-1 mc-fucks-dw-anal-cow-anim-01")
image e17s06-a84-1-f = Movie(play = "images/E-17/s06/anim/e17s06-a84-1-2x-60fps.webm", start_image = "e17s06-a84-1 mc-fucks-dw-anal-cow-anim-01")
image e17s06-a84-2 = Movie(play = "images/E-17/s06/anim/e17s06-a84-2-2x-50fps.webm", start_image = "e17s06-a84-2 mc-fucks-dw-anal-cow-anim-01")
image e17s06-a84-2-f = Movie(play = "images/E-17/s06/anim/e17s06-a84-2-2x-60fps.webm", start_image = "e17s06-a84-2 mc-fucks-dw-anal-cow-anim-01")
image e17s06-a84-3 = Movie(play = "images/E-17/s06/anim/e17s06-a84-3-2x-50fps.webm", start_image = "e17s06-a84-3 mc-fucks-dw-anal-cow-anim-01")
image e17s06-a84-3-f = Movie(play = "images/E-17/s06/anim/e17s06-a84-3-2x-60fps.webm", start_image = "e17s06-a84-3 mc-fucks-dw-anal-cow-anim-01")

image e17s06-a26-glam = Movie(play = "images/E-17/s06/anim/e17s06-a26-01-2x-50fps.webm", start_image = "e17s06-a26-01 dw-enters-room-in-bdsm-outfit-glambot-26-01-00_i", image = "e17s06-a26-01 dw-enters-room-in-bdsm-outfit-glambot-26-01-78_i", loop = False)

label e17s06:

    scene black
    show screen scene_transistion(_("Months Later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_dishes_slicing1 loop fadein 2.0
    scene e17s06-01 establish-shot-mc-cooking-kitchen_c1
    with Fade(0.5, 0.5, 0.9)
    $ renpy.music.set_volume(0.6, 3.0, "music")
    queue music music_ooh_positive
    pause
    play sound sfx_door_open1
    scene e17s06-02 mc-looks-at-door_c1 with dissolve
    play voice2 mc_surprised_huh4 noloop
    "*door opening*"
    scene e17s06-03 dw-opens-door-says-home-ask-about-mess_c1 with dissolve
    play sound sfx_door_closed2
    play voice3 dahlia_hey_angry noloop
    dw "I'm home."
    dw "You making a mess in here?"
    scene e17s06-04 mc-glass-obcures-pregnancy-orderly-cooking-dw-good_c1 with dissolve
    play voice2 mc_no_nope1 noloop
    mc "Nope. Very orderly cooking."
    play voice3 dahlia_thinking_hmm2 noloop
    dw "Good."
    play sound sfx_cup_slide1
    scene e17s06-05 mc-gives-glass-dw-reveals-pregnancy_c1 with dissolve
    pause
    scene e17s06-06 mc-hey-momma-dw-prefers-mistress_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hey, Momma."
    play voice3 dahlia_old_argh2 noloop
    dw "You know I prefer \"Mistress\", [mcname]."
    scene e17s06-07 mc-not-playing-yet-dw-always-playing_c1 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "We're not playing yet, Dahlia."
    play voice3 dahlia_old_laugh1 noloop
    dw "I'm always playing with you, you know that."
    scene e17s06-08 mc-returns-cooking-ask-happy-dw-owes-to-dd_c1 with dissolve
    play voice2 d1s5_mchappy noloop
    mc "Happy to be done?"
    play voice3 dahlia_disappointed_hmm1 noloop
    dw "I could have gone an extra week. I owe it to Daisy."
    scene e17s06-09 dw-runs-finger-mc-back-he-talks_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "The fact that you think that tells me right now was the perfect time for you."
    mc "It's going to take you the whole weekend just to properly change course from a hard-working marathon into maternity leave mode."
    scene e17s06-10 dw-tease-him-calls-worthless-mct-she-misses-slave_c1 with dissolve
    play voice3 dahlia_angry_oh noloop
    dw "I like my work. We can't all be worthless busybodies like you.."
    mct "I think she really misses calling me \"slave\"."
    play sound sfx_cucumber_bite1
    scene e17s06-11 dw-starts-eating-pickle-with-peanutbutter_c1 with dissolve
    pause
    scene e17s06-12 mc-jokes-who-disgusting-now-she-tells-he-made-her_c1 with dissolve
    play voice2 mc_disgust_meh4 noloop
    mc "And you always said I was the disgusting one."
    play voice3 dahlia_yes_yeah3 noloop
    dw "You made me like this."
    scene e17s06-13 mc-no-regrets_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.3
    mc "Hashtag \"no regrets\"."
    play sound dahlia_kiss_french1
    scene e17s06-14 dw-mc-kiss_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    pause
    scene e17s06-15 dw-sultry-look_c1 with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    dw "Mmm."
    scene e17s06-16 dw-puts-hands-on-belly-complain-mc-chuckles_c1 with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    dw "You should know, your brat wouldn't behave at all today."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh... {i}my{/i} child misbehaving? How odd?"
    scene e17s06-17 dw-takes-bite-pickle-says-mhm_c1 with dissolve
    play voice3 dahlia_yes_ugu noloop
    dw "Mmhmm."
    scene e17s06-18 dw-hand-belly-baby-kicked-twice_c1 with dissolve
    play voice3 dahlia_yes_yeah2 noloop
    dw "Yup. Damn kid kicked me twice during some of my meetings."
    dw "We- We will have to put down a very strict set of rules for the brat to follow once they're here."
    scene e17s06-19 mc-touches-dw-belly_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "If they take after you, I'm not sure they'll like that."
    scene e17s06-20 dw-enough-talk-gremlin_c1 with dissolve
    play voice3 dahlia_arrogant_heh noloop
    dw "Enough gremlin talk. Your Mistress-"
    scene e17s06-21 dw-expression-softens-needs-something-mc-listening_c1 with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    dw "I need something from you."
    play voice2 mc_yes_sure1 noloop
    mc "I'm listening."
    scene e17s06-22 dw-ask-to-play-with-mc_c1 with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    dw "Your Mistress would like to play with you. Okay?"
    scene e17s06-23 mc-smiles_c1 with dissolve
    pause
    scene e17s06-24 mc-points-to-cooking-tells-after-dinner-dw-dissapointed_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "After dinner."
    play voice3 dahlia_happy_hmm1 noloop
    dw "Okay. After dinner."

    jump e17s06_later

label e17s06_later:

    scene black
    show screen scene_transistion(_("Later that evening"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene e17s06-25 later-mc-reads-book-bedroom_c1
    with Fade(0.5, 0.5, 0.9)
    pause
label replay_e17s06:

    if _in_replay:
        $ renpy.music.set_volume(0.6, 0.0, "music")
        play music music_ooh_positive
    scene e17s06-26 dw-enters-room-in-bdsm-outfit_c1 with dissolve
    pause
    play sound sfx_heels_steps1_slow
    scene e17s06-a26-glam with dissolve
    pause
    stop sound fadeout 1.0
    scene e17s06-27 dw-ask-mc-everything-alright_c1 with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    dw "How are you doing? Seriously?"
    scene e17s06-28 mct-blood-gone-south_c1 with dissolve
    play voice2 d1s1_mmm noloop
    mct "Well, all the blood just ran down south, so there is that."
    scene e17s06-29 all-good-has-clean-bill-health_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Everything is good. You're worrying about nothing."
    mc "Last checkup, the doctor gave me a clean bill of health."
    scene e17s06-30 mc-points-dw-should-be-careful-she-will-judge_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "It's you who needs the most care now."
    play voice3 dahlia_arrogant_ha noloop
    dw "I'll be the judge of that."
    play sound sfx_cloth_rustling4
    scene e17s06-32 dw-mad-herself-what-did-unforgivable_c1 with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    dw "If you wanted to switch places, you would know just how fun it is to have a kid kicking you throughout the day."
    dw "Sometimes I think, this is your little revenge."
    scene e17s06-31 dw-sits-next-mc-sighs_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "This again?"
    play voice3 dahlia_pain_sobs noloop
    dw "I know I know."
    dw "*sniff* But what I did. It was unforgivable."
    scene e17s06-33 mc-puts-shoulder-dw-shoulder-forgiven-dw-worried-kids_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "And I forgave you. Many times now. Our child is just... showing how strong they're going to be."
    play voice3 dahlia_sex_closedmoan1 noloop
    dw "What if they turn out as bad as me?"
    play voice2 mc_no_noway noloop
    mc "No one is as bad as you."
    scene e17s06-34 mc-noone-bad-as-dw-she-laughs_c1 with dissolve
    play voice3 dahlia_happy_laugh6 noloop
    dw "*laughs*"
    scene e17s06-35 dw-wipes-tear-wants-mc-cock_c1 with dissolve
    play voice3 allison_pain_sniff1 noloop
    dw "*sniffles* You cock."
    dw "Enough baby talk. Your Mistress has an itch for you to scratch."
    scene e17s06-36 mc-ask-if-dw-sure-she-nods_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Are you sure about that."
    play voice3 dahlia_yes_simple noloop
    dw "Never been more sure of anything in my life, peabrain. Let's play."
    scene e17s06-37 mc-game-face-on-absoleutly_c1 with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "Absolutely."
    scene e17s06-38 mc-on-knees-yes-mistress_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "Mistress, may I please you."


    $ Lovense.stop()

    scene e17s06-39 dw-plays-tit-slim-chance-mc-satisfy-mc-bows-head_c1 with dissolve
    play voice3 dahlia_yes_angry noloop
    dw "Yes. I've had a long day. And there is a slim chance you could satisfy me."
    play voice2 mc_yes_ugu1 noloop
    mc "Of course, Mistress. Yet that is my only purpose."
    play sound sfx_skirt_off2
    $ Lovense.vibrate(3)
    scene e17s06-a41-1 mc-fingers-dw-suck-tit-anim-01 with dissolve
    pause
    play sound2 sfx_vagina_penetration1_fast volume 0.5
    play voice2 mc_sex_sucking_slow1
    play voice3 dahlia_sex_openmoans2
    $ Lovense.pattern("5;8", 1400)
    scene e17s06-a41-1
    pause
    scene e17s06-a41-2 with dissolve
    pause
    scene e17s06-a41-3 with dissolve
    pause
    dw "Stop teasing me. You know I hate waiting!"
    $ Lovense.pattern("5;8", 700)
    scene e17s06-a41-1-f with dissolve
    dw "Bhuraah... what are you doing to me?"
    pause
    scene e17s06-a41-2-f with dissolve
    mc "*hungry sucking*"
    pause
    scene e17s06-a41-3-f with dissolve
    pause
    stop sound2 fadeout 1.0
    stop voice2 fadeout 1.0
    scene e17s06-43 dw-calls-mc-idiot-milk-for-kids-mc-just-borrowing_c1 with dissolve
    $ Lovense.stop()
    $ Lovense.vibrate(3)
    play voice3 dahlia_angry_argh2 noloop
    dw "Idiot. That milk isn't for you. It's for the brat."
    play voice2 mc_thinking_emm1 noloop
    mc "I think they'll survive if I borrow a little."
    scene e17s06-44 mc-tells-dw-gotten-big-she-moans_c1 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "I love how big they've gotten, Mistress."
    play voice3 dahlia_old_moan1 noloop
    dw "Nrrwaaah..."
    scene e17s06-45 dw-shut-up-talks-mom-tits_c1 with dissolve
    play voice3 dahlia_old_moan2 noloop
    dw "Shut up. Damn. I never expected to get Mom Tits so quickly."
    queue voice3 dahlia_old_orgasm2 noloop
    dw "Butaah... Nrrrn... Stupid weak, pregnant body. Why does it feel so good?"
    play sound sfx_cloth_rustling2
    scene e17s06-46 dw-moves-away-from-mc_c1 with dissolve
    play voice3 dahlia_angry_oof noloop
    dw "Such a bad boy. You need to be punished."
    scene e17s06-47 dw-walks-towards-dresser-tells-mc-follow-her_c1 with dissolve
    play voice3 dahlia_angry_hm1 noloop
    dw "Come along, pet."
    play sound sfx_jeans_on1
    scene e17s06-48 dw-bends-open-dresser-mc-takes-off-pants_c1 with dissolve
    pause
    play sound sfx_cloth_rustling3
    scene e17s06-49 dw-puts-mask-mc_c1 with dissolve
    pause
    scene e17s06-50 dw-gests-behind-mc-ask-if-wants-get-hard-mc-nods_c1 with dissolve
    play voice3 dahlia_arrogant_yeah noloop
    dw "Good boy. You want to get hard, don't you?"
    play voice2 mc_undermask_orgasm noloop
    mc "Yes, Mistress."
    play sound sfx_handjob_cream1 loop
    scene e17s06-51 dw-gets-mc-hard_c1 with dissolve
    play voice2 mc_undermask_breathing
    play voice3 dahlia_happy_hmm2 noloop
    pause
    stop voice2 fadeout 1.0
    stop sound fadeout 1.0
    scene e17s06-52 dw-walks-around-mc_c1 with dissolve
    play voice3 dahlia_disgust_oeah noloop
    dw "So insufferable. Getting off on your Mistress humiliating you. Degrading you."
    scene e17s06-53 dw-standing-front-mc-all-hers-wants-see-his-erection_c1 with dissolve
    play voice3 dahlia_angry_hm2 noloop
    dw "You're all mine."
    dw "All mine. Now hurry up and show me your pathetic excuse for an erection."
    scene e17s06-54 dw-inspecting-mc-cock-aroused-biting-finger_c1 with dissolve
    play voice3 dahlia_disgust_oof noloop
    dw "Shit. For a second there, it almost looked like you had a big, thick cock."
    play sound sfx_biologic_spit1
    scene e17s06-55 dw-spits-mc-cock_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "It's cool. I can take it."
    scene e17s06-56 dw-rubs-mc-cock_c1 with dissolve
    play voice2 mc_pain_rrrr noloop
    mct "Fuck Dahlia, even pregnant, you know just where to hit."
    play voice3 dahlia_thinking_hmm1 noloop
    dw "But it must have just been a trick of the light. I have nothing to worry about."
    scene e17s06-57 mc-ask-how-look-dw-fav-worm_c1 with dissolve
    play voice3 dahlia_disgust_meh noloop
    dw "This slab of meat just takes up space. It has no use. I'm sure it could never make a woman like me feel anything other than disgust."
    play voice2 mc_pain_mff1 noloop
    mct "Holy fuck. She hasn't lost her touch. She's going to break me."
    scene e17s06-58 dw-looks-down-mc-dick-second-fav-worm_c1 with dissolve
    play voice3 dahlia_old_argh noloop
    dw "On the bed, worm!"
    scene e17s06-59 dw-instructs-mc-position_c1 with dissolve
    play voice3 dahlia_arrogant_huh noloop
    dw "Legs spread, yes that it. It's time to see just how strong that tool of yours is."
    scene e17s06-60 dw-climbs-mc-already-knocked-no-use_c1 with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    dw "Now... give me your stupid dick. It already knocked me up once."
    dw "I don't think it has any more use to me."
    play sound sfx_fisting_fist2
    scene e17s06-61 mc-yes-mistress-puts-cock-inside-dw-ass_c1 with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Yes, Mistress."
    scene e17s06-62 dw-forgotten-mc-size-he-thinks-she-tight_c1 with dissolve
    play voice2 mc_pain_mff2 noloop
    play voice3 dahlia_old_moan3 noloop
    mct "Fuck she's tight. With the mask and how tight her asshole is, I need to be careful."
    $ Lovense.pattern("7;12", 1400)
    scene e17s06-a63-1 with dissolve
    play voice2 mc_undermask_breathing
    play voice3 dahlia_sex_openmoans2
    play sound2 sfx_vagina_penetration1_fast volume 0.5
    pause
    scene e17s06-a63-2 with dissolve
    pause
    scene e17s06-a63-3 with dissolve
    pause
    dw "*hisses* I like that."
    dw "Fuck my tight hole. Make your Mistress really feel it, peabrain!"
    play sound3 sfx_sex_bodyslaps1
    $ Lovense.pattern("7;12", 700)
    scene e17s06-a63-1-f with dissolve
    dw "*moaning* Fuck, I've gotten so sensitive after getting pregnant!"
    pause
    play sound3 sfx_sex_bodyslaps1
    scene e17s06-a63-2-f with dissolve
    pause
    play sound3 sfx_sex_bodyslaps1
    scene e17s06-a63-3-f with dissolve
    pause
    mct "I have to give her the signal."
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene e17s06-66 mc-has-give-signal-grunts-three-times_c1 with dissolve
    $ Lovense.stop()
    $ Lovense.vibrate(3)
    play voice2 mc_undermask_orgasm2 noloop
    mc "*grunts three times in order*"
    scene e17s06-67 dw-removes-hand-mc-nose-ask-everything-okay_c1 with dissolve
    play voice3 dahlia_old_moan2 noloop
    dw "*panting* Ahwuah. One second."
    dw "Everything okay?"
    scene e17s06-68 mc-enough-breathplay-dw-okay-not-done-punishing_c1 with dissolve
    play voice2 mc_undermask_orgasm noloop
    mc "Think I'm good for breathplay tonight, Mistress."
    play voice3 dahlia_thinking_oh noloop
    dw "Very well. But that doesn't mean I'm done punishing you."
    scene e17s06-69 dw-removes-mc-mask_c1 with dissolve
    play voice2 mc_undermask_hah2 noloop
    mc "Of course."
    play sound sfx_cloth_planket2
    scene e17s06-70 dw-shows-cock-ring-tells-mc-get-ready_c1 with dissolve
    play voice3 dahlia_old_laugh1 noloop
    dw "Get ready."
    play sound sfx_sextoy_cuff2
    $ Lovense.vibrate(8)
    scene e17s06-71 dw-puts-cockring-mc-tightens-it_c1 with dissolve
    play voice2 mc_pain_mff5 noloop
    mct "Mother of god. This is why you put the ring on earlier."
    scene e17s06-72 mc-groans-dw-ask-everything-alright_c1 with dissolve
    play voice2 mc_pain_argh1 noloop
    mc "Hurrraaahh..."
    play voice3 dahlia_thinking_hmm3 noloop
    dw "Everything alright, my pet?"
    scene e17s06-73 mc-answers-all-good-thinks-at-least-not-cock-cage_c1 with dissolve
    $ Lovense.vibrate(3)
    play voice2 d3s7_mcemm noloop
    mc "Perfect. No problem."
    mct "At least it's not another cock cage."
    scene e17s06-74 dw-happy-good_c1 with dissolve
    play voice3 dahlia_arrogant_hm noloop
    dw "Good!"
    scene e17s06-75 dw-gets-sixty-nine-position_c1 with dissolve
    pause
    scene e17s06-76 dw-takes-mc-cock_c1 with dissolve
    play voice3 dahlia_old_moan1 noloop
    pause
    scene e17s06-77 mc-starts-licking-dw_c1 with dissolve
    play voice2 mc_sex_sucking_slow1
    pause
    $ Lovense.pattern("7;10", 1400)
    scene e17s06-a78-1 with dissolve
    play voice3 dahlia_sex_openmoans2
    pause
    scene e17s06-a78-2 with dissolve
    pause
    dw "Get to work. My pussy is not going to please itself!"
    dw "Mrraah... not bad."
    $ Lovense.pattern("7;10", 700)
    scene e17s06-a78-1-f with dissolve
    dw "Too bad I can't play with your cock right now. That would be like torture."
    mct "Just keep licking. Just keep licking."
    dw "That's it. Swirl that tongue around. God. You're tongue-fucking me like my pussy is your last scoop of ice cream..."
    scene e17s06-a78-2-f with dissolve
    mct "Spirits, have mercy on my cock!"
    dw "Nrrahwaaaah!"
    stop voice2 fadeout 1.0
    stop voice3 fadeout 1.0
    scene e17s06-82 dw-positions-herself-for-anal_c1 with fade
    pause
    scene e17s06-a84-1 mc-fucks-dw-anal-cow-anim-01 with dissolve
    pause
    $ Lovense.pattern("7;14", 1400)
    scene e17s06-a84-1
    play sound2 sfx_vagina_penetration1_fast volume 0.5
    play voice2 d7s4_mcbreathing
    play voice3 dahlia_sex_openmoans1
    pause
    scene e17s06-a84-2 with dissolve
    pause
    scene e17s06-a84-3 with dissolve
    pause
    mct "Her ass is throbbing."
    mct "Who is going to break first?"
    play sound3 sfx_sex_bodyslaps1
    $ Lovense.pattern("7;15", 700)
    scene e17s06-a84-1-f with dissolve
    pause
    dw "*moaning and panting*"
    play sound3 sfx_sex_bodyslaps1
    scene e17s06-a84-2-f with dissolve
    pause
    dw "Don't hold back, worm."
    dw "I want it so badly."
    play sound3 sfx_sex_bodyslaps1
    scene e17s06-a84-3-f with dissolve
    pause
    dw "Break this bad momma's asshole!"
    dw "You know how bad you want it."
    play voice3 dahlia_sex_orgasming1
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(18)
    scene e17s06-89 dw-cant-hold-more-cums-hard_c1 with vpunch
    dw "Oh fuck. No... You're making me..."
    play voice3 dahlia_old_orgasm1 noloop
    play sound sfx_squirt1
    $ Lovense.vibrate(19)
    scene e17s06-90 dw-screams-and squirts_c1 with vpunch
    dw "*screaming blissfully*"
    queue voice3 dahlia_sex_orgasming2
    scene e17s06-91 dw-wants-mc-cum-he-obeys_c1 with dissolve
    dw "Oh god, [mcname]!"
    dw "Cum. I want you to cum. For meuuaaah!"
    mc "Yes, Mistress!"
    stop voice3 fadeout 1.0
    scene e17s06-92 dw-positions-herself_c1 with dissolve
    pause
    play voice2 d1s5_orgasm2 noloop
    play voice3 dahlia_pain_ah1 noloop
    play sound mc_cum_sound1
    $ Lovense.vibrate(20)
    scene e17s06-93 mc-cums-little_c1 with vpunch
    pause
    scene e17s06-94 dw-takes-rest-of-mc-cum-gulps-down_c1 with dissolve
    $ Lovense.vibrate(18)
    play voice3 dahlia_sex_closedmoan5 noloop
    dw "Mrrrmmmm."
    play sound [audio.gulp, "<silence 0.15>", audio.gulp, "<silence 0.15>", audio.gulp]
    dw "*gulp. gulp. gulp*"
    scene e17s06-95 dw-licks-mc-dick-clean_c1 with dissolve
    play voice3 dahlia_sex_closedmoan1 noloop
    dw "Mlllrrmmm."
    scene e17s06-96 dw-takes-cockring-off-cleans-lips_c1 with dissolve
    $ Lovense.vibrate(3)
    play voice3 dahlia_disappointed_ehh2 noloop
    dw "Gaahwaah..."
    play sound sfx_cloth_rustling4
    scene e17s06-97 dw-mc-recovering-on-bed_c1 with dissolve
    pause
    scene e17s06-98 dw-will-step-away_c1 with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    dw "I'll be right back."
    scene e17s06-99 dw-leaves-bedroom_c1 with dissolve
    pause

    $ Lovense.stop()

    $ renpy.end_replay()

    jump e17s06_end

label e17s06_end:

    $ renpy.music.set_volume(0.35, 5.0, "music")
    scene e17s06-101 dw-returns-in-towel_c1 with Fade(0.5, 0.5, 0.5)
    $ Lovense.vibrate(1)
    play sound sfx_barefoot_steps1
    pause
    scene e17s06-100 mc-sees-dw-entering-room_c1 with dissolve
    play voice2 mc_scared_huuuh1 noloop
    pause
    play sound sfx_cloth_rustling2
    scene e17s06-102 dw-asking-everything-safe-takes-off-towel-come-in-bed_c1 with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    dw "Everything was safe? Did you ever think you were getting close to needing to use the safe word?"
    scene e17s06-103 she-rubs-him-down-mc-confirms-ask-about-her_c1 with dissolve
    $ Lovense.vibrate(3)
    play voice2 mc_no_no2 noloop
    mc "Not once."
    mc "How did it go for you?"
    scene e17s06-104 dw-tells-mc-explosive-they-shift-mc-stroking-her-tigh_c1 with dissolve
    $ Lovense.vibrate(1)
    play voice3 dahlia_thinking_mmm2 noloop
    dw "Explosively."
    play voice2 mc_thinking_mmm4 noloop
    mc "Come on, you can tell me, Dahlia."
    scene e17s06-105 dw-uncertain-talks-about-control_c1 with dissolve
    play voice3 dahlia_old_upset noloop
    dw "Sometimes it feels like my anger is in control. I panic a little and look at you for any sign."
    dw "It would have made cumming a bitch until you got me just right."
    scene e17s06-106 mc-grins-aims-to-please_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "I aim to please."
    scene e17s06-107 dw-wants-mc-tell-truth-mc-is-telling_c1 with dissolve
    play voice3 dahlia_yes_yeah4 noloop
    dw "Yes but, you have to tell me the truth."
    play voice2 d9s2_ugu noloop volume 1.7
    mc "I am. And everything was fine."
    scene e17s06-108 mc-wants-dw-say-it-she-cant-emabarrased_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Come on."
    play voice3 dahlia_old_oh noloop
    dw "I can't."
    scene e17s06-109 mc-insist-both-say-i-love-you_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "I know you want to."
    play voice3 dahlia_disappointed_hmm2 noloop
    dw "I love you, [mcname]."
    play voice2 d9s2_mcyes noloop volume 2.2
    mc "I love you too, Dahlia."
    $ unlock_gallery_slot("scene", "e17s06")
    scene e17s06-110 dw-nervous-mc-asking-what-matter-wants-her-talk-to-him_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "What's the matter?"
    play voice3 dahlia_thinking_hmm3 noloop
    dw "It's nothing."
    mc "Talk to me."
    scene e17s06-111 dw-turns-towards-mc-how-better-before-mc-answers-dw-that-helps_c1 with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    dw "How does it feel better than before?"
    play voice2 mc_arrogant_heh1 noloop
    mc "No prison walls."
    dw "That certainly helps."
    scene e17s06-112 dw-reaches-mc-feels-better-dw-going-easy-mc-can-go-together_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "But I think it feels better because of how far we've come."
    play voice3 dahlia_disappointed_ehh1 noloop
    dw "You're going easy on me. I still have a long way to go."
    play voice2 d9s2_yeah noloop volume 1.5
    mc "Maybe. But we can go there together."
    play sound sfx_cloth_rustling4
    scene e17s06-113 dw-straddles-mc-ask-what-do-about-kid_c1 with dissolve
    $ Lovense.vibrate(3)
    play voice3 dahlia_arrogant_huh noloop
    dw "What are we going to do?"
    play voice2 d2s9_confused noloop
    mc "Uh. Sleep?"
    play voice3 dahlia_arrogant_pff noloop
    dw "With the kid, idiot. Parenting is coming. I'm not ready for that puny bit of flesh and bones to be... consuming me."
    scene e17s06-114 mc-tells-dw-kid-already-own-them-she-agrees_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.3
    mc "Dahlia, I think it already owns us."
    play voice3 dahlia_surprised_oh noloop
    dw "Exactly. Oh god, just imagine when it can walk."
    mc "Or talk back."
    scene e17s06-115 dw-mc-continue-talking-baby-walk-talk-back-etc_c1 with dissolve
    play voice3 dahlia_arrogant_heh noloop
    dw "Last chance to back out. To run for the hills."
    play voice2 mc_arrogant_huh1 noloop
    mc "Like you wouldn't hunt me down?"
    play voice3 dahlia_happy_hmm2 noloop
    dw "I absolutely would. But it felt good to offer you an out."
    scene e17s06-117 mc-kiss-belly-dw-no-idea-both-will-have-be-strong_c1 with dissolve
    play sound maria_kiss1
    pause
    scene e17s06-113 dw-straddles-mc-ask-what-do-about-kid_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "I am good right here. I don't want an out."
    mc "I just want you."
    play voice3 dahlia_thinking_hmm4 noloop
    dw "Good. Because when I'm a mother. I'll have no idea what is going to happen."
    scene e17s06-118 mc-laying-dw-on-side-they-will-make-it-dw-certainly-make-rules_c1 with dissolve
    play voice3 dahlia_angry_oof noloop
    dw "We're both going to have to be strong."
    play voice2 mc_yes_yeah6 noloop
    mc "We will make it. Then bam, as soon as they're eighteen, they're out the fucking door."
    play voice3 dahlia_yes_simple noloop
    dw "Yes. We'll certainly have to make that one of our rules."
    scene e17s06-119 mc-loves-dw-past-is-past-wants-hand_c1 with dissolve
    $ Lovense.vibrate(1)
    play voice2 mc_disappointed_ah2 noloop
    mc "I love you, Dahlia. The past is the past and... well it had a few bumps and bruises, but we've worked it out."
    mc "Can I have your hand?"
    scene e17s06-120 mc-dw-hold-hand-front-dw-belly_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Being good enough for my Mistress is all I need."
    play voice3 dahlia_thinking_mmm1 noloop
    dw "You have been adequate."
    dw "There have been surprises."
    scene e17s06-121 dw-tells-loves-mc-he-jokes_c1 with dissolve
    play voice3 dahlia_arrogant_ha noloop
    dw "But I can't imagine anyone else being half as good of a pet as you, my love."
    play voice2 mc_happy_hah1 noloop
    mc "Haha. Mistress, did you really say the \"L\" word twice in one night?"
    scene e17s06-122 dw-shut-up-will-evaluate_c1 with dissolve
    play voice3 dahlia_happy_laugh2 noloop
    dw "Don't ruin the moment, idiot."
    dw "Because {b}you{/b} know, I'm going to have to evaluate you even more when you become a Pappa."
    $ unlock_gallery_slot("cg", "e17s01")
    $ unlock_gallery_slot("cg", "e17s02")
    scene e17s06-123 mc-kisses-dw-hand_c1 with dissolve
    play sound maria_kiss3
    pause
    scene e17s06-124 mc-dw-fall-asleep-end-scene_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Bring it on."

    $ Lovense.stop()


    play sound sfx_camera_fly1
    $ renpy.music.set_volume(1.0, 5.0, "music")
    scene ending_17_art_2 with Fade(1.25, 1.0, 1.75, color="#fff")
    pause
    call end_game_text (_("You have finished playing Ending #17!")) from _call_end_game_text_13
    $ persistent.finished_e17 = True
    $ fl_achievement_unlock("e17_finish")

    stop music fadeout 3.0
    stop sound fadeout 1.0
    jump end

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
