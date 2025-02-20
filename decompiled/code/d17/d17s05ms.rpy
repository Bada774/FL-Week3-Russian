image d17s05c-a0 = Movie(play = "images/Day-17/s05c-stacy/anim/d17s05c-a0-2x-50fps.webm", start_image = "d17s05-102-a1-v2 sy mh - stacy-glambot-1-v2-000_i", image = "d17s05-102-a1-v2 sy mh - stacy-glambot-1-v2-198_i", loop=False)

label d17s05ms:

    scene black
    show screen scene_transistion(_("30 minutes later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.35, 0.0, "sound3")
    play sound3 subwaycar fadein 3.0
    scene d17s05-00-sy-mh-stacy-lyssa-subway
    with Fade(0.5, 0.5, 0.9)
    play voice2 d2s9_mchey noloop
    mc "You alright? You look like you're about to throw up."
    scene d17s05-01-sy-mh-stacy-lyssa-subway with dissolve
    play voice3 stacy_upset1 noloop
    sy "What? I'm fine."
    scene d17s05-02-sy-mh-stacy-lyssa-subway with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yes, you have the distinct hunch-backed and anxious expression of someone that is completely zen."
    mc "Talk to me, what's wrong?"
    scene d17s05-03-sy-mh-stacy-lyssa-subway with dissolve
    play voice3 stacy_smell noloop
    sy "I'm just a little anxious."
    play voice2 mc_thinking_hmm5 noloop
    mc "...That it?"
    scene d17s05-04-sy-mh-stacy-lyssa-subway with dissolve
    play voice3 stacy_mmm1 noloop
    sy "Maybe this was a bad idea. I barely know her."
    scene d17s05-05-sy-mh-stacy-lyssa-subway with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "And?"
    scene d17s05-06-sy-mh-stacy-lyssa-subway with dissolve
    play voice3 stacy_oh2 noloop
    sy "And I'm going over to her house, and it's just..."
    scene d17s05-07-sy-mh-stacy-lyssa-subway with dissolve
    play voice2 d1s2_hmm noloop volume 1.8
    mc "Worried that she won't like you or something?"
    scene d17s05-08-sy-mh-stacy-lyssa-subway with dissolve
    sy "..."
    scene d17s05-09-sy-mh-stacy-lyssa-subway with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.5
    mc "Look, you'll be fine."
    scene d17s05-10-sy-mh-stacy-lyssa-subway with dissolve
    pause
    scene d17s05-11-sy-mh-stacy-lyssa-subway with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.5
    mc "She's not going to be put off by your little schoolyard crush."
    scene d17s05-12-sy-mh-stacy-lyssa-subway with dissolve
    play voice3 stacy_no2 noloop
    sy "I don't have a crush on her!"
    scene d17s05-13-sy-mh-stacy-lyssa-subway with dissolve
    play voice2 mc_arrogant_pff1 noloop
    mc "Stacy please, you {i}clearly{/i} have a crush on her."
    mc "And I'm fine with it."
    scene d17s05-14-sy-mh-stacy-lyssa-subway with dissolve
    play voice3 stacy_huh noloop
    sy "What?"
    scene d17s05-15-sy-mh-stacy-lyssa-subway with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Y'know, at first I thought you were just being a nosy ass, but then the puzzle pieces fit together and everything made sense."
    scene d17s05-16-sy-mh-stacy-lyssa-subway with dissolve
    play voice3 stacy_oh noloop
    sy "It's really that obvious?"
    scene d17s05-17-sy-mh-stacy-lyssa-subway with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "It kinda is."
    scene d17s05-18-sy-mh-stacy-lyssa-subway with dissolve
    play voice3 stacy_angryhuh noloop
    sy "Sheesh."
    scene d17s05-19-sy-mh-stacy-lyssa-subway with dissolve
    sy "I just think she's neat man, I dunno what to say."
    scene d17s05-20-sy-mh-stacy-lyssa-subway with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Well, I think she's neat as well. And I think she'll think that you're neat too."
    scene d17s05-21-sy-mh-stacy-lyssa-subway with dissolve
    mc "Now sit up straight before you get scoliosis or something. We're getting off here."
    scene d17s05-22-sy-mh-stacy-lyssa-subway with dissolve
    play voice3 amrose_arrogant_pff noloop
    sy "Ugh, you're not my real dad."
    stop sound3 fadeout 3.5
    scene black with Dissolve (0.7)
    pause

    play sound2 park fadein 1.5
    scene d17s05-00-sy-mh-stacy-lyssa with dissolve
    play voice3 stacy_surprised_whistle noloop
    sy "*Whistles* Damn. I knew she was rich, but this is {i}nice{/i}."
    scene d17s05-01-sy-mh-stacy-lyssa with dissolve
    play voice2 d9s2_mcyes noloop volume 2.5
    mc "It's nicer inside, come on."
    scene d17s05-02-sy-mh-stacy-lyssa with dissolve
    play voice3 daisy_hey noloop
    mh "Hey, you two. I've been waiting."
    $ renpy.music.set_volume(0.4, 4.0, "music")
    play music tender_moment fadein 0.4
    stop sound2 fadeout 3.0
    play voice2 d1s1_mmm noloop
    play sound maria_kiss1
    play voice3 lissa_mmm1 noloop
    scene d17s05-03-sy-mh-stacy-lyssa with dissolve
    pause
    scene d17s05-04-sy-mh-stacy-lyssa with dissolve
    queue voice3 lissa_haha noloop
    $ renpy.music.set_volume(0.3, 4.0, "music")
    mh "Stacy, right? I haven't seen you in a while."
    scene d17s05-05-sy-mh-stacy-lyssa with dissolve
    play voice4 polly_hey noloop
    sy "Hey, yeah. Aside from that time I crashed the date you and [mcname] were on."
    scene d17s05-06-sy-mh-stacy-lyssa with dissolve
    play voice3 lissa_oh2 noloop
    mh "Oh that's nothing to worry about."
    mh "Come on in."
    scene d17s05-07-sy-mh-stacy-lyssa with dissolve
    play voice4 stacy_hmm noloop
    sy "Amazing house you have here."
    sy "Quiet."
    scene d17s05-08-sy-mh-stacy-lyssa with dissolve
    play voice3 lissa_thinking noloop
    mh "Thank you. After having to endure hours of courtroom and client chatter, it's nice to come home to quiet."
    scene d17s05-09-sy-mh-stacy-lyssa with dissolve
    mh "Sit. Please."
    scene d17s05-10-sy-mh-stacy-lyssa with dissolve
    mh "Can I get you two something to drink?"
    scene d17s05-11-sy-mh-stacy-lyssa with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Don't think my life is fucked up enough to be day drinking yet."
    scene d17s05-12-sy-mh-stacy-lyssa with dissolve
    play voice4 stacy_huh2 noloop
    sy "Does that mean you expect it to get that fucked up?"
    scene d17s05-13-sy-mh-stacy-lyssa with dissolve
    play voice3 lissa_haha2 noloop
    mh "*Laughs* Tea? Coffee? Some fresh juice perhaps?"
    scene d17s05-14-sy-mh-stacy-lyssa with dissolve
    play voice4 polly_aga noloop
    sy "I could go for some tea."
    scene d17s05-15-sy-mh-stacy-lyssa with dissolve
    play voice3 lissa_ugu2 noloop
    mh "Great. [mcname], you sure you don't want anything?"
    scene d17s05-16-sy-mh-stacy-lyssa with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Guess I'll take tea as well."
    scene d17s05-17-sy-mh-stacy-lyssa with dissolve
    mh "Alright. I'll be back in a bit."
    scene d17s05-18-sy-mh-stacy-lyssa with dissolve
    play voice4 amrose_old_psst noloop volume 1.5
    sy "*Whispers* This is so awkward."
    scene d17s05-19-sy-mh-stacy-lyssa with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What? What do you mean?"
    scene d17s05-20-sy-mh-stacy-lyssa with dissolve
    play voice4 stacy_upset1 noloop
    sy "I have no clue what I'm doing!"
    scene d17s05-21-sy-mh-stacy-lyssa with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Just calm down, you're doing great."
    scene d17s05-22-sy-mh-stacy-lyssa with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Lyssa! Where are the games? I can set 'em up while you do that."
    scene d17s05-23-sy-mh-stacy-lyssa with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    mh "Check there."
    scene d17s05-24-sy-mh-stacy-lyssa with dissolve
    pause
    scene d17s05-25-sy-mh-stacy-lyssa with dissolve
    pause
    scene d17s05-26-sy-mh-stacy-lyssa with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    mh "How about we play some Cards Against Humans? See where we go from there."
    scene d17s05-27-sy-mh-stacy-lyssa with dissolve
    play voice4 stacy_oh2 noloop
    sy "Oh, that could be fun!"
    scene d17s05-28-sy-mh-stacy-lyssa with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "I'm down with whatever you two want to do."
    scene d17s05-29-sy-mh-stacy-lyssa with dissolve
    play voice3 lissa_ugu noloop
    mh "Cards Against Humans it is then."
    mh "So... Who went to the bathroom most recently?"
    scene d17s05-30-sy-mh-stacy-lyssa with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "I'm sorry, what?"
    scene d17s05-31-sy-mh-stacy-lyssa with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    mh "Have you never played Cards Against Humans?"
    scene d17s05-32-sy-mh-stacy-lyssa with dissolve
    play voice2 d2s9_confused noloop volume 1.5
    mc "I've heard about it, but I've never played."
    scene d17s05-33-sy-mh-stacy-lyssa with dissolve
    play voice3 lissa_thinking noloop
    mh "Well, the game starts by picking the most recent person that went uh...\"potty.\""
    scene d17s05-34-sy-mh-stacy-lyssa with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "...That's an interesting way to randomize the beginning player I guess."
    mc "Uhm, I think I might be the one that most recently took a shit then?"
    scene d17s05-35-sy-mh-stacy-lyssa with dissolve
    play voice3 lissa_laugh2 noloop
    mh "Great. We found our Card Czar then."
    scene d17s05-36-sy-mh-stacy-lyssa with fade
    play voice3 lissa_aga noloop
    mh "Alright, {i}Czar{/i}, pick a black card."
    scene d17s05-37-sy-mh-stacy-lyssa with dissolve
    pause
    scene d17s05-37-sy-mh-stacy-lyssa-house-extra with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "\"Men like...\""
    mc "Oh this'll be fun. You two have to pick the most heinous white card, right?"
    scene d17s05-38-sy-mh-stacy-lyssa with dissolve
    play voice3 lissa_yes noloop
    mh "Pretty much."
    scene d17s05-37-sy-mh-stacy-lyssa-house-extra-2 with dissolve
    mh "Now shuffle the white cards and pick the funniest one."
    scene d17s05-39-sy-mh-stacy-lyssa-house-extra with dissolve
    pause
    play voice2 d14s16_smell noloop
    scene d17s05-40-sy-mh-stacy-lyssa with dissolve
    pause
    scene d17s05-41-sy-mh-stacy-lyssa with dissolve
    play voice2 d1s5_mchappy noloop volume 1.5
    mc "The cards you two picked are, \"Men like... Women with daddy Issues.\""
    mc "and, \"Men like... Shitting out a part of a turd, sucking it back in, and shitting it back out over and over so you're basically fucking yourself with your own shit...\""
    scene d17s05-42-sy-mh-stacy-lyssa with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Well, huh."
    scene d17s05-43-sy-mh-stacy-lyssa with dissolve
    play voice3 lissa_laugh noloop
    mh "*Snickers*"
    play voice2 mc_thinking_emm1 noloop
    mc "I kinda {i}have{/i} to go with that one at this point."
    scene d17s05-44-sy-mh-stacy-lyssa with dissolve
    play voice3 dahlia_happy_yay noloop
    mh "One point for me then."
    scene d17s05-45-sy-mh-stacy-lyssa with dissolve
    play voice2 mc_disgust_meh4 noloop
    mc "Jesus, Lyssa."
    scene d17s05-46-sy-mh-stacy-lyssa with dissolve
    play voice3 daisy_hey noloop
    mh "Hey, don't judge me."
    play voice2 d4s4_mclaugh noloop
    play voice3 lissa_laugh2 noloop
    play voice4 stacy_laugh noloop
    scene d17s05-47-sy-mh-stacy-lyssa with dissolve
    pause

    scene black
    show screen scene_transistion(_("30 minutes later"))
    with Fade(0.8, 0.5, 0.1)
    pause

    hide screen scene_transistion
    scene d17s05-48-sy-mh-stacy-lyssa
    with Fade(0.1,0.5,0.8)
    play voice4 stacy_angryhuh noloop
    sy "You're fucked up, [mcname]."
    scene d17s05-49-sy-mh-stacy-lyssa with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I'm playing the game the way it was meant to be played!"
    scene d17s05-50-sy-mh-stacy-lyssa with dissolve
    play voice4 polly_nouh noloop
    sy "Nah, man, that was fucked."
    scene d17s05-51-sy-mh-stacy-lyssa with dissolve
    play voice3 lissa_shyoh noloop
    mh "The poor orphans."
    scene d17s05-52-sy-mh-stacy-lyssa with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "This is an organized attack on my character."
    play sound sfx_doorbell_lyssa
    scene d17s05-53-sy-mh-stacy-lyssa with dissolve
    play voice3 lissa_oh noloop
    mh "Oh, I think that's our food."
    scene d17s05-54-sy-mh-stacy-lyssa with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "I'll go get it. You two socialize or something."
    scene d17s05-55-sy-mh-stacy-lyssa with dissolve
    play voice3 lissa_haha2 noloop
    mh "This is fun."
    scene d17s05-56-sy-mh-stacy-lyssa with dissolve
    play voice4 stacy_yes3 noloop
    sy "It is! Thank you for inviting me over."
    scene d17s05-57-sy-mh-stacy-lyssa with dissolve
    play voice3 lissa_moan1 noloop
    mh "Of course. You're a delight."
    scene d17s05-58-sy-mh-stacy-lyssa with dissolve
    pause
    scene d17s05-59-sy-mh-stacy-lyssa with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    mh "You said you were still studying, right? Or I think it might've been [mcname] that said it."
    scene d17s05-60-sy-mh-stacy-lyssa with dissolve
    play voice4 stacy_nono noloop
    sy "No, actually. I'll be going next year. Kinda just hanging out, enjoying my freedom."
    sy "I {i}have{/i} been applying to some gigs. Can't live on handouts forever. Mostly ghosts though."
    scene d17s05-61-sy-mh-stacy-lyssa with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    mh "Ah, I understand the pain."
    scene d17s05-62-sy-mh-stacy-lyssa with dissolve
    play voice4 stacy_hmm noloop
    sy "I actually got an interview recently though."
    sy "CPD of all places."
    scene d17s05-63-sy-mh-stacy-lyssa with dissolve
    play voice3 lissa_oh2 noloop
    mh "Oh? You applied to CPD?"
    scene d17s05-64-sy-mh-stacy-lyssa with dissolve
    play voice4 stacy_yeahno noloop
    sy "Yeah, I saw a flier and just kinda yoloed it."
    scene d17s05-65-sy-mh-stacy-lyssa with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    mh "I actually know a few people in the CPD."
    scene d17s05-66-sy-mh-stacy-lyssa with dissolve
    play voice4 stacy_huh2 noloop
    sy "Really? Wow, you must be well connected."
    scene d17s05-67-sy-mh-stacy-lyssa with dissolve
    play voice3 dahlia_yes_ugu noloop
    mh "It helps to know people in my profession. It helps to know people in any profession to be honest."
    scene d17s05-68-sy-mh-stacy-lyssa with dissolve
    play voice4 stacy_laugh4 noloop
    sy "True, true."
    scene d17s05-65-sy-mh-stacy-lyssa with dissolve
    play voice3 lissa_haha noloop
    mh "But yes, I can put in a good word for you."
    scene d17s05-67-sy-mh-stacy-lyssa with dissolve
    mh "If you're alright with that, of course."
    scene d17s05-60-sy-mh-stacy-lyssa with dissolve
    play voice4 stacy_mmm2 noloop
    sy "No, yeah, that would be great! I, uhm, actually..."
    scene d17s05-69-sy-mh-stacy-lyssa with dissolve
    play voice2 mc_eating_mmm noloop
    mc "*Muffled* Back."
    scene d17s05-70-sy-mh-stacy-lyssa with dissolve
    queue voice2 d1s5_mcthinks noloop volume 1.5
    mc "What have you two been gossiping about without me?"
    scene d17s05-71-sy-mh-stacy-lyssa with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    mh "Stacy here was telling me about her applying to CPD."
    scene d17s05-72-sy-mh-stacy-lyssa with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Oh yeah?"
    scene d17s05-73-sy-mh-stacy-lyssa with dissolve
    play voice3 lissa_ugu2 noloop
    mh "She was going to ask me something I think."
    scene d17s05-74-sy-mh-stacy-lyssa with dissolve
    play voice4 stacy_mmm1 noloop
    sy "I, well, the gig that CPD had for me was basically being a digital janitor."
    sy "I was looking for something more in the direction of actual software development."
    scene d17s05-75-sy-mh-stacy-lyssa-house with dissolve
    play voice3 lissa_oh noloop
    mh "And you want me to see if I can get you that instead?"
    scene d17s05-76-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_upset1 noloop
    sy "Uhm, yep."
    scene d17s05-77-sy-mh-stacy-lyssa-house with dissolve
    play voice3 lissa_ha noloop
    mh "Of course, I can."
    mh "I can't guarantee anything, but I can sure see if there's anything I can do."
    scene d17s05-78-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "Man, it sure is helpful having friends in high places, huh?"
    scene d17s05-79-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_yay noloop
    sy "Thank you. That means a lot."
    scene d17s05-80-sy-mh-stacy-lyssa-house with dissolve
    play voice3 lissa_yes noloop
    mh "Of course."
    mh "Shall we get back to the game?"
    scene d17s05-81-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Think Stacy's going next."
    scene d17s05-82-sy-mh-stacy-lyssa-house with dissolve
    pause
    sy "\"A romantic, candlelit dinner would be incomplete without...\""
    if persistent.is_special is True:
        scene d17s05-83-sy-mh-stacy-lyssa-house with dissolve
        pause
        scene d17s05-85-sy-mh-stacy-lyssa-house with dissolve
    else:
        scene d17s05-84-sy-mh-stacy-lyssa-house with dissolve
        pause
        scene d17s05-86-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_hmm noloop
    sy "Someone said, \"A romantic, candlelit dinner would be incomplete without... Farting and walking away."
    scene d17s05-87-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_laugh noloop
    sy "Classy."
    scene d17s05-88-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_happy_hah1 noloop
    mc "Gassy."
    scene d17s05-89-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_huh noloop
    if persistent.is_special is True:
        sy "And someone else said, A romantic, candlelit dinner would be incomplete without... *Chuckling* Fucking my sister."
    else:
        sy "And someone else said, A romantic, candlelit dinner would be incomplete without... *Chuckling* Fucking my best friend."
    sy "That one wins."
    scene d17s05-88-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_happy_wooh3 noloop
    mc "Woo!"
    scene d17s05-89-sy-mh-stacy-lyssa-house with dissolve
    play voice4 polly_laughter noloop
    sy "You've never taken me out to a candlelit dinner though— Uhm."
    scene d17s05-90-sy-mh-stacy-lyssa-house with dissolve
    play voice3 lissa_oh2 noloop
    mh "Oh?"
    scene d17s05-91-sy-mh-stacy-lyssa-house with dissolve
    mh "Are you two—?"
    scene d17s05-92-sy-mh-stacy-lyssa-house with hpunch
    play voice4 stacy_ah noloop
    sy "What!? No, hah! Of course not."
    scene d17s05-93-sy-mh-stacy-lyssa-house with dissolve
    play voice3 lissa_laugh noloop
    mh "Oh my God. I don't believe you!"
    scene d17s05-94-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Now, I'm not saying anything...{i}but{/i}."
    scene d17s05-95-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_angry noloop
    sy "\"But\"!?"
    scene d17s05-96-sy-mh-stacy-lyssa-house with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    mh "\"{i}But{/i}\"?"
    scene d17s05-97-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Stacy, she's fine with it."
    scene d17s05-98-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_impressed noloop
    sy "I— What?"
    scene d17s05-99-sy-mh-stacy-lyssa-house with dissolve
    play voice3 lissa_thinking noloop
    mh "I can't believe that you two are actually close like that."
    scene d17s05-100-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Alright. You want proof?"
    scene d17s05-101-sy-mh-stacy-lyssa-house with dissolve
    pause
    $ renpy.music.set_volume(0.7, 2.0, "music")
    play sound ["<silence 0.5>", maria_kiss1]
    play voice2 ["<silence 0.5>", d1s1_mmm] noloop
    play voice4 ["<silence 0.5>", stacy_suckmoan2] noloop
    queue voice4 stacy_sucks1
    play voice3 ["<silence 7.0>", lissa_moan2] noloop
    scene d17s05c-a0 with fade
    pause
    scene d17s05-103-sy-mh-stacy-lyssa-house with dissolve
    pause
    play voice3 lissa_moan1 noloop
    scene d17s05-104-sy-mh-stacy-lyssa-house with dissolve
    pause
    scene d17s05-105-sy-mh-stacy-lyssa-house with dissolve
    pause
    stop voice4 fadeout 1.0
    $ renpy.music.set_volume(0.3, 2.0, "music")
    scene d17s05-106-sy-mh-stacy-lyssa-house with dissolve
    play voice3 lissa_mmm1 noloop
    mh "You two are unbelievable."
    scene d17s05-107-sy-mh-stacy-lyssa-house with dissolve
    if persistent.is_special is True:
        mh "Here I was thinking you two were just close siblings, but oh-no."
    else:
        mh "Here I was thinking you two were just close friends, but oh-no."
    scene d17s05-108-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_suckmoan1 noloop
    sy "I'm...confused."
    scene d17s05-109-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "We don't have to hide anything with Lyssa."
    scene d17s05-110-sy-mh-stacy-lyssa-house with dissolve
    play voice3 dahlia_thinking_oh noloop
    mh "Oh, you didn't explain to her?"
    scene d17s05-111-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Didn't find the time."
    scene d17s05-112-sy-mh-stacy-lyssa-house with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    mh "Oh you poor thing. Come here."
    scene d17s05-113-sy-mh-stacy-lyssa-house with dissolve
    pause
    scene d17s05-114-sy-mh-stacy-lyssa-house with dissolve
    pause
    scene d17s05-115-sy-mh-stacy-lyssa-house with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    if persistent.is_special is True:
        mh "Your brother and I are in a sort of...open relationship."
    else:
        mh "Your friend and I are in a sort of...open relationship."
    scene d17s05-116-sy-mh-stacy-lyssa-house with dissolve
    play voice3 lissa_haha noloop
    mh "I don't mind your relationship with him. I think it's cute even."
    mh "And about the uh, {i}specifics{/i} of the relationship between you two, I don't mind that either."
    scene d17s05-117-sy-mh-stacy-lyssa-house with dissolve
    mh "Feelings come in all shapes and forms, and I'm not the thought police."
    mh "If you two like each other that way, then I say that's as valid as any other loving, consenting relationship."
    scene d17s05-118-sy-mh-stacy-lyssa-house with dissolve
    mh "So you don't have to worry about me knowing. Got it?"
    scene d17s05-119-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_angryhuh noloop
    sy "You really are a hypocrite."
    scene d17s05-120-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hey, I only said \"public.\""
    scene d17s05-121-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_mmm1 noloop
    sy "He really had the audacity to tell me to keep it on the down low, and he just goes and tells you."
    scene d17s05-122-sy-mh-stacy-lyssa-house with dissolve
    play voice3 lissa_aga noloop
    mh "I like that about him. He's honest."
    scene d17s05-123-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "That's me, honest [mcname]."
    scene d17s05-124-sy-mh-stacy-lyssa-house with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    mh "You two want to continue playing?"
    scene d17s05-125-sy-mh-stacy-lyssa-house with dissolve
    play voice4 polly_aga noloop
    sy "I'd like that."
    scene d17s05-126-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure."
    $ renpy.music.set_volume(0.7, 3.0, "music")
    scene d17s05-127-sy-mh-stacy-lyssa-house with fade
    pause
    scene d17s05-128-sy-mh-stacy-lyssa-house with fade
    pause
    scene d17s05-129-sy-mh-stacy-lyssa-house with fade
    pause
    scene d17s05-130-sy-mh-stacy-lyssa-house with fade
    pause
    scene d17s05-131-sy-mh-stacy-lyssa-house with fade
    pause
    scene d17s05-132-sy-mh-stacy-lyssa-house with fade
    pause
    $ renpy.music.set_volume(0.3, 3.0, "music")
    scene d17s05-133-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_suckmoan2 noloop
    sy "Man, I didn't know [mcname] was such a cheater."
    scene d17s05-134-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_no_uhuh1 noloop
    mc "Using every tactic at my disposal doesn't make me a cheater."
    scene d17s05-135-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_hey noloop
    sy "Back me up here, girl."
    scene d17s05-136-sy-mh-stacy-lyssa-house with dissolve
    play voice3 lissa_laugh noloop
    mh "He's a cheater, but he's a cute cheater."
    scene d17s05-137-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_yeahno noloop
    sy "Agreed. But, a cheater nonetheless."
    sy "The council has decided."
    sy "Off with his head!"
    scene d17s05-138-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "This is tyranny!"
    play voice4 stacy_laugh2 noloop
    play voice3 lissa_laugh noloop
    play voice2 d4s4_mclaugh noloop
    scene d17s05-139-sy-mh-stacy-lyssa-house with dissolve
    pause
    scene d17s05-140-sy-mh-stacy-lyssa-house with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    mh "*Yawns* This has been really fun."
    scene d17s05-141-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Hm. Yeah. We need to do it again."
    scene d17s05-142-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_upset1 noloop
    sy "*Yawns* I'm down. Maybe we can have a sleepover or something."
    scene d17s05-143-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "Are you two seriously sleepy right now?"
    scene d17s05-144-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_hmm noloop
    sy "What? It's cold and I feel comfy."
    scene d17s05-145-sy-mh-stacy-lyssa-house with dissolve
    play voice3 lissa_haha2 noloop
    mh "What she said."
    scene d17s05-146-sy-mh-stacy-lyssa-house with dissolve
    play voice2 d3s11b_mcheh noloop
    mc "*Chuckles* We're never having any sleepovers at this rate."

    scene d17s05-147-sy-mh-stacy-lyssa-house with dissolve
    play voice2 d2s9_confused noloop volume 1.5
    mc "It {i}is{/i} getting pretty late though, we should probably head off."
    scene d17s05-148-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_oh noloop
    sy "Aww, do we have to?"
    scene d17s05-149-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Yes, we do."
    mc "For being an anxious wreck earlier, you sure changed your tune now."
    scene d17s05-150-sy-mh-stacy-lyssa-house with dissolve
    play voice4 polly_angry noloop
    sy "I— You—!"
    scene d17s05-151-sy-mh-stacy-lyssa-house with dissolve
    play voice3 lissa_thinking noloop
    mh "You were anxious? Why?"
    scene d17s05-152-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_mmm2 noloop
    sy "It was just...a new experience."
    scene d17s05-153-sy-mh-stacy-lyssa-house with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    mh "Hm. Well, I understand the feeling."
    if persistent.is_special is True:
        mh "You shouldn't tease your little sister so much, [mcname]."
    else:
        mc "You shouldn't tease your friend so much, [mcname]."
    scene d17s05-154-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Why does it always come around to me being blamed?"
    scene d17s05-155-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_smell noloop
    sy "Cause you're more often than not the one {i}{b}to{/b}{/i} blame."
    scene d17s05-156-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_disappointed_meh1 noloop
    mc "This is some sort of 'ism."
    scene d17s05-157-sy-mh-stacy-lyssa-house with dissolve
    pause
    scene d17s05-158-sy-mh-stacy-lyssa-house with dissolve
    play voice4 min_happy_relief noloop volume 0.7
    sy "This was really fun, Lyssa."
    scene d17s05-159-sy-mh-stacy-lyssa-house with dissolve
    play voice3 lissa_aga noloop
    mh "I'm glad you enjoyed it. It was really nice relaxing with you two today."
    scene d17s05-160-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I'm not sure I'd call it \"relaxing\" exactly, though. I was fighting for my life out there."
    play voice3 lissa_haha2 noloop
    play voice2 d4s4_mclaugh noloop
    play voice4 stacy_laugh noloop
    scene d17s05-161-sy-mh-stacy-lyssa-house with dissolve
    pause
    scene d17s05-162-sy-mh-stacy-lyssa-house with fade
    play voice4 stacy_upset1 noloop
    sy "*Sighs* We need to meet up again. I'm tired, but I don't want to go."
    scene d17s05-163-sy-mh-stacy-lyssa-house with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    mh "Hm, I feel the same way."
    scene d17s05-164-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_yes_yeah6 noloop
    mc "Alright, you lovebirds, we'll get plenty of time to chat in the future."
    scene d17s05-165-sy-mh-stacy-lyssa-house with dissolve
    play voice3 lissa_ha noloop
    mh "He's right. We can meet up again soon."
    scene d17s05-166-sy-mh-stacy-lyssa-house with dissolve
    mh "Be safe, alright?"
    play voice2 d1s1_mmm noloop
    play sound maria_kiss1
    play voice3 lissa_mmm1 noloop
    scene d17s05-167-sy-mh-stacy-lyssa-house with dissolve
    pause
    play sound maria_kiss2
    scene d17s05-168-sy-mh-stacy-lyssa-house with dissolve
    pause
    scene d17s05-169-sy-mh-stacy-lyssa-house with dissolve
    play voice2 d9s2_mcyes noloop volume 2.2
    mc "Always."
    scene d17s05-170-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_angry noloop
    sy "Heh, don't I get a kiss too?"
    scene d17s05-171-sy-mh-stacy-lyssa-house with dissolve
    pause
    scene d17s05-172-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_mmm1 noloop
    sy "Wai—"
    play voice4 stacy_suckmoan1 noloop
    play voice3 lissa_mmm2 noloop
    play sound maria_kiss1
    scene d17s05-173-sy-mh-stacy-lyssa-house with dissolve
    pause
    play sound maria_kiss2
    scene d17s05-174-sy-mh-stacy-lyssa-house with dissolve
    pause
    scene d17s05-175-sy-mh-stacy-lyssa-house with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    mh "Happy?"
    play voice4 min_thinking_mhh noloop
    sy "I—"
    scene d17s05-176-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_scared_oh3 noloop
    mc "Look at that, you broke the poor thing."
    scene d17s05-177-sy-mh-stacy-lyssa-house with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    mh "You two stay safe now."
    scene d17s05-178-sy-mh-stacy-lyssa-house with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "We will. You should go lay down a bit."
    scene d17s05-179-sy-mh-stacy-lyssa-house with dissolve
    play voice3 lissa_moan2 noloop
    mh "I will. I love you."

    menu:
        "I love you too"(hint="d17s05msm01c01"):
            $ d17s05_love_mh_sy = True
            scene d17s05-180-sy-mh-stacy-lyssa-house with dissolve
            play voice2 mc_yes_yeah1 noloop
            mc "I love you too."
        "Kiss her instead"(hint="d17s05msm01c02"):

            play voice2 d1s1_mmm noloop
            play sound maria_kiss1
            play voice3 lissa_mmm1 noloop
            scene d17s05-181-sy-mh-stacy-lyssa-house with dissolve
            pause

    scene d17s05-182-sy-mh-stacy-lyssa-house with dissolve
    play voice3 lissa_ugu noloop
    mh "Rest up well. I'll talk to you tomorrow. Goodnight."
    scene d17s05-183-sy-mh-stacy-lyssa-house with dissolve
    play voice4 polly_aga noloop
    sy "Hm? Yeah. Goodnight, Lyssa."
    scene d17s05-184-sy-mh-stacy-lyssa-house with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    mh "Goodnight, Stacy. I'm sorry for the surprise kiss."
    $ unlock_gallery_slot("cg", "d17s05")
    scene d17s05-185-sy-mh-stacy-lyssa-house with dissolve
    play voice4 stacy_nono noloop
    sy "No, no, I...liked it."
    scene d17s05-186-sy-mh-stacy-lyssa-house with dissolve
    play voice3 lissa_ugu2 noloop volume 1.8
    mh "Well, I'm glad."
    scene d17s05-187-sy-mh-stacy-lyssa-house with dissolve
    pause
    scene d17s05-188-sy-mh-stacy-lyssa-house with dissolve
    pause
    scene d17s05-189-sy-mh-stacy-lyssa-house with dissolve
    pause
    $ persistent.d17s05_mh_sy = True

    stop music fadeout 4.0
    jump d17s06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
