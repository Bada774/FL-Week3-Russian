image d15s07-a1-ntr = Movie(play = "images/Day-15/Scene-07/anim/d15s04-55-anim1-60fps.webm", start_image = "d15s04-55-anim1 mc-lc-mes-push-deeper-ntr-anim1-00")
image d15s07-a1-ntr-f = Movie(play = "images/Day-15/Scene-07/anim/d15s04-55-anim1-30fps.webm", start_image = "d15s04-55-anim1 mc-lc-mes-push-deeper-ntr-anim1-00")
image d15s07-a2-ntr = Movie(play = "images/Day-15/Scene-07/anim/d15s04-55-anim2-60fps.webm", start_image = "d15s04-55-anim2 mc-lc-mes-push-deeper-ntr-anim2-00")
image d15s07-a2-ntr-f = Movie(play = "images/Day-15/Scene-07/anim/d15s04-55-anim2-30fps.webm", start_image = "d15s04-55-anim2 mc-lc-mes-push-deeper-ntr-anim2-00")

image d15s07-a1 = Movie(play = "images/Day-15/Scene-07/anim/d15s07-a1-1-2x-50fps.webm", start_image = "d15s07-a1-1 mc-lc-min-mc-piss-anim-1-1-0000")
image d15s07-a2 = Movie(play = "images/Day-15/Scene-07/anim/d15s07-a1-2-2x-50fps.webm", start_image = "d15s07-a1-2 mc-lc-min-mc-piss-anim-1-2-0000")

image d15s07-a3-ntr = Movie(play = "images/Day-15/Scene-07/anim/d15s07-a2-1-2x-50fps.webm", start_image = "d15s07-a2-1 mc-lc-min-mc-piss-anim-2-1-0000")
image d15s07-a3-lc = Movie(play = "images/Day-15/Scene-07/anim/d15s07-a2-3-2x-50fps.webm", start_image = "d15s07-a2-3 mc-lc-min-mc-piss-anim-2-3-0000")

image d15s07-a4-ntr = Movie(play = "images/Day-15/Scene-07/anim/d15s07-a2-2-2x-50fps.webm", start_image = "d15s07-a2-2 mc-lc-min-mc-piss-anim-2-2-0000")
image d15s07-a4-lc = Movie(play = "images/Day-15/Scene-07/anim/d15s07-a2-4-2x-50fps.webm", start_image = "d15s07-a2-4 mc-lc-min-mc-piss-anim-2-4-0000")

image d15s07-a4 = Movie(play = "images/Day-15/Scene-07/anim/d15s07-a3-2-2x-50fps.webm", start_image = "d15s07-a3-2 mc-lc-min-swallow-anim-3-2-0000", image = "d15s07-a3-2 mc-lc-min-swallow-anim-3-2-9999", loop = False)
image d15s07-a5 = Movie(play = "images/Day-15/Scene-07/anim/d15s07-a3-2x-50fps.webm", start_image = "d15s07-00-a3 mes-piss-anim-3-0000", image = "d15s07-00-a3 mes-piss-anim-3-0198", loop = False)

image d15s07-a6 = Movie(play = "images/Day-15/Scene-07/anim/d15s07-a4-1-2x-50fps.webm", start_image = "d15s07-a4-2 mc-lc-min-lc-piss-anim-4-2-0000")
image d15s07-a7 = Movie(play = "images/Day-15/Scene-07/anim/d15s07-a4-2-2x-50fps.webm", start_image = "d15s07-a4-1 mc-lc-min-lc-piss-anim-4-1-0000")

image d15s07-a8 = Movie(play = "images/Day-15/Scene-07/anim/d15s07-a5-2x-50fps.webm", start_image = "d15s07-a5 mc-lc-min-swallow-anim-5-1-0000")
image d15s07-a9 = Movie(play = "images/Day-15/Scene-07/anim/d15s07-a6-2x-50fps.webm", start_image = "d15s07-a6 mc-lc-min-swallow-anim-6-2-0000")

label d15s07:

    $ d15s07_mc_pee = False
    $ d15s07_mc_peed_on = False
    $ d15s07_more_watersports = False
    $ d15s07_points = 0

    if date_mes is False:
        jump d15s08

    scene black
    show screen scene_transistion(_("Later that day"))
    with Fade(0.9, 0.5, 0.5)
    pause

