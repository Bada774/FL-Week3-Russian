image d18s01-a1-f = Movie(play = "images/Day-18/s01/anim/d18s01-a01-2x-50fps.webm", start_image = "d18s01-a01 mc-lc-animation-start-bj-anim01-01_i")
image d18s01-a1 = Movie(play = "images/Day-18/s01/anim/d18s01-a01-4x-60fps.webm", start_image = "d18s01-a01 mc-lc-animation-start-bj-anim01-01_i")
image d18s01-a2-f = Movie(play = "images/Day-18/s01/anim/d18s01-a02-2x-50fps.webm", start_image = "d18s01-a02 mc-lc-animation-start-bj-anim02-01_i")
image d18s01-a2 = Movie(play = "images/Day-18/s01/anim/d18s01-a02-4x-60fps.webm", start_image = "d18s01-a02 mc-lc-animation-start-bj-anim02-01_i")
image d18s01-a3-f = Movie(play = "images/Day-18/s01/anim/d18s01-a03-2x-50fps.webm", start_image = "d18s01-a03 mc-lc-animation-start-bj-anim03-01_i")
image d18s01-a3 = Movie(play = "images/Day-18/s01/anim/d18s01-a03-4x-60fps.webm", start_image = "d18s01-a03 mc-lc-animation-start-bj-anim03-01_i")

label replay_d18s01:
label d18s01:

    $ d18s01_points = 6

    scene black
    if not _in_replay:
        show screen scene_transistion(_("Thursday\nDay-18"))
        with Fade(0.5, 0.5, 0.5)
        pause
        hide screen scene_transistion

    $ Lovense.stop()

    play voice2 d1s1_mmm noloop
    play voice3 mc_sex_sucking_slow1 volume 0.4 fadein 3.0
    mct "Oh fuck yes.{w}... Dream slut, you're going to drain me dry..."
    $ Lovense.vibrate(3)
    mct "Wait...{w} just a second...{w} I've never cum in a dream."
    mct "Someone's actually on my dick!"
    play voice3 maria_kiss1 noloop
    $ Lovense.vibrate(4)
    scene d18s01-01 mc-lc-eyes-open-bj-kiss with Fade(0.1, 0.1, 2.5)
    $ renpy.music.set_volume(0.7, 0.0, "music")
    play music deep_romance

    if cage_ntr is True:
        jump d18s01_ntr
    elif True:
        jump d18s01_lc

label d18s01_ntr:

    play voice2 mc_scared_huuuh3 noloop
    mc "Lydia!?!"
    scene d18s01-03 mc-lc-handjob with dissolve
    play voice3 lydia_shhh noloop
    lc "Shhhhhh."
    mct "Oh my fucking cuddely fuzzy Lord I can't believe it!"
    mct "I'm laying here asleep and she's working my fucking cock like a professional fluffer!!"
    scene d18s01-04 mc-lc-handjob-mc-camera with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "You feel so damn good."
    play voice3 lydia_aga noloop
    lc "Just enjoy it."
    play sound4 sfx_handjob_cream1
    play voice2 d7s4_mcbreathing fadein 2.0 volume 0.6
    $ Lovense.vibrate(5)
    scene d18s01-03 mc-lc-handjob with dissolve
    mct "Part of me wants to get up, grab her, and fuck the virgin out of her."
    mct "Mostly I just want to...{w}enjoy..."
    mc "OHHHhhh fucccccccccck."
    scene d18s01-06 mc-lc-blowjob-talk-interrupt with dissolve
    play voice3 lydia_moan1 noloop
    lc "Cum for me, babe"
    mct "I'm gonna cum all over you!"
    stop sound4 fadeout 1.0
    play voice2 mc_angry_errr4 noloop
    $ Lovense.vibrate(13)
    scene d18s01-07 mc-lc-blowjob-cum-shot with hpunch
    pause
    play voice2 d1s5_orgasm2 noloop
    play sound mc_cum_sound1
    scene d18s01-08 mc-lc-blowjob-cum-on-self with vpunch
    stop sound fadeout 0.5
    pause
    $ Lovense.vibrate(1)
    scene d18s01-09 mc-blowjob-cum-on-self-realize with dissolve
    play voice2 mc_disgust_ooh1 noloop
    mc "Oh!{w} Ew!!"
    scene d18s01-09-02 mc-blowjob-cum-on-self-realize with dissolve
    play voice3 lydia_oops noloop
    lc "Looks like that cannon was fully loaded."
    play voice2 mc_happy_hah2 noloop
    mc "Booommmutherfucker."
    scene d18s01-09-03 mc-blowjob-after-talk with dissolve
    play voice3 lydia_haha noloop
    lc "I'm glad I could make you cum that hard."
    scene d18s01-09-04 mc-blowjob-after-talk with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Impressive."
    mct "Especially after...{w} When was the last time I came?"

    jump d18s01_cuddle

