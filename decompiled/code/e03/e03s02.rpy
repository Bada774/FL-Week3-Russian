image e03s02-a18-glambot-1 = Movie(play = "images/E-03/s02/anim/e03s02-a18-2x-50fps.webm", start_image = "e03s02-a18 favor_for_a_friend_mh_talk_mc_sitting-glambot-18-000_i", image = "e03s02-a18 favor_for_a_friend_mh_talk_mc_sitting-glambot-18-198_i", loop = False)

label e03s02:

    scene black
    show screen scene_transistion(_("A couple weeks later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play voice3 stacy_disappointed_snoring fadein 3.0 volume 0.3
    play voice2 d7s6_snoring fadein 1.5
    scene e03s02-00 favor_for_a_friend_sleeeping_sy
    with Fade(0.5, 0.5, 0.5)
    $ renpy.music.set_volume(0.75, 3.0, "music")
    $ renpy.music.set_volume(0.0, 0.0, "music2")
    $ renpy.music.play(audio.music_morning_news, "music" , True, None, True, 0.0)
    $ renpy.music.play(audio.music_morning_news_reverbed, "music2", True, None, True, 0.0)
    pause
    sy "Zzzzzz."
    scene e03s02-01 favor_for_a_friend_sleeeping_mh with dissolve
    play voice4 dahlia_thinking_mmm1 noloop
    mh "Mmmm... mmmm."
    play voice2 d7s6_moan1 noloop
    scene e03s02-02 favor_for_a_friend_mc_thought_halfwake with dissolve
    mct "Mmmm. This is so nice. And Lyssa mentioned she'd get to sleep in today."
    mct "After last night, we all could use the rest."
    scene e03s02-03 favor_for_a_friend_mc_thought_look_mh with dissolve
    play voice2 d1s1_mmm noloop
    mct "Woah. That is a beautiful sight to wake up to."
    scene e03s02-04 favor_for_a_friend_mc_thought_look_sy with dissolve
    mct "And now it's even better than the last time I stayed over at Lyssa's."
    scene e03s02-05 favor_for_a_friend_mc_thought_mc_relax with dissolve
    pause
    scene e03s02-06 favor_for_a_friend_mc_thought_eyes_open with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "Crap. Now I have to pee."
    scene e03s02-07 favor_for_a_friend_mc_thought_arm_trap with dissolve
    pause
    play sound sfx_cloth_rustling2
    scene e03s02-08 favor_for_a_friend_mc_thought_arm_out with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "One."
    play sound sfx_cloth_rustling3
    scene e03s02-09 favor_for_a_friend_mc_thought_arm_lift with dissolve
    mct "And two."
    play sound2 sfx_barefoot_steps1
    scene e03s02-10 favor_for_a_friend_mc_thought_tiptoe_offbed with dissolve
    pause

    call buzz from _call_buzz_48
    scene e03s02-11 favor_for_a_friend_mh_talk_phone_open_eyes with dissolve
    play voice4 dahlia_disappointed_hmm2 noloop
    mh "Mmmhawa."
    play sound2 sfx_door_creak2 noloop
    scene e03s02-12 favor_for_a_friend_mc_thought with dissolve
    play voice2 mc_pain_rrrr noloop
    pause
    scene e03s02-13 favor_for_a_friend_mh_talk_wave_notice with dissolve
    play voice4 daisy_hey noloop
    mh "Hey there."
    scene e03s02-14 favor_for_a_friend_mc_talk with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "Good morning."
    play sound sfx_cloth_rustling2
    scene e03s02-15 favor_for_a_friend_mh_look_phone with dissolve
    pause
    scene e03s02-16 favor_for_a_friend_mc_talk_mh_sigh with dissolve
    play voice2 mc_arrogant_hm2 noloop
    mc "Duty calls?"
    scene e03s02-17 favor_for_a_friend_mh_talk with dissolve
    play voice4 dahlia_yes_yeah3 noloop
    mh "Yes, except it's too early and Oliver shouldn't be in till after lunch."
    scene e03s02-a18 favor_for_a_friend_mh_talk_mc_sitting-glambot-18-000_i with dissolve
    pause 0.01
    play sound [sfx_camera_fly1, sfx_camera_fly1] volume 2.0
    play sound2 ["<silence 2.5>", sfx_camera_fly1] volume 2.0 noloop
    scene e03s02-a18-glambot-1
    pause
    play voice4 dahlia_thinking_hmm4 noloop
    mh "I told him that I'd be having a lazy morning."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene e03s02-19 favor_for_a_friend_mc_talk_mc_sitting with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "Mmm. Sounds good to me."
    scene e03s02-20 favor_for_a_friend_mc_talk_mh_phone with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Everything okay with Oliver?"
    scene e03s02-21 favor_for_a_friend_mh_talk_mh_phone with dissolve
    play voice4 lissa_aga noloop
    mh "I assume so. This message isn't from him."
    scene e03s02-22 favor_for_a_friend_mc_talk_mh_phone with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Who is it from?"
    scene e03s02-23 favor_for_a_friend_mh_talk with dissolve
    play voice4 dahlia_thinking_hmm3 noloop
    mh "And old friend of mine named Stephanie."
    play sound sfx_cloth_rustling1
    scene e03s02-24 favor_for_a_friend_mh_talk_situp with dissolve
    play voice4 dahlia_disappointed_ehh2 noloop
    mh "I need to get showered and get dressed."
    mh "There is a {i}situation{/i}." id e03s02_34f838e3
    scene e03s02-25 favor_for_a_friend_sy_talk_mumbling with dissolve
    play voice3 stacy_disappointed_moan3 noloop
    sy "*half-asleep mumbling*"
    scene e03s02-26 favor_for_a_friend_mh_talk_leaning_shoulder with dissolve
    play voice4 lissa_haha noloop
    mh "Did you get any of that?"
    scene e03s02-27 favor_for_a_friend_mc_talk_smiles with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Stacy asked if she can help."
    mc "And I'd like to extend my own offer of assistance." id e03s02_755b434d
    scene e03s02-28 favor_for_a_friend_mh_talk_look with dissolve
    play voice4 lissa_oh noloop
    mh "You don't have to do that."
    scene e03s02-29 favor_for_a_friend_mc_talk_look with dissolve
    play voice2 d2s9_mchey noloop
    mc "At the very least, we can get you coffee and donuts."
    scene e03s02-30 favor_for_a_friend_kiss with dissolve
    play voice2 mc_thinking_mmm4 noloop
    play voice4 lissa_moan1 noloop
    play sound maria_kiss2
    pause
    scene e03s02-31 favor_for_a_friend_kiss with dissolve
    pause
    scene e03s02-32 favor_for_a_friend_mh_talk with dissolve
    play voice4 dahlia_happy_hmm1 noloop
    mh "*yawns* Mmm. You read my mind."
    play sound sfx_cloth_rustling5
    scene e03s02-33 favor_for_a_friend_mh_talk_getup with dissolve
    mh "Having you two live with me is already revealing hidden perks."
    mh "We should have done this a while ago."
    scene e03s02-34 favor_for_a_friend_mc_talk_mh_yawn with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.5
    mc "Haha."
    play sound sfx_car_startmove fadein 1.0
    scene e03s02-35 favor_for_a_friend_walkinginto_office with Fade(0.5, 1.5, 0.5)
    play sound2 sfx_door_closed7 noloop
    stop sound fadeout 3.0
    pause
    scene e03s02-36 favor_for_a_friend_mh_talk_coffee with dissolve
    play voice4 dahlia_happy_hmm2 noloop
    mh "Thank you, [mcname]."
    scene e03s02-37 favor_for_a_friend_mh_talk_turn_stephanie with dissolve
    play voice4 dahlia_hey_active1 noloop
    mh "This is Stephanie. Steph meet [mcname] and Stacy."
    play sound sfx_cloth_rustling2
    scene e03s02-38 favor_for_a_friend_mc_talk_shakehands_stephanie with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "Nice to meet you Stephanie."
    play voice5 girl36_hey_greeting1 noloop
    sw "It's a treat to meet you, [mcname]."
    play sound sfx_cloth_dress_off1 volume 1.3
    scene e03s02-39 favor_for_a_friend_sy_talk_shakehands_stephanie with dissolve
    play voice5 girl36_yes_aga noloop
    sw "And you too, Stacy."
    scene e03s02-40 favor_for_a_friend_sw_talk_mh with dissolve
    play voice5 girl36_happy_mmm noloop
    sw "Lyssa caught me up with everything that has been going on with her."
    sw "Any friend of Lyssa's is a friend of mine."
    scene e03s02-41 favor_for_a_friend_sw_talk_turnrose_somber with dissolve
    play voice5 girl36_thinking_hmm noloop
    sw "But I'm afraid I didn't ask Lyssa here for just a reunion."
    scene e03s02-42 favor_for_a_friend_mc_talk_wave with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh. Hey."
    scene e03s02-43 favor_for_a_friend_rose_looksaway_mc_thought with dissolve
    mct "Who is this girl?"
    scene e03s02-44 favor_for_a_friend_sw_talk_lyssa_clasp_hand with dissolve
    play voice5 girl36_pain_cough4 noloop
    sw "*clears throat* And this is my friend. Rose."
    scene e03s02-45 favor_for_a_friend_sy_talk_lyssa_wave with dissolve
    play voice3 stacy_hey noloop
    sy "Hello Rose."
    scene e03s02-46 favor_for_a_friend_rd_talk_awkward_swn_frame with dissolve
    rd "..."
    scene e03s02-47 favor_for_a_friend_mc_talk with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Is she alright?"
    scene e03s02-48 favor_for_a_friend_sw_talk_mh with dissolve
    play voice5 girl36_thinking_eem noloop
    sw "Are you sure about this?"
    scene e03s02-49 favor_for_a_friend_mh_talk with dissolve
    play voice4 dahlia_thinking_hmm1 noloop
    mh "I don't want to keep secrets from them."
    scene e03s02-50 favor_for_a_friend_sw_talk_sigh with dissolve
    play voice5 girl36_happy_relief2 noloop
    sw "*sigh*"
    scene e03s02-51 favor_for_a_friend_sw_talk_mc_sy with dissolve
    play voice5 girl36_disappointed_aah noloop
    sw "What I'm about to tell you is... well it's not for the faint of heart."
    scene e03s02-52 favor_for_a_friend_mc_talk_grin with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "I've been through a lot recently. I don't faint easily."
    scene e03s02-53 favor_for_a_friend_sy_talk with dissolve
    play voice3 stacy_surprised_oh1 noloop
    sy "Unless its kangaroos."
    scene e03s02-54 favor_for_a_friend_mc_talk with dissolve
    play voice2 mc_scared_huuuh3 noloop
    mc "What kind of an animal has a pouch to carry smaller versions of themselves?"
    scene e03s02-55 favor_for_a_friend_sw_talk with dissolve
    play voice5 girl36_no_angry1 noloop
    sw "Well, this has nothing to do with kangaroos."
    scene e03s02-56 favor_for_a_friend_mc_talk_sy_talk with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Can't believe you just blurted that out."
    scene e03s02-57 favor_for_a_friend_mc_talk_sw_talk_handup with dissolve
    play voice5 girl36_angry_cough noloop volume 0.75
    sw "Ahem, the situation, that I came here to share with Lyssa concerns a group of individuals."
    sw "A very insidious group."
    scene e03s02-58 favor_for_a_friend_mc_talk_mc_talk with dissolve
    play voice2 d1s5_mchappy noloop volume 1.5
    mc "But no kangaroos."
    scene e03s02-59 favor_for_a_friend_mc_talk_sw_talk with dissolve
    play voice5 girl36_no_angry2 noloop
    sw "No. No kangaroos."
    scene e03s02-60 favor_for_a_friend_mh_talk with dissolve
    play voice4 dahlia_disappointed_ehh3 noloop
    mh "Stephanie, please continue."
    scene e03s02-61 favor_for_a_friend_sw_talk with dissolve
    play voice5 girl36_arrogant_he noloop
    sw "Right, this group is known as the Empyrean Dream. In my capacity as an employee of the District Attorney's office, I've been investigating them over the past year."
    sw "They practice strange archaic rituals. They believe that soon, the time of prophecy will be upon the world."
    sw "And their leader, the mysterious entity known as Dyma will return to reshape the world and bless all true believers with great power and wealth."
    scene e03s02-62 favor_for_a_friend_sw_talk_speech with dissolve
    play voice5 girl36_angry_hmm noloop
    sw "But that's all just a cover for their nefarious acts."
    sw "Once you join the cult, they quickly cut off all contact to your friends and family. They isolate you, twisting you to their agenda."
    scene e03s02-63 favor_for_a_friend_sw_talk_speech with dissolve
    play voice5 girl36_disappointed_eeh noloop
    sw "Obviously, people have their own personal freedom to make their choices. Many people like to feel like they're part of something better."
    scene e03s02-64 favor_for_a_friend_sw_talk_deflated with dissolve
    play voice5 girl36_angry_breath noloop
    sw "But, through Rose, I have learned that any who questions the cult, or... god-forbid, attempt to leave..."
    sw "Are imprisoned within their complex. And that, without a doubt, is against the law. These acts can be prosecuted."
    play sound ["<silence 0.2>", sfx_hands_clap4] volume 0.6
    scene e03s02-65 favor_for_a_friend_mc_talk_excited with dissolve
    play voice2 mc_hey_hey10 noloop
    mc "Cool, so you can take down this cult."
    scene e03s02-66 favor_for_a_friend_sy_talkfelse with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    if persistent.is_special is True:
        sy "Bro, if she could take down the cult on her own, we wouldn't be talking."
    else:
        sy "[mcname], if she could take down the cult on her own, we wouldn't be talking."
    scene e03s02-67 favor_for_a_friend_mc_talk with dissolve
    play voice2 d2s9_confused noloop volume 1.8
    mc "Oh yeah. So then what is the problem?"
    scene e03s02-68 favor_for_a_friend_sw_talk_look_rose with dissolve
    play voice5 girl36_yes_yeah noloop
    sw "In the perfect world, I could put Rose on the stand. She could tell a judge and jury about her experiences within the cult and I could bring them down."
    scene e03s02-69 favor_for_a_friend_sw_talk_bowhead with dissolve
    sw "But Rose has what some could call a checkered past. Putting her up on the witness stand would leave her open to cross-examination."
    scene e03s02-70 favor_for_a_friend_mh_talk_armscrossed with dissolve
    play voice4 dahlia_thinking_hmm3 noloop
    mh "Any defense lawyer worth their salt would poke holes in her story. It's pretty basic stuff."
    scene e03s02-71 favor_for_a_friend_sw_talk with dissolve
    play voice5 girl36_yes_happy2 noloop
    sw "Exactly, and I don't want to put her in that situation unless I have no other choice."
    scene e03s02-72 favor_for_a_friend_rd_talk_sad with dissolve
    play voice6 girl34_happy_relief3 noloop
    rd "I'm sorry."
    scene e03s02-73 favor_for_a_friend_mh_talk_comfort with dissolve
    play voice4 dahlia_no_high3 noloop
    mh "Rose, this is not your fault. We all make mistakes, but that doesn't mean we don't deserve justice when someone hurts us."
    scene e03s02-74 favor_for_a_friend_mc_talk with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Damn straight."
    scene e03s02-75 favor_for_a_friend_sy_talk with dissolve
    play voice3 stacy_yes_ugu1 noloop
    sy "Mmhmm!"
    scene e03s02-76 favor_for_a_friend_rd_talk_lookgroup with dissolve
    play voice6 girl34_thinking_eeh1 noloop
    rd "Okay. So... so what does that mean?"
    scene e03s02-77 favor_for_a_friend_mh_talk with dissolve
    play voice4 dahlia_thinking_hmm2 noloop
    mh "We're going to help you."
    scene e03s02-78 favor_for_a_friend_sy_talk_point with dissolve
    play voice3 stacy_mmm2 noloop
    sy "I don't understand. You work for the district attorney's office. Can't you just report in a tip to the police?"
    scene e03s02-79 favor_for_a_friend_sw_talk with dissolve
    play voice5 girl36_disappointed_oof noloop volume 0.85
    sw "I already tried that before, but the police have never been able to make something stick when they investigate."
    sw "The cult seems especially capable at putting up a good front to cover their activities."
    sw "We don't have enough for a warrant to search inside the compound."
    play sound sfx_bed_slide2 volume 0.6
    scene e03s02-80 favor_for_a_friend_sw_talk_sit_defeated with dissolve
    play voice5 girl36_disappointed_geh noloop
    sw "It's been three months with no results. That's why I decided we are going to have to go a little... outside the law."
    scene e03s02-81 favor_for_a_friend_mh_talk_everyone_serious with dissolve
    play voice4 dahlia_disappointed_hmm1 noloop
    mh "I always prefer to think we're bending the law in very specific times."
    scene e03s02-82 favor_for_a_friend_mc_talk with dissolve
    play voice2 mc_thinking_hm noloop volume 1.5
    mc "Haha. Call it what you like, sounds like an adventure to me."
    scene e03s02-83 favor_for_a_friend_sy_talk_serious with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "Wait, you have to be joking. We can't just bring down a cult."
    scene e03s02-84 favor_for_a_friend_mc_talk_shrug with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Why not? We already brought down a secret sex app that was messing up people's lives."
    mc "This can't be much harder."
    scene e03s02-85 favor_for_a_friend_sy_talk_worried with dissolve
    play voice3 stacy_disappointed_oh1 noloop
    sy "You're crazy."
    play sound sfx_cloth_rustling5
    scene e03s02-86 favor_for_a_friend_mh_talk_shoulder_sy with dissolve
    play voice4 dahlia_thinking_mmm2 noloop
    mh "I thought the same at first. But then I thought of the other people who might still be locked up by the cult."
    mh "They're in trouble, and I couldn't look myself in the mirror if I didn't try to help."
    scene e03s02-87 favor_for_a_friend_sy_talk_shocked with dissolve
    play voice3 stacy_surprised_huh3 noloop
    sy "What is going on today? Lyssa, this is a cult, it could be dangerous."
    scene e03s02-88 favor_for_a_friend_mh_talk_shoulder_sy with dissolve
    play voice4 dahlia_yes_yeah4 noloop
    mh "Which is why, I thought instead of going it alone, I would ask the two of you to help me. It's like they always say."
    mh "There is strength in numbers."
    scene e03s02-89 favor_for_a_friend_mc_talk with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, we can be like the three amigos, protecting the villagers and taking down the corrupt landowners."
    mc "Or in this case, some alien worshiping freaks." id e03s02_1ef99a76
    scene e03s02-90 favor_for_a_friend_sy_talk with dissolve
    play voice3 stacy_yes_fine4 noloop
    sy "Alright."
    scene e03s02-91 favor_for_a_friend_sy_talk_sw with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "But wait, how are we supposed to join the cult?"
    scene e03s02-92 favor_for_a_friend_sy_talk_gesture with dissolve
    sy "It's not like any of us are actors or used to infiltrating groups of bad guys."
    scene e03s02-93 favor_for_a_friend_mh_talk_shoulder_sy with dissolve
    play voice4 lissa_thinking noloop volume 1.4
    mh "Stephanie can explain."
    scene e03s02-94 favor_for_a_friend_sw_talk_sigh with dissolve
    play voice5 girl36_happy_mmm noloop volume 1.5
    sw "So during the investigation, the police and private eyes have kept coming up against brick-walls."
    sw "Every time the cops come, the cults make sure nothing sordid is happening and the cops can't stick around."
    sw "And none of the private eyes have managed to infiltrate the cult."
    scene e03s02-95 favor_for_a_friend_sw_talk_gesture_lyssa with dissolve
    play voice5 girl36_thinking_hmm noloop
    sw "But according to Rose, the cult has recently been interested in trans individuals."
    sw "And naturally, with Lyssa's legal expertise, she'll be able to locate evidence of criminal wrong-doings."
    scene e03s02-96 favor_for_a_friend_mc_talk_thinking with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.5
    mc "So if we get in, and we find evidence of what the cult is up to."
    scene e03s02-97 favor_for_a_friend_sy_talk with dissolve
    play voice3 stacy_arrogant_huh4 noloop
    sy "I'll figure out some devices to help us gather evidence. We'll catch those bastards red-handed."
    scene e03s02-98 favor_for_a_friend_mh_talk_smile with dissolve
    play voice4 dahlia_thinking_oh noloop
    mh "So... you two are sure about helping me on this?"
    play sound sfx_cloth_rustling4
    scene e03s02-99 favor_for_a_friend_sy_talk_hug with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "Mmmm. We're not letting you do this alone."
    scene e03s02-100 favor_for_a_friend_mc_talk with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "Exactly!"
    scene e03s02-101 favor_for_a_friend_mh_talk with dissolve
    play voice4 dahlia_thinking_hmm4 noloop
    mh "Thanks, you two."
    scene e03s02-102 favor_for_a_friend_mh_talk_rose with dissolve
    play voice4 daisy_aga noloop
    mh "We're going to do this, Rose. For you and anyone else the cult has wronged."
    scene e03s02-103 favor_for_a_friend_rd_talk_smile with dissolve
    play voice6 girl34_happy_relief1 noloop
    rd "Thank you, Lyssa."
    scene e03s02-104 favor_for_a_friend_mh_talk_gentle with dissolve
    play voice4 dahlia_yes_ugu noloop
    mh "You're welcome. And we'll need your help too."
    scene e03s02-105 favor_for_a_friend_rd_talk with dissolve
    play voice6 girl34_thinking_emm3 noloop
    rd "I'll... I'll try my best."
    scene e03s02-106 favor_for_a_friend_mh_talk with dissolve
    play voice4 dahlia_yes_yeah2 noloop
    mh "Good. It's going to be easy."
    mh "We just need to know how to find one of the cult's recruiters..."
    scene black
    show screen scene_transistion(_("A few weeks later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound3 d12s2_cafe_crowd fadein 3.5
    scene e03s02-107 favor_for_a_friend_bar_mh_talk
    $ renpy.music.set_volume(0.0, 3.0, "music")
    $ renpy.music.set_volume(1.0, 3.0, "music2")
    with Fade(0.5, 0.5, 0.5)
    pause
    scene e03s02-108 favor_for_a_friend_bar_mc_talk with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "I don't like this."
    scene e03s02-109 favor_for_a_friend_bar_sy_talk with dissolve
    play voice3 stacy_hmm noloop
    sy "Mmmm."
    scene e03s02-110 favor_for_a_friend_bar_mc_talk_sy_notice with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "I said 'I don't like this'."
    scene e03s02-111 favor_for_a_friend_bar_sy_talk with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Well, I didn't like it at the start either. But Lyssa is right, those people need our help."
    scene e03s02-112 favor_for_a_friend_bar_mc_talk_lookmh with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure..."
    mct "That sentiment was a lot easier when Lyssa wasn't talking to some cultist weirdo."
    play sound sfx_paper_slide1
    scene e03s02-113 favor_for_a_friend_bar_mhcult_paper with dissolve
    pause
    play sound2 sfx_bed_slide2 noloop
    queue sound sfx_heels_steps2
    scene e03s02-114 favor_for_a_friend_bar_cultist_getup_leaves with dissolve
    stop sound fadeout 4.0
    pause
    scene e03s02-115 favor_for_a_friend_bar_mh_talk_relief with dissolve
    play voice4 dahlia_happy_phew noloop volume 0.8
    mh "Phew."
    play sound sfx_heels_steps1
    scene e03s02-116 favor_for_a_friend_bar_mc_talk_mh_walk with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Thank god, she's coming over."
    stop sound fadeout 1.0
    scene e03s02-117 favor_for_a_friend_bar_mh_talk_table with dissolve
    play voice4 dahlia_disgust_yah noloop
    mh "Blegh. I want a shower just thinking about how long I had to sit there making nice with them."
    scene e03s02-118 favor_for_a_friend_bar_mc_talk_table with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "Are you alright?"
    play sound sfx_paper_rustl1
    scene e03s02-119 favor_for_a_friend_bar_mh_talk_note with dissolve
    play voice4 dahlia_yes_angry noloop
    mh "Yes. But I'll feel a lot better once we get in there and start taking down this cult from the inside."
    mh "For now, I've got us our ticket in."
    scene e03s02-122 favor_for_a_friend_bar_mc_talk_glad with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Great. The sooner we're done with this, the sooner our life can return to normal."
    play sound2 sfx_cloth_rustling4 noloop
    scene e03s02-123 favor_for_a_friend_bar_mh_talk_kiss with dissolve
    play voice4 lissa_mmm1 noloop
    play sound maria_kiss2
    play voice2 d14s16_smell noloop
    mh "Mmmhmm."
    scene e03s02-124 favor_for_a_friend_bar_mh_talk_kiss with dissolve
    pause
    scene e03s02-125 favor_for_a_friend_bar_mh_talk_smile with dissolve
    play voice4 lissa_haha2 noloop
    mh "Come on now, [mcname]. I've gotten plenty of normal."
    mh "Plus, I didn't really get to help you take down Fetish Locator."
    scene e03s02-127 favor_for_a_friend_bar_mh_talk with dissolve
    play voice4 dahlia_thinking_hmm1 noloop
    mh "But, if you want me to tell Stephanie we're out, I will."
    play sound sfx_cloth_rustling2
    scene e03s02-128 favor_for_a_friend_bar_mc_talk_holdhands with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Nah, you two are right. We have the chance to help."
    mc "We should take it."
    scene e03s02-129 favor_for_a_friend_bar_mh_talk_happy with dissolve
    play voice4 lissa_aga noloop
    mh "Good. Then let's get out of here."
    mh "Tomorrow morning, we're putting the plan into action."
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop sound3 fadeout 2.0

    jump e03s03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