label replay_d15s07 hide:

    $ renpy.music.set_volume(0.02, 0.0, "sound2")
    play sound2 shower fadein 3.0
    hide screen scene_transistion
    scene d15s07-01 mc-bathroom-door
    with Fade(0.5, 0.5, 0.9)
    pause
    mct "Min messaged me to meet her here. I wonder-"
    $ renpy.music.set_volume(0.2, 1.0, "sound2")
    scene d15s07-04 lc-min-sing with dissolve
    play voice4 lydia_shower_sing1 noloop
    lc "And now I tell you openly..."
    $ renpy.music.set_volume(0.02, 0.5, "sound2")
    $ renpy.music.set_volume(0.2, 0.5, "voice4")
    scene d15s07-02 mc-hear-singing with dissolve
    play voice2 d1s5_mchappy noloop
    mct "Wait. {w}Is Lydia singing?"
    $ renpy.music.set_volume(0.2, 2.0, "sound2")
    $ renpy.music.set_volume(1.0, 0.5, "voice4")
    scene d15s07-04 lc-min-sing with dissolve
    queue voice4 lydia_shower_sing2 noloop
    lc "... You have my heart..."
    lc "...so don't hurt me..."
    scene d15s07-05 lc-min-talk-why-sing with dissolve
    lc "...You're everything to me. {w}Hey!"
    play voice3 min_old_argh noloop
    mes "Just because we're near a shower doesn't mean you can sing."
    scene d15s07-05-02 lc-min-talk-why-sing-turn-around with dissolve
    play voice4 lydia_laugh noloop
    lc "Oh, ha ha. {w}You know I can sing."
    play voice3 min_happy_mmm noloop
    mes "Well, not that. Not now."
    scene d15s07-06 lc-min-stop-singing-talk with dissolve
    play voice4 lydia_morningoh noloop
    lc "Oh, sorry. I forgot. {w}How are you doing with-?"
    play voice3 min_arrogant_hm noloop
    mes "Antony isn't in the picture anymore."
    scene d15s07-08 lc-min-mc-walk-in-interrupt with dissolve
    play voice4 lydia_hmmmm noloop
    lc "Is there someone else...?"
    scene d15s07-08-02 lc-mc-hey-join-room with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hello, ladies. I hope I'm not interrupting."
    scene d15s07-09 lc-min-mc-excited-to-see with dissolve
    play voice3 min_happy_relief noloop
    mes "Perfect timing!"
    play voice4 lydia_huh2 noloop
    lc "Agreed. It's always a perfect time to see the love of my life."
    play voice2 mc_happy_oof2 noloop
    scene d15s07-10 lc-min-mc-hug with hpunch
    play voice4 lydia_haha noloop
    pause
    scene d15s07-11 lc-min-mc-hug-close-up-love with dissolve
    queue voice2 mc_thinking_mmm1 noloop
    mc "I love being with you."
    play voice4 lydia_lydyes noloop
    lc "Same."
    scene d15s07-12 lc-min-mc-interrupt with dissolve
    play voice3 min_angry_cough noloop
    mes "*fake cough*"
    scene d15s07-13 lc-min-mc-talking-mc with dissolve
    play voice2 mc_scared_huuuh2 noloop
    mc "Oh, right. What can I do for you two?"
    scene d15s07-16 lc-min-mc-talking-lc-look-mc with dissolve
    play voice4 lydia_thinking noloop
    lc "Min wants to finish what we started yesterday. {w}And to be honest, I kinda want to as well."
    scene d15s07-17 lc-min-mc-talking-mc-look-lydia with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh?"
    scene d15s07-15 lc-min-mc-talking-min-pov with dissolve
    play voice3 min_surprised_huh1 noloop
    mes "Oh?"
    scene d15s07-14 lc-min-mc-talking-lydia with dissolve
    play voice4 lydia_moan1 noloop
    lc "I'm not saying we should make it a regular thing, but... {w}Min has a point."
    scene d15s07-15-02 lc-min-mc-talking-min-pov-_cage with dissolve
    play voice3 min_yes_yeah1 noloop
    mes "I told her how important it is to push our limits and explore things that we normally wouldn't do."
    scene d15s07-16 lc-min-mc-talking-lc-look-mc with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "So, I'm here for moral support? To help Lydia get through this?"
    play voice4 lydia_hmmmm noloop
    lc "Well..."
    scene d15s07-15 lc-min-mc-talking-min-pov with dissolve
    play voice3 min_old_hmm noloop
    mes "Lydia already had a couple glasses of water, so it's just a waiting game now."
    mes "That said... {w}would you like something to drink, [mcname]?"
    menu:
        "I am ready to pee"(hint="d15s07m01c01"):
            $ d15s07_mc_pee = True
            $ d15s07_points = 12

            scene d15s07-16 lc-min-mc-talking-lc-look-mc with dissolve
            play voice2 mc_yes_yeah1 noloop
            mc "I'm ready to go."
            scene d15s07-15-02 lc-min-mc-talking-min-pov-_cage with dissolve
            play voice3 min_happy_woohoo noloop
            mes "Alright! Let's get naked and hop into the shower."
        "I want to drink Min's piss first"(hint="d15s07m01c02"):

            $ d15s07_mc_peed_on = True
            $ d15s07_mc_pee = True
            $ d15s07_points = 12

            scene d15s07-16 lc-min-mc-talking-lc-look-mc with dissolve
            play voice2 mc_yes_yeah4 noloop
            mc "I'm ready to go... but could use a drink first, if you know what I mean."
            scene d15s07-15-02 lc-min-mc-talking-min-pov-_cage with dissolve
            play voice3 min_thinking_oh noloop
            mes "Oh! Sure, let's get nude and hop into the shower."
        "I'm just here for moral support"(hint="d15s07m01c03"):

            $ d15s07_mc_pee = False
            $ d15s07_mc_peed_on = False
            $ d15s07_points = 6

            scene d15s07-16 lc-min-mc-talking-lc-look-mc with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "I'm just here for moral support."
            scene d15s07-15-02 lc-min-mc-talking-min-pov-_cage with dissolve
            play voice3 min_disappointed_off noloop
            mes "Oh, alright."
            scene d15s07-14 lc-min-mc-talking-lydia with dissolve
            play voice4 lydia_aga noloop
            lc "Well, let's get undressed and step into the shower."

    jump d15s07_whatsthat