label d18s01_lc:

    play voice2 mc_scared_huuuh3 noloop
    mc "Lydia!?!"
    scene d18s01-03 mc-lc-handjob with dissolve
    play voice3 lydia_shhh noloop
    lc "Shhhhhh."
    mct "Oh my fucking snuggly fluffy Lord I can't believe it!"
    $ Lovense.vibrate(8)
    play voice3 mc_sex_sucking_fast2
    scene d18s01-02 mc-lc-eyes-open-bj with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "I'm laying here asleep and she's sucking my fucking cock like a cheap whore!!"
    scene d18s01-04 mc-lc-blowjob-mc-camera with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "You feel so damn good."
    scene d18s01-04 mc-lc-handjob-mc-camera with dissolve
    play voice3 lydia_aga noloop
    lc "Just enjoy it."
    play voice3 mc_sex_sucking_slow2
    play voice4 daisy_sucking
    play voice2 d7s4_mcbreathing volume 0.6
    $ Lovense.pattern("7;12", 1700)
    scene d18s01-a1 with dissolve
    mct "Part of me wants to grab her hair and fuck her face."
    scene d18s01-a2 with dissolve
    if persistent.is_special is True:
        mct "Or maybe get up and take her virginity by force!"
    elif True:
        mct "Or maybe get up and fuck the virginity right out of her!"
    scene d18s01-a3 with dissolve
    mct "Mostly I just want to-"
    mct "-enjoy-"
    play voice3 mc_sex_sucking_fast2
    $ Lovense.pattern("7;12", 900)
    scene d18s01-a1-f with dissolve
    pause
    scene d18s01-a2-f with dissolve
    pause
    play voice2 mc_angry_errr4 noloop
    mc "OHHHhhh fucccccccccck."
    stop voice4 fadeout 1.0
    $ Lovense.stop()
    $ Lovense.vibrate(12)
    scene d18s01-06 mc-lc-blowjob-talk-interrupt with dissolve
    play voice3 lydia_moan1 noloop
    lc "Cum for me, babe"
    play voice3 mc_sex_sucking_fast2
    play voice4 daisy_sucking
    play voice2 d7s4_mcbreathing
    $ Lovense.pattern("9;14", 900)
    scene d18s01-a3-f with dissolve
    pause
    scene d18s01-05 mc-lc-blowjob-mc-view with dissolve
    play voice2 mc_scared_huuuh1 noloop
    mct "I'm gonna cum all over you!"
    stop voice4 fadeout 0.3
    play voice3 dahlia_sex_closedmoan1 noloop
    play voice2 d1s5_orgasm2 noloop
    play sound mc_cum_sound1
    $ Lovense.stop()
    $ Lovense.vibrate(18)
    scene d18s01-04-02 mc-lc-blowjob-cum-lc-face with vpunch
    stop sound fadeout 0.5
    pause
    play voice2 d1s5_orgasm noloop
    play voice3 dahlia_sex_closedmoan2 noloop
    scene d18s01-04-03 mc-lc-blowjob-cum-lc-face with vpunch
    pause
    play voice2 mc_scared_oh2 noloop
    mc "Oh!{w} Yeah!!"
    scene d18s01-04-04 mc-lc-blowjob-cum-lc-face-talk with dissolve
    $ Lovense.vibrate(2)
    play voice3 lydia_oops noloop
    lc "Looks like that cannon was fully loaded."
    lc "I'm glad I could make you cum that hard."
    play voice2 mc_yes_yeah1 noloop
    mc "Impressive."
    scene d18s01-04-03 mc-lc-blowjob-cum-lc-face with dissolve
    mct "Especially after...{w} When was the last time I came?"
    $ renpy.end_replay()
    $ unlock_gallery_slot("scene", "d18s01lc")

    jump d18s01_cuddle

