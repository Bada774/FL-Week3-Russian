image e11s01-a3-glam = Movie(play = "images/E-11/s01/anim/e11s01-a3-2x-50fps.webm", start_image = "e11s01-a3 mc-enters-glambot-3-00_i", image = "e11s01-a3 mc-enters-glambot-3-89_i", loop = False)

label e11_menu_jump:

    stop music fadeout 2.0
    call start_ending_from_menu from _call_start_ending_from_menu_9
    $ mcname = persistent.mcname
    $ mclogin = persistent.mclogin
    $ cage_ntr = persistent.cage_ntr
    $ stop_all_sound()
    call hide_fl_points_overlay from _call_hide_fl_points_overlay_22

    if mcname == "Charlie" or mcname == "Charles":
        $ d17s06_teddy_name  = _("Xander")
    else:
        $ d17s06_teddy_name  = _("Charlie")
    $ d19s04_dd_black = False
    $ d19s04_dd_odd = False
    $ d19s04_dd_dozen = False
    $ d19s04_dd_corner = False
    $ d19s04_dd_single = False
    $ d19s04_dd_end = False
    $ d19s04_dd_spot_plushie = False

    $ renpy.music.set_volume(0.4, 1.5, "music")
    play music music_feel_with_me fadein 5.0
    jump d19s04dd_after

