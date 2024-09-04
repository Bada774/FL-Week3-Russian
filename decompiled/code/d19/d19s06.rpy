image d19s06-a1 = Movie(play = "images/Day-19/s06/anim/d19s06-a21-1-2x-50fps.webm", start_image = "d19s06-a21-1 arj-chokes-cl-slaps-breasts-anim1-01")
image d19s06-a2 = Movie(play = "images/Day-19/s06/anim/d19s06-a21-2-2x-50fps.webm", start_image = "d19s06-a21-2 arj-chokes-cl-slaps-breasts-anim2-01")
image d19s06-a3 = Movie(play = "images/Day-19/s06/anim/d19s06-a24-1-2x-50fps.webm", start_image = "d19s06-a24-1 arj-pinches-cl-nipple-anim-1-01")
image d19s06-a4 = Movie(play = "images/Day-19/s06/anim/d19s06-a24-2-2x-50fps.webm", start_image = "d19s06-a24-2 arj-pinches-cl-nipple-anim-2-01")
image d19s06-a5 = Movie(play = "images/Day-19/s06/anim/d19s06-a24-3-2x-50fps.webm", start_image = "d19s06-a24-3 arj-pinches-cl-nipple-anim-3-01")

label d19s06:

    $ d19s06_purchase_video = False
    $ d19s06_mes = False
    $ d19s06_both_lewalds = False
    $ d19s06_call_tl = False
    $ d19s06_video_points = 120
    $ d19s06_not_enough = False
    $ d19s06_random = renpy.random.randint(0, 9)

    scene d19s06-02 mc-leaves-laptop-table_c1 with dissolve
    pause
    scene d19s06-03 mc-lying-couch_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mct "Well, I suppose I'll start with figuring out what to do about Lewald."
    mct "Lewald is a nutcase. I think pretty much everyone knows it."
    scene d19s06-04 mc-fiddles-phone_c1 with dissolve
    mct "I don't think I'm gonna have much luck trying to discredit her or whatever considering that the rest of the faculty knowingly tolerates her for some reason."
    mct "I think I have to approach her differently..."
    play sound sfx_phone_tapping1 loop
    scene d19s06-05 mc-checks-phone_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "Let's see. I hope Cynthia had her phone on her..."
    mct "If I could just get an audio recording or {i}something{/i}."
    scene d19s06-06 mc-finds-video-cl_c1 with dissolve
    "..."
    play voice2 mc_thinking_hmm3 noloop
    stop sound fadeout 0.5
    mct "There's a concerning amount of \"religious\" porn here."
    mct "Bingo."
    scene d19s06-07 mc-thoughts_c1 with dissolve
    play voice2 mc_scared_huuuh3 noloop
    mct "Holy shit, this is exactly what I need. A whole video!"
    mct "I can't get much from the preview, I don't see any faces."
    mct "But that outfit. That has to be AmRose. Cynthia too."
    scene d19s06-09 mc-looking-phone-points_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mct "Wait... If AmRose and Cynthia are being recorded, Lewald has to be the one recording."
    mct "But if it's on Fetish Locator, that means that Lewald uses the app as well."
    scene d19s06-06 mc-finds-video-cl_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "I'm not sure why I'm surprised, to be honest."
    mct "Whatever. I'm not gonna look a gift horse in the mouth. Maybe I can use that as well..."
    scene d19s06-07 mc-thoughts_c1 with dissolve
    play voice2 mc_scared_huh3 noloop
    mct "Jesus fucking christ."
    mct "[d19s06_video_points] points for a single video!? What the fuck!?"
    mct "How many points do I even have?"
    if d19s06_random == 3:
        scene d19s06-08 mc-looking-at-gui-points_c1 with dissolve
    elif True:
        scene d19s06-09 mc-looking-phone-points_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mct "[fl_points] points."
    if fl_points == d19s06_video_points:
        mct "I have just {i}barely{/i} enough to afford it."

        jump d19s06_video_choice

    elif fl_points > d19s06_video_points and fl_points < 140:
        mct "I can afford it, but it's gonna cost me a lot of points."

        jump d19s06_video_choice

    elif fl_points >= 160:
        mct "I can afford it."
        scene d19s06-11 mc-look-camera-naughty-boy_c1 with dissolve
        play voice2 d1s5_mcthinks noloop volume 1.6
        mct "But only 'cause someone's been very naughty."

        jump d19s06_video_choice

    elif fl_points < d19s06_video_points:
        $ d19s06_not_enough = True
        scene d19s06-10 mc-cant-afford-it_c1 with dissolve
        play voice2 mc_angry_hm2 noloop
        mct "I can't fucking afford it."
        mct "Fuck!"
        scene d19s06-12 mc-phone-table-massage-head_c1 with dissolve
        play voice2 mc_angry_errr3 noloop
        mct "I might be able to do something for Nordin, but I {i}know{/i} that Zarah isn't going to be on my side."
        mct "What can I do to get Lewald on my side?"
        mct "Think, think, think."

        if date_mes is True:

            jump d19s06_mes_text

        elif date_mk is True or date_mk_tr is True:
            scene d19s06-14 mc-sighs_c1 with dissolve
            play voice2 mc_disappointed_ehh1 noloop
            mct "Alright. No point bashing my head against the wall here."
            mct "I can think about Nordin while I come up with something for Lewald."
            mct "Hm... I wonder what Maria is up to?"
            scene d19s06-13 mc-leaves_c1 with dissolve
            pause

            stop music fadeout 3.0
            jump d19s07
        elif True:

            scene d19s06-14 mc-sighs_c1 with dissolve
            play voice2 mc_disappointed_ehh1 noloop
            mct "...I got nothing."
            mct "Welp, I had a good run I guess."
            mct "God fucking damn it."
            scene d19s06-13 mc-leaves_c1 with dissolve
            play voice2 mc_arrogant_hm3 noloop
            mct "*Sigh* Might as well study some more and hope to God that I can pass on that alone."

            stop music fadeout 3.0
            jump d19s07