label d15s07_whatsthat:

    scene d15s07-18 lc-min-mc-talk-about-cock-cage with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Before I get undressed, there's a little something you should know..."
    scene d15s07-19 lc-min-mc-talk-about-cock-cage-lc-response with dissolve
    play voice4 lydia_thinking noloop
    lc "What's that?"
    scene d15s07-20 lc-min-mc-talk-about-cock-cage-mes-response with dissolve
    if d15s07_mc_peed_on is True:
        play voice3 min_disappointed_off noloop
    else:
        play voice3 min_thinking_oh noloop
    mes "I think he's talking about the penis cage."
    scene d15s07-21 lc-min-mc-angry-lc-told-mes with dissolve
    play voice2 d9s5_auch2 noloop
    mc "You told her about that?!"
    scene d15s07-24 lc-group-talk-mc-apologize with dissolve
    play voice3 min_yes_active noloop
    mes "Of course she did."
    scene d15s07-23 lc-min-mc-apologize-sad with dissolve
    play voice4 lydia_oof noloop
    lc "She is my closest friend, and..."
    play voice2 mc_yes_yeah5 noloop
    scene d15s07-22 lc-min-mc-of-course-she-did with dissolve
    mc "Yeah, no. I get it. It was just a surprise."
    scene d15s07-23 lc-min-mc-apologize-sad with dissolve
    play voice4 lydia_hmmmm noloop
    lc "I haven't told anyone else."
    scene d15s07-23-02 lc-min-mc-_cage-mc-talk with dissolve
    play voice3 min_yes_ugu noloop
    mes "Neither have I."
    play voice2 mc_disappointed_ehh2 noloop
    scene d15s07-22 lc-min-mc-of-course-she-did with dissolve
    mc "Alright, sorry for my outburst."
    scene d15s07-24 lc-group-talk-mc-apologize with dissolve
    play voice3 min_happy_yeah noloop
    mes "Right! Let's get down to business."
    scene d15s07-25 lc-min-mc-group-talk-lydia-sing with dissolve
    play voice4 lydia_oops noloop
    lc "To defeat... the Huns!"
    $ renpy.music.set_volume(0.6, 3.0, "music")
    play music the_beato_book fadein 1.0
    $ renpy.music.set_volume(0.35, 3.0, "sound2")

    if d15s07_mc_peed_on is True:
        jump d15s07_mes_pee_on_mc
    elif d15s07_mc_pee is True:
        jump d15s07_mc_pee_on_mes
    else:
        jump d15s07_lc_pee_on_mes

