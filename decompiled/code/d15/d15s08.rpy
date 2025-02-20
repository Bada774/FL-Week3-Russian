label d15s08:

    if not hasattr(renpy.store, "d12s02_gavepass"):
        if hasattr(renpy.store, "d11s02_gavepass"):
            $ d12s02_gavepass = d11s02_gavepass
        else:
            $ d12s02_gavepass = False

    scene black
    show screen scene_transistion(_("30 minutes later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene d15s08-00 mc-hr-sy-arj-talking
    with Fade(0.5, 0.5, 0.9)
    play sound3 sfx_door_closed1 noloop
    pause
    if date_mes is True:
        call buzz from _call_buzz_6
        show x-phone-background
        show phone-fl-logo
        pause
        play sound sfx_message_in1
        call add_points (d15s07_points) from _call_add_points_3
        flr "You earned [d15s07_points] points."
        hide x-phone-background
        hide phone-fl-logo
        pause
    play voice2 mc_hey_hey5 noloop
    mc "Hi Honey, I'm hoooooome."
    $ renpy.music.set_volume(0.4, 0.0, "voice3")
    play voice3 stacy_mmm1 noloop
    sy "We're in the... {w}We can see you."
    $ renpy.music.set_volume(0.8, 3.0, "music")
    $ renpy.music.set_volume(1.0, 3.0, "voice3")
    play music thinking_music_3
    scene d15s08-01 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Oh, right. {w}Sorry I couldn't be here sooner. It's been one hell of a day."
    play voice4 amrose_arrogant_hmm2 noloop
    arj "Studying for finals?"
    play voice2 mc_arrogant_heh2 noloop
    mc "Some..."
    scene d15s08-02 mc-hr-sy-arj-talking with dissolve
    play voice3 hana_hmm noloop
    hr "I suppose we can get started now? Is the magical field of protection working correctly?"
    play voice4 stacy_hey noloop
    scene d15s08-03 mc-hr-sy-arj-talking with dissolve
    sy "It's not magic... it's just a Faraday cage."
    scene d15s08-04 mc-hr-sy-arj-talking with dissolve
    play voice3 hana_argh noloop
    hr "But it's working? You're sure of that?"
    scene d15s08-05 mc-hr-sy-arj-talking with dissolve
    play voice4 amrose_yes_yap noloop
    arj "No electrical signals can be sent into or out of this apartment. You can check your cell phone coverage if you don't believe us."
    scene d15s08-06 mc-hr-sy-arj-talking with dissolve
    play voice3 hana_emm noloop
    hr "I turned it off a few blocks away. I don't want the app to know my location."
    scene d15s08-11 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Well, we're about as safe as we can be. What are we talking about?"
    scene d15s08-08 mc-hr-sy-arj-talking with dissolve
    play voice4 stacy_oh2 noloop
    sy "Oh, we were talking about shades of lipstick. {w}Did you know that we're running out of the color blue?"
    sy "Not just us here, I mean. The whole world is running out of the color blue."
    scene d15s08-09 mc-hr-sy-arj-talking with dissolve
    play voice3 amrose_old_chmchm noloop
    arj "That's not what he meant."
    scene d15s08-10 mc-hr-sy-arj-talking with dissolve
    play voice4 dahlia_angry_hm1 noloop
    hr "Yes. Can we please get down to business."
    scene d15s08-08 mc-hr-sy-arj-talking with dissolve
    play voice3 stacy_oh noloop
    if is_antagonist_mode is False:
        sy "The business of discovering who is behind Fetish Locator and winning the treasure?"
    else:
        sy "The business of saving the world from the horrors of Fetish Locator?"
    scene d15s08-07 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yes. That.{w} So, where are we?"
    scene d15s08-13 mc-hr-sy-arj-talking with dissolve
    play voice4 amrose_thinking_hmm2 noloop
    arj "I'm working on the hardware."
    scene d15s08-12 mc-hr-sy-arj-talking with dissolve
    play voice3 polly_aga noloop
    sy "I'm working on the software!"
    scene d15s08-14 mc-hr-sy-arj-talking with dissolve
    play voice4 hana_argh2 noloop
    hr "I'm working on a headache.{w}.. but I've also provided these girls with everything I know about Fetish Locator."
    scene d15s08-12 mc-hr-sy-arj-talking with dissolve
    play voice3 stacy_huh2 noloop
    sy "Did you know she cloned Pete's phone?"
    play voice2 mc_yes_yes1 noloop
    mc "Yes."
    scene d15s08-13 mc-hr-sy-arj-talking with dissolve
    play voice3 amrose_disappointed_oh3 noloop
    arj "She seems rather fixated on your roommate. She even got access to his laptop."
    if d12s02_gavepass is False:
        play voice2 mc_yes_yeah4 noloop
        mc "Yeah, I heard about that."
        scene d15s08-15 mc-hr-sy-arj-talking with dissolve
        play voice4 hana_hmm2 noloop
        hr "You didn't leave me any other choice."
        scene d15s08-13 mc-hr-sy-arj-talking with dissolve
        play voice3 amrose_surprised_huh2 noloop
        arj "Huh?"
        scene d15s08-16 mc-hr-sy-arj-talking with dissolve
        play voice2 mc_disappointed_off2 noloop
        mc "She stole it. {w}Even though we agreed there was nothing useful on Pete's laptop."
        scene d15s08-15 mc-hr-sy-arj-talking with dissolve
        play voice4 dahlia_no_uhuh noloop
        hr "No, we didn't agree. You just refused to give me his password. {w}I was forced to verify your claim myself."
        scene d15s08-16 mc-hr-sy-arj-talking with dissolve
        play voice2 mc_arrogant_hm3 noloop
        mc "You're still a thief."
        scene d15s08-18 mc-hr-sy-arj-talking with dissolve
        play voice3 allison_wow noloop
        sy "Woah, whoa, whoa. {w}Let's not say anything we are going to regret later."
        scene d15s08-17 mc-hr-sy-arj-talking with dissolve
        play voice4 amrose_angry_ergh noloop
        arj "I agree with Stacy."
    else:
        play voice2 mc_yes_yeah4 noloop
        mc "Yeah..."
    scene d15s08-19 mc-hr-sy-arj-talking with dissolve
    play voice4 dahlia_angry_hm1 noloop
    hr "He was the most likely suspect, but not the only one. I also provided them the information I found on Min, Antony, Davey, and others."
    play voice2 d1s2_hmm noloop
    mc "Davey?"
    hr "And others."
    mct "I feel like Charlie.{w}.. or at least Bosworth."
    scene d15s08-20 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, Angels! Let's recap. Fetish Locator should have a physical server and we're going to find it."
    scene d15s08-21 mc-hr-sy-arj-talking with dissolve
    play voice4 dahlia_yes_angry noloop
    hr "That's the working theory, yes."
    scene d15s08-22 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Is there any basis for that assumption? I mean, it could be anywhere online, right?"
    scene d15s08-23 mc-hr-sy-arj-talking with dissolve
    play voice3 amrose_arrogant_hmm2 noloop
    arj "It's not a perfect theory, but it is the best hypothesis we have."
    scene d15s08-26 mc-hr-sy-arj-talking with dissolve
    play voice4 stacy_mmm2 noloop
    sy "Most likely the app is using some 3rd party cloud service, but that would make it really difficult to track."
    sy "So, we're working under the assumption that the app has physical servers somewhere nearby."
    scene d15s08-28 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Okay. And if they aren't?"
    scene d15s08-24 mc-hr-sy-arj-talking with dissolve
    play voice3 amrose_old_haha2 noloop
    arj "We'll burn that bridge when we come to it."
    play voice2 d1s5_mchappy noloop
    mc "Fair enough. AmRose, how's the hardware going?"
    scene d15s08-25 mc-hr-sy-arj-talking with dissolve
    play voice3 amrose_thinking_oh1 noloop
    arj "I picked up this little toy a couple months ago. I wasn't sure what I would ever use it for, but it is perfect for this."
    arj "This little baby is packed with two independent FPGAs connected to a custom SoC for optimal performance and a relatively reasonable power demand."
    scene d15s08-28 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Relatively reasonable?"
    play voice3 amrose_yes_yeah1 noloop
    arj "Yeah..."
    play voice2 mc_thinking_mmm3 noloop
    mc "How bad are we talking about?"
    scene d15s08-27 mc-hr-sy-arj-talking with dissolve
    play voice4 stacy_huh2 noloop
    sy "How do you feel about carrying around a couple of car batteries?"
    scene d15s08-20 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "I don't like that idea at all."
    scene d15s08-23 mc-hr-sy-arj-talking with dissolve
    play voice3 amrose_thinking_emm noloop
    arj "There's a parasitic power drain. {w}It's a hardware problem. There will be a hardware solution."
    scene d15s08-30 mc-hr-sy-arj-talking with dissolve
    play voice4 hana_argh noloop
    hr "We're kinda on the clock here. Time is a factor."
    scene d15s08-24 mc-hr-sy-arj-talking with dissolve
    play voice3 amrose_no_nah noloop
    arj "Don't worry. I'm on it."
    scene d15s08-28 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Good enough for me. Stacy, how's the software going?"
    scene d15s08-26 mc-hr-sy-arj-talking with dissolve
    play voice4 stacy_hmm noloop
    sy "I've built an emulator for AmRose's little device. I should have the code ready by the time she solves the power issues."
    scene d15s08-20 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Cool. AmRose is on hardware; Stacy is on software; and Hana provided technical information."
    scene d15s08-30 mc-hr-sy-arj-talking with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    hr "I guess that makes you the project manager, [mcname]."
    scene d15s08-27 mc-hr-sy-arj-talking with dissolve
    play voice4 stacy_hey noloop
    sy "Hey! He's got the most important job of all{w} - [mcname] is the bait!"
    scene d15s08-28 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, it won't just be me."
    scene d15s08-19 mc-hr-sy-arj-talking with dissolve
    play voice3 hana_emm noloop
    hr "What do you mean?"
    play voice2 mc_arrogant_hm1 noloop
    mc "I'll carry the device. I'm earning points again, so I'll earn as much as possible."
    mc "I'll attract the attention of Fetish Locator, but I won't be doing that all by myself."
    scene d15s08-24 mc-hr-sy-arj-talking with dissolve
    play voice4 amrose_yes_ugu noloop
    arj "You know I'll help you with that."
    if date_sy is True:
        scene d15s08-12 mc-hr-sy-arj-talking with dissolve
        play voice3 stacy_yes2 noloop
        sy "I can help too!"
        if persistent.is_special is True:
            scene d15s08-29 mc-hr-sy-arj-talking with dissolve
            play voice4 hana_yeah2 noloop
            hr "You are his sister... right?"
            play voice3 stacy_mmm1 noloop
            sy "Well, you know... within reason.{w} I'm sure there's something I can do."
    scene d15s08-22 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "I'm sure Hana will be willing to help as needed, right?"
    scene d15s08-21 mc-hr-sy-arj-talking with dissolve
    play voice4 dahlia_thinking_hmm3 noloop
    hr "Yeah... about that."
    scene d15s08-22 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "You're not interested in seeing this through to the finish?"
    scene d15s08-21 mc-hr-sy-arj-talking with dissolve
    play voice4 dahlia_disappointed_ehh2 noloop
    hr "You know I am. {w}You also know you have a virtual stockade of fresh prime meat waiting for another ride on your manhood."
    scene d15s08-22 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "Uh huh."
    scene d15s08-21 mc-hr-sy-arj-talking with dissolve
    play voice4 dahlia_arrogant_yeah noloop
    hr "I'm willing to help, but you're not going to be calling me up for every challenge, right?"
    scene d15s08-22 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Not with that attitude. {w}We want to get and keep the app's attention."
    scene d15s08-05 mc-hr-sy-arj-talking with dissolve
    play voice3 amrose_yes_yap noloop
    arj "We want the app to be connecting [mcname]'s phone as often as possible. It'll give us the best chance to track it."
    scene d15s08-20 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "I'm going to be doing everything I can to get points, with as many people as possible, as often as possible."
    scene d15s08-30 mc-hr-sy-arj-talking with dissolve
    play voice4 dahlia_disappointed_ehh1 noloop
    hr "*sigh* And I suppose that part will include me."
    scene d15s08-29 mc-hr-sy-arj-talking with dissolve
    play voice3 stacy_huh noloop
    sy "Is that a problem?"
    play voice4 dahlia_no_serious noloop
    hr "No. No problem. {w}I just don't want to be taken advantage of."
    scene d15s08-20 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "On my honor, the only person I intend to exploit here is myself."
    scene d15s08-11 mc-hr-sy-arj-talking with dissolve
    play voice4 dahlia_arrogant_hm noloop
    hr "Sounds good.{w} On that note - I'll leave you ladies to work in peace."
    scene d15s08-29 mc-hr-sy-arj-talking with dissolve
    play voice3 stacy_upset1 noloop
    sy "You don't want to stay for a... what's a threesome when there are four people?"
    scene d15s08-09 mc-hr-sy-arj-talking with dissolve
    play voice4 amrose_arrogant_huh2 noloop
    arj "A foursome?"
    scene d15s08-06 mc-hr-sy-arj-talking with dissolve
    play voice3 hana_emm noloop
    hr "Um... no. {w}There are no points in it."
    scene d15s08-12 mc-hr-sy-arj-talking with dissolve
    play voice4 stacy_oh noloop
    sy "Oh, right. Because of the Faraday cage."
    scene d15s08-20 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Still, it's something to consider... that could be a great way to earn points..."
    scene d15s08-23 mc-hr-sy-arj-talking with dissolve
    play voice3 amrose_happy_laugh2 noloop
    arj "Except for one big minor issue."
    play voice2 mc_pain_ou1 noloop
    mc "Right. That."
    scene d15s08-30 mc-hr-sy-arj-talking with dissolve
    play voice4 dahlia_angry_oof noloop
    hr "... I don't want to know, do I?"
    scene d15s08-29 mc-hr-sy-arj-talking with dissolve
    play voice3 stacy_yeahno noloop
    sy "Probably not."
    play voice4 dahlia_thinking_mmm1 noloop
    hr "Let me know when you have that device working. Just text me \"Game on\" or something."
    scene d15s08-31 mc-hr-sy-arj-talking with dissolve
    play voice3 stacy_yes noloop
    sy "Yes, ma'am!"
    hr "..."
    scene d15s08-05 mc-hr-sy-arj-talking with dissolve
    play voice4 amrose_yes_okay2 noloop
    arj "We'll let you know."
    scene d15s08-06 mc-hr-sy-arj-talking with dissolve
    play voice3 dahlia_angry_hm1 noloop
    hr "Thanks."
    scene d15s08-32 mc-hr-sy-arj-talking with dissolve
    hr "Alright. I will be on my way."
    scene d15s08-33 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Take care. {w}Are you feeling okay about this?"
    play voice3 dahlia_disappointed_hmm1 noloop
    hr "Hmm? Yeah, it's just..."
    play voice2 mc_yes_yeah8 noloop
    mc "What is it?"
    scene d15s08-32-03 mc-hr-sy-arj-talkingextra with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    hr "Um, I don't really want to talk about it right now."
    scene d15s08-32-02 mc-hr-sy-arj-talkingextra with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "This is a safe space. In the cage and all that."
    scene d15s08-32-01 mc-hr-sy-arj-talkingextra with dissolve
    play voice3 dahlia_angry_oh noloop
    hr "Oh, okay.{w}.. I've been to your dorm room and know that AmRose has a house."
    hr "So, why do you three all choose to sleep together here?"
    scene d15s08-32-02 mc-hr-sy-arj-talkingextra with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What? No. {w}Stacy was joking about the orgy."
    scene d15s08-32-03 mc-hr-sy-arj-talkingextra with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    hr "Foursome."
    scene d15s08-35 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Right. That was a joke."
    scene d15s08-34 mc-hr-sy-arj-talking with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    hr "Uh huh. {w}Well, it's none of my business."
    scene d15s08-35 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_yes_okay3 noloop
    mc "Have a good night."
    scene d15s08-34 mc-hr-sy-arj-talking with dissolve
    play voice3 nora_aga noloop
    hr "You too."

    play sound ["<silence 0.4>", sfx_door_closed2]
    scene d15s08-36 mc-hr-sy-arj-talking with fade
    mct "Pretty sure that was a distraction. There's something else bothering her."
    play voice4 stacy_laugh noloop
    sy "What took you so long? Did she suck your cock on the way out?"
    scene d15s08-37 mc-hr-sy-arj-talking with dissolve
    play voice3 amrose_old_chmchm noloop
    arj "Stacy!"
    scene d15s08-38 mc-hr-sy-arj-talking with dissolve
    play voice4 stacy_oh2 noloop
    sy "Oh, right. You mentioned..."
    scene d15s08-40 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "AmRose? What did you mention?"
    scene d15s08-41 mc-hr-sy-arj-talking with dissolve
    play voice3 amrose_old_upset noloop
    arj "Just girl talk. {w}Um, now that you're inside the Faraday cage... did anything change?"
    play voice2 mc_thinking_mmm4 noloop
    mc "You mean? No, I'm guessing it needs a signal to unlock."
    scene d15s08-37 mc-hr-sy-arj-talking with dissolve
    play voice4 stacy_huh2 noloop
    sy "You know, it's an electronic lock. I'm sure we could bust that tonight and reattach it before you leave."
    play voice3 amrose_no_uhuh noloop
    arj "Too risky. It might have a record of being unlocked."
    play voice4 stacy_mmm2 noloop
    sy "But I could check the-"
    scene d15s08-39 mc-hr-sy-arj-talking with dissolve
    play voice2 mc_no_no4 noloop
    mc "NO.{w} I appreciate the thought, but I can get through another day or so of this."
    scene d15s08-41 mc-hr-sy-arj-talking with dissolve
    play voice3 amrose_yes_yeah1 noloop
    arj "I agree with [mcname]."
    play voice4 stacy_angryhuh noloop
    sy "Well, okay."
    if date_sy is True:
        scene d15s08-41-01 mc-hr-sy-arj-talkingextra with dissolve
        pause

        $ Lovense.stop()

        scene d15s08-42 mc-hr-sy-arj-talking with dissolve
        $ Lovense.vibrate(2)
        play sound maria_kiss1
        play voice2 mc_pain_mff1 noloop
        mct "What the hell is she doing?! AmRose is right there!"
        play sound maria_kiss2
        play voice4 stacy_moan4 noloop
        scene d15s08-43 mc-hr-sy-arj-talking with dissolve
        pause
        scene d15s08-44 mc-hr-sy-arj-talking with dissolve
        play voice3 amrose_happy_laugh3 noloop
        arj "*giggles*"
        scene d15s08-45 mc-hr-sy-arj-talking with dissolve
        play voice2 mc_scared_huuuh1 noloop
        mc "Stacy?! What the hell was that?!"
        scene d15s08-46 mc-hr-sy-arj-talking with dissolve
        play voice4 stacy_huh noloop
        if persistent.is_special is True:
            sy "What? I can't show a little affection to my brother?"
        else:
            sy "What? I can't show a little affection to my closest friend?"
        scene d15s08-45 mc-hr-sy-arj-talking with dissolve
        play voice2 mc_scared_oh4 noloop
        mc "That felt like more than a little affection!"
        scene d15s08-46 mc-hr-sy-arj-talking with dissolve
        play voice4 stacy_angry noloop
        sy "Maybe I should drop on my knees and suck the life out of your cock cage, then."
        scene d15s08-45 mc-hr-sy-arj-talking with dissolve
        play voice2 mc_surprised_wtf1 noloop
        mc "What the fuck?!"
        $ Lovense.vibrate(1)
        scene d15s08-48 mc-hr-sy-arj-talking with dissolve
        play voice3 amrose_happy_laugh1 noloop
        arj "Relax - I heard all about it."
        scene d15s08-49 mc-hr-sy-arj-talking with dissolve
        play voice2 mc_angry_cough1 noloop
        mc "I repeat - WHAT THE FUCK?!"
        scene d15s08-47 mc-hr-sy-arj-talking with dissolve
        play voice4 stacy_hey noloop
        sy "Of course she knows. AmRose is practically my big sister."
        scene d15s08-48 mc-hr-sy-arj-talking with dissolve
        play voice3 amrose_arrogant_yeah1 noloop
        arj "Except we're both fucking the same guy."
        scene d15s08-50 mc-hr-sy-arj-talking with dissolve
        play voice4 polly_aga noloop
        sy "What are sisters for?"
        play voice3 amrose_happy_laugh6 noloop
        play voice4 stacy_laugh2 noloop
        arj "*laughs*"
        scene d15s08-51 mc-hr-sy-arj-talking with dissolve
        play voice2 mc_disappointed_ah2 noloop
        mc "I'm confused.{w} I'm aroused.{w} And I'm angry."
        mc "Also, being aroused is fucking uncomfortable due to this damn cage."
        scene d15s08-53 mc-hr-sy-arj-talking with dissolve
        play voice3 stacy_oh noloop
        sy "Oh, yeah. AmRose told me about that."
        scene d15s08-52 mc-hr-sy-arj-talking with dissolve
        play voice4 amrose_yes_confident1 noloop
        arj "There are no secrets between sisters."
        scene d15s08-51 mc-hr-sy-arj-talking with dissolve
        play voice2 mc_angry_huh2 noloop
        mc "Fuck the what?!"
        mc "Okay. {w}So now I'm just angry and confused."
        scene d15s08-54 mc-hr-sy-arj-talking with dissolve
        play voice3 amrose_thinking_emm noloop
        arj "I mean, don't get me wrong. At first it was a hell of a shock."
        if persistent.is_special is True:
            arj "I mean, you fucked your sister. {w}You are fucking your sister."
        else:
            arj "I mean, you fucked Stacy. You two are fucking."
        arj "That's pretty shocking. Stacy isn't just another girl. You two are really important to each other."


        scene d15s08-52 mc-hr-sy-arj-talking with dissolve
        play voice3 amrose_thinking_hmm1 noloop
        arj "But, I guess the most surprising part was that I wasn't jealous about it."
        arj "I didn't feel... I don't feel like you would want to exclude me."
        arj "It's not like with Lydia, ya'know? I don't feel like it is a competition."
        scene d15s08-54 mc-hr-sy-arj-talking with dissolve
        play voice3 amrose_old_psst2 noloop
        if cage_ntr is True:
            arj "{i}{b}*whispers*{/b} I don't feel like it's a competition that maybe I'm losing.{/i}"
        else:
            arj "{i}{b}*whispers*{/b} Although, I am starting to like Lydia.{/i}"
        arj "I feel like Stacy and I can share you together."
        play voice2 mc_yes_okay1 noloop
        mc "Okay. I guess I'm cool with that."
        scene d15s08-55 mc-hr-sy-arj-talking with dissolve
        play voice4 stacy_hmm noloop
        sy "[mcname] needs to relax."
        scene d15s08-54 mc-hr-sy-arj-talking with dissolve
        play voice3 amrose_yes_confident1 noloop
        arj "He really does."
        scene d15s08-56 mc-hr-sy-arj-talking with dissolve
        play voice4 stacy_laugh4 noloop
        sy "I can't think of any ways to relax him that wouldn't make him more aroused."
        arj "Good point."
        scene d15s08-57 mc-hr-sy-arj-talking with dissolve
        play voice4 stacy_oh noloop
        sy "Shall we just get ready for bed?"
        play voice3 amrose_yes_yeah1 noloop
        arj "Excellent idea."
        play sound sfx_skirt_off3
        scene d15s08-58 mc-hr-sy-arj-talking with dissolve
        play voice4 stacy_angryhuh noloop
        sy "I always prefer to sleep in the nude."
        scene d15s08-59 mc-hr-sy-arj-talking with dissolve
        play voice3 amrose_thinking_oh1 noloop
        arj "I'm sure that [mcname] prefers that as well."
        play voice4 stacy_huh2 noloop
        sy "[mcname], do you need some help getting undressed?"
        play voice2 d3s7_mcemm noloop
        mc "..."
        play sound sfx_cloth_rustling1
        scene d15s08-60 mc-hr-sy-arj-talking with dissolve
        mc "I can take care of it myself."
        play voice4 stacy_upset1 noloop
        sy "He is no fun."


        play sound sfx_skirt_off2
        scene d15s08-62 mc-hr-sy-arj-talking with dissolve
        play voice2 mc_arrogant_hm3 noloop
        mc "I'm beginning to wonder if I should just go back to my dorm room for the night."
        scene d15s08-61 mc-hr-sy-arj-talking with dissolve
        play voice3 amrose_no_uhuh noloop
        arj "You wouldn't want to miss this. Because we know exactly how to relax you."
        play voice2 mc_thinking_hmm1 noloop
        mc "What's that?"
        play sound sfx_underpants_off1
        scene d15s08-64 mc-hr-sy-arj-talking with dissolve
        play voice3 amrose_thinking_hmm4 noloop
        arj "It starts by you laying down on this bed."
        play voice4 stacy_hmm2 noloop
        sy "Then we lay our naked bodies down."
        play voice3 amrose_old_haha2 noloop
        arj "Curled up on either side of you."
        scene d15s08-63 mc-hr-sy-arj-talking with dissolve
        play voice4 stacy_yes2 noloop
        sy "And then you fall asleep in a pile of warmth and comfort."
        play voice2 mc_arrogant_heh2 noloop
        mc "..."
        play voice2 mc_yes_okay2 noloop
        mc "Okay. That does sound good."

        $ Lovense.stop()

        $ unlock_gallery_slot("cg", "d15s08")
        stop music fadeout 3.0
    else:

        scene black with fade
        pause
        scene d15s08-65 mc-hr-sy-arj-talking with fade
        mct "..."
        scene d15s08-66 mc-hr-sy-arj-talking with dissolve
        play voice3 amrose_old_hey1 noloop
        arj "[mcname]?"
        play voice2 mc_scared_huh3 noloop
        mc "Huh?"
        scene d15s08-67 mc-hr-sy-arj-talking with dissolve
        play voice4 stacy_hmm noloop
        sy "You're falling asleep on your feet."
        scene d15s08-66 mc-hr-sy-arj-talking with dissolve
        play voice3 amrose_yes_ugu noloop
        arj "Why don't you lay down on the bed and get some rest."
        play voice2 mc_yes_yeah1 noloop
        mc "Yeah, yeah. {w}Just a really busy day. I guess I'm a little brain fried."
        play sound sfx_cloth_rustling3
        scene d15s08-68 mc-hr-sy-arj-talking with dissolve
        play voice2 mc_disappointed_ehh3 noloop
        mc "Don't let me nap too long."
        scene d15s08-69 mc-hr-sy-arj-talking with dissolve
        play voice3 amrose_thinking_hmm3 noloop
        arj "Just relax."
        play voice2 mc_arrogant_huh3 noloop
        mc "Don't you two need to sleep?"
        play sound sfx_keyboard_typing1
        scene d15s08-70 mc-hr-sy-arj-talking with dissolve
        play voice4 stacy_mmm1 noloop
        sy "Just a few more lines of code..."
        scene d15s08-69 mc-hr-sy-arj-talking with dissolve
        play voice3 amrose_arrogant_hmm2 noloop
        arj "Don't worry about us. {w}I'm sure you're going to have a busy day tomorrow."
        mct "Oh yeah, tomorrow. {w}Gotta think of some ways to earn points."
        scene d15s08-70 mc-hr-sy-arj-talking with dissolve
        play voice4 stacy_angryhuh noloop
        sy "Hey AmRose, do you think we could wire something to know when he cums?"
        scene d15s08-69 mc-hr-sy-arj-talking with dissolve
        mct "What... what did she just say?"
        play voice3 amrose_thinking_oh2 noloop
        arj "You mean as a trigger for the tracking device?"
        $ unlock_gallery_slot("cg", "d15s08")

        play voice2 mc_disappointed_snoring1 fadein 2.0
        scene d15s08-71 mc-hr-sy-arj-talking with dissolve
        mct "...zzZZZzzzz..."
        stop music fadeout 3.0
        stop voice2 fadeout 3.0

    jump d16s01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
