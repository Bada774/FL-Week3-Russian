image d15s04dd-a1 = Movie(play = "images/Day-15/Scene-04/daisy/anim/d15s01-a1-2x-50fps.webm", start_image = "d14s04b-01-lick-anim-01_i")
image d15s04dd-a2 = Movie(play = "images/Day-15/Scene-04/daisy/anim/d15s04-a2-2x-50fps.webm", start_image = "d14s04b-02-lick-anim-01_i")
image d15s04dd-a3 = Movie(play = "images/Day-15/Scene-04/daisy/anim/d15s04-a3-2x-50fps.webm", start_image = "d14s04b-03-lick-anim-01_i")
image d15s04dd-a4 = Movie(play = "images/Day-15/Scene-04/daisy/anim/d15s04-a4-2x-50fps.webm", start_image = "d14s04b-04-lick-anim-01_i")
image d15s04dd-a5-2 = Movie(play = "images/Day-15/Scene-04/daisy/anim/d15s05-a5-2-2x-50fps.webm", start_image = "d14s04b-05-lick-anim-01_i")

image d15s04dd-a5 = Movie(play = "images/Day-15/Scene-04/daisy/anim/d15s04b-a5-4x-60fps.webm", start_image = "d14s04b-01-fingering-anim-01_i")
image d15s04dd-a5-f = Movie(play = "images/Day-15/Scene-04/daisy/anim/d15s04b-a5-2x-50fps.webm", start_image = "d14s04b-01-fingering-anim-01_i")
image d15s04dd-a6 = Movie(play = "images/Day-15/Scene-04/daisy/anim/d15s04b-a6-4x-60fps.webm", start_image = "d14s04b-02-fingering-anim-01_i")
image d15s04dd-a6-f = Movie(play = "images/Day-15/Scene-04/daisy/anim/d15s04b-a6-2x-50fps.webm", start_image = "d14s04b-02-fingering-anim-01_i")
image d15s04dd-a7 = Movie(play = "images/Day-15/Scene-04/daisy/anim/d15s04b-a7-4x-60fps.webm", start_image = "d14s04b-03-fingering-anim-01_i")
image d15s04dd-a7-f = Movie(play = "images/Day-15/Scene-04/daisy/anim/d15s04b-a7-2x-50fps.webm", start_image = "d14s04b-03-fingering-anim-01_i")
image d15s04dd-a8 = Movie(play = "images/Day-15/Scene-04/daisy/anim/d15s04b-a8-4x-60fps.webm", start_image = "d14s04b-00-a8 fingering-anim-8-01_i")
image d15s04dd-a8-f = Movie(play = "images/Day-15/Scene-04/daisy/anim/d15s04b-a8-2x-50fps.webm", start_image = "d14s04b-00-a8 fingering-anim-8-01_i")
image d15s04dd-a9 = Movie(play = "images/Day-15/Scene-04/daisy/anim/d15s04b-a9-4x-60fps.webm", start_image = "d14s04b-00-a9 fingering-anim-9-01_i")
image d15s04dd-a9-f = Movie(play = "images/Day-15/Scene-04/daisy/anim/d15s04b-a9-2x-50fps.webm", start_image = "d14s04b-00-a9 fingering-anim-9-01_i")