label d15s07_mes_pee_on_mc:

    scene d15s07-26-02 lc-min-mc-talk-wait-not-ready-_cage-camera with dissolve
    lc "Wait..."
    play voice2 mc_thinking_hmm2 noloop
    mc "Huh? What's wrong?"
    scene d15s07-26-03 lc-min-mc-talk-wait-not-ready-face-min-camera
    if cage_ntr is True:
        show d15s07-26-03-over-lc-min-mc-talk-wait-not-ready-face-min-camera-ntr
    with dissolve
    play voice4 lydia_moan1 noloop
    lc "This isn't... {w}I'm not ready for this."
    play voice3 min_hey_simple noloop
    mes "You don't have to do anything. I'm gonna-"
    scene d15s07-27 lc-min-mc-talk-mes-not-pee-on-mc with dissolve
    play voice4 lydia_lydyes noloop
    lc "I know, but..."
    lc "Look. I'm gonna want to kiss him later. I'm gonna want him to kiss me."
    scene d15s07-26-03 lc-min-mc-talk-wait-not-ready-face-min-camera
    if cage_ntr is True:
        show d15s07-26-03-over-lc-min-mc-talk-wait-not-ready-face-min-camera-ntr
    with dissolve
    lc "I know this is something that is fun for you and I promise I'll watch it sometime, but right now-"
    scene d15s07-27-02 lc-min-mc-talk-mes-not-pee-on-mc-_cage-camera
    if cage_ntr is True:
        show d15s07-27-02-over-lc-min-mc-talk-mes-not-pee-on-mc-_cage-camera-ntr
    with dissolve
    play voice2 mc_no_no2 noloop
    mc "No, I understand. It's okay."
    scene d15s07-27 lc-min-mc-talk-mes-not-pee-on-mc with dissolve
    play voice4 daisy_ugu noloop
    lc "Okay."
    scene d15s07-27-02 lc-min-mc-talk-mes-not-pee-on-mc-_cage-camera
    if cage_ntr is True:
        show d15s07-27-02-over-lc-min-mc-talk-mes-not-pee-on-mc-_cage-camera-ntr
    with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Are you okay if I pee on her, though?"
    play voice3 min_old_laugh noloop
    mes "I don't think she's planning on kissing me."
    scene d15s07-28 lc-min-mc-talk-it-is-fine with dissolve
    play voice4 daisy_aga noloop
    lc "Yeah, that's fine."
    scene d15s07-29-02 lc-min-mc-okay-to-kiss with dissolve
    play voice3 min_old_huh noloop
    mes "Would it be alright if I kiss him?"
    scene d15s07-29 min-mc-pull-closer with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Not after I pee in your mouth, I'm guessing."
    play voice3 min_no_simple noloop
    mes "No, I was thinking about now. Before we get started."
    scene d15s07-29-02-02 lc-min-mc-okay-to-kiss-2_c2 with dissolve
    play voice4 dahlia_surprised_huh2 noloop
    lc "Huh? {w}Why would you want to do that?"
    scene d15s07-29-02 lc-min-mc-okay-to-kiss with dissolve
    play voice3 min_old_hmm noloop
    mes "He's an attractive guy. We're sharing an intimate moment. There's an emotional connection."
    scene d15s07-29-02-02 lc-min-mc-okay-to-kiss-2_c2 with dissolve
    play voice4 lydia_morningoh noloop
    lc "Oh, I didn't realize you felt that way about each other."
    play voice2 mc_arrogant_hm1 noloop
    mc "Well, you did arrange for me to take her out on a date."
    play voice4 dahlia_thinking_hmm1 noloop
    lc "Hmm. Is this one of those times when I'm supposed to get jealous?"
    scene d15s07-29-02-02 lc-min-mc-okay-to-kiss-2_c1 with dissolve
    play voice2 mc_no_no5 noloop
    mc "Not unless you want it to be."
    play voice3 min_disappointed_off noloop
    mes "I'm not trying to steal your boyfriend. I just want to share him."
    scene d15s07-29-02-02 lc-min-mc-okay-to-kiss-2_c2 with dissolve
    play voice4 dahlia_thinking_mmm1 noloop
    lc "Well, let's give it a try and see how I feel about it."
    play voice3 min_arrogant_heh2 noloop
    scene d15s07-29 min-mc-pull-closer with dissolve
    mes "Are you good with this? Making out with me in front of your girlfriend?"
    play voice2 d9s2_mcyes noloop
    mc "I want this."

    $ Lovense.stop()

    play sound maria_kiss1
    scene d15s07-29-03 min-mc-kiss with dissolve
    $ Lovense.vibrate(2)
    pause
    play voice3 dahlia_sex_closedmoan1 noloop
    scene d15s07-29-04 min-mc-squeeze-butt with dissolve
    pause
    play voice4 lydia_lydwow noloop
    lc "Wow."
    scene d15s07-29-05 lc-min-mc-squeeze-butt-lydia-reaction with dissolve
    lc "Okay. That is HOT!"
    scene d15s07-29-06 min-mc-invite-in-shower with dissolve
    play voice3 min_happy_relief noloop
    mes "Get your ass in here. I want your piss in my mouth."

    jump d15s07_mc_pee_on_mes

