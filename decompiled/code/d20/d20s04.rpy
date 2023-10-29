label d20s04:

    $ d20s04_tl_vote = False
    $ d20s04_rn_vote = False
    $ d20s04_zw_vote = False
    $ d20s04_rn_answer = None
    $ d20s04_rn_correct = False
    $ d20s04_zw_q1_answer = None
    $ d20s04_zw_q2_answer = None
    $ d20s04_zw_q3_answer = None
    $ d20s04_zw_q4_answer = None
    $ d20s04_zw_q4_lie = False
    $ d20s04_votes = 0
    $ d20s04_pass_exam = False

    $ nordin_required_points = 6

    scene black
    show screen scene_transistion(_("Some time later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.7, 1.5, "sound2")
    play sound2 sfx_university_ambience fadein 3.0
    scene d20s04-01 mc-looking-at-phone
    with Fade(0.5, 0.5, 0.9)

    $ renpy.music.set_volume(0.2, 1.5, "music")
    if date_pw is True:
        play voice2 mc_thinking_hmm5 noloop
        mct "I got a recent message from Nora. Looks like she's still online."
        mct "\"Need to see you asap. Polly@Coffee Shop w/me. <3 Nora\"."
        scene d20s04-02 mc-looking-at-phone with dissolve
        mct "That sounds urgent. I better text her back."
        play sound sfx_message_out1
        mct "\"RU Okay? I'm about to take my final exams. Can it wait until after that?\""
        play sound sfx_message_in1
        mct "Cool, she says it can wait. They'll be there all day."
        scene d20s04-06 mc-smiling with dissolve
        play voice2 mc_angry_huh2 noloop
        mct "I hope she's not pregnant."
        mct "Shit. This is just what I need before exams."
        if date_op is True:
            call buzz from _call_buzz_41

    if date_op is True:
        play voice2 mc_arrogant_huh1 noloop
        mct "Oliver?"
        scene d20s04-03 mc-phonecall with dissolve
        play voice2 mc_thinking_hmm1 noloop
        mc "Hello? Oliver?"
        play voice3 oliver_phonetalk_hello noloop
        op "Hey, hi, [mcname]! Uhm, I'm not bothering you, am I?"
        play voice2 mc_no_uhuh1 noloop
        mc "No, it's alright. What's up?"
        op "Uh, do you remember when I, uhm, asked if you were free this week?"
        scene d20s04-04 mc-phonecall with dissolve
        play voice2 mc_thinking_oh1 noloop
        mc "Oh, {i}oh{/i}."
        play voice3 oliver_phonetalk_oh noloop
        op "It's alright if you don't remember, I know you're busy—"
        play voice2 mc_angry_cough1 noloop
        mc "Oliver, calm down. I remember. Are you calling to ask if I'm free today?"
        play voice3 oliver_phonetalk_yes noloop
        op "...Yes."
        scene d20s04-05 mc-phonecall with dissolve
        play voice2 d4s4_mclaugh noloop
        mc "*Chuckles* You don't have to be nervous around me. I don't bite."
        mc "Anyway. I have a couple things going on today, but I should be free in around a couple hours."
        mc "How does that sound?"
        scene d20s04-03 mc-phonecall with dissolve
        play voice3 oliver_phonetalk_mmm noloop
        op "That sounds great! I was thinking we could go watch a movie, or uh, something like that."
        play voice2 d3s11b_mcheh noloop
        mc "*Chuckles* A movie sounds great, Oliver. How about I call you when I'm free then?"
        op "Yes. Just let me know when you're free, and I'll come pick you up."
        scene d20s04-04 mc-phonecall with dissolve
        play voice2 mc_yes_aga2 noloop
        mc "Great. Talk to you then."
        play voice3 oliver_phonetalk_huh noloop
        op "Bye. I, uh, can't wait."
        mc "Me neither."
        scene d20s04-07 mc-talking with dissolve
        play voice2 mc_thinking_mmm3 noloop
        mct "He's cute. It'll be nice to unwind with him after the exams."

    if date_pw is False and date_op is False:
        play voice2 mc_thinking_hmm5 noloop
        mct "It is time. Let's get this over with."

    stop music fadeout 3.0
    stop sound2 fadeout 3.0
    play sound sfx_door_closed2
    scene d20s04-08 mc-rn-tl-zw-talking with Fade(0.3, 0.3, 0.3)
    pause
    queue music music_battledrums_exam
    scene d20s04-09 rn-talking with dissolve
    play voice3 pete_thinking_hmm1 noloop
    rn "Good afternoon, Mister [mcname] Young."
    $ renpy.music.set_volume(0.8, 4.0, "music")
    rn "As I'm sure you are aware, we are gathered together today for your Final Examination."
    rn "As you know, my name is Professor Ronald Nordin. I am joined by two other judges to determine whether you deserve to pass this semester."
    scene d20s04-10 tl-talking with dissolve
    $ renpy.music.set_volume(1.0, 4.5, "sound2")
    play voice4 teresa_hey_calm noloop
    tl "My name is Professor Theresa Lewald."
    scene d20s04-11 zw-talking with dissolve
    play voice3 chloe_disappointed_ehh2 noloop
    zw "You know me.{w} Zarah Waller. Not a professor."
    scene d20s04-12 mc-talking with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "It's a pleasure to-"
    scene d20s04-09 rn-talking with dissolve
    play voice2 pete_yes_simple1 noloop
    rn "Yes, I'm sure it is.{w} Theresa, please get us started."

    jump d20s04_tl

label d20s04_tl:

    scene d20s04-13 mc-tl-zw-talking with dissolve
    if d20s02tl_vote is True:
        $ d20s04_tl_vote = True
        play voice3 teresa_thinking_hmm2 noloop
        tl "Until I learned I was going to be evaluating this young man, I was not familiar with him."
        tl "However, since then I have become quite familiar with Mr. Young."
        scene d20s04-15 tl-talking with dissolve
        play voice3 teresa_thinking_hmm3 noloop
        tl "He is talented, authoritative, well versed, and the perfect example of what our students should strive to become."
        tl "I have no further questions. He has my vote."
    elif True:

        play voice3 teresa_happy_laugh6 noloop
        tl "Well, I suggest you get comfortable, Mister Young, because we're going to be here a while."
        scene d20s04-16 mc-rn-tl-talking with dissolve
        play voice2 mc_arrogant_huh3 noloop
        mc "Am I permitted to take any other position than standing upright here?"
        scene d20s04-17 mc-rn-talking with dissolve
        play voice4 pete_no_simple3 noloop volume 0.5
        rn "No."
        play voice2 d2s9_confused noloop
        mc "Well, then I guess I'm as comfortable as possible."
        scene d20s04-15 tl-talking with dissolve
        play voice3 teresa_thinking_hmm3 noloop
        tl "Very well, let's start with Question #1."
        tl "In the words of Thomas Bacon..."
        scene black
        show screen scene_transistion(_("One eighth of an eternity later"))
        with Fade(0.4, 0.4, 0.4)
        pause
        hide screen scene_transistion
        scene d20s04-20 tl-talking
        with Fade(0.4, 0.4, 0.4)
        play voice3 teresa_disappointed_ohh1 noloop
        tl "...symphonies number two and three are spurious at best. And of course, thirty-seven is extremely unlikely."
        scene d20s04-19 mc-talking with dissolve
        play voice2 d1s5b_ehhh noloop
        mc "I'm sorry, what was the question?"
        scene d20s04-18 tl-zw-talking with dissolve
        play voice3 teresa_disappointed_mph noloop
        tl "In 1788, Mozart wrote three symphonies that might be considered his last symphony. Please name one of them."
        scene d20s04-24 mc-talking with dissolve
        play voice2 mc_arrogant_nah1 noloop
        mc "I'm sure I've said this before, but I'm a business management major. I haven't taken any courses in music history."
        scene d20s04-22 tl-zw-talking with dissolve
        play voice3 teresa_arrogant_hmm noloop
        tl "And I'm sure I've said this before, but I don't care. Answer the damn question."
        scene d20s04-14 rn-tl-zw-talking with dissolve
        play voice4 pete_hey_attention noloop
        rn "Language."
        play voice3 teresa_arrogant_heh noloop
        tl "Cheerfully withdrawn."
        scene d20s04-25 tl-talking with dissolve
        tl "Answer the question."
        scene d20s04-23 mc-thinking with dissolve
        play voice2 d14s16_smell noloop
        mct "Okay, I've got three possible answers. Yet I know nothing about symphonies. Everything I know about Mozart was from that movie."
        mct "Fuck it. Let's take a guess."
        scene d20s04-24 mc-talking with dissolve
        play voice2 mc_thinking_hmm4 noloop
        mc "Così fan tutte."
        scene d20s04-26 tl-talking with dissolve
        play voice3 teresa_thinking_oh noloop
        tl "I assume you are referring to \"Così fan tutte, ossia La scuola degli amanti\"?"
        scene d20s04-12 mc-talking with dissolve
        play voice2 d2s12_emmm noloop
        mc "Uhh... of course. What else could I be referring to?"
        scene d20s04-25 tl-talking with dissolve
        play voice3 teresa_thinking_hmm1 noloop
        tl "The sex comedy film by Tinto Brass."
        scene d20s04-24 mc-talking with dissolve
        play voice2 mc_happy_a1 noloop
        mc "1992, All Ladies Do It?"
        scene d20s04-20 tl-talking with dissolve
        play voice3 teresa_disappointed_ehh1 noloop
        tl "I see that you are familiar with both."
        play voice2 mc_yes_yeah7 noloop
        mc "Umm... yes?"
        tl "Either way, your answer is incorrect{w}, but I will grant you one-half point for obscure knowledge."
        scene d20s04-19 mc-talking with dissolve
        play voice2 mc_arrogant_hm2 noloop
        mc "Is that the last of the questions?"
        scene d20s04-18 tl-zw-talking with dissolve
        play voice3 teresa_yes_yeah1 noloop
        tl "That was the last of my questions, but you might wish you had more to choose from."
        scene d20s04-46 mc-talking with dissolve
        play voice2 d1s1_mmm noloop
        mct "I can't imagine why.{w} Musicals, philosophers, and just plain nonsense..."
        scene d20s04-10 tl-talking with dissolve
        play voice3 teresa_thinking_mmm noloop
        tl "I'm sorry, but you failed my portion of the exam."
        scene d20s04-41 mc-talking with dissolve
        play voice2 mc_arrogant_hm3 noloop
        mc "Was it close?"
        play voice3 teresa_no_simple2 noloop
        tl "No."
        mc "Oh."

        jump d20s04_rn

label d20s04_rn:

    scene d20s04-27 rn-talking with dissolve
    play voice4 pete_thinking_hmm3 noloop
    rn "I have been teaching this particular student for the duration of this semester."
    if d19s07_mk_nordin is True:
        $ d20s04_rn_vote = True
        rn "And despite disappearing for weeks at a time, and distracting other students during my classes..."
        scene d20s04-31 rn-talking with dissolve
        play voice4 pete_arrogant_heh3 noloop
        rn "He has proven himself as someone who is capable of achieving the impossible."
        rn "He has my vote. No further questions."

        jump d20s04_zw
    elif True:

        rn "And he's disappeared for weeks at a time and barely paid attention - preferring to talk and distract other students."
        scene d20s04-31 rn-talking with dissolve
        play voice4 pete_disappointed_mmf1 noloop
        rn "To that end, I have a very special examination prepared for him.{w} Two hundred questions on everything he should know."
        scene d20s04-30 mc-thinking with dissolve
        play voice2 mc_pain_mff3 noloop
        mct "Oh, fuck."
        scene d20s04-32 rn-talking with dissolve
        play voice4 pete_happy_laugh3 noloop
        rn "Let's begin..."

        jump d20s04_rn_qa

label d20s04_rn_qa:

    scene black
    show screen scene_transistion(_("199 questions later"))
    with Fade(0.4, 0.4, 0.4)
    pause
    hide screen scene_transistion
    scene d20s04-27 rn-talking
    with Fade(0.4, 0.4, 0.4)
    play voice4 pete_happy_mmm2 noloop
    rn "Last one. Make it count."
    rn "Who famously wrote, \"Death may beget life, but oppression can beget nothing other than itself\"?"
    scene d20s04-33 mc-tired with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I don't-{w} I'm so exhausted..."
    scene d20s04-31 rn-talking with dissolve
    play voice4 pete_happy_relief1 noloop
    rn "I'll make it easier for you, they also wrote, \"There is prodigious strength in sorrow and despair.\" and we covered them during the weeks you skipped my classes."
    play voice2 mc_yes_yeah3 noloop
    mc "I was sick."
    play voice4 pete_yes_ugu1 noloop
    rn "Surely, you took the opportunity to review someone else's notes, or watch the classes you missed on the internets."
    scene d20s04-30 mc-thinking with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "Fuck me.{w} I'm so exhausted he could quote my mother and I wouldn't recognize it."
    mct "I've got to come up with something to tell him."
    menu:
        "Edwin Le Chiffre"(hint="d20s04m01c01") if True:
            $ d20s04_rn_answer = 1
        "Jean Rene Mathis"(hint="d20s04m01c02") if True:

            $ d20s04_rn_answer = 2
        "Vladimer Dmitrovich Zukovsky"(hint="d20s04m01c03") if True:

            $ d20s04_rn_answer = 3
        "Charles Dickens?"(hint="d20s04m01c04") if True:

            $ d20s04_rn_answer = 4
            $ d20s04_rn_correct = True
            $ study_points += 1

            scene d20s04-29 rn-talking with dissolve
            play voice4 pete_disgust_meh2 noloop
            rn "Well, I'm not surprised."

    if d20s04_rn_correct is False:
        scene d20s04-29 rn-talking with dissolve
    if study_points >= nordin_required_points:
        $ d20s04_rn_vote = True
        rn "You passed my portion of the final exam.{w} Barely."
        rn "I guess you were paying some attention after all."
        scene d20s04-32 rn-talking with dissolve
        play voice4 pete_disappointed_ehh4 noloop
        rn "Mister Young has my vote."
    elif True:
        rn "That was pathetic."
        rn "I expect better from even my worst students."
        scene d20s04-32 rn-talking with dissolve
        play voice4 pete_disappointed_ehh4 noloop
        rn "Mister Young does NOT have my vote."

    jump d20s04_zw

label d20s04_zw:

    if d20s02zw_influenced is True:
        $ d20s04_zw_vote = True
        scene d20s04-37 zw-talking with dissolve
        play voice3 chloe_disappointed_ehh7 noloop
        zw "After some deep soul-searching and consideration of this young man's qualities..."
        zw "I have reluctantly determined that he has my vote."
        zw "In my opinion, [mcname] Young deserves a pass for this semester."

        jump d20s04_results
    elif True:

        scene d20s04-40 zw-talking with dissolve
        play voice3 chloe_arrogant_heh1 noloop
        zw "I've been looking forward to this, [mcname] Young."
        zw "It would be perfectly acceptable - and delightful - to simply reject you outright."
        zw "After all, you have been a constant pain in my neck all semester."
        scene d20s04-37 zw-talking with dissolve
        play voice3 chloe_disappointed_ehh7 noloop
        zw "However, I'm going to give you a chance."
        zw "I've prepared a short list of questions. If you answer all of them correctly, you get my vote."
        scene d20s04-43 zw-talking with dissolve
        play voice3 chloe_happy_hmm noloop
        zw "If you miss even one, then...{w} No vote for you."
        zw "Are you prepared?"
        scene d20s04-41 mc-talking with dissolve
        play voice2 mc_arrogant_hm1 noloop
        mc "Do I have a choice?"
        scene d20s04-40 zw-talking with dissolve
        play voice3 chloe_no_nouh2 noloop
        zw "I don't want to hear any whining about \"I was tired\" or \"It wasn't my fault\" when you fail."
        play voice2 mc_yes_ugu1 noloop
        mc "Whatever. Let's just get this over with."

        jump d20s04_zw_qa

label d20s04_zw_qa:

    scene d20s04-40 zw-talking with dissolve
    play voice3 chloe_yes_aga2 noloop
    zw "Good enough.{w} Question 1."
    zw "Sun Tzu famously wrote, \"The Art of War\". In that book, what is the supreme art of war?"
    menu:
        "Who shot who in the what now?"(hint="d20s04m02c01") if True:
            $ d20s04_zw_q1_answer = 1
            jump d20s04_zw_wrong
        "Subdue the enemy without fighting"(hint="d20s04m02c02") if True:

            $ d20s04_zw_q1_answer = 2
            scene d20s04-43 zw-talking with dissolve
            play voice3 chloe_yes_simple noloop
            zw "That is acceptable."
        "Overpowering a vastly superior enemy"(hint="d20s04m02c03") if True:

            $ d20s04_zw_q1_answer = 3
            jump d20s04_zw_wrong
        "Achieving perfect certainty in your impending victory"(hint="d20s04m02c04") if True:

            $ d20s04_zw_q1_answer = 4
            jump d20s04_zw_wrong

    if d20s04_zw_q1_answer != 2:
        scene d20s04-43 zw-talking with dissolve
    zw "Question 2."
    zw "Adam Smith is best known for \"the invisible hand of the market.\" Please finish the following quote, \"Wherever there is great property\"..."
    scene d20s04-42 mc-talking with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "That's easy.{w} Oh fuck!"
    mct "I know this. Why is my mind completely blank?"
    mct "Think brain think!!!"
    menu:
        "... there is tremendous wealth."(hint="d20s04m03c01") if True:
            $ d20s04_zw_q2_answer = 1
            jump d20s04_zw_wrong
        "... there is financial security."(hint="d20s04m03c02") if True:

            $ d20s04_zw_q2_answer = 2
            jump d20s04_zw_wrong
        "... there are huge tracts of land."(hint="d20s04m03c03") if True:

            $ d20s04_zw_q2_answer = 3
            jump d20s04_zw_wrong
        "... there is great inequality."(hint="d20s04m03c04") if True:

            $ d20s04_zw_q2_answer = 4
            scene d20s04-37 zw-talking with dissolve
            play voice3 chloe_yes_yeah1 noloop
            zw "That is acceptable."

    if d20s04_zw_q2_answer != 4:
        scene d20s04-37 zw-talking with dissolve
    zw "Question 3."
    zw "What book is the following quote from: \"If you want loyalty, hire a cocker spaniel\"?"
    menu:
        "The Snowball: Warren Buffett and the Business of Life"(hint="d20s04m04c01") if True:
            $ d20s04_zw_q3_answer = 1
            jump d20s04_zw_wrong
        "Liar's Poker"(hint="d20s04m04c02") if True:

            $ d20s04_zw_q3_answer = 2
            scene d20s04-11 zw-talking with dissolve
            play voice3 chloe_surprised_oh noloop
            zw "That is acceptable."
        "The Last Boy Scout"(hint="d20s04m04c03") if True:

            $ d20s04_zw_q3_answer = 3
            jump d20s04_zw_wrong
        "Yellow Bicycles Radish Greenly"(hint="d20s04m04c04") if True:

            $ d20s04_zw_q3_answer = 4
            scene d20s04-43 zw-talking with dissolve
            play voice3 chloe_surprised_what noloop
            zw "What?!"
            play voice2 d1s5b_emmm noloop
            scene d20s04-41 mc-talking with dissolve
            mc "Um, I mean...{w} \"Reminiscences of a Stock Operator\"?"

            jump d20s04_zw_wrong

    if d20s04_zw_q3_answer != 2:
        scene d20s04-11 zw-talking with dissolve
    zw "Question 4..."
    scene black
    show screen scene_transistion(_("An eternity later..."))
    with Fade(0.4, 0.4, 0.4)
    pause
    hide screen scene_transistion
    scene d20s04-44 rn-tl-zw-talking
    with Fade(0.4, 0.4, 0.4)
    play voice4 pete_angry_argh2 noloop
    rn "Miss Wallace, are we going to be here all day with this?"
    scene d20s04-45 rn-tl-zw-talking with dissolve
    play voice3 chloe_disappointed_ehh3 noloop
    zw "Waller.{w} My name is Zarah Waller."
    play voice4 teresa_yes_yeah2 noloop
    tl "I have to agree with my fellow professor. This has gone on long enough."
    scene d20s04-44 rn-tl-zw-talking with dissolve
    play voice3 pete_angry_hmm5 noloop
    rn "He's correctly answered all of your questions.{w} I'm not easily impressed, but apparently he knows enough."
    scene d20s04-45 rn-tl-zw-talking with dissolve
    play voice4 teresa_yes_ugu noloop
    tl "Indeed. I didn't even know some of the answers to those questions."
    play voice3 chloe_disappointed_ehh4 noloop
    zw "I suppose.{w}.. Fine."
    scene d20s04-43 zw-talking with dissolve
    play voice3 chloe_arrogant_okay noloop
    zw "Reluctantly, you have my vote."

    $ d20s04_zw_vote = True

    jump d20s04_results

label d20s04_zw_wrong:

    play voice3 chloe_disappointed_off noloop
    zw "Next Question."
    zw "Three weeks ago, I saw a tattooed whore leaving your dorm room. What was she doing there?"
    if d20s04_rn_vote is True:
        play voice4 pete_angry_cough1 noloop
        rn "I must object!"
    elif d20s04_tl_vote is True:
        play voice4 teresa_happy_relief1 noloop
        tl "I must object!"
    elif True:
        play voice2 mc_surprised_what3 noloop
        mc "What?! How is that even a question?!"
    scene d20s04-28 rn-tl-zw-talking with dissolve
    play voice4 pete_angry_hmm2 noloop
    rn "Miss Wallace, I strenuously suggest that you keep these questions to academic facts."
    scene d20s04-38 mc-rn-tl-zw-talking with dissolve
    play voice3 chloe_angry_cough noloop
    zw "Waller.{w} My name is Zarah Waller."
    scene d20s04-36 rn-tl-zw-talking with dissolve
    play voice4 pete_yes_yeah noloop
    rn "Noted.{w} Do I make myself clear?"
    scene d20s04-38 mc-rn-tl-zw-talking with dissolve
    play voice3 chloe_arrogant_heh4 noloop
    zw "According to the rules-"
    scene d20s04-47 tl-talking with dissolve
    play voice4 teresa_no_nah2 noloop
    tl "The question really isn't appropriate."
    scene d20s04-39 zw-talking with dissolve
    play voice3 chloe_disappointed_ehh1 noloop
    zw "We can ask whatever we want."
    scene d20s04-44 rn-tl-zw-talking with dissolve
    play voice4 pete_yes_simple3 noloop
    rn "Technically, you are correct.{w} In reality-"
    scene d20s04-45 rn-tl-zw-talking with dissolve
    play voice3 teresa_disappointed_ohh2 noloop
    tl "In reality we could have you thrown off this panel and have your employment at the college re-evaluated."
    scene d20s04-46 mc-talking with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "Woah.{w} Zarah really fucked up asking me that question."
    scene d20s04-39 zw-talking with dissolve
    play voice3 chloe_arrogant_yeah1 noloop
    zw "I'll compromise.{w} Let this question stand, and I'll forgo the other questions I have written here."
    scene d20s04-21 rn-tl-zw-talking with dissolve
    play voice4 pete_thinking_hmm6 noloop
    rn "Hmm.{w} Theresa, what do you think?"
    scene d20s04-14 rn-tl-zw-talking with dissolve
    play voice3 teresa_thinking_emm1 noloop
    tl "I do kinda want to hear [mcname]'s answer, even though it is inappropriate to ask."
    scene d20s04-21 rn-tl-zw-talking with dissolve
    play voice4 pete_thinking_mmf noloop
    rn "We have no way of verifying whether he tells us the truth or not."
    scene d20s04-38 mc-rn-tl-zw-talking with dissolve
    play voice3 chloe_yes_happy noloop
    zw "Leave that to me."
    scene d20s04-28 rn-tl-zw-talking with dissolve
    play voice4 pete_surprised_ah noloop
    rn "It is highly unorthodox...{w} but I'll allow it."
    scene d20s04-41 mc-talking with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "What does that mean?"
    scene d20s04-32 rn-talking with dissolve
    play voice4 pete_angry_hmm1 noloop
    rn "It depends on his answer."
    scene d20s04-47 tl-talking with dissolve
    play voice3 teresa_hey_happy noloop
    tl "The three of us will judge whether you are telling the truth. Not just Zarah."
    scene d20s04-43 zw-talking with dissolve
    play voice4 chloe_yes_yeah3 noloop
    zw "Fine.{w} Do you need me to repeat the question, [mcname]?"
    play voice2 mc_thinking_mmm5 noloop
    mc "I think I can remember it."
    zw "Three weeks ago, I saw a tattooed whore leaving your dorm room. What had she been doing there?"
    scene d20s04-41 mc-talking with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "I said that I could remember it."
    mc "*sigh*"
    mc "Fine. I suppose I have no choice."
    menu:
        "Seduced and distracted my roommate"(hint="d20s04m05c01") if True:
            $ d20s04_zw_q4_answer = 1
            scene d20s04-24 mc-talking with dissolve
            play voice2 mc_arrogant_heh3 noloop
            mc "At the time, I didn't know.{w} I was surprised to see her that morning."
            play voice3 chloe_disappointed_ehh5 noloop
            zw "That's it?"
            play voice2 mc_no_no1 noloop
            mc "No. Since then, I learned that she had seduced and distracted my roommate while trying to get information out of him."
        "Journalist investigating an app"(hint="d20s04m05c02") if True:

            $ d20s04_zw_q4_answer = 2
            scene d20s04-24 mc-talking with dissolve
            play voice2 d1s5_mchappy noloop volume 1.6
            mc "As far as I know, she is a journalism major here. At least that's what she told me."
            mc "She was investigating some new app and believed she could get information from my roommate."
        "She was just visiting."(hint="d20s04m05c03") if True:

            $ d20s04_zw_q4_answer = 3
            $ d20s04_zw_q4_lie = True
            scene d20s04-24 mc-talking with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "Um, nothing much."
            mc "She came by early that morning because she wanted some notes or something."
            scene d20s04-37 zw-talking with dissolve
            play voice3 chloe_disappointed_ehh5 noloop
            zw "She was carrying her pants in her hands when she left the room."
            scene d20s04-41 mc-talking with dissolve
            play voice2 mc_no_nah2 noloop
            mc "I don't know what to tell you. It didn't have anything to do with me."

    if d20s04_zw_q4_lie is False:
        scene d20s04-43 zw-talking with dissolve
        play voice3 chloe_surprised_huh1 noloop
        zw "Why-?"
        scene d20s04-36 rn-tl-zw-talking with dissolve
        play voice4 pete_angry_cough2 noloop
        rn "I believe you asked your last question, Miss Waller."
        scene d20s04-38 mc-rn-tl-zw-talking with dissolve
        play voice3 chloe_hey_whisper noloop
        zw "But, rules were broken."
        scene d20s04-44 rn-tl-zw-talking with dissolve
        play voice4 pete_angry_hmm6 noloop
        rn "This is not an investigation. It is an exam."
        scene d20s04-45 rn-tl-zw-talking with dissolve
        play voice3 teresa_yes_ugu noloop
        tl "I believe his response was truthful."
        scene d20s04-44 rn-tl-zw-talking with dissolve
        play voice4 pete_arrogant_hm2 noloop
        rn "I agree."
        scene d20s04-43 zw-talking with dissolve
        play voice3 chloe_disappointed_oh noloop
        zw "I still don't believe you.{w}"
        zw "You are a liar and do NOT have my vote."
        $ d20s04_zw_vote = False
    elif True:
        scene d20s04-40 zw-talking with dissolve
        play voice3 chloe_no_uhuh noloop
        zw "I don't believe you."
        scene d20s04-32 rn-talking with dissolve
        play voice4 pete_yes_ugu2 noloop
        rn "Agreed. He's lying."
        scene d20s04-20 tl-talking with dissolve
        play voice3 teresa_arrogant_hmm noloop
        tl "It's unanimous."
        scene d20s04-43 zw-talking with dissolve
        play voice4 chloe_happy_yeah4 noloop
        zw "There is no need to continue further. Mr. Young does NOT have my vote."
        $ d20s04_zw_vote = False

    jump d20s04_results

label d20s04_results:

    $ d20s04_votes = d20s04_tl_vote + d20s04_rn_vote + d20s04_zw_vote

    if d20s04_votes == 3:
        $ d20s04_pass_exam = True
        scene d20s04-18 tl-zw-talking with dissolve
        play voice3 teresa_thinking_mmm noloop
        tl "Well, this is a rare treat."
        if d20s02zw_influenced is True:
            scene d20s04-50 zw-talking with dissolve
            play voice4 chloe_happy_yeah1 noloop
            zw "*deadpan* Yaaaaaaaaaaay."
        scene d20s04-27 rn-talking with dissolve
        play voice3 pete_happy_relief1 noloop
        rn "I suppose congratulations are in order, Mister Young."
        scene d20s04-35 mc-rn-talking with dissolve
        play voice2 d1s2_hmm noloop volume 1.6
        mc "You mean, I passed?"
        scene d20s04-25 tl-talking with dissolve
        play voice4 teresa_thinking_oh noloop
        tl "You didn't just pass. You got all three votes."



        scene d20s04-32 rn-talking with dissolve
        play voice3 pete_thinking_hmm7 noloop
        rn "That doesn't happen as often as you would think."



        scene d20s04-16 mc-rn-tl-talking with dissolve
        play voice2 mc_happy_wow2 noloop
        mc "Wow! Thanks."

        scene d20s04-31 rn-talking with dissolve
        play voice4 pete_thinking_hmm10 noloop
        rn "Take this win and do something with it."

        scene d20s04-37 zw-talking with dissolve
        play voice3 chloe_surprised_huh3 noloop
        zw "What can he?..."



















        scene d20s04-20 tl-talking with dissolve
        play voice3 teresa_thinking_hmm1 noloop
        tl "You have a tremendous opportunity ahead of you."
        scene d20s04-12 mc-talking with dissolve
        play voice2 mc_arrogant_hm1 noloop
        mc "I'm not following..."
        scene d20s04-09 rn-talking with dissolve
        play voice4 pete_happy_mmm1 noloop
        rn "With your skill-set and ability to think outside the box - I recommend that you consider another option."
        play voice2 mc_yes_yeah8 noloop
        mc "What is that?"
        rn "Start a business. Do what you love. And write your next semesters course work about that."
        scene d20s04-23 mc-thinking with dissolve
        play voice2 d1s5_mcthinks noloop
        mct "Now there's an idea..."
        scene d20s04-14 rn-tl-zw-talking with dissolve
        play voice3 teresa_yes_aga noloop
        tl "I agree with Ron-"
        scene d20s04-10 tl-talking with dissolve
        tl "That is, I agree with Professor Nordin's recommendation.{w} Do what you love."
        scene d20s04-49 mc-talking with dissolve
        play voice2 mc_hey_hey5 noloop
        mc "I'll seriously consider what you've said."

        $ fl_achievement_unlock("d20s04n01")
        $ unlock_gallery_slot("extra", "d20s04n01")

        scene d20s04-11 zw-talking with dissolve
        play voice4 chloe_happy_hmm noloop
        zw "Before you leave, may I give you some advice as well?"
        play voice2 mc_yes_sure1 noloop
        mc "Sure, why not?"
        play voice4 chloe_disappointed_off noloop
        zw "Don't be an asshole."
        scene d20s04-41 mc-talking with dissolve
        play voice2 mc_disappointed_ah2 noloop
        mc "*sigh* Thanks."

    elif d20s04_votes == 2:
        $ d20s04_pass_exam = True
        scene d20s04-25 tl-talking with dissolve
        play voice3 teresa_thinking_hmm2 noloop
        tl "Congratulations, [mcname] Young."
        scene d20s04-27 rn-talking with dissolve
        play voice4 pete_arrogant_laugh noloop
        rn "You have passed this semester."
        scene d20s04-26 tl-talking with dissolve
        play voice3 teresa_thinking_hmm1 noloop
        tl "You may move on to your next semester in the Autumn."
        scene d20s04-49 mc-talking with dissolve
        play voice2 mc_happy_oof1 noloop
        mct "*Whew*"
        mc "Thank you.{w} Thank you both."
        scene d20s04-32 rn-talking with dissolve
        play voice4 pete_hey_happy noloop
        if d20s04_rn_vote is True:
            rn "No thanks needed. You earned it."
            rn "Don't let anyone tell you otherwise."
        elif True:
            rn "You earned it. Don't let anyone - even me - tell you that you didn't."
            rn "Although you could have worked harder...{w} and been smarter..."

    elif d20s04_votes == 1:
        $ d20s04_pass_exam = False
        scene d20s04-20 tl-talking with dissolve
        play voice4 teresa_disappointed_ehh2 noloop
        tl "I'm afraid.{w} *sigh* This is never easy."
        scene d20s04-34 rn-tl-talking with dissolve
        play voice3 pete_arrogant_heh4 noloop
        rn "Allow me.{w} [mcname] Young you have failed."
        scene d20s04-43 zw-talking with dissolve
        play voice4 chloe_happy_mmm noloop
        zw "You should be used to it. You are a failure."
        scene d20s04-26 tl-talking with dissolve
        play voice3 teresa_thinking_hmm1 noloop
        tl "That's not necessary."
        scene d20s04-32 rn-talking with dissolve
        play voice4 pete_arrogant_heh1 noloop
        rn "If you choose to return next semester, you will have to repeat this semester."
        scene d20s04-41 mc-talking with dissolve
        play voice2 mc_disappointed_ehh4 noloop
        mc "But I can come back, right?"
        scene d20s04-25 tl-talking with dissolve
        play voice3 teresa_yes_simple noloop
        tl "Yes."
        scene d20s04-46 mc-talking with dissolve
        play voice2 mc_thinking_mmm3 noloop
        mct "Well, that sucks donkey ass.{w}.. but, at least I can come back and finish my degree."
    elif True:

        $ d20s04_pass_exam = False
        scene d20s04-43 zw-talking with dissolve
        play voice4 chloe_happy_mmm noloop
        zw "I warned you, [mcname]."
        zw "It is with tremendous pleasure that I get to say this."
        zw "Not only did you fail this semester, but you will NOT be welcome back in future semesters."
        scene d20s04-41 mc-talking with dissolve
        play voice2 mc_surprised_what1 noloop
        mc "What?!"
        scene d20s04-40 zw-talking with dissolve
        play voice4 chloe_disappointed_ehh7 noloop
        zw "May you live long and endure your failure as a college student and as a human being."
        zw "Pack your bags swiftly and get the hell out, because you won't be seeing this place ever again."
        zw "At least not as a student. Maybe someday I will hire you on as a janitor."
        scene d20s04-19 mc-talking with dissolve
        play voice2 mc_angry_huh1 noloop
        mc "I don't understand-"
        scene d20s04-34 rn-tl-talking with dissolve
        play voice3 pete_disappointed_mmf2 noloop
        rn "Like any student, you have until the end of term to remove yourself and your belongings."
        scene d20s04-22 tl-zw-talking with dissolve
        play voice3 teresa_thinking_hmm1 noloop
        tl "However, you will not be allowed back next term."
        scene d20s04-37 zw-talking with dissolve
        play voice4 chloe_arrogant_heh2 noloop
        zw "Goodbye."

    stop music fadeout 3.0
    jump d20s05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
