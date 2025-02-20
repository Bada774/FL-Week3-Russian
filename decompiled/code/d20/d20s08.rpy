image d20s08-fight-a1 = Movie(play = "images/Day-20/s08/anim/d20s08-a51-1-2x-60fps.webm", start_image = "d20s08-a51-1 mc-js-spar-mc-uppercut-anim-00", image = "d20s08-a51-1 mc-js-spar-mc-uppercut-anim-66", loop = False)
image d20s08-fight-a2 = Movie(play = "images/Day-20/s08/anim/d20s08-a52-1-2x-60fps.webm", start_image = "d20s08-a52-1 mc-js-spar-mc-block-anim-00", image = "d20s08-a52-1 mc-js-spar-mc-block-anim-68", loop = False)
image d20s08-fight-a3 = Movie(play = "images/Day-20/s08/anim/d20s08-a52-2-2x-60fps.webm", start_image = "d20s08-a52-2 mc-js-spar-mc-block-anim-00", image = "d20s08-a52-2 mc-js-spar-mc-block-anim-68", loop = False)
image d20s08-fight-a4 = Movie(play = "images/Day-20/s08/anim/d20s08-a54-01-2x-50fps.webm", start_image = "d20s08-a54-01 mc-kicks-js-through-glass-anim-54-01-000_i", image = "d20s08-a54-01 mc-kicks-js-through-glass-anim-54-01-150_i", loop = False)
image d20s08-fight-a5 = Movie(play = "images/Day-20/s08/anim/d20s08-a54-02-2x-50fps.webm", start_image = "d20s08-a54-02 mc-kicks-js-through-glass-anim-54-02-000", image = "d20s08-a54-02 mc-kicks-js-through-glass-anim-54-02-150", loop = False)

image d20s08-ir-a1 = Movie(play = "images/Day-20/s08/anim/d20s08-a78-01-2x-60fps.webm", start_image = "d20s08-a78-01 ir-masturbates-01")
image d20s08-ir-a2 = Movie(play = "images/Day-20/s08/anim/d20s08-a78-02-2x-60fps.webm", start_image = "d20s08-a78-02 ir-masturbates-02")

image d20s08_arj_tase_pb:
    "d20s08-44 arj-tases-pb_c3"
    pause 0.3
    "d20s08-44 arj-tases-pb_c4"
    pause 0.3
    "d20s08-44 arj-tases-pb_c5"
    pause 0.3
    repeat

