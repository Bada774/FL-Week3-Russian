image e08s03-a46-glambot-1 = Movie(play = "images/E-08/s03/anim/e08s03-a46-2x-50fps.webm", start_image = "e08s03-a46 arj-mc-compare-sex-in-tornado-to-oz-glambot-46-00_i", image = "e08s03-a46 arj-mc-compare-sex-in-tornado-to-oz-glambot-46-78_i", loop = False)

image e08s03_lighting_storm:
    "e08s03-20-01 arj-screams-another-lightning-flashes-no-lightning_c1" with hpunch
    pause (0.2)
    "e08s03-20 arj-screams-another-lightning-flashes_c1" with hpunch
    pause (0.3)
    "e08s03-20-01 arj-screams-another-lightning-flashes-no-lightning_c1" with dissolve

image e08s03_lighting_storm2:
    "e08s03-35-01 loud-thunder-strikes-mc-arj-lit-rj-gets-anxious-no-lightning_c1" with dissolve
    pause (0.4)
    "e08s03-35 loud-thunder-strikes-mc-arj-lit-rj-gets-anxious_c1" with hpunch
    pause (0.3)
    "e08s03-35-01 loud-thunder-strikes-mc-arj-lit-rj-gets-anxious-no-lightning_c1" with dissolve

image e08s03_lighting_storm3:
    "e08s03-73-01 mc-arj-lighted-by-lightning-no-lightning_c1" with hpunch
    pause (0.22)
    "e08s03-73 mc-arj-lighted-by-lightning_c1" with hpunch
    pause (0.3)
    "e08s03-73-01 mc-arj-lighted-by-lightning-no-lightning_c1" with dissolve

