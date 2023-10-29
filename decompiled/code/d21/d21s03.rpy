label d21s03:

    $ d21s03_statement_1 = False
    $ d21s03_statement_2 = False

    if d21s02_bring_sy is True:
        scene d21s03-1 mc-arj-sy-start1_c2 with dissolve
        play voice3 amrose_arrogant_huh1 noloop
        arj "How'd it go?"
    elif d21s02_bring_arj is True:
        scene d21s03-1 mc-arj-sy-start1_c1 with dissolve
        play voice3 stacy_huh2 noloop
        sy "What's she sayin'?"
    scene d21s03-1 mc-arj-sy-start1_c3 with dissolve
    play voice2 d1s5_mchappy noloop
    mc "She—"
    scene d21s03-04 mc-vumc-talk1_c1 with dissolve
    play voice4 vumc_thinking_hmm6 noloop
    vumc "Excuse me. Are you [mcname] Young?"
    play voice2 mc_yes_yes2 noloop
    mc "Uh, yes. Yeah. That's me. Why?"
    play sound sfx_hands_clap2 volume 0.5
    scene d21s03-03 mc-vumc-handshake_c2 with dissolve
    play voice4 vumc_hey_simple2 noloop
    vumc "Nice to meet you, Mr. Young."
    vumc "My name is Matthew Cheney and I'm the lead on your case."
    scene d21s03-03 mc-vumc-handshake_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Nice to meet you too officer."
    scene d21s03-04 mc-vumc-talk1_c2 with dissolve
    play voice4 vumc_thinking_hmm3 noloop
    vumc "After you called in your report, we didn't manage to get a full statement from you."
    vumc "We looked for you at your dorm, but you weren't there."
    vumc "Would you mind coming with me to wrap that up now?"
    scene d21s03-04 mc-vumc-talk1_c1 with dissolve
    play voice2 d1s5b_emmm noloop volume 1.6
    mc "I don—"
    scene d21s03-05 mc-vumc-talk2_c2 with dissolve
    play voice4 vumc_arrogant_heh3 noloop
    vumc "I assure you, it'll only take a minute."
    scene d21s03-05 mc-vumc-talk2_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay. Sure, I guess."
    scene d21s03-06 mc-vumc-sy-arj-bye_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "You guys good to head off on your own? I can handle this."
    scene d21s03-06 mc-vumc-sy-arj-bye_c2 with dissolve
    play voice3 amrose_surprised_uh3 noloop
    arj "You sure?"
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah."
    scene d21s03-06 mc-vumc-sy-arj-bye_c3 with dissolve
    play voice3 amrose_yes_okay1 noloop
    arj "Okay, we'll head off then. Gimme a call after you're done."
    play voice4 stacy_hey noloop
    sy "Don't let him shake you down! Ask for a lawyer!"
    scene d21s03-07 mc-vumc-sy-arj-bye2_c2 with dissolve
    play voice3 vumc_happy_laugh8 noloop
    vumc "*Chuckles* They seem like good friends."
    scene d21s03-07 mc-vumc-sy-arj-bye2_c1 with dissolve
    play voice2 d9s2_yeah noloop volume 2.3
    mc "They are."
    play sound sfx_chair_slide1
    scene d21s03-10 mc-vumc-sit1_c2 with dissolve
    play voice3 vumc_yes_aga3 noloop
    vumc "Okay. This won't be long."
    vumc "And we're rolling. Let's start off with something simple..."
    vumc "Now, what's your relation to Lydia Cox?"
    scene d21s03-10 mc-vumc-sit1_c1 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Relation? Uh, I guess she's my girlfriend, or was my girlfriend."
    scene d21s03-11 mc-vumc-sit2_c2 with dissolve
    play voice3 vumc_yes_aga1 noloop
    vumc "Mm-hm, and when exactly did you meet her?"
    scene d21s03-11 mc-vumc-sit2_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "I'm not sure. We ran into each other a couple times on campus, but we never really met properly."
    mc "I guess if I have to put a date on it, it'd be the first FL— Uh, Fetish Locator, party."
    scene d21s03-12 mc-vumc-sit3_c2 with dissolve
    play voice3 vumc_thinking_mmm2 noloop
    vumc "Did Lydia throw this party?"
    scene d21s03-12 mc-vumc-sit3_c1 with dissolve
    play voice2 mc_no_no2 noloop
    mc "No. Well, I don't know. Min said something about the app—"
    scene d21s03-13 mc-vumc-sit4_c2 with dissolve
    play voice3 vumc_thinking_emm6 noloop
    vumc "I'm sorry, {i}\"Min\"{/i}?"
    scene d21s03-13 mc-vumc-sit4_c1 with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Oh, yeah. Min Eun-Soo is her full name, if I recall correctly."
    mc "The party was at her house. But it was sponsored by Fetish Locator. Or certain events were at least, I don't know the specifics."
    play sound sfx_keyboard_typing2
    scene d21s03-21 mc-vumc-desk1_c2 with dissolve
    play voice3 vumc_happy_hmm1 noloop
    vumc "Interesting. Did you feel like you were being coerced at any point during this event? Were you pressured to go to it perhaps?"
    scene d21s03-22 mc-vumc-desk2_c1 with dissolve
    play voice2 mc_no_no3 noloop
    mc "No, I did it 'cause I wanted to... Well. My friends talked about it and told me to go, and it wasn't like I was against the idea."
    stop sound fadeout 1.0
    scene d21s03-19 mc-vumc-sit10_c2 with dissolve
    play voice3 vumc_thinking_hm1 noloop
    vumc "\"Friends\"? Any specific friends that I should know about?"
    scene d21s03-19 mc-vumc-sit10_c1 with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Peter Butler and Kevin Bennet."
    if cage_ntr is True:
        scene d21s03-16 mc-vumc-sit7_c2 with dissolve
        play voice3 vumc_surprised_huh7 noloop
        vumc "Peter Butler? The same—"
        scene d21s03-16 mc-vumc-sit7_c1 with dissolve
        play voice2 mc_yes_yes1 noloop
        mc "Yes. The same."
        scene d21s03-17 mc-vumc-sit8_c2 with dissolve
        play voice3 vumc_disappointed_hmm1 noloop
        vumc "Are you sure he wasn't pushing you towards the party?"
        scene d21s03-17 mc-vumc-sit8_c1 with dissolve
        play voice2 d3s7_mcemm noloop volume 1.6
        mc "I... He talked about it, but I didn't feel like I was being pushed."
    play sound sfx_keyboard_typing2
    scene d21s03-23 mc-vumc-desk3_c2 with dissolve
    play voice3 vumc_yes_simple1 noloop
    vumc "Mm-hm. Noted."
    if cage_ntr is True:
        vumc "One last thing before we go to the next section."
        vumc "Did Lydia Cox abduct you?"
        menu:
            "Tell the truth"(hint="d21s03m01c01") if True:
                $ d21s03_statement_1 = True

                scene d21s03-23 mc-vumc-desk3_c1 with dissolve
                play voice2 mc_yes_yes3 noloop
                mc "...Yes."
                scene d21s03-24 mc-vumc-desk4_c2 with dissolve
                play voice3 vumc_surprised_huh3 noloop
                vumc "And how did this happen?"
                scene d21s03-24 mc-vumc-desk4_c1 with dissolve
                play voice2 mc_disappointed_ehh3 noloop
                mc "After I found out that she was behind the app, I was...not in a stable mood."
                mc "So I got drunk and passed out somewhere, I don't remember."
                mc "She then found me and brought me to her place and chained me up like a dog."
                scene d21s03-19 mc-vumc-sit10_c2 with dissolve
                play voice3 vumc_disappointed_mmm3 noloop
                vumc "Hm. I understand that it must be hard to talk about it. But this is very valuable information, Mr. Young."
            "Cover for Lydia"(hint="d21s03m01c02") if True:

                scene d21s03-23 mc-vumc-desk3_c1 with dissolve
                play voice2 mc_no_no5 noloop
                mc "No."
                scene d21s03-24 mc-vumc-desk4_c2 with dissolve
                play voice3 vumc_yes_questioning3 noloop
                vumc "Are you sure? From what I understand, you were held within her home against your will."
                scene d21s03-24 mc-vumc-desk4_c1 with dissolve
                play voice2 mc_disappointed_ehh3 noloop
                mc "I went there. I was drunk and...angry."
                mc "It was stupid of me, but she didn't abduct me."
                scene d21s03-21 mc-vumc-desk1_c2 with dissolve
                play voice3 vumc_disappointed_mmm3 noloop
                vumc "Hm. Interesting."

    vumc "You're doing great, by the way. Just a couple more things."
    vumc "Let's talk a little about this app, \"Fetish Locator\". When did you start using it?"
    scene d21s03-13 mc-vumc-sit4_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Around three weeks back. My friend, Kevin, introduced me to it."
    mc "It was taking off like wildfire all over campus."
    scene d21s03-13 mc-vumc-sit4_c2 with dissolve
    play voice3 vumc_thinking_hmm1 noloop
    vumc "Did you feel coerced to download the app in any way? Did Kevin push you towards it?"
    scene d21s03-18 mc-vumc-sit9_c1 with dissolve
    play voice2 d9s3_no noloop
    mc "No. He just told me about it. I downloaded it on my own."
    scene d21s03-15 mc-vumc-sit6_c2 with dissolve
    play voice3 vumc_yes_aga2 noloop
    vumc "And then what happened?"
    scene d21s03-17 mc-vumc-sit8_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "Well, it lived up to its name, I guess."
    mc "I used it to meet some people, I had some fun."
    scene d21s03-16 mc-vumc-sit7_c2 with dissolve
    play voice3 vumc_thinking_mmm1 noloop
    vumc "Were you at any point coerced, defrauded, or manipulated by the app?"
    if is_antagonist_mode is False:
        menu:
            "Tell about Fetish Locator's wrongdoings"(hint="d21s03m02c01") if True:
                $ d21s03_statement_2 = True

                scene d21s03-19 mc-vumc-sit10_c1 with dissolve
                play voice2 mc_arrogant_nah1 noloop
                mc "Well... I'm not sure. There was this \"VIP Fetish Challenge Program\" thing."
                play sound sfx_keyboard_typing1
                scene d21s03-22 mc-vumc-desk2_c2 with dissolve
                play voice3 vumc_thinking_oh2 noloop
                vumc "Interesting. What was this program? How did you get into it?"
                scene d21s03-22 mc-vumc-desk2_c1 with dissolve
                play voice2 mc_disappointed_off1 noloop
                mc "After the party I wanted to delete the app, but I couldn't."
                mc "I got this message saying that I got entered into some program—"
                scene d21s03-25 mc-vumc-desk5_c2 with dissolve
                play voice3 vumc_thinking_hm2 noloop
                vumc "The VIP Fetish Challenge Program?"
                scene d21s03-25 mc-vumc-desk5_c1 with dissolve
                play voice2 d9s2_ugu noloop volume 2.0
                mc "Yes. And that I could win a million bucks if I continued to play its little games."
                scene d21s03-24 mc-vumc-desk4_c2 with dissolve
                play voice3 vumc_thinking_hmm5 noloop
                vumc "Such as?"
                scene d21s03-24 mc-vumc-desk4_c1 with dissolve
                play voice2 mc_happy_a1 noloop
                mc "Well, they mostly involved doing some sort of fetishy thing to stay in the game. The more fetishy, the better."
                scene d21s03-25 mc-vumc-desk5_c2 with dissolve
                play voice3 vumc_surprised_ohh3 noloop
                vumc "Is this related to the 20 people challenge?"
                scene d21s03-25 mc-vumc-desk5_c1 with dissolve
                play voice2 mc_yes_yeah7 noloop
                mc "Yes, it's— Wait, how do you know about that?"
                stop sound fadeout 1.0
                scene d21s03-26 mc-vumc-desk6_c2 with dissolve
                play voice3 vumc_angry_cough3 noloop
                vumc "You aren't the first person we talked to about this, Mr. Young."
            "Don't mention it"(hint="d21s03m02c02") if True:

                scene d21s03-19 mc-vumc-sit10_c1 with dissolve
                play voice2 mc_no_nono1 noloop
                mc "No. Not really."
                play sound sfx_keyboard_typing1
                scene d21s03-22 mc-vumc-desk2_c2 with dissolve
                play voice3 vumc_arrogant_huh2 noloop
                vumc "Are you sure?"
                scene d21s03-22 mc-vumc-desk2_c1 with dissolve
                play voice2 d9s2_mcyes2 noloop volume 2.3
                mc "...Yes."
                stop sound fadeout 1.0
    elif True:
        menu:
            "Tell about Fetish Locator's wrongdoings"(hint="d21s03m03c01") if True:
                $ d21s03_statement_2 = True

                scene d21s03-19 mc-vumc-sit10_c1 with dissolve
                play voice2 d1s5b_ehhh noloop
                mc "I... Yes."
                scene d21s03-22 mc-vumc-desk2_c2 with dissolve
                play sound sfx_keyboard_typing1
                play voice3 vumc_disappointed_mff noloop
                vumc "Please, go on. This is invaluable information to solving this case."
                scene d21s03-22 mc-vumc-desk2_c1 with dissolve
                play voice2 mc_arrogant_nah1 noloop
                mc "After the party... I wanted to delete the app. But I couldn't."
                mc "I got this message saying that I got entered into some \"Retention Program.\""
                mc "It said that I had to keep playing its little games if I didn't want my photos leaked."
                scene d21s03-24 mc-vumc-desk4_c2 with dissolve
                play voice3 vumc_surprised_huh1 noloop
                vumc "What type of requests did it make from you?"
                scene d21s03-24 mc-vumc-desk4_c1 with dissolve
                play voice2 mc_happy_a1 noloop
                mc "Well, they mostly involved doing some sort of fetishy thing to stay in the game. The more fetishy, the better."
                scene d21s03-25 mc-vumc-desk5_c2 with dissolve
                play voice3 vumc_surprised_ohh3 noloop
                vumc "Is this related to the 20 people challenge?"
                scene d21s03-25 mc-vumc-desk5_c1 with dissolve
                play voice2 mc_yes_yeah7 noloop
                mc "Yes, it's— Wait, how do you know about that?"
                stop sound fadeout 1.0
                scene d21s03-26 mc-vumc-desk6_c2 with dissolve
                play voice3 vumc_angry_cough3 noloop
                vumc "You aren't the first person we talked to about this, Mr. Young."
            "Don't mention it"(hint="d21s03m03c02") if True:

                scene d21s03-19 mc-vumc-sit10_c1 with dissolve
                play voice2 mc_no_nono1 noloop
                mc "No. Not really."
                play sound sfx_keyboard_typing1
                scene d21s03-22 mc-vumc-desk2_c2 with dissolve
                play voice3 vumc_arrogant_huh2 noloop
                vumc "Are you sure?"
                scene d21s03-22 mc-vumc-desk2_c1 with dissolve
                play voice2 d9s2_mcyes2 noloop volume 2.3
                mc "...Yes."
                stop sound fadeout 1.0

    play sound sfx_heels_steps1
    scene d21s03-27 mc-vumc-desk7_c2 with dissolve
    pause
    stop sound fadeout 1.0
    scene d21s03-27 mc-vumc-desk7_c1 with dissolve
    play voice4 girl8_hey_tired noloop
    pm "Heya."
    play sound sfx_paper_slide1
    play sound3 sfx_cup_place1 noloop
    scene d21s03-28 mc-vumc-desk8_c2 with dissolve
    play voice3 vumc_hey_sexy3 noloop
    vumc "Thanks."
    scene d21s03-28 mc-vumc-desk8_c1 with dissolve
    play voice4 girl8_disappointed_oof2 noloop
    pm "Black, no sugar. I dunno why you like to torture yourself so much."
    play voice3 vumc_happy_relief4 noloop
    vumc "I like the caffeine, but I don't want the diabetes. Is that such a crime?"
    scene d21s03-29 mc-vumc-pm-talk2_c2 with dissolve
    play voice4 girl8_surprised_huh2 noloop
    pm "Oh, hi."
    pm "You must be the 20-girls-guy?"
    scene d21s03-29 mc-vumc-pm-talk2_c1 with dissolve
    play voice2 mc_surprised_wow1 noloop
    mc "Wow, does everybody know about that?"
    scene d21s03-30 mc-vumc-pm-talk3_c2 with dissolve
    play voice4 girl8_arrogant_huh1 noloop
    pm "Sorry. I didn't mean to make light of it. But it {i}is{/i} an impressive number."
    if fl_w2_sex_count == 19:
        scene d21s03-30 mc-vumc-pm-talk3_c1 with dissolve
        play voice2 mc_thinking_emm1 noloop
        mc "I'm still mad about that, to be honest."
        mc "I busted ass trying to win, but lost on a technicality."
        if cage_ntr is True:
            scene d21s03-32 mc-vumc-pm-end1_c1 with dissolve
            play voice2 mc_arrogant_hm3 noloop
            mc "I guess that was another way for her to control me."
    elif True:
        scene d21s03-31 mc-vumc-pm-talk4_c1 with dissolve
        play voice2 mc_thinking_emm1 noloop
        mc "Well, it wasn't actually 20 people. I only got [fl_w2_sex_count]."
        play voice3 girl8_thinking_mmm2 noloop
        pm "That's still pretty impressive, I say."
    scene d21s03-32 mc-vumc-pm-end1_c2 with dissolve
    play voice4 girl8_disappointed_eeh1 noloop
    pm "Reminds me of his undercover days."
    play voice3 vumc_hey_arrogant noloop
    vumc "Hey! I did what I had to. The case was solved, wasn't it?"
    play sound sfx_heels_steps1
    scene d21s03-33 mc-vumc-pm-end2_c1 with dissolve
    play voice4 girl8_no_uhuh2 noloop
    pm "*Chuckles* Uh-huh. Keep telling yourself that, Matthew."
    stop sound fadeout 2.5
    scene d21s03-33 mc-vumc-pm-end2_c3 with dissolve
    play voice2 d1s2_hmm noloop volume 1.8
    mc "What was that about?"
    scene d21s03-33 mc-vumc-pm-end2_c2 with dissolve
    play voice3 vumc_happy_laugh4 noloop
    vumc "*Chuckles* Old memories."
    vumc "Anyway. I think we're good here at this point."
    vumc "Let me finish writing this up and then you can go."

    stop music fadeout 3.0
    jump d21s04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
