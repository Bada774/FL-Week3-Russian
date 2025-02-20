label e01s02:

    scene black
    show screen scene_transistion(_("At Subway Station"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_vehicle_escalator fadein 3.0 loop
    scene e01s02-01 mc-sy-talking
    with Fade(0.5, 0.5, 0.9)
    $ renpy.music.set_volume(0.7, 3.0, "music")
    queue music music_sucksexful
    pause
    scene e01s02-02 mc-sy-talking with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Where the fuck are we going?"
    scene e01s02-03 mc-sy-talking with dissolve
    play voice3 polly_impressed noloop
    sy "I told you. It's a surprise."
    scene e01s02-02 mc-sy-talking with dissolve
    play voice2 d1s2_hmm noloop volume 1.8
    mc "It's a surprise that requires we get on the train?"
    scene e01s02-05 mc-sy-talking with dissolve
    play voice3 stacy_no2 noloop
    sy "No, silly. Just riding the metro for a few stops. I promise we'll stay in the same city."
    scene e01s02-04 mc-sy-talking with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, okay."
    stop sound fadeout 5.0
    $ renpy.music.set_volume(1.0, 3.0, "sound2")
    play sound2 subwaystation fadein 3.0 noloop
    scene e01s02-07 mc-sy-talking with fade
    play voice3 stacy_upset1 noloop
    sy "I'm glad you decided to live with me. I was afraid you'd go to AmRose's house."
    scene e01s02-06 mc-sy-talking with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "I hadn't thought of that. She does have a bigger bed..."
    scene e01s02-08 mc-sy-talking with dissolve
    play voice3 stacy_impressed noloop
    sy "What?!"
    scene e01s02-09 mc-sy-talking with dissolve
    play voice2 d4s4_mclaugh noloop
    mc "I'm kidding. You know you're my number one girl."
    mc "You're the only one I want to go to bed with at night and wake up next to in the morning."
    scene e01s02-10 mc-sy-talking with dissolve
    play voice3 stacy_hmm noloop
    sy "I believe you."
    sy "Okay, enough with the mushy stuff. Let me tell you about your surprise!"
    scene e01s02-11 mc-sy-talking with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "I'm all ears. {w}Train it coming!"
    scene e01s02-12 mc-sy-talking with dissolve
    pause
    scene e01s02-13 mc-sy-talking with dissolve
    pause
    stop sound2 fadeout 1.0
    play sound sfx_metro_closed1
    scene e01s02-14 mc-sy-talking with dissolve
    $ renpy.music.set_volume(0.5, 3.0, "sound2")
    play sound2 subwaycar fadein 1.0
    play voice3 stacy_suckmoan3 noloop
    sy "What do you want most in life?"
    scene e01s02-15 mc-sy-talking with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "I have no idea."
    play voice3 stacy_hey noloop
    sy "Of course you do! What would you want to do right now if you weren't doing this?"
    mc "Play some video games and take a nap?"
    scene e01s02-16 mc-sy-talking with dissolve
    play voice3 polly_angry noloop
    sy "Gah! Just..."
    sy "What would you do if you won a few hundred million dollars?"
    scene e01s02-18 mc-sy-talking with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Isn't it supposed to be just a million dollars?"
    play voice3 stacy_yeahno noloop
    play sound sfx_cloth_rustling4 volume 1.5
    scene e01s02-17 mc-sy-talking with dissolve
    sy "Yeah, but if you work a decent job with raises and inflation and all that - I'd be surprised if you don't make a few million before you turn seventy."
    scene e01s02-18-03 mc-sy-talking with dissolve
    play voice2 d1s5_mchappy noloop
    mc "Alright, alright. So, I hit the lotto or go to the casino and hit the jackpot."
    scene e01s02-18-02 mc-sy-talking with dissolve
    play voice3 polly_aga noloop
    sy "Something like that. Enough money that you'll never have to work again."
    scene e01s02-18-04 mc-sy-talking with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "If I'm smart I get a lawyer to accept it for me, buying me a few months before the con artists figure out who I am."
    mc "Every fucking relative will come out of the woodwork asking for a few thousand for something or a few hundred thousand to start their own business."
    mc "Every time I go to the grocery store or whatever I'd have to worry about scam artists trying to fake injuries and sue me."
    play voice2 mc_thinking_hmm1 noloop
    mc "Not to mention all the women I've had sex with who suddenly want something out of me."
    mc "I'd end up secluded in some desert compound having my meals delivered to me by bonded couriers until the million ran out."
    scene e01s02-19 mc-sy-talking with dissolve
    play voice3 stacy_mmm1 noloop
    sy "..."
    sy "Wow."
    scene e01s02-20 mc-sy-talking with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "I'm just saying... it sounds like hell."
    scene e01s02-21 mc-sy-talking with dissolve
    play voice3 stacy_angry noloop
    sy "Let's try this another way. Forget about the windfall income. If you could do anything you want - what would you do?"
    play voice2 mc_arrogant_hm3 noloop
    mc "Exactly what I'm doing."
    sy "Will you take this seriously?"
    scene e01s02-22 mc-sy-talking with dissolve
    play voice2 d2s9_mchey noloop volume 1.3
    mc "Seriously, I've learned that I can do anyone I want. So, that's what I do."
    scene e01s02-23 mc-sy-talking with dissolve
    play voice3 min_happy_relief noloop
    sy "*sigh*"
    play voice2 mc_thinking_mmm5 noloop
    mc "That's why I'm with you."
    sy "Okay, good save, but you're not making this easy."
    scene e01s02-24 mc-sy-talking with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Let's turn those questions around. If you had unlimited wealth and the ability to do anything you wanted to do - what would you do?"
    scene e01s02-29 mc-sy-talking with dissolve
    play voice3 stacy_yes3 noloop
    sy "EXACTLY!!!"
    sy "That's what I'm talking about. Phase two of my master plan."
    scene e01s02-28 mc-sy-talking with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Your master plan? Does it involve computers?"
    scene e01s02-27 mc-sy-talking with dissolve
    play voice3 polly_nouh noloop
    sy "No, not really. You're off track again."
    sy "I do enjoy computers and comp sci stuff, but that's just my backup plan."
    sy "My real passions involve you, me, and your porn stash."
    scene e01s02-26 mc-sy-talking with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Speaking of which - when will I get that back?"
    scene e01s02-23 mc-sy-talking with dissolve
    play voice3 polly_laughter noloop
    sy "As if you need it anymore. Anyway, I've confiscated it for research purposes."
    scene e01s02-22 mc-sy-talking with dissolve
    play voice2 d3s11b_mcheh noloop
    mc "Alright, alright. What was the first part of your master plan."
    scene e01s02-27 mc-sy-talking with dissolve
    play voice3 polly_impressed noloop
    sy "You, of course. Now that you're mine I can move on to the second part."
    scene e01s02-28 mc-sy-talking with dissolve
    play voice2 d2s9_confused noloop volume 1.8
    mc "And that would be... ?"
    scene e01s02-29 mc-sy-talking with dissolve
    play voice3 stacy_yay noloop
    sy "We start our own porn studio!!!"
    scene e01s02-30 mc-sy-talking with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "I don't... we... what?"
    scene e01s02-32 mc-sy-talking with dissolve
    play voice3 fshhh noloop
    sy "Shhhh. Relax your brain and listen."
    scene e01s02-31 mc-sy-talking with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "Uh huh..."
    scene e01s02-34 mc-sy-talking with dissolve
    play voice3 stacy_angryhuh noloop
    sy "As I was saying, we start our own porn studio."
    sy "I'll run everything behind the scenes, but you'll be the star of the show."
    scene e01s02-33 mc-sy-talking with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "Me? A porn star?"
    scene e01s02-36 mc-sy-talking with dissolve
    play voice3 stacy_mmm2 noloop
    sy "Face it, lover. You already are."
    sy "Don't worry about the details. I'll arrange everything."
    sy "Well, almost everything. You'll need to do some things."
    scene e01s02-35 mc-sy-talking with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Like what?"
    scene e01s02-41 mc-sy-talking with dissolve
    play voice3 stacy_oh noloop
    sy "I mean, we'll need cameras, lighting, actresses, film crew, money, and a few other things."
    scene e01s02-37 mc-sy-talking with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "You want me to do all that?"
    scene e01s02-38 mc-sy-talking with dissolve
    play voice3 stacy_nono noloop
    sy "No, like I said, I'll arrange almost everything. We'll have to divide up the work."
    scene e01s02-40 mc-sy-talking with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "I suppose I have a few friends who might be okay with acting..."
    scene e01s02-41 mc-sy-talking with dissolve
    play voice3 stacy_oh2 noloop volume 1.4
    sy "Oh, that's the best part! I have some great leads on new talent."
    scene e01s02-42 mc-sy-talking with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "What kind of leads?"
    if d20s08_copy_files is True:
        scene e01s02-43 mc-sy-talking with dissolve
        play voice3 polly_wooh noloop
        sy "This is why I copied the Fetish Locator data."
        scene e01s02-44 mc-sy-talking with dissolve
        play voice2 mc_yes_aga1 noloop
        mc "AmRose is still pretty pissed about that."
        scene e01s02-45 mc-sy-talking with dissolve
        play voice3 stacy_huh2 noloop
        sy "Don't get me wrong - I enjoy watching the photos and videos that people submitted."
        scene e01s02-46 mc-sy-talking with dissolve
        play voice2 mc_thinking_hmm4 noloop
        mc "I wouldn't mind seeing more of those... but it's wrong, isn't it?"
        scene e01s02-47 mc-sy-talking with dissolve
        play voice3 polly_mmmuhuh noloop
        sy "I mean, that's great for jilling off, but the real value is in the metadata."
        scene e01s02-48 mc-sy-talking with dissolve
        play voice2 mc_surprised_huh6 noloop
        mc "Huh?"
        scene e01s02-49 mc-sy-talking with dissolve
        play voice3 stacy_hmm noloop
        sy "The metadata. Who did what. Where they did it. What they did. That kinda thing."
        scene e01s02-50 mc-sy-talking with dissolve
        play voice2 d2s12_emmm noloop
        mc "But we all used pseudonyms and I assume some players used masks or-"
        scene e01s02-45 mc-sy-talking with dissolve
        play voice3 stacy_yeahno noloop
        sy "Yes, but say you knew that there was someone at a particular office or bar or even a classroom..."
        sy "And that person did a specific fetish that you wanted..."
        sy "I might not be able to tell you who did it, but if you went there-"
        scene e01s02-46 mc-sy-talking with dissolve
        play voice2 mc_thinking_hmm3 noloop
        mc "I might be able to recognize the person some other way."
        scene e01s02-47 mc-sy-talking with dissolve
        play voice3 min_yes_ugu noloop
        sy "Precisely."
    elif cage_ntr is False:
        scene e01s02-47 mc-sy-talking with dissolve
        play voice3 stacy_hmm noloop
        sy "Do you remember what Lydia said about social nexii?"
        scene e01s02-48 mc-sy-talking with dissolve
        play voice2 mc_surprised_huh6 noloop
        mc "Social nexus? Vaguely. It sounded like some science fiction philosophy."
        scene e01s02-49 mc-sy-talking with dissolve
        play voice3 stacy_yeahno noloop
        sy "I mean, yeah, but the general idea is pretty good."
        sy "I think I can identify places where sexual people get together."
        scene e01s02-50 mc-sy-talking with dissolve
        play voice2 mc_arrogant_heh2 noloop
        mc "What? Like strip clubs?"
        scene e01s02-45 mc-sy-talking with dissolve
        play voice3 polly_nouh noloop
        sy "Nah. I thought about that, but the data said no."
        scene e01s02-46 mc-sy-talking with dissolve
        play voice2 mc_thinking_hmm4 noloop
        mc "What data?"
        scene e01s02-43 mc-sy-talking with dissolve
        play voice3 stacy_mmm1 noloop
        sy "I've been doing some research online, cross referencing various databases..."
        scene e01s02-44 mc-sy-talking with dissolve
        play voice2 mc_surprised_what2 noloop
        mc "You created what... some sort of locator for particular fetishes?"
        scene e01s02-41 mc-sy-talking with dissolve
        play voice3 min_happy_relief noloop
        sy "Yeah. It's a shame that name was already taken."
    else:
        scene e01s02-43 mc-sy-talking with dissolve
        play voice3 polly_wooh noloop
        sy "This is why I wish you had let me copy the Fetish Locator database."
        scene e01s02-44 mc-sy-talking with dissolve
        play voice2 mc_thinking_hmm4 noloop
        mc "You did, didn't you?"
        scene e01s02-45 mc-sy-talking with dissolve
        play voice3 min_yes_ugu noloop
        sy "Mostly."
        scene e01s02-35 mc-sy-talking with dissolve
        play voice2 mc_angry_errr4 noloop
        mc "Stacy!"
        scene e01s02-36 mc-sy-talking with dissolve
        play voice3 stacy_hey noloop
        sy "I got rid of anything that could be used against anyone."
        scene e01s02-37 mc-sy-talking with dissolve
        play voice2 mc_disappointed_ehh1 noloop
        mc "AmRose is going to be pissed when she finds out."
        scene e01s02-47 mc-sy-talking with dissolve
        play voice3 stacy_angryhuh noloop
        sy "All the photos and videos and player info was wiped and overwritten. I swear!"
        scene e01s02-46 mc-sy-talking with dissolve
        play voice2 mc_thinking_hmm3 noloop
        mc "So, what did you keep?"
        scene e01s02-49 mc-sy-talking with dissolve
        play voice3 stacy_hmm noloop
        sy "The metadata. Locations. Vague information. Nothing that could be traced back to a single person."
        scene e01s02-50 mc-sy-talking with dissolve
        play voice2 mc_angry_huh1 noloop
        mc "Why would you keep that?"
        scene e01s02-39 mc-sy-talking with dissolve
        play voice3 stacy_mmm1 noloop
        sy "I couldn't just let it all go. I need that data for what I have planned next."
    scene e01s02-40 mc-sy-talking with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "So, what exactly are you proposing?"
    play sound sfx_cloth_rustling2 volume 1.6
    scene e01s02-51 mc-sy-talking with dissolve
    play voice3 stacy_suckmoan1 noloop
    sy "We work together on our own Porn Studio. I identify locations where you should go to meet people, and you do your magic."
    scene e01s02-52 mc-sy-talking with dissolve
    pause
    scene e01s02-54 mc-sy-talking with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "My magic?"
    scene e01s02-55 mc-sy-talking with dissolve
    play voice3 polly_aga noloop
    sy "You do that voodoo that you do so well."
    scene e01s02-56 mc-sy-talking with dissolve
    play voice2 mc_happy_a1 noloop
    mc "What are you talking about, babe?"
    scene e01s02-59 mc-sy-talking with dissolve
    play voice3 stacy_laugh4 noloop
    sy "We do almost everything together, but I identify prospective actresses and then you seduce and encourage them to have sex with you... and we film it."
    scene e01s02-60 mc-sy-talking with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "You want us to do what?!"
    scene e01s02-61 mc-sy-talking with dissolve
    pause
    play voice3 stacy_suckmoan2 noloop
    scene e01s02-63 mc-sy-talking with dissolve
    pause
    play sound sfx_kick_leg1
    scene e01s02-64 mc-sy-talking with vpunch
    play voice2 d9s5_auch2 noloop
    mc "We are NOT going to film sex scenes without their knowledge!!! That's horrible!!!"
    scene e01s02-65 mc-sy-talking with dissolve
    play voice3 stacy_angry noloop
    sy "I didn't say anything like that. Of course we'd have them agree on pseudonyms and get consent forms."
    scene e01s02-66 mc-sy-talking with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh. Maybe that's not so bad then, but I still feel like... I dunno..."
    scene e01s02-67 mc-sy-talking with dissolve
    play voice3 polly_laughter noloop
    sy "Like you're the bait and I'm the fisherman?"
    play voice2 d1s5_mcthinks noloop volume 1.6
    mc "Fisherwoman? Fisherperson? Fisher Gal? Fishgal?"
    scene e01s02-68 mc-sy-talking with dissolve
    play voice2 d2s9_confused noloop volume 1.4
    mc "Anyway, what were we talking about?"
    scene e01s02-69 mc-sy-talking with dissolve
    play voice3 stacy_huh2 noloop
    sy "Remember your porn collection - we could do that together!"
    scene e01s02-70 mc-sy-talking with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "Didn't we do that this morning?"
    scene e01s02-71 mc-sy-talking with dissolve
    play voice3 stacy_yeahno noloop
    sy "Yes, but with professional equipment, a real photographer, multiple actresses!"
    scene e01s02-72 mc-sy-talking with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "That's a good idea. There are so many fetishes, but they aren't really mainstream."
    scene e01s02-73 mc-sy-talking with dissolve
    play voice3 stacy_yes2 noloop
    sy "Exactly, we can be the one stop shopping for people of all fetish flavors!"
    scene e01s02-74 mc-sy-talking with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "And if we could put them all together we could create some sort of Magnum Opus."
    scene e01s02-75 mc-sy-talking with dissolve
    play voice3 stacy_oh2 noloop
    sy "Now there's an idea. The Citizen Kane of porn."
    scene e01s02-76 mc-sy-talking with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mc "*chuckle* Maybe we could even win best picture AND an eXXXstacy award."
    scene e01s02-77 mc-sy-talking with dissolve
    play voice3 polly_impressed noloop
    sy "There you go. We have our stretch goal."
    play voice2 d1s2_hmm noloop volume 1.5
    mc "My porn collection inspired you to do all this?"
    sy "Well, when I was watching it, I was imagining us doing all of those things."
    scene e01s02-68 mc-sy-talking with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "I see, so you have that all planned out."
    scene e01s02-73 mc-sy-talking with dissolve
    play voice3 stacy_upset1 noloop
    sy "Do you mind?"
    scene e01s02-84 mc-sy-talking with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Mind? It sounds awesome."
    mc "I love you."
    scene e01s02-85 mc-sy-talking with dissolve
    play voice3 polly_yes1 noloop
    sy "I love you too!"
    $ unlock_gallery_slot("cg", "e01s02")
    scene e01s02-86 mc-sy-talking with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "But seriously, where are we really going?"
    scene e01s02-87 mc-sy-talking with dissolve
    play voice3 stacy_oh noloop
    sy "You must have figured out the surprise by now."
    scene e01s02-88 mc-sy-talking with dissolve
    play voice2 d1s5b_emmm noloop volume 1.6
    mc "You don't mean...?"

    stop sound2 fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.5, "music")
    play sound sfx_camera_fly1 volume 2.0
    jump e01s02_end

label e01s02_end:

    scene ending_01_art with Fade(1.25, 1.0, 1.75, color="#fff")
    pause
    call end_game_text (_("You have finished Ending #01!")) from _call_end_game_text_3
    call end_game_text (_("Stacy and [mcname] will return!")) from _call_end_game_text_4
    call end_game_text (_("In Fetish Locator: S&M Studio!")) from _call_end_game_text_5
    $ persistent.finished_e01 = True
    $ fl_achievement_unlock("e01_finish")

    stop music fadeout 3.0
    jump end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