label e08s03:

    scene black
    show screen scene_transistion(_("One late afternoon"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.0, 0.0, "sound4")
    $ renpy.music.set_volume(0.3, 0.0, "sound5")
    $ renpy.music.play(audio.sfx_weather_tornado1, "sound4" , True, None, True, 1.0)
    $ renpy.music.play(audio.sfx_weather_tornado1_muffled, "sound5", True, None, True, 24.0)
    scene e08s02-01 mc-arj-clean-prepare-barn_c1
    play sound ["<silence 0.5>", sfx_bath_out1]
    with Fade(0.5, 0.5, 0.9)
    pause
    scene e08s02-02 mc-could-really-use-a-shower_c1 with dissolve
    play voice2 mc_disgust_ooh2 noloop
    mc "I could really use a shower."
    scene e08s02-03 mc-brought-equipment-inside-except-fly-traps_c1 with dissolve
    play voice3 amrose_yes_yeah2 noloop
    arj "We're almost done."
    arj "Did you remember to bring all the farm equipment inside?"
    scene e08s02-02 mc-could-really-use-a-shower_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Most of it. I still have to clear the fly traps, I'll do that tomorrow."
    mc "The more important question is, did you decide on what you want to watch today?"
    play sound sfx_cleaning_floor2 fadein 1.5
    scene e08s02-04 arj-doesnt-know-why_c1 with dissolve
    play voice3 amrose_happy_laugh1 noloop
    arj "I was looking for something to watch, it feels like we've seen everything already."
    play voice2 mc_yes_aga1 noloop
    mc "It's because we can't ever decide what to watch, so I turn on a nature documentary, and we watch it for twenty minutes before passing out."
    play voice3 amrose_yes_yeah4 noloop
    arj "Yeah, I don't know why."
    arj "It mostly happens when they show underwater footage, all those marble blue contrasts takes me out."
    stop sound fadeout 1.0
    scene e08s02-05 mc-suggest-living-creek-farm-be-diff_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Farm life must be different near a creek, right?"
    play voice3 amrose_thinking_hmm1 noloop
    arj "It's probably way harder."
    mc "Really? I imagined it'd be quite enjoyable, you know, even avoiding the temptation of taking a swim."
    arj "Ah, come on, you're getting distracted."
    scene e08s02-06 arj-hands-mc-toolbox_c1 with dissolve
    play voice3 amrose_arrogant_hmm2 noloop
    arj "Put all the tools in here."
    arj "Then we're done for the day."
    play sound sfx_bandage_off1
    $ renpy.music.set_volume(1.0, 4.0, "music")
    play music music_ruthless_nature fadein 5.0
    scene e08s02-07 mc-arj-leave-barn_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.4, 3.5, "sound4")
    $ renpy.music.set_volume(0.0, 1.5, "sound5")
    scene e08s03-08 mc-picking-tools-outside-barn_c1 with dissolve
    pause
    scene e08s03-09 mc-tells-arj-outside-mess-asks-dog_c1 with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "It's a real mess out here."
    mc "We should really finish up quick. Where's the dog?"
    play sound ["<silence 0.4>", sfx_horror_message1] volume 1.5
    scene e08s03-10 mc-gets-storm-alert_c1 with dissolve
    pause
    play voice3 amrose_hey_attention noloop
    arj "Remy! Are you in the house?"
    scene e08s03-11 mc-sees-alert-phone-arj-gets-worried_c1 with dissolve
    play voice3 amrose_arrogant_huh2 noloop
    arj "What is it?"
    play voice2 mc_angry_huh2 noloop
    mc "Storm's approaching."
    mc "Says we should get inside."
    scene e08s03-12 arj-calls-remy_c1 with dissolve
    play voice3 amrose_surprised_ahh3 noloop
    arj "Remy!"
    play sound dog_bark6
    queue sound dog_growl1
    scene e08s03-13 rj-runs-back-in-barn_c1 with dissolve
    play voice3 amrose_disappointed_oh5 noloop
    arj "She's scared of storms."
    play voice2 mc_yes_yeah5 noloop
    mc "So scared, she didn't even bother getting in the house."
    scene e08s03-14 arj-explains-rj-afraid-storms_c1 with dissolve
    play voice3 amrose_surprised_huh3 noloop
    arj "How severe is the storm, does it say?"
    scene e08s03-15 tells-storm-will-be-bad- lightning-flashes_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Pretty sure it's going to be okay, although it's warning of very strong winds."
    mc "Guessing it's a tornado."
    play voice3 amrose_arrogant_huh1 noloop
    arj "Tornado?"
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah."
    scene e08s03-16 arj-tells-they-have-to-board-barn-windows_c1 with dissolve
    play voice3 amrose_disappointed_oh1 noloop
    arj "We need to board up the barn then, and hope it doesn't get damaged too badly."
    play voice2 mc_yes_yes3 noloop
    mc "Alright, you get me the boards, I'll start boarding up the windows."
    play sound ["<silence 0.4>", sfx_hammer_loop1]
    scene e08s03-17 arj-helps-mc-bar-the-barn_c1 with fade
    pause
    scene e08s03-18 mc-asks-arj-barn-or-house_c1 with dissolve
    play voice2 mc_yes_okay2 noloop volume 1.7
    mc "Okay, so should we stay in the barn or go back in the house?"
    play voice3 amrose_thinking_emm noloop
    arj "I don't know. It's my first experience dealing with a tornado."
    arj "I'm trying my hardest not to freak out right now."
    scene e08s03-19 mc-tells-arj-will-be-fine-go-barn-before-sucked_c1 with dissolve
    play voice2 mc_no_no2 noloop
    mc "No, it's going to be fine. We should go in the barn now, though. Before we get sucked in."
    play sound sfx_thunder_2 volume 0.8
    scene e08s03_lighting_storm
    play voice3 amrose_surprised_ahh2 noloop volume 1.8
    arj "Ahh!!!"
    queue voice3 amrose_pain_sobs5 noloop
    scene e08s03-21 arj-rushes-scared-into-barn-mc-follows-her-thinking_c1 with hpunch
    pause
    play voice2 d1s1_mmm noloop volume 1.5
    mct "Maybe not the best thing to say when someone tells you they're terrified..."
    stop voice3 fadeout 1.0
    $ renpy.music.set_volume(0.0, 1.5, "sound4")
    $ renpy.music.set_volume(0.7, 1.5, "sound5")
    $ renpy.music.set_volume(0.5, 8.0, "music")
    play sound sfx_door_slide2 volume 2.5
    scene e08s03-22 mc-closes-barn-door_c1 with dissolve
    pause
    play sound sfx_door_slide4
    scene e08s03-23 arj-holds-rj-asks-mc-will-be-fine_c1 with dissolve
    play voice3 amrose_disappointed_ehh2 noloop
    queue sound dog_moan1
    arj "It's going to be okay."
    arj "Right, [mcname]?"
    scene e08s03-24 mc-prepared-emergency-kit_c1 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "I hope so."
    mc "Thankfully we prepared for this. Little emergency kit with a water, flashlight, batteries, and energy bars."
    play voice3 amrose_arrogant_huh4 noloop
    arj "Didn't we do that like months ago?"
    play sound3 dog_breath2 noloop
    play sound sfx_bag_fall1
    scene e08s03-25 mc-arj-talk-about-water-in-kit_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Does bottled water have an expiration date?"
    play voice3 amrose_yes_ugu noloop
    arj "Surely it does."
    play sound sfx_paper_bag_2
    scene e08s03-26 mc-opens-kit-takes-out-flashlight_c1 with dissolve
    play voice2 mc_pain_ou1 noloop
    mc "Oh no."
    play voice3 amrose_surprised_uh3 noloop
    arj "What, oh no?"
    play sound sfx_flashlight_on1
    scene e08s03-27 mc-says-oh-no-flashlight-not-working_c1 with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "Flashlight isn't working."
    play voice3 amrose_thinking_hmm4 noloop
    arj "Well, your phone's still good, right?"
    mc "I think so. Not getting any reception, but it should be enough charge to last us a day or two."
    play sound dog_moan2
    scene e08s03-28 arj-asks-if-phone-light-still-good_c1 with dissolve
    pause
    scene e08s03-29 mc-was-about-to-shower_c1 with dissolve
    play voice2 d1s5b_ehhh noloop
    mc "Just when I wanted to shower."
    mc "I'll probably have to step out in the rain to wash."
    play voice3 amrose_arrogant_huh3 noloop
    arj "How long have you gone without showering?"
    scene e08s03-30 arj-showers-everyday_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "Like in a row?"
    play voice3 amrose_arrogant_yeah1 noloop
    arj "I take a bath every day."
    mc "I try and do it every day, but sometimes it doesn't work out. Exegient circumstances."
    scene e08s03-31 arj-shower-diff-from-bathing_c1 with dissolve
    play voice3 amrose_arrogant_hmm1 noloop
    arj "Taking a shower is different from bathing."
    scene e08s03-32 mc-thinks-bath-too-steamy_c1 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "I bathe every once in a while. I don't like spending too much time in there."
    play sound sfx_hair_scratch1
    scene e08s03-33 arj-asking-whats-wrong-with-thinking-pets-dog_c1 with dissolve
    play voice3 amrose_thinking_oh2 noloop
    arj "Why not?"
    scene e08s03-34 mc-thinks-arj-takes-baths-too-often_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "I don't know. It's too hot and steamy. I just want to wash up."
    mc "You spend too much time in there and you start thinking about all sorts of stuff, you know."
    mc "The sound of the water running, it's like after a while, you start meditating."
    scene e08s03-33 arj-asking-whats-wrong-with-thinking-pets-dog_c1 with dissolve
    play voice3 amrose_yes_questioning noloop
    arj "What's wrong with that?"
    scene e08s03-34 mc-thinks-arj-takes-baths-too-often_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Who wants to spend time thinking about things?"
    play voice3 amrose_old_chmchm noloop
    arj "I do that."
    mc "Yeah, but you do that all the time, apparently. If I do it once in a while, fine, but spend too much time alone, you start blending into the environment, you know what I mean?"
    arj "It's not so bad."
    play sound sfx_thunder_1
    scene e08s03_lighting_storm2
    pause 0.7
    scene e08s03-36 mc-searches-for-light-on-his phone_c1 with fade
    play voice3 amrose_pain_sobs1 noloop
    arj "I take that back."
    play voice2 mc_arrogant_heh3 noloop
    mc "*laughs* Yeah."
    arj "I really hope that wasn't the roof that just got blown off."
    scene e08s03-37 mc-worried-about-roof-too_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, that's the thing that worries me. Structurally it should be fine, this is a relatively new barn, it's not like those ones that aren't maintained."
    mc "And the rain, it's a good thing we have a drainage hole because the whole barn would be filled with water."
    scene e08s03-38 arj-thinks-bad-thing-pile-up-mc-put-phone-down-for-light_c1 with dissolve
    play voice3 amrose_disappointed_ehh1 noloop
    arj "I don't underestimate this getting worse."
    arj "Do you ever stop and think about when things are hard, it's because everything starts piling up all at once?"
    arj "It'd be easy if it was just the storm, but no, none of our flashlights work, the roof might collapse, and the water might drown us all."
    play sound3 sfx_phone_button1 noloop
    scene e08s03-39 mc-phone-light-up-floor-mc-arj-discuss-karma_c1 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "This is like the real life version of finals week. Karma is cramming in all the shit we can't handle in one go."
    play voice3 amrose_old_huh2 noloop
    arj "Karma?"
    mc "That's what you call it, right?"
    arj "What do you mean? Like we deserved it or something?"
    scene e08s03-40 arj-asks-what-sins-mc-committed_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Kinda?"
    play voice3 amrose_surprised_uh4 noloop
    arj "Did you commit any sins that would warrant divine intervention?"
    play voice2 mc_no_no5 noloop
    mc "I didn't mean it like that, I was just adding to your observation. Bad things happen right, even if you don't deserve it. Is that still called karma, or something else?"
    mc "I don't really know what I'm saying, forget it."
    arj "Mhmm..."
    scene e08s03-41 arj-asking-time-cant-believe-its-only-five_c1 with dissolve
    play voice3 amrose_hey_whisper noloop
    arj "What time is it now?"
    scene e08s03-42 mc-points-out-phone-useless-no-wifi_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Would you believe it, it's only five."
    play voice3 amrose_happy_mmm noloop
    arj "Wow."
    play voice2 mc_angry_hm1 noloop
    mc "The internet isn't working, so this phone is pretty much useless."
    mc "Somehow even with this technology, we're no different than cavemen at this point."
    play voice3 amrose_thinking_hmm1 noloop
    arj "Do you still have Fetish Locator installed? The app?"
    scene e08s03-43 mc-thinks-arj-jokes-about-having-fl-still-installed_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mc "That's funny."
    mc "After what you told me about your experience with Fetish Locator, it'd be a crime to still have it installed."
    play voice3 amrose_arrogant_huh1 noloop
    arj "You didn't have any positive experiences with it?"
    scene e08s03-44 mc-fl-phase-in-life-arj-agrees_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "I did, but I don't think about it fondly. It was just a phase in my life that's over now."
    play voice3 amrose_yes_yap noloop
    arj "That's a good way to put it."
    scene e08s03-45 mc-tells-sex-in-tornado-would-be-hundreds-points_c1 with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Can you imagine if that thing was still going on? What would today's challenge, having sex in the eye of a tornado, five hundred points."
    scene e08s03-46 arj-mc-compare-sex-in-tornado-to-oz_c1 with dissolve
    play voice3 amrose_happy_laugh3 noloop
    arj "I doubt anyone has ever dared to do that."
    scene e08s03-a46 arj-mc-compare-sex-in-tornado-to-oz-glambot-46-00_i with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.6
    mc "Why not? People have sex while jumping out of planes. That's going in the reverse direction."
    mc "What would having sex be like in that instance, would you even know what's going on, if you had sex in a tornado?"
    play sound sfx_camera_fly1
    scene e08s03-a46-glambot-1
    pause
    play voice3 amrose_disappointed_oh3 noloop
    arj "I imagine you'd get transported to Oz."
    arj "Remy would be Toto, I'd be Dorothy, and you'd be..."
    play voice2 mc_happy_hah1 noloop
    mc "In the Lollipop Guild."
    scene e08s03-47 arj-scared-from-lollipop-guild_c1 with dissolve
    play voice3 amrose_thinking_oh1 noloop
    arj "Those guys used to scare me."
    play voice2 mc_happy_a1 noloop
    mc "Come on, they're harmless."
    scene e08s03-48 arj-still-wouldnt-do-it-mc-thinks-they-can-work-up_c1 with dissolve
    play voice3 amrose_thinking_hmm2 noloop
    arj "Well, still, I don't think I could complete that challenge, not in a million years."
    play voice2 mc_hey_hey3 noloop
    mc "We can work up to it."
    mc "First, tornadoes, then hurricanes, categories one-five, then, what's after hurricanes?"
    scene e08s03-49 arj-surprised-mc-asked-said-death_c1 with dissolve
    play voice3 amrose_arrogant_huh4 noloop
    arj "Death?"
    play voice2 d9s2_yeah noloop volume 2.2
    mc "If we want to be realistic, death probably comes first."
    mc "Which is also what we're waiting for."
    scene e08s03-50 arj-scared-waiting-for-death_c1 with dissolve
    play voice3 amrose_disappointed_oh5 noloop
    arj "Waiting for Death. It's like Waiting for Godot, except death actually appears."
    play voice2 d1s2_hmm noloop volume 1.5
    mc "Are you really that scared? I really don't think we're going to die. If I scared you earlier, I'm sorry."
    scene e08s03-51 arj-worries-they-might-stay-the-night-here-mc-tells-her-it-be-fine_c1 with dissolve
    play voice3 amrose_no_simple2 noloop
    arj "It's not your fault. I don't know how I'm feeling, to be honest."
    arj "Mostly worrying, because I don't know when this is going to end. We have to stay in here until the storm ends."
    play voice2 mc_thinking_hmm5 noloop
    mc "We're going to be okay, I promise."
    play sound sfx_cloth_rustling2
    scene e08s03-52 mc-arj-hug-each-other-sit-by-light-in-silence_c1 with dissolve
    pause
    scene e08s03-53 mc-asks-arj-about-kids_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "Ever think about having kids?"
    play voice3 amrose_arrogant_huh3 noloop
    arj "Kids?"
    mc "You know, sanctifying our marriage with the birth of the next generation."
    scene e08s03-54 arj-reminds-mc-they-talked-about-it_c1 with dissolve
    play voice3 amrose_yes_yeah2 noloop
    arj "Yeah, we talked about it. We talked about it, how we'd like to have children in the future."
    arj "We haven't made any specific plans."
    play voice2 mc_yes_yes1 noloop
    mc "Too busy setting up our living space."
    scene e08s03-55 mc-tells-mc-will-be-hard-taking-care-of-children_c1 with dissolve
    play voice3 amrose_thinking_hmm3 noloop
    arj "It's going to be difficult, taking care of the children, and tending to the farm."
    play voice2 mc_yes_yeah2 noloop
    mc "For a couple of years, yeah."
    mc "When they grow up, we would have some extra hands to help us."
    scene e08s03-56 arj-asks-how-many-kids-mc-expects_c1 with dissolve
    play voice3 amrose_surprised_uh5 noloop
    arj "They? How many are you expecting?"
    play voice2 mc_thinking_mmm2 noloop
    mc "I don't know. I want a big family."
    scene e08s03-57 mc-tells-arj-hes-youngest-of-five_c1 with dissolve
    mc "It's not something you really see anymore, because of economic sustainability."
    play voice3 amrose_happy_laugh2 noloop
    arj "I'm the youngest of five siblings."
    play voice2 mc_surprised_what1 noloop
    mc "How come I never met them?"
    scene e08s03-58 mc-tells-arj-hed-remember-meeting-siblings_c1 with dissolve
    play voice3 amrose_hey_active2 noloop
    arj "You met them."
    play voice2 mc_no_uhuh1 noloop
    mc "I would remember it if I did."
    scene e08s03-59 arj-talks-downsides-of-many-siblings_c1 with dissolve
    play voice3 amrose_happy_mmm noloop
    arj "Having a big family has its upsides and downsides."
    arj "One upside is you'll never be alone."
    arj "The downside is, you'll never be left alone."
    play voice2 mc_yes_yeah7 noloop
    mc "What's wrong with that?"
    arj "Won't you miss our movie nights?"
    scene e08s03-60 arj-worried-movienights-mc-tells-they-will-still-have-moments_c1 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "We can still have our moments, right?"
    mc "It won't be just..."
    scene e08s03-61 mc-starring-the-walls_c1 with fade
    pause
    scene e08s03-62 arj-talks-benefits-being-alone_c1 with dissolve
    play voice3 amrose_thinking_hmm5 noloop
    arj "Being alone has its benefits, you know?"
    arj "Did you always have a girlfriend?"
    scene e08s03-63 arj-asking-mc-if-lonely-when-single_c1 with dissolve
    play voice2 d9s3_no noloop volume 1.5
    mc "No."
    play voice3 amrose_arrogant_yeah2 noloop
    arj "Were you lonely?"
    scene e08s03-64 mc-doesnt-really-remember-life-before-college_c1 with dissolve
    play voice2 mc_arrogant_hm2 noloop
    mc "I wouldn't say I was lonely."
    mc "I don't really remember what I was before going to college. I hung around with friends, and when I was at home, I spent time playing games."
    play voice3 amrose_arrogant_hmm2 noloop
    arj "So you never felt that way?"
    scene e08s03-65 mc-was-in-good-state-of-mind-asks-arj-same_c1 with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "I did, but it wasn't so scary. I was in a good state of mind."
    mc "How about you?"
    scene e08s03-66 arj-doesnt-know-where-would-be-without-mc_c1 with dissolve
    play voice3 amrose_disappointed_ehh2 noloop
    arj "Meh."
    arj "As I said, if I didn't meet you... I don't know where I'd be."
    scene e08s03-67 arj-looks-despondent-not-in-mc_c1 with dissolve
    arj "I poured myself entirely into my work, that I never really thought about having a boyfriend, or finding someone to be with."
    arj "I was really missing out, as it turns out."
    play voice2 mc_thinking_hmm2 noloop
    mc "What do you mean?"
    scene e08s03-68 arj-tries-to-describe-it-but-its-hard_c1 with dissolve
    play voice3 amrose_thinking_emm noloop
    arj "It's like, I don't know how to describe it. It's like having an invisible wound, and that only other people can see it."
    arj "Some poet said youth is wasted on the young. I understand why they said that. I didn't even know what was wrong with me."
    scene e08s03-69 arj-tries-to-explain-mc-gets-what-shes-trying-to-say_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "There was nothing wrong with you. That's just a part of growing up."
    play voice3 amrose_arrogant_hmm1 noloop
    arj "Not like I was expressing an inexpressible thought. Just articulating my thoughts, or failing to."
    mc "It's okay. I get what you're trying to say."
    scene e08s03-68 arj-tries-to-describe-it-but-its-hard_c1 with dissolve
    play voice3 amrose_thinking_hmm2 noloop
    arj "How many children were you thinking of having with me?"
    scene e08s03-70 mc-wants-at-least-five-kids_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "At least five."
    scene e08s03-71 arj-not-sure-if-they-can-support-five-children_c1 with dissolve
    play voice3 amrose_surprised_huh1 noloop
    arj "Five?"
    scene e08s03-69 arj-tries-to-explain-mc-gets-what-shes-trying-to-say_c1 with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "It's my lucky number."
    scene e08s03-67 arj-looks-despondent-not-in-mc_c1 with dissolve
    play voice3 amrose_surprised_uh2 noloop
    arj "Can we support that much?"
    arj "I doubt we're making a windfall in terms of profit, right?"
    scene e08s03-72 mc-reminds-arj-they-can-ask-neighbours_c1 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "We'll make it work."
    mc "And if not, we can always ask the neighbors."
    play sound sfx_thunder_1
    play voice3 amrose_surprised_oh1 noloop
    scene e08s03_lighting_storm3
    pause
    play voice2 d2s9_mchey noloop
    mc "Come on, let's keep talking."
    scene e08s03-74 arj-getting-really-scared_c1 with dissolve
    play voice3 amrose_angry_breath2 noloop
    arj "I'm getting really scared."
    play voice2 mc_yes_aga2 noloop
    mc "It'll pass."
    scene e08s03-75 arj-asking-mc-if-he-is-scared_c1 with dissolve
    play voice3 amrose_arrogant_huh2 noloop
    arj "Aren't you a little scared?"
    play voice2 mc_disappointed_ah2 noloop
    mc "More than a little scared."
    arj "..."
    scene e08s03-76 mc-tells-arj-they-made-it-this-far_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "We made it this far, right? I find it difficult something would happen to us right now, when we're talking about children."
    mc "That would be the ultimate irony."
    play voice3 amrose_yes_ugu noloop
    arj "I suppose."
    scene e08s03-77 mc-insists-not-joking_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "I'm not joking. We have known each other for a long time."
    mc "And whatever happened, throughout it all, we ended up together."
    mc "We both decided, all the choices we made, it would be to ensure we were here right here, right now, in this barn, having this conversation."
    play voice3 amrose_surprised_ahh2 noloop
    play voice2 mc_scared_huh3 noloop
    play sound sfx_thunder_2 volume 0.8
    scene e08s03-78 lightning-strikes-debris-collapse-from-roof_c1 with vpunch
    play sound3 sfx_other_rooftop_down1 noloop
    pause
    scene e08s03-79 mc-arj-crawl-back-from-debris-embraces-shocked-rj-howls_c1 with hpunch
    pause
    scene e08s03-80 mc-asking-arj-if-okay_c1 with dissolve
    play voice2 mc_pain_mff1 noloop
    mc "Are you okay?"
    play voice3 amrose_pain_sobs1 noloop
    arj "Holy hell, that scared me."
    mc "When is this going to be over?"
    arj "Hold me."
    play sound sfx_cloth_rustling4
    scene e08s03-81 mc-promises-arj-he-wont-let-her-go_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "I'll never let you go."
    play voice3 amrose_pain_sobs3 noloop
    arj "Do you regret any of it?"
    play voice2 mc_no_no5 noloop
    mc "No."
    arj "Me neither."
    scene black with dissolve
    pause 0.2
    scene e08s03-82 phone-battery-runs-out_c1 with dissolve
    pause

    stop sound4 fadeout 4.0
    stop sound5 fadeout 4.0
    stop music fadeout 4.0
    jump e08s04

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