label d15s07_mc_pee_on_mes:

    scene d15s07-30 mc-lc-min-cock-cage-talk
    if cage_ntr is True:
        show d15s07-30-over-mc-lc-min-cock-cage-talk_ntr
    with dissolve
    play voice3 min_arrogant_huh2 noloop
    mes "Huh. Is this going to be a problem?"
    scene d15s07-31 mc-lc-min-talk-min-pov
    if cage_ntr is True:
        show d15s07-31-over-mc-lc-min-talk-min-pov_ntr
    with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Physically it only restricts blood flow, not urine."
    mc "Mentally, well, it's uncomfortable as hell and that makes it difficult to relax my bladder and pee."
    scene d15s07-32-02 mc-lc-min-talk-lydia
    if cage_ntr is True:
        show d15s07-32-02-over-mc-lc-min-talk-lydia-ntr
    with dissolve
    play voice4 lydia_lydiahey noloop
    lc "It's okay. Just take your time. Pretend no one is watching, right?"
    scene d15s07-32 mc-lc-min-talk-lydia
    if cage_ntr is True:
        show d15s07-32-over-mc-lc-min-talk-lydia-ntr
    with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Exactly. {w}Although, I'm not sure how likely it is that I can pretend that hard."
    scene d15s07-32-03 mc-lc-min-talk-lydia
    if cage_ntr is True:
        show d15s07-32-03-over-mc-lc-min-talk-lydia-ntr
    with dissolve
    play voice4 lydia_hmmmm noloop
    lc "You mean because you've got one beautiful naked woman on her knees before your cock while your girlfriend is watching?"
    scene d15s07-33 mc-lc-min-talk-min-how-is-that-helpful
    if cage_ntr is True:
        show d15s07-33-over-mc-lc-min-talk-min-how-is-that-helpful_cage
    with dissolve
    play voice3 min_disappointed_mph noloop
    mes "How is that helpful?"
    play voice2 mc_no_nah2 noloop
    mc "It's alright. Pretty soon Lydia will be in my place..."
    $ Lovense.vibrate(4)
    $ renpy.music.set_volume(0.4, 0.0, "sound3")
    play sound sfx_piss_loop2 loop
    play sound3 sfx_piss_loop1
    scene d15s07-a1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    play voice3 min_old_moans
    mc "... with a beautiful naked woman on her knees before her..."
    mc "... trying not to get aroused in front of her significant other..."
    scene d15s07-a2 with dissolve
    mes "{i}*moans*{/i}"
    play voice2 d1s5_orgasm noloop
    mc "... and trying not to notice that everyone else in the room is horny as fuck."

    play voice3 min_old_sinking
    $ renpy.music.set_volume(0.6, 1.0, "sound3")
    if cage_ntr is True:
        scene d15s07-a4-ntr with dissolve
        pause
        pause
    else:
        scene d15s07-a4-lc with dissolve
        pause
        pause

    if cage_ntr is True:
        scene d15s07-a3-ntr with dissolve
        pause
        pause
    else:
        scene d15s07-a3-lc with dissolve
        pause
        pause

    stop sound fadeout 1.0
    stop sound3 fadeout 1.0
    play voice3 ["<silence 0.5>", jessie_breathe2, gulp, "<silence 1.5>", jessie_breathe4, "<silence 0.5>", jessie_breathe3] noloop
    scene d15s07-a5 with dissolve
    pause

    play voice4 lydia_moan1 noloop
    scene d15s07-36 mc-lc-touching-self with dissolve
    pause
    scene d15s07-36-02 mc-lc-touching-self-realize with dissolve
    play voice4 lydia_ah noloop
    lc "What? Oh! Dammit, I'm sorry."
    play sound gulp
    scene d15s07-37 mc-min-suck-tip-of-cage with dissolve
    pause
    scene d15s07-38 mc-lc-talking with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "It's perfectly normal. Min doesn't seem to mind."
    play voice4 dahlia_thinking_hmm3 noloop
    lc "Are you still-?"
    play voice2 mc_no_nope2 noloop
    mc "Nope. My tank is empty now."
    $ Lovense.vibrate(1)
    scene d15s07-40 mc-lc-min-talking-unsure with dissolve
    play voice3 min_angry_breath noloop
    mes "I'm sorry, I'm sorry. I got a little carried away for a moment there."
    play voice2 mc_happy_a1 noloop
    mc "It's okay. This is supposed to be a pleasurable experience for everyone involved."
    play voice3 min_yes_simple noloop
    mes "I know, but I shouldn't... {w}I should have more self control."

    jump d15s07_lc_pee_on_mes

