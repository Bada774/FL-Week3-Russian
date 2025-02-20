image d18s06-a1 = Movie(play = "images/Day-18/s06/anim/d18s06-06-a1-4x-40fps.webm", start_image = "d18s06-06-a1 mc-sy-arj-hr-walking-glam-anim1-000_i", image = "d18s06-06-a1 mc-sy-arj-hr-walking-glam-anim1-109_i", loop=False)

label d18s06:

    scene black
    show screen scene_transistion(_("Some time later\nAt the college campus"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene d18s06-01 mc-sy-arj-hr-enter-mc_c1
    with Fade(0.5, 0.5, 0.9)
    play voice2 mc_arrogant_huh3 noloop
    mc "AmRose?"
    scene d18s06-01 mc-sy-arj-hr-enter-mc_c2 with dissolve
    play voice3 amrose_old_hey1 noloop
    arj "Hey [mcname]. Welcome to the mission."
    mc "What are you wearing... ?"
    scene d18s06-02 mc-sy-arj-hr-talking_c1 with dissolve
    play voice3 amrose_arrogant_huh1 noloop
    arj "*sigh* Stacy got us mission outfits."
    play voice2 mc_disappointed_off2 noloop
    mc "Oh dear."
    play voice3 amrose_thinking_hmm3 noloop
    arj "You don't like it?"
    scene d18s06-03 mc-sy-arj-hr-mike-unsure_c1 with dissolve
    play voice2 d2s9_confused noloop
    mc "I mean, it looks really sexy on you..."
    scene d18s06-04 mc-sy-arj-hr-arj-question_c2 with dissolve
    play voice3 amrose_happy_laugh1 noloop
    arj "Good save."
    $ renpy.music.set_volume(1.0, 0.0, "sound2")
    play sound2 sfx_heels_steps1 fadein 1.5 noloop
    $ renpy.music.set_volume(0.8, 0.0, "music")
    play music music_special_operation fadein 10.5
    scene d18s06-a1 with Fade(0.5, 0.3, 2.5)
    stop sound2 fadeout 8.0
    pause
    stop sound2 fadeout 1.0
    scene d18s06-06 mc-sy-arj-hr-walking_c1 with dissolve
    $ renpy.music.set_volume(0.45, 4.0, "music")
    play voice4 stacy_angry noloop
    sy "I'm telling you. This is tactical, practical, professional, and slutty. It's perfect for this mission!"
    scene d18s06-06 mc-sy-arj-hr-walking_c2 with dissolve
    play voice3 hana_argh noloop
    hr "I'm wearing it. That's enough. Stop trying to convince me it's a good idea."
    scene d18s06-07 mc-sy-arj-hr-hello_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hello ladies...{w} You all look stunning."
    scene d18s06-08 mc-sy-talk1_c2 with dissolve
    play voice4 stacy_hmm noloop
    sy "Thank you!"
    scene d18s06-06 mc-sy-arj-hr-walking_c2 with dissolve
    play voice3 hana_argh2 noloop
    hr "I loathe this attire."
    scene d18s06-07 mc-sy-arj-hr-talk1_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Then why are you wearing it?"
    scene d18s06-02 mc-sy-arj-hr-talking_c1 with dissolve
    play voice3 amrose_disappointed_ehh2 noloop
    arj "Stacy said she wouldn't open the door unless we wore matching outfits."
    scene d18s06-08 mc-sy-talk1_c2 with dissolve
    play voice4 stacy_hey noloop
    sy "Give me your phone."
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    scene d18s06-09 mc-sy-talk2_c2 with dissolve
    play voice4 stacy_angryhuh noloop
    sy "Give. Me. Your. Phone."
    play voice2 mc_yes_okay1 noloop
    mc "Okay."
    scene d18s06-20 mc-sy-arj-hr-result5-so_c3 with dissolve
    play voice3 hana_hmm noloop
    hr "And since it's an electronic lock connected to a steel core door..."
    play sound sfx_keyboard_typing2 volume 1.5
    scene d18s06-14 mc-sy-arj-hr-testing1_c1 with dissolve
    play voice4 amrose_yes_yeah1 noloop
    arj "Basically, Stacy is about the only one who can unlock it without the code."
    play voice3 stacy_mmm1 noloop
    sy "I said I MIGHT be able to unlock it."
    hr "Duly noted, now will you please start trying."
    sy "Of course."
    scene d18s06-13 mc-sy-phone2_c2 with dissolve
    play voice3 polly_aga noloop
    sy "Here."
    play voice2 mc_thinking_hmm2 noloop
    mc "It's my phone. And it is turned off."
    scene d18s06-12 mc-sy-phone1_c2 with dissolve
    play voice3 stacy_no2 noloop
    sy "It isn't just turned off.{w} Fetish Locator can't turn it back on anymore."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, nice."
    scene d18s06-14 mc-sy-arj-hr-testing1_c1 with dissolve
    play voice3 stacy_huh2 noloop
    sy "AmRose, can you help me with this?"
    scene d18s06-14 mc-sy-arj-hr-testing1_c2 with dissolve
    play voice4 amrose_yes_okay2 noloop
    arj "Okay."
    scene d18s06-14 mc-sy-arj-hr-testing1_c3 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "What exactly are they doing?"
    scene d18s06-14 mc-sy-arj-hr-testing1_c4 with dissolve
    play voice3 nora_hmm noloop
    play sound sfx_photocamera_flash2
    hr "Something with computers and electronics."
    scene d18s06-15 mc-sy-arj-hr-testing2_c3 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "That clears that up."
    scene d18s06-15 mc-sy-arj-hr-testing2_c4 with dissolve
    play voice3 hana_hmm2 noloop
    hr "CompSci girl is trying to brute force codes through a simulation or something like that."
    hr "Engineer girl is trying to detect signals and prevent the simulation from tripping an alarm."
    play voice2 mc_happy_a1 noloop
    mc "Sounds like a good plan."
    hr "Think it will work?"
    scene d18s06-16 mc-sy-arj-hr-result1_c1 with dissolve
    play voice4 amrose_thinking_emm noloop
    arj "Well, we have good news..."
    scene d18s06-16 mc-sy-arj-hr-result1_c2 with dissolve
    play voice3 stacy_hmm noloop
    sy "We're certain there are only 4 digits to the correct code."
    scene d18s06-16 mc-sy-arj-hr-result1_c1 with dissolve
    play voice4 amrose_yes_yeah3 noloop
    arj "And we have bad news..."
    scene d18s06-16 mc-sy-arj-hr-result1_c2 with dissolve
    play voice3 stacy_angryhuh noloop
    sy "The system will lock us out and set off an alarm if the wrong code is entered too often."
    scene d18s06-16 mc-sy-arj-hr-result1_c3 with dissolve
    play voice4 hana_emm noloop
    hr "Can you bypass the alarm?"
    scene d18s06-17 mc-sy-arj-hr-result2_c1 with dissolve
    play voice3 amrose_yes_ugu noloop
    arj "I could, but it would involve seriously damaging the lock..."
    scene d18s06-16 mc-sy-arj-hr-result1_c3 with dissolve
    play voice4 chloe_arrogant_heh1 noloop
    hr "I'm okay with that."
    scene d18s06-18 mc-sy-arj-hr-result3_c1 with dissolve
    play voice3 amrose_disappointed_oh5 noloop
    arj "And I'm fairly certain it would permanently lock the door."
    scene d18s06-16 mc-sy-arj-hr-result1_c4 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "I'm not okay with that."
    scene d18s06-17 mc-sy-arj-hr-result2_c1 with dissolve
    play voice3 amrose_thinking_hmm1 noloop
    arj "Also, we're certain there is at least one person inside."
    scene d18s06-17 mc-sy-arj-hr-result2_c3 with dissolve
    play voice4 nora_angrymoan noloop
    hr "How do you know that?"
    scene d18s06-18 mc-sy-arj-hr-result3_c2 with dissolve
    play voice3 stacy_mmm2 noloop
    sy "I have a WiFi detector and there's at least one signal moving around in there."
    scene d18s06-18 mc-sy-arj-hr-result3_c3 with dissolve
    play voice4 nora_oh noloop
    hr "Who is it? Can you identify the... I dunno, the MAC Address or something?"
    scene d18s06-20 mc-sy-arj-hr-result5-so_c1 with dissolve
    play voice3 amrose_disappointed_ehh1 noloop
    arj "*sigh* Just pretend that it's magic."
    hr "Okay..."
    scene d18s06-18 mc-sy-arj-hr-result3_c2 with dissolve
    play voice4 stacy_upset1 noloop
    sy "We magically know there is at least one person inside."
    scene d18s06-16 mc-sy-arj-hr-result1_c4 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "So, why don't we just knock on the door and see if they open up?"
    scene d18s06-20 mc-sy-arj-hr-result5-so_c1 with dissolve
    play voice3 amrose_yes_yap noloop
    arj "Or we could come back tonight when nobody is in there."
    scene d18s06-20 mc-sy-arj-hr-result5-so_c3 with dissolve
    play voice4 chloe_no_active noloop
    hr "No! If there's someone in there. I want to catch them in the act!"
    scene d18s06-20 mc-sy-arj-hr-result5-so_c4 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "I'm still thinking about knocking."
    scene d18s06-20 mc-sy-arj-hr-result5-so_c1 with dissolve
    play voice3 amrose_arrogant_hmm2 noloop
    arj "Stacy could still be able to get the door open."
    scene d18s06-20 mc-sy-arj-hr-result5-so_c2 with dissolve
    play voice4 stacy_no1 noloop
    sy "Nope."
    scene d18s06-20 mc-sy-arj-hr-result5-so_c3 with dissolve
    play voice3 chloe_angry_hm noloop
    hr "What do you mean, \"Nope\"?"
    scene d18s06-20 mc-sy-arj-hr-result5-so_c2 with dissolve
    play voice4 stacy_yeahno noloop
    sy "I've tried everything I can think of... it all results in a best case scenario of a 0.3%% chance of success."
    scene d18s06-16 mc-sy-arj-hr-result1_c4 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "That doesn't sound good."
    hr "That isn't good."
    play voice3 amrose_yes_yeah2 noloop
    arj "Yeah."
    scene d18s06-20 mc-sy-arj-hr-result5-so_c3 with dissolve
    play voice4 chloe_happy_hmm noloop
    hr "Okay, plan B."
    scene d18s06-20 mc-sy-arj-hr-result5-so_c4 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Knock on the door?"
    scene d18s06-20 mc-sy-arj-hr-result5-so_c3 with dissolve
    play voice3 chloe_arrogant_pff noloop
    hr "I saw a fireaxe around the corner. I can knock with that."
    scene d18s06-21 mc-sy-arj-hr-knock_c3 with dissolve
    play voice4 amrose_arrogant_huh2 noloop
    arj "It's a steel core."
    scene d18s06-20 mc-sy-arj-hr-result5-so_c4 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Also, the person inside would call security."
    scene d18s06-20 mc-sy-arj-hr-result5-so_c3 with dissolve
    play voice3 chloe_disappointed_mff noloop
    hr "Fuck.{w} Fine. You knock."
    scene d18s06-21 mc-sy-arj-hr-knock_c1 with dissolve
    call metalknock1 from _call_metalknock1
    play voice2 mc_hey_hey1 noloop
    mc "Hello?"
    scene d18s06-21 mc-sy-arj-hr-knock_c2 with hpunch
    play voice3 stacy_impressed noloop
    sy "Land shark!"
    scene d18s06-21 mc-sy-arj-hr-knock_c3 with dissolve
    play voice4 amrose_disappointed_oh3 noloop
    arj "You're not old enough to understand that reference."
    scene d18s06-21-2 mc-sy-arj-hr-knock2_c1 with dissolve
    play voice2 shhh noloop
    mc "Shush."
    scene d18s06-21 mc-sy-arj-hr-knock_c1 with dissolve
    call metalknock2 from _call_metalknock2
    play voice2 mc_hey_hey4 noloop
    mc "HELLO?!"
    scene d18s06-23 mc-sy-arj-hr-planc_c4 with dissolve
    play voice3 chloe_arrogant_okay noloop
    hr "Okay, then. Plan C."
    scene d18s06-24 mc-sy-arj-hr-planc2_c3 with dissolve
    play voice4 stacy_huh noloop
    sy "Is that where we set everything on fire?"
    scene d18s06-24 mc-sy-arj-hr-planc2_c1 with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "What? No!"
    scene d18s06-24 mc-sy-arj-hr-planc2_c2 with dissolve
    play voice3 amrose_thinking_hmm2 noloop
    arj "Let's skip Plan C and go right to Plan D."
    scene d18s06-23 mc-sy-arj-hr-planc_c4 with dissolve
    play voice4 chloe_disappointed_ehh5 noloop
    hr "How did I get teamed up with the 3 Stooges?"
    scene d18s06-25 mc-sy-arj-hr-planc5_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "You're definitely not old enough to-"
    scene d18s06-21 mc-sy-arj-hr-knock_c3 with dissolve
    play voice3 amrose_surprised_oh4 noloop
    arj "Waller!"
    scene d18s06-23 mc-sy-arj-hr-planc_c1 with hpunch
    play voice2 mc_surprised_huh3 noloop
    mc "Fuck! WHERE?!"
    scene d18s06-25 mc-sy-arj-hr-planc5_c2 with dissolve
    play voice3 amrose_no_simple1 noloop
    arj "No, I mean Zarah Waller should have access to every door on campus - in case there is a fire or something like that."
    scene d18s06-24 mc-sy-arj-hr-planc2_c3 with dissolve
    play voice4 stacy_oh noloop
    sy "I'm pretty sure that door is meant to stay closed if there's a fire."
    scene d18s06-24 mc-sy-arj-hr-planc2_c2 with dissolve
    play voice3 amrose_thinking_hmm5 noloop
    arj "Well, she should still know."
    scene d18s06-23 mc-sy-arj-hr-planc_c4 with dissolve
    play voice4 hana_yeah2 noloop
    hr "Okay, where can we find her?"
    scene d18s06-25 mc-sy-arj-hr-planc5_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "At this time of day?{w} She's probably on rounds at my dorm."
    scene d18s06-23 mc-sy-arj-hr-planc_c4 with dissolve
    play voice4 hana_hmm noloop
    hr "Alright, Stooges. Let's get ramblin'."
    play voice3 amrose_disappointed_pff noloop
    arj "That doesn't even make sense."
    scene d18s06-25 mc-sy-arj-hr-planc5_c2 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "Maybe we can be like the 3 Musketeers?{w} There were 4 of them."
    scene d18s06-25 mc-sy-arj-hr-planc5_c4 with dissolve
    play voice4 stacy_laugh4 noloop
    sy "I thought we were [mcname]'s Angels."
    scene d18s06-25 mc-sy-arj-hr-planc5_c3 with dissolve
    play voice3 hana_argh noloop
    hr "Whatever.{w} Hey - why doesn't [mcname] have to wear a tactical slut outfit?"
    scene d18s06-25 mc-sy-arj-hr-planc5_c4 with dissolve
    play voice4 stacy_oh2 noloop
    sy "I just assumed he would dress professionally."
    scene d18s06-23 mc-sy-arj-hr-planc_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Was I supposed to wear a suit or something?"
    scene d18s06-25 mc-sy-arj-hr-planc5_c2 with dissolve
    play voice3 amrose_yes_yeah4 noloop
    arj "Maybe we can pick one up at your dorm. Let's go."

    jump d18s07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