label d19s06_video_choice:

    scene d19s06-09 mc-looking-phone-points_c1 with dissolve
    play voice2 d2s9_confused noloop
    mct "Should I purchase the video?"
    menu:
        "Purchase"(hint="d19s06m03c01"):
            $ d19s06_purchase_video = True
            jump d19s06_video
        "Don't"(hint="d19s06m03c02"):

            play voice2 mc_no_nah1 noloop
            mct "No thanks. I don't need to see that."
            if date_mes is True and date_cl is True:
                jump d19s06_mes_text
            elif True:
                stop music fadeout 3.5
                jump d19s07

label replay_d19s06:
label d19s06_video:

    call add_points (-(d19s06_video_points)) from _call_add_points_26
    scene d19s06-15 mc-watches-video_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "Let's see what is going on."
    stop music fadeout 3.5
    scene d19s06-15-01 mc-watches-video-phone-view_c1 with dissolve
    play voice3 teresa_disappointed_ehh1_phonetalk noloop
    tl "Good. I think I'm recording."
    scene d19s06-16 tl-wrong-camera_c1 with fade
    play sound sfx_phone_button1
    play voice3 teresa_disappointed_ohh1 noloop
    tl "This needs to be captured so that this memory of humiliation, the consequences of her actions, are never forgotten."
    scene d19s06-18 cl-avoiding-arj-phone_c1 with dissolve
    queue music badass_rock
    pause
    scene d19s06-17 arj-cl-uncomfortable_c1 with dissolve
    play voice3 teresa_disappointed_mph noloop
    tl "Go on, dear. Teach my failure of a daughter the meaning of being a pure, righteous woman of God."
    tl "Do what you must, do what I can't."
    scene d19s06-15 mc-watches-video_c1 with fade
    play voice2 d3s11b_mcheh noloop
    mct "Jesus, AmRose looks so uncomfortable."
    scene d19s06-19 exremely-uncomfortable_c1 with fade
    play voice3 amrose_thinking_emm noloop
    arj "Uhm... Mrs. Lewald, when my mother was disciplining my...sister."
    mct "\"Sister\"? AmRose is an only child. Why would she lie?"
    scene d19s06-20 cl-tells-arj-begin_c1 with dissolve
    queue voice3 amrose_thinking_hmm1 noloop
    arj "She said that the best way to erase bad habits was to destroy the positive feeling associated with it."
    scene d19s06-21 arj-confused-cl-pleading-look_c1 with dissolve
    play voice4 cynthia_arrogant_he noloop
    pause
    scene d19s06-22 arj-starts-explaining-herself_c1 with dissolve
    play voice3 teresa_thinking_hmm1 noloop
    tl "Hm. I suppose that makes a certain amount of sense."
    scene d19s06-23 arj-talking_c1 with dissolve
    play voice4 amrose_yes_yeah2 noloop
    arj "Exactly. So I think the best way to help her would be to...to, uhm, first figure out what she likes so much about her...debaucherous activities."
    scene d19s06-25 arj-continues_c1 with dissolve
    arj "Her fetishes, in other words."
    play voice2 d1s2_hmm noloop volume 1.4
    mct "What is she trying to do here?"
    scene d19s06-24 tl-considers-arj-proposal_c1 with dissolve
    play voice3 teresa_disgust_ogh noloop
    tl "Ugh, such an ugly word. But I can see what you're saying."
    tl "Very well. Cynthia, answer her."
    scene d19s06-26 cl-likes-being-choked_c1 with dissolve
    play voice4 cynthia_happy_mmm noloop
    cl "I uh...I like being choked?"
    scene d19s06-27 tl-disgusted-with-cl_c1 with dissolve
    play voice3 teresa_surprised_huh3 noloop
    tl "{i}Choking{/i}. Oh my Lord, what did I do to deserve such a lost daughter? You're a disgrace to our kind."
    scene d19s06-28 cl-starts-tearing-up_c1 with dissolve
    play voice3 cynthia_sex_closedmoan2 noloop
    pause
    scene d19s06-29 arj-wants-to-lead_c1 with dissolve
    play voice4 amrose_disappointed_ehh1 noloop
    arj "I uh... Let me handle her, Ma'am. You shouldn't bring yourself down to her level."
    play voice3 teresa_yes_yeah1 noloop
    tl "You're right, you're right. That's very true. Please, I won't interrupt, continue."
    scene d19s06-30 cl-like-abusing-breasts_c1 with dissolve
    play voice3 amrose_thinking_hmm2 noloop
    arj "Go on, Cynthia."
    play voice4 cynthia_pain_crying3 noloop
    cl "*Sniffles* I uhm, I like it when... I like it when men abuse my breasts."
    stop voice4 fadeout 1.0
    scene d19s06-31 arj-explains-plan_c1 with dissolve
    play voice3 amrose_yes_okay1 noloop
    arj "Good, good. Now that we know what she likes, we can punish her with those very things and rip out that thread of sin from her."
    scene d19s06-32 arj-takes-cl-arm-leads-to-desk_c1 with dissolve
    pause
    play voice3 amrose_old_psst2 noloop
    scene d19s06-33 arj-whisper-cl-ear_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop

    $ Lovense.stop()

    mct "What is she whispering? She's up to something."
    scene d19s06-34 arj-sets-cl-desk-exposes-breast_c1 with dissolve
    $ Lovense.vibrate(2)
    play voice3 amrose_thinking_hmm3 noloop
    arj "I'm doing this so that she can truly feel the shame in being undressed by a complete stranger."
    scene d19s06-35 cl-both-breasts-exposed_c1 with dissolve
    play voice4 cynthia_arrogant_huh noloop
    arj "So that she associates this kind of intimacy with shame and embarrassment instead of pleasure."
    play voice3 amrose_angry_argh1 noloop
    $ Lovense.vibrate(3)
    scene d19s06-36 arj-chokes-cl_c1 with dissolve
    play voice4 cynthia_pain_cough2 noloop volume 0.7
    arj "Now, you will learn to understand that this is sin. Nothing more."
    scene d19s06-a1 with dissolve
    $ Lovense.vibrate(5)
    play voice4 cynthia_sex_openmoans1
    play sound [sfx_hands_clap1, "<silence 0.6>", sfx_hands_clap2, "<silence 0.7>", sfx_hands_clap3, "<silence 0.7>", sfx_hands_clap4, "<silence 0.96>"] loop
    pause
    stop sound
    scene d19s06-a2 with dissolve
    play sound [sfx_hands_clap1, "<silence 0.6>", sfx_hands_clap2, "<silence 0.7>", sfx_hands_clap3, "<silence 0.7>", sfx_hands_clap4, "<silence 0.9>"] loop
    pause
    stop sound fadeout 1.0
    stop voice4 fadeout 1.5
    $ Lovense.vibrate(3)
    scene d19s06-39 tl-aproves-arj-punishment_c1 with dissolve
    play voice3 teresa_yes_angry noloop
    tl "Very good. You're doing wonderfully."
    scene d19s06-36 arj-chokes-cl_c1 with dissolve
    play voice4 amrose_angry_argh2 noloop
    arj "You will cry out in pain, and you will banish the demon of lust from within you."
    arj "Understood?"
    scene d19s06-38 cl-secretly-enjoys_c1 with dissolve
    play voice3 cynthia_yes_horny noloop
    cl "Y-Yes."
    play voice4 amrose_arrogant_hmm1 noloop
    arj "Good."
    $ Lovense.vibrate(5)
    scene d19s06-a3 with dissolve
    play voice3 cynthia_sex_openmoans1
    play voice4 daisy_moaning
    pause
    scene d19s06-a4 with dissolve
    pause
    scene d19s06-a5 with dissolve
    pause
    stop voice4 fadeout 1.0
    $ Lovense.vibrate(3)
    scene d19s06-41 cl-tries-to-fake_c1 with dissolve
    play voice3 cynthia_no_nonono noloop
    cl "No! No! *Choked moans* Please! I beg of you! Stop!"
    cl "I can't take anymore! My precious breasts! Oh lord have mercy!"
    scene d19s06-42 tl-has-something-to-give-arj_c1 with dissolve
    play voice4 teresa_angry_dough noloop
    tl "This {i}is{/i} mercy, Cynthia. Learn, learn before you subject yourself to the eternal fires of hell!"
    scene d19s06-43 mc-looking-at-phone_c1 with fade
    play voice2 mc_scared_oh4 noloop
    mct "Man, Cynthia's acting is terrible, but Lewald is buying it."
    scene d19s06-44 tl-stops-shooting-doesnt-turn-phone-off_c1 with fade
    play voice4 cynthia_sex_openmoans1
    cl "*Dramatic cries and whimpers of \"pain\".*"
    scene d19s06-45 cl-holding-on-cross_c1 with dissolve
    play voice4 cynthia_scared_ah2 noloop
    cl "Please! {i}{b}Please{/b}{/i}! As God is my witness, I'm free of lust! Please, stop this terrible pain!"
    scene d19s06-46 tl-rummage-through-desk-phone-records_c1 with dissolve
    play voice3 teresa_hey_angry noloop
    tl "Wait. I have something for you."
    scene d19s06-47 tl-shows-clamp-arj_c1 with dissolve
    play voice2 amrose_surprised_uh5 noloop
    play voice4 cynthia_scared_huh noloop
    pause
    scene d19s06-48 tl-wants-arj-using-clamps_c1 with dissolve
    play voice3 teresa_yes_aga noloop
    tl "Take these. They are my clamps of virtue. To remind me to always remain in the light of God."
    tl "Use them to guide her into the light as well."
    scene d19s06-49 arj-holding-clamps-agrees-to-use_c1 with dissolve
    play voice4 amrose_arrogant_huh2 noloop
    arj "I uh...I will. Thank you."
    scene d19s06-50 arj-wants-cl-cup-breasts_c1 with dissolve
    play voice4 amrose_arrogant_hmm2 noloop
    arj "Cup your breasts and present them to me."
    scene d19s06-51 cl-complies_c1 with dissolve
    play voice3 cynthia_arrogant_hm noloop
    pause
    play sound sfx_sextoy_cuff1
    scene d19s06-52 arj-goes-clamp-nipple_c1 with dissolve
    $ Lovense.vibrate(4)
    play voice4 amrose_angry_ehh noloop
    arj "The first virtue, humility."
    arj "You must understand that under God, you're nothing. No accomplishment of man would stand up to his greatness."
    play sound sfx_sextoy_cuff2
    scene d19s06-53 cl-breast-clamped_c1 with dissolve
    $ Lovense.vibrate(5)
    play voice4 amrose_happy_mmm noloop
    arj "The second virtue, kindness."
    arj "You break your poor mother's heart with your sinful ways. Is that kindness?"
    scene d19s06-54 cl-lip-bite-stays-quiet_c1 with dissolve
    play voice4 amrose_arrogant_huh4 noloop
    arj "Tell me."
    scene d19s06-55 arj-puts-second-clamp_c1 with dissolve
    play voice3 cynthia_no_calm noloop
    cl "No. No it isn't."
    play voice4 amrose_yes_yap noloop
    arj "Good girl. Then learn."
    arj "The third virtue, patience."
    $ Lovense.vibrate(6)
    play sound sfx_sextoy_cuff1
    scene d19s06-56 arj-puts-third-clamp_c1 with dissolve
    play voice4 amrose_disappointed_ehh2 noloop
    arj "We all need patience. I can understand your desires. But our time will come when we have to give our bodies."
    arj "When we will be made whole with our husbands and be allowed to birth the next generation."
    play voice2 mc_surprised_wow3 noloop
    mct "AmRose is surprisingly convincing here... She's a better actor than Cynthia, Christ."
    scene d19s06-57 tl-complains-cl-never-listens_c1 with dissolve
    play voice4 teresa_yes_active noloop
    tl "I keep telling her, but she never listens."
    play sound sfx_sextoy_cuff2
    $ Lovense.vibrate(7)
    scene d19s06-58 arj-puts-fourth clamp-other-breast_c1 with dissolve
    play voice3 amrose_arrogant_huh3 noloop
    arj "She will now. Won't you?"
    play voice4 cynthia_yes_horny2 noloop
    cl "Yes..."
    scene d19s06-60 arj-talking-fifth-clamp-in-hand_c1 with dissolve
    play voice3 amrose_thinking_hmm4 noloop
    arj "The fourth virtue, diligence."
    arj "Until the time your divine purpose manifests, you need to put yourself into your study of God."
    arj "No mortal may ever truly understand him, but you will still gain a closer connection to him through diligent study."
    $ Lovense.vibrate(8)
    scene d19s06-59 cl-in-pain_c1 with dissolve
    play voice4 cynthia_scared_ah4 noloop
    cl "{i}Please{/i} stop. It hurts so bad."
    scene d19s06-60 arj-talking-fifth-clamp-in-hand_c1 with dissolve
    play voice3 amrose_disappointed_oh1 noloop
    arj "It's better to hurt now than to burn forever in eternal hellfire."
    arj "This is for your own good."
    play sound sfx_sextoy_cuff1
    $ Lovense.vibrate(9)
    scene d19s06-61 arj-puts-fifth-clamp_c1 with dissolve
    play voice3 amrose_thinking_hmm5 noloop
    arj "The fifth virtue, charity."
    arj "Love and give on to others as you love yourself."
    play sound sfx_sextoy_cuff2
    $ Lovense.vibrate(10)
    scene d19s06-62 arj-puts-sixth-clamp_c1 with dissolve
    play voice4 cynthia_sex_closedmoan6 noloop
    arj "The sixth virtue, temperance."
    arj "One must never covet. Whether that be material wealth or earthly pleasures. To covet is to run into the clutches of Satan."
    play sound sfx_jeans_fly1
    scene d19s06-63 arj-takes-cl-pants-down_c1 with dissolve
    play voice2 amrose_thinking_oh1 noloop
    arj "And finally, chastity. The one virtue that you are sorely missing."
    $ Lovense.vibrate(12)
    play sound sfx_sextoy_cuff1
    scene d19s06-64 arj-clamps-cl-clit_c1 with dissolve
    pause
    scene d19s06-65 cl-shouts-pain_c1 with dissolve
    play voice3 cynthia_pain_ah2 noloop
    cl "*Shout* Pl-{i}Please{/i}."
    scene d19s06-66 arj-puts-hand-cl-chin_c1 with dissolve
    play voice2 mc_pain_ou1 noloop
    mct "Jesus. Considering how fangirly she got when she first met Cynthia, AmRose sure isn't holding back here."
    play voice4 amrose_arrogant_yeah2 noloop
    arj "Do you now understand, whore? Do you understand what happens when you stray from your flock?"
    scene d19s06-67 arj-hands-cl-neck_c1 with dissolve
    play voice4 amrose_angry_ergh noloop
    arj "You're a lone, weak sheep. Your place is with your flock."
    play voice3 teresa_happy_yeah noloop
    tl "Yes! Yes! Exactly!"
    play sound sfx_bed_slide4
    play voice4 amrose_angry_ugh noloop
    $ Lovense.vibrate(16)
    scene d19s06-68 arj-really-chokes-cl_c1 with dissolve
    play voice2 cynthia_pain_cough1 noloop volume 0.7
    pause
    scene d19s06-69 tl-moves-for-better-view_c1 with dissolve
    play voice2 cynthia_scared_ah1 noloop
    pause
    stop sound fadeout 1.0

    $ Lovense.stop()

    scene d19s06-70 feed-over-cut-mc_c1 with fade
    $ renpy.music.set_volume(0.2, 1.5, "music")
    play voice2 mc_surprised_huh6 noloop
    mct "Huh?{w} That's it!?"
    mct "All those points and that's all I fucking get!?"
    mct "Alright... Serenity now. I'm not here for the video."
    $ renpy.end_replay()
    $ unlock_gallery_slot("scene", "d19s06")
    scene d19s06-71 mc-fiddles-phone_c1 with dissolve
    play voice2 mc_disappointed_ehh4 noloop
    mct "I'm here for Lewald, and I got everything I need."
    mct "All AmRose had to do was babble some religious bullshit and she had Lewald wrapped around her finger."
    mct "All I have to do is do the same thing."
    if date_mes is False:
        scene d19s06-72 mc-fiddles-phone-more_c1 with dissolve
    elif True:
        scene d19s06-05 mc-checks-phone_c1 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mct "Let's see... Alright. I got Lewald's contact info."
    mct "I just need to give her a call and hope for the best."

    if date_mes is True and date_cl is True:
        jump d19s06_mes_text
    elif True:
        jump d19s06_lewald