label d20s08:

    $ d20s08_copy_files = False
    $ d20s08_ir_video = False

    scene black
    show screen scene_transistion(_("Some time later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene d20s08-01 mc-arives-server-arj-sy-already-there_c1
    with Fade(0.5, 0.5, 0.9)
    queue music music_action_question
    $ renpy.music.set_volume(0.35, 5.0, "music")
    pause
    play voice3 amrose_arrogant_hmm2 noloop
    arj "Well, that answers that question."
    scene d20s08-02 arj-looking-mc-pov_c1 with dissolve
    play voice2 d1s2_hmm noloop
    mc "What question was that?"
    play voice3 amrose_disappointed_ehh2 noloop
    arj "Whether or not you were the one that broke through the police tape."
    scene d20s08-03 mc-asking-what-sy-doing_c1 with dissolve
    play voice2 mc_no_nope2 noloop
    mc "Nope, not me. What's Stacy doing?"
    play voice3 amrose_thinking_hmm1 noloop
    arj "She's trying to determine if someone is still inside."
    play voice4 stacy_hmm noloop
    sy "We don't want to be surprised or ambushed in there or accidentally walk in on the cops."
    scene d20s08-04 sy-doesnt-think-so_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.3
    mc "Good thinking. So, is anyone there?"
    play voice4 stacy_mmm2 noloop
    sy "I don't think so..."
    play voice3 amrose_arrogant_huh3 noloop
    arj "I think that means, \"No.\""
    play voice4 stacy_yeahno noloop
    sy "I didn't say, \"No.\" I need more time to be sure."
    scene d20s08-05 sy-tells-couple-hours-are-enough_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "How much time? How long is this going to take?"
    sy "A couple of hours should be sufficient."
    play voice3 amrose_surprised_uh4 noloop
    arj "I understand why you said it would take a while..."
    arj "But two more hours?!"
    scene d20s08-06 mc-thinks-its-too-much_c1 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "That seems a bit much."
    play voice4 stacy_angry noloop
    sy "Well, if you can just bust out your Superman vision and see through walls go right ahead."
    sy "Either that, or go find me a fuck ton of antennas so I can scan more than one point at a time!"
    scene d20s08-07 arj-goes-whoah-whoah-whoah_c1 with dissolve
    play voice3 amrose_surprised_oh1 noloop
    arj "Whoa, whoa, whoa."
    play voice2 d2s9_mchey noloop
    mc "Stacy - we both love you - so when I say this I mean it from the deepest part of my heart..."
    mc "W.T.F. girl?"
    scene d20s08-08 sy-puts-device-away-says-sorry_c1 with dissolve
    play voice4 stacy_upset1 noloop volume 1.2
    sy "Sorry, this is just really tedious and probably pointless and my hands are cramping and I'm a LITTLE frustrated."
    play voice3 amrose_yes_okay2 noloop
    arj "Okay. We get that. So, Plan B?"
    play voice4 stacy_no1 noloop
    sy "I didn't bring any Molotovs."
    play voice2 mc_arrogant_heh1 noloop
    mc "I thought that was Plan C."
    scene d20s08-09 arj-explains-plan-b_c1 with dissolve
    play voice3 amrose_no_long noloop
    arj "No, I mean, we just go in there and see what's what."
    play voice4 stacy_oh2 noloop
    sy "Oh, B as in Brute force?"
    play voice2 d1s1_mmm noloop
    mct "I'm not sure I like that idea."
    play voice3 amrose_happy_laugh1 noloop
    arj "Well, I mean, [mcname] got the code from Hana. It's not like we have to force the door open."
    scene d20s08-10 sy-looks-mc_c1 with dissolve
    play voice4 stacy_angryhuh noloop
    sy "I'm sorry, but I need a break. I'm going to get some ice for my hands and coffee for my bloodstream."
    sy "Either of you want anything?"
    play voice2 d2s9_confused noloop
    mc "I could, uh..."
    scene d20s08-11 arj-winks-slightly-mc_c1 with dissolve
    play voice3 amrose_no_uhuh noloop
    arj "We're good."
    mct "AmRose is up to something, but I have no idea what."
    scene d20s08-10 sy-looks-mc_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, no. I mean, I'm good."
    scene d20s08-12 arj-like-plan_c1 with dissolve
    play voice4 stacy_laugh4 noloop
    sy "Okay. I'll be back in a few minutes and then we can all go in together."
    play voice3 amrose_yes_yeah2 noloop
    arj "Sounds like a plan."
    play voice2 mc_yes_ugu1 noloop
    mc "Uh, yeah. That sounds good."
    scene d20s08-14 sy-walks-away-normal_c1 with dissolve
    pause

    jump d20s08_mc_arj

label d20s08_mc_arj:

    scene d20s08-11 arj-winks-slightly-mc_c1 with dissolve
    play voice3 amrose_disappointed_ehh1 noloop
    arj "I thought she'd never leave."
    play sound dahlia_kiss_french1
    play voice3 amrose_happy_mmm noloop
    scene d20s08-15 arj-interupts-mc-jumping-kissing-him_c1 with hpunch
    play voice2 mc_pain_mff1 noloop
    mct "Wha?"
    mct "Oh... nice."
    scene d20s08-16 arj-relaxes-mc-hands_c1 with dissolve
    play voice3 amrose_disappointed_oh5 noloop
    arj "I needed that."
    play voice2 mc_happy_yay2 noloop
    mc "I'm glad. Although, I assume you didn't want her to leave just so we could have a make-out session here."
    scene d20s08-17 mc-looking-arj-eyes-pov_c1 with dissolve
    play voice3 amrose_no_nope noloop
    arj "Nope. I just knew that Stacy would sneak a look back to see what we were doing."
    play voice2 mc_thinking_oh1 noloop
    mc "So, kissing me was just a diversion for you."
    play voice3 amrose_no_nah noloop
    arj "Not just. It was also for luck."
    scene d20s08-18 arj-takes-step-back_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Uh huh. So, what are we really doing?"
    mct "Please say \"Blow Job\". Please say \"Blow Job\"."
    play voice3 amrose_thinking_hmm2 noloop
    arj "We're going behind Stacy's back... what else could I have in mind?"
    play voice2 mc_arrogant_huh1 noloop
    mc "I literally have no idea."
    scene d20s08-19 arj-points-control-pad_c1 with dissolve
    play voice3 amrose_happy_woo noloop
    arj "Viola!"
    play voice2 d1s5_mcthinks noloop volume 1.4
    mc "I think you meant, \"Voila\"."
    arj "Either, both, whatever. Just punch in the code and let's go."
    mc "Even though it's not safe?"
    scene d20s08-20 arj-approaches-pad-mc-asks-if-safe_c1 with dissolve
    play voice3 amrose_arrogant_huh4 noloop
    arj "Who said it wasn't safe? Besides, if Stacy gets back before we go in she'll want to copy everything before we delete it."
    play voice2 mc_thinking_hmm1 noloop
    mc "And you want to just delete it."
    arj "I want to destroy any record of those photos and videos ever existing."
    mc "So, what's stopping you?"
    scene d20s08-21 mc-asking-what_s stopping-arj_c1 with dissolve
    play voice3 amrose_arrogant_huh1 noloop
    arj "What's with all the questions? Just open the door already."
    play voice2 mc_thinking_emm1 noloop
    mc "Hana didn't give you the code?"
    play voice3 amrose_surprised_uh2 noloop
    arj "I didn't-"
    play voice2 mc_yes_yeah8 noloop
    mc "And Stacy didn't tell you the code?"
    scene d20s08-22 arj-explains-sy-fears-mc-aproach-her_c1 with dissolve
    play voice3 amrose_no_angry1 noloop
    arj "No. She's afraid I'll delete everything before she can copy it."
    play voice2 mc_hey_hey2 noloop
    mc "What's on there that you're so afraid of?"
    play voice3 amrose_angry_argh2 noloop
    if is_antagonist_mode is True:
        arj "My blackmail photos, dumbass."
        scene d20s08-23 mc-leans-wall-smug_c1 with dissolve
        play voice2 mc_thinking_hmm3 noloop
        mc "Well, of course we're going to delete those. Stacy cannot plan on doing anything with the blackmail-"
    else:
        arj "My photos, dumbass."
        scene d20s08-23 mc-leans-wall-smug_c1 with dissolve
        play voice2 mc_thinking_hmm3 noloop
        mc "Well, of course we're going to delete those. Stacy wouldn't do anything-"
    play voice3 amrose_angry_argh1 noloop
    arj "I NEED THEM GONE."
    play voice2 mc_yes_okay2 noloop
    mc "Okay, then convince me."
    scene d20s08-24 arj-promises-to-be-mc-friend_c1 with dissolve
    play voice3 amrose_angry_ergh noloop
    arj "What do you want?"
    play voice2 mc_thinking_mmm1 noloop
    mc "I know you're not a business major, but you were in enough business courses to know how to negotiate."
    mc "I have something you want. What are you willing to give for it?"
    play voice3 amrose_arrogant_hmm1 noloop
    arj "I'll be your best friend."
    scene d20s08-25 mc-explains-options_c1 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "You already are."
    play voice3 amrose_disappointed_ah noloop
    arj "I won't murder you."
    play voice2 mc_arrogant_pff1 noloop volume 1.4
    mc "If you murder me before Stacy gets back, you'll never get that door open."
    mc "If you murder me after Stacy gets back, it would be pointless."
    scene d20s08-26 arj-angry-mc-sides-sy_c1 with dissolve
    play voice3 amrose_angry_ugh noloop
    arj "Seriously, what do you want?"
    play voice2 mc_disappointed_ehh1 noloop
    mc "I don't know. I'm kinda hoping to keep you pitching ideas before Stacy gets back."
    play voice3 amrose_surprised_what noloop
    if is_antagonist_mode is True:
        arj "You're siding with her?! You want copies of everyone's blackmail just out there somewhere???"
    else:
        arj "You're siding with her?! You want copies of everything anyone did just out there somewhere???"
    play voice2 mc_no_no2 noloop
    mc "I didn't say that. I just don't see a reason to go behind Stacy's back like this."
    scene d20s08-27 mins-later-arj-has-idea_c1 with dissolve
    play voice3 amrose_thinking_hmm4 noloop
    arj "Alright. I've got an offer you can't refuse."
    if is_antagonist_mode is True:
        arj "You open the door. You delete the blackmail files."
    else:
        arj "You open the door. You delete the files."
    play voice2 mc_thinking_hmm5 noloop
    mc "Sounds like it is all work for me."
    play voice3 amrose_no_questioning2 noloop
    arj "You don't have to delete any other files until Stacy gets back."
    scene d20s08-28 mc-asks-if-arj-stays-outside_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "And you stay out here?"
    play voice3 amrose_no_simple1 noloop
    arj "No. I come with you and suck your cock while you do it."
    play voice2 mc_yes_okay3 noloop
    mc "Sounds like a plan."
    play voice3 amrose_arrogant_huh2 noloop
    arj "So, you agree?"
    scene d20s08-27 mins-later-arj-has-idea_c1 with dissolve
    play voice2 mc_no_no1 noloop
    mc "No. That's what you told Stacy, \"Sounds like a plan\"."
    play voice3 amrose_disappointed_oh4 noloop
    arj "Oh."
    mc "I'm not worried about the files. I'm worried about going behind Stacy's back."
    arj "Look, I'll do anything you want. ANYTHING you want."
    scene d20s08-29 arj-ready-to-do-anything_c1 with dissolve
    play voice3 amrose_angry_ehh noloop
    arj "You can shit in my face and tell me to swallow it. I don't care."
    arj "I just need to get in there before Stacy gets back!"
    play voice2 mc_thinking_mmm2 noloop
    mc "There's a thought..."
    play voice3 amrose_surprised_huh1 noloop
    arj "Really? You're into that?!"
    scene d20s08-30 mc-wants-three-wishes_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Not the scat. Be my genie. Grant me 3 wishes - anything I want."
    play voice3 amrose_yes_happy1 noloop
    arj "Done. Agreed. Whatever. Just hurry up before she gets back!!!"
    play voice2 mc_arrogant_huh2 noloop
    mc "In addition to the earlier terms. I'm the only one that accesses the server until Stacy gets back, and you suck my cock while I delete the files."
    play voice3 amrose_yes_yeah4 noloop
    arj "Anything else?"
    play sound [sfx_server_pincode_0, "<silence 0.3>", sfx_server_pincode_0, "<silence 0.3>", sfx_server_pincode_7, "<silence 0.3>", sfx_server_pincode_1]
    scene d20s08-31 mc-puts-hand-pad_c1 with dissolve
    play voice2 mc_no_uhuh1 noloop
    mc "That's it."
    play voice3 amrose_yes_ugu noloop
    arj "I agree."
    mc "Alright."
    play sound sfx_door_scifi_open1 volume 0.6

    jump d20s08_jumped

label d20s08_jumped:

    $ renpy.music.set_volume(0.1, 3.0, "music")
    $ renpy.music.set_volume(0.6, 0.0, "sound4")
    play sound4 sfx_server_room fadein 1.5
    scene d20s08-32 mc-arj-enter-server-room_c1 with dissolve
    pause
    scene d20s08-33 arj-mc-talking-getting-interupted_c1 with dissolve
    stop music fadeout 5.0
    play sound sfx_locker_open1
    play voice3 amrose_thinking_hmm3 noloop
    arj "What was the code anyway?"
    play voice2 mc_happy_a1 noloop
    mc "Oh, it is-"
    scene d20s08-34 ma-spots-js-ambush_c1 with dissolve
    play voice2 mc_angry_huh1 noloop
    pause
    play music music_last_holy_fight
    $ renpy.music.set_volume(0.6, 0.0, "music")
    scene d20s08-35 js-jumps-mc-arj_c1 with vpunch
    play voice4 boy4_pain_oh2 noloop
    js "Die, motherfucker!!"
    play sound sfx_throw_something1
    scene d20s08-36 mc-blocks-js-punch-tells-arj-run_c1 with hpunch
    play voice3 amrose_surprised_oh2 noloop
    arj "Oh, fuck!"
    play voice2 mc_hey_hey1 noloop
    mc "AmRose, Run!"
    play voice4 boy4_angry_kghh2 noloop
    scene d20s08-37 js-kicks-mc-blocks_c1 with vpunch
    play voice2 mc_angry_hm2 noloop
    pause
    play sound sfx_kick1
    play voice4 boy4_pain_oh1 noloop
    scene d20s08-38 mc-punches-js_c1 with hpunch
    pause
    play voice4 boy4_scared_huh1 noloop
    play voice2 mc_angry_errr3 noloop
    scene d20s08-39 mc-catches-js-leg-arj-runs-into-server-rows_c1 with hpunch
    pause
    play voice4 boy4_pain_oof1 noloop
    play sound sfx_kick2
    scene d20s08-40 mc-pushes-js-towards-server_c1 with vpunch
    play voice2 d9s5_auch2 noloop
    mc "Jerome.{w} You asshole.{w} I should've known-"
    if cage_ntr is True:
        scene d20s08-41 arj-walking-between-servers_c1 with dissolve
        pause
        scene d20s08-42 pb-ambush-arj_c1 with dissolve
        play voice5 pete_hey_angry noloop
        pb "Hey you-"
        scene d20s08-43 arj-pulls-out-taser_c1 with dissolve
        play voice3 amrose_old_chmchm noloop
        pause
        play sound sfx_taser_start
        scene d20s08-44 arj-tases-pb_c2 with hpunch
        pause
        play sound sfx_taser_loop loop
        play voice5 pete_pain_arrr noloop
        scene d20s08_arj_tase_pb
        pb "Yaahaahaaah!!!"
        stop sound fadeout 0.4
        $ renpy.music.set_volume(1.0, 0.0, "sound2")
        play sound2 sfx_taser_end noloop volume 2.0
        queue sound sfx_fall_down1 volume 1.6
        scene d20s08-45 pb-drops-arj-walks-over-him_c1 with vpunch
        pause
        scene d20s08-46 mc-wants-arj-zap-js-arj-tells-one-time_c1 with dissolve
        play voice2 mc_angry_errr4 noloop volume 1.5
        mc "Go AmRose!{w} Hit this fucker next!!"
        play voice3 amrose_thinking_oh1 noloop
        arj "It was single use only!"
    play sound sfx_throw_something1
    scene d20s08-47 mc-throws-punch-misses-wide_c1 with hpunch
    play voice2 mc_surprised_huh5 noloop volume 2.0
    mct "Fuck! I missed!"
    play sound sfx_kick3
    play voice4 boy4_angry_kghh1 noloop
    scene d20s08-48 js-punches-mc-square-jaw_c1 with hpunch
    play voice2 mc_pain_mff5 noloop
    pause
    play voice4 boy4_happy_laugh6 noloop
    scene d20s08-49 mc-steps-back-js-getting-cocky_c1 with dissolve
    js "What did five fingers say to the face!"
    play voice2 mc_pain_rrrr noloop
    mc "Damn. You're quick."
    if cage_ntr is True:
        play voice4 boy4_angry_mmm2 noloop
        js "You sucker punched me this morning, bitch!"
        play voice2 mc_hey_hey4 noloop
        mc "You had me strapped to a chair!"
    play voice4 boy4_angry_dough1 noloop
    play sound sfx_kick_leg1
    scene d20s08-50 mc-js-spar-kick-block_c1 with vpunch
    if cage_ntr is True:
        js "You should still be there!"
    else:
        js "Punkass dumbfuck."
    play voice2 mc_scared_huuuh3 noloop
    mc "When the hell did you get so good at this?"
    scene d20s08-49 mc-steps-back-js-getting-cocky_c1 with dissolve
    play voice4 boy4_arrogant_ha1 noloop
    if cage_ntr is True:
        js "I was faking during our previous fight."
        play voice2 mc_surprised_what1 noloop
        mc "What?"
        play voice4 boy4_yes_yeah noloop
        js "When I fought you over Lydia... that was all pretend."
    else:
        js "I was distracted during our previous fight."
        play voice2 mc_scared_oh1 noloop
        mc "When you tried to rape Lydia?!"
        play voice4 boy4_yes_yeah noloop
        js "She deserved it!"
    play voice2 mc_pain_argh1 noloop
    play voice3 ["<silence 0.76>", boy4_pain_cough1] noloop
    play sound2 ["<silence 0.16>", sfx_epic_kick1] noloop
    scene d20s08-fight-a1 with dissolve
    pause
    play voice3 boy4_angry_argh1 noloop
    scene d20s08-fight-a2 with dissolve
    play sound2 sfx_epic_kick2 noloop
    pause
    play voice3 boy4_angry_breath2 noloop
    scene d20s08-fight-a3 with dissolve
    play sound2 sfx_epic_kick2 noloop
    pause
    scene d20s08-53 js-steps-back-towards-control-room_c1 with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "I'm going to hurt you so much for that."
    play voice4 boy4_arrogant_yeah2 noloop
    js "Yeah?! Go ahead, big man. Hit me with your best shot."
    js "I'll break you like-"
    play voice2 d9s5_auch2 noloop
    play voice4 ["<silence 0.6>", boy4_pain_argh3] noloop
    play sound2 sfx_epic_kick3 noloop
    scene d20s08-fight-a4 with dissolve
    pause
    play sound2 sfx_epic_kick4 noloop
    scene d20s08-fight-a5 with dissolve
    pause 5.8
    play voice4 boy4_pain_sobs1 noloop fadein 1.5 volume 0.5
    play sound2 sfx_epic_jump1 noloop
    scene d20s08-55 mc-time-to-bring-pain_c1 with dissolve
    play voice2 mc_pain_mff4 noloop
    mc "Time to bring the pain."
    play voice2 mc_pain_argh1 noloop
    play voice4 boy4_pain_cough2 noloop
    play sound sfx_kick3
    scene d20s08-56 mc-beats-js-ground_c1 with vpunch
    mc "Just{w} fucking{w} die{w} already!"
    stop music fadeout 4.5
    scene d20s08-57 mc-stands-over-unconscious-js_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, you're unconscious.{w} I guess that will do."

    jump d20s08_server

label d20s08_server:

    if cage_ntr is True:
        scene d20s08-59 js-pb-both-tied-floor_c1 with Fade(0.4, 0.4, 0.4)
    else:
        scene d20s08-58 js-tied-floor_c1 with Fade(0.4, 0.4, 0.4)
    play voice3 amrose_disappointed_oh1 noloop
    arj "Well, that settles that."
    play voice2 mc_yes_yeah1 noloop
    mc "Good thing you always carry a length of rope with you."
    play voice3 amrose_yes_yeah1 noloop
    arj "A woman's gotta be prepared for her man."
    play music music_legendary_shutdown fadein 2.5
    if cage_ntr is True:
        scene d20s08-61 sy-comes-in-sees-js-pb_c1 with dissolve
    else:
        scene d20s08-60 sy-comes-in-sees-js_c1 with dissolve
    play voice4 stacy_ah noloop
    sy "What the fuck?!"
    play voice2 mc_thinking_emm1 noloop
    mc "It wasn't safe."
    play voice3 amrose_disappointed_ehh2 noloop
    arj "I'm sorry. It was my fault."
    scene d20s08-62 sy-comes-asks-if-she-should-call-police_c1 with dissolve
    play voice4 stacy_huh noloop
    sy "Fuck that. Should I call the police?"
    play voice2 mc_no_uhuh2 noloop
    mc "Not yet."
    scene d20s08-63 gang-goes-computer-interface_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.5, 3.5, "music")
    play sound sfx_keyboard_typing2 volume 2.0
    scene d20s08-64 mc-sits-desk-talking-arj-about-blowjob_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    if date_sy is True:
        mc "I'm pretty sure one of you should be sucking my cock while I'm sitting here."
    else:
        mc "AmRose - shouldn't you be sucking my dick right now?"
    play voice3 amrose_arrogant_hmm1 noloop
    arj "The deal was that we did that before Stacy got back."
    scene d20s08-65 sy-wants-her-chair_c1 with dissolve
    play voice4 stacy_huh2 noloop
    sy "What are you two talking about?"
    play voice3 amrose_no_nah noloop
    arj "Nothing. Don't worry about it."
    play voice4 stacy_mmm2 noloop
    sy "Okay. [mcname] would you mind getting out of my chair?"
    scene d20s08-66 mc-explains-need-to-delete-files_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    if is_antagonist_mode is True:
        mc "Actually, yes. I need to delete the blackmail files before you do anything."
    else:
        mc "Actually, yes. I need to delete all of AmRose's files before you do anything."
    play voice4 polly_laughter noloop
    sy "Oh! It's easy."
    play voice3 amrose_surprised_huh2 noloop
    arj "How will you know which-?"
    scene d20s08-67 sy-tells-file-directory_c1 with dissolve
    play voice4 polly_impressed noloop
    sy "There is a directory for those. I will delete them before I do anything else."
    play voice3 amrose_arrogant_huh4 noloop
    arj "You didn't see-?"
    play voice4 stacy_nono noloop
    sy "No. No. I didn't look at any of them."
    if is_antagonist_mode is True:
        play voice3 amrose_arrogant_yeah2 noloop
        arj "Even mine?"
        scene d20s08-68 sy-promises-havent-seen-files-will-delete-them_c1 with dissolve
        play voice4 stacy_oh noloop
        sy "Especially yours."
        play voice2 d3s11b_mcheh noloop
        mc "What about mine?"
        play voice3 stacy_no1 noloop
        sy "No, I didn't see you jerking off next to Lydia while she was asleep."
        play voice2 mc_surprised_what3 noloop
        mc "What?!"
        scene d20s08-67 sy-tells-file-directory_c1 with dissolve
        play voice3 amrose_surprised_huh3 noloop
        arj "Wait a second..."
        play voice4 stacy_hey noloop
        sy "I swear that I will delete all the blackmail files before I do anything else."
    else:
        play voice3 amrose_happy_mmm noloop
        arj "I'm trusting you."
        scene d20s08-68 sy-promises-havent-seen-files-will-delete-them_c1 with dissolve
        play voice4 polly_aga noloop
        sy "You can watch me do it."
        sy "See this folder called \"ErikaRed\"?"
        mct "Oh yeah, I almost forgot her username."
        scene d20s08-67 sy-tells-file-directory_c1 with dissolve
        play voice4 stacy_upset1 noloop
        sy "[mcname], please press the delete button."
        play sound sfx_keyboard_enter1
        play voice2 mc_yes_yes2 noloop
        mc "Done."
        sy "And it's gone."
    scene d20s08-69 arj-asking-about-copies_c1 with dissolve
    play voice3 amrose_thinking_emm noloop
    arj "What about backups? Or anything the police already copied?"
    sy "Let me check..."
    play sound sfx_keyboard_typing2 volume 2.0
    scene d20s08-67-01 sy-leans-towards-screen_c1 with dissolve
    play voice4 stacy_no2 noloop
    sy "I'm not seeing any other users accessing this data recently... and there is no backup set."
    play voice2 mc_thinking_mmm5 noloop
    mc "That will have to be good enough."
    scene d20s08-70 arj-prefers-all-burned_c1 with dissolve
    play voice3 amrose_angry_ergh noloop
    arj "I'd still feel better if we burned it all to ash."
    scene d20s08-71 mc-warns-sy-not-cool_c1 with dissolve
    play voice4 stacy_angry noloop
    if persistent.is_special is True:
        sy "I might sneak a peek at what my brother has been doing."
    else:
        sy "I might sneak a peek at what [mcname] has been doing."
    play voice3 amrose_thinking_oh2 noloop
    arj "Oh... that's fine with me."
    play voice2 mc_no_no4 noloop
    mc "Not cool!"
    play voice4 stacy_yeahno noloop
    sy "We can discuss it later. Now scoot!"
    scene d20s08-72 sy-takes-sit-asking-what-to-do_c1 with dissolve
    play voice3 polly_impressed noloop
    sy "So, we had a disagreement. I'm willing to let this be solved democratically."
    sy "May I back-up the other files to an external drive before deleting everything?"
    sy "Or am I just deleting everything?"
    scene d20s08-72-01 sy-arj-talk_c1 with dissolve
    play voice3 amrose_disappointed_ehh1 noloop
    arj "You know my opinion. Destroy it all. No copies."
    play voice4 stacy_angryhuh noloop
    sy "You know my opinion. I want a backup copy of the code, pics, and videos. {w}Not to publish, but for my own... for educational purposes."
    scene d20s08-73 mc-making-choice_c1 with dissolve
    play voice3 amrose_arrogant_hmm2 noloop
    arj "So, I guess it's up to you, [mcname]."
    play voice2 mc_yes_yeah4 noloop
    mc "Well, I've been thinking a lot about this, and..."
    menu:
        "Side with Stacy - Copy then Delete"(hint="d20s08m01c01"):
            $ d20s08_copy_files = True
            play voice2 mc_thinking_hmm4 noloop
            mc "Stacy... make your copies then delete everything."
        "Side with AmRose - Destroy it Completely"(hint="d20s08m01c02"):

            play voice2 mc_thinking_hmm4 noloop
            mc "Stacy, I agree with AmRose. Destroy everything."

    $ fl_achievement_unlock("d20s08n01")
    $ unlock_gallery_slot("extra", "d20s08n01")

    mc "And I mean everything. I don't want to find out there's some rogue copies on a cloud server or something."
    scene d20s08-74 sy-wants-show-something_c1 with dissolve
    play voice4 polly_aga noloop
    sy "Understood. I'll nuke everything."
    play voice2 mc_arrogant_huh3 noloop
    mc "Alright, I suppose we should wait until you are done to call the police."
    sy "Before I do this... can I show you something?"
    scene d20s08-76 arj-asking-seriously_c1 with dissolve
    play voice3 amrose_surprised_oh3 noloop
    arj "What?!"
    play voice4 stacy_suckmoan1 noloop
    sy "Nothing involving either of you... just something that looks hot."
    scene d20s08-75 sy-talks-about-ir-video_c1 with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "What is it?"
    play voice4 stacy_suckmoan3 noloop
    sy "It's labeled \"IR masturbating\" and I've watched the first few seconds..."
    sy "You know that bartender? Iona?"
    sy "It's looks like a fucking hot video of her getting a little alone time."
    scene d20s08-76 arj-asking-seriously_c1 with dissolve
    play voice3 amrose_surprised_uh5 noloop
    arj "Seriously?"
    play voice4 stacy_hey noloop
    if is_antagonist_mode is True:
        sy "It's in the standard files - not the blackmail. Are you telling me you don't want to see it?"
    else:
        sy "Are you telling me you don't want a peek at that?"
    play voice3 amrose_yes_okay1 noloop
    arj "Okay, I'll admit that she is kinda hot."
    scene d20s08-75 sy-talks-about-ir-video_c1 with dissolve
    play voice4 stacy_hmm noloop
    sy "See? [mcname], what do you think?"
    menu:
        "Alright, I want to see the video"(hint="d20s08m02c01"):
            $ d20s08_ir_video = True
            play voice2 mc_yes_okay1 noloop
            mc "Okay. Let's check this out."
            jump d20s08_ir_video
        "No, I don't want to see that."(hint="d20s08m02c02"):

            play voice2 mc_no_no3 noloop
            mc "No. Let's hurry up and finish what we came for."
            jump d20s08_end

label d20s08_ir_video:

    if _in_replay:
        $ renpy.music.set_volume(0.6, 0.0, "sound4")
        $ renpy.music.set_volume(0.5, 3.5, "music")
        play sound4 sfx_server_room fadein 1.5
        play music music_legendary_shutdown fadein 2.5
    scene d20s08-77 gang-starts-video_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.0, 1.5, "sound4")
    $ renpy.music.set_volume(0.2, 1.5, "music")
    play voice3 iona_moans6
    play sound sfx_sex_fingering_fast1 loop volume 0.4
    scene d20s08-ir-a1 with dissolve
    pause
    scene d20s08-ir-a2 with dissolve
    pause
    play sound sfx_door_open3
    play voice3 iona_ou2 noloop
    scene d20s08-78-02 ir-interupted-by-hana_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.5, 2.0, "music")
    $ renpy.music.set_volume(0.6, 1.5, "sound4")
    scene d20s08-79 mc-tells-fun-part-over-sy-asking-if-sure_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Looks like the fun part's over."
    play voice4 stacy_huh2 noloop
    sy "Are you sure?"
    play voice2 mc_yes_yes1 noloop
    mc "Definitely."
    scene d20s08-82 sy-asks-if-arj-sure-arj-is-sure_c1 with dissolve
    play voice3 amrose_yes_yap noloop
    arj "I agree with [mcname]. Stop the video."
    sy "Okay."

    jump d20s08_end