label d15s07_lc_pee_on_mes:

    play voice2 mc_hey_hey5 noloop
    scene d15s07-41 mc-lc-min-invite-inside-shower
    if cage_ntr is True:
        show d15s07-41-over-mc-lc-min-invite-inside-shower_ntr
    with dissolve
    mc "Honey, come here."


    scene d15s07-43 mc-lc-talking-close-up with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "This isn't going to be like last time, because we're going to try something different."
    scene d15s07-45 mc-lc-talking-close-up with dissolve
    play voice4 lydia_hmmmm noloop
    lc "We are?"
    scene d15s07-47 mc-lc-min-talking-look-down-pov with dissolve
    play voice3 min_surprised_huh2 noloop
    mes "We are?"
    $ Lovense.vibrate(2)
    scene d15s07-46 mc-lc-talking-look-down with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Min, I want you to focus your self-control on not making physical contact with my girlfriend. Okay?"
    scene d15s07-47 mc-lc-min-talking-look-down-pov with dissolve
    play voice3 min_yes_serious noloop
    mes "Yes, definitely. Agreed."
    scene d15s07-49 mc-lc-min-talking-look-down-hand-shoulder with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Now Lydia, if Min does lose control and accidentally makes physical contact, you're not going to run screaming out of the room. Right?"
    scene d15s07-45 mc-lc-talking-close-up with dissolve
    play voice4 lydia_morningoh noloop
    lc "I'm not?"
    scene d15s07-43 mc-lc-talking-close-up with dissolve
    play voice2 mc_no_uhuh1 noloop
    mc "No, you're not. Do you know why?"
    scene d15s07-45 mc-lc-talking-close-up with dissolve
    play voice4 lydia_uhuh noloop
    lc "No. {w}Why?"
    scene d15s07-43 mc-lc-talking-close-up with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Because I'm going to be right here with you, and if something sexual or arousing starts to happen, you're going to focus on me."
    scene d15s07-45 mc-lc-talking-close-up with dissolve
    play voice4 lydia_moan1 noloop
    lc "Oh?"
    scene d15s07-43 mc-lc-talking-close-up with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Consider this practice. The two people you are closest to in the world are going to give you pleasure and you don't have to be afraid of it."
    scene d15s07-45 mc-lc-talking-close-up with dissolve
    play voice4 lydia_lydyes noloop
    lc "Oh. That's true."
    scene d15s07-47 mc-lc-min-talking-look-down-pov with dissolve
    play voice3 min_thinking_emm noloop
    mes "Wait - now I'm confused. Am I supposed to-?"
    scene d15s07-46 mc-lc-talking-look-down with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Just focus on Lydia's piss and we'll see what happens. Is that okay with you?"
    scene d15s07-47 mc-lc-min-talking-look-down-pov with dissolve
    play voice3 min_yes_aga noloop
    mes "That sounds great to me. Lydia? What do you think?"
    play voice4 lydia_oof noloop
    lc "I'm willing to try. It wouldn't make us lesbians or lovers or anything like that. It would just be something that happened."
    scene d15s07-49 mc-lc-min-talking-look-down-hand-shoulder with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Exactly. We can figure out later whether it meant something or not - if it even happens at all."


    scene d15s07-45 mc-lc-talking-close-up with dissolve
    play voice4 dahlia_thinking_hmm4 noloop
    lc "Okay. I think I'm ready to start."
    scene d15s07-43 mc-lc-talking-close-up with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Good, I want you to take a good look down at your best friend."
    $ Lovense.vibrate(3)
    scene d15s07-46 mc-lc-talking-look-down with dissolve
    pause
    scene d15s07-47 mc-lc-min-talking-look-down-pov with dissolve
    pause
    scene d15s07-46 mc-lc-talking-look-down with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "You're not actually looking at your best friend."
    play voice4 dahlia_thinking_mmm2 noloop
    lc "Yes, I am."
    scene d15s07-43 mc-lc-talking-close-up with dissolve
    play voice2 mc_no_nope1 noloop
    mc "Nope. You're looking at a human toilet. She's just a receptacle for your pee."
    scene d15s07-45 mc-lc-talking-close-up with dissolve
    play voice4 lydia_morningoh noloop
    lc "Oh."
    scene d15s07-49 mc-lc-min-talking-look-down-hand-shoulder with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "You're relaxed and standing in front of a worthless piss-slut that wants to drink your urine."
    play voice3 [jessie_breathe4, "<silence 0.8>", jessie_breathe3, "<silence 0.8>", jessie_breathe2, "<silence 0.8>", jessie_breathe1, "<silence 0.8>"]
    play sound ["<silence 0.4>", sfx_piss_shorts1] loop fadeout 0.5
    scene d15s07-a6 with dissolve
    play voice4 lydia_orgasm2 noloop
    lc "I think it's working."
    play sound ["<silence 0.25>", sfx_piss_shorts1] loop fadeout 0.5
    $ Lovense.vibrate(5)
    scene d15s07-a7 with dissolve
    play voice2 d9s2_ugu noloop
    mc "You may stop looking at her. Just lean back against me and let your body and bladder relax."
    play sound sfx_piss_loop2 loop
    play sound3 sfx_piss_loop1
    scene d15s07-a8 with dissolve
    play voice2 d1s5_orgasm noloop
    play voice3 min_old_sinking
    mc "Do you feel that? That soft pleasure as the liquid releases from you?"
    play voice4 lydia_orgasm3 noloop
    lc "Yes. It feels so good."
    lc "You feel so good. {w}[mcname], I want you to touch me."
    scene d15s07-50 mc-lc-min-kiss-grope-boob with dissolve
    play voice2 d14s16_smell noloop
    mc "Tell me what you want."
    queue voice4 lydia_lydyes noloop
    lc "Yesssss... {w}I want this."

    if cage_ntr is True:
        jump d15s07_ntr_path
    else:
        jump d15s07_lc_path