label d19s06_mes_text:

    if d19s06_not_enough is True:
        scene d19s06-73 min-text-mc_c1 with dissolve
        pause
    call buzz from _call_buzz_39
    if d19s06_not_enough is True:
        scene d19s06-72 mc-fiddles-phone-more_c1 with dissolve
    elif True:
        scene d19s06-71 mc-fiddles-phone_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.5
    mct "Min?"
    play sound sfx_message_in1
    mes "Can you come over? I got a surprise for you."
    if d19s06_not_enough is True:
        scene d19s06-71 mc-fiddles-phone_c1 with dissolve
    elif True:
        scene d19s06-72 mc-fiddles-phone-more_c1 with dissolve
    play sound sfx_message_out1
    mct "Whats the surprise?"
    play sound sfx_message_in1
    mes "I don't wanna spoil it. Just come if you can."
    play sound sfx_message_out1
    mct "Alright I'll be there"
    scene d19s06-74 mc-leaves-apartment_c1 with dissolve
    pause

    stop music fadeout 3.0
    jump d19s06mes

label d19s06_lewald:

    if d19s06_mes is True:
        scene d19s06-09-2 mc-min-phone-look_c2 with Fade(0.4, 0.4, 0.4)
        pause
        play voice2 mc_yes_okay2 noloop
        mct "Let's see... Alright. I got Prof. Lewald's contact info."
        scene d19s06-09-2 mc-min-phone-look_c1 with dissolve
        mct "I should give her a call now."

    menu:
        "Call Prof. Lewald"(hint="d19s06m01c01"):
            $ d19s06_call_tl = True
            pass
        "Do Not to Influence Prof Lewald"(hint="d19s06m01c02"):

            stop sound4 fadeout 3.0
            stop music fadeout 3.0
            jump d19s07

    play sound sfx_phone_call1
    mct "Alright. I think I have a plan for this.{w} Time to give Professor Lewald a call."
    if d19s06_mes is True:
        scene d19s06-08 mc-min-talk1_c1 with dissolve
    elif True:
        scene d19s06-75-03 mc-talking-phone_three_c1 with dissolve
    play voice3 teresa_disappointed_ehh1_phonetalk noloop
    tl "Hello?"
    play voice2 mc_angry_cough1 noloop
    mc "*Clears throat* Yes, hello. Is this Professor Lewald?"
    $ renpy.music.set_volume(0.05, 0.7, "sound4")
    scene d19s06-01 lt-talk-desk1_c1 with dissolve
    play voice3 teresa_yes_simple noloop
    tl "Yes, it is. Who is this?"
    if d19s06_mes is True:
        play voice2 mc_thinking_hmm3 noloop
        $ renpy.music.set_volume(0.5, 0.7, "sound4")
        scene d19s06-11 mc-min-talk4_c1 with dissolve
    mc "[mcname] Young. You may have heard of me. I'm also known as [mclogin]."
    $ renpy.music.set_volume(0.05, 0.7, "sound4")
    scene d19s06-01 lt-talk-desk1_c2 with dissolve
    play voice3 teresa_disappointed_ohh1 noloop
    tl "Ah, Mister Young. Yes, I've been expecting you to try to contact me about your finals."
    if d19s06_mes is True:
        play voice2 mc_yes_yeah4 noloop
        $ renpy.music.set_volume(0.5, 0.7, "sound4")
        scene d19s06-09 mc-min-talk2_c2 with dissolve
    mc "We can discuss that later. Right now, we should talk about how you need my help."
    $ renpy.music.set_volume(0.05, 0.7, "sound4")
    scene d19s06-01-2 lt-talk-desk4_c1 with dissolve
    play voice3 teresa_surprised_huh3 noloop
    tl "I do?"
    if d19s06_mes is True:
        play voice2 mc_yes_aga2 noloop
        $ renpy.music.set_volume(0.5, 0.7, "sound4")
        scene d19s06-10 mc-min-talk3_c1 with dissolve
    mc "Indeed. It is a matter of discipline."
    $ renpy.music.set_volume(0.05, 0.7, "sound4")
    scene d19s06-01-2 lt-talk-desk4_c2 with dissolve
    play voice3 teresa_thinking_emm1 noloop
    tl "[mclogin], you say? Are you one of the faithful?"
    if d19s06_mes is True:
        $ renpy.music.set_volume(0.5, 0.7, "sound4")
        scene d19s06-10 mc-min-talk3_c2 with dissolve
    elif True:
        scene d19s06-75-02 mc-talking-phone_two_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "What I am is a master of biological response, bondage, discipline, and behavioral conditioning."
    tl "Hmm..."
    mct "The bait is in the water, now let's set the hook."
    $ renpy.music.set_volume(0.05, 0.7, "sound4")
    scene d19s06-01-3 lt-talk-desk5_c1 with dissolve
    play voice3 teresa_disappointed_mph noloop
    tl "So, you're not part of our spiritual collective? I'm not sure-"
    if d19s06_mes is True:
        $ renpy.music.set_volume(0.5, 0.7, "sound4")
        scene d19s06-11 mc-min-talk4_c1 with dissolve
        play voice2 mc_arrogant_hm3 noloop
    mc "I specialize in situations like your daughter - and yourself. But if you think your current practices are working-"
    $ renpy.music.set_volume(0.05, 0.7, "sound4")
    scene d19s06-01-3 lt-talk-desk5_c2 with dissolve
    play voice3 teresa_no_active noloop
    tl "No!{w} *clears throat* Um, I mean...{w} I've tried everything..."
    if d19s06_mes is True:
        $ renpy.music.set_volume(0.5, 0.7, "sound4")
        scene d19s06-11 mc-min-talk4_c2 with dissolve
        play voice2 mc_arrogant_heh3 noloop
    mc "I can assure you this will be a life altering experience."
    $ renpy.music.set_volume(0.05, 0.7, "sound4")
    scene d19s06-02 lt-talk-desk2_c1 with dissolve
    play voice3 teresa_thinking_hmm2 noloop
    tl "Do I need to provide payment?"
    if d19s06_mes is True:
        $ renpy.music.set_volume(0.5, 0.7, "sound4")
        scene d19s06-12 mc-min-talk5_c1 with dissolve
        play voice2 mc_yes_yeah1 noloop
    mc "Let's meet tomorrow. Let's say... a few hours before my final exam."
    $ renpy.music.set_volume(0.05, 0.7, "sound4")
    scene d19s06-02 lt-talk-desk2_c2 with dissolve
    play voice3 teresa_thinking_oh noloop
    tl "I see."
    scene d19s06-03 lt-talk-desk3_c2 with dissolve
    play voice3 teresa_thinking_hmm1 noloop
    tl "You want to make it a wager."
    if d19s06_mes is True:
        $ renpy.music.set_volume(0.5, 0.7, "sound4")
        scene d19s06-12 mc-min-talk5_c2 with dissolve
        play voice2 d9s2_yeah noloop volume 3.0
    mc "I suppose you could see it like that."
    $ renpy.music.set_volume(0.05, 0.7, "sound4")
    scene d19s06-03 lt-talk-desk3_c1 with dissolve
    play voice3 teresa_thinking_hmm3 noloop
    tl "Your performance will influence my decision. Is that it?"
    if d19s06_mes is True:
        $ renpy.music.set_volume(0.5, 0.7, "sound4")
        scene d19s06-13 mc-min-sit1_c2 with dissolve
        play voice2 mc_no_uhuh1 noloop
    mc "I wouldn't say anything so vulgar.{w} Neither should you."
    $ renpy.music.set_volume(0.05, 0.7, "sound4")
    scene d19s06-04 lt-talk-walk1_c2 with dissolve
    play voice3 teresa_yes_yeah1 noloop
    tl "Alright, I'll make sure Cynthia is there for you to punish."
    if d19s06_mes is True:
        $ renpy.music.set_volume(0.5, 0.7, "sound4")
        scene d19s06-13 mc-min-sit1_c1 with dissolve
    elif True:
        scene d19s06-75-01 mc-talking-phone_one_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "I think you misunderstood me."
    tl "Oh?"
    menu:
        "Just the Professor"(hint="d19s06m02c01"):
            play voice2 d4s4_mclaugh noloop
            mc "Cynthia shouldn't be there. Just you, Professor."

        "Both Cynthia and Her Mother"(hint="d19s06m02c02") if persistent.is_special is True and date_cl is True:
            $ d19s06_both_lewalds = True
            play voice2 d4s4_mclaugh noloop
            mc "Both of you should be there."

    $ renpy.music.set_volume(0.05, 0.7, "sound4")
    scene d19s06-04 lt-talk-walk1_c1 with dissolve
    play voice3 teresa_surprised_what noloop
    tl "Excuse me?"
    if d19s06_mes is True:
        $ renpy.music.set_volume(0.5, 0.7, "sound4")
        scene d19s06-14 mc-min-sit2_c1 with dissolve
    elif True:
        scene d19s06-75-03 mc-talking-phone_three_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    if date_mes is True:
        mc "I've already punished Cynthia today."
    elif True:
        mc "I've already seen how you punished Cynthia."
    if d19s06_mes is True:
        scene d19s06-15 mc-min-sit3_c2 with dissolve
    mc "The root of the problem - the core issue - is your method and your mentality."
    mc "Tomorrow I will teach you what real discipline means."
    $ renpy.music.set_volume(0.05, 0.7, "sound4")
    scene d19s06-05 lt-talk-walk2_c1 with dissolve
    play voice3 teresa_happy_relief2 noloop
    tl "I see."
    if d19s06_mes is True:
        $ renpy.music.set_volume(0.5, 0.7, "sound4")
        scene d19s06-14 mc-min-sit2_c2 with dissolve
        play voice2 mc_arrogant_hm1 noloop
    mc "Sir.{w} You should address me as \"Sir\", \"Master\", or \"[mclogin]\" from now on."
    $ renpy.music.set_volume(0.05, 0.7, "sound4")
    scene d19s06-06 lt-talk-walk3_c1 with dissolve
    play voice3 teresa_disappointed_ohh2 noloop
    tl "Master?"
    if d19s06_mes is True:
        $ renpy.music.set_volume(0.5, 0.7, "sound4")
        scene d19s06-15 mc-min-sit3_c1 with dissolve
        play voice2 mc_yes_yes3 noloop
    mc "Yes, Theresa."
    $ renpy.music.set_volume(0.05, 0.7, "sound4")
    scene d19s06-07 lt-talk-walk4_c1 with dissolve
    play voice3 teresa_thinking_mmm noloop
    tl "I see... Sir."
    if d19s06_mes is True:
        $ renpy.music.set_volume(0.5, 0.7, "sound4")
        scene d19s06-15 mc-min-sit3_c2 with dissolve
    elif True:
        scene d19s06-75-04 mc-talking-phone_four_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "I look forward to seeing you tomorrow, Theresa."
    $ renpy.music.set_volume(0.05, 0.7, "sound4")
    scene d19s06-07 lt-talk-walk4_c2 with dissolve
    play voice3 teresa_happy_relief1 noloop
    tl "Thank you, Sir. I look forward to seeing you as well.{w}.. Master."

    if d19s06_mes is True:
        $ renpy.music.set_volume(0.5, 0.7, "sound4")
        scene d19s06-16 mc-min-end_c1 with dissolve
    elif True:
        scene d19s06-75-05 mc-talking-phone_five_c1 with dissolve
    play voice2 mc_scared_oh2 noloop
    mct "It worked!!! I can't believe I pulled that off!"
    mct "I really didn't expect that to-"
    if d19s06_mes is True:
        scene d19s06-16 mc-min-end_c2 with dissolve
    elif True:
        scene d19s06-75-06 mc-talking-phone_six_c1 with dissolve
    play voice2 mc_pain_mff5 noloop
    mct "Oh, shit! What the hell am I going to do tomorrow?!"

    stop sound4 fadeout 3.0
    stop music fadeout 3.0
    jump d19s07

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
