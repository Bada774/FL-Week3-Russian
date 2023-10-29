label d21s04:

    $ d21s04_love_lc = False
    $ d21s04_lc_choice = None
    $ d21s04_mh_end = None

    $ d17s05_did_you_love_her_back = d17s05_love_mh_op or d17s05_love_mh_sy or d17s05_love_mh
    $ d21s04_is_lyssa_solo_available = date_mh and d15s06_asslicked and d15s06_luvutoo and d17s05_did_you_love_her_back
    $ d21s04_is_lyssa_oliver_available = date_mh and d17s05_mh_op and d15s06_assfucked and d17s05_did_you_love_her_back
    $ d21s04_is_lyssa_stacy_available = date_mh and d17s05_mh_sy and d14s19_everything and d15s06_assfucked and d15s06_luvutoo and d17s05_did_you_love_her_back

    if not hasattr(renpy.store, "d19s03_watersports"):
        $ d19s03_watersports = False

    if date_mh is False:
        jump d21s05

    scene black
    show screen scene_transistion(_("1 hour later\nAt Lyssa's Office"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.18, 3.0, "sound2" )
    play sound2 sfx_clock_ticks_loop1 fadein 1.5
    scene d21s04-01-mh-in-office
    with Fade(0.5, 0.5, 0.9)
    pause
    scene d21s04-02-mh-close-up with dissolve
    pause
    stop sound2 fadeout 1.0
    play sound sfx_door_open1
    scene d21s04-03-mc-opens-door with dissolve
    $ renpy.music.set_volume(0.5, 3.0, "music" )
    play music music_decision_made fadein 3.0
    pause
    play sound sfx_door_closed1
    scene d21s04-05-mh-talk-mc with dissolve
    play voice3 lissa_oh2 noloop
    mh "[mcname]? What are you doing here?"
    mh "Why didn't you call?"
    play sound sfx_cloth_rustling4
    scene d21s04-06-mh-hugs-mc with dissolve
    pause
    scene d21s04-07-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah5 noloop volume 0.75
    mc "Yeah... Sorry about just dropping in like this."
    scene d21s04-08-mh-talk-mc with dissolve
    play voice3 lissa_thinking noloop
    mh "You look tired. Is everything okay?"
    scene d21s04-09-mc-talk-mh with dissolve
    play voice2 mc_no_no5 noloop
    mc "No. Not really."
    mc "I just gave my statement for Lydia's case."
    scene d21s04-10-mh-talk-mc with dissolve
    play voice3 lissa_shyoh noloop
    mh "Oh."
    scene d21s04-11-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    mh "Sit down. Tell me what happened."
    play sound sfx_cloth_rustling2
    scene d21s04-12-mc-sits-sighs with dissolve
    play voice2 d14s16_smell noloop
    mc "*Sighs*"
    scene d21s04-13-mc-talk-mh with dissolve
    play voice2 mc_disappointed_ah2 noloop
    if d21s03_statement_1 is True or d21s03_statement_2 is True:
        mc "I think I just signed her prison sentence."
    elif True:
        mc "After everything, I still couldn't go against her."
    scene d21s04-14-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    mh "Come here. Give me your hands."
    scene d21s04-15-mh-talk-mc with dissolve
    mh "What you did was give a statement. That's all."
    mh "Nothing more. Nothing less."
    scene d21s04-16-mc-talk-mh with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Maybe."
    scene d21s04-17-mc-talk-mh with dissolve
    mc "Do you think I did the right thing?"
    scene d21s04-18-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    mh "...I don't know. But what I {i}do{/i} know is that you said what you feel is right."
    mh "And I trust you to have said what needed to be said."
    scene d21s04-19-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "*Deep breath* Yeah."
    scene d21s04-20-mh-talk-mc with dissolve
    play voice3 nora_pleasure noloop
    mh "Do you still care about her?"
    scene d21s04-21-mc-talk-mh with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "I..."
    menu:
        "Yes, I still love Lydia"(hint="d21s04m01c01") if True:
            $ d21s04_lc_choice = 1
            $ d21s04_love_lc = True
            scene d21s04-22-c1-mc-talk-mh with dissolve
            play voice2 mc_disappointed_ehh1 noloop volume 0.8
            mc "*Sighs* Yes."
            mc "I know it's dumb of me. But I cared about her. And through everything, she has done. I still care about her."
        "I don't know"(hint="d21s04m01c02") if True:

            $ d21s04_lc_choice = 2
            scene d21s04-23-c1-c2-mc-talk-mh with dissolve
            play voice2 mc_disappointed_ehh1 noloop volume 0.8
            mc "I don't know. I cared about her. But now? I have so many feelings when I think about her."
        "Absolutely not"(hint="d21s04m01c02") if True:

            $ d21s04_lc_choice = 3
            scene d21s04-24-c3-mc-talk-mh with dissolve
            play voice2 mc_no_uhuh1 noloop
            mc "Absolutely not. She almost ruined my life. Not to mention the lives of so many others."
            mc "I cared about her. And a small part of me still does."
            mc "But I hate her so much more."

    scene d21s04-26-mh-talk-mc with dissolve
    play voice3 nora_hmm noloop
    mh "I can understand. It's a complex situation."
    scene d21s04-27-mc-talk-mh with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mc "*Chuckles* To say the least."
    scene d21s04-28-mh-talk-mc with dissolve
    play voice3 lissa_haha noloop volume 0.7
    mh "*Chuckles* Indeed."
    scene d21s04-29-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    mh "Hm... How about this?"
    mh "Do you want to go grab lunch with me?"
    mh "Forgot about all this for a second."
    scene d21s04-30-mc-talk-mh with dissolve
    play voice2 mc_disgust_fu1 noloop
    mc "Oh? Miss Harris, you're not asking me out on a date are you?"
    scene d21s04-31-mh-talk-mc with dissolve
    play voice3 lissa_aga noloop
    mh "What if I am?"
    scene d21s04-32-mc-talk-mh with dissolve
    play voice2 d2s9_mchey noloop volume 1.4
    mc "Don't you think that's a bit inappropriate for a lawyer to ask that from a client?"
    play sound sfx_cloth_rustling1
    scene d21s04-33-mh-talk-mc with dissolve
    play voice3 lissa_laugh2 noloop
    mh "Perhaps. But you're much more than a client, and I don't hear you saying no."
    scene d21s04-34-mc-talk-mh with dissolve
    play voice2 d4s4_mclaugh noloop volume 1.4
    mc "*Chuckle* You're right. How could I ever say no to you?"
    scene d21s04-35-mh-talk-mc with dissolve
    play voice3 lissa_moan1 noloop
    mh "Good. I know a good asian place. Their spicy tonkatsu will sort you out."
    scene d21s04-36-mc-talk-mh with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Oh boy. Nothing like eating mind-numbingly spicy food to get over a tragic betrayal."
    scene d21s04-37-mh-talk-mc with dissolve
    play voice3 lissa_ugu noloop
    mh "Exactly."
    $ renpy.music.set_volume(0.8, 3.0, "music" )
    scene d21s04-38-mc-mh-at-restaurant with Fade(0.9, 0.5, 0.9)
    play sound2 park fadein 3.0
    pause
    scene d21s04-39-mc-mh-at-restaurant with dissolve
    pause
    $ renpy.music.set_volume(0.5, 3.0, "music" )
    scene d21s04-41-mh-talk-mc with dissolve
    play voice3 lissa_laugh noloop
    mh "*Laughing* I need you to stop making me laugh while I have food in my mouth."
    scene d21s04-40-mc-mh-at-restaurant with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "But it's so funny though! You look like a cute little chipmunk."
    mc "Alright. Alright. I'll lay off the jokes for now. But continue what you were saying."
    scene d21s04-44-mh-talk-mc with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    mh "Right. As I was saying before you {i}rudely{/i} interrupted me."
    mh "I haven't really had many other relationships aside from Allison, and you already know about that."
    mh "There were certain other people that I had a connection with but none of them evolved into anything more."
    scene d21s04-42-mc-talk-mh with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Just sex then?"
    scene d21s04-46-mh-talk-mc with dissolve
    play voice3 lissa_haha2 noloop
    mh "*Chuckles* Not exactly. There was a lot of cuddling as well."
    scene d21s04-43-mc-talk-mh with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "*Chuckles* Woah. Scandalous. Any hand holding?"
    scene d21s04-48-mh-talk-mc with dissolve
    play voice3 lissa_oh noloop
    mh "Oh, we held hands all over the place."
    mh "*Laughs* It was more for us to not be completely lonely, to be perfectly honest."
    scene d21s04-49-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    mh "Most of us were laser-focused on our studies. So we had a sort of...camaraderie."
    scene d21s04-47-mc-talk-mh with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "You understood each other."
    scene d21s04-51-mh-talk-mc with dissolve
    play voice3 dahlia_yes_ugu noloop volume 0.8
    mh "Exactly. And some of us were there for each other. Emotionally, and sometimes, physically."
    scene d21s04-50-mc-talk-mh with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "I bet you got up to all sorts of kinky stuff in your dorm then, huh?"
    scene d21s04-53-mh-talk-mc with dissolve
    play voice3 lissa_lno noloop
    mh "Would you believe me if I said no?"
    mh "I was surprisingly...vanilla back then."
    scene d21s04-52-mc-talk-mh with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Seriously?"
    if d19s03_watersports is True:
        mc "This coming from the woman with a piss kink?"
    scene d21s04-56-mh-talk-mc with dissolve
    play voice3 lissa_yes noloop
    mh "Yes! Seriously. I didn't start to open up more sexually until after I graduated."
    mh "But I still wouldn't consider myself especially kinky."
    scene d21s04-57-mc-talk-mh with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "*Chuckles* What {i}are{/i} your kinks, though? We never talked about it."
    scene d21s04-58-mh-talk-mc with dissolve
    play voice3 nora_huh noloop
    mh "Do you really want to talk about something like that here? In public?"
    scene d21s04-59-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Why not? It's a free country."
    scene d21s04-60-mc-talk-mh with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "Besides. There's barely anyone else here."
    $ unlock_gallery_slot("cg", "d21s04")
    scene d21s04-62-mh-talk-mc with dissolve
    play voice3 lissa_haha noloop
    mh "*Chuckles* Well..."
    if d19s03_watersports is True:
        mh "You already know about my interest in certain...{i}watersports{/i}."
        mh "Beyond that, I also like to take a submissive role in bed. But I would actually consider myself a switch."
    elif True:
        mh "Well, I generally like to take a submissive role in bed, but I would actually consider myself a switch."
    scene d21s04-63-mc-talk-mh with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh?"
    scene d21s04-64-mh-talk-mc with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    mh "It doesn't come out all that often, but sometimes...I like to get somewhat dominant as well."
    play voice2 mc_thinking_emm1 noloop
    if date_mh_bdsm is True:
        scene d21s04-65-mc-talk-mh with dissolve
        mc "Do you now? Looks like someone's gunning for my position."
        scene d21s04-70-mh-talk-mc with dissolve
        play voice3 dahlia_disappointed_hmm2 noloop
        mh "{size=23}Only if you want me to be in that position, {i}Sir{/i}.{/size}"
    elif True:
        scene d21s04-65-mc-talk-mh with dissolve
        mc "Have you ever wanted to be dominant with me?"
        scene d21s04-66-mh-talk-mc with dissolve
        play voice3 dahlia_thinking_mmm1 noloop
        mh "Well... Sometimes."
        scene d21s04-67-mc-talk-mh with dissolve
        play voice2 mc_hey_hey2 noloop
        mc "Why didn't you say anything?"
        scene d21s04-68-mh-talk-mc with dissolve
        play voice3 dahlia_disappointed_hmm2 noloop
        mh "You made it clear that you were new to this sort of relationship when we first met."
        mh "I didn't want to push you onto anything too fast and hurt you."
        mh "And it wasn't like I {i}wasn't{/i} enjoying our time together."
    scene d21s04-71-mh-talk-mc with dissolve
    mh "Beyond that, however, I don't have many other \"serious\" kinks. But I'm open to most things."
    scene d21s04-72-mc-talk-mh with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Hm. I'll take that as an open invitation to try out some absolutely heinous kinks in the bedroom then."
    scene d21s04-73-mh-talk-mc with dissolve
    play voice3 lissa_ha noloop
    mh "That's what I like about you, [mcname]."
    scene d21s04-74-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "What do you mean?"
    scene d21s04-75-mh-talk-mc with dissolve
    play voice3 lissa_mmm1 noloop
    mh "You got me to open up to experience a lot more things without once feeling uncomfortable or judged."
    mh "I...I appreciate you. A lot."
    scene d21s04-76-mh-talk-mc with dissolve
    play voice3 lissa_moan3 noloop
    mh "I had everything I ever wanted when I met you."
    mh "But then you showed me that there's more. That I wanted more. That I needed more."
    mh "And... I just wanted to say thank you."
    scene d21s04-77-mc-talk-mh with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "I guess you could say that I really {i}showed you the world{/i}, huh?"
    scene d21s04-78-mh-looks-away with dissolve
    play voice3 stacy_smell noloop
    pause
    scene d21s04-79-mc-talk-mh with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "...But I'm assuming there's more to it?"
    if d21s04_love_lc is False:
        jump d21s04_mh_end_choice
    elif True:
        scene d21s04-80-if-mh-talk-mc with dissolve
        play voice3 dahlia_thinking_hmm1 noloop
        mh "Nevermind. I'm just getting sentimental. Looks like the spice is getting to me instead of you."
        scene d21s04-81-if-mc-talk-mh with dissolve
        play voice2 mc_happy_a1 noloop
        mc "Lyssa. You know you can tell me anything, right?"
        scene d21s04-82-if-mh-talk-mc with dissolve
        play voice3 lissa_aga noloop
        mh "I know. I appreciate that. That's all."
        scene d21s04-83-if-mc-talk-mh with dissolve
        play voice2 mc_yes_okay1 noloop
        mc "Okay."

        jump d21s04_end

label d21s04_mh_end_choice hide:

    if from_ending_menu is True:
        $ renpy.music.set_volume(0.5, 3.0, "music" )
        play music music_decision_made fadein 3.0
    scene d21s04-82-if-mh-talk-mc with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    mh "*Sigh* You're also very young."
    mh "You have a whole life ahead of you."
    scene d21s04-84-mc-talk-mh with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "Lyssa, c'mon. You're talking like you're decades older than me."
    scene d21s04-85-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    mh "I know. It's not just age. It's..."
    mh "When I said that you've showed me what I wanted, this is—"
    scene d21s04-86-mh-talk-mc with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    mh "*Sigh* I'm sorry. I'm just not sure how exactly to say this."
    scene d21s04-87-mc-talk-mh with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "It's okay."
    scene d21s04-88-mh-talk-mc with dissolve
    play voice3 lissa_laugh noloop
    mh "*Chuckles* You'd think all my experience defending clients would come in handy to find the words, but no."
    scene d21s04-89-mh-talk-mc with dissolve
    mh "So I'll say this as plainly as I can."
    scene d21s04-90-c1-c2-mh-talk-mc with dissolve
    play voice3 lissa_moan2 noloop
    mh "I love you, [mcname]. And I want to have a serious relationship with you."
    mh "But I'm afraid because that is a big commitment and I'm not sure whether you want that or not."
    if d17s05_mh_sy is True:
        mh "And it's not just you, either. I've been thinking a lot about Stacy as well."
        scene d21s04-91-mc-talk-mh with dissolve
        play voice2 d1s2_hmm noloop volume 1.8
        mc "Stacy?"
        scene d21s04-92-mh-talk-mc with dissolve
        play voice3 lissa_yes noloop
        mh "Yes. I know we've only met a handful of times, but she has really grown on me. To say the least."
        scene d21s04-93-mc-talk-mh with dissolve
        play voice2 mc_happy_hah2 noloop
        mc "*Chuckles* She'd probably literally pass out from excitement if she heard you say that."
    if d17s05_mh_op is True:
        mh "And it's not just you, either. I've been thinking a lot about Oliver as well."
        scene d21s04-91-mc-talk-mh with dissolve
        play voice2 d1s2_hmm noloop volume 1.8
        mc "Oliver?"
        scene d21s04-92-mh-talk-mc with dissolve
        play voice3 lissa_yes noloop
        mh "Yes. Ever since you told me about his feelings for you, and he showed me the feelings he had for me. He has...really grown on me. To say the least."
        scene d21s04-93-mc-talk-mh with dissolve
        play voice2 mc_happy_hah2 noloop
        mc "*Chuckles* I wonder what he'd say if he heard you right now."
    scene d21s04-94-mh-laughs with dissolve
    play voice3 lissa_haha2 noloop
    mh "*Laughs*"
label ending_02_return hide:
label ending_03_return hide:
label ending_05_return hide:
    scene d21s04-95-mh-talk-mc with dissolve
    queue voice3 lissa_thinking noloop
    mh "So there it is. All my feelings laid bare."
    if from_ending_menu is True:
        if d17s05_mh_sy is True:
            $ d21s04_mh_end = 2
            jump d21s04_mh_sy_end
        elif d17s05_mh_op is True:
            $ d21s04_mh_end = 3
            jump d21s04_mh_op_end
        elif True:
            $ d21s04_mh_end = 1
            jump d21s04_mh_solo_end
    if d21s04_is_lyssa_solo_available or d21s04_is_lyssa_stacy_available or d21s04_is_lyssa_oliver_available:
        call update_ending_variables from _call_update_ending_variables
    if d21s04_is_lyssa_solo_available:
        $ unlock_ending("02")
    if d21s04_is_lyssa_stacy_available is True:
        $ unlock_ending("03")
    if d21s04_is_lyssa_oliver_available is True:
        $ unlock_ending("05")
    scene d21s04-96-c1-c4-choice-menu with dissolve
    menu:
        "I want to be with you"(hint="d21s04m02c01") if d21s04_is_lyssa_solo_available is True:
            $ d21s04_mh_end = 1
            jump d21s04_mh_solo_end

        "I want to be with you and Stacy"(hint="d21s04m02c02") if d21s04_is_lyssa_stacy_available is True:
            $ d21s04_mh_end = 2
            jump d21s04_mh_sy_end

        "I want to be with you and Oliver"(hint="d21s04m02c03") if d21s04_is_lyssa_oliver_available is True:
            $ d21s04_mh_end = 3
            jump d21s04_mh_op_end
        "I need to think about this"(hint="d21s04m02c04") if True:

            $ d21s04_mh_end = 4
            jump d21s04_continue

label d21s04_mh_solo_end hide:

    scene d21s04-97-c1-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Lyssa. I want to be with you too."
    mc "Yours and yours alone."
    scene d21s04-98-c1-mc-talk-mh with dissolve
    mc "And I'll do anything to be with you."

    jump d21s04_mcgoeswithmh

label d21s04_mh_sy_end hide:

    scene d21s04-99-c1-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Lyssa. I want to be with you and Stacy too."
    scene d21s04-100-c4-mc-talk-mh with dissolve
    mc "You two mean the world to me."

    jump d21s04_mcgoeswithmh

label d21s04_mh_op_end hide:

    scene d21s04-99-c1-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Lyssa. I want to be with you too. And I want to see where we go with Oliver."
    scene d21s04-100-c4-mc-talk-mh with dissolve
    mc "I know that it hasn't been long, but I don't care. I want this. I know that."

    jump d21s04_mcgoeswithmh

label d21s04_continue hide:

    scene d21s04-101-c4-mc-talk-mh with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "Lyssa... I..."
    scene d21s04-102-c4-mc-talk-mh with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "I really care about you as well."
    mc "And I wish that I could just say what you want to hear, but I need time to think this over."
    scene d21s04-103-c4-mh-talk-mc with dissolve
    play voice3 lissa_oh noloop
    mh "I understand. You don't need to say anything more."
    scene d21s04-104-c4-mh-talk-mc with dissolve
    play voice3 dahlia_sex_closedmoan1 noloop
    mh "Regardless of what you choose, I will always remember our time together fondly. And I still appreciate everything you've shown me."
    $ renpy.music.set_volume(0.8, 3.0, "music" )
    scene d21s04-105-c5-mc-mh-end-1 with dissolve
    pause

    jump d21s04_end

label d21s04_mcgoeswithmh:

    scene d21s04-106-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    mh "Really? Are you really ready to leave all your other girls behind?"
    scene d21s04-107-mc-talk-mh with dissolve
    play voice2 mc_yes_yes1 noloop
    if d21s04_mh_end is 1:
        mc "Yes. For you, I'd do it in a heartbeat."
    elif d21s04_mh_end is 2:
        mc "Yes. For you and Stacy, I'd do anything."
    elif d21s04_mh_end is 3:
        mc "Yes. For you, I'd do anything."
    scene d21s04-108-mc-talk-mh with dissolve
    mc "I love you, Lyssa."
    scene d21s04-109-mh-talk-mc with dissolve
    play voice3 dahlia_pain_sobs noloop
    mh "*Smiles* I think I got something in my eye."
    $ renpy.music.set_volume(0.8, 3.0, "music" )
    scene d21s04-110-c5-mc-mh-end-2 with dissolve
    pause

    stop sound2 fadeout 3.0
    $ renpy.music.set_volume(1.0, 10.0, "sound2" )
    if d21s04_mh_end is 1:
        jump ending_02
    elif d21s04_mh_end is 2:
        jump ending_03
    elif d21s04_mh_end is 3:
        jump ending_05
    elif True:
        jump d21s04_end

label d21s04_end:

    stop sound2 fadeout 3.0
    $ renpy.music.set_volume(1.0, 10.0, "sound2" )
    stop music fadeout 6.0
    jump d21s05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