label e11s01:

    call hide_fl_points_overlay from _call_hide_fl_points_overlay_23
    scene black
    show screen scene_transistion(_("Ending #11\nRed Diamond"))
    with Fade(0.9, 0.9, 0.9)
    pause
    hide screen scene_transistion
    stop music fadeout 3.0
    scene black
    show screen scene_transistion(_("Twenty years later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(1.0, 1.0, "sound")
    $ renpy.music.set_volume(1.0, 1.0, "sound2")
    $ renpy.music.set_volume(1.0, 1.0, "sound3")
    $ renpy.music.set_volume(1.0, 1.0, "sound4")
    $ renpy.music.set_volume(1.0, 1.0, "sound5")
    play sound3 d12s2_cafe_crowd fadein 3.0 volume 0.7
    $ renpy.music.set_volume(0.0, 0.0, "music")
    $ renpy.music.set_volume(1.0, 0.0, "music2")
    $ renpy.music.play(audio.languid_love, "music" , True, None, True, 1.0)
    $ renpy.music.play(audio.languid_love_reverbed, "music2", True, None, True, 1.0)
    scene e11s01-02-ly-waiting-for-mc
    with Fade(0.5, 0.5, 0.5)
    pause
    play sound sfx_door_closed9
    scene e11s01-a3 mc-enters-glambot-3-00_i with dissolve
    pause
    play sound sfx_camera_fly1
    scene e11s01-a3-glam
    pause
    stop sound fadeout 1.0
    scene e11s01-04-ly-excited with dissolve
    play voice3 girl28_happy_mmm1 noloop
    pause
    scene e11s01-05-mc-talk-ly with dissolve
    play voice2 d2s9_mchey noloop
    mc "Hey! Sorry I'm late."
    scene e11s01-06-ly-talk-mc with dissolve
    play voice3 girl28_hey_sexy noloop
    ly "It's okay! I'm so happy to see you Dad!"
    play sound sfx_cloth_rustling2
    scene e11s01-07-ly-mc-hug with dissolve
    pause
    scene e11s01-08-mc-talk-ly with dissolve
    play voice2 mc_happy_a1 noloop
    mc "It's good to see you kiddo."
    scene e11s01-09-mc-talk-ly with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "I don't know if I said this earlier, but you picked a good restaurant! Your Mom would have loved to eat here."
    play sound sfx_cloth_dress_off3
    scene e11s01-10-mc-talk-ly with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "I used to come here all the time when I was going to college."
    scene e11s01-11-ly-talk-mc with dissolve
    play voice3 girl28_yes_yeah3 noloop
    ly "Then you'll have to tell me what to get!"
    scene e11s01-12-mc-talk-ly with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I don't think I ever actually got food here..."
    scene e11s01-13-ly-talk-mc with dissolve
    play voice3 girl28_surprised_what noloop
    ly "Then what'd you do here?"
    scene e11s01-14-mc-talk-ly with dissolve
    play voice2 mc_pain_cough1 noloop
    mc "I, uh-studied sweetie. Studied with my... Spanish study group."
    scene e11s01-15-ly-talk-mc with dissolve
    play voice3 girl28_yes_yeah2 noloop
    ly "Sure, Dad. Sure."
    scene e11s01-16-mc-talk-ly with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Speaking of studying! How is University?"
    scene e11s01-17-ly-talk-mc with dissolve
    play voice3 girl28_happy_great2 noloop
    ly "It's good! I'm actually top of my class in English writing. And I've got this really exciting lecture on astronomy."
    scene e11s01-18-mc-talk-ly with dissolve
    play voice2 mc_happy_thatsgood noloop
    mc "That's good! Staying out of trouble?"
    scene e11s01-19-ly-talk-mc with dissolve
    play voice3 girl28_happy_laugh2 noloop
    ly "Only as well as you and Mom would have."
    scene e11s01-20-mc-talk-ly with dissolve
    play voice2 mc_scared_oh2 noloop
    mc "God, I hope that's not true."
    play sound sfx_heels_steps2
    scene e11s01-21-ly-talk-mc with dissolve
    play voice3 girl28_surprised_why1 noloop
    ly "Why?"
    stop sound fadeout 1.0
    scene e11s01-22-mc-talk-wa with dissolve
    play voice2 mc_happy_oof2 noloop
    mc "Thank God."
    scene e11s01-23-wa-talk-mc with dissolve
    play voice4 boy4_hey_simple noloop
    "Waiter" "Good afternoon! I just wanted to check, just the two of you this afternoon?"
    play voice2 mc_yes_yeah1 noloop
    mc "That's right."
    play voice4 boy4_thinking_hmm1 noloop
    "Waiter" "Great, can I get a drink order started for you?"
    scene e11s01-24-mc-talk-wa with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "I'll have a glass of wine and-"
    scene e11s01-25-ly-talk-wa with dissolve
    play voice3 girl28_yes_yap2 noloop
    ly "The same for me!"
    scene e11s01-26-mc-talk-ly with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "You have to go back to uni!"
    scene e11s01-27-ly-talk-mc with dissolve
    play voice3 girl28_no_nah2 noloop
    ly "A little bit of wine won't hurt Dad, be cool."
    scene e11s01-28-wa-talk-mc with dissolve
    play voice4 boy4_thinking_emm1 noloop
    "Waiter" "Two glasses of wine. Red okay?"
    scene e11s01-29-mc-talk-wa with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Sounds great, thank you."
    play sound sfx_heels_steps2
    scene e11s01-30-ly-thoughtful with dissolve
    pause
    scene e11s01-31-mc-talk-ly with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "Hey, sweetie, what's going on?"
    scene e11s01-32-ly-talk-mc with dissolve
    play voice3 girl28_disappointed_eeh1 noloop
    ly "Just... Missing Mom."
    scene e11s01-33-mc-talk-ly with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "I miss her too."
    scene e11s01-34-ly-talk-mc with dissolve
    play voice3 girl28_happy_relief2 noloop
    ly "I wish she could've been here today."
    scene e11s01-35-mc-talk-ly with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "I know. Me too."
    scene e11s01-36-ly-talk-mc with dissolve
    play voice3 girl28_disappointed_mmm2 noloop
    ly "I just hope she's proud of me."
    scene e11s01-37-mc-talk-ly with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "I don't think you have to be worried about that. Daisy, your Mom, would support you no matter what you did."
    scene e11s01-38-ly-talk-mc with dissolve
    play voice3 girl28_hey_active noloop
    ly "You know, I've always wondered, how did you and Mom meet?"
    scene e11s01-39-mc-talk-ly with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Well. That is a whoooooole story."
    scene e11s01-34-ly-talk-mc with dissolve
    play voice3 girl28_yes_yeah4 noloop
    ly "Wel we have a whooooooooole lunch to talk about it!"
    scene e11s01-41-mc-talk-ly with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay well, where to start..."
    scene e11s01-40-mc-talk-ly with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "When I was in college, there was this app-"
    $ renpy.music.set_volume(0.0, 1.0, "sound3")
    $ renpy.music.set_volume(0.5, 2.0, "music")
    $ renpy.music.set_volume(0.5, 2.0, "music2")
    play sound sfx_memory_in4
    scene d03s01-03 finger-punch-1
    show d03s01-03-over finger-move-4
    show memory-overlay
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    play sound sfx_memory_change1 volume 0.5
    scene d03s01-04 punch-look
    show memory-overlay
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    play sound sfx_memory_change1 volume 0.5
    scene d03s01-04-02 lift-blanket
    show memory-overlay
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    play sound sfx_memory_change1 volume 0.5
    scene d04s02-09 dd-kneeling-2
    show memory-overlay
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    play sound sfx_memory_change1 volume 0.5
    scene d04s02-10 dd-lick-the-tip
    show memory-overlay
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    play sound sfx_memory_change1 volume 0.5
    scene d12s06-037 mc-dd-transition_c1
    show memory-overlay
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    play sound sfx_memory_change1 volume 0.5
    scene d12s06-049 mc-dd-cuddle_c1
    show memory-overlay
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    $ renpy.music.set_volume(0.0, 2.0, "music")
    $ renpy.music.set_volume(1.0, 2.0, "music2")
    $ renpy.music.set_volume(0.7, 1.0, "sound3")
    play sound sfx_memory_back4 volume 1.7
    scene e11s01-39-mc-talk-ly with Fade(0.15, 0.05, 0.5, color="#fffefd")
    play voice2 mc_pain_cough2 noloop
    mc "Uhm, maybe I'll skip some of that."
    scene e11s01-42-ly-talk-mc with dissolve
    play voice3 girl28_happy_laugh3 noloop
    ly "Please. I don't need to know about {i}everything{/i} you did in college."
    scene e11s01-43-mc-talk-ly with dissolve
    play voice2 d2s9_confused noloop
    mc "You're probably right. Let's just say that me and your mom had a mutual friend."
    scene e11s01-44-mc-inner-talk with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "Which isn't exactly a lie."
    scene e11s01-45-ly-talk-mc with dissolve
    play voice3 girl28_arrogant_hmm3 noloop
    ly "That's right, didn't you meet through that one lady... Uhm, the flower from the murders."
    scene e11s01-46-mc-talk-ly with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Dahlia, you're right. Kind of. I met Dahlia because of my roommate Pete."
    scene e11s01-38-ly-talk-mc with dissolve
    play voice3 girl28_arrogant_huh1 noloop
    ly "Love at first sight?"
    scene e11s01-47-mc-talk-ly with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "In a way. I always knew your Mom was special."
    scene e11s01-48-mc-talk-ly with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "We had a lot of fun while I was in college but..."
    $ renpy.music.set_volume(0.5, 2.0, "music")
    $ renpy.music.set_volume(0.5, 2.0, "music2")
    $ renpy.music.set_volume(0.0, 1.0, "sound3")
    play sound sfx_memory_in4
    scene d11s04-80 doc-examine-dd-2
    show memory-overlay
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    play voice2 mc_angry_huh2 noloop
    mc "That was also around the time that she started to learn about her illness."
    play sound sfx_memory_change1 volume 0.5
    scene d11s04-96 dd-talking-with-doc
    show memory-overlay
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    play voice2 mc_thinking_mmm3 noloop
    mc "It was tough, but I think that if it wasn't for your mom being sick, you wouldn't be here today."
    $ renpy.music.set_volume(0.0, 2.0, "music")
    $ renpy.music.set_volume(1.0, 2.0, "music2")
    $ renpy.music.set_volume(0.7, 1.0, "sound3")
    play sound sfx_memory_back4 volume 1.7
    scene e11s01-49-ly-talk-mc with Fade(0.15, 0.05, 0.5, color="#fffefd")
    play voice3 girl28_disappointed_eeh2 noloop
    ly "What do you mean?"
    scene e11s01-50-mc-talk-ly with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Well, I think it was maybe after the second time I went with your mom to the doctor."
    mc "I went over to see her and-"
    $ renpy.music.set_volume(0.0, 1.0, "sound3")
    $ renpy.music.set_volume(0.5, 2.0, "music")
    $ renpy.music.set_volume(0.5, 2.0, "music2")
    play sound sfx_memory_change1 volume 0.5
    scene d19s04-dd-10 dd-talk-mc
    show memory-overlay
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    play sound sfx_memory_change1 volume 0.5
    scene d19s04-dd-22 dd-suck-mc-anim
    show memory-overlay
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    $ renpy.music.set_volume(0.0, 2.0, "music")
    $ renpy.music.set_volume(1.0, 2.0, "music2")
    $ renpy.music.set_volume(0.7, 1.0, "sound3")
    play sound sfx_memory_back4 volume 1.7
    scene e11s01-48-mc-talk-ly with Fade(0.15, 0.05, 0.5, color="#fffefd")
    play voice2 d3s7_mcemm noloop
    mc "-we, uhm, talked. And she told me about her bucket list."
    scene e11s01-51-ly-talk-mc with dissolve
    play voice3 girl28_arrogant_huh2 noloop
    ly "Mom had a bucket list?"
    scene e11s01-52-mc-talk-ly with dissolve
    play voice2 mc_scared_oh3 noloop
    mc "Oh boy did she. She wanted to go skydiving, and gambling, and climb a mountain-"
    scene e11s01-53-ly-talk-mc with dissolve
    play voice3 girl28_surprised_eeh noloop
    ly "Mom climbed a mountain!?"
    scene e11s01-54-mc-talk-ly with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yep. I was there with her."
    scene e11s01-55-ly-talk-mc with dissolve
    play voice3 girl28_surprised_huh noloop
    ly "YOU climbed a MOUNTAIN!?"
    scene e11s01-56-mc-talk-ly with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "What's so difficult to believe about that!"
    scene e11s01-57-ly-talk-mc with dissolve
    play voice3 girl28_happy_laugh4 noloop
    ly "I love you Dad, but I've seen you get tired from walking up the stairs."
    scene e11s01-58-mc-talk-ly with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hey, I was a lot more active when I was your age."
    scene e11s01-59-ly-talk-mc with dissolve
    play voice3 girl28_arrogant_yeah2 noloop
    ly "Yeah, yeah. So you and Mom-"
    scene e11s01-60-mc-talk-ly with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "We started working through her bucket list. Then-"
    scene e11s01-61-ly-talk-mc with dissolve
    play voice3 girl28_hey_angry noloop
    ly "Wait! You're just going to skip over the bucket list!?"
    scene e11s01-62-mc-talk-ly with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "I guess?"
    scene e11s01-63-ly-talk-mc with dissolve
    play voice3 girl28_angry_dough1 noloop
    ly "You're just going to drop the 'your Mom climbed a mountain' on me, and not tell me more!?"
    scene e11s01-64-mc-talk-ly with dissolve
    play voice2 mc_surprised_wow1 noloop
    mc "I was just trying to keep the story short."
    scene e11s01-65-ly-talk-mc with dissolve
    play voice3 girl28_no_nonono2 noloop
    ly "I want to know the whole story! Plus, you said it's the reason I'm here!"
    scene e11s01-66-mc-talk-ly with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Okay, okay. I'll tell you the whole story."
    scene e11s01-67-ly-talk-mc with dissolve
    play voice3 girl28_happy_yay1 noloop
    ly "Yay!"
    scene e11s01-68-mc-talk-ly with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, so your Mom and I talked and she invited me to join her on her bucket list tour."
    scene e11s01-69-ly-talk-mc with dissolve
    play voice3 girl28_happy_relief1 noloop
    ly "What did you do first?"
    scene e11s01-70-mc-talk-ly with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "I think we... Yeah, we started with skydiving. There was a place like an hour away we could go to."
    scene e11s01-71-ly-talk-mc with dissolve
    play voice3 girl28_surprised_wow noloop
    ly "So you and Mom actually jumped out of a plane?"
    scene e11s01-72-mc-talk-ly with dissolve
    play voice2 d9s2_mcyes noloop volume 2.5
    mc "We did. It was exciting, terrifying. I don't think I've ever had a more intense e-"
    scene e11s01-73-ly-talk-mc with dissolve
    play voice3 girl28_pain_ah noloop
    ly "Dad!"
    scene e11s01-74-mc-talk-ly with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Sorry, that's right. Skipping some of the details. Skydiving."
    scene e11s01-75-ly-talk-mc with dissolve
    play voice3 girl28_arrogant_hmm1 noloop
    ly "What was after that?"
    scene e11s01-76-mc-talk-ly with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Well, the next part of our trip meant that we had to fly to Italy."
    scene e11s01-77-ly-talk-mc with dissolve
    play voice3 girl28_happy_nice1 noloop
    ly "That sounds so romantic Dad."
    scene e11s01-78-mc-talk-ly with dissolve
    play voice2 mc_no_nah2 noloop
    mc "It was all your Mom's idea. Daisy was... She was a dreamer and so passionate about what she wanted. I just helped her when I could."
    scene e11s01-79-ly-talk-mc with dissolve
    play voice3 girl28_yes_yeah1 noloop
    ly "I bet she appreciated it."
    scene e11s01-80-mc-talk-ly with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "I think she did."
    scene e11s01-81-ly-talk-mc with dissolve
    play voice3 girl28_arrogant_hmm2 noloop
    ly "Did you spring for first class tickets?"
    scene e11s01-82-mc-talk-ly with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Not quite first class. But the service was definitely first-class."
    scene e11s01-75-ly-talk-mc with dissolve
    play voice3 girl28_surprised_ohmy noloop
    ly "What do you mean, dad?"
    scene e11s01-84-mc-talk-ly with dissolve
    mc "Going in, I was a little stressed out about a long plane ride."
    scene e11s02-01-04 mc-continues-story_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "But as it turned out, that was the day your mom and I joined the mile-high club."

    stop music fadeout 3.0
    stop music2 fadeout 3.0
    $ renpy.music.set_volume(0.0, 3.0, "sound3")
    jump e11s02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
