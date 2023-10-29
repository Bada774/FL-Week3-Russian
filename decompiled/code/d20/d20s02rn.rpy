image d20s02rn-a1-1 = Movie(play = "images/Day-20/s02-nor/anim/d20s02-99-01-2x-50fps.webm", start_image = "d20s02-99-01 mk-suck-anim_c100_i")
image d20s02rn-a1-2 = Movie(play = "images/Day-20/s02-nor/anim/d20s02-99-02-2x-50fps.webm", start_image = "d20s02-99-02 mk-suck-anim_c200_i")
image d20s02rn-a1-3 = Movie(play = "images/Day-20/s02-nor/anim/d20s02-a101-01-2x-50fps.webm", start_image = "d20s02-a101-01 mk-suck-anim-101-01-00_i")
image d20s02rn-a1-4 = Movie(play = "images/Day-20/s02-nor/anim/d20s02-a101-02-2x-50fps.webm", start_image = "d20s02-a101-02 mk-suck-anim-101-02-00_i")
image d20s02rn-a2 = Movie(play = "images/Day-20/s02-nor/anim/d20s02-a74-1-2x-50fps.webm", start_image = "d20s02-a74-1 mk-mout-fuck-anim-01")
image d20s02rn-a2-f = Movie(play = "images/Day-20/s02-nor/anim/d20s02-a74-1-2x-60fps.webm", start_image = "d20s02-a74-1 mk-mout-fuck-anim-01")
image d20s02rn-a3 = Movie(play = "images/Day-20/s02-nor/anim/d20s02-a74-2-2x-50fps.webm", start_image = "d20s02-a74-2 mk-mout-fuck-anim-01")
image d20s02rn-a3-f = Movie(play = "images/Day-20/s02-nor/anim/d20s02-a74-2-2x-60fps.webm", start_image = "d20s02-a74-2 mk-mout-fuck-anim-01")
image d20s02rn-a4 = Movie(play = "images/Day-20/s02-nor/anim/d20s02-a90-1-2x-50fps.webm", start_image = "d20s02-a90-1 mk-anal-anim-01")
image d20s02rn-a4-f = Movie(play = "images/Day-20/s02-nor/anim/d20s02-a90-1-2x-60fps.webm", start_image = "d20s02-a90-1 mk-anal-anim-01")
image d20s02rn-a5 = Movie(play = "images/Day-20/s02-nor/anim/d20s02-a90-2-2x-50fps.webm", start_image = "d20s02-a90-2 mk-anal-anim-01")
image d20s02rn-a5-f = Movie(play = "images/Day-20/s02-nor/anim/d20s02-a90-2-2x-60fps.webm", start_image = "d20s02-a90-2 mk-anal-anim-01")
image d20s02rn-a6 = Movie(play = "images/Day-20/s02-nor/anim/d20s02-a90-3-2x-50fps.webm", start_image = "d20s02-a90-3 mk-anal-anim-01")
image d20s02rn-a6-f = Movie(play = "images/Day-20/s02-nor/anim/d20s02-a90-3-2x-60fps.webm", start_image = "d20s02-a90-3 mk-anal-anim-01")
image d20s02rn-a7 = Movie(play = "images/Day-20/s02-nor/anim/d20s02-a110-1-2x-50fps.webm", start_image = "d20s02-a110-1 mk-fuck-anim-01")
image d20s02rn-a7-f = Movie(play = "images/Day-20/s02-nor/anim/d20s02-a110-1-2x-60fps.webm", start_image = "d20s02-a110-1 mk-fuck-anim-01")
image d20s02rn-a8 = Movie(play = "images/Day-20/s02-nor/anim/d20s02-a110-2-2x-50fps.webm", start_image = "d20s02-a110-2 mk-fuck-anim-01")
image d20s02rn-a8-f = Movie(play = "images/Day-20/s02-nor/anim/d20s02-a110-2-2x-60fps.webm", start_image = "d20s02-a110-2 mk-fuck-anim-01")
image d20s02rn-a9 = Movie(play = "images/Day-20/s02-nor/anim/d20s02-a110-3-2x-50fps.webm", start_image = "d20s02-a110-3 mk-fuck-anim-01")
image d20s02rn-a9-f = Movie(play = "images/Day-20/s02-nor/anim/d20s02-a110-3-2x-60fps.webm", start_image = "d20s02-a110-3 mk-fuck-anim-01")

