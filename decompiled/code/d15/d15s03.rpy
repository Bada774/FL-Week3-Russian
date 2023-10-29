label d15s03:

    if not hasattr(renpy.store, "d12s02_gavepass"):
        if hasattr(renpy.store, "d11s02_gavepass"):
            $ d12s02_gavepass = d11s02_gavepass
        elif True:
            $ d12s02_gavepass = False

    $ d15s03_quartet = False

    scene black
    show screen scene_transistion(_("20 minutes later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    play sound sfx_door_closed1
    hide screen scene_transistion
    scene d15s03-01 mc-pt-room-entry1_c1
    with Fade(0.5, 0.5, 0.9)
    mct "Just need to get my stuff and-"
    $ renpy.music.set_volume(0.8, 3.0, "music")
    play music thinking_music_1
    scene d15s03-01 mc-pt-room-entry1_c2 with dissolve
    pause
    scene d15s03-02 mc-pt-room-entry2_c2 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, hey Pete. {w}It's almost weird seeing you here."
    scene d15s03-02 mc-pt-room-entry2_c1 with dissolve
    play voice3 pete_thinking_hmm1 noloop
    pb "Likewise. It seems like I've been spending more time in our room than you have lately."
    scene d15s03-03 mc-pt-room-entry3_c2 with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Seriously? Next thing you're going to tell me you've been spending all your free time studying."
    scene d15s03-03 mc-pt-room-entry3_c1 with dissolve
    play voice3 pete_arrogant_heh1 noloop
    pb "Funny you should mention that."
    play sound sfx_cloth_rustling2
    scene d15s03-05 mc-pt-room-talk1_c2 with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "You're shitting me."
    scene d15s03-05 mc-pt-room-talk1_c1 with dissolve
    play voice3 pete_arrogant_laugh noloop
    pb "Hand to dog."
    scene d15s03-06 mc-pt-room-talk2_c2 with dissolve
    play voice2 d1s5_mchappy noloop
    mc "Shit. I need to study a lot more too. Finals are just a few days away."
    scene d15s03-06 mc-pt-room-talk2_c1 with dissolve
    play voice3 pete_hey_attention noloop
    pb "Hey... I've been wanting to ask you something."
    scene d15s03-06 mc-pt-room-talk2_c2 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "What's up?"

    if d12s02_gavepass is False:
        jump d15s03_hr_theft
    elif True:
        jump d15s03_middle

label d15s03_hr_theft:

    scene d15s03-07 mc-pt-room-talk3_c1 with dissolve
    play voice3 pete_thinking_hmm4 noloop
    pb "You haven't been messing with my stuff, have you?"
    scene d15s03-07 mc-pt-room-talk3_c2 with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What? No. {w}Why do you ask?"
    scene d15s03-08 mc-pt-room-talk4_c1 with dissolve
    play voice3 pete_thinking_hmm6 noloop
    pb "My laptop is missing."
    scene d15s03-08 mc-pt-room-talk4_c2 with dissolve
    play voice2 mc_scared_huh2 noloop
    mc "Did somebody steal it?"
    scene d15s03-09 mc-pt-room-talk5_c1 with dissolve
    play voice3 pete_yes_yeah noloop
    pb "Well, it was here on my desk like always. Then it wasn't here. So, yeah, someone took it."
    scene d15s03-09 mc-pt-room-talk5_c2 with dissolve
    play voice2 mc_pain_ffff noloop
    mc "Fuck. That sucks. {w}Maybe one of the guys is pranking you?"
    scene d15s03-10 mc-pt-room-talk6_c1 with dissolve
    play voice3 pete_no_nah noloop
    pb "Nah, they'd leave a note or a soiled condom or something. It wouldn't just be gone."
    scene d15s03-10 mc-pt-room-talk6_c2 with dissolve
    mc "Fucking combination locks. I guess we could ask around if someone has been standing outside our room a lot recently."
    scene d15s03-11 mc-pt-room-talk7_c1 with dissolve
    pb "Maybe. {w}Are you sure you didn't... ya'know?"
    scene d15s03-11 mc-pt-room-talk7_c2 with dissolve
    play voice2 mc_no_no4 noloop
    mc "Fuck no! Would I do that to you?"
    scene d15s03-12 mc-pt-room-talk8_c1 with dissolve
    play voice3 pete_happy_laugh2 noloop
    pb "It's just the other day... maybe a week or two ago? You were jerking off at my desk?"
    scene d15s03-12 mc-pt-room-talk8_c2 with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Oh, yeah. The spinny chair."
    scene d15s03-13 mc-pt-room-talk9_c1 with dissolve
    play voice3 pete_hey_heyo noloop
    pb "If you accidentally broke my laptop doing something... I could see why you'd try to hide it, but I wouldn't be pissed at you, ya'know?"
    scene d15s03-13 mc-pt-room-talk9_c2 with dissolve
    play voice2 mc_no_noway noloop
    mc "No, no, no. Man, hell no. {w}If I did something like that I'd come clean with you straight up."
    scene d15s03-14 mc-pt-room-talk10_c1 with dissolve
    play voice3 pete_disappointed_geh1 noloop
    pb "Cool, brah. My bad, I shouldn't have even asked."
    scene d15s03-14 mc-pt-room-talk10_c2 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Nah, we're cool. No harm, no foul. It was a reasonable ask."
    scene d15s03-07 mc-pt-room-talk3_c1 with dissolve
    play voice3 pete_thinking_mmf noloop
    pb "Thanks. So, anyone you can think of that would have taken it?"
    scene d15s03-07 mc-pt-room-talk3_c2 with dissolve
    mct "Would Hana have done that? Would she have told me if she did?"
    play voice2 mc_thinking_emm1 noloop
    mc "Well, actually..."
    play voice3 pete_angry_ergh3 noloop
    scene d15s03-08 mc-pt-room-talk4_c1 with dissolve
    pb "Who?"
    scene d15s03-08 mc-pt-room-talk4_c2 with dissolve
    play voice2 d2s9_confused noloop
    mc "I was just thinking maybe it was Samiya."
    scene d15s03-09 mc-pt-room-talk5_c1 with dissolve
    play voice3 pete_surprised_huh2 noloop
    pb "Samiya? {w}Huh. She does know where our room is."
    scene d15s03-09 mc-pt-room-talk5_c2 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "And she did steal Stacy's luggage when she was pissed at you that one time."
    scene d15s03-10 mc-pt-room-talk6_c1 with dissolve
    play voice3 pete_disappointed_ehh2 noloop
    pb "I haven't done anything to piss her off since then... {w}that I know of..."
    scene d15s03-10 mc-pt-room-talk6_c2 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "And if you accuse her of stealing your laptop that could piss her off."
    scene d15s03-11 mc-pt-room-talk7_c1 with dissolve
    play voice3 pete_thinking_hmm2 noloop
    pb "And then she would just steal something else to prove that she didn't steal anything."
    scene d15s03-11 mc-pt-room-talk7_c2 with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "As weird as that sounds, you're probably right."
    scene d15s03-12 mc-pt-room-talk8_c1 with dissolve
    play voice3 pete_disappointed_mmf1 noloop
    pb "Fuck. Well, there's nothing for it."
    scene d15s03-12 mc-pt-room-talk8_c2 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "How's that?"
    scene d15s03-13 mc-pt-room-talk9_c1 with dissolve
    pb "If I go around looking for who stole it, I'll just make things worse."
    pb "So, I just gotta say, \"It's gone\" and move on with my life."
    scene d15s03-13 mc-pt-room-talk9_c2 with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "Wow. That's really chill of you."
    scene d15s03-14 mc-pt-room-talk10_c1 with dissolve
    play voice3 pete_yes_yeah noloop
    pb "Yeah, I've been trying this Zen meditation stuff..."
    scene d15s03-14 mc-pt-room-talk10_c2 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Really? How did you get into that?"
    scene d15s03-11 mc-pt-room-talk7_c1 with dissolve
    play voice3 pete_disgust_oof1 noloop
    pb "Have you ever tried Hot Yoga? There are so many positions."
    scene d15s03-11 mc-pt-room-talk7_c2 with dissolve
    play voice2 mc_no_nah1 noloop
    mc "I really don't want to imagine you hot, sweaty, and stretching."
    scene d15s03-12 mc-pt-room-talk8_c1 with dissolve
    play voice3 pete_happy_laugh5 noloop
    pb "Ha! You'd love it, dude. {w}I'm the only guy in class."

    jump d15s03_middle

label d15s03_middle:

    if d11s05_pb_retention is True and is_antagonist_mode is True:
        call buzz from _call_buzz
        scene d15s03-18 mc-pt-room-stand-phone_c1 with dissolve
        play voice3 pete_angry_fuck1 noloop
        pb "What the fuck...? Again?!"
        scene d15s03-18 mc-pt-room-stand-phone_c2 with dissolve
        play voice2 d1s2_hmm noloop
        mc "What is it?"
        scene d15s03-16 mc-pt-room-stand-talk2_c1 with dissolve
        play voice3 pete_angry_ehh1 noloop
        pb "I don't know. This app has been all buggy recently."
        scene d15s03-16 mc-pt-room-stand-talk2_c2 with dissolve
        play voice2 mc_thinking_mmm4 noloop
        mc "What do you mean?"
        scene d15s03-17 mc-pt-room-stand-talk3_c1 with dissolve
        play voice3 pete_angry_hmm5 noloop
        pb "Fetish Locator. It keeps trying to get me to do really weird shit."
        scene d15s03-17 mc-pt-room-stand-talk3_c2 with dissolve
        play voice2 mc_pain_ou1 noloop
        mc "Oh?"
        scene d15s03-19 mc-pt-room-stand-talk4_c1 with dissolve
        play voice3 pete_yes_simple1 noloop
        pb "Yeah, it says it is some kind of retainer program... some kinda 3rd party bullshit."
        scene d15s03-19 mc-pt-room-stand-talk4_c2 with dissolve
        mc "What is it trying to get you to do?"
        scene d15s03-20 mc-pt-room-stand-talk5_c1 with dissolve
        pb "You don't want to know. It's some disgusting shit."
        scene d15s03-20 mc-pt-room-stand-talk5_c2 with dissolve
        play voice2 mc_arrogant_hm1 noloop
        mc "So, you're not doing it?"
        scene d15s03-21 mc-pt-room-stand-talk6_c1 with dissolve
        play voice3 pete_no_simple3 noloop
        if persistent.is_special is True:
            pb "Hell no. I'm not about to shit in some guy's mouth and I sure as fuck ain't gonna let some slut do that to me."
        elif True:
            pb "Hell no. I mean, if that's the way a guy swings, fine for him. That shit isn't for me."
        scene d15s03-21 mc-pt-room-stand-talk6_c2 with dissolve
        play voice2 mc_scared_oh2 noloop
        mc "Woah! Yeah, I don't blame you, but..."
        scene d15s03-22 mc-pt-room-stand-talk7_c1 with dissolve
        play voice3 pete_thinking_hmm1 noloop
        pb "But what?"
        scene d15s03-22 mc-pt-room-stand-talk7_c2 with dissolve
        play voice2 d2s12_emmm noloop
        mc "What happens if you don't... {w}er, what do you get for doing that stuff, if you did it?"
        scene d15s03-23 mc-pt-room-stand-talk8_c1 with dissolve
        pb "Jack shit. {w}It claims that it will share my pics with my parents or something, but I don't care about that."
        scene d15s03-23 mc-pt-room-stand-talk8_c2 with dissolve
        play voice2 mc_scared_huuuh1 noloop
        mc "Really?"
        scene d15s03-24 mc-pt-room-stand-talk9_c1 with dissolve
        play voice3 pete_arrogant_pff1 noloop
        pb "Dude, if you knew half the things my parents have seen-"
        scene d15s03-24 mc-pt-room-stand-talk9_c2 with dissolve
        play voice2 mc_thinking_emm1 noloop
        mc "You know what, I think I'd rather not know."
        scene d15s03-16 mc-pt-room-stand-talk2_c1 with dissolve
        play voice3 pete_yes_ugu1 noloop
        pb "Exactly. Let's talk about something else."
        scene d15s03-16 mc-pt-room-stand-talk2_c2 with dissolve
        play voice2 mc_happy_a1 noloop
        mc "What's on your mind?"
    scene d15s03-17 mc-pt-room-stand-talk3_c1 with dissolve
    play voice3 pete_thinking_mmf noloop
    pb "I, uh... {w} I heard some rumors through the grapevine. Any truth to them?"
    scene d15s03-17 mc-pt-room-stand-talk3_c2 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "I guess that depends on the rumors. What are people saying?"
    scene d15s03-19 mc-pt-room-stand-talk4_c1 with dissolve
    play voice3 pete_arrogant_heh2 noloop
    pb "Well, it sounds like you and Lydia are getting pretty damn serious."
    scene d15s03-19 mc-pt-room-stand-talk4_c2 with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Oh, yeah. Fuck, I should have told you."
    scene d15s03-20 mc-pt-room-stand-talk5_c1 with dissolve
    play voice3 pete_arrogant_huh2 noloop
    pb "Wedding bells ringing?"
    scene d15s03-20 mc-pt-room-stand-talk5_c2 with dissolve
    play voice2 mc_happy_hah1 noloop
    mc "Ha! I wish. {w}Wait, seriously? Is that what people are saying?"
    scene d15s03-21 mc-pt-room-stand-talk6_c1 with dissolve
    play voice3 pete_yes_yeah noloop
    pb "Yeah. Somebody said that you two were at a jewelry store, shopping for rings."
    scene d15s03-21 mc-pt-room-stand-talk6_c2 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "I think they were pulling your leg."
    if love_lc is True:
        mc "Don't get me wrong, I love her. We just haven't known each other that long."
    elif True:
        mc "Don't get me wrong. She's the woman of my dreams, but no, we haven't gone shopping at any jewelry shops."
    scene d15s03-22 mc-pt-room-stand-talk7_c1 with dissolve
    play voice3 pete_surprised_oh1 noloop
    pb "Oh, cool. Does she know that you're...?"
    scene d15s03-22 mc-pt-room-stand-talk7_c2 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "That I'm screwing every woman I can get my hands on?"
    scene d15s03-23 mc-pt-room-stand-talk8_c1 with dissolve
    play voice3 pete_arrogant_yeah1 noloop
    pb "Yeah."
    scene d15s03-15 mc-pt-room-stand-talk11_c2 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Yep. She's cool with it."
    scene d15s03-15 mc-pt-room-stand-talk11_c1 with dissolve
    play voice3 pete_surprised_ohmy1 noloop
    pb "Fucken hell, dude. {w}You better slap a ring on that fast."

    if date_dw is True:
        jump d15s03_dw_setup
    elif True:
        jump d15s03_end

label d15s03_dw_setup:

    scene d15s03-26 mc-pt-room-sit2_c2 with dissolve
    play voice2 d3s11b_mcheh noloop
    mc "Ha! {w}I'll think about it. Was that all the rumors?"
    scene d15s03-26 mc-pt-room-sit2_c1 with dissolve
    play voice3 pete_thinking_hmm3 noloop
    pb "There was one more. Sounds like you've been getting pretty serious with Dahlia as well."
    scene d15s03-27 mc-pt-room-sit3_c2 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Oh, yeah."
    scene d15s03-27 mc-pt-room-sit3_c1 with dissolve
    play voice3 pete_thinking_hmm7 noloop
    pb "Does she know about Lydia?"
    scene d15s03-28 mc-pt-room-sit4_c2 with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "I don't know.{w}.. I don't think so."
    scene d15s03-29 mc-pt-room-sit5_c1 with dissolve
    play voice3 pete_thinking_mmf noloop
    pb "Does she know about the other women you've been fucking?"
    scene d15s03-29 mc-pt-room-sit5_c2 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "I don't know.{w}.. maybe? She should. I don't think I've told her, but it's not like I've been hiding it."
    mc "I mean, I know she saw me and Samiya together yesterday."
    scene d15s03-31 mc-pt-room-sit7_c1 with dissolve
    play voice3 pete_surprised_what3 noloop
    pb "You were with Samiya?"
    scene d15s03-31 mc-pt-room-sit7_c2 with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "It was an event at a party, ya'know? {w}Started as mud wrestling, ended up being something else."
    scene d15s03-35 mc-pt-room-sit10_c1 with dissolve
    play voice3 pete_surprised_huh3 noloop
    pb "Dahlia saw that?"
    scene d15s03-35 mc-pt-room-sit10_c2 with dissolve
    play voice2 mc_no_nono1 noloop
    mc "I don't think so. I ran into her after Samiya and I got out of the shower."
    mc "She said something about Samiya fucking someone else's boyfriend \"again\"."
    scene d15s03-30 mc-pt-room-sit6_c1 with dissolve
    play voice3 pete_yes_simple3 noloop
    pb "Yeah... {w}That girl is damaged goods, ya'know?"
    scene d15s03-30 mc-pt-room-sit6_c2 with dissolve
    play voice2 d1s2_hmm noloop
    mc "Samiya? I mean, she's a-"
    scene d15s03-34 mc-pt-room-sit9_c1 with dissolve
    play voice3 pete_no_nonono noloop
    pb "No. I mean Dahlia. She's got this fucked up Predator versus Prey way of looking at things."
    scene d15s03-34 mc-pt-room-sit9_c2 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Huh? {w}I mean, she's a dominatrix, but-"
    scene d15s03-26 mc-pt-room-sit2_c1 with dissolve
    play voice3 pete_no_uhuh noloop
    pb "She's not a dom. She's not a sub. She's not a switch."
    scene d15s03-26 mc-pt-room-sit2_c2 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What are you talking about?"
    scene d15s03-27 mc-pt-room-sit3_c1 with dissolve
    play voice3 pete_disappointed_ehh2 noloop
    pb "It all goes back to some bad blood between her and Samiya over some prom incident with Dahlia's boyfriend back then... I don't know all the details."
    scene d15s03-27 mc-pt-room-sit3_c2 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, I heard about that, but what are you talking about?"
    scene d15s03-28 mc-pt-room-sit4_c1 with dissolve
    play voice3 pete_thinking_hmm4 noloop
    pb "As far as Dahlia is concerned everyone - especially Samiya - is either a predator or prey. If you show weakness, she treats you as prey."
    pb "If you show strength, she submits like you're the predator and she's the prey."
    scene d15s03-28 mc-pt-room-sit4_c2 with dissolve
    play voice2 d1s5b_ehhh noloop
    mc "You're losing me with this whole predator/prey thing. What are you trying to say?"
    scene d15s03-29 mc-pt-room-sit5_c1 with dissolve
    play voice3 pete_hey_angry noloop
    pb "I'm saying that if you aren't strong, she thinks you're weak. You've gotta be strong. And in her mind the strongest person she's ever met is Samiya."
    scene d15s03-29 mc-pt-room-sit5_c2 with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "Huh."
    scene d15s03-30 mc-pt-room-sit6_c1 with dissolve
    play voice3 pete_arrogant_heh2 noloop
    pb "So, unless you want Dahlia walking all over you... well, you know what you've gotta do, right?"
    scene d15s03-30 mc-pt-room-sit6_c2 with dissolve
    play voice2 d9s2_ugu noloop
    mc "Yeah, I think I get it."
    scene d15s03-29 mc-pt-room-sit5_c2 with dissolve
    mct "I should get Dahlia and Samiya together and show them both who is boss."
    mct "Then I can work out Dahlia's issues with Samiya, show Dahlia that I'm strong."
    mct "Then we can have a healthy sexual relationship where she knows I'm strong and yet I'm submitting to her, rather than her just pushing me around."
    scene d15s03-31 mc-pt-room-sit7_c1 with dissolve
    play voice3 pete_hey_heyo noloop
    pb "You still there? You tune out on me?"
    scene d15s03-31 mc-pt-room-sit7_c2 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, yeah. I know exactly what to do."
    scene d15s03-35 mc-pt-room-sit10_c1 with dissolve
    play voice3 pete_yes_ugu2 noloop
    pb "Okay then. {w}Show her who's boss."
    scene d15s03-35 mc-pt-room-sit10_c2 with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Exactly."
    if date_dw is True and cage_ntr is False and pete_ntr is True:
        scene d15s03-34 mc-pt-room-sit9_c1 with dissolve
        play voice3 pete_happy_relief1 noloop
        pb "*sigh* There must be some kind of way outta here."
        scene d15s03-33 mc-pt-room-sit8_c2 with dissolve
        play voice2 d1s5_mcthinks noloop
        mc "How's that?"
        scene d15s03-31 mc-pt-room-sit7_c1 with dissolve
        play voice3 pete_thinking_hmm11 noloop
        pb "Studying, working our butts off in class, trying to make sense out of all this confusion."
        scene d15s03-34 mc-pt-room-sit9_c2 with dissolve
        play voice2 mc_yes_yeah7 noloop
        mc "Yeah, but you always skate by. Nobody's going to fail you or risk your scholarship."
        scene d15s03-33 mc-pt-room-sit8_c1 with dissolve
        play voice3 pete_disappointed_mmf1 noloop
        pb "Ordinarily I'd agree with you, but this season... I don't know."
        pb "I push myself as hard as I can out there on the court and I talk a good game, but..."
        pb "They might not think it is worth passing me this semester."
        scene d15s03-35 mc-pt-room-sit10_c2 with dissolve
        play voice2 mc_no_nah2 noloop
        mc "No reason to get excited. There are many fans here that love you and want to see you succeed."
        mc "I'm sure you've got some serious support among the alumni and donors that keep the lights on around campus."
        scene d15s03-35 mc-pt-room-sit10_c1 with dissolve
        play voice3 pete_arrogant_hm2 noloop
        pb "I just think that sometimes it's all one big joke."
        pb "Maybe I'm good enough for college, but no one is scouting me to go Pro."
        scene d15s03-25 mc-pt-room-sit1_c2 with dissolve
        play voice2 mc_thinking_hmm5 noloop
        mc "So, you get a degree and ride that with your charisma when you get out."
        scene d15s03-25 mc-pt-room-sit1_c1 with dissolve
        play voice3 pete_thinking_hmm3 noloop
        pb "Maybe. {w}Maybe I don't want to wait."
        scene d15s03-26 mc-pt-room-sit2_c2 with dissolve
        play voice2 mc_arrogant_hm1 noloop
        mc "What do you mean?"
        scene d15s03-26 mc-pt-room-sit2_c1 with dissolve
        play voice3 pete_surprised_huh2 noloop
        pb "What if you and me - just grab a couple of girls and take off?"
        scene d15s03-27 mc-pt-room-sit3_c2 with dissolve
        play voice2 mc_surprised_what2 noloop
        mc "What? Where?"
        scene d15s03-27 mc-pt-room-sit3_c1 with dissolve
        play voice3 pete_thinking_eeh1 noloop
        pb "The Bahamas. We hop in a car or grab a train ticket. Ride that down to Florida."
        pb "Catch a plane or ship out to the Bahamas and go into business with my Uncle Carlos."
        scene d15s03-28 mc-pt-room-sit4_c2 with dissolve
        play voice2 mc_surprised_huh6 noloop
        mc "Carlos?"
        scene d15s03-28 mc-pt-room-sit4_c1 with dissolve
        play voice3 pete_yes_yeah noloop
        pb "Yeah, Carlos. He used to be just Uncle Carl. Then he had one of those mid-life crisis things."
        pb "Cashed out his 401k and shit, moved to the Bahamas, and started calling himself Carlos."
        scene d15s03-29 mc-pt-room-sit5_c2 with dissolve
        play voice2 mc_thinking_hmm1 noloop
        mc "What's the business?"
        scene d15s03-29 mc-pt-room-sit5_c1 with dissolve
        play voice3 pete_arrogant_heh4 noloop
        pb "Rental cars. You believe it? He's pulling down almost seven figures a year renting caddies and fiats to tourists."
        scene d15s03-30 mc-pt-room-sit6_c2 with dissolve
        play voice2 mc_surprised_wow1 noloop
        mc "Damn. {w}Wait, do you even have a driver's license?"
        scene d15s03-30 mc-pt-room-sit6_c1 with dissolve
        play voice3 pete_yes_simple2 noloop
        pb "License, passport, and I even know who we should take with us."
        scene d15s03-33 mc-pt-room-sit8_c2 with dissolve
        play voice2 mc_arrogant_huh3 noloop
        mc "Who?"
        scene d15s03-33 mc-pt-room-sit8_c1 with dissolve
        play voice3 pete_disappointed_oof2 noloop
        pb "I'll bring Samiya - she needs out of her current situation so that's no problem there."
        scene d15s03-31 mc-pt-room-sit7_c2 with dissolve
        play voice2 mc_yes_aga2 noloop
        mc "And for me?"
        scene d15s03-31 mc-pt-room-sit7_c1 with dissolve
        play voice3 pete_thinking_hmm2 noloop
        pb "Well, it seems like you've got your pick of the ladies lately, but if we can keep them from killing each other..."
        scene d15s03-34 mc-pt-room-sit9_c2 with dissolve
        play voice2 mc_yes_okay2 noloop
        mc "You want Dahlia and Samiya and you and me to go to the Bahamas to rent cars to tourists."
        scene d15s03-34 mc-pt-room-sit9_c1 with dissolve
        play voice3 pete_happy_laugh1 noloop
        pb "Pretty much."
        scene d15s03-35 mc-pt-room-sit10_c2 with dissolve
        play voice2 mc_thinking_hmm2 noloop
        mc "Let's get through finals first. Maybe we can do that during the Summer."
        scene d15s03-35 mc-pt-room-sit10_c1 with dissolve
        play voice3 pete_angry_argh4 noloop
        pb "Fuck. {w}That means more studying."

        $ d15s03_quartet = True
    elif True:

        scene d15s03-35 mc-pt-room-sit10_c1 with dissolve

    jump d15s03_end

label d15s03_end:

    play voice3 pete_thinking_mmf noloop
    pb "Anyway, I am heading out.{w} Later dude."

    stop music fadeout 3.0
    jump d15s04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