label d18s01_cuddle:

    $ renpy.music.set_volume(0.35, 2.0, "music")
    scene d18s01-10 mc-lc-cuddle with Fade(0.4, 0.4, 0.4)
    $ Lovense.stop()
    play voice3 dahlia_thinking_hmm4 noloop
    lc "That was spectacular.{w} I wish we had gotten it on film."
    play voice2 mc_happy_a1 noloop
    mc "There will be plenty of opportunities for that."
    scene d18s01-11-01 mc-lc-phone-alert with dissolve
    play voice3 lydia_thinking noloop
    lc "I'll hold you to that promise."
    scene d18s01-11-02 mc-lc-phone-alert with dissolve
    call buzz from _call_buzz_33
    scene d18s01-12 mc-lc-notice-phone-alert with dissolve
    pause
    scene d18s01-14 mc-lc-looking-at-phones with dissolve
    play voice2 d1s5_mcthinks noloop
    mct "Stacy sent me something. \"My apartment. ASAP.\""
    mct "\"We have treats. Punch & Pie.\""
    mct "Punch and pie? What does she think this is, South Park?"
    if date_mes is True:
        play sound sfx_phone_tapping1 volume 1.5
        scene d18s01-16 mc-lc-min-response-text with dissolve
        mct "Looks like Min and/or Squizzle also texted me."
        stop sound fadeout 1.0
        scene d18s01-15 mc-lc-texts-upclose-c3 with dissolve
        mct "\"Hey sexy mama, wanna kill all humans\""
        mct "Yeah, yeah. I get the joke. Does everyone use this?"
        mct "\"Study. Finals. My place. Be there. Yes?\""
        scene d18s01-17 mc-lc-min-response-text-02 with dissolve
        mct "That sounds more like Min.{w} Sure, I guess I'll be there."
    scene d18s01-14 mc-lc-looking-at-phones with dissolve
    call add_points (d18s01_points) from _call_add_points_21
    mct "I alse got [d18s01_points] points. Nice."
    scene d18s01-18 mc-lc-get-attention with dissolve
    play voice3 lydia_lydiahey noloop
    lc "Hey lover."
    scene d18s01-20 mc-lc-talk-fetish-locator with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "What's up, hon?"
    scene d18s01-19 mc-lc-talk-fetish-locator with dissolve
    play voice3 lydia_hmmmm noloop
    lc "Is this a good time to set up my Fetish Locator account?"
    scene d18s01-22 mc-lc-talk-fetish-locator with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Oh."
    scene d18s01-21 mc-lc-talk-fetish-locator-c1 with dissolve
    play voice3 lydia_oof noloop
    lc "You don't want me to have one?{w} I mean, I'd only get points for the things we do together."
    lc "You know that, right?"
    play voice2 mc_happy_thatsgood noloop
    scene d18s01-10 mc-lc-cuddle with dissolve
    stop voice2 fadeout 0.45
    mc "That's not my-"
    mc "Hmm.{w} Tell you what. Let's get a shower and breakfast and then we can talk about it."
    play voice3 lydia_morningoh noloop
    lc "Oh, okay. Do you want first shower or second shower."
    scene d18s01-23 mc-lc-talk-fetish-locator-close-up with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Is it okay if we shower together?"
    play voice3 dahlia_thinking_hmm3 noloop
    lc "I'm not sure how to say this..."
    mc "It's okay. It's just you and me."
    scene d18s01-24 mc-lc-talk-fetish-locator-hug-excited with dissolve
    play voice3 lydia_huh2 noloop
    lc "FUCK YES!!!"
    play voice2 mc_happy_yay2 noloop
    mc "That's my girl."

    jump d18s01_shower