label d20s08_end:

    scene d20s08-80 mc-tells-sy-destroy-video-or-ask-if-copied_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.5
    if d20s08_copy_files is False:
        mc "Alright, Stacy. Destroy it all."
    else:
        mc "Alright, Stacy. Is your copy finished?"
        play voice4 stacy_hmm noloop
        sy "Yup. It's done."
        mc "Good enough."
        scene d20s08-76 arj-asking-seriously_c1 with dissolve
        play voice3 amrose_angry_breath1 noloop
        arj "Destroy it all."
    play voice4 stacy_mmm1 noloop
    sy "I wrote a special program just for this task."
    sy "It will wipe everything related from Fetish Locator so completely even the NSA won't be able to recover it."
    scene d20s08-82 sy-asks-if-arj-sure-arj-is-sure_c1 with dissolve
    sy "Are you sure we want to do this?"
    play voice3 amrose_yes_happy2 noloop
    arj "YES!"
    scene d20s08-83 sy-tells-mc-program-is-running_c1 with dissolve
    play voice4 min_thinking_hmm1 noloop
    sy "[mcname]?"
    play voice2 d9s2_mcyes noloop volume 2.2
    mc "Definitely."
    play sound sfx_keyboard_typing1
    scene d20s08-80 mc-tells-sy-destroy-video-or-ask-if-copied_c1 with dissolve
    play voice4 stacy_upset1 noloop
    sy "Okay...{w} Pressing return."
    play voice2 mc_surprised_huh6 noloop
    mc "Huh?"
    sy "It's running."
    mc "Good."
    scene d20s08-81 sy-doing-her-thing_c1 with dissolve
    play voice3 amrose_arrogant_huh3 noloop
    arj "How long will this take?"
    play voice4 stacy_laugh4 noloop
    sy "Sixteen hours."
    play voice2 d1s5b_ehhh noloop
    mc "*sigh* Really?"
    sy "Did I say hours? I meant minutes."
    scene d20s08-82 sy-asks-if-arj-sure-arj-is-sure_c1 with dissolve
    play voice3 amrose_thinking_hmm1 noloop
    arj "Alright. While you're doing that I'll prepare an anonymous report that there was a break-in at this server room."
    scene d20s08-84 arj-will-prepare-anonymous-report_c1 with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What?! Why?!"
    play voice3 amrose_arrogant_hmm1 noloop
    if cage_ntr is True:
        arj "So the police can arrest Pete and Jerome."
    else:
        arj "So the police can arrest Jerome."
    play voice2 mc_disappointed_off2 noloop
    mc "Oh, right. Don't send it yet, though."
    play voice3 amrose_yes_yeah3 noloop
    arj "Of course not. I'll send it anonymously after we leave."
    play sound sfx_hands_clap3
    scene d20s08-85 sy-pretends-to-be-spiderguy-arj-makes-report_c1 with dissolve
    play voice4 polly_angry noloop
    sy "Cool. We're just like those spider guys."
    play voice3 amrose_thinking_hmm2 noloop
    arj "I think that's trademarked."
    sy "It's an homage, or parody, or something..."
    play voice2 mc_disappointed_ehh4 noloop
    mc "How are we like those spider guys? Do you expect us to break our backs falling from dangerous heights on-stage?"
    scene d20s08-86 sy-suggests-leaving-bad-guys-without-explanation-arj-agrees_c1 with dissolve
    play voice4 polly_laughter noloop
    sy "You know, tying the bad guys up and leaving them for the police without any explanation."
    play voice3 amrose_arrogant_yeah1 noloop
    arj "Good point. I'll add a list of their possible crimes to the anonymous report."
    mct "I can't believe that we're putting more thought into this than..."
    play sound sfx_horror_message1
    scene d20s08-87 sy-program-done-arj-report-sent-mc-asks-if-they-should-hurry_c1 with dissolve
    play voice4 stacy_yay noloop
    sy "It's done!"
    play sound sfx_message_out1
    play voice3 amrose_yes_ugu noloop
    arj "Sent the report!"
    play voice2 d2s12_emmm noloop
    mc "That means the cops are coming, right?"
    play voice3 amrose_surprised_ahh2 noloop
    arj "Fuck! Run!!!"
    $ renpy.music.set_volume(1.0, 2.0, "music")
    scene d20s08-88 gang-runs-out-of-server-room_c1 with dissolve
    pause

    stop sound4 fadeout 3.0
    stop music fadeout 5.0
    jump d20s09
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