label d15s04dd:

    scene black
    show screen scene_transistion(_("1 hour later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    play sound2 classroom fadein 1.5
    hide screen scene_transistion
    scene d15s04-01-dd-mc-coming-into-the-hospital
    with Fade(0.5, 0.5, 0.9)
    pause
    scene d15s04-02-mc-talking-with-dd with dissolve
    play voice2 d1s2_hey noloop
    mc "Not as many people here today."
    scene d15s04-03-dd-talking-with-mc with dissolve
    play voice3 daisy_ugu noloop
    dd "Yeah. I like it. It's not as suffocating."
    scene d15s04-04-dd-mc-go-to-the-receptionist with dissolve
    pause
    scene d15s04-05-dd-talking-with-rec with dissolve
    play voice3 daisy_hey noloop
    dd "Hi, I had an appointment with Dr. uhm, Dr. Bier..."
    scene d15s04-06-rec-talking-with-dd with dissolve
    play voice4 lissa_oh noloop
    "Receptionist" "Oh, right. Let me see."
    play sound sfx_keyboard_typing2
    scene d15s04-07-rec-checks-her-computer with dissolve
    pause
    stop sound fadeout 1.0
    scene d15s04-08-rec-talking-with-dd with dissolve
    play voice4 lissa_thinking noloop
    "Receptionist" "Right. Are you Ms. Daisy Diamond?"
    scene d15s04-09-dd-talking-with-rec with dissolve
    play voice3 daisy_aga noloop
    dd "Yes."
    scene d15s04-10-rec-talking-with-dd with dissolve
    "Receptionist" "Wonderful."
    "Receptionist" "You can go right in. It's over—"
    scene d15s04-11-dd-talking-with-rec with dissolve
    dd "Oh, I know. Thank you."
    scene d15s04-12-rec-talking-with-dd with dissolve
    play voice4 lissa_ugu2 noloop
    "Receptionist" "Great. The doctor might be away for a bit, but you can just wait inside until they're back."
    scene d15s04-11-dd-talking-with-rec with dissolve
    play voice3 samiya_mmm1 noloop
    dd "Thank you."
    play music white_and_black fadein 1.5
    stop sound2 fadeout 1.5

    play sound sfx_door_closed9
    scene d15s04-13-dd-mc-go-to-the-doc-office with dissolve
    pause
    scene d15s04-14-doc-isnt-in-the-room with dissolve
    pause
    scene d15s04-15-mc-dd-sits-down with dissolve
    pause
    scene d15s04-16-mc-talking-with-dd with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "What's the doctor's name again? Dr. Beer?"
    scene d15s04-17-dd-talking-with-mc with dissolve
    play voice3 daisy_oof noloop
    dd "Oh."
    scene d15s04-18-mc-talking-with-dd with dissolve
    play voice2 d2s12_emmm noloop
    mc "Wait, what? Is it really Dr. Beer?"
    scene d15s04-19-dd-talking-with-mc with dissolve
    play voice3 daisy_uhuh noloop
    dd "No, it's worse. Her full last name is Dr. Bierbottom."
    scene d15s04-20-mc-talking-with-dd with dissolve
    mc "..."
    scene d15s04-21-mc-talking-with-dd with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "I... What!? How? What?"
    scene d15s04-22-dd-talking-with-mc with dissolve
    play voice3 daisy_laugh noloop
    dd "I have no clue."
    scene d15s04-23-mc-talking-with-dd with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "That poor woman... I can't even imagine the bullying she must've gone through."
    scene d15s04-24-dd-talking-with-mc with dissolve
    play voice3 daisy_yes noloop
    dd "I'm not sure how she hasn't changed it yet. Like... I don't get it."
    scene d15s04-26-mc-talking-with-dd with dissolve
    play voice2 mc_scared_huuuh3 noloop
    mc "This also implies that there's a whole dynasty of Bierbottoms out there."
    scene d15s04-25-dd-talking-with-mc with dissolve
    play voice3 daisy_impressed noloop
    dd "Oh God."
    scene d15s04-27-dd-talking-with-mc with dissolve
    dd "A whole army of Bierbottoms."
    dd "God, we're part of the problem."
    scene d15s04-28-mc-talking-with-dd with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "We are, but still... Fucking Bierbottom?"
    scene d15s04-29-dd-talking-with-mc with dissolve
    play voice3 daisy_aah noloop
    dd "It would be awful if she came in right now."
    dd "I'd move towns honestly.{w} Change names."
    scene d15s04-30-mc-talking-with-dd with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "To Bierbottom?"
    scene d15s04-31-dd-talking-with-mc with dissolve
    play voice3 daisy_haha noloop
    dd "*Snorts*"
    scene d15s04-33-mc-talking-with-dd with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I mean, if she has the confidence to rock Bierbottom as a last name, I don't think she's gonna care about us talking about it."
    scene d15s04-32-dd-talking-with-dd with dissolve
    play voice3 daisy_aga noloop
    dd "Hah, good point."
    scene d15s04-35-mc-talking-with-dd with dissolve
    play voice2 d2s9_confused noloop
    mc "How are you feeling?"
    scene d15s04-34-dd-talking-with-mc with dissolve
    play voice3 daisy_thinking noloop
    dd "...I'm alright. Just thinking about stuff."
    scene d15s04-37-mc-talking-with-dd with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "A penny for your thoughts?"
    scene d15s04-36-dd-talking-with-mc with dissolve
    play voice3 daisy_hey noloop
    dd "My thoughts are worth a lot more than that, come on now."
    scene d15s04-28-mc-talking-with-dd with dissolve
    play voice2 d4s4_mclaugh noloop
    mc "*Chuckles* Right, right. Sorry."
    scene d15s04-38-dd-talking-with-mc with dissolve
    play voice3 daisy_oof noloop
    dd "It's just...all of this has got me thinking."
    scene d15s04-39-dd-talking-with-mc with dissolve
    dd "I haven't really lived."
    scene d15s04-40-mc-talking-with-dd with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "...What do you mean?"
    scene d15s04-31-dd-talking-with-mc with dissolve
    play voice3 daisy_ugu noloop
    dd "I've had fun, but I've never been truly happy and content."
    dd "I've messed around, but I've never truly been in love."
    scene d15s04-17-dd-talking-with-mc with dissolve
    dd "I've been in the moment so long that I never planned for the future."
    dd "And now the future has caught up with me and I'm... I don't know what to do."
    dd "I'm scared and I'm lost."
    scene d15s04-41-mc-talking-with-dd with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "Have you thought about getting away from all of this?"
    scene d15s04-42-dd-talking-with-mc with dissolve
    play voice3 aaleyah_disappointed_mff2 noloop
    dd "Hm."
    scene d15s04-35-mc-talking-with-dd with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "And how do you feel about that?"
    scene d15s04-36-dd-talking-with-mc with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    dd "Unsure."
    dd "The more I think about it, the more it feels like...like it might be what I need."
    scene d15s04-31-dd-talking-with-mc with dissolve
    dd "I have enough saved up to make it work...for the most part."
    dd "But I'll need to get a job somewhere."
    scene d15s04-25-dd-talking-with-mc with dissolve
    dd "I've been thinking about setting up a little cabin in the mountains, maybe I can become a lumberjack or something."
    dd "Supply firewood for the town."
    scene d15s04-37-mc-talking-with-dd with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "I think you'd be supplying wood to the town either way."
    scene d15s04-42-dd-talking-with-mc with dissolve
    play voice3 daisy_haha noloop
    dd "*Chuckles*"
    scene d15s04-41-mc-talking-with-dd with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "What's taking Bierbottom so long anyway?"
    scene d15s04-42-dd-talking-with-mc with dissolve
    play voice3 daisy_laugh noloop
    dd "{i}Dr.{/i} Bierbottom."
    scene d15s04-40-mc-talking-with-dd with dissolve
    play voice2 d3s11b_mcheh noloop
    mc "*Chuckles*"

    play sound sfx_door_closed9
    scene d15s04-43-nurse-talking-with-dd with dissolve
    play voice4 amrose_hey_scared noloop
    "???" "Hi, are you Daisy Diamond?"
    scene d15s04-44-dd-talking-with-nurse with dissolve
    dd "Yes?"
    scene d15s04-45-nurse-talking-with-dd with dissolve
    play voice4 amrose_thinking_hmm1 noloop
    "???" "Are you waiting for Dr. Bier?"
    scene d15s04-46-dd-talking-with-nurse with dissolve
    play voice3 daisy_aga noloop
    dd "Yes."
    scene d15s04-47-nurse-talking-with-dd with dissolve
    play voice4 amrose_disappointed_ehh2 noloop
    "???" "I'm really sorry, but Dr. Bier has been called in for an emergency."
    scene d15s04-44-dd-talking-with-nurse with dissolve
    play voice3 daisy_oof noloop
    dd "Oh, is everything alright?"
    scene d15s04-45-nurse-talking-with-dd with dissolve
    play voice4 amrose_yes_ugu noloop
    "???" "Of course, there's nothing you need to worry about. But you will most likely have to wait a while longer."
    scene d15s04-48-mc-talking-with-nurse with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "\"While\"?"
    scene d15s04-49-nurse-talking-with-mc with dissolve
    play voice4 amrose_yes_yeah1 noloop
    "???" "I would say about 20 - 40 minutes. It's hard to say."
    "???" "If you can wait, that's great, but we can get you another appointment at another date as well if you would prefer that."
    scene d15s04-50-dd-talking-with-mc with dissolve
    play voice3 daisy_thinking noloop
    dd "Are you alri—?"
    scene d15s04-51-mc-talking-with-dd with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "I'm fine. We should stay and get this done."
    scene d15s04-52-dd-talking-with-nurse with dissolve
    play voice3 dahlia_yes_ugu noloop
    dd "It's alright. We'll stay for a bit longer."
    scene d15s04-53-nurse-talking-with-dd with dissolve
    play voice4 amrose_thinking_hmm1 noloop
    "???" "Sure. I'm really sorry for the inconvenience."
    scene d15s04-52-dd-talking-with-nurse with dissolve
    play voice3 daisy_uhuh noloop
    dd "It's okay. Thank you."
    scene d15s04-54-nurse-leaves-and-dd-stand-up with dissolve
    pause
    play sound sfx_door_closed8
    queue sound sfx_door_closed9

label replay_d15s04dd hide:
    if _in_replay:
        play music white_and_black fadein 1.5

    scene d15s04-55-mc-talking-with-dd with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "What are you doing?"
    scene d15s04-56-dd-talking-with-mc with dissolve
    play voice3 daisy_haha noloop
    dd "I wanna see what she has in here. She'll take a bit to come anyway, might as well explore."
    scene d15s04-57-mc-stand-up-and-look-at-daisy with dissolve
    dd "Come with me."
    scene d15s04-58-dd-check-out-some-of-stuff with dissolve
    pause
    $ renpy.music.set_volume(1.0, 0.0, "sound")
    play sound sfx_door_creak1
    scene d15s04-59-dd-gasps with dissolve
    play voice3 daisy_impressed noloop
    dd "*Gasps*"
    scene d15s04-60-mc-talking-with-dd with dissolve
    play voice2 d1s2_hmm noloop
    mc "What?"
    scene d15s04-61-mc-talking-with-dd with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "It's a corpse isn't it?"
    scene d15s04-62-mc-see-whats-inside-the-drawer with dissolve
    pause
    scene d15s04-63-mc-talking-with-dd with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Scrubs?"
    scene d15s04-64-dd-talking-with-mc with dissolve
    play voice3 daisy_yay noloop
    dd "Yeah. I've always wanted to dress up as a nurse!"
    scene d15s04-66-dd-talking-with-mc with dissolve
    dd "It might be weird, but I've always had it on my bucket list."
    scene d15s04-65-mc-talking-with-dd with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Wait a minute, are you thinking about dressing up as a nurse {i}right now?{/i}"
    scene d15s04-68-dd-talking-with-mc with dissolve
    play voice3 daisy_aah noloop
    dd "Are you really going to deny a dying woman her last wishes?"
    scene d15s04-67-mc-talking-with- dd with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Alright, first of all. You're not dying. So write that down."
    mc "Second of all, the doctor might come in soon. What if you get caught?"
    scene d15s04-66-dd-talking-with-mc with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    dd "It'll be fine. Cover me."
    scene d15s04-69-mc-talking-with-dd with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "I can't believe you're doing this right now. I could've bought you scrubs if you had just told me."
    scene d15s04-70-dd-talking-with-mc with dissolve
    play voice3 daisy_hey noloop
    dd "Tada! I'm done, turn around."
    scene d15s04-71-mc-looking-at-dd with dissolve
    pause
    scene d15s04-72-mc-looking-at-dd with dissolve
    pause
    scene d15s04-73-dd-talking-with-mc with dissolve
    play voice3 daisy_hmm1 noloop
    dd "What do you think? How do I look?"
    scene d15s04-74-mc-talking-with-dd with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "Ravishing with a side of slightly crazy."
    scene d15s04-75-dd-talking-with-mc with dissolve
    play voice3 daisy_impressed noloop
    dd "Why, thank you."
    scene d15s04-76-dd-saunters-over-to-mc with dissolve
    pause
    scene d15s04-77-dd-talking-with-mc with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    dd "Come with me, the doctor told me to get your vitals."
    scene d15s04-78-dd-grabs-mc-and-bring-him-to-the-chair with dissolve
    pause
    scene d15s04-79-dd-gets-the-stethoscope with dissolve
    pause
    scene d15s04-80-dd-bends-over-and-gets-his-heartbeat with dissolve
    pause
    scene d15s04-81-dd-talking-with-mc with dissolve
    play voice3 dahlia_surprised_oh noloop
    dd "Oh my, your heart is beating very fast. You wouldn't happen to be excited, would you?"
    scene d15s04-82-dd-moves-stethoscope-down with dissolve
    pause
    scene d15s04-83-dd-talking-with-mc with dissolve
    play voice3 daisy_hmm2 noloop
    dd "Oh you're definitely excited now, aren't you?"
    scene d15s04-84-mc-talking-with-dd with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Well, what can I say? It's not everyday I get a physical from an aspiring lumberjack."
    play sound sfx_clothes_undress1
    scene d15s04-85-dd-lets-the-steth-drop with dissolve
    pause

    $ Lovense.stop()

    scene d15s04-86-dd-talking-with-mc with dissolve
    $ Lovense.vibrate(1)
    play voice3 daisy_hmm1 noloop
    dd "Oh gosh. If I'm responsible for this hardwood, I want to try and ease your pain a bit."
    dd "Would you like that?"
    scene d15s04-87-mc-talking-with-dd with dissolve
    play voice2 d1s5b_emmm noloop
    mc "Daisy, wait—"
    play sound ["<silence 0.2>", sfx_comic_attention1]
    stop music fadeout 0.15
    play sound3 sfx_cloth_planket2 noloop
    $ Lovense.stop()
    scene d15s04-88-dd-pulls-down-mc-pant with vpunch
    pause
    mct "Shit."
    scene d15s04-89-dd-talking-with-mc with dissolve
    play voice3 daisy_oof noloop
    dd "Is this what I think it is?"
    play music rudeboy_jazz
    scene d15s04-90-mc-sighs with dissolve
    play voice2 d1s5b_ehhh noloop
    mc "*Sigh*"
    scene d15s04-91-dd-talking-with-mc with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    dd "Did Dahlia do this to you?"
    scene d15s04-92-mc-talking-with-dd with dissolve
    play voice2 mc_no_no2 noloop
    mc "No. It was Fetish Locator."
    scene d15s04-93-dd-talking-with-mc with dissolve
    play voice3 dahlia_surprised_huh2 noloop
    dd "What? How?"
    scene d15s04-94-mc-talking-with-dd with dissolve
    play voice2 mc_disgust_meh4 noloop
    if is_antagonist_mode is False:
        mc "I failed a challenge. My new challenge is this cockcage."
    elif True:
        mc "I failed a challenge. The punishment was a cockcage."
    scene d15s04-95-dd-talking-with-mc with dissolve
    play voice3 daisy_thinking noloop
    dd "Is it impossible to take off?"
    scene d15s04-96-mc-talking-with-dd with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Well, we could probably cut it off, but uh... For one thing, I don't want tools like that near my junk."
    mc "Second, it's remote activated. They can probably detect whether it's been tampered with."
    scene d15s04-97-dd-talking-with-mc with dissolve
    dd "Are you alright? Does it hurt?"
    scene d15s04-98-mc-talking-with-dd
    if cage_ntr is False:
        show d15s04-98-mc-talking-with-dd-2
    with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Well... Yes, a little uncomfortable. But mostly just when I get hard."
    mc "It's a pain in the ass then. Well...pain in my dick."
    scene d15s04-99-dd-talking-with-mc with dissolve
    play voice3 daisy_laugh noloop
    dd "God, I'm so sorry. I didn't know. I wouldn't have—"
    scene d15s04-100-mc-talking-with-dd with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "It's alright. Don't worry about it."
    scene d15s04-101-dd-talking-with-mc with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    dd "We shouldn't do—"
    play voice3 ["<silence 0.3>", dahlia_pain_ah2] noloop
    play sound sfx_bag_fall1
    play sound3 sfx_chair_slide1 noloop
    scene d15s04-102-mc-pulls-dd with hpunch
    pause
    scene d15s04-103-mc-talking-with-dd with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "I mean... Just 'cause {i}I{/i} can't do much, doesn't mean that I can't do anything for {i}you{/i}."
    scene d15s04-104-dd-talking-with-mc with dissolve
    play voice3 daisy_aah noloop
    dd "That's a tempting offer, but I don't want to hurt you."
    dd "And I wanted to make you feel good—"
    scene d15s04-105-mc-talking-with-dd with dissolve
    play voice2 shhh noloop
    mc "Shhh!"
    scene d15s04-106-mc-talking-with-dd with dissolve
    play voice2 d9s2_mcyes noloop
    mc "Just let {i}me{/i} make you feel good."

    play voice3 daisy_scream1 noloop
    $ Lovense.vibrate(1)
    scene d14s04b-01-lick-anim-01_i with dissolve
    pause
    play voice2 d2s12_licking
    play voice3 daisy_moaning2
    $ Lovense.vibrate(3)
    scene d15s04dd-a1
    pause
    scene d15s04dd-a2 with dissolve
    pause
    scene d15s04dd-a4 with dissolve
    pause
    play voice2 d1s5_mcthinks noloop
    scene d15s04-106-mc-talking-with-dd with dissolve
    play voice3 polly_breathing noloop
    mc "You like it when I eat you out, don't you? My dirty little slut."
    scene d15s04dd-a3 with dissolve
    play voice3 daisy_yes noloop
    queue voice3 daisy_moaning2
    play voice2 [d2s12_flicking, d2s12_flicking, d2s12_flicking, d2s12_licking]
    dd "*Loudly moans* Yes... Your tongue feels so good. Ah! Just like that, God."
    pause
    scene d15s04dd-a5-2 with dissolve
    pause

    stop voice2 fadeout 0.6
    stop voice3 fadeout 0.6
    scene d15s04-108-dd-toes-start-to-curl with dissolve
    pause
    play voice3 daisy_scream7 noloop
    scene d14s04b-01-fingering-anim-01_i with dissolve
    pause
    play voice3 amrose_old_moaning2
    play voice2 d7s4_mcbreathing
    play sound2 sfx_handjob_cream1
    $ Lovense.vibrate(5)
    scene d15s04dd-a5
    pause
    scene d15s04dd-a6 with dissolve
    pause
    scene d15s04dd-a7 with dissolve
    pause
    scene d15s04dd-a8 with dissolve
    pause
    scene d15s04dd-a9 with dissolve
    pause
    play voice3 amrose_old_orgasming
    scene d15s04dd-a5-f with dissolve
    dd "*Starts to moan even louder*"
    pause
    scene d15s04dd-a6-f with dissolve
    pause
    scene d15s04dd-a7-f with dissolve
    pause
    scene d15s04dd-a8-f with dissolve
    pause
    scene d15s04dd-a9-f with dissolve
    pause

    stop sound2 fadeout 0.6
    scene d15s04-109-mc-talking-with-dd with dissolve
    play voice3 polly_breathing
    play voice2 mc_angry_errr4 noloop
    mc "Are you gonna cum for me? Hm? Are you gonna cum for me like a good little slut?"
    scene d15s04-110-dd-talking-with-mc with dissolve
    play voice3 daisy_scream8 noloop
    dd "Ye—yes! I— [mcname]!"
    play sound sfx_squirt1
    play voice3 daisy_scream4 noloop
    scene d15s04-111-dd-cums with hpunch
    pause
    play voice3 daisy_scream3 noloop
    scene d15s04-110-dd-talking-with-mc with hpunch
    pause
    play voice3 daisy_aah noloop
    scene d15s04-112-mc-looking-at-dd with dissolve
    pause
    $ Lovense.vibrate(2)
    scene d15s04-113-mc-talking-with-dd with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Did that feel good?"
    scene d15s04-114-dd-talking-with-mc with dissolve
    play voice3 daisy_yes noloop
    dd "It felt {i}really{/i} fucking good."
    play voice3 daisy_moaning
    play sound maria_kiss1
    scene d15s04-115-mc-kiss-dd with dissolve
    pause
    play sound maria_kiss3
    scene d15s04-116-dd-talking-with-mc with dissolve
    pause
    scene d15s04-117-dd-cups-mcs-balls
    if cage_ntr is False:
        show d15s04-117-dd-cups-mcs-balls-2
    with dissolve
    pause
    scene d15s04-118-dd-talking-with-mc with dissolve
    dd "I...can't {i}{b}wait{/b}{/i}, till you're out of this thing."
    scene d15s04-119-dd-talking-with-mc with dissolve
    dd "I'm going to drain you till you have nothing left. I won't let a single drop go to waste. I want it all in me."
    dd "And..."
    scene d15s04-122-dd-talking-with-mc with dissolve
    play voice3 daisy_hmm1 noloop
    dd "You haven't fucked my ass yet, have you?"
    scene d15s04-120-mc-smiles with dissolve
    play voice2 mc_scared_huuuh2 noloop
    pause
    scene d15s04-121-dd-embrace-mc with dissolve
    play voice3 daisy_hmm2 noloop
    dd "Mmm, I. Can't. Wait."

    $ Lovense.stop()

    $ renpy.end_replay()

    scene black with fade
    pause
    $ renpy.music.set_volume(0.4, 8.0, "music")
    scene d15s04-123-dd-putting-away-the-scrubs with fade
    pause
    scene d15s04-124-dd-talking-with-mc with dissolve
    play voice3 daisy_thinking noloop
    dd "Did you clean it all?"
    scene d15s04-125-mc-talking-with-dd with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "I think so. Or she's gonna be in for a nice surprise."
    scene d15s04-126-dd-talking-with-mc with dissolve
    play voice3 daisy_impressed noloop
    dd "Oh God, [mcname]—"
    play sound sfx_door_closed9
    scene d15s04-127-doc-talking-with-dd with dissolve
    play voice4 lissa_thinking noloop
    "Doctor" "Ms. Diamond! I'm extremely sorry about the wait time. I had an emergency that I was called for."
    scene d15s04-128-dd-talking-with-doc with dissolve
    play voice3 daisy_haha noloop
    dd "Oh, it's no problem."
    scene d15s04-129-doc-talking-with-dd with dissolve
    play voice4 lissa_ugu noloop
    "Doctor" "Thank you. Please, sit. I have your test results here..."

    $ renpy.music.set_volume(0.2, 4.0, "music")
    scene black with fade
    pause
    play sound2 subwaycar fadein 1.5
    scene d15s04-130-mc-dd-in-the-subway with fade
    pause
    scene d15s04-131-mc-talking-with-dd with dissolve
    play voice2 mc_scared_oh3 noloop
    mc "Could you imagine if we had been caught?"
    scene d15s04-132-dd-talking-with-mc with dissolve
    play voice3 daisy_uhuh noloop
    dd "I'd rather not."
    dd "I don't know what came over me, but I can't say that it wasn't hot."
    if is_extended_edition is True:
        play sound3 "<from 8.0>audio/freesound/extended/250516_389377-lq.ogg" fadein 1.0 noloop
    stop sound2 fadeout 1.5
    scene d15s04-133-mc-chuckles with dissolve
    play voice2 d4s4_mclaugh noloop
    mc "*Chuckles*"
    scene d15s04-134-subway-stops with dissolve
    pause
    scene d15s04-134-subway-stops-2 with dissolve
    pause
    scene d15s04-135-dd-talking-with-mc with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    dd "You said you had to get off here, right?"
    scene d15s04-136-mc-talking-with-dd with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah..."
    scene d15s04-137-dd-talking-with-mc with dissolve
    play voice3 daisy_hey noloop
    dd "Hey, it's alright. I had fun today, a {i}lot{/i} of fun. It would've been boring as hell without you."
    dd "Thank you for being with me."
    scene d15s04-138-mc-talking-with-dd with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course."
    scene d15s04-139-mc-dd-looking-at-each-other with dissolve
    menu:
        "Kiss her"(hint="d15s04ddm01c01"):
            $ d15s04_dd_kiss = True
            $ unlock_gallery_slot("scene", "d15s04dd")

            scene d15s04-142-opt1-dd-talking-with-mc with dissolve
            play voice3 daisy_oof noloop
            dd "[mcname]..."
            play sound maria_kiss1
            scene d15s04-141-opt1-mc-kiss-dd with dissolve
            pause
        "Don't"(hint="d15s04ddm01c02"):

            pass

    if d15s04_dd_kiss is True:
        scene d15s04-143-opt1-mc-talking-with-dd with dissolve
    elif True:
        scene d15s04-145-opt2-mc-talking-with-dd with dissolve
    play voice2 d1s5_mchappy noloop
    mc "I better go. I'll talk to you later, alright?"
    if d15s04_dd_kiss is True:
        play voice3 daisy_impressed noloop
        scene d15s04-144-opt1-dd-nods with dissolve
    elif True:
        play voice3 daisy_aga noloop
        scene d15s04-146-opt2-dd-talking-with-dd with dissolve
    dd "Hm. Take care."
    $ unlock_gallery_slot("cg", "d15s04dd")
    scene d15s04-147-mc-walk-away with dissolve
    pause
    scene d15s04-147-2-mc-check-his-phone with dissolve
    play sound sfx_message_in1
    call add_points (d15s04dd_points) from _call_add_points
    flr "You earned [d15s04dd_points] points."
    mct "Ok that was for fingering Daisy."
    mct "Does it bring me closer to getting rid of the cage? {w} I hope so..."
    play sound2 subwaycar fadein 2.0
    scene d15s04-147-2-opt2-dd-expression with dissolve
    pause
    stop sound2 fadeout 3.5

    $ renpy.music.set_volume(0.05, 5.0, "music")
    scene black with fade
    pause
    $ renpy.music.set_volume(0.7, 3.0, "music")
    scene d15s04-148-doc-looking-at-some-docs with fade
    pause
    scene d15s04-149-doc-looking-at-book with dissolve
    pause
    scene d15s04-150-doc-looking-at-ground with dissolve
    play voice4 chloe_surprised_huh3 noloop
    "Doctor" "Huh?"
    scene d15s04-151-cum-on-ground with dissolve
    pause
    play voice4 chloe_surprised_oh noloop
    scene d15s04-152-doc-confused with dissolve
    pause

    stop music fadeout 3.5
    jump d15s05

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