label d18s01_shower:

    $ renpy.music.set_volume(0.5, 0.0, "sound2")
    play sound2 shower fadein 2.5
    scene d18s01-25 mc-lc-in shower with Fade(0.4, 0.4, 0.4)
    pause
    $ Lovense.vibrate(1)
    play voice2 mc_happy_wow2 noloop
    mc "Goddamn."
    scene d18s01-27 mc-lc-mc-question with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    lc "What are you thinking?"
    scene d18s01-28 mc-lc-lusting-for-lydia with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.5
    mc "You are so goddamn gorgeous..."
    scene d18s01-29 mc-lc-washing-hair-talking with dissolve
    if persistent.is_special is True and date_jdg is True:
        mct "... if I wasn't dating you I'd want to rape the shit out of you."
    elif True:
        mct "... I can't believe nobody's fucked the living shit out of you yet."
    scene d18s01-30 mc-lc-washing-hair-talking-close-up with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "I'm just incredibly lucky to share this moment with you."
    play voice3 lydia_laugh noloop
    lc "Well, don't go thinking I get naked in the shower with just any guy."
    play voice2 mc_thinking_hmm3 noloop
    mc "It's a short list?"
    scene d18s01-31 mc-lc-talk-facing-each-ther with dissolve
    play voice3 lydia_uhuh noloop
    lc "You're the first and only."
    if date_mes is True:
        mct "True enough. Min isn't a guy."
    scene d18s01-31-02 mc-lc-talk-facing-each-other with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I'm worried that I won't be able to get through this shower-"
    play voice3 dahlia_thinking_hmm2 noloop
    lc "Without plucking my virginity?"
    play voice2 mc_yes_yes1 noloop
    mc "At the very least."
    scene d18s01-31-03 mc-lc-talk-facing-each-other with dissolve
    play voice3 lydia_hmmmm noloop
    lc "I'm...{w} not ready for that.{w} Just yet."
    play voice2 mc_yes_ugu1 noloop
    mc "I understand."
    lc "Besides, there was something you wanted to talk to me about."
    scene d18s01-30 mc-lc-washing-hair-talking-close-up with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "There was?"
    play voice3 dahlia_disappointed_hmm1 noloop
    lc "I'm not a fool.{w} There's something you've wanted to tell me for a while now."
    scene d18s01-31-02 mc-lc-talk-facing-each-other with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "Before you were naked, wet, and lathering in front of me?"
    play voice3 dahlia_disappointed_ehh3 noloop volume 0.65
    lc "Something about that app...?"
    scene d18s01-31 mc-lc-talk-facing-each-ther with dissolve
    play voice2 mc_pain_rrrr noloop
    mc "FUCK! Fetish Locator.{w} I'm sorry, my brain was..."
    play voice3 dahlia_yes_ugu noloop
    lc "Your brain wasn't doing the thinking for a little bit there."
    scene d18s01-31-02 mc-lc-talk-facing-each-other with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Fetish Locator. Right.{w} I just need a moment."
    play sound sfx_handjob_cream1 volume 8.0
    $ Lovense.vibrate(3)
    scene d18s01-32 mc-lc-lather-boobs with dissolve
    stop sound fadeout 5.0
    play voice3 dahlia_thinking_mmm2 noloop
    lc "Is this helping?"
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah.{w} Fuck.{w} No... Yes?"
    lc "What exactly is it you want to tell me about that sex game you're playing?"
    scene d18s01-33 mc-lc-eye-candy-talk with dissolve
    play voice2 d1s1_mmm noloop
    mct "FUCK it's distracting as hell to see her like this."
    lc "Think, think, think..."
    scene d18s01-34-01 mc-lc-think with dissolve
    mct "Think, THink, THINK!!!"

    $ Lovense.stop()

    scene d18s01-34-02 mc-lc-talk-blackmail with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    if is_antagonist_mode is False:
        mc "The VIP Program."
    elif True:
        mc "Blackmail."
    scene d18s01-34-06 mc-lc-talk-blackmail-alt-view with dissolve
    play voice3 dahlia_surprised_what noloop
    lc "What?"
    play voice2 mc_arrogant_hm3 noloop
    if is_antagonist_mode is False:
        mc "Fetish Locator has a VIP Program.{w}.. and I've teamed up with some other people to win the $$1kk prize."
    elif True:
        mc "Fetish Locator is blackmailing me.{w}.. and some other people."
    play voice3 lydia_ah noloop
    lc "What?!"
    scene d18s01-34-04 mc-lc-talk-blackmail with dissolve
    play voice2 mc_thinking_mmm3 noloop
    if is_antagonist_mode is False:
        mc "There are three other people I know in the VIP Program.{w} But my team includes a couple people who aren't even playing the game."
        lc "You're telling me that this stupid sex app somehow has $$1kk to give away???"
    elif True:
        mc "Three of them, at least.{w} I don't know what they have, but it's gotta be bad."
        lc "You're telling me that this stupid sex app is somehow blackmailing you???"
    scene d18s01-34-07 mc-lc-talk-blackmail-alt-view with dissolve
    play voice3 dahlia_arrogant_pff noloop
    lc "Your pictures are already all over it!!"
    lc "How many women you've fucked... it's public knowledge by now!"
    if is_antagonist_mode is False:
        lc "You're doing all this for money?! Isn't that prostitution?!?!"
    elif True:
        lc "What the fuck could it be blackmailing you with?!?!"
    scene d18s01-34-03 mc-lc-talk-blackmail with dissolve
    play voice2 mc_no_no5 noloop
    mc "At first it was something simple... not that important."
    lc "I don't understand."
    scene d18s01-34-05 mc-lc-talk-blackmail with dissolve
    play voice2 mc_disappointed_meh1 noloop
    if is_antagonist_mode is False:
        mc "It doesn't matter. The important thing is that you understand I'm not playing the game just for fun."
    elif True:
        mc "It doesn't matter. The important thing is that you understand that Fetish Locator is NOT to be trusted."
    play voice3 dahlia_thinking_hmm1 noloop
    lc "I don't... why?"
    play voice2 mc_thinking_mmm3 noloop
    if is_antagonist_mode is False:
        mc "It's all about the prize money. Well, almost entirely. It is also fun."
    elif True:
        mc "Because it blackmails people. It forces us to do things."

    if cage_ntr is True:
        jump d18s01_shower_ntr
    elif True:
        jump d18s01_shower_lc

