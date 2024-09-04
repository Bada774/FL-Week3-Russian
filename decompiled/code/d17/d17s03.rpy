label d17s03:

    scene black
    show screen scene_transistion(_("30 minutes later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound2 sfx_university_ambience fadein 3.0
    scene d17s03-01-somewhere-on-vu-campus
    with Fade(0.5, 0.5, 0.9)
    pause
    scene d17s03-02-mc-talk-ir with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Iona."
    scene d17s03-03-ir-talk-mc with dissolve
    $ renpy.music.set_volume(0.7, 3.0, "music")
    queue music acid_jazz
    play voice3 iona_hm2 noloop
    ir "Hey [mcname]. Glad you could make it."
    scene d17s03-04-mc-talk-ir with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Hana texted me that I should meet you here?"
    scene d17s03-05-ir-talk-mc with dissolve
    play voice3 iona_yes2 noloop
    ir "Yup. I'm supposed to take you to her."
    scene d17s03-06-mc-talk-ir with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Oh? Why didn't she just tell me where to meet her?"
    scene d17s03-07-ir-talk-mc with dissolve
    play voice3 iona_hah1 noloop
    ir "Because I know where she is, dumbass."
    scene d17s03-09-ir-talk-mc with dissolve
    ir "She's on her boat. C'mon, let's walk and talk."
    stop sound2 fadeout 4.0
    play sound3 park fadein 3.0
    $ renpy.music.set_volume(0.1, 0.0, "sound4")
    play sound4 distanttraffic fadein 3.0
    scene d17s03-10-mc-ir-start-walking with dissolve
    pause
    scene d17s03-11-mc-talk-ir with dissolve
    play voice2 d1s2_hmm noloop volume 1.3
    mc "Boat? The nearest water I know of-"
    scene d17s03-12-ir-talk-mc with dissolve
    play voice3 dahlia_yes_aga noloop
    ir "Yup. We'll take a bus there.{w} Anyway, there was something I wanted to talk to you about."
    scene d17s03-13-mc-talk-ir with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Actually, there was something I wanted to ask you about as well."
    scene d17s03-14-ir-talk-mc with dissolve
    play voice3 iona_hm1 noloop
    ir "Go ahead."
    scene d17s03-15-mc-talk-ir with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "You're a bartender, right?"
    scene d17s03-16-ir-talk-mc with dissolve
    play voice3 iona_yes1 noloop
    ir "Yup. Going on about a year now."
    scene d17s03-17-mc-talk-ir with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "So, you know how to handle drunks and difficult situations."
    scene d17s03-18-ir-talk-mc with dissolve
    play voice3 iona_laughing1 noloop
    ir "There are three things under the bar if I need them: a shotgun, a fubar, and a phone."
    scene d17s03-19-mc-talk-ir with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What's a fubar?"
    scene d17s03-20-ir-talk-mc with dissolve
    play voice3 iona_ou1 noloop
    ir "It's part tomahawk, part crowbar, part multi-tool. Mostly it's an effective club that can be explained as a utility tool."
    ir "It Fucks stuff Up Beyond All Recognition."
    scene d17s03-21-mc-talk-ir with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay...{w} So why was Hana so concerned about your safety at Min's Party last week?"
    scene d17s03-22-ir-talk-mc with dissolve
    play voice3 iona_geh noloop
    ir "That's actually related to what I wanted to talk to you about."
    scene d17s03-23-mc-talk-ir with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh?"
    scene d17s03-24-ir-talk-mc with dissolve
    play voice3 iona_eeem1 noloop
    ir "I mean, obviously I don't have the usual tools when I tend bar outside the bar."
    scene d17s03-25-mc-talk-ir with dissolve
    play voice2 d4s4_mclaugh noloop
    mc "You still seem quite capable of handling yourself in a sticky situation."
    scene d17s03-26-ir-talk-mc with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop volume 0.6
    ir "Well, I used to be an athlete. I know some martial arts and taught a few self defense classes."
    scene d17s03-27-mc-talk-ir with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "You're an athlete? I don't think I knew that."
    scene d17s03-28-ir-talk-mc with dissolve
    play voice3 iona_mmm1 noloop
    ir "Were, past tense.{w} Back in my younger and stupider days."
    scene d17s03-29-mc-talk-ir with dissolve
    play voice2 d2s9_mchey noloop
    mc "I don't think there's anything stupid about being an athlete."
    scene d17s03-30-ir-talk-mc with dissolve
    play voice3 iona_no1 noloop
    ir "No, there isn't.{w} Anyway, tales for another time."
    scene d17s03-31-mc-talk-ir with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Right, so why was Hana so concerned?"
    scene d17s03-33-ir-talk-mc with dissolve
    play voice3 iona_hmm1 noloop
    ir "Well, there are a couple of reasons. One I can't say. The other I won't talk about."
    scene d17s03-34-mc-talk-ir with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "I can guess one of those. You were working at that Party for the same reason I was."
    scene d17s03-35-ir-talk-mc with dissolve
    play voice3 dahlia_yes_yeah1 noloop
    ir "Yeah, I can imagine.{w} That's the one I won't talk about."
    ir "Hana learned about it somehow. She's certain that I'm being exploited."
    scene d17s03-36-mc-talk-ir with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Aren't we?"
    scene d17s03-37-ir-talk-mc with dissolve
    play voice3 dahlia_yes_simple noloop
    ir "Yes, but-{w} Anyway, I wanted to talk to you about the one I can't say."
    scene d17s03-38-mc-talk-ir with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.8
    mc "I'm lost."
    scene d17s03-39-ir-talk-mc with dissolve
    play voice3 iona_hah1 noloop
    ir "I can't talk about it because I don't know about it. I suspect maybe you do."
    scene d17s03-40-mc-talk-ir with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "I'm not getting less confused."
    $ renpy.music.set_volume(0.4, 5.0, "sound4")
    scene d17s03-41-ir-talk-mc with dissolve
    play voice3 iona_cagh noloop
    ir "Hana's paranoid. She sees threats everywhere. Sometimes she's right, sometimes she's not."
    ir "She didn't used to be like that."
    scene d17s03-42-mc-talk-ir with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "And you think I know why that is?"
    scene d17s03-43-ir-talk-mc with dissolve
    play voice3 iona_huh2 noloop
    ir "You're friends, right? Has she ever told you about the Senator?"
    scene d17s03-44-mc-talk-ir with dissolve
    play voice2 mc_no_no2 noloop
    mc "No."
    mct "Actually \"No\" to both questions, but maybe it's better if Iona thinks I am friends with Hana."
    scene d17s03-46-ir-talk-mc with dissolve
    play voice3 iona_ou2 noloop
    ir "The Senator is...{w} complicated."
    scene d17s03-45-mc-talk-ir with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "I'm guessing we have time."
    scene d17s03-48-ir-talk-mc with dissolve
    play voice3 iona_mmm3 noloop
    ir "Well, let's start with what you already know."
    scene d17s03-38-mc-talk-ir with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Okay."
    scene d17s03-39-ir-talk-mc with dissolve
    play voice3 iona_huh4 noloop
    ir "What do you know about us?"
    scene d17s03-40-mc-talk-ir with dissolve
    play voice2 mc_thinking_hmm1 noloop
    if persistent.is_special is True:
        mc "Hana said that you're her sister."
    elif True:
        mc "Hana said that you're her girlfriend."
    scene d17s03-41-ir-talk-mc with dissolve
    play voice3 dahlia_yes_aga noloop volume 0.75
    ir "Uh huh. What else?"
    scene d17s03-42-mc-talk-ir with dissolve
    play voice2 d2s12_emmm noloop
    mc "That's about it."
    scene d17s03-43-ir-talk-mc with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    ir "Oh, boy.{w} Well, for starters Hana is two and a half minutes older than me."
    scene d17s03-45-mc-talk-ir with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "You're twins?"
    scene d17s03-46-ir-talk-mc with dissolve
    if persistent.is_special is True:
        play voice3 iona_yes2 noloop
        ir "Exactly.{w} Fraternal, not identical."
        scene d17s03-47-mc-talk-ir with dissolve
        play voice2 mc_happy_yay2 noloop
        mc "I was going to say you didn't look THAT much alike."
        scene d17s03-48-ir-talk-mc with dissolve
        ir "We shared a womb, not a zygote."
        scene d17s03-47-mc-talk-ir with dissolve
        play voice2 mc_hey_hey3 noloop
        mc "I know the difference."
        scene d17s03-46-ir-talk-mc with dissolve
        play voice3 iona_ou1 noloop
        ir "Oh, right. College boy."
        scene d17s03-45-mc-talk-ir with dissolve
        play voice2 mc_angry_hm1 noloop
        mc "So, you're twins and she's the older sister. She's protective of you."
    elif True:
        play voice3 dahlia_no_nah noloop volume 0.6
        ir "Not quite. Our fathers met in the Maternity Ward. My dad brought cigars."
        scene d17s03-47-mc-talk-ir with dissolve
        play voice2 mc_surprised_what2 noloop
        mc "How long ago was this? You can't smoke in a hospital."
        scene d17s03-48-ir-talk-mc with dissolve
        play voice3 iona_laughing1 noloop
        ir "They weren't smoking. He was just handing them out. It was the politically expedient thing to do."
        scene d17s03-47-mc-talk-ir with dissolve
        play voice2 mc_thinking_hmm3 noloop
        mc "So the Senator is your father?"
        scene d17s03-46-ir-talk-mc with dissolve
        play voice3 iona_ou1 noloop
        ir "Good job, College Boy."
        scene d17s03-45-mc-talk-ir with dissolve
        play voice2 mc_thinking_hmm5 noloop
        mc "So, your family is elite with political ties, and her family...?"
    scene d17s03-43-ir-talk-mc with dissolve
    play voice3 dahlia_yes_yeah2 noloop
    ir "You got it. She's always been reliable and trying to succeed while I was usually looking for trouble."
    scene d17s03-42-mc-talk-ir with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Tale as old as time. Although, you don't seem to be looking for trouble."
    scene d17s03-41-ir-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    ir "I was a pretty wild child. I guess I've matured in the past few years."
    scene d17s03-40-mc-talk-ir with dissolve
    play voice2 d2s9_confused noloop volume 1.3
    mc "Did something happen? Something involving this Senator?"
    scene d17s03-39-ir-talk-mc with dissolve
    play voice3 dahlia_disgust_yah noloop volume 0.75
    ir "Yeah... among other things."
    scene d17s03-38-mc-talk-ir with dissolve
    play voice2 d1s1_mmm noloop volume 1.8
    mct "Sounds like there's a story there.{w} I need to stay focused."
    scene d17s03-57-mc-talk-ir with dissolve
    if persistent.is_special is True:
        play voice2 mc_angry_cough1 noloop
        mc "Who is he?"
        scene d17s03-60-ir-talk-mc with dissolve
        play voice3 iona_geh noloop
        ir "The Senator is our father."
        scene d17s03-59-mc-talk-ir with dissolve
        play voice2 mc_scared_oh4 noloop
        mc "Oh."
    mc "Is there something you want to tell me about him?"
    scene d17s03-58-ir-talk-mc with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    ir "I'd love to, but I don't know what it is."
    scene d17s03-55-mc-talk-ir with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "That's cryptic."
    scene d17s03-56-ir-talk-mc with dissolve
    play voice3 iona_mmm1 noloop
    ir "You know that she used to hate the idea of tattoos?"
    scene d17s03-53-mc-talk-ir with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Strange."
    scene d17s03-54-ir-talk-mc with dissolve
    ir "Then about two weeks after she started working for the Senator she got her first tat."
    scene d17s03-51-mc-talk-ir with dissolve
    play voice2 mc_surprised_huh5 noloop
    mc "Not Yours?"
    scene d17s03-52-ir-talk-mc with dissolve
    play voice3 iona_yes1 noloop
    ir "Exactly."
    scene d17s03-49-mc-talk-ir with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "Huh.{w} Tell me about your mother."
    scene d17s03-50-ir-talk-mc with dissolve
    play voice3 iona_huh3 noloop
    ir "Is that some kind of joke? I don't need psychotherapy - I need information and an outside perspective."
    scene d17s03-47-mc-talk-ir with dissolve
    play voice2 mc_no_no4 noloop
    mc "Not a joke. Not therapy.{w} What does your mother think about her behavior?"
    scene d17s03-50-ir-talk-mc with dissolve
    play voice3 dahlia_arrogant_pff noloop
    if persistent.is_special is True:
        ir "No idea. She's never really been in the picture."
    elif True:
        ir "Hana has become distant. The Senator is beyond distant with me now. Mom... well, she's basically nonexistent."
    scene d17s03-49-mc-talk-ir with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "Oh, I didn't realize-"
    scene d17s03-52-ir-talk-mc with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    ir "It's not like they divorced or anything. She has her career and she's always there for the Senator's campaigns, but..."
    scene d17s03-51-mc-talk-ir with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "She wasn't interested in being a mother?"
    scene d17s03-54-ir-talk-mc with dissolve
    play voice3 min_arrogant_hm noloop
    if persistent.is_special is True:
        ir "We always had nannies."
    elif True:
        ir "I always had nannies."
    scene d17s03-53-mc-talk-ir with dissolve
    play voice2 d1s2_hmm noloop volume 2.0
    mc "Plural?"
    scene d17s03-56-ir-talk-mc with dissolve
    play voice3 iona_hm1 noloop
    if persistent.is_special is True:
        ir "They never stuck around for long. Our parents didn't want us getting attached to any of them. They weren't family."
    elif True:
        ir "They never stuck around for long. My parents didn't want me getting attached to any of them. They weren't family."
    scene d17s03-55-mc-talk-ir with dissolve
    play voice2 mc_pain_auh1 noloop
    mc "Sounds tough."
    scene d17s03-58-ir-talk-mc with dissolve
    play voice3 dahlia_yes_yeah3 noloop
    if persistent.is_special is True:
        ir "Yeah, well, we're spoiled little rich girls. There were upsides and downsides."
    elif True:
        ir "Yeah, well, I always had Hana and her family. Even after her parents divorced, they both stayed close with us."
    scene d17s03-57-mc-talk-ir with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "I can't even imagine.{w} So, your dad - sorry, the Senator - was just as distant?"
    scene d17s03-60-ir-talk-mc with dissolve
    play voice3 iona_no1 noloop
    ir "Not when we were young. When we were children he was always there and always spoiled us both."
    if persistent.is_special is True:
        ir "Maybe me more than Hana. He always said that I was his favorite."
        scene d17s03-59-mc-talk-ir with dissolve
        play voice2 mc_pain_auch1 noloop
        mc "Ouch."
    elif True:
        ir "Maybe he spoiled me more than Hana, but he always included her. Made sure we had the best clothes and dolls and all that."
        scene d17s03-59-mc-talk-ir with dissolve
        play voice2 mc_happy_a1 noloop
        mc "Sounds nice."
    scene d17s03-62-ir-talk-mc with dissolve
    play voice3 iona_hmm1 noloop
    ir "Anyway, by the time we were teenagers he had lost interest in either of us. I felt guilty for years - like I had done something to push him away."
    ir "Hana was always there for me, though."
    scene d17s03-61-mc-talk-ir with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "But she's gotten more distant?"
    scene d17s03-64-ir-talk-mc with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    ir "Ever since she started working for the Senator."
    ir "She's not just distant... She's different."
    scene d17s03-63-mc-talk-ir with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Hmm."
    if persistent.is_special is True:
        mc "Let me get this straight. You and Hana have known each other since before you were even born."
    elif True:
        mc "Let me get this straight. You and Hana have known each other practically since birth."
    $ renpy.music.set_volume(0.5, 1.5, "sound4")
    scene d17s03-65-mc-ir-arrived-at-a-bus-stop with dissolve
    pause
    play voice3 dahlia_yes_yeah4 noloop
    ir "Yup."
    $ renpy.music.set_volume(0.1, 5.5, "sound4")
    scene d17s03-66-mc-talk-ir with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Now you fuck."
    scene d17s03-67-ir-talk-mc with dissolve
    play voice3 iona_hm2 noloop
    ir "Most people do."
    if persistent.is_special is True:
        scene d17s03-68-mc-talk-ir with dissolve
        play voice2 d1s5_mchappy noloop volume 1.8
        mc "I mean, you fuck each other."
        scene d17s03-69-ir-talk-mc with dissolve
        play voice3 iona_hm3 noloop
        ir "What?! No!{w} Hell no!"
        ir "Dude, she's my twin sister!"
        scene d17s03-85-mc-talk-ir with dissolve
        play voice2 d1s5b_emmm noloop volume 1.5
        mc "Sorry, I guess I misunderstood.{w} But you're both sexy, single, and attracted to women?"
        scene d17s03-84-ir-talk-mc with dissolve
    elif True:
        scene d17s03-85-mc-talk-ir with dissolve
        play voice2 d1s5_mchappy noloop volume 1.8
        mc "I mean, you fuck each other.{w} Now you're girlfriends."
        scene d17s03-84-ir-talk-mc with dissolve
        play voice3 dahlia_no_high3 noloop
        ir "Not really..."

    play voice3 iona_geh noloop
    ir "She's bisexual. I'm pansexual."
    scene d17s03-83-mc-talk-ir with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Wait a sec...{w} What's the difference?"
    scene d17s03-84-ir-talk-mc with dissolve
    play voice3 iona_kghhh noloop
    ir "As far as you're concerned, nothing. We both fuck whoever we find attractive."
    scene d17s03-85-mc-talk-ir with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "I'd love to hear about that someday."
    scene d17s03-82-ir-talk-mc with dissolve
    play voice3 iona_mmm2 noloop
    ir "Someday I'll tell you all about our 18th birthday party. We invited the entire volleyball team."
    scene d17s03-81-mc-talk-ir with dissolve
    play voice2 mc_surprised_huh3 noloop
    mc "You both fucked the entire volleyball team?!"
    scene d17s03-79-ir-talk-mc with dissolve
    play voice3 iona_no1 noloop
    ir "No, of course not.{w} We only did what we wanted to do."
    scene d17s03-75-mc-talk-ir with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh.{w} Did that involve fucking most of the volleyball team?"
    scene d17s03-77-ir-talk-mc with dissolve
    play voice3 iona_huh4 noloop
    ir "I'll tell you all about it sometime, but not now."
    scene d17s03-74-ir-talk-mc with dissolve
    mct "Right. Focus."
    scene d17s03-73-mc-talk-ir with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "I'm sorry, I got kinda distracted."
    if persistent.is_special is True:
        scene d17s03-71-ir-talk-mc with dissolve
        play voice3 dahlia_thinking_mmm2 noloop
        ir "You were saying we are twins, known each other our entire lives, and are both sexually active."
        scene d17s03-70-mc-talk-ir with dissolve
        play voice2 mc_thinking_hmm1 noloop
        mc "But not with each other."
        scene d17s03-76-ir-talk-mc with dissolve
        play voice3 iona_yes3 noloop
        ir "Right."
    elif True:
        scene d17s03-71-ir-talk-mc with dissolve
        play voice3 dahlia_thinking_mmm2 noloop
        ir "You were saying that we've known each other our entire lives and we're girlfriends."
    scene d17s03-70-mc-talk-ir with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "So, at some point Hana started working for your father."
    scene d17s03-69-ir-talk-mc with dissolve
    play voice3 dahlia_yes_yeah2 noloop
    ir "The Senator, yeah."
    scene d17s03-68-mc-talk-ir with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "And since then he's been paying more attention to her, and they've both been paying less attention to you."
    scene d17s03-67-ir-talk-mc with dissolve
    play voice3 iona_yes2 noloop
    ir "Yuuup."
    scene d17s03-66-mc-talk-ir with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "And you suspect something is wrong with that?"
    scene d17s03-67-ir-talk-mc with dissolve
    play voice3 iona_mmm1 noloop
    ir "It might be a coincidence, but Hana's been very strange since she took that job at his office."
    scene d17s03-68-mc-talk-ir with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "You're sure you're not jealous?"
    scene d17s03-69-ir-talk-mc with dissolve
    play voice dahlia_thinking_hmm4 noloop
    ir "Maybe I've changed my mind.{w} Maybe I should just beat the living shit out of you and make sure you're so brain damaged that you can't remember this conversation."
    scene d17s03-70-mc-talk-ir with dissolve
    play voice2 mc_scared_huh1 noloop
    mc "Fuck! Whoa!! Whoa!!!"
    play voice3 iona_grrr noloop volume 2.0
    scene d17s03-71-ir-talk-mc with dissolve
    ir "Give me one fucking reason I shouldn't put you in the coma ward."
    scene d17s03-73-mc-talk-ir with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "I can help you. I was just trying to sort out the possibilities."
    scene d17s03-74-ir-talk-mc with dissolve
    play voice3 iona_cagh noloop
    ir "I am not fucking jealous.{w} If there is something twisted going on between those two, it isn't right."
    scene d17s03-75-mc-talk-ir with dissolve
    mct "That doesn't sound like jealousy at all."
    play voice2 mc_yes_aga1 noloop
    mc "I believe you."
    scene d17s03-77-ir-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    ir "If he's hurting her - you need to tell me."
    scene d17s03-78-mc-talk-ir with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "I'll see what I can find out!{w} Please don't hurt me."
    scene d17s03-79-ir-talk-mc with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    ir "Alright. Anyway, Let's get on the damn bus."
    scene d17s03-81-mc-talk-ir with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, okay."
    scene d17s03-82-ir-talk-mc with dissolve
    play voice3 iona_ou2 noloop
    ir "And don't mention any of this - even on the bus. I don't want anyone else to hear about it."
    scene d17s03-83-mc-talk-ir with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Right. There's a political career to think of here."
    scene d17s03-84-ir-talk-mc with dissolve
    play voice3 iona_yes3 noloop
    ir "And Hana's reputation.{w} I WILL NOT HAVE HER DRAGGED IN FRONT OF THE MEDIA."
    scene d17s03-85-mc-talk-ir with dissolve
    $ unlock_gallery_slot("cg", "d17s03")
    play voice2 mc_yes_sure1 noloop
    mc "Understood."
    play sound sfx_bus_startmove volume 0.7
    stop sound3 fadeout 3.0
    stop sound4 fadeout 3.0
    stop music fadeout 5.0

    jump d17s04

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