label d15s07_ntr_path:

    scene d15s07-a9 with dissolve
    play voice4 lydia_laugh noloop
    lc "You're wrong, [mcname]."
    lc "This worthless piss-slut is my best friend."
    lc "And I'm going to give her exactly what she wants."
    lc "Every last drop."
    stop sound fadeout 0.8
    stop sound3 fadeout 0.8
    play voice3 ["<silence 0.5>", jessie_breathe2, gulp, "<silence 0.5>", gulp, "<silence 0.85>", jessie_breathe1, min_old_orgasm3] noloop
    scene d15s07-a4 with dissolve
    pause
    play voice3 dahlia_sex_closedmoan5 noloop
    queue voice3 samiya_moans6
    $ renpy.music.set_volume(2.0, 1.0, "sound3")
    play sound3 d3s8_sucking2 loop
    play voice4 lydia_ah noloop
    $ Lovense.vibrate(7)
    scene d15s07-55 mc-lc-min-push-deeper-ntr with vpunch
    pause
    scene d15s07-56 mc-lc-min-push-deeper-ntr-lydia-look-down with dissolve
    pause
    scene d15s07-57 mc-lc-push-deeper-ntr-lydia-look-down-min-pov with dissolve
    play voice4 lydia_orgasm1 noloop
    lc "Oh FUCK her tongue is amazing!"
    lc "I can't believe I'm still passing water while she's doing this!!"
    scene d15s07-57-02 mc-lc-push-deeper-lydia-look-down-min-pov-_cage with dissolve
    play voice4 aaleyah_closed_moan6 noloop
    lc "I'm going to cum so hard after this!!!"
    queue voice4 chastity_openmoans2
    scene d15s07-a1-ntr with dissolve
    lc "Oh god! Oh God! OH GOD!!!"
    lc "How?! {w}FUCK!!!"
    scene d15s07-a2-ntr with dissolve
    lc "How is this possible?!"
    scene d15s07-58 mc-lc-push-deeper-moan with hpunch
    play voice4 chastity_orgasm noloop
    lc "Fuck fuck fuck..."
    lc "Min. Stop. That's enough."
    $ Lovense.vibrate(10)
    scene d15s07-a1-ntr-f with dissolve
    play voice3 dahlia_sex_closedmoan3 noloop
    queue voice3 samiya_moans6
    mes "{i}MmmMmmph!{/i}"
    queue voice4 lydia_moan1 noloop
    lc "shit... I need to sit down..."
    scene d15s07-a2-ntr-f with dissolve
    play voice3 dahlia_sex_closedmoan5 noloop
    mes "{i}MmmmMmppphhh!!!{/i}"
    scene d15s07-57 mc-lc-push-deeper-ntr-lydia-look-down-min-pov with dissolve
    play voice4 lydia_oof noloop
    lc "oh, shit. I'm sorry."
    stop sound3 fadeout 1.0
    $ renpy.music.set_volume(1.0, 1.0, "sound3")
    $ Lovense.vibrate(3)
    scene d15s07-47 mc-lc-min-talking-look-down-pov with dissolve
    play voice3 dahlia_old_angry noloop
    mes "{i}*breathes deeply*{/i} It's fine."

    jump d15s07_end

label d15s07_lc_path:

    play voice2 d1s1_mmm noloop
    mc "Just focus on me. Relax and enjoy."
    scene d15s07-a9 with dissolve
    mc "That's it. Receiving pleasure while releasing pressure."
    play voice4 lydia_moan1 noloop
    lc "It feels wonderful, [mcname], but you are wrong."
    lc "She's not some worthless human toilet."
    lc "She's my best friend. {w}We would do anything for each other."
    stop sound fadeout 0.8
    stop sound3 fadeout 0.8
    play voice3 ["<silence 0.5>", jessie_breathe2, gulp, "<silence 0.5>", gulp, "<silence 0.85>", jessie_breathe1, min_old_orgasm3] noloop
    scene d15s07-a4 with dissolve
    pause
    scene d15s07-50 mc-lc-min-kiss-grope-boob with dissolve
    play voice4 lydia_orgasm2 noloop
    lc "Wow. That was-"
    play voice4 lydia_orgasm1 noloop
    $ Lovense.vibrate(7)
    scene d15s07-57 mc-lc-push-deeper-ntr-lydia-look-down-min-pov with vpunch
    lc "{i}*gasp*{/i}"
    play voice2 mc_surprised_huh4 noloop
    mc "Are you okay?"
    play voice3 dahlia_sex_closedmoan5 noloop
    queue voice3 samiya_moans6
    $ renpy.music.set_volume(2.0, 1.0, "sound3")
    play sound3 d3s8_sucking2 loop
    scene d15s07-56 mc-lc-min-push-deeper-ntr-lydia-look-down with dissolve
    play voice4 lydia_orgasm3 noloop
    lc "She's doing me. {w}Her tongue..."
    play voice2 mc_yes_yeah7 noloop
    mc "How does that make you feel?"
    scene d15s07-a1-ntr with dissolve
    queue voice4 chastity_openmoans2
    lc "I want this."
    lc "I can't believe... {w}I'm still passing water... {w}even while she's doing this."
    play voice2 d14s16_smell noloop
    mc "Relax and enjoy. Release and receive pleasure."
    scene d15s07-a2-ntr with dissolve
    lc "I feel so close to both of you right now."
    lc "I want you inside me."
    scene d15s07-a1-ntr-f with dissolve
    lc "Oh god!"
    play voice2 mc_yes_yeah1 noloop
    mc "I wish I could."
    lc "Her tongue.{w}.. Min's tongue is inside me!"
    mc "How does it feel?"
    lc "Wonderful."
    scene d15s07-57-02 mc-lc-push-deeper-lydia-look-down-min-pov-_cage with dissolve
    play voice4 aaleyah_closed_moan6 noloop
    lc "[mcname], I'm going to-"
    play voice2 mc_yes_yeah8 noloop
    mc "Yes?"
    scene d15s07-a2-ntr-f with dissolve
    play voice4 lydia_orgasm1 noloop
    queue voice4 chastity_openmoans2
    lc "[mcname]?!"
    play voice2 mc_thinking_hmm4 noloop
    mc "I'm right here with you."
    lc "[mcname]! May I climax? Please!"
    play voice2 mc_yes_yes1 noloop
    mc "Cum for me, Lydia. {w}Cum from your best friend's tongue."
    play voice4 chastity_orgasm noloop fadeout 1.0
    queue voice4 chastity_orgasm2 noloop
    $ Lovense.vibrate(10)
    scene d15s07-58 mc-lc-push-deeper-moan with hpunch
    lc "I LOVE YOU BOTH!!!!!!!!!!"
    with hpunch
    lc "GAaaaAAaaaAHHHHH!!!"
    with hpunch
    lc "Yesssss........"
    stop voice3 fadeout 1.0
    stop sound3 fadeout 1.0
    $ renpy.music.set_volume(2.0, 1.0, "sound3")
    $ Lovense.vibrate(2)
    scene d15s07-60 mc-lc-rest with dissolve
    play voice4 lydia_moan1 noloop
    lc "[mcname]?"
    scene d15s07-60-02 mc-lc-rest with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "I'm right here."
    scene d15s07-60 mc-lc-rest with dissolve
    play voice4 lydia_huh2 noloop
    lc "Hold me."
    scene d15s07-60-02 mc-lc-rest with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "How was that?"
    scene d15s07-47 mc-lc-min-talking-look-down-pov with dissolve
    play voice3 min_disappointed_ehh2 noloop
    mes "It was amazing."
    scene d15s07-60 mc-lc-rest with dissolve
    play voice4 daisy_ugu noloop
    lc "It really was."

    jump d15s07_end