label d18s01_shower_ntr:

    scene d18s01-35 mc-lc-talk-question with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    if is_antagonist_mode is False:
        lc "You're doing all this for money?"
    elif True:
        lc "You're blackmailed?"
    play voice2 mc_yes_yes1 noloop
    mc "Yes."
    play voice3 dahlia_pain_ah1 noloop
    if is_antagonist_mode is False:
        lc "All the things you've done!{w} You're basically the poster child for sex on this campus. You've probably fucked every willing woman in town... is it every willing man too?"
    elif True:
        lc "What did you do?!{w} You're basically the poster child for sex. Did you fuck a guy or something?"
    scene d18s01-36 mc-lc-talk-listen with dissolve
    play voice2 mc_no_no3 noloop
    mc "No, nothing like that.{w} Do you think I would care if it was gay sex?"
    scene d18s01-37-02 mc-lc-talk-listen-alt-angle with dissolve
    play voice3 dahlia_pain_argh noloop
    if is_antagonist_mode is False:
        lc "How did you find out about this? Why did you even start playing the game?!"
    elif True:
        lc "Then what are you being blackmailed with?"
    scene d18s01-38 mc-lc-talk-make-excuse with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Look. I don't want to talk about it."
    lc "Tell me."
    scene d18s01-39 mc-lc-talk-make-excuse-alt-look with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "It's nothing. It was a mistake. There was nothing important except how it looked."
    play voice3 dahlia_surprised_huh2 noloop
    lc "So, what did it look like?"
    scene d18s01-38 mc-lc-talk-make-excuse with dissolve
    play voice2 d2s12_emmm noloop
    mc "It looked like..."
    play voice3 lydia_moan1 noloop
    lc "You can trust me. Did you hurt someone? Did you fuck someone you shouldn't have?"
    scene d18s01-46 mc-lc-shocked with dissolve
    lc "What is it?"
    play voice2 d2s9_confused noloop
    mc "Do you remember when we met?"
    play voice3 lydia_morningoh noloop
    lc "At Min's Party? After Jerome tried to-"
    scene d18s01-45 mc-lc-angry-talk-down-shock with dissolve
    play voice2 mc_yes_yeah5 noloop volume 0.8
    mc "Yeah."
    lc "You saved me. He didn't lay a hand on me."
    mc "After that.{w} When you fell asleep."
    scene d18s01-47 mc-lc-shocked-talk with dissolve
    play voice3 dahlia_surprised_oh noloop
    lc "Oh fuck. What did you do to me while I was sleeping?!"
    play voice2 mc_scared_huh3 noloop
    if is_antagonist_mode is False:
        mc "NOTHING!!!{w} Nothing. I just did all that to meet you."
        play voice3 lydia_moan1 noloop
        lc "You started playing Fetish Locator just to meet me?"
    elif True:
        mc "NOTHING!!!{w} Nothing. It just looked like... something."
        play voice3 lydia_moan1 noloop
        lc "What could it possibly look like?"
    scene d18s01-38 mc-lc-talk-make-excuse with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    if is_antagonist_mode is False:
        mc "I've been obsessed with you for months. {w}I almost couldn't help myself from jerking off after you fell asleep."
    elif True:
        mc "It looked like...{w} *sigh* it looked like I was masturbating while in bed next to you."
    scene d18s01-40 mc-lc-angry with dissolve
    play voice3 dahlia_pain_mmh noloop
    lc "WHAT THE FUCK?!"
    mc "It wasn't like that!"
    scene d18s01-41 mc-lc-angry-alt-angle with dissolve
    play voice3 dahlia_pain_ah2 noloop
    lc "So what was it like?!"
    play voice2 mc_arrogant_hm2 noloop volume 1.6
    mc "You fell asleep. I fell asleep."
    lc "And then you decided to jerk off to the thought of Jerome raping me?!?!?!"
    scene d18s01-45 mc-lc-angry-talk-down-shock with dissolve
    play voice2 mc_no_no4 noloop
    mc "NO!!!"
    play voice3 dahlia_pain_ah3 noloop
    lc "You sleeze!!! You jacked off thinking about it!!!"
    play voice2 mc_pain_ou1 noloop
    mc "No! I fell asleep!!!"
    scene d18s01-46 mc-lc-shocked with dissolve
    play voice3 dahlia_surprised_huh1 noloop
    lc "Then why are you hard now?!"
    play voice2 mc_surprised_huh6 noloop
    mc "I don't know!{w} You're naked in the shower with me!"
    scene d18s01-41 mc-lc-angry-alt-angle with dissolve
    play voice3 dahlia_arrogant_hm noloop
    lc "I'm not about to orgasm thinking about some girl involuntarily pegging your ass!!!"
    play voice2 mc_hey_hey1 noloop
    mc "It's nothing like that!!!"
    scene d18s01-42 mc-lc-told-to-leave with dissolve
    play voice3 dahlia_angry_argh2 noloop
    lc "You know what, we're done!"
    play voice2 mc_pain_mff1 noloop
    mc "Hear me out, please!"
    lc "You jerked off thinking I might get raped?!"
    scene d18s01-43 mc-lc-told-to-leave with dissolve
    play voice2 mc_angry_errr1 noloop
    mc "It's nothing like that!"
    play voice3 dahlia_thinking_oh noloop
    lc "Oh, really?"
    scene d18s01-42 mc-lc-told-to-leave with dissolve
    lc "You just happened to be jerking off while I was laying there asleep?"
    lc "It was some wild crazy coincidence?"
    scene d18s01-50 mc-lc-wide-view with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "Please..."
    play voice3 dahlia_sex_closedmoan2 noloop
    lc "Get out."
    play voice2 mc_pain_argh1 noloop
    mc "WILL YOU SHUT UP AND LISTEN TO ME FOR A SECOND!!!!!!!"
    scene d18s01-49 mc-lc-talk-mc side with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Lydia, I respect you.{w} I respect your wishes.{w} I'm gonna leave."
    mc "Just give me a chance when you've calmed down so I can explain myself."
    scene d18s01-42 mc-lc-told-to-leave with dissolve
    play voice3 dahlia_pain_argh noloop
    lc "Let me rephrase."
    lc "GET{w} THE FUCK{w} OUT."
    scene d18s01-52 mc-lc-look-back with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "Fine."
    scene d18s01-44 mc-lc-walk-away with dissolve
    mct "Hopefully she'll calm down later."

    stop music fadeout 3.0
    stop sound2 fadeout 2.0
    jump d18s02

