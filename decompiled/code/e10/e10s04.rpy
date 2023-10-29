image e10s04-a29-glam-1 = Movie(play = "images/E-10/s04/anim/e10s04-a29-2x-50fps.webm", start_image = "e10s04-a29 mc-cups-mes-face-anim-29-00_i", image = "e10s04-a29 mc-cups-mes-face-anim-29-78_i", loop = False)

label e10s04:

    scene black
    show screen scene_transistion(_("Weeks later\nAt the end of Summer"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene e10s04-01 opening-shot-mes-watching-mc-writing-white-board_c1
    queue music "<silence 0.2>"
    $ renpy.music.set_volume(0.4, 3.0, "music")
    queue music music_summerend_jazz fadein 2.0
    with Fade(0.5, 0.5, 0.9)
    pause
    play sound sfx_feltpen_writing4 volume 0.65
    scene e10s04-02 mc-finishes-writing-the-pros-cons_c1 with dissolve
    pause
    scene e10s04-03 mc-asking-mes-where-to-start_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Alright. So which should we start with?"
    scene e10s04-06 mes-not-sure-why-thats-con_c1 with dissolve
    play voice3 min_thinking_hmm3 noloop
    mes "Let's do a con first. I wanna get those out of the way as soon as possible."
    scene e10s04-04 mc-nods-good-idea_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Good idea. Okay, so first con."
    play sound sfx_feltpen_writing2 volume 0.65
    scene e10s04-05 mc-writes-first-con-mes-job-going-well_c1 with dissolve
    "Min job going well."
    scene e10s04-06 mes-not-sure-why-thats-con_c1 with dissolve
    play voice3 min_arrogant_huh2 noloop
    mes "Why is that a con?"
    scene e10s04-10 mc-points-mes_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Well, I'm not saying that it's bad, but it certainly makes pivoting to our business harder if you get rooted in your father's company."
    scene e10s04-07 mes-looks-uncomfortable_c1 with dissolve
    play voice3 min_thinking_hmm1 noloop
    mes "...Alright. I guess that makes sense."
    scene e10s04-08 mc-explains-mes_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.7
    mc "What else?"
    scene e10s04-07 mes-looks-uncomfortable_c1 with dissolve
    play voice3 min_happy_relief noloop
    mes "Me having to deal with my family's shit if I go into this."
    scene e10s04-08 mc-explains-mes_c1 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah but as far as they'll know, you'd still be working for your father. This would just be my thing."
    mc "So I don't think that's a con exactly."
    scene e10s04-09 mc-dont-think-con-mes-fair-enough_c1 with dissolve
    play voice3 min_thinking_hmm2 noloop
    mes "Mm... Fair enough.{w} How about your studies then?"
    scene e10s04-10 mc-points-mes_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "Good one."
    play sound sfx_feltpen_writing1 volume 0.65
    scene e10s04-11 mc-writing-dropout-on-board_c1 with dissolve
    "Drop out."
    scene e10s04-12 mc-explains-hell-drop-business-degree-for-this_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "If I do this, I'll be dropping out to fully focus on this. So, sayonara business degree."
    play sound sfx_feltpen_writing5 volume 0.65
    scene e10s04-11 mc-writing-dropout-on-board_c1 with dissolve
    "Stacy study alone."
    scene e10s04-13 mc-writes-stacy-con_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "More than the degree though, hopefully Stacy isn't too upset."
    scene e10s04-14 mes-asking-mc-if-he-wants-abandon-studies_c1 with dissolve
    play voice3 min_surprised_huh1 noloop
    mes "Are you completely sure that you want to just abandon your studies when you're so close to finishing it?"
    scene e10s04-15 mc-going-all-in_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Doing another whole semester without you and always wondering \"What if?\" is something that I don't wanna do, Min."
    mc "I'm confident in this. And I'm going all in."
    play sound maria_kiss3
    scene e10s04-16 mes-eats-strawberry-says-okay_c1 with dissolve
    play voice3 min_arrogant_hm noloop
    mes "*Sighs and smiles* Okay."
    scene e10s04-17 mc-look-board-decided-to-go-pros_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "I think that's enough cons for now. Let's do a couple pros."
    play sound sfx_feltpen_writing6 volume 0.65
    scene e10s04-18 mc-writes-pros-plan-progress-investors_c1 with dissolve
    "Good business plan progress."
    "Potential investors found."
    scene e10s04-19 mes-asking-what-investors_c1 with dissolve
    play voice3 min_surprised_huh2 noloop
    mes "Investors? You already found investors?"
    scene e10s04-20 mes-thinks-investors-cool-mc-reveal-biggest-up_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Well... Let's say that I've found out that they exist and I've gotten their info."
    mc "I still have to actually get them on board, but I'm optimistic."
    scene e10s04-14 mes-asking-mc-if-he-wants-abandon-studies_c1 with dissolve
    play voice3 min_arrogant_huh1 noloop
    mes "Huh. Okay. That's pretty good news."
    scene e10s04-20 mes-thinks-investors-cool-mc-reveal-biggest-up_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Exactly— Oh! And the biggest thing."
    play sound sfx_feltpen_writing3 volume 0.65
    scene e10s04-21 mc-writes-freedom-pro_c1 with dissolve
    "Freedom."
    scene e10s04-22 mes-sighs-would-be-free-from-family_c1 with dissolve
    play voice3 min_disappointed_ehh1 noloop
    mes "*Sighs* If it takes off—which is a big if—we might be free from my family."
    mes "But that doesn't mean we won't be free from the investors and any trouble we will inevitably come across."
    scene e10s04-23 mc-thinks-free-choice-better-than-mes-father_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah. But wouldn't you rather be free to make those choices yourself instead of being forced to go with whatever your father says?"
    play sound sfx_cloth_rustling4
    scene e10s04-24 mc-plops-down-next-to-mes_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "We'll make mistakes, I'm sure we'll fuck up plenty, but we'll also be our own people."
    scene e10s04-25 mc-takes-mes-hand_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "{i}You{/i} will be your own person."
    scene e10s04-26 mes-looking-mc-hand-holding-her-hand_c1 with dissolve
    pause
    scene e10s04-27 mes-looking-board-pros-equal-cons_c1 with dissolve
    pause
    scene e10s04-28 mc-chuckles_c1 with dissolve
    play voice3 min_old_laugh noloop
    mes "Looks like we got an equal number of pros and cons."
    play voice2 d3s11b_mcheh noloop
    mc "*Chuckles* Yeah. It isn't as helpful as I thought it would be."
    scene e10s04-25 mc-takes-mes-hand_c1 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "But that doesn't matter."
    mc "Just say the words and I'll stay and make this work."
    scene e10s04-29 mc-cups-mes-face_c1 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "Trust me, Min."
    play voice3 ["<silence 1.0>", stacy_smell] volume 2.0 noloop
    play sound sfx_camera_fly1
    scene e10s04-a29-glam-1 with Dissolve(0.3)
    pause
    play voice3 min_disappointed_ehh3 noloop
    mes "*Sighs*"
    scene e10s04-31 mes-opens-eyes-smiles-agrees-to-do-it_c1 with dissolve
    play voice3 min_yes_yeah1 noloop
    mes "I guess we're doing this then."
    play voice2 mc_happy_laugh1 noloop
    $ renpy.music.set_volume(0.75, 7.0, "music")
    play sound sfx_bed_fall1 volume 2.0
    scene e10s04-32 mc-jump-up-fuck-yeah-mes-laughs_c1 with dissolve
    mc "Fuck yeah!"
    scene e10s04-33 mc-walks-towards-kitchen-like-a-boss_c1 with dissolve
    queue voice2 mc_happy_oof1 noloop
    mc "This calls for a little celebration!"
    scene e10s04-34 mes-asking-what-mc-doing_c1 with dissolve
    play voice3 min_surprised_ehh1 noloop
    mes "What are you doing?"
    play sound sfx_bottle_chponk1
    scene e10s04-35 mc-pulls-out-wine-bottle-two-glasses_c1 with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "I had a lil' something stashed away just for the occasion."
    scene e10s04-34 mes-asking-what-mc-doing_c1 with dissolve
    play voice3 min_arrogant_heh1 noloop
    mes "*Laughs* You knew I'd agree!?"
    play sound sfx_door_slide6 volume 2.0
    scene e10s04-36 mc-trying-to-open-balcony-door-with-foot_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "Well... Let's just say I was optimistic."
    mc "Help me out here, will ya?"
    play sound sfx_door_slide7
    scene e10s04-37 mes-opens-door-for-mc-they-get-on-balcony_c1 with dissolve
    pause
    play voice3 min_happy_mmm noloop
    play sound sfx_bottle_pouring1
    scene e10s04-38 mc-opens-bottle-pours-glass-to-mes_c1 with dissolve
    pause
    scene e10s04-39 mc-hands-mes-glass-wine_c1 with dissolve
    pause
    scene e10s04-40 mc-raises-toast_c1 with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "To forging our own life!"
    play sound sfx_wineglass_ding1
    scene e10s04-41 mc-mes-clink-glasses_c1 with dissolve
    play voice3 min_disappointed_off noloop
    mes "I hope you know what you're doing, [mcname]."
    scene e10s04-42 mc-holding-mes-by-waist_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Stop worrying. It's all gonna work out just fine."
    play sound sfx_drink_loop1 volume 2.0
    scene e10s04-43 mc-takes-a-sip_c1 with dissolve
    pause
    stop sound fadeout 1.0
    scene e10s04-44 mes-remembers-something_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.7
    mc "Now I just need to register the business and sort out all the bureaucratic stuff."
    mc "I was also thinking I'd start looking for someone to help me get the alpha model going."
    play voice3 min_surprised_oh noloop
    mes "Oh!"
    play sound sfx_phone_tapping1 volume 3.5
    scene e10s04-45 mes-searches-through-phone_c1 with dissolve
    mes "I actually think I might've found just the right person."
    scene e10s04-46 mc-surprised-mes-has-someone-in-mind_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "Really? Who?"
    scene e10s04-47 mes-shows-mc-picture-of-nari_c1 with dissolve
    play voice3 min_old_hmm noloop
    mes "She applied to my father's company, but I swiped her file 'cause she looked perfect."
    scene e10s04-48 mc-raises-eyebrow_c1 with dissolve
    play voice2 mc_arrogant_tsktsk noloop
    mc "Tsk, tsk, we haven't even begun yet and you're already poaching talent from your father, huh? I knew you had it in you."
    scene e10s04-49 mes-rolls-eyes_c1 with dissolve
    play voice3 min_disappointed_mph noloop
    mes "She would've been constricted at my father's place anyway."
    mes "She seems to know the field and is very motivated. Perfect for a startup."
    scene e10s04-50 mc-takes-mes-phone-looks-nari_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "She's cute. Send me the details. I'll check her out."
    scene e10s04-51 mes-incredilous-smile-mc_c1 with dissolve
    play voice3 min_surprised_ehh2 noloop
    mes "\"Check her out\", huh?"
    play voice2 d4s4_mclaugh noloop
    play voice3 polly_laugh2 noloop
    play sound sfx_wineglass_ding1
    scene e10s04-52 mc-mes-both-laugh_c1 with dissolve
    pause
    scene e10s04-53 mc-talks-close-to-mes-touches-foreheads_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "Don't worry. She might be cute, but you're the only woman I love."
    play sound dahlia_kiss_french1
    play sound4 sfx_plate_place1 noloop
    $ unlock_gallery_slot("cg", "e10s04")
    scene e10s04-54 mc-kisses-mes_c1 with dissolve
    pause

    stop music fadeout 5.0
    jump e10s05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
