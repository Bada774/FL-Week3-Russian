label d16s08:

    $ d16s08_fl_points = d16s02_points + d16s03_points + d16s06_points

    scene black
    show screen scene_transistion(_("1 hour later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    play sound sfx_door_openclosed2
    hide screen scene_transistion
    scene d16s08-01-mc-enters-the-room
    with Fade(0.5, 0.5, 0.9)
    pause
    play music past_sadness fadein 1.5
    $ renpy.music.set_volume(0.9, 3.0, "music")
    scene d16s08-02-mc-looks-at-arj-sy with dissolve
    play sound sfx_keyboard_typing2
    pause
    scene d16s08-03-arj-talking-with-mc with dissolve
    play voice3 amrose_arrogant_hmm2 noloop
    arj "Did you call Lydia before coming over here?"
    scene d16s08-04-mc-talking-with-arj with dissolve
    play voice2 mc_no_no2 noloop
    mc "No. She doesn't expect me to call her until tonight."
    scene d16s08-05-sy-talking-with-mc with dissolve
    play voice3 stacy_hmm noloop
    sy "We shouldn't need that long. Let me see the device."

    scene d16s08-06-mc-gives-usb-to-sy with dissolve
    pause
    scene d16s08-07-arj-talking-with-mc with dissolve
    play voice3 amrose_old_hey1 noloop
    arj "While Stacy is working on that, I wanted to talk to you about your plans for this week."
    play voice2 mc_arrogant_hm1 noloop
    mc "Well, it's Finals Week. {w}Mind if I study a bit?"
    play sound sfx_paper_rustl1
    scene d16s08-08-arj-looks-at-mc with dissolve
    play voice3 amrose_yes_yeah2 noloop
    arj "Yeah, we both need to do some studying, but I meant your other plans."
    play sound sfx_pen_writing1
    scene d16s08-09-mc-talking-with-arj with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Other than that I just need to rack up as many points in the app as I can."
    scene d16s08-10-arj-talking-with-mc with dissolve
    play voice3 amrose_yes_confident2 noloop
    arj "Exactly. Let's brainstorm."
    scene d16s08-11-mc-talking-with-arj with dissolve
    play voice2 mc_happy_a1 noloop
    mc "I figured it would just happen naturally. I didn't really need to plan last week-"
    scene d16s08-12-arj-talking-with-mc with dissolve
    play voice3 amrose_arrogant_huh1 noloop
    arj "And you lost that challenge. We should have planned better."
    play sound sfx_pen_writing2
    scene d16s08-13-mc-talking-with-arj with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, so who...{w} or what do you have in mind?"
    scene d16s08-14-arj-talking-with-mc with dissolve
    play voice3 amrose_happy_mmm noloop
    arj "Well, two of us are obvious."
    scene d16s08-15-mc-talking-with-arj with dissolve
    play voice2 d1s2_hmm volume 1.5 noloop
    mc "You mean you and Lydia?"
    scene d16s08-16-arj-talking-with-mc with dissolve
    play voice3 amrose_no_uhuh noloop
    arj "I meant Hana and myself. {w}I'm not sure you can rely on Lydia for points."
    play sound sfx_pen_writing3
    scene d16s08-17-mc-talking-with-arj with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Fair enough."
    scene d16s08-18-arj-talking-with-mc with dissolve
    play voice3 amrose_thinking_hmm2 noloop
    arj "I'm always available, as you know. {w}Hana might be a bit more tricky..."

    scene d16s08-19-mc-talking-with-arj with dissolve
    if d12s02_hr_sex is True:
        play voice2 mc_no_nah2 noloop
        mc "She won't be difficult. We already fucked last week."
        scene d16s08-20-arj-talking-with-mc with dissolve
        play voice3 amrose_thinking_oh1 noloop
        arj "Oh, yeah."
    else:
        play voice2 mc_thinking_mmm2 noloop
        mc "Apparently she's amazing at blow jobs, so I'll probably pursue her in that direction."
        scene d16s08-26-arj-talking-with-mc with dissolve
        play voice3 amrose_arrogant_huh3 noloop
        arj "I won't ask how you know that."
        scene d16s08-51-mc-talking-with-arj with dissolve
        play voice2 d2s9_confused volume 1.5 noloop
        mc "Pete-"
        scene d16s08-52-arj-talking-with-sy-mc with dissolve
        play voice3 amrose_angry_argh3 noloop
        arj "I WON'T ASK."

    if d13s03_ir_sex is True:
        scene d16s08-53-mc-talking-with-arj with dissolve
        play voice2 d1s5_mchappy volume 1.5 noloop
        if persistent.is_special is True:
            mc "Then there is Hana's sister, Iona."
        else:
            mc "Then there is Hana's girlfriend, Iona."
        scene d16s08-54-arj-talking-with-mc with dissolve
        play voice3 amrose_thinking_oh2 noloop
        if is_antagonist_mode is False:
            arj "Oh yeah, the bartender. She's in the VIP Program too."
        else:
            arj "Oh yeah, the bartender. She's in retention too."
        play voice2 mc_yes_ugu1 noloop
        if is_antagonist_mode is False:
            mc "Which is probably how Hana found out about Fetish Locator and the VIP Program."
        else:
            mc "Which is probably how Hana found out about Fetish Locator and the Retention Program."
        scene d16s08-50-arj-talking-with-mc with dissolve
        play voice3 amrose_arrogant_huh4 noloop
        arj "You think Hana will convince her to do something with you?"
        scene d16s08-19-mc-talking-with-arj with dissolve
        play voice2 mc_no_uhuh1 volume 0.7 noloop
        mc "I don't need Hana to convince her. Remember?"
        scene d16s08-24-arj-talking-with-mc with dissolve
        play voice3 amrose_disappointed_oh3 noloop
        arj "Oh, right. She was on your list last week."

    if date_pw is True:
        scene d16s08-50-arj-talking-with-mc with dissolve
        play voice3 amrose_thinking_hmm1 noloop
        arj "What about Polly and Nora? You had something going with both of them, right?"
        play sound sfx_pen_writing5
        scene d16s08-13-mc-talking-with-arj with dissolve
        play voice2 mc_thinking_mmm5 noloop
        mc "At this point their blind dates are over, but I got the feeling they both still want me to be involved in their relationship."
        scene d16s08-22-arj-talking-with-mc with dissolve
        play voice3 amrose_old_amha noloop
        arj "I still can't believe you hooked up with both of them.{w}.. and especially can't believe you hooked up with both of them together."
        scene d16s08-15-mc-talking-with-arj with dissolve
        play voice2 d9s2_yeah volume 1.6 noloop
        mc "What can I say? I'm awesome."
        scene d16s08-58-arj-talking-with-mc with dissolve
        arj "They just seem so different."

    if date_dd is True:
        scene d16s08-53-mc-talking-with-arj with dissolve
        play voice2 d1s5b_ehhh volume 1.5 noloop
        mc "Daisy and I have been getting pretty close, but... I don't know."
        scene d16s08-14-arj-talking-with-mc with dissolve
        play voice3 amrose_surprised_huh2 noloop
        arj "What? You're losing interest in her?"
        scene d16s08-57-mc-talking-with-arj with dissolve
        play voice2 mc_no_no5 noloop
        mc "No, definitely not. {w}She's got some medical condition..."
        play voice3 amrose_disappointed_oh2 noloop
        arj "Oh."
        scene d16s08-64-mc-talking-with-sy with dissolve
        play voice2 mc_disappointed_ah1 noloop
        mc "I'm worried that the next time she gets too excited... it won't be good for her."
        scene d16s08-67-arj-talking-with-mc with dissolve
        play voice3 amrose_happy_mmm noloop
        arj "I guess that's her choice. {w}Talk to her about it."
        scene d16s08-59-mc-talking-with-arj with dissolve
        play voice2 mc_yes_yeah1 noloop
        mc "Yeah. {w}If we do anything, it won't be just for the points. That would be...{w} wrong."
        arj "I can understand that."

    if date_dw is True:
        scene d16s08-62-mc-talking-with-sy with dissolve
        play voice2 mc_thinking_hmm2 noloop
        mc "Dahlia and I have been getting pretty close."
        scene d16s08-26-arj-talking-with-mc with dissolve
        play voice3 amrose_surprised_uh4 noloop
        arj "Close? She doesn't seem like the type to get close with anyone."
        scene d16s08-55-mc-talking-with-arj with dissolve
        play voice2 mc_arrogant_heh3 noloop
        mc "She's got a prickly exterior, but a warm heart."
        scene d16s08-22-arj-talking-with-mc with dissolve
        play voice3 amrose_surprised_oh3 noloop
        arj "Didn't she almost kill you once?"
        scene d16s08-21-mc-talking-with-arj with dissolve
        play voice2 mc_happy_yay2 noloop
        mc "She's trying to be a better dominatrix. I don't think that will be a problem again."
        scene d16s08-58-arj-talking-with-mc with dissolve
        play voice3 amrose_angry_ergh noloop
        arj "If she hurts you - I'll kill her."
        play sound sfx_pen_writing4
        scene d16s08-13-mc-talking-with-arj with dissolve
        play voice2 d3s11b_mcheh volume 1.5 noloop
        mc "Good to know. {w}My red-headed avenger."

    if date_mh is True:
        scene d16s08-15-mc-talking-with-arj with dissolve
        play voice2 mc_arrogant_hm1 noloop
        mc "Lyssa is definitely an option. I don't like putting her in Fetish Locator's sights, but we are intimate."
        scene d16s08-14-arj-talking-with-mc with dissolve
        play voice3 amrose_hey_whisper noloop
        arj "She's Stacy's landlord. She's a lawyer. And she's a bad ass motherfucker."
        scene d16s08-55-mc-talking-with-arj with dissolve
        play voice2 mc_yes_yes1 noloop
        mc "All true."
        scene d16s08-74-arj-talking-with-mc with dissolve
        play voice3 amrose_happy_laugh1 noloop
        arj "Fetish Locator should be more afraid of her than she should be of the app."
        mc "Good point."

    if date_op is True:
        scene d16s08-67-arj-talking-with-mc with dissolve
        play voice3 amrose_thinking_emm noloop
        arj "What about that guy at the party?"
        scene d16s08-57-mc-talking-with-arj with dissolve
        play voice2 d1s2_hmm volume 1.5 noloop
        mc "Oliver? He and I are..."
        scene d16s08-22-arj-talking-with-mc with dissolve
        play voice3 amrose_surprised_huh3 noloop
        arj "You two are?"
        scene d16s08-55-mc-talking-with-arj with dissolve
        play voice2 mc_happy_a1 noloop
        mc "He's cute. I can help him out. And he's very good at...{w} some things."
        scene d16s08-24-arj-talking-with-mc with dissolve
        play voice3 amrose_arrogant_huh2 noloop
        arj "I guess no one knows better how to pleasure a man than another man."
        scene d16s08-68-mc-talking-with-arj with dissolve
        play voice2 mc_arrogant_nah1 noloop
        mc "I wouldn't say that. {w}It's more of a same-sex experiment for me."
        arj "Well, we are in college."

    if date_sy is True:
        scene d16s08-20-arj-talking-with-mc with dissolve
        play voice3 amrose_surprised_oh4 noloop
        arj "Of course, you need to make some time for Stacy."
        scene d16s08-21-mc-talking-with-arj with dissolve
        play voice2 mc_hey_hey3 noloop
        mc "I don't want her involved in any of this. Fetish Locator shouldn't-"
        scene d16s08-58-arj-talking-with-mc with dissolve
        play voice3 amrose_old_chmchm volume 1.3 noloop
        arj "The app already knows that you two fucked."
        scene d16s08-19-mc-talking-with-arj with dissolve
        play voice2 mc_disappointed_off2 noloop
        if is_antagonist_mode is False:
            mc "Oh, right."
        else:
            mc "Oh, fuck."
        scene d16s08-60-arj-talking-with-mc with dissolve
        play voice3 amrose_old_upset volume 1.7 noloop
        arj "It's very sweet that you wanted to keep her safe, but she brought herself in on this."
        scene d16s08-57-mc-talking-with-arj with dissolve
        play voice2 d1s5b_ehhh volume 1.5 noloop
        mc "Alright. Stacy can be on the list."
        scene d16s08-56-sy-talking-with-arj-mc with dissolve
        play voice4 polly_pollyangry volume 0.8 noloop
        sy "My ears are burning."
        scene d16s08-52-arj-talking-with-sy-mc with dissolve
        play voice3 amrose_old_hey1 volume 1.3 noloop
        arj "We were just discussing how [mcname] will make love to you."
        scene d16s08-61-sy-talking-with-mc with dissolve
        play voice4 stacy_oh noloop
        sy "Oh! Carry on, then!"

    if date_jf is True:
        scene d16s08-16-arj-talking-with-mc with dissolve
        play voice3 amrose_thinking_hmm4 noloop
        arj "What about that... odd girl?"
        play sound sfx_pen_writing3
        scene d16s08-17-mc-talking-with-arj with dissolve
        play voice2 mc_arrogant_heh1 noloop
        mc "You're going to have to narrow that down."
        scene d16s08-18-arj-talking-with-mc with dissolve
        play voice3 amrose_disappointed_oh1 noloop
        arj "The cosplayer? The one that was swimming around Lydia's aquarium at the party?"
        queue sound sfx_pen_writing2
        scene d16s08-13-mc-talking-with-arj with dissolve
        mc "I don't know."
        arj "What do you mean?"
        scene d16s08-19-mc-talking-with-arj with dissolve
        play voice2 mc_arrogant_hm2 noloop
        mc "I think she may want me to dress up next time. {w}Get into some sort of costume."
        scene d16s08-20-arj-talking-with-mc with dissolve
        play voice3 amrose_disappointed_ah noloop
        arj "I guess that's not really surprising."
        scene d16s08-21-mc-talking-with-arj with dissolve
        play voice2 mc_thinking_hmm5 noloop
        mc "I'm not sure how I feel about it. {w}It could be really exciting or it could be just plain weird."
        scene d16s08-22-arj-talking-with-mc with dissolve
        play voice3 amrose_happy_laugh3 noloop
        arj "Embrace your weird."
        scene d16s08-51-mc-talking-with-arj with dissolve
        play voice2 mc_yes_yeah6 noloop
        mc "That's the thing. I'm not sure if it's my weird or if I'd just be going along."
        scene d16s08-50-arj-talking-with-mc with dissolve
        play voice3 amrose_thinking_hmm3 noloop
        arj "Either way, she's hot and fuckable."
        mc "True."

    if date_vw is True:
        scene d16s08-60-arj-talking-with-mc with dissolve
        play voice3 amrose_disappointed_ehh2 noloop
        arj "Anyone else come to mind?"
        scene d16s08-55-mc-talking-with-arj with dissolve
        play voice2 d1s5_mchappy volume 1.5 noloop
        mc "Dozens, but the next one worth mentioning here is Vanessa."
        scene d16s08-22-arj-talking-with-mc with dissolve
        play voice3 amrose_arrogant_huh1 noloop
        arj "The M.I.L.F."
        scene d16s08-57-mc-talking-with-arj with dissolve
        play voice2 mc_yes_yeah4 noloop
        mc "Yeah. I really need to talk to her about some things tomorrow, so maybe I can work a little fun time in as well."
        scene d16s08-58-arj-talking-with-mc with dissolve
        arj "What's her kink?"
        scene d16s08-59-mc-talking-with-arj with dissolve
        mc "She's basically D.T.F., but her biggest fetish is probably feet."
        scene d16s08-74-arj-talking-with-mc with dissolve
        play voice3 amrose_thinking_oh2 noloop
        arj "Oh cool. There isn't enough of that."
        scene d16s08-68-mc-talking-with-arj with dissolve
        play voice2 d9s2_ugu volume 1.6 noloop
        mc "Agreed. We should put in a request with the app or something. Let it know our favorite kinks and fetishes."
        play voice3 amrose_no_nah noloop
        arj "Nah. They already know too much about us."

    scene d16s08-82-arj-talking-with-mc with dissolve
    play voice3 amrose_yes_okay2 noloop
    arj "I guess there's just one other thing we should try to figure out."
    scene d16s08-81-mc-talking-with-arj with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "What's that?"
    scene d16s08-67-arj-talking-with-mc with dissolve
    play voice3 amrose_arrogant_hmm2 noloop
    arj "Any ideas what tomorrow's Fetish of the Day will be?"
    scene d16s08-59-mc-talking-with-arj with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "I don't know. Has there been any sort of pattern?"
    scene d16s08-24-arj-talking-with-mc with dissolve
    play voice3 amrose_thinking_hmm1 noloop
    arj "Just on Mondays and Tuesdays."
    scene d16s08-57-mc-talking-with-arj with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, I figured that out too. Mondays for Men, Tuesdays for Women."
    scene d16s08-58-arj-talking-with-mc with dissolve
    play voice3 amrose_thinking_emm noloop
    arj "The rest of the week... well, aside from the Crossword Puzzle pattern."
    play voice2 mc_surprised_huh6 noloop
    mc "Huh?"
    scene d16s08-61-sy-talking-with-mc with dissolve
    play voice4 stacy_mmm2 noloop
    sy "Crossword puzzles in the newspapers. Monday is the easiest, Saturday is the hardest."
    scene d16s08-55-mc-talking-with-arj with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "What about Sundays?"
    scene d16s08-16-arj-talking-with-mc with dissolve
    play voice3 amrose_old_upset volume 1.7 noloop
    arj "No pattern that I know of. Just that they tend to get more obscure or difficult as the week goes on."
    scene d16s08-51-mc-talking-with-arj with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Wasn't creampie a Saturday? That didn't seem so difficult."
    scene d16s08-26-arj-talking-with-mc with dissolve
    play voice3 amrose_old_argh noloop
    arj "You are such a guy. {w}Creampie means no condom, risk of pregnancy, and all that."
    scene d16s08-64-mc-talking-with-sy with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Good point. Okay, so what about tomorrow?"
    scene d16s08-50-arj-talking-with-mc with dissolve
    play voice3 amrose_no_uhuh noloop
    arj "No idea. It could be anything."
    scene d16s08-63-sy-talking-with-mc with dissolve
    play voice4 stacy_hmm noloop
    sy "Suggestions?"
    scene d16s08-79-mc-talking-with-sy with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "It was foot fetishes a couple weeks ago and {w}was it outercourse last week?"
    scene d16s08-72-arj-talking-with-sy with dissolve
    play voice3 amrose_disappointed_ehh2 noloop
    arj "I think so. I haven't been keeping track."
    scene d16s08-70-mc-talking-with-sy with dissolve
    play voice2 mc_yes_yeah5 volume 0.7 noloop
    mc "Yeah. Whatever it is tomorrow, it should be easy enough."

    if d16s08_fl_points == 0:
        scene d16s08-63-sy-talking-with-mc with dissolve
        play voice4 stacy_huh noloop
        sy "W.T.F. [mcname]???"
        scene d16s08-64-mc-talking-with-sy with dissolve
        play voice2 mc_arrogant_huh1 noloop
        mc "What is it?"
        scene d16s08-65-sy-talking-with-mc with dissolve
        play voice4 stacy_mmm1 noloop
        sy "I checked it. I double checked it. I even double checked the hardware and software."
        sy "Yet there's no fucking data on this."
        scene d16s08-75-mc-talking-with-sy with dissolve
        play voice2 mc_thinking_oh1 noloop
        mc "Oh. Yeah, it was a busy day."
        scene d16s08-76-sy-talking-with-arj with dissolve
        play voice4 stacy_angry noloop
        sy "Apparently not."
        scene d16s08-60-arj-talking-with-mc with dissolve
        play voice3 amrose_hey_active1 noloop
        arj "You do realize just how important this is, don't you?"
        scene d16s08-77-mc-talking-with-sy with dissolve
        play voice2 mc_yes_aga1 noloop
        mc "I get it. No lecture needed. {w}I'll get you plenty of data tomorrow."
        scene d16s08-78-sy-talking-with-mc with dissolve
        play voice3 stacy_angryhuh noloop
        sy "Promise?"
        scene d16s08-79-mc-talking-with-sy with dissolve
        play voice2 mc_yes_yes3 noloop
        mc "I promise that I'll do my best."
        scene d16s08-72-arj-talking-with-sy with dissolve
        play voice3 amrose_yes_yeah1 noloop
        arj "I'll promise you, Stacy. I guarantee he'll log some data points tonight."
    else:
        scene d16s08-72-arj-talking-with-sy with dissolve
        play voice3 amrose_hey_active2 noloop
        arj "Hey Stacy, how is that data looking?"
        scene d16s08-73-sy-talking-with-arj with dissolve
        play voice4 stacy_oh noloop
        sy "We have...{w} a plethora."
        scene d16s08-74-arj-talking-with-mc with dissolve
        play voice3 amrose_surprised_uh5 noloop
        arj "Reeeaaaalllly? {w}What did you get up to today, [mcname]?"
        scene d16s08-62-mc-talking-with-sy with dissolve
        play voice2 mc_thinking_hmm1 noloop
        mc "Just the usual. {w}I didn't think I did all that much today."
        scene d16s08-76-sy-talking-with-arj with dissolve
        play voice4 stacy_mmm1 noloop
        sy "It's not what he did. It's the amount of data obfuscation the app uses, I think."
        sy "There's a few GB of data that I copied off this thing. I'm gonna have to crank through it all night just to figure out what's significant."
        scene d16s08-64-mc-talking-with-sy with dissolve
        play voice2 mc_thinking_hmm5 noloop
        mc "Can't you write a program to do that for you?"
        scene d16s08-78-sy-talking-with-arj-mc with dissolve
        play voice4 polly_aga noloop
        sy "Yes, but I need to analyze the data to write parameters for the program."
        scene d16s08-62-mc-talking-with-sy with dissolve
        play voice2 mc_thinking_oh1 noloop
        mc "Oh, well, shouldn't that be easy? We're just looking for location-"
        scene d16s08-26-arj-talking-with-mc with dissolve
        play voice3 amrose_angry_errr noloop
        arj "Don't do that."
        scene d16s08-62-mc-talking-with-sy with dissolve
        play voice2 mc_surprised_what2 noloop
        mc "Do what?"
        scene d16s08-58-arj-talking-with-mc with dissolve
        play voice3 amrose_old_chmchm volume 1.3 noloop
        arj "Never use the word, \"just\". If anything was \"just\" as easy as you think then it would be done already."
        scene d16s08-65-sy-talking-with-mc with dissolve
        play voice4 stacy_angryhuh noloop
        sy "I'll forgive you this time. Partially because I have too much to do tonight trying to make this seem like it was easy."

    scene d16s08-84-arj-talking-with-mc with dissolve
    play voice3 amrose_thinking_hmm5 noloop
    arj "Alright, we should get going. We have things to do tonight."
    scene d16s08-85-mc-talking-with-arj with dissolve
    play voice2 d1s2_hmm volume 1.5 noloop
    mc "We do? {w}Where are we going?"

    scene d16s08-86-arj-talking-with-mc with dissolve
    play voice3 amrose_arrogant_hmm1 noloop
    if d16s08_fl_points == 0:
        arj "My house. {w}We'll get you some data points before bedtime."
    else:
        arj "My house. {w}We'll get you some more data points before bedtime."

    if date_sy is True:
        scene d16s08-87-sy-talking-with-arj with dissolve
        play voice4 stacy_oh2 noloop
        sy "Oh! I'd love to join you both, but-"
        scene d16s08-88-arj-talking-with-sy with dissolve
        play voice3 amrose_yes_yeah2 noloop
        arj "I would have invited you but-"
        scene d16s08-89-sy-talking-with-arj with dissolve
        play voice4 stacy_laugh4 noloop
        sy "Right."
        scene d16s08-90-arj-talking-with-sy with dissolve
        play voice3 amrose_yes_ugu noloop
        arj "Exactly."
        scene d16s08-89-sy-talking-with-arj with dissolve
        play voice4 stacy_upset1 noloop
        sy "Love you both."
        scene d16s08-90-arj-talking-with-sy with dissolve
        play voice3 daisy_ugu noloop
        arj "Ditto."

    if date_nk_preg is True:
        scene d16s08-91-mc-thinking with dissolve
        play voice2 d1s1_mmm noloop
        mct "Fuck. I'm supposed to meet Nora soon."
        mct "Well, shit. I haven't actually decided whether I'm going with her or not."
        scene d16s08-92-mc-thinking with dissolve
        mct "If I go there, then I'm leaving with her. For good."
        mct "If I don't go, then she'll probably leave without me..."
        mct "She'll keep in touch and I'll still be a stand-up guy and father to our kid, but..."

    scene d16s08-93-arj-talking-with-mc with dissolve
    play voice3 daisy_thinking volume 1.3 noloop
    arj "Well, are you coming?"

    if date_nk_preg is True:
        scene d16s08-94-mc-talking-with-arj with dissolve
        play voice2 d2s9_confused volume 1.5 noloop
        mc "I'll meet you there. I have something else to take care of."
        scene d16s08-95-arj-talking-with-mc with dissolve
        play voice3 amrose_disappointed_oh5 noloop
        arj "Oh... okay. {w}Don't keep me waiting too long."
        scene d16s08-96-mc-thinking with dissolve
        play voice2 mc_arrogant_heh2 noloop
        mct "I'm just going to take a little walk and think this all over."
        mct "Then I'll decide whether I'm leaving with Nora or not."
    else:
        scene d16s08-97-mc-talking-with-arj with dissolve
        play voice2 mc_thinking_mmm2 noloop
        mc "Not yet, but hopefully when we get to your house."
        scene d16s08-98-arj-talking-with-mc with dissolve
        play voice3 amrose_happy_laugh2 noloop
        arj "Ha ha. Let's go, then."

    stop music fadeout 3.5
    jump d16s09
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