label d15s07_end:

    $ renpy.end_replay()
    $ unlock_gallery_slot("scene", "d15s07")

    $ Lovense.stop()

    scene d15s07-60-03 mc-lc-rest-eyes-open with dissolve
    play voice4 daisy_oof noloop
    lc "[mcname]? Can you carry me to the bedroom?"
    play voice2 mc_yes_sure1 noloop
    mc "Of course."
    scene d15s07-61 mc-lc-min-leave-get-out-of-way with dissolve
    play voice3 min_old_laugh noloop
    mes "Let me get out of your way."
    $ renpy.music.set_volume(0.1, 6.0, "sound2")
    scene d15s07-62 mc-lc-min-carry-leave-bathroom with dissolve
    pause
    scene d15s07-63 mc-lc-carry-lydia-view with dissolve
    play voice4 dahlia_thinking_hmm3 noloop
    lc "That was wonderful. Thank you so much."
    scene d15s07-63-03 mc-lc-min-carry-talk with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Was it everything you hoped for, Min?"
    scene d15s07-63-02 mc-lc-min-carry-talk with dissolve
    play voice3 min_yes_simple noloop
    mes "Yes... {w}With one tiny exception."
    scene d15s07-63-03 mc-lc-min-carry-talk with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh?"
    scene d15s07-63-02 mc-lc-min-carry-talk with dissolve
    play voice3 min_thinking_mhh noloop
    mes "We should try something like this again when you get that cage off."
    menu:
        "We should definitely do that"(hint="d15s07m02c01"):
            $ d15s07_more_watersports = True

            scene d15s07-63-03 mc-lc-min-carry-talk with dissolve
            play voice2 mc_yes_yeah1 noloop
            mc "Definitely. This was a lot of fun."
            scene d15s07-63-02 mc-lc-min-carry-talk with dissolve
            play voice3 min_arrogant_huh2 noloop
            mes "Maybe next time we could even start training her to enjoy a sip."
            scene d15s07-63 mc-lc-carry-lydia-view with dissolve
            play voice2 mc_arrogant_huh1 noloop
            mc "Huh. Lydia, what do you think about that?"
        "I'm getting kinda bored of the watersports"(hint="d15s07m02c02"):

            $ fl_watersports = False

            scene d15s07-63-03 mc-lc-min-carry-talk with dissolve
            play voice2 mc_arrogant_hm2 noloop
            mc "Maybe we could try some other things. I'm getting a little tired of just watersports."
            scene d15s07-63-02 mc-lc-min-carry-talk with dissolve
            play voice3 min_thinking_oh noloop
            mes "Oh?{w} I'll keep that in mind."

    if d15s07_more_watersports is False:
        scene d15s07-63 mc-lc-carry-lydia-view with dissolve
    play voice4 min_disappointed_snoring noloop
    lc "{i}*ZZzzzzzzZZZzzzzz*{/i}"
    scene d15s07-64 mc-lc-min-bye with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "I better get her to bed."
    play voice3 min_yes_ugu noloop
    mes "Of course."

    stop sound2 fadeout 3.0
    stop music fadeout 3.5
    jump d15s08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