label d20s02rn:

    $ d20s02rn_stop_facefuck = False
    $ d20s02rn_stop_anal = False
    $ d20s02rn_stop_atm = False
    $ d20s02rn_stop_creampie = False

    if d19s07_mk_nordin is False:
        jump d20s02zw

    scene black
    show screen scene_transistion(_("Some time later\nOutside Nordin's office"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene d20s02-01-outside-rn-office
    with Fade(0.5, 0.5, 0.9)
    play sound sfx_door_creak2
    pause
    $ renpy.music.set_volume(0.5, 1.0, "music")
    play music thinking_music_5
    scene d20s02-02-mk-talk-mc with dissolve
    play voice3 min_disappointed_ehh1 noloop
    mk "Is he there?{w} Do you have a good view of his desk?"
    scene d20s02-03-mc-talk-mk with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Yes and yes. He's there and I've got a pretty good view. I should be able to see when he penetrates you."
    scene d20s02-04-mk-talk-mc with dissolve
    play voice3 min_thinking_hmm3 noloop
    mk "Yeah, about that. Do you know why I asked you for rough sex yesterday?"
    scene d20s02-05-mc-look-mk with dissolve
    pause
    scene d20s02-11-mc-talk-mk with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "I assumed it was just because you're a kinky bitch and it got you off."
    scene d20s02-06-mk-talk-mc with dissolve
    play voice3 min_yes_aga noloop
    mk "That too.{w} Nordin has particular tastes, from what I've heard."
    mk "He might choke me. It might seem like he's hurting me.{w} He might even hurt me."
    scene d20s02-07-mc-talk-mk with dissolve
    play voice2 mc_scared_huuuh2 noloop
    mc "Fuck, Maria, I didn't know."
    scene d20s02-08-mk-talk-mc with dissolve
    play voice3 min_no_nah noloop
    mk "Doesn't matter. I'm ready for it.{w} I might even enjoy it."
    mk "I mean, he is a pretty disgusting old man, but..."
    scene d20s02-09-mc-talk-mk with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I'm having second thoughts. We should reconsider this."
    scene d20s02-10-mk-talk-mc with dissolve
    play voice3 min_no_simple noloop
    if is_antagonist_mode is True:
        mk "No.{w} We're only going to get one shot at this, so don't interrupt until you're certain you have him caught in the act."
    elif True:
        mk "No.{w} We're only going to get one shot at this, so don't interrupt until you're certain he's sufficiently satisfied."
    scene d20s02-11-mc-talk-mk with dissolve
    play voice2 d2s9_confused noloop volume 1.5
    mc "If you say so.{w} If you want to back out of this - no harm, no foul. I won't hold it against you."
    scene d20s02-12-mk-talk-mc with dissolve
    play voice3 min_happy_mmm noloop
    mk "Don't worry, [mcname]. I've done worse things for worse reasons."
    play sound maria_kiss1
    scene d20s02-13-mk-kiss-mc with dissolve
    play voice2 mc_pain_mff1 noloop
    pause
    scene d20s02-14-mc-inner-talk with dissolve
    mct "What?{w} I'm so confused."
    scene d20s02-15-mk-talk-mc with dissolve
    play voice3 min_happy_relief noloop
    mk "I've got this."
    scene d20s02-16-mk-talk-mc with dissolve
    mk "Just make sure you do your part."
    scene d20s02-17-mc-inner-talk with dissolve
    play voice2 d1s1_mmm noloop
    mct "And away she goes.{w} Let's see what happens."
    stop music fadeout 3.0

label replay_d20s02rn hide:

    scene d20s02-18-mk-enter-office with fade
    pause
    scene d20s02-19-mk-talk-rn with dissolve
    play voice3 min_thinking_emm noloop
    mk "Professor... ?"
    mk "Professor Nordin?"
    scene d20s02-20-mk-walk-rn with dissolve
    pause
    scene d20s02-21-mk-talk-rn with dissolve
    play voice3 min_arrogant_hm noloop
    mk "I wanted to interact with you, sir."
    $ renpy.music.set_volume(0.45, 3.0, "music")
    queue music urine
    scene d20s02-22-mk-talk-rn with dissolve
    play voice3 min_happy_phew noloop
    mk "Whew. Is it hot in here?"
    scene d20s02-23-rn-talk-mk with dissolve
    play voice4 pete_yes_simple1 noloop
    rn "Yes, Miss Kovalevich. It is rather warm. I prefer it that way.{w} You'll understand when you get older."
    scene d20s02-24-mk-talk-rn with dissolve
    play voice3 min_thinking_oh noloop
    mk "Oh good, I thought it was just me.{w} Hot, that is."
    scene d20s02-25-rn-talk-mk with dissolve
    play voice4 pete_thinking_hmm1 noloop
    rn "What can I do for you, Miss Kovalevich?"
    scene d20s02-26-mk-talk-rn with dissolve
    play voice3 min_thinking_hmm2 noloop
    mk "Well, I've heard that you are always available at these hours for your students."
    scene d20s02-27-rn-talk-mk with dissolve
    play voice4 pete_yes_ugu1 noloop
    rn "Obviously."
    scene d20s02-28-mk-talk-rn with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    mk "Is it true, Professor Nordin?{w} Are you available?"
    play voice4 pete_angry_cough2 noloop
    scene d20s02-29-rn-talk-mk with dissolve
    rn "I'm rapidly running out of availability and you don't seem to be getting any closer to telling me what this is about."
    scene d20s02-30-mk-talk-rn with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    mk "It's about my pencil..."
    scene d20s02-31-rn-talk-mk with dissolve
    play voice4 pete_disappointed_mmf1 noloop
    rn "That didn't affect your grades. What you and Mister Young get up to in private is none of my concern."
    scene d20s02-32-mk-talk-rn with dissolve
    play voice3 min_thinking_mhh noloop
    mk "Did you like it?"
    scene d20s02-33-rn-talk-mk with dissolve
    play voice4 pete_thinking_eeh1 noloop
    rn "Excuse me?"
    scene d20s02-34-mk-talk-rn with dissolve
    play voice3 polly_laugh2 noloop
    mk "When I dropped my pencil.{w} Did you enjoy what you saw?"
    scene d20s02-35-rn-talk-mk with dissolve
    play voice4 pete_angry_hmm6 noloop
    rn "Miss Kovalevich, you've already passed your exams for this semester - with flying colors I might add."
    scene d20s02-36-mk-talk-rn with dissolve
    play voice3 min_yes_simple noloop
    mk "Exactly, Ronald.{w} We're not Professor and Student anymore. At least not for the summer."
    mk "It could be a long, hard summer for both of us."


    $ Lovense.stop()

    scene d20s02-35-rn-talk-mk with dissolve
    play voice4 pete_surprised_what3 noloop
    rn "Is this some kind of prank?"
    play sound sfx_skirt_off3 volume 2.5
    scene d20s02-37-mk-talk-rn with dissolve
    $ Lovense.vibrate(1)
    play voice3 polly_laugh3 noloop
    mk "Tell me, Professor, what name do you prefer?"
    scene d20s02-38-mk-talk-rn with dissolve
    mk "Ronald?"
    play sound sfx_cloth_rustling2 volume 2.3
    scene d20s02-39-mk-talk-rn with dissolve
    mk "Ron?"
    scene d20s02-40-mk-talk-rn with dissolve
    mk "Professor?"
    scene d20s02-41-mk-talk-rn with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    mk "Daddy?"
    play sound sfx_underpants_off1 volume 3.0
    scene d20s02-45-mk-turn-back with dissolve
    mk "Master?"
    scene d20s02-46-rn-talk-mk with dissolve
    play voice4 pete_angry_cough1 noloop
    rn "Miss Kovalevich.{w} *Ahem*, Maria. I'm not sure what you've heard."
    scene d20s02-47-mk-talk-rn with dissolve
    play voice3 min_surprised_oh noloop
    mk "Never listen to gossip or rumors, Master. You've taught us that well."
    scene d20s02-48-rn-talk-mk with dissolve
    play voice4 pete_thinking_hmm7 noloop
    rn "This could be considered a compromising position..."
    scene d20s02-49-mk-talk-rn with dissolve
    play voice3 min_disappointed_ehh2 noloop
    mk "Don't worry, Master.{w} I locked the door on the way in."
    scene d20s02-50-mc-inner-talk with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.5
    mct "Well, that's a lie. I hope he believes it."
    mct "Otherwise this is going to get real awkward real fast."
    scene d20s02-51-rn-talk-mk with dissolve
    play voice4 pete_disappointed_ehh1 noloop
    rn "You can't know what you're saying."
    scene d20s02-52-mk-talk-rn with dissolve
    play voice3 dahlia_arrogant_hm noloop
    mk "Believe me, I do.{w} I did my research."
    scene d20s02-53-rn-talk-mk with dissolve
    play voice4 pete_arrogant_hm2 noloop
    rn "What do you mean?"
    scene d20s02-54-mk-talk-rn with dissolve
    play voice3 maria_argh noloop
    if persistent.is_special is True and is_antagonist_mode is True:
        mk "I've read the court reports. Her testimony is a matter of public record."
    elif True:
        mk "I tracked down your last girlfriend.{w} She told me exactly what to expect."
    scene d20s02-51-rn-talk-mk with dissolve
    play voice4 pete_surprised_oh1 noloop
    rn "You're... serious?"
    scene d20s02-52-mk-talk-rn with dissolve
    play voice3 min_yes_ugu noloop
    mk "I am.{w} And still I'm here. Offering myself to you."
    scene d20s02-55-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "I have a bad feeling about this..."
    scene d20s02-57-rn-talk-mk with dissolve
    play voice4 pete_surprised_huh3 noloop
    rn "Then you should know what I expect from you."
    scene d20s02-56-mk-talk-rn with dissolve
    play voice3 min_surprised_ehh1 noloop
    mk "I apologize for not letting you tear my clothes off.{w} I hope that can wait until later."
    scene d20s02-59-rn-talk-mk with dissolve
    play voice4 pete_happy_laugh1 noloop
    rn "I don't keep a cage or collar here. That will need to wait until I get you home."
    scene d20s02-58-mk-talk-rn with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    mk "I can think of nothing that I would rather do."
    mk "But before we get to that. I need something from you."
    scene d20s02-60-mk-touch-rn with dissolve
    play voice4 pete_disappointed_oof1 noloop
    rn "You should know not to make demands."
    scene d20s02-61-mk-talk-rn with dissolve
    play voice3 min_no_uhuh noloop
    mk "I wouldn't dream of it. Consider it a good faith gesture, or payment for my services."
    scene d20s02-60-mk-touch-rn with dissolve
    play voice4 pete_angry_hmm5 noloop
    rn "What do you have in mind?"
    scene d20s02-62-mk-talk-rn with dissolve
    play voice3 min_disappointed_off noloop
    mk "You taught us never to listen to gossip or rumors. I need proof."
    mk "Right here. Right now."
    scene d20s02-63-mk-talk-rn with dissolve
    play voice3 dahlia_old_moan1 noloop
    if persistent.is_special is True:
        mk "I want you to rape the shit out of me right here on your desk."
    elif True:
        mk "I want you to fuck me senseless right here on your desk."
    mk "Can you do that for me, Ronald?"
    if persistent.is_special is True:
        play voice3 maria_ah2 noloop
        $ Lovense.vibrate(3)
        scene d20s02-64-c1-rn-choke-mk with dissolve
        pause
        play voice4 pete_angry_ergh4 noloop
        scene d20s02-65-c1-rn-talk-mk with dissolve
        rn "Don't worry, cunt.{w} You'll live to regret this."
        scene d20s02-66-c1-rn-choke-mk-2 with dissolve
        pause
        scene d20s02-67-c1-rn-talk-mk with dissolve
        play voice4 pete_angry_ehh1 noloop
        rn "Although you might stop breathing."
    elif True:
        scene d20s02-68-c2-mk-talk-rn with dissolve
        play voice3 min_arrogant_huh2 noloop
        mk "I'll make it even easier for you. You can start with my mouth."
        scene d20s02-69-c2-mk-talk-rn with dissolve
        mk "Don't worry, I can hold my breath a long time."
        scene d20s02-70-c2-mk-lay-down with dissolve
        pause
    play sound sfx_jeans_on1
    scene d20s02-71-rn-undress with dissolve
    pause
    scene d20s02-72-rn-talk-mk with dissolve
    play voice4 pete_arrogant_heh5 noloop
    rn "If the worst should happen, I'm CPR certified."
    scene d20s02-73-mk-talk-rn with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    mk "I didn't know that, Professor."
    scene d20s02-72-rn-talk-mk with dissolve
    play voice4 pete_angry_ehh2 noloop
    rn "Call me, \"Master\"."
    scene d20s02-73-mk-talk-rn with dissolve
    play voice3 min_yes_simple noloop
    mk "Yes, Master!"
    play voice3 samiya_mfff3 noloop
    $ Lovense.vibrate(5)
    scene d20s02-a74-1 mk-mout-fuck-anim-01 with dissolve
    pause
    $ renpy.music.set_volume(0.8, 1.5, "music")
    play voice4 pete_sex_openmoans1
    play voice3 aaleyah_sucking_deep
    $ Lovense.pattern("5;8", 1400)
    scene d20s02rn-a2
    pause
    stop voice3 fadeout 1.0
    $ renpy.music.set_volume(0.5, 1.5, "music")
    scene d20s02-75-rn-talk-mk with dissolve
    $ Lovense.stop()
    $ Lovense.vibrate(5)
    play voice4 pete_surprised_ah noloop
    rn "And I think I'll call you...{w} Cum Slut."
    rn "Learn it. Memorize it. Become it."
    $ renpy.music.set_volume(0.8, 1.5, "music")
    play voice4 pete_sex_openmoans1
    play voice3 aaleyah_sucking_deep
    $ Lovense.pattern("5;8", 1400)
    scene d20s02rn-a3 with dissolve
    pause
    stop voice3 fadeout 1.0
    $ renpy.music.set_volume(0.5, 1.5, "music")
    $ Lovense.stop()
    $ Lovense.vibrate(5)
    scene d20s02-77-rn-talk-mk with dissolve
    play voice4 pete_angry_argh3 noloop
    rn "Cum Slut is who you are."
    $ Lovense.vibrate(6)
    scene d20s02-78-rn-talk-mk with dissolve
    play voice4 pete_angry_ergh3 noloop
    rn "Cum Slut is what you are."
    $ Lovense.vibrate(7)
    scene d20s02-79-rn-talk-mk with dissolve
    play voice4 pete_angry_ergh5 noloop
    rn "Cum Slut is all you will ever be."
    $ Lovense.vibrate(8)
    scene d20s02-80-rn-talk-mk with dissolve
    rn "Cum Slut is who you will be - even after I get bored of you and leave you in a dumpster."
    $ renpy.music.set_volume(0.8, 1.5, "music")
    play voice4 pete_sex_orgasm3
    queue voice4 pete_sex_openmoans1
    play voice3 aaleyah_sucking_deep
    $ Lovense.pattern("5;8", 700)
    scene d20s02rn-a2-f with dissolve
    pause
    scene d20s02rn-a3-f with dissolve
    pause
    $ renpy.music.set_volume(0.15, 1.0, "voice3")
    $ renpy.music.set_volume(0.15, 1.0, "voice4")
    $ renpy.music.set_volume(0.5, 1.5, "music")
    scene d20s02-81-mc-inner-talk with dissolve
    play voice2 d1s5_orgasm noloop
    mct "Fuck. This can't be what she came prepared for."
    mct "I didn't mean to ask this much of her."
    scene d20s02-82-mc-inner-talk with dissolve
    play voice2 d1s5_mchappy noloop volume 1.4
    mct "Technically he is penetrating her - but it's only her mouth.{w} That might be enough."
    menu:
        "Interrupt them"(hint="d20s02rnm01c01") if True:
            $ d20s02rn_stop_facefuck = True
            jump d20s02rn_interrupt
        "Let them keep going"(hint="d20s02rnm01c02") if True:

            jump d20s02rn_cont_anal

label d20s02rn_cont_anal:

    $ Lovense.stop()
    $ Lovense.vibrate(3)
    $ renpy.music.set_volume(1.0, 1.0, "voice3")
    $ renpy.music.set_volume(1.0, 1.0, "voice4")
    play voice3 samiya_mfff2 noloop
    scene d20s02-83-rn-talk-mk with dissolve
    play voice4 pete_angry_hmm4 noloop
    rn "Enough of that."
    rn "It's time that I try the other end."
    scene d20s02-84-mk-rotate with dissolve
    pause
    scene d20s02-85-mk-bend with dissolve
    pause
    scene d20s02-86-mk-talk-rn with dissolve
    play voice3 maria_aah noloop
    mk "Would you like to take my virginity, Master?"
    scene d20s02-87-rn-talk-mk with dissolve
    play voice4 pete_arrogant_pff1 noloop
    rn "Don't lie to me, Cum Slut.{w} I'm sure all your holes have been well used and abused."
    scene d20s02-88-mk-talk-rn with dissolve
    play voice3 min_disappointed_mph noloop
    mk "I'm sorry, Master."
    scene d20s02-89-rn-talk-mk with dissolve
    play voice4 pete_pain_mmm3 noloop
    rn "That's better."
    $ Lovense.vibrate(4)
    scene d20s02-90-mk-anal-anim with dissolve
    pause
    play voice3 maria_orgasming noloop
    $ Lovense.vibrate(6)
    scene d20s02-91-mk-expression with dissolve
    stop voice3 fadeout 0.165
    mk "OH FUCK!!"
    scene d20s02-92-rn-talk-mk with dissolve
    play voice4 pete_arrogant_huh2 noloop
    rn "What was that, Cum Slut?"
    scene d20s02-93-mk-talk-rn with dissolve
    play voice3 min_angry_breath noloop
    mk "Use me however you like, Master!"
    scene d20s02-a90-3 mk-anal-anim-01 with dissolve
    play voice4 pete_pain_mmm1 noloop
    rn "Better.{w} In the future, keep yourself lubed and prepared."
    play voice3 min_old_longmoan1
    play voice4 pete_sex_openmoans2
    $ Lovense.pattern("6;10", 1400)
    scene d20s02rn-a6
    mk "Yes, Master!!"
    pause
    $ renpy.music.set_volume(0.9, 1.5, "music")
    scene d20s02rn-a4 with dissolve
    pause
    scene d20s02rn-a5 with dissolve
    pause
    play voice4 pete_sex_openmoans1
    $ Lovense.pattern("6;10", 700)
    scene d20s02rn-a6-f with dissolve
    pause
    scene d20s02rn-a4-f with dissolve
    pause
    scene d20s02rn-a5-f with dissolve
    pause
    $ renpy.music.set_volume(0.15, 1.0, "voice3")
    $ renpy.music.set_volume(0.15, 1.0, "voice4")
    $ renpy.music.set_volume(0.4, 1.5, "music")
    scene d20s02-94-mc-inner-talk with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "She said this might happen.{w} He's fucking her ass. I could interrupt them now."
    menu:
        "Interrupt them"(hint="d20s02rnm02c01") if True:
            $ d20s02rn_stop_anal = True
            jump d20s02rn_interrupt
        "Let them keep going"(hint="d20s02rnm02c02") if True:

            jump d20s02rn_cont_atm

label d20s02rn_cont_atm:

    $ renpy.music.set_volume(1.0, 1.0, "voice3")
    $ renpy.music.set_volume(1.0, 1.0, "voice4")
    scene d20s02-96-mk-talk-rn with dissolve
    play voice3 maria_orgasming
    mk "Master! Master!! Master!!!"
    mk "Fuck Yes, Master!"
    scene d20s02-97-mk-talk-rn with dissolve
    mk "Your Cum Slut Is Happy To Serve You, Master!!!"
    stop voice3 fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(3)
    scene d20s02-98-rn-talk-mk with dissolve
    play voice4 pete_happy_laugh3 noloop
    rn "Time to spin you around again."
    play voice3 samiya_mfff noloop
    $ Lovense.vibrate(5)
    scene d20s02-99-01 mk-suck-anim_c100_i with dissolve
    pause
    $ renpy.music.set_volume(0.8, 1.5, "music")
    play voice4 pete_sex_openmoans2
    play voice3 polly_licking
    $ Lovense.pattern("5;8", 1400)
    scene d20s02rn-a1-1
    pause
    scene d20s02rn-a1-2 with dissolve
    pause
    stop voice3 fadeout 1.5
    $ Lovense.stop()
    $ Lovense.vibrate(4)
    scene d20s02-100-rn-talk-mk with dissolve
    play voice4 pete_pain_mmm4 noloop
    rn "That's a good cocksucking dyke."
    rn "Make it nice and clean."
    play voice4 pete_sex_openmoans1
    play voice3 polly_licking
    $ Lovense.pattern("5;8", 1400)
    scene d20s02rn-a1-3 with dissolve
    pause
    scene d20s02rn-a1-4 with dissolve
    pause
    stop voice3 fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(4)
    scene d20s02-102-rn-talk-mk with dissolve
    play voice4 pete_pain_cough2 noloop
    rn "Because it's going into your worthless cunt next."
    $ renpy.music.set_volume(0.4, 1.5, "music")
    scene d20s02-103-mc-inner-talk with dissolve
    play voice2 mc_pain_mff4 noloop
    mct "Fuck this is hard to watch. He's actually making her ATM his cock."
    mct "I should probably interrupt them before..."
    menu:
        "Interrupt them"(hint="d20s02rnm03c01") if True:
            $ d20s02rn_stop_atm = True
            jump d20s02rn_interrupt
        "Let them keep going"(hint="d20s02rnm03c02") if True:

            jump d20s02rn_cont_creampie

label d20s02rn_cont_creampie:

    $ d20s02rn_stop_creampie = True

    scene d20s02-104-mc-inner-talk with dissolve
    play voice2 d14s16_smell noloop
    mct "Fuck it, I need to see how this ends."
    scene d20s02-105-rn-talk-mk with dissolve
    play voice4 pete_pain_mmm6 noloop
    rn "And now for the final proof that you belong to me..."
    rn "... until you are properly collared and caged, of course."
    scene d20s02-106-rn-talk-mk with dissolve
    play voice4 pete_happy_mmm1 noloop
    rn "Cum Slut, give me your pussy."
    scene d20s02-107-mk-rotate with dissolve
    pause
    scene d20s02-108-rn-talk-mk with dissolve
    play voice4 pete_disappointed_geh1 noloop
    rn "Tell me what you are."
    scene d20s02-109-mk-talk-rn with dissolve
    play voice3 min_disgust_nah noloop
    mk "I'm your Cum Slut, Master!"
    $ Lovense.vibrate(6)
    scene d20s02-110-mk-fuck-anim with dissolve
    play voice4 pete_pain_arrr noloop
    rn "Damn Right."
    scene d20s02-111-rn-talk-mk with dissolve
    rn "Say It Again!"
    scene d20s02-112-mk-talk-rn with dissolve
    play voice3 dahlia_pain_sobs noloop
    mk "I'm your Cum Slut, Master!"
    $ renpy.music.set_volume(0.8, 1.5, "music")
    play voice4 pete_angry_hmm3 noloop
    queue voice4 pete_sex_openmoans2
    play voice3 min_pain_sobs1
    queue voice3 dahlia_sex_openmoans1
    $ Lovense.pattern("7;12", 1300)
    scene d20s02rn-a7
    rn "Again!!!"
    pause
    scene d20s02rn-a8 with dissolve
    mk "I'm your Cum Slut, Master!!"
    pause
    scene d20s02rn-a9 with dissolve
    pause
    play voice3 dahlia_sex_orgasming2
    $ Lovense.pattern("7;12", 700)
    scene d20s02rn-a7-f with dissolve
    pause
    scene d20s02rn-a8-f with dissolve
    pause
    scene d20s02rn-a9-f with dissolve
    pause
    play voice4 pete_angry_ergh5 noloop
    play voice3 maria_orgasming
    $ Lovense.stop()
    $ Lovense.vibrate(18)
    scene d20s02-113-mk-creampie-2 with hpunch
    pause
    scene d20s02-114-rn-talk-mk with dissolve
    play voice4 pete_pain_argh3 noloop
    rn "TAKE MY CUM YOU SLUT!!"
    scene d20s02-115-mk-talk-rn with dissolve
    mk "THANK YOU MASTER!!!"
    stop voice4 fadeout 1.0
    stop voice3 fadeout 1.0
    $ renpy.music.set_volume(0.4, 1.5, "music")
    $ Lovense.vibrate(1)
    scene d20s02-104-mc-inner-talk with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "Now is definitely the time to interrupt them."

    jump d20s02rn_interrupt

label d20s02rn_interrupt:

    $ unlock_gallery_slot("scene", "d20s02rn")
    $ renpy.music.set_volume(1.0, 2.0, "voice3")
    $ renpy.music.set_volume(1.0, 2.0, "voice4")
    stop voice3 fadeout 1.0
    stop voice4 fadeout 1.0
    play sound sfx_door_closed2 volume 1.4
    $ renpy.music.set_volume(0.25, 1.5, "music")
    scene d20s02-116-mc-enter-office with fade


    $ Lovense.stop()

    pause
    scene d20s02-117-mc-talk-rn with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Good morning, Professor.{w} I see you're enjoying my present."
    scene d20s02-118-rn-talk-mc with dissolve
    play voice4 pete_thinking_hmm3 noloop
    rn "I see.{w} Good morning, Mister Young."
    scene d20s02-119-rn-talk-mc with dissolve
    play voice4 pete_thinking_hm noloop
    rn "Are you here to watch?"
    scene d20s02-120-mc-talk-rn with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Oh, I think I've seen enough. I hope it was sufficiently satisfying."
    scene d20s02-121-rn-talk-mc with dissolve
    play voice4 pete_yes_simple1 noloop
    if is_antagonist_mode is False:
        rn "Quite satisfying. I'm sure this will reflect positively on your exam today."
    elif True:
        rn "Quite satisfying.{w} Do you plan to blackmail me?"
    scene d20s02-122-mc-talk-rn with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "I prefer to think it was a friendly transaction - influencing your disposition."
    scene d20s02-123-rn-talk-mc with dissolve
    play voice4 pete_disappointed_mmf2 noloop
    rn "Well played."
    $ renpy.end_replay()
    scene d20s02-124-mc-talk-rn with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Of course, it could turn less friendly if needed."
    scene d20s02-125-rn-talk-mc with dissolve
    play voice4 pete_no_uhuh noloop
    rn "That won't be necessary. You won't need to worry about my vote during your exam."
    scene d20s02-126-mc-talk-rn with dissolve
    play voice2 mc_happy_yay4 noloop
    mc "Thank you."
    scene d20s02-125-rn-talk-mc with dissolve
    play voice4 pete_thinking_hmm2 noloop
    rn "You should know that she promised herself to me. To be my pet for the summer."
    scene d20s02-126-mc-talk-rn with dissolve
    play voice2 mc_yes_yeah6 noloop
    mc "I heard that. Unfortunately, she doesn't belong to herself. She already gave herself to another owner."
    scene d20s02-127-rn-talk-mc with dissolve
    play voice4 pete_disappointed_mmm1 noloop
    rn "Is that so?{w} I would be willing to negotiate with you for her."
    scene d20s02-128-mc-talk-rn with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Unfortunately, she doesn't belong to me either. I'm just borrowing her."
    scene d20s02-129-rn-talk-mc with dissolve
    play voice4 pete_thinking_hmm4 noloop
    rn "Hmmm...{w} Please pass my offer on to her owner."
    scene d20s02-130-mc-talk-rn with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "I'll mention it. No promises."
    scene d20s02-131-mk-talk-mc with dissolve
    play voice3 min_happy_relief noloop
    mk "May I clean up and get dressed now?"
    scene d20s02-132-mc-talk-mk with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Please do.{w} Unless you have any objections."
    scene d20s02-133-rn-talk-mc with dissolve
    play voice4 pete_no_nah noloop
    rn "No objection. I am done with her."
    play sound sfx_chair_slide1 volume 1.3
    scene d20s02-134-mc-mk-exit with dissolve
    pause
    scene d20s02-135-rn-talk-mc with dissolve
    play voice4 pete_happy_mmm2 noloop
    rn "Assuming you pass, Mr. Young. I look forward to your presence in my classes next semester."
    scene d20s02-136-mc-talk-rn with dissolve
    play voice2 d3s11b_mcheh noloop
    mc "Thank you, sir."
    scene d20s02-137-rn-talk-mc with dissolve
    play voice4 pete_disappointed_ehh4 noloop
    rn "As for your companion. I do not like being used, duped, and lied to... \"Maria\"."
    scene d20s02-138-mk-talk-rn with dissolve
    play voice3 maria_what noloop
    mk "Sir?"
    scene d20s02-139-rn-talk-mk with dissolve
    play voice4 pete_disappointed_mmf3 noloop
    rn "I suggest you find a different professor for your future coursework."
    scene d20s02-140-mk-talk-rn with dissolve
    play voice3 min_thinking_oh noloop
    mk "I didn't mean-"
    scene d20s02-141-mk-talk-rn with dissolve
    play voice3 min_thinking_hmm3 noloop
    mk "Yes, sir. I understand."
    play sound sfx_door_openclosed2
    scene d20s02-142-outside-rn-office with dissolve
    pause
    scene d20s02-143-mk-talk-mc with dissolve
    play voice3 maria_argh noloop
    mk "I didn't realize I was misleading him. I thought the only way I could help you-"
    scene d20s02-144-mc-talk-mk with dissolve
    play voice2 mc_yes_yeah1 noloop
    if d19s07_friend is True:
        mc "I know.{w} I would never let that happen to a friend of mine."
    elif True:
        mc "I know.{w} Luckily, I remembered what you promised to AmRose."
    play sound sfx_cloth_rustling4
    scene d20s02-145-mk-hug-mc with dissolve
    pause
    scene d20s02-146-mk-talk-mc with dissolve
    play voice3 min_disappointed_ehh1 noloop
    mk "Thank you."

    stop music fadeout 3.0
    jump d20s02zw
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
