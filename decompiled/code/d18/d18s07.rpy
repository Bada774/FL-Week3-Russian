image d18s07_glam_1 = Movie(play = "images/Day-18/s07/anim/d18s07-a1-4x-40fps.webm", start_image = "d18s07-06-01-a1 gang-appears-glambot-1-000_i", image = "d18s07-06-01-a1 gang-appears-glambot-1-098_i", loop = False)
image d18s07_glam_2 = Movie(play = "images/Day-18/s07/anim/d18s07-a2-4x-48fps.webm", start_image = "d18s07-54-01-a2 gang-appears-glambot-2-00_i",  image = "d18s07-54-01-a2 gang-appears-glambot-2-50_i",  loop = False)

label d18s07:

    $ renpy.music.set_volume(0.1, 3.0, "music")
    scene d18s07-01-zw-walking-down with Fade(0.6, 0.6, 0.6)
    pause
    play voice4 zbackground_mfm_orgy_muffled1 fadein 1.5
    scene d18s07-02-zw-hears-moaning with dissolve
    "*Muffled Moaning*"
    scene d18s07-03-zw-shout with dissolve
    play voice3 chloe_angry_argh5 noloop
    zw "Mr. Turner!"
    scene d18s07-04-zw-talk-waller with dissolve
    zw "You better not be doing what I think you're doing inside there!"
    stop voice4 fadeout 1.0
    scene d18s07-06-01-a1 gang-appears-glambot-1-000_i with dissolve
    play voice3 chloe_angry_cough noloop
    zw "Open this door {i}right now{/i}, young man!"
    $ renpy.music.set_volume(0.8, 2.0, "music")
    scene d18s07_glam_1 with dissolve
    pause
    $ renpy.music.set_volume(0.35, 3.0, "music")
    scene d18s07-05-mc-talk-gang with dissolve
    play voice2 shhh noloop
    mc "{i}Shuush{/i}."
    scene d18s07-07-mc-peek-zw with dissolve
    pause
    scene d18s07-08-mc-talk-gang with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Fuck."
    scene d18s07-09-mc-talk-gang with dissolve
    mc "Alright. Good news and bad news."
    scene d18s07-10-mc-talk-gang with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Good news, we found Zarah."
    scene d18s07-11-mc-talk-gang with dissolve
    mc "Bad news, she's right around the corner and she's {i}not{/i} in a good mood."
    scene d18s07-12-hr-talk-mc with dissolve
    play voice3 hana_argh noloop
    hr "Christ, that woman needs some good dick."
    scene d18s07-13-mc-talk-hr with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Tell me about it."
    play sound sfx_comic_idea_1
    scene d18s07-14-sy-raise-a-finger with dissolve
    pause
    scene d18s07-15-mc-talk-sy with dissolve
    play voice2 mc_no_no1 noloop
    mc "Don't even think about it."
    play voice4 min_thinking_mhh noloop
    play sound sfx_comic_disappointed_1
    scene d18s07-16-sy-pouts-finger-down with dissolve
    pause
    scene d18s07-17-arj-talk-gang with dissolve
    play voice3 amrose_thinking_emm noloop
    arj "So what are we doing? One of us has to go talk with her."
    arj "[mcname] has the mos—"
    scene d18s07-18-sy-talk-gang with dissolve
    play voice4 stacy_laugh noloop
    sy "Let me handle this."
    play sound2 sfx_heels_steps1
    scene d18s07-19-sy-moves with dissolve
    pause
    scene d18s07-20-mc-talk-sy with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "Stacy! What are you—!?"
    $ renpy.music.set_volume(0.6, 3.0, "music")
    scene d18s07-21-sy-walk-into-the-zw with dissolve
    pause
    play voice2 mc_pain_rrrr noloop
    scene d18s07-22-mc-back-to-cover with dissolve
    pause
    stop sound2 fadeout 2.0
    scene d18s07-23-zw-talk-wt with dissolve
    $ renpy.music.set_volume(0.2, 4.0, "music")
    play voice4 chloe_angry_argh2 noloop
    zw "Mr. Turner, you know the rules. Open this door immediately."
    scene d18s07-24-sy-talk-zw with dissolve
    play voice3 stacy_hey noloop
    sy "Hi! You're Ms. Zarah Waller, I assume?"
    scene d18s07-25-zw-talk-sy with dissolve
    play voice4 chloe_yes_angry noloop
    zw "Missus. And yes.{w} Who are you?"
    scene d18s07-26-sy-talk-zw with dissolve
    play voice3 stacy_oh2 noloop
    sy "Ah, of course. Pardon."
    sy "My name is Tracy and I'm the fire inspector assigned to inspect the college grounds—including the dorms—and reassess the fire maps, and create up to date digital fire maps."
    scene d18s07-27-zw-talk-sy with dissolve
    play voice4 chloe_surprised_oh noloop
    zw "Oh, I wasn't aware that we had anything like that scheduled today."
    scene d18s07-28-sy-talk-zw with dissolve
    play voice3 stacy_mmm1 noloop
    sy "That's unfortunate. I—"
    play sound sfx_door_open3 volume 1.5
    scene d18s07-29-wt-sneak-out with dissolve
    pause
    play sound sfx_barefoot_run1 volume 1.5
    play sound2 sfx_sport_run1 volume 2.0 noloop
    scene d18s07-30-02-zw-talk-wt with dissolve
    pause
    scene d18s07-30-03-zw-talk-wt with vpunch
    play voice4 chloe_angry_argh3 noloop
    zw "Mr. Turner!"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    stop music fadeout 3.0
    scene d18s07-31-sy-talk-zw with dissolve
    play voice3 stacy_laugh4 noloop
    sy "Kids, am I right?"
    scene d18s07-32-zw-talk-sy with dissolve
    play voice4 chloe_disappointed_off noloop
    zw "I'm sorry, how old are you again?"
    $ renpy.music.set_volume(0.6, 0.0, "music2")
    play music2 stacy_time
    scene d18s07-33-sy-talk-zw with dissolve
    play voice3 polly_impressed noloop
    sy "37."
    play sound sfx_whip_slap2
    scene d18s07-34-gang-face-palm with dissolve
    pause
    scene d18s07-35-zw-talk-sy with dissolve
    zw "..."
    scene d18s07-36-sy-talk-zw with dissolve
    play voice3 stacy_mmm2 noloop
    sy "Moisturizing every day does wonders for your skin."
    sy "Anyway. Where was I? Ah, right."
    scene d18s07-37-sy-talk-zw with dissolve
    sy "You see, I was inspecting the faculty sector in the college and came across a locked door leading to the I.T. room."
    sy "I was informed that {i}you{/i} were the person that I needed to go to if I needed any help accessing certain locations within the college."
    scene d18s07-38-zw-talk-sy with dissolve
    play voice4 chloe_disappointed_ehh4 noloop
    zw "Oh. Well, yes. But why would you need access to the I.T. room?"
    scene d18s07-39-sy-talk-zw with dissolve
    play voice3 stacy_huh2 noloop
    sy "I.T rooms are horribly unsafe Mrs. Waller. You wouldn't believe the things I've seen."
    sy "Electrical cables strewn all over the place, servers with barely any ventilation, and all sorts of other unsafe practices."
    scene d18s07-42-sy-talk-zw with dissolve
    sy "This is just between two working professionals, but I was responsible for checking out Vinovella University as well."
    scene d18s07-40-sy-talk-zw with dissolve
    play voice3 dahlia_disgust_oeah noloop
    sy "And let me tell you, for being such a prestigious school, some of the things I saw there, especially in their I.T. department was just {i}awful{/i}."
    scene d18s07-43-zw-talk-sy with dissolve
    play voice4 chloe_happy_mmm noloop
    zw "Really? I always knew those prissy rich kids weren't all that."
    scene d18s07-44-sy-talk-zw with dissolve
    play voice3 polly_aga noloop
    sy "By that metric, your college is practically a shining example of what to do right."
    sy "I've yet to find a single major violation."
    sy "So I'm sure your I.T. room is well managed as well.{w} But I still need to make sure. I'm sure you understand."
    scene d18s07-45-zw-talk-sy with dissolve
    play voice4 chloe_disappointed_oh noloop
    zw "Oh, of course. But sadly I don't have access to that room."
    scene d18s07-46-gang-appears with dissolve
    pause
    scene d18s07-47-zw-talk-sy with dissolve
    play voice4 chloe_disappointed_ehh1 noloop
    zw "We got a new I.T. professor and she's the one that's responsible for that department now."
    play voice3 stacy_oh noloop
    sy "Oh."
    scene d18s07-46-gang-perks-up with dissolve
    pause
    scene d18s07-47-zw-talk-sy with dissolve
    play voice4 chloe_happy_hmm noloop
    zw "I could go ask now if you'd like? She's probably in the teacher's lounge. She might be able to help with your digital fire ma—"
    scene d18s07-48-sy-talk-zw with dissolve
    play voice3 stacy_yeahno noloop
    sy "Oh, that's alright. We don't need to do that right this second."
    scene d18s07-49-sy-sign-gang with dissolve
    pause
    scene d18s07-50-arj-talk-gang with dissolve
    play voice4 amrose_arrogant_huh4 noloop
    arj "What's she saying?"
    scene d18s07-51-hr-talk-gang with dissolve
    play voice3 hana_emm noloop
    hr "I think she's telling us to find the professor while she stalls."
    scene d18s07-52-sy-talk-zw with dissolve
    play voice4 stacy_angryhuh noloop
    sy "There were some other locations that I had some questions about as well."
    scene d18s07-54-01-a2 gang-appears-glambot-2-00_i with dissolve
    play voice3 chloe_surprised_oh noloop
    zw "Oh?"
    scene d18s07_glam_2 with dissolve
    pause
    play voice2 mc_yes_yes1 noloop
    mc "Yep. She wants us to go."
    scene d18s07-55-mc-talk-gang with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Alright. Let's go, she can clearly handle this."
    scene d18s07-56-gang-sneak-off with dissolve
    pause
    stop music2 fadeout 3.5

    jump d18s08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
