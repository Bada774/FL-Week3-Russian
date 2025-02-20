image e10s03-a65-1 = Movie(play = "images/E-10/s03/anim/e10s03-a65-1-2x-60fps.webm", start_image = "e10s03-a65-1 mc-mes-montage-anal-00001")
image e10s03-a66-2 = Movie(play = "images/E-10/s03/anim/e10s03-a66-1-2x-60fps.webm", start_image = "e10s03-a66-1 mc-mes-couch-sex-00001")
image e10s03-a67-3 = Movie(play = "images/E-10/s03/anim/e10s03-a67-1-2x-60fps.webm", start_image = "e10s03-a67-1 mc-mes-cock-lick-00001")

label e10s03:

    scene black
    show screen scene_transistion(_("Some time later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound ["<silence 1.0>", sfx_door_open6]
    scene e10s03-01 mc-peeking_c1
    with Fade(0.5, 0.5, 0.9)
    $ renpy.music.set_volume(0.3, 3.0, "music")
    queue music music_everyday_thesame
    pause
    play sound sfx_door_closed2
    scene e10s03-02 mc-mes-enter_c1 with dissolve
    pause
    play voice2 stacy_surprised_whistle noloop
    scene e10s03-02 mc-mes-enter_c2 with dissolve
    mc "*Whistles* Damn. This is one bougie apartment."
    scene e10s03-03 mc-mes-impressed_c2 with dissolve
    play voice3 min_yes_yeah1 noloop
    mes "Yeah..."
    scene e10s03-04 mc-mes-looking-around_c2 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "I wonder how much this place costs?"
    scene e10s03-05 mc-mes-pensive_c2 with dissolve
    play voice3 min_thinking_hmm1 noloop
    mes "Who knows? My dad doesn't care about the bill."
    scene e10s03-06 mc-mes-angry_c2 with dissolve
    play voice3 min_angry_breath noloop
    mes "{i}The daughter of the \"illustrious CEO\" needs to have a publicly glamorous apartment.{/i}"
    scene e10s03-07 mc-mes-couch_c2 with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "What do you mean?"
    scene e10s03-08 mc-mes-min-pacing_c2 with dissolve
    play voice3 min_angry_argh2 noloop
    mes "It means it's all a ploy to keep up appearances to the outside world."
    mes "My comfort is just a nice little bonus."
    play sound sfx_glass_bottle_bonk volume 0.5
    scene e10s03-09 mc-mes-bottle-up_c2 with dissolve
    play voice3 min_old_shy noloop volume 4.8 fadein 0.8
    mes "{size=22}It's all about control.{/size}"
    scene e10s03-10 mc-mes-bottle-down_c1 with dissolve
    play sound sfx_cup_place1
    play voice2 mc_arrogant_heh3 noloop
    mc "Control?"
    mc "Damn if I wouldn't like to be controlled like {i}this{/i}."
    play voice3 min_arrogant_pff noloop
    scene e10s03-10 mc-mes-bottle-down_c2 with dissolve
    mes "..."
    scene e10s03-11 mc-mes-mc-grimace_c1 with dissolve
    play voice2 d1s1_mmm noloop
    mct "Well shit. That completely bombed."
    scene e10s03-12 mc-mes-hug_c2 with dissolve
    play voice2 d2s9_mchey noloop
    mc "Hey. It's going to be alright."
    mc "I wish that you could just do what you want to. But I understand the obligation you feel to your family."
    scene e10s03-13 mc-mes-min-smile_c1 with dissolve
    play voice3 min_arrogant_hm noloop
    mes "I appreciate that."
    play sound maria_kiss1
    scene e10s03-14 mc-mes-kiss_c1 with dissolve
    pause
    scene e10s03-15 mc-mes-min-question_c1 with dissolve
    play voice3 min_happy_relief noloop
    mes "But enough about my situation. What are you going to do?"
    mes "Do you really want to spend the Summer here with me?"
    scene e10s03-15 mc-mes-min-question_c2 with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Of course! Where else would I go?"
    scene e10s03-16 mc-mes-mc-gesture_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "I'm in an amazing country with so many things to do and learn and I'm here with my beautiful girlfriend."
    mc "What more could I ask for?"
    play voice3 min_scared_ah1 noloop
    play sound sfx_skirt_off1 volume 2.5
    scene e10s03-17 mc-mes-mc-carry-min_c1 with dissolve
    mes "*Yelps*"
    play voice2 mc_happy_hah2 noloop
    mc "Now what do you say we go put that comfy couch to some use?"
    scene e10s03-17 mc-mes-mc-carry-min_c2 with dissolve
    play voice3 min_yes_simple noloop
    mes "That's the best idea I've heard all week."
    $ renpy.music.set_volume(0.7, 3.0, "music")
    scene e10s03-18 mc-mes-mc-carry-min_c1 with dissolve
    pause
    scene e10s03-19 mc-wake-up-couch-naked_c1 with Fade (0.5, 0.5, 0.5,)
    pause
    scene e10s03-20 mc-wake-up-couch-naked_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.4, 2.0, "music")
    play voice2 d7s6_moan1 noloop volume 1.4
    scene e10s03-20 mc-wake-up-couch-naked_c2 with dissolve
    mc "*Yawns*"
    scene e10s03-21 mc-mes-getting-dressed_c1 with dissolve
    play voice2 mc_angry_huh1 noloop
    mc "Min?"
    scene e10s03-21 mc-mes-getting-dressed_c2 with dissolve
    play voice3 min_hey_greeting noloop
    mes "Good morning. You sure slept well."
    play sound sfx_cloth_rustling2
    scene e10s03-22 mc-mes-getting-dressed_c1 with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah... Morning. Why are you up so early?"
    scene e10s03-22 mc-mes-getting-dressed_c2 with dissolve
    play voice3 min_disappointed_off noloop
    mes "I have work, remember?"
    play voice2 d7s6_moan2 noloop volume 1.5
    scene e10s03-23 mc-mes-stretching_c1 with dissolve
    mc "Oh yeah..."
    mc "I slept like a baby."
    scene e10s03-24 mc-mes-failed-hug_c1 with dissolve
    play voice3 min_no_angry noloop
    mes "No. Not right now. I just ironed them. I don't want them to wrinkle."
    scene e10s03-25 mc-mes-slightly-hurt_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh... Okay, sorry."
    scene e10s03-25 mc-mes-slightly-hurt_c2 with dissolve
    play voice3 min_pain_sobs2 noloop
    mes "I jus— *Sighs* I'm sorry. It's just I'm already stressed and anxious, and I want to look well put together for my first day."
    scene e10s03-26 mc-mes-holding-hand_c1 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Hey. I understand. It's okay."
    scene e10s03-26 mc-mes-holding-hand_c2 with dissolve
    play voice3 min_disappointed_ehh2 noloop
    mes "Thank you."
    play sound maria_kiss2
    scene e10s03-27 mc-mes-cheek-kiss_c2 with dissolve
    pause
    scene e10s03-28 mc-mes-asking_c2 with dissolve
    play voice3 min_thinking_hmm2 noloop
    mes "Okay. I should get back to it. I need to get there early."
    mes "Are you sure you're gonna be okay?"
    scene e10s03-29 mc-mes-mc-fine_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Don't worry about me. I'll be just—"
    play sound sfx_door_closed2
    scene e10s03-29-01 mc-mes-mc-fine_c1 with dissolve
    play voice2 mc_angry_huh2 noloop volume 1.6
    mc "Fine..."
    scene e10s03-29-02 mc-shrug_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "...Well, I might as well get busy."
    play sound sfx_tv_off2
    scene e10s03-29-03 mc-tv-on_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Maybe I'll see what all this fuss with this about K-drama stuff is about."
    $ renpy.music.set_volume(0.8, 3.0, "music")
    scene e10s03-33 mc-mes-montage_c1 with dissolve
    pause
    scene e10s03-34 mc-mes-montage_c1 with dissolve
    pause
    scene e10s03-35 mc-mes-montage_c1 with dissolve
    pause
    scene e10s03-30 mc-mes-montage_c1 with dissolve
    pause
    scene e10s03-36 mc-mes-montage_c1 with dissolve
    pause
    scene e10s03-41 mc-mes-montage_c1 with dissolve
    pause
    scene e10s03-31 mc-mes-montage_c1 with dissolve
    pause
    scene black
    show screen scene_transistion(_("Later that evening"))
    with Fade(0.5, 0.5, 0.5)
    pause
    $ renpy.music.set_volume(0.3, 3.0, "music")
    hide screen scene_transistion
    play sound sfx_door_closed1
    scene e10s03-29-04 mc-mes-falling-asleep-min-coming-home_c1
    with Fade(0.5, 0.5, 0.5)
    pause
    scene e10s03-29-05 mc-mes-mc-wakes-up-happy_c1 with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "Hey! I missed you!"
    scene e10s03-29-06 mc-mes-hug_c1 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "How was your first day at work?"
    play sound sfx_cloth_rustling4
    scene e10s03-29-07 mc-mes-min-couch_c1 with dissolve
    play voice3 min_disappointed_ehh1 noloop
    mes "Exhausting."
    scene e10s03-29-08 mc-mes-removing-shoe_c1 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Damn. What'd they have you do? Hard labor?"
    scene e10s03-29-08 mc-mes-removing-shoe_c2 with dissolve
    play voice3 min_disappointed_mph noloop
    mes "Worse. I was basically paraded around the company and introduced to people."
    mes "I would've preferred hard labor."
    play sound sfx_shoes_off1
    scene e10s03-29-09 mc-mes-mc-chuckle-min-stretch_c1 with dissolve
    play voice2 d4s4_mclaugh noloop volume 1.7
    mc "*Chuckles* I'm sure it'll get better once you get into the groove of it."
    scene e10s03-29-09 mc-mes-mc-chuckle-min-stretch_c2 with dissolve
    play voice3 min_happy_mmm noloop
    mes "Yeah, hopefully."
    scene e10s03-29-10 mc-mes-min-leaning_c2 with dissolve
    play voice3 min_old_argh noloop
    mes "I think I'm just going to go pass out. I'm way too tired to exist right now."
    scene e10s03-29-11 mc-mes-min-removing-clothes_c1 with dissolve
    play voice2 d2s9_confused noloop
    mc "Do you want me to order some dinner real quick, though?"
    scene e10s03-29-12 mc-mes-min-door-talk_c1 with dissolve
    play voice3 min_no_nah noloop
    mes "No, it's okay. I had dinner with dad and some of the board members."
    scene e10s03-29-13 mc-disheartened_c2 with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Oh... Okay."
    mct "I'll just heat something up for myself then."

    jump e10s03_motage

label replay_e10s03:
label e10s03_motage:

    if not _in_replay:
        scene black
        show screen scene_transistion(_("The next day"))
        with Fade(0.5, 0.5, 0.5)
        pause
        hide screen scene_transistion
    if _in_replay:
        play music music_everyday_thesame
    $ renpy.music.set_volume(0.85, 3.0, "music")
    scene e10s03-68 mc-mes-montage_c1
    with Fade(0.5, 0.5, 0.5)
    pause(0.5)
    scene e10s03-30 mc-mes-montage_c1 with dissolve
    pause(0.5)
    scene e10s03-37 mc-mes-montage_c1 with dissolve
    pause(0.5)
    scene e10s03-39 mc-mes-montage_c1 with dissolve
    pause(0.5)
    scene e10s03-51 mc-mes-montage_c1 with dissolve
    pause(0.5)
    scene e10s03-54 mc-mes-montage_c1 with dissolve
    pause(0.5)
    scene e10s03-55 mc-mes-montage-night_c1 with Dissolve (0.7)
    pause(0.5)
    scene e10s03-60 mc-mes-montage-night_c1 with dissolve
    pause(0.5)
    scene e10s03-a65-1 with dissolve
    pause(1.0)
    scene e10s03-69 mc-mes-montage-night_c1 with dissolve
    pause(0.6)
    scene black
    show screen scene_transistion(_("New day new possibilities"))
    with dissolve
    pause(0.5)
    hide screen scene_transistion
    scene e10s03-68 mc-mes-montage_c1
    with dissolve
    pause(0.5)
    scene e10s03-34 mc-mes-montage_c1 with dissolve
    pause(0.5)
    scene e10s03-38 mc-mes-montage_c1 with dissolve
    pause(0.5)
    scene e10s03-40 mc-mes-montage_c1 with dissolve
    pause(0.5)
    scene e10s03-54-02 mc-mes-montage_c1 with dissolve
    pause(0.5)
    scene e10s03-44 mc-mes-montage_c1 with dissolve
    pause(0.5)
    scene e10s03-56 mc-mes-montage-night_c1 with dissolve
    pause(0.5)
    scene e10s03-60 mc-mes-montage-night_c1 with dissolve
    pause(0.5)
    scene e10s03-a66-2 with dissolve
    pause(1.0)
    scene e10s03-69 mc-mes-montage-night_c1 with dissolve
    pause(0.5)
    scene black
    show screen scene_transistion(_("New day new beginning"))
    with dissolve
    pause(0.6)
    hide screen scene_transistion
    scene e10s03-68 mc-mes-montage_c1
    with dissolve
    pause(0.4)
    scene e10s03-32 mc-mes-montage_c1 with dissolve
    pause(0.5)
    scene e10s03-42 mc-mes-montage_c1 with dissolve
    pause(0.4)
    scene e10s03-54-03 mc-mes-montage_c1 with dissolve
    pause(0.4)
    scene e10s03-50 mc-mes-montage_c1 with dissolve
    pause(0.4)
    scene e10s03-52 mc-mes-montage_c1 with dissolve
    pause(0.4)
    scene e10s03-57 mc-mes-montage-night_c1 with dissolve
    pause(0.4)
    scene e10s03-61 mc-mes-montage-night_c1 with dissolve
    pause(0.4)
    scene e10s03-a67-3 with dissolve
    pause(0.9)
    scene e10s03-69 mc-mes-montage-night_c1 with dissolve
    pause(0.5)

    scene e10s03-68 mc-mes-montage_c1 with dissolve
    pause(0.4)
    scene e10s03-37 mc-mes-montage_c1 with dissolve
    pause(0.4)
    scene e10s03-54-04 mc-mes-montage_c1 with dissolve
    pause(0.4)
    scene e10s03-33 mc-mes-montage_c1 with dissolve
    pause(0.4)
    scene e10s03-44 mc-mes-montage_c1 with dissolve
    pause(0.4)
    scene e10s03-45 mc-mes-montage_c1 with dissolve
    pause(0.4)
    scene e10s03-56 mc-mes-montage-night_c1 with dissolve
    pause(0.4)
    scene e10s03-61 mc-mes-montage-night_c1 with dissolve
    pause(0.4)
    scene e10s03-63 mc-mes-montage-night_c1 with dissolve
    pause(0.4)
    scene e10s03-69 mc-mes-montage-night_c1 with dissolve
    pause(0.5)

    scene e10s03-68 mc-mes-montage_c1 with dissolve
    pause(0.3)
    scene e10s03-38 mc-mes-montage_c1 with dissolve
    pause(0.3)
    scene e10s03-40 mc-mes-montage_c1 with dissolve
    pause(0.3)
    scene e10s03-41 mc-mes-montage_c1 with dissolve
    pause(0.3)
    scene e10s03-52 mc-mes-montage_c1 with dissolve
    pause(0.3)
    scene e10s03-54-03 mc-mes-montage_c1 with dissolve
    pause(0.3)
    scene e10s03-55 mc-mes-montage-night_c1 with dissolve
    pause(0.3)
    scene e10s03-60 mc-mes-montage-night_c1 with dissolve
    pause(0.3)
    scene e10s03-a66-2 with dissolve
    pause(0.7)
    scene e10s03-69 mc-mes-montage-night_c1 with dissolve
    pause(0.4)

    scene e10s03-68 mc-mes-montage_c1 with dissolve
    pause(0.3)
    scene e10s03-33 mc-mes-montage_c1 with dissolve
    pause(0.3)
    scene e10s03-35 mc-mes-montage_c1 with dissolve
    pause(0.3)
    scene e10s03-43 mc-mes-montage_c1 with dissolve
    pause(0.3)
    scene e10s03-54-05 mc-mes-montage_c1 with dissolve
    pause(0.3)
    scene e10s03-54-04 mc-mes-montage_c1 with dissolve
    pause(0.3)
    scene e10s03-58 mc-mes-montage-night_c1 with dissolve
    pause(0.3)
    scene e10s03-61 mc-mes-montage-night_c1 with dissolve
    pause(0.3)
    scene e10s03-63 mc-mes-montage-night_c1 with dissolve
    pause(0.3)
    scene e10s03-69 mc-mes-montage-night_c1 with dissolve
    pause(0.4)

    scene e10s03-68 mc-mes-montage_c1 with dissolve
    pause(0.25)
    scene e10s03-31 mc-mes-montage_c1 with dissolve
    pause(0.25)
    scene e10s03-41 mc-mes-montage_c1 with dissolve
    pause(0.25)
    scene e10s03-45 mc-mes-montage_c1 with dissolve
    pause(0.25)
    scene e10s03-54-05 mc-mes-montage_c1 with dissolve
    pause(0.25)
    play sound sfx_lightsword_on1 volume 0.3 
    scene e10s03-47 mc-mes-montage_c1 with dissolve
    pause(0.25)
    stop sound fadeout 0.4
    scene e10s03-59 mc-mes-montage-night_c1 with dissolve
    pause(0.25)
    scene e10s03-62 mc-mes-montage-night_c1 with dissolve
    pause(0.25)
    scene e10s03-64 mc-mes-montage-night_c1 with dissolve
    pause(0.25)
    scene e10s03-69 mc-mes-montage-night_c1 with dissolve
    pause(0.4)

    scene e10s03-68 mc-mes-montage_c1 with dissolve
    pause(0.25)
    scene e10s03-36 mc-mes-montage_c1 with dissolve
    pause(0.25)
    scene e10s03-30 mc-mes-montage_c1 with dissolve
    pause(0.25)
    play sound sfx_throw_something1 volume 0.3 
    scene e10s03-46 mc-mes-montage_c1 with dissolve
    pause(0.25)
    play sound sfx_epic_jump1 volume 0.3
    scene e10s03-53 mc-mes-montage_c1 with dissolve
    pause(0.25)
    stop sound fadeout 0.4
    scene e10s03-48 mc-mes-montage_c1 with dissolve
    pause(0.25)
    scene e10s03-49 mc-mes-montage_c1 with dissolve
    pause(1.0)
    $ renpy.music.set_volume(0.3, 3.0, "music")

    jump e10s03_motage_end

label e10s03_motage_end:

    scene e10s03-71 mc-breathes-out_c1 with Fade(0.3, 0.3, 0.3)
    play voice2 mc_thinking_mmm4 noloop volume 1.6
    mc "Aauuuummmm."
    $ renpy.end_replay()
    $ unlock_gallery_slot("scene", "e10s03")
    play sound sfx_door_open1
    scene e10s03-72 mes-enters-apartment_c1 with dissolve
    play voice3 min_hey_simple noloop
    mes "I'm home—!"
    play sound sfx_door_closed2
    scene e10s03-73 mes-calling-mc-worried_c1 with dissolve
    play voice3 min_surprised_ehh1 noloop
    mes "...[mcname]?"
    scene e10s03-74 mc-does-not-react_c1 with dissolve
    pause
    scene e10s03-75 mes-gets-closer-still-worried_c1 with dissolve
    play voice3 min_old_huh noloop
    mes "[mcname]? What are you doing?"
    scene e10s03-76 mc-talks-decides-save-them_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "I've decided to save us."
    scene e10s03-78 mes-very-concerned-not-knowing_c1 with dissolve
    play voice3 min_arrogant_huh2 noloop
    mes "...Huh?"
    scene e10s03-79 mc-opens-eyes-mes-asking-save-from-what_c1 with dissolve
    mes "Save us from what?"
    scene e10s03-80 mc-gestures-surroundings_c1 with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "From this.{w} From this dull and mundane life."
    mc "From this existence where we watch idly as life drifts away. This life where we barely touch each other anymore."
    play voice3 min_thinking_mhh noloop
    scene e10s03-81 mes-stands-up-amused_c1 with dissolve
    pause
    scene e10s03-82 mes-asking-how-exactly-will-be-saved_c1 with dissolve
    play voice3 min_surprised_huh2 noloop
    mes "And how exactly do you intend to \"save us\" from this?"
    scene e10s03-83 mc-holds-mes-hands_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "By making your dream come true!"
    scene e10s03-84 mes-incredulous-asking-about-her-dream_c1 with dissolve
    play voice3 min_arrogant_huh1 noloop
    mes "My dream being...?"
    scene e10s03-85 mc-raises-hands-tells-idea_c1 with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "High-frequency trading by using sentiment analysis!"
    scene e10s03-86 mes-perks-up_c1 with dissolve
    play voice3 min_surprised_what noloop
    mes "...What? What are you saying?"
    scene e10s03-87 mc-leads-mes-by-hand_c1 with dissolve
    play voice2 d1s5b_ehhh noloop
    mc "Min, I'll be honest. I've been bored out of my mind staying here, all alone without you."
    mc "Not to mention, I see how tired it makes you to work at that job."
    scene e10s03-88 mc-mentions-the-abriviation_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "So I decided to take matters into my own hands."
    mc "If I have an abundance of anything, it's time, so I've been using that time to research and learn more about HFTUSA—though I haven't had time to workshop a good name for it."
    scene e10s03-89 mes-chuckles_c1 with dissolve
    play voice3 min_old_laugh noloop
    mes "That's a terrible acronym."
    scene e10s03-90 mc-idea-to-specialize_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "It really is."
    mc "Anyway. I know that this is what you want to do, and after having looked into it, I find it really interesting as well!"
    mc "So then an idea came to me. Why don't we make a company that specializes in that?"
    mc "With your knowledge and my business acumen, we could do it!"
    scene e10s03-91 mes-unsure_c1 with dissolve
    play voice3 min_thinking_emm noloop
    mes "[mcname] I'm not sure... Especially with my work—"
    scene e10s03-92 mes-steps-up-smirks_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "I knew you'd say that. And that's why you will only be helping me when you can."
    scene e10s03-93 mc-points-himself_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "{i}I'll{/i} take care of the rest of it. I already have a solid business plan going."
    scene e10s03-94 mes-still-unsure_c1 with dissolve
    play voice3 min_disappointed_ehh3 noloop
    mes "...I don't know..."
    scene e10s03-95 mc-takes-mes-by-waist_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Min, I know you're not satisfied with this life either. You can do so much more than this. {i}Achieve{/i} so much more."
    mc "But I know that you can't do that while also working at your father's place.{w} So let me {i}help{/i}.{w} Together, we can do this."
    scene e10s03-96 mes-looking-determined_c1 with dissolve
    play voice3 min_thinking_hmm3 noloop
    mes "...You said you had a business plan?"
    scene e10s03-97 mc-back-away-mes-smirks_c1 with dissolve
    pause
    scene e10s03-98 mc-celebration-pose_c1 with dissolve
    play voice2 mc_angry_errr4 noloop
    mc "Yes! That's what I'm talking about."
    mc "Alright, sit your butt down and get comfy 'cause we're gonna be here a while."
    play voice3 polly_laugh2 noloop
    $ unlock_gallery_slot("cg", "e10s03")
    scene e10s03-99 mes-laughs_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.7, 3.0, "music")
    scene e10s03-100 mc-mes-brainstorm-montage-one_c1 with fade
    pause
    scene e10s03-101 mc-mes-brainstorm-montage-two_c1 with fade
    pause
    scene e10s03-102 mc-mes-brainstorm-montage-three_c1 with fade
    pause
    scene e10s03-103 mc-mes-brainstorm-montage-four_c1 with fade
    pause
    stop music fadeout 4.5

    jump e10s04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