label d18s01_shower_lc:

    scene d18s01-35 mc-lc-talk-question with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    lc "That cannot be true."
    play voice2 d9s2_mcyes2 noloop volume 3.0
    mc "It is."
    play voice3 dahlia_thinking_hmm4 noloop
    if is_antagonist_mode is False:
        lc "How is that possible? Did you pay the app money to participate or something?"
    elif True:
        lc "How is that possible? Is it blackmailing every player???"
    scene d18s01-36 mc-lc-talk-listen with dissolve
    play voice2 mc_no_no3 noloop
    if is_antagonist_mode is False:
        mc "No, of course not. I never really thought about where it got the money. Corporate sponsorship or something?"
    elif True:
        mc "Not everyone. I think there are only a few of us. But, for someone in your position-"
    scene d18s01-37-02 mc-lc-talk-listen-alt-angle with dissolve
    play voice3 dahlia_arrogant_hm noloop
    if is_antagonist_mode is False:
        lc "Okay. I don't see why you don't want me to sign up, though."
    elif True:
        lc "Us? Like you?{w} What has it made you do?"
    scene d18s01-38 mc-lc-talk-make-excuse with dissolve
    play voice2 d2s9_confused noloop
    if is_antagonist_mode is False:
        mc "Well, I mean, someone in your position-"
        play voice3 lydia_huh2 noloop
        lc "You think it would hurt my popularity if I showed my ass on camera?"
    elif True:
        mc "Mandatory challenges with the threat of-"
        play voice3 lydia_huh2 noloop
        lc "The Penis Cage?!?! Oh my-"
    scene d18s01-39 mc-lc-talk-make-excuse-alt-look with dissolve
    play voice2 mc_thinking_hmm5 noloop
    if is_antagonist_mode is False:
        mc "I mean, you're not some dumb blonde like London Qualityinn. You have actual talent and personality."
        lc "And it is up to you whether I expose myself or not?!"
    elif True:
        mc "Yeah, that was a punishment for-"
        lc "And I pushed you to do it. I should have realized!"
    scene d18s01-38 mc-lc-talk-make-excuse with dissolve
    play voice2 mc_disappointed_ah1 noloop
    if is_antagonist_mode is False:
        mc "I think we're getting off topic. I'm just trying to look out for you."
        lc "Tell me about the challenges. What sort of things do you think it would want me to do?"
    elif True:
        mc "It wasn't so bad."
        lc "Still... what else has it forced you to do?"
    mc "It's given me certain goals, but that's not important. The important thing is that you stay away from that app."
    scene d18s01-40 mc-lc-angry with dissolve
    play voice3 dahlia_pain_mmh noloop
    lc "So, all this crazy lewd behavior you've done recently."
    play voice2 mc_yes_yeah4 noloop
    mc "I mean, yeah. I'm not like that normally, but it's been fun-"
    scene d18s01-41 mc-lc-angry-alt-angle with dissolve
    play voice3 dahlia_pain_ah2 noloop
    lc "And it's brought us closer together."
    mc "There is that."
    lc "Bastard!"
    scene d18s01-45 mc-lc-angry-talk-down-shock with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What?"
    play voice3 lydia_moan1 noloop
    lc "It's been using you to get close to me, hasn't it?"
    mc "I don't think so... why?"
    scene d18s01-48 mc-lc-thinking with dissolve
    play voice3 lydia_oops noloop
    lc "FUCK!{w} We even met at that Fetish Locator Party."
    play voice2 mc_thinking_emm1 noloop
    mc "Well, that was before-"
    play voice3 dahlia_thinking_hmm3 noloop
    lc "Do you even like me at all? Or is it just the app pushing you at me???"
    scene d18s01-49 mc-lc-talk-mc side with dissolve
    play voice2 mc_scared_huuuh2 noloop
    mc "Honestly - I've been dreaming about you for months."
    scene d18s01-47 mc-lc-shocked-talk with dissolve
    play voice3 lydia_oof noloop
    lc "I wish I could believe that."
    mc "I swear. I've wanted to be with you since long before this app existed."
    lc "Maybe.{w} I need some time."
    scene d18s01-45 mc-lc-angry-talk-down-shock with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "Are you serious?"
    play voice3 lydia_lydyes noloop
    lc "This is just a lot to process. I need some time alone."
    play voice2 mc_yes_okay2 noloop
    mc "Okay, well-"
    scene d18s01-50 mc-lc-wide-view with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    lc "You finished showering, right?"
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah, yeah. Maybe I can call you later?"
    lc "Maybe.{w} Maybe I should call you instead."
    scene d18s01-49 mc-lc-talk-mc side with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure. I'll be available."
    mc "Just don't mention this on the phone. It listens."
    scene d18s01-41 mc-lc-angry-alt-angle with dissolve
    play voice3 dahlia_pain_ah1 noloop
    lc "Fucking hell."
    play voice2 d1s5b_ehhh noloop
    mc "I'll just go, but I really want to see you again soon."
    scene d18s01-51 mc-lc-leave-talk with dissolve
    play voice3 lydia_hmmmm noloop
    lc "Yeah, me too. {w}I just need some time to process all this."
    scene d18s01-52 mc-lc-look-back with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "Okay."
    scene d18s01-53 mc-lc-good-bye with dissolve
    pause

    stop sound2 fadeout 2.0
    stop music fadeout 3.0
    jump d18s02

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
