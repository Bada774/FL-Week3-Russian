image e18s02-a66-glam = Movie(play = "images/E-18/s02/anim/e18s02-a66-2x-50fps.webm", start_image = "e18s02-a66 working_at_the_car_wash_yeah_pb_talk-glambot-66-000_i", image = "e18s02-a66 working_at_the_car_wash_yeah_pb_talk-glambot-66-149_i", loop = False)

label e18s02:

    scene black
    show screen scene_transistion(_("The next day"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.7, 0.0, "music")
    play music music_caribbean_morning fadein 1.5
    play sound3 sfx_sea_guls_1 fadein 1.5 noloop
    play sound4 sfx_seawaves_ambience2 fadein 1.0 volume 0.1
    scene e18s02-00 working_at_the_car_wash_yeah_mc_relaxing
    with Fade(0.5, 0.5, 0.9)
    pause
    $ renpy.music.set_volume(0.45, 6.0, "music")
    play sound sfx_cola_open1 volume 0.6
    scene e18s02-01 working_at_the_car_wash_yeah_mc_thought_beer with dissolve
    queue sound sfx_drink_loop1 volume 2.0 loop
    play voice2 mc_thinking_mmm7 noloop
    mct "Not bad."
    stop sound fadeout 1.0
    scene e18s02-02 working_at_the_car_wash_yeah_mc_thought_finished with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mct "Not bad at all."
    play sound sfx_heels_steps2
    scene e18s02-03 working_at_the_car_wash_yeah_pb_talk_find with dissolve
    stop sound fadeout 2.0
    play voice5 pete_hey_attention noloop
    pb "There you are. You know we're supposed to be cleaning. Dahlia warned us if it's not done well, she'll rip off our ball hair."
    scene e18s02-04 working_at_the_car_wash_yeah_mc_talk_chuckles with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "She's always warning me about ripping off my ball hairs or cutting one of my balls off."
    mc "But she never ends up doing it."
    play sound sfx_drink_slurp2
    scene e18s02-05 working_at_the_car_wash_yeah_mc_talk_drink with dissolve
    pause
    scene e18s02-06 working_at_the_car_wash_yeah_mc_talk_pat with dissolve
    play sound sfx_cup_slide1
    play voice2 mc_happy_a1 noloop
    mc "Constant threats are just her way. She's like that big hairy alien in that space show." id e18s02_fcb64edb
    mc "It's just how she talks. She doesn't mean it."
    scene e18s02-07 working_at_the_car_wash_yeah_pb_talk_unconvinced with dissolve
    play voice5 pete_no_nah noloop
    pb "I can't take that chance."
    pb "I don't want anything happening to little Pete. Come on dude, we're in this together. If we work together, it will be clean before you know it."
    scene e18s02-08 working_at_the_car_wash_yeah_mc_talk_look_around with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "We already cleaned the place."
    scene e18s02-09 working_at_the_car_wash_yeah_pb_talk_look with dissolve
    play voice5 pete_yes_yeah noloop
    pb "Yeah, but now we have to maintain the place. Come on."
    scene e18s02-10 working_at_the_car_wash_yeah_mc_talk_sighs with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "*Sigh*"
    $ renpy.music.set_volume(1.5, 2.0, "music")
    play sound sfx_plate_place1
    play sound5 sfx_heels_steps1 noloop
    scene e18s02-11 working_at_the_car_wash_yeah_mc_talk_walks_over with dissolve
    pause
    stop sound5 fadeout 1.0
    play sound2 sfx_cleaning_floor2
    play sound sfx_cleaning_floor1
    scene e18s02-12 working_at_the_car_wash_yeah_cleaning with dissolve
    pause
    scene e18s02-13 working_at_the_car_wash_yeah_cleaning with dissolve
    pause
    scene e18s02-14 working_at_the_car_wash_yeah_cleaning with dissolve
    pause
    scene e18s02-15 working_at_the_car_wash_yeah_cleaning with dissolve
    pause
    $ renpy.music.set_volume(0.7, 3.0, "music")
    stop sound2 fadeout 2.3
    scene e18s02-16 working_at_the_car_wash_yeah_mc_talk_bag with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Looks like some luggage got left down here."
    scene e18s02-17 working_at_the_car_wash_yeah_pb_talk_bag with dissolve
    play voice5 pete_thinking_oh1 noloop
    pb "You talking about that bag? Yeah, I thought the same thing."
    pb "But I asked Samiya and Dahlia. They both say that they have all of their stuff."
    scene e18s02-18 working_at_the_car_wash_yeah_mc_talk_pb_walk with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "So if no one is missing anything."
    scene e18s02-19 working_at_the_car_wash_yeah_pb_talk_pb with dissolve
    play voice5 pete_arrogant_yeah1 noloop
    pb "Yeah..."
    play sound sfx_footsteps_grass1
    scene e18s02-20 working_at_the_car_wash_yeah_pb_talk_mc_crouch with dissolve
    stop sound fadeout 2.0
    play voice5 pete_hey_angry noloop
    pb "What the fuck?"
    scene e18s02-21 working_at_the_car_wash_yeah_mc_talk with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What?"
    scene e18s02-22 working_at_the_car_wash_yeah_pb_talk with dissolve
    play voice5 pete_surprised_huh1 noloop
    pb "You were just going to open the bag. What if there is a bomb in it?"
    scene e18s02-23 working_at_the_car_wash_yeah_mc_talk with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "A bomb? Someone randomly just left a bomb at an abandoned car wash."
    scene e18s02-24 working_at_the_car_wash_yeah_pb_talk with dissolve
    play voice5 pete_yes_simple2 noloop
    pb "It could happen."
    play sound sfx_tent_closed1 volume 0.5
    scene e18s02-25 working_at_the_car_wash_yeah_mc_talk_openbag with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "We really never should have taken you off the court, buddy."
    scene e18s02-26 working_at_the_car_wash_yeah_pb_talk_openbag with dissolve
    play voice5 pete_angry_argh1 noloop
    pb "Fuck you."
    $ renpy.music.set_volume(1.0, 0.0, "music2")
    play music2 music_caribbean_morning_surprisemfck2 noloop
    stop music fadeout 0.8
    play sound sfx_pills_shaking1
    play sound2 sfx_skirt_off2 noloop
    scene e18s02-27 working_at_the_car_wash_yeah_mc_talk_shocked with hpunch
    queue music music_error404_ver1
    play voice2 d2s12_emmm noloop
    mc "I think we're both fucked."
    scene e18s02-28 working_at_the_car_wash_yeah_pb_talk_shocked with dissolve
    pb "..."
    scene e18s02-29 working_at_the_car_wash_yeah_pb_talk_look_other with dissolve
    play voice5 pete_disgust_oof2 noloop
    pb "What do we do now? That bag is full of pill bottles."
    scene e18s02-30 working_at_the_car_wash_yeah_mc_talk_look_other with dissolve
    play voice2 mc_thinking_mmm5 noloop volume 1.5
    mc "We keep a lid on this."
    scene e18s02-31 working_at_the_car_wash_yeah_pb_talk_look_other with dissolve
    play voice5 pete_surprised_what3 noloop
    pb "What?"
    play sound sfx_cloth_planket2
    scene e18s02-32 working_at_the_car_wash_yeah_mc_talk_standingbag with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "Just trust me. If Dahlia found out, she'd probably just freak out and want us to bail."
    scene e18s02-33 working_at_the_car_wash_yeah_pb_talk with dissolve
    play voice5 pete_yes_simple3 noloop
    pb "And I'd agree with her."
    scene e18s02-34 working_at_the_car_wash_yeah_mc_talk with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah but what about Samiya? She's gone out a limb to get here."
    mc "We can't let a little hiccup screw over her changes at a new life."
    scene e18s02-35 working_at_the_car_wash_yeah_pb_talk_worried with dissolve
    play voice5 pete_arrogant_huh2 noloop
    pb "So what do we do?"
    play sound sfx_locker_open1 volume 1.5
    play sound2 ["<silence 0.4>", sfx_vending_door1] noloop
    scene e18s02-36 working_at_the_car_wash_yeah_pb_talk_mc_cabinet with dissolve
    play sound3 sfx_pills_shaking1 noloop volume 0.7
    queue sound sfx_vending_cola
    queue sound2 sfx_skirt_off2 noloop
    play voice5 pete_thinking_eeh1 noloop
    pb "What if they find it?"
    play sound sfx_locker_closed1 volume 2.0
    play sound2 sfx_vending_door1 noloop
    scene e18s02-37 working_at_the_car_wash_yeah_mc_talk_mc_cabinet with dissolve
    play voice2 mc_no_nah2 noloop
    mc "It's behind the cleaning supplies and they keep making us clean."
    mc "Dahlia will never look in here."
    stop music fadeout 3.0
    $ renpy.music.set_volume(0.7, 0.0, "music3")
    play sound sfx_heels_steps1 volume 0.5
    scene e18s02-38 working_at_the_car_wash_yeah_dw_talk_hear_call with dissolve
    play voice3 dahlia_arrogant_huh noloop
    dw "Where are our pets?"
    play music3 music_caribbean_morning fadein 0.1
    play sound sfx_heels_steps2 loop
    scene e18s02-39 working_at_the_car_wash_yeah_pb_talk_wave with dissolve
    play voice5 pete_hey_heyo noloop
    pb "Hey Samiya."
    stop sound fadeout 1.0
    scene e18s02-40 working_at_the_car_wash_yeah_mc_talk with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Mistress. I'm glad you've returned."
    scene e18s02-41 working_at_the_car_wash_yeah_dw_talk_mc_submissive with dissolve
    play voice3 dahlia_thinking_oh noloop
    dw "Ah, how sweet. What are you up to?"
    scene e18s02-42 working_at_the_car_wash_yeah_mc_talk_sides with dissolve
    play voice2 mc_surprised_oh1 noloop
    mc "Nothing. Just been cleaning up the place. Like you asked."
    scene e18s02-43 working_at_the_car_wash_yeah_sb_talk with dissolve
    play voice4 samiya_laughing1 noloop
    sb "Excellent. Hope you're ready for some more cleaning."
    play sound "<from 0 to 6.0>audio/zvukipro/extended/paperwork/sfx_paper_bag_1.ogg"
    scene e18s02-44 working_at_the_car_wash_yeah_sb_talk_sponge with dissolve
    play voice4 girl35_thinking_hmm1 noloop
    sb "Dahlia and I got everything we need to get this place going as a car wash again."
    scene e18s02-45 working_at_the_car_wash_yeah_mc_talk_bondage with dissolve
    play voice2 d2s9_confused noloop volume 1.4
    mc "And uh, something for the off-hours?"
    scene e18s02-46 working_at_the_car_wash_yeah_dw_talk_grin with dissolve
    play voice3 dahlia_old_laugh1 noloop
    dw "You wish."
    scene e18s02-47 working_at_the_car_wash_yeah_sb_talk_all with dissolve
    play voice4 samiya_yes2 noloop
    sb "So we went to the store and got the sponges and soap and everything else for the car wash."
    sb "And as we were coming back, we came across the local BDSM store." id e18s02_e9d108b9
    scene e18s02-48 working_at_the_car_wash_yeah_dw_talk_happy with dissolve
    play voice3 dahlia_yes_yeah3 noloop
    dw "Naturally, we had to make a stop. See what styles the island has compared to home."
    dw "And we realized, how fun it would be to make you guys into fuckboy washer-boys."
    scene e18s02-49 working_at_the_car_wash_yeah_pb_talk with dissolve
    play voice5 pete_surprised_eh noloop
    pb "Do we really need to be fuckboys and washer-boys?"
    scene e18s02-50 working_at_the_car_wash_yeah_mc_talk with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah I always saw myself as a {b}fuckman{/b}."
    queue voice2 mc_thinking_wait1 noloop
    mc "Wait. That came out wrong."
    play voice3 dahlia_happy_laugh6 noloop
    scene e18s02-51 working_at_the_car_wash_yeah_pb_talk_laugh with dissolve
    pause
    play sound sfx_whip_slap6
    play sound2 sfx_skirt_off2 noloop volume 1.5
    scene e18s02-53 working_at_the_car_wash_yeah_dw_talk_crack with vpunch
    "CRACK!"
    play voice3 dahlia_angry_argh1 noloop
    dw "You will be fuck boys and you will like it."
    scene e18s02-54 working_at_the_car_wash_yeah_pb_mc_talk with dissolve
    play voice5 pete_yes_questioning noloop
    play voice2 mc_yes_yes6 noloop
    "{color=#03ad68}Pete{/color} and {color=#5480ff}[mcname]{/color}" "Yes Mistress!"
    scene e18s02-55 working_at_the_car_wash_yeah_sb_laugh with dissolve
    play voice4 samiya_haha1 noloop volume 1.7
    pause
    scene e18s02-56 working_at_the_car_wash_yeah_sb_talk_bag with dissolve
    play voice4 girl35_yes_aga3 noloop
    sb "You two can get dressed out here. We'll take a look around and see how your cleaning went."
    scene e18s02-57 working_at_the_car_wash_yeah_dw_talk with dissolve
    play voice3 dahlia_yes_simple noloop
    dw "Yes. Then we'll decide just how badly to punish you."
    play sound sfx_paper_bag_2
    scene e18s02-58 working_at_the_car_wash_yeah_mc_talk with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Eep."
    play sound2 sfx_heels_steps1
    play sound3 sfx_heels_steps2
    scene e18s02-59 working_at_the_car_wash_yeah_dw_sb_leave with dissolve
    pause
    play sound2 sfx_door_openclosed2 noloop
    stop sound3 fadeout 1.0
    scene e18s02-60 working_at_the_car_wash_yeah_pb_talk with dissolve
    play voice5 pete_angry_ehh2 noloop
    pb "I can't believe they want us to get dressed out here."
    scene e18s02-61 working_at_the_car_wash_yeah_mc_talk with dissolve
    play voice2 mc_arrogant_nah1 noloop volume 1.4
    mc "Come on. We're close enough to the beach. I'm sure they get lots of people undressing around here."
    mc "Just be quick."
    play sound sfx_jeans_on1
    play sound2 sfx_bag_fall1 noloop
    scene e18s02-62 working_at_the_car_wash_yeah_changing with dissolve
    pause
    play sound sfx_skirt_off2
    play sound2 sfx_clothes_undress1 noloop volume 1.5
    scene e18s02-63 working_at_the_car_wash_yeah_changing with dissolve
    pause
    play sound sfx_cloth_planket2
    scene e18s02-64 working_at_the_car_wash_yeah_changing with dissolve
    pause
    scene e18s02-65 working_at_the_car_wash_yeah_sb_talk_sb_dw_domming with dissolve
    pause
    scene e18s02-66 working_at_the_car_wash_yeah_pb_talk with dissolve
    play voice2 mc_thinking_mmm2 noloop volume 1.4
    mc "Woah. You two look great."
    play voice5 pete_hey_sexy noloop volume 0.8
    pb "Yeah. I'm down for whatever you want, Mistress."
    scene e18s02-a66 working_at_the_car_wash_yeah_pb_talk-glambot-66-000_i with Dissolve(0.35)
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.0>", sfx_camera_fly1] noloop volume 2.0
    scene e18s02-a66-glam
    pause
    play voice4 samiya_hah1 noloop
    sb "Good doggie."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene e18s02-68 working_at_the_car_wash_yeah_mc_talk_sb_cabinet_pb_worried with dissolve
    play voice4 girl35_thinking_hmf1 noloop
    play sound sfx_heels_steps1 loop
    sb "I'm thinking anal beads. Time to give that ass of yours some fun, Pete."
    play voice2 mc_hey_hey4 noloop
    mc "Wait. I was just in there, I uh... didn't see any anal beads there."
    play voice4 samiya_hm1 noloop volume 1.4
    sb "Okay."
    play sound sfx_locker_open1 volume 1.5
    play sound2 sfx_vending_door1 noloop
    play sound3 "<from 0 to 2.0>audio/dlc1_pack0224/zvukipro/extended/cloth/sfx_cloth_shuffle1.ogg" noloop
    queue sound sfx_leg_kick7
    play sound5 sfx_pills_shaking1 noloop
    queue sound2 sfx_flag_wiggle1 noloop
    stop music3 fadeout 1.0
    play music2 music_caribbean_morning_surprisemfck noloop
    scene e18s02-70 working_at_the_car_wash_yeah_sb_talk_fall with dissolve
    play voice4 samiya_heeh noloop
    sb "What?"
    play sound sfx_bag_fall1 volume 2.0
    scene e18s02-71 working_at_the_car_wash_yeah_sb_talk_ground with dissolve
    $ renpy.music.set_volume(0.0, 0.0, "music")
    $ renpy.music.set_volume(1.0, 0.0, "music2")
    $ renpy.music.play(audio.music_error404_ver3, "music" , True, None, True, 0.0)
    $ renpy.music.play(audio.music_error404_ver2, "music2", True, None, True, 0.0)
    play voice4 samiya_huh5 noloop
    sb "Wait, where did this come from?"
    scene e18s02-72 working_at_the_car_wash_yeah_dw_talk_open_bag with dissolve
    play voice3 dahlia_angry_argh2 noloop
    dw "Explain worm."
    scene e18s02-73 working_at_the_car_wash_yeah_mc_talk with dissolve
    play voice2 d1s5b_emmm noloop volume 1.9
    mc "I have no idea."
    scene e18s02-74 working_at_the_car_wash_yeah_dw_talk with dissolve
    play voice3 dahlia_angry_ah2 noloop
    dw "You just said that you were in the cabinet earlier."
    dw "You better loosen your tongue or I will-"
    play sound sfx_tent_closed1 volume 0.6
    scene e18s02-75 working_at_the_car_wash_yeah_sb_talk_shock with dissolve
    pause
    play voice4 samiya_huh noloop
    scene e18s02-76 working_at_the_car_wash_yeah_sb_talk_shock with hpunch
    sb "What the fuck is this?"
    play voice2 d3s7_mcemm noloop volume 1.6
    play voice5 pete_pain_mmm6 noloop
    scene e18s02-77 working_at_the_car_wash_yeah_mcpb_look_other with dissolve
    pause
    scene e18s02-78 working_at_the_car_wash_yeah_mc_talk_point with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Pete's steroids."
    play voice5 pete_surprised_what1 noloop
    scene e18s02-79 working_at_the_car_wash_yeah_pb_talk_angry with dissolve
    pb "What the fuck dude?"
    pb "You know I'm all natural."
    scene e18s02-80 working_at_the_car_wash_yeah_dw_talk with dissolve
    play voice3 dahlia_angry_oh noloop
    dw "And he already has enough problems with getting it up." id e18s02_2d361f4b
    scene e18s02-81 working_at_the_car_wash_yeah_pb_talk_all_four with dissolve
    play voice5 pete_happy_yeah1 noloop
    pb "Yeah."
    scene e18s02-82 working_at_the_car_wash_yeah_pb_talk_turn_dw with dissolve
    play voice5 pete_angry_dagh1 noloop
    pb "Wait... fuck you."
    scene e18s02-83 working_at_the_car_wash_yeah_dw_talk_angry with dissolve
    play voice3 dahlia_surprised_huh1 noloop
    dw "What was that?"
    play voice5 pete_thinking_hmm5 noloop
    pb "Fuck you, Mistress?"
    play sound sfx_heels_steps1
    scene e18s02-84 working_at_the_car_wash_yeah_sb_talk with dissolve
    play voice4 samiya_huh4 noloop
    sb "You can punish him later."
    stop sound fadeout 1.0
    scene e18s02-85 working_at_the_car_wash_yeah_sb_talk_mc with dissolve
    play voice4 samiya_hmm1 noloop volume 1.7
    sb "[mcname], tell us everything. From the top."
    scene e18s02-86 working_at_the_car_wash_yeah_mc_talk with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "We found it today. We were going to tell you as soon as we figured out what to do with it."
    scene e18s02-87 working_at_the_car_wash_yeah_dw_talk with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    dw "I apologize for my worthless worm."
    dw "It's not the first time I wished his dick was attached to a better brain."
    play sound sfx_cloth_rustling2
    play sound2 sfx_pills_shaking1 noloop volume 0.5
    play sound3 sfx_leg_kick8 noloop volume 0.6
    scene e18s02-88 working_at_the_car_wash_yeah_sb_talk_bag_mc with dissolve
    play voice4 samiya_hm2 noloop
    sb "I want you to march out to the ocean and toss this in."
    scene e18s02-89 working_at_the_car_wash_yeah_dw_talk with dissolve
    play voice3 dahlia_arrogant_ha noloop
    dw "Or we could sell it."
    scene e18s02-90 working_at_the_car_wash_yeah_sb_talk_pete_worrried with dissolve
    play voice4 samiya_ah noloop volume 1.5
    sb "Sell it? Are you crazy?"
    scene e18s02-91 working_at_the_car_wash_yeah_dw_talk with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    dw "What?"
    scene e18s02-92 working_at_the_car_wash_yeah_sb_talk with dissolve
    play voice4 samiya_kghhh noloop
    sb "This is Santa Domina, not a college campus. You get caught selling drugs here and it's not a slap on the wrist."
    scene e18s02-93 working_at_the_car_wash_yeah_pb_talk with dissolve
    play voice5 pete_thinking_eeh2 noloop
    pb "Guys..."
    scene e18s02-94 working_at_the_car_wash_yeah_dw_talk with dissolve
    play voice3 dahlia_happy_laugh3 noloop
    dw "Alright, it was just an idea."
    dw "But I think you're overreacting. It wasn't like you and I were going to take the risks."
    scene e18s02-95 working_at_the_car_wash_yeah_mc_talk with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "Mistress!"
    scene e18s02-96 working_at_the_car_wash_yeah_dw_talk with dissolve
    play voice3 dahlia_old_argh3 noloop
    dw "What?"
    $ renpy.music.set_volume(0.8, 3.0, "music")
    play sound sfx_car_startmove
    scene e18s02-97 working_at_the_car_wash_yeah_dw_talk_police with dissolve
    play sound2 sfx_police_siren_short1 noloop
    pause
    $ renpy.music.set_volume(0.0, 10.0, "music2")
    scene e18s02-98 working_at_the_car_wash_yeah_dw_talk_police with dissolve
    play voice3 dahlia_pain_ah1 noloop
    dw "Oh fuck my ass."
    scene e18s02-99 working_at_the_car_wash_yeah_pb_talk_police with dissolve
    play voice5 pete_disappointed_oof2 noloop
    pb "That's what I've been trying to tell you."
    scene e18s02-100 working_at_the_car_wash_yeah_dw_talk_freaking with dissolve
    play voice3 dahlia_pain_ah2 noloop
    dw "I can't go to prison."
    dw "I'd never survive being someone else's bitch."
    play sound3 sfx_heels_steps2 noloop
    scene e18s02-101 working_at_the_car_wash_yeah_sb_talk_mctrash with dissolve
    play voice4 samiya_cagh noloop
    sb "You can say that again."
    play sound3 sfx_vending_door1 noloop
    play sound2 sfx_metal_fence1 noloop volume 1.5
    play sound5 "<from 0 to 1.3>audio/dlc1_pack0224/zvukipro/extended/cloth/sfx_cloth_shuffle1.ogg" noloop
    scene e18s02-102 working_at_the_car_wash_yeah_sb_talk_notice_mc with dissolve
    play voice4 girl35_thinking_hm2 noloop
    sb "Good thinking, [mcname]."
    play sound sfx_car_approach1
    scene e18s02-103 working_at_the_car_wash_yeah_sb_talk_carstop with dissolve
    play voice4 girl35_thinking_hmm5 noloop
    sb "Just take a deep breath. I'm going to get us out of this."
    sb "And follow my lead."
    play sound2 sfx_car_door_open1 noloop
    play sound sfx_heels_steps1 loop
    play sound3 sfx_heels_steps2
    scene e18s02-104 working_at_the_car_wash_yeah_sb_talk_wave with dissolve
    pause
    stop sound fadeout 1.0
    stop sound3 fadeout 1.0
    scene e18s02-105 working_at_the_car_wash_yeah_cop_talk with dissolve
    play voice6 boy5_hey_calm noloop
    "Cop" "Good morning."
    scene e18s02-106 working_at_the_car_wash_yeah_sb_talk with dissolve
    play voice4 girl35_hey_laughing noloop
    sb "Good morning, officers. Come to get your car washed?"
    scene e18s02-107 working_at_the_car_wash_yeah_cop_talk_shrug with dissolve
    play sound sfx_cucumber_bite1
    play voice6 boy5_yes_yep noloop
    "Cop" "Of course, Miss. You guys are the new owners?"
    play sound2 sfx_skirt_off1 noloop
    scene e18s02-108 working_at_the_car_wash_yeah_sb_talk_shake hands with dissolve
    play voice4 girl35_yes_aga9 noloop
    sb "That's me. Samiya Byers. My co-owner is Dahlia, and we're at your service."
    scene e18s02-109 working_at_the_car_wash_yeah_sb_talk_turnto_mcpete with dissolve
    play voice4 girl35_angry_cough2 noloop
    sb "Get to work."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene e18s02-110 working_at_the_car_wash_yeah__mcpete_move_away with dissolve
    pause
    stop sound fadeout 1.5
    stop sound2 fadeout 1.5
    scene e18s02-111 working_at_the_car_wash_yeah_cop_talk with dissolve
    play voice6 boy5_thinking_huh noloop volume 1.4
    "Cop" "These men are your employees?"
    scene e18s02-112 working_at_the_car_wash_yeah_sb_talk with dissolve
    play voice4 samiya_yes1 noloop
    sb "Something like that.."
    sb "He's [mcname], and that is Pete."
    scene e18s02-113 working_at_the_car_wash_yeah_sb_talk_flirt with dissolve
    play voice4 samiya_mmm3 noloop volume 1.4
    sb "Your timing is perfect. We were about to go to the beach."
    scene e18s02-114 working_at_the_car_wash_yeah_cop_talk with dissolve
    play voice6 boy5_surprised_oh1 noloop
    "Cop" "In those?"
    scene e18s02-115 working_at_the_car_wash_yeah_sb_talk_giggle with dissolve
    play voice4 girl35_yes_yeah3 noloop
    sb "Yeah. Little mix-up with our luggage."
    sb "We lost all of our bathing suits."
    scene e18s02-116 working_at_the_car_wash_yeah_sb_talk_gesture with dissolve
    play voice4 girl35_happy_mmm2 noloop volume 1.5
    sb "But since you're here, you can enjoy our premium service. Free of charge, of course."
    scene e18s02-117 working_at_the_car_wash_yeah_cop_talk with dissolve
    play voice6 boy5_surprised_oh2 noloop
    "Cop" "What is that?"
    scene e18s02-118 working_at_the_car_wash_yeah_sb_talk with dissolve
    play voice4 girl35_happy_laugh4 noloop
    sb "Excellent question. Dahlia?"
    scene e18s02-119 working_at_the_car_wash_yeah_dw_talk with dissolve
    play voice3 dahlia_yes_yeah2 noloop
    dw "Right. Well, we tried this out back home, but we were eager to try it out here." id e18s02_c33dd4f8
    dw "As you can tell, our staff work in exotic bondage gear to provide our customers with a delicious sight while we hand-wash your ride."
    dw "The premium part is we put the same care into cleaning your car that our pets put into serving their masters."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene e18s02-120 working_at_the_car_wash_yeah_dw_talk_tell with dissolve
    play sound3 sfx_washing_with_sponge1
    play voice3 dahlia_hey_active1 noloop
    dw "Get in deeper, slave. I want to see my reflection on those rims!"
    stop sound2 fadeout 1.0
    play sound sfx_whip_slap5
    scene e18s02-121 working_at_the_car_wash_yeah_dw_talk_hit_mac with hpunch
    play voice2 mc_pain_auh4 noloop
    mc "Yeouch."
    mc "Yes mistress..."
    play voice3 dahlia_angry_hm2 noloop
    dw "Put your back into it, you ox. Don't embarrass me in front of the policemen."
    play sound sfx_whip_slap6
    scene e18s02-124 working_at_the_car_wash_yeah_pb_talk_dw_smack with dissolve
    play voice5 pete_pain_ouch2 noloop
    pb "Giah. Thank you, Mistress. I'm sorry, mistress."
    scene e18s02-125 working_at_the_car_wash_yeah_cop_talk_laugh with dissolve
    play voice7 boy8_happy_laugh3 noloop
    play voice6 boy5_happy_laugh6 noloop
    "Cop" "Hahah."
    play sound sfx_cloth_wiping1 volume 1.8
    scene e18s02-126 working_at_the_car_wash_yeah_cop_talk_finish_sandwich with dissolve
    play voice6 boy5_arrogant_tshah noloop
    "Cop" "De mesye sa yo se subs. Nou ta dwe pran yon foto pou montre mesye yo."
    "Cop" "Just throw it in the dumpster."
    play sound sfx_heels_steps1
    scene e18s02-127 working_at_the_car_wash_yeah_cop_walks_to_trash with dissolve
    pause
    stop sound fadeout 1.0
    play voice3 dahlia_hey_greeting noloop
    $ renpy.music.set_volume(0.4, 1.5, "sound3")
    scene e18s02-128 working_at_the_car_wash_yeah_sb_talk_walkup_to_cop with dissolve
    pause
    play sound sfx_cloth_rustling2 volume 1.6
    scene e18s02-129 working_at_the_car_wash_yeah_dw_talk_grab_forearm with dissolve
    play voice3 dahlia_yes_ugu noloop
    dw "Please let me take care of that officer."
    play sound sfx_cloth_rustling3
    scene e18s02-130 working_at_the_car_wash_yeah_dw_talk_bicep with dissolve
    play voice3 dahlia_surprised_wow noloop
    dw "Oh wow. Your forearm feels like steel. You must work out a lot."
    dw "What do you bench? Like two hundred? Two fifty. Must be high..."
    scene e18s02-131 working_at_the_car_wash_yeah_mc_thought with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "Just relax. Don't panic. Dahlia is handling it. Wait, suddenly I feel worried about not being worried."
    play sound sfx_heels_steps1
    scene e18s02-132 working_at_the_car_wash_yeah_dw_walks_to_trash with dissolve
    pause
    play sound sfx_vending_door1 noloop
    play sound2 sfx_metal_fence1 noloop volume 1.5
    $ renpy.music.set_volume(0.1, 1.0, "sound3")
    scene e18s02-133 working_at_the_car_wash_yeah_dw_walks_to_trash_throw with dissolve
    pause
    play sound sfx_heels_steps1
    $ renpy.music.set_volume(1.0, 1.5, "sound3")
    scene e18s02-134 working_at_the_car_wash_yeah_dw_talks_point_mc_angry with dissolve
    play voice3 dahlia_angry_ah1 noloop
    dw "Come on, no slacking off."
    stop sound fadeout 1.0
    scene e18s02-135 working_at_the_car_wash_yeah_sb_talks with dissolve
    play voice4 samiya_laughing1 noloop
    sb "Haha, yeah, I make sure to stay fit. But my friend was the track and field pro."
    scene e18s02-136 working_at_the_car_wash_yeah_sb_talk_sexypose with dissolve
    play voice4 girl35_thinking_hmm3 noloop
    sb "Good genes I guess."
    scene e18s02-137 working_at_the_car_wash_yeah_mc_talk_cop_look_mc with dissolve
    play voice2 d2s9_mchey noloop
    mc "Everything alright?"
    scene e18s02-138 working_at_the_car_wash_yeah_mc_thought_cop_look_mc with dissolve
    play voice2 mc_angry_errr5 noloop
    mct "What is this guy's deal?"
    play sound sfx_cloth_rustling4
    scene e18s02-139 working_at_the_car_wash_yeah_dw_talk_touch with dissolve
    play voice3 dahlia_old_moan1 noloop
    dw "You don't talk much do you? That's okay. I like the strong... silent types."
    play sound2 sfx_police_walkie_talkie_order1 noloop
    scene e18s02-140 working_at_the_car_wash_yeah_cop_talk_radio with dissolve
    "*static on the walkie talkie*"
    scene e18s02-141 working_at_the_car_wash_yeah_pn_mc_stare with dissolve
    play voice6 boy5_yes_aga noloop
    "Cop" "Si."
    scene e18s02-142 working_at_the_car_wash_yeah_samiya_nervous_looking_at_trash with dissolve
    play voice6 boy5_yes_angry2 noloop
    "Cop" "Got it."
    play voice4 samiya_mmm1 noloop volume 2.5
    sb "Mmm."
    scene e18s02-143 working_at_the_car_wash_yeah_samiya_smile_cop_talk with dissolve
    play voice6 boy5_disappointed_ehh1 noloop
    "Cop" "Sorry ladies, we'll have to cut this short."
    "Cop" "Duty calls. You know how it is."
    scene e18s02-144 working_at_the_car_wash_yeah_samiya_talk with dissolve
    play voice4 samiya_yes3 noloop
    sb "Of course! So sorry to see you go."
    stop sound3 fadeout 1.0
    scene e18s02-145 working_at_the_car_wash_yeah_dw_talk_car_clean with dissolve
    play voice3 dahlia_yes_happy noloop
    dw "Yes. But we hope you like what we managed to do so far."
    dw "Feel free to come back anytime."
    scene e18s02-146 working_at_the_car_wash_yeah_cop_talk_car_clean with dissolve
    play voice7 boy8_arrogant_phah noloop
    "Cop" "Of course. It already looks five times better. We'll be sure to come back."
    scene e18s02-147 working_at_the_car_wash_yeah_cop_talk_look_mc_pb with dissolve
    play voice7 boy8_thinking_hmm1 noloop
    "Cop" "Your men are good. But you should consider getting a little down and dirty yourself, momma."
    scene e18s02-148 working_at_the_car_wash_yeah_sb_talk with dissolve
    play voice4 samiya_hmm1 noloop volume 1.7
    sb "Hmmm?"
    play sound sfx_car_door_open1 volume 1.5
    scene e18s02-149 working_at_the_car_wash_yeah_copsn_car with dissolve
    pause
    play sound sfx_car_window1
    scene e18s02-150 working_at_the_car_wash_yeah_cop_talk with dissolve
    play voice7 boy8_disappointed_ahh noloop
    "Cop" "A couple girls like you, wearing {i}that{/i}... I could be here for hours."
    scene e18s02-151 working_at_the_car_wash_yeah_sb_talk with dissolve
    play voice4 samiya_ou1 noloop volume 2.0
    sb "Oh. Well we'll be sure to consider it. Thanks for coming by."
    scene e18s02-152 working_at_the_car_wash_yeah_cop_talk with dissolve
    play voice7 boy8_yes_yeah noloop
    "Cop" "Of course. Welcome to Santa Domina. Be safe out there, gorgeous." id e18s02_9317bad4
    scene e18s02-153 working_at_the_car_wash_yeah_cop_talk_mc_pb_dw_watch with dissolve
    play voice7 boy8_disappointed_nah noloop
    "Cop" "The island is beautiful, but it has some bad people in the cracks."
    "Cop" "I wouldn't want anything to happen to you."
    scene e18s02-154 working_at_the_car_wash_yeah_cop_talk_grins_at_mc_pb_dw_watch with dissolve
    play voice7 boy8_hey_arrogant noloop
    "Cop" "Or your wonderful staff."
    play sound sfx_car_startmove
    play sound2 sfx_car_drive1 fadein 2.0
    scene e18s02-155 working_at_the_car_wash_yeah_cop_drive_away_sb_wave with dissolve
    stop sound2 fadeout 5.0
    pause
    scene e18s02-156 working_at_the_car_wash_yeah_cop_drive_away_dw_talk_scared with dissolve
    play voice3 dahlia_pain_sobs noloop
    dw "He knows!"
    scene e18s02-157 working_at_the_car_wash_yeah_cop_drive_away_sb_talk_sigh with dissolve
    play voice4 samiya_hah1 noloop volume 1.4
    sb "If he knew, we'd be in cuffs, getting ready for a grope and a cavity search."
    sb "[mcname], get that bag out of the trash and bring it inside."
    $ renpy.music.set_volume(0.0, 6.0, "music")
    $ renpy.music.set_volume(0.6, 3.0, "music2")
    play sound sfx_heels_steps2 loop
    scene e18s02-158 working_at_the_car_wash_yeah_cop_drive_away_mc_walk_to_trash_dw_worried with dissolve
    pause
    stop sound4 fadeout 2.0

    jump e18s02_apartment

label e18s02_apartment:

    play sound sfx_door_openclosed1
    scene e18s02-159 working_at_the_car_wash_yeah_cop_drive_away_dw_apartment with Fade(0.5, 0.5, 0.5)
    play voice3 dahlia_surprised_ohmy noloop
    dw "That was too close. Shit."
    scene e18s02-160 working_at_the_car_wash_yeah_cop_drive_away_mc_talk with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "So what do we do now?"
    scene e18s02-161 working_at_the_car_wash_yeah_cop_drive_away_pb_talkdea with dissolve
    play voice5 pete_disappointed_aah1 noloop
    pb "I say we torch the drugs."
    scene e18s02-162 working_at_the_car_wash_yeah_cop_drive_away_dw_talk with dissolve
    play voice3 dahlia_yes_angry noloop
    dw "Or chuck them into the sea, like we planned originally."
    scene e18s02-163 working_at_the_car_wash_yeah_cop_drive_away_sb_talk with dissolve
    play voice4 samiya_eeem1 noloop
    sb "We will get rid of them. Just not today, Dahlia."
    sb "The cops could be sitting around the corner, waiting for us to do something stupid."
    scene e18s02-164 working_at_the_car_wash_yeah_cop_drive_away_pb_talk with dissolve
    play voice5 pete_surprised_huh1 noloop
    pb "You don't think they were just here for a car wash."
    scene e18s02-165 working_at_the_car_wash_yeah_cop_drive_away_sb_talk with dissolve
    play voice4 samiya_ou2 noloop
    sb "My gut smells bullshit. Maybe they wanted to just check us out. Maybe they were thinking about shaking us down."
    sb "Either way, I'd rather not risk it."
    scene e18s02-167 working_at_the_car_wash_yeah_cop_drive_away_mc_talk with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "But you said if they knew, we'd be in cuffs already."
    scene e18s02-166 working_at_the_car_wash_yeah_cop_drive_away_sb_talk_shake_head with dissolve
    play voice4 girl35_thinking_hmf2 noloop
    sb "A lesson I learned from hooking. Always cover your ass. For now, we'll keep the bag hidden."
    scene e18s02-167 working_at_the_car_wash_yeah_cop_drive_away_mc_talk with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "I'm starting to get worried about this, Samiya."
    scene e18s02-168 working_at_the_car_wash_yeah_sb_talk_grin with dissolve
    play voice4 samiya_huh3 noloop
    sb "Well, worry in fucking silence."
    scene e18s02-169 working_at_the_car_wash_yeah_mc_talk with dissolve
    play voice2 mc_surprised_wow2 noloop
    mc "Jeez."
    scene e18s02-170 working_at_the_car_wash_yeah_sb_talk_softens with dissolve
    play voice4 samiya_cugh noloop
    sb "You don't-"
    queue voice4 samiya_mmm2 noloop
    sb "*sighs* Sorry, [mcname]. I haven't had to lie to cops in a while. My stomach feels like two snakes trying to strangle each other."
    play sound sfx_cloth_rustling2
    scene e18s02-171 working_at_the_car_wash_yeah_sb_talk_shoulders with dissolve
    play voice4 girl35_disappointed_mff2 noloop
    sb "But I think we're safe. And with a little more luck, it will work out, [mcname]."
    scene e18s02-172 working_at_the_car_wash_yeah_sb_talk_all_worried with dissolve
    play voice4 girl35_yes_ugu6 noloop
    sb "We just got to be cool and stick together."
    scene e18s02-173 working_at_the_car_wash_yeah_pb_talk_breaks_silence with dissolve
    play voice5 pete_disappointed_geh1 noloop
    pb "I don't know about you guys, but I could eat a shit ton of that jerked chicken and flying fish at the cafe down the road."
    scene e18s02-174 working_at_the_car_wash_yeah_sb_talk with dissolve
    play voice4 samiya_yes1 noloop
    sb "Good idea. Here, that should cover it."
    play sound sfx_paper_slide1 volume 1.8
    scene e18s02-175 working_at_the_car_wash_yeah_pb_talk_hand_money with dissolve
    play voice5 pete_hey_happy noloop
    pb "You looked super hot, keeping those cops busy, Samiya."
    scene e18s02-176 working_at_the_car_wash_yeah_sb_talk_shakehead with dissolve
    play voice4 samiya_huh2 noloop
    sb "Seriously dickhead? We just narrowly escaped prison, and you want to fuck?"
    scene e18s02-177 working_at_the_car_wash_yeah_pb_talk with dissolve
    play voice5 pete_surprised_huh4 noloop
    pb "What? I can't be the only one."
    pb "The whole time the cops were here, I was thinking about how many packs of cigs I could sell my ass for."
    pb "Now that we're safe, I want to make the most of it."
    scene e18s02-178 working_at_the_car_wash_yeah_sb_talk_laugh with dissolve
    play voice4 girl35_happy_laugh3 noloop
    sb "Hahaha. Always the charmer, Pete."
    scene e18s02-179 working_at_the_car_wash_yeah_dw_talk_hips with dissolve
    play voice3 dahlia_arrogant_heh noloop
    dw "First things first, you two go get us some grub."
    dw "Then after lunch, if we're in a good mood, we can talk rewards."
    scene e18s02-180 working_at_the_car_wash_yeah_mc_talk_excited with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Yes, Mistress."
    play sound sfx_heels_steps2 volume 1.6 loop
    scene e18s02-181 working_at_the_car_wash_yeah_mc_pete_exit with dissolve
    pause
    play sound sfx_door_openclosed1

    stop music fadeout 3.0
    stop music2 fadeout 3.0
    jump e18s03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
