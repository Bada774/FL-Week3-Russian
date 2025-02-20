image e18s06-a26-glambot = Movie(play = "images/E-18/s06/anim/e18s06-a26-2x-50fps.webm", start_image = "e18s06-a26 business_is_booming_montage_lo_wet-glambot-26-000_i", image = "e18s06-a26 business_is_booming_montage_lo_wet-glambot-26-179_i", loop = False)

label e18s06:

    scene black
    show screen scene_transistion(_("The next day"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound3 sfx_sea_guls_1 fadein 1.5 noloop
    play sound4 sfx_seawaves_ambience2 fadein 1.0 volume 0.1
    $ renpy.music.set_volume(0.7, 3.0, "music2")
    play music2 music_miami_reggae3 fadein 3.0
    scene e18s06-00 businesss_booming
    with Fade(0.5, 0.5, 0.9)
    pause
    scene e18s06-01 businesss_booming_sb_talk with dissolve
    play voice4 samiya_hah1 noloop
    sb "Looks like word is spreading."
    scene e18s06-02 businesss_booming_dw_talk with dissolve
    play voice3 dahlia_yes_yeah1 noloop
    dw "Yeah, getting more and more popular by the day."
    scene e18s06-03 businesss_booming_sb_talk with dissolve
    play voice4 samiya_huh4 noloop
    sb "It's gotta' be the new gals. We were never this popular with just the boys."
    scene e18s06-04 businesss_booming_mc_talk with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "Hey!"
    scene e18s06-05 businesss_booming_sb_talk_smirk with dissolve
    play voice4 samiya_laughing1 noloop
    sb "Just jerking your chain, [mcname]."
    scene e18s06-06 businesss_booming_dw_talk with dissolve
    play voice3 dahlia_no_nouh noloop
    dw "Not yet, we're not. I can go get his chain out though."
    stop music2 fadeout 3.0
    scene e18s06-07 businesss_booming_sb_talk_cars_waiting with dissolve
    play voice4 samiya_geh noloop
    sb "What I mean, is without you boys we wouldn't even have this business."
    play sound ["<silence 0.25>", sfx_hands_clap3]
    play sound2 ["<silence 0.45>", sfx_hands_clap1] noloop
    scene e18s06-08 businesss_booming_sb_talk_cars_clap with dissolve
    $ renpy.music.set_volume(0.65, 0.0, "music")
    play music music_sexy_workout
    play voice4 samiya_hm3 noloop volume 1.7
    sb "Now, chop, chop gang. These cars won't wash themselves! And if you don't hurry, we're going to switch from the riding crop to the whip."
    scene e18s06-09 businesss_booming_pb_talk with dissolve
    play voice5 pete_yes_simple2 noloop
    pb "Yes, Mistress."
    scene e18s06-10 businesss_booming_mc_talk with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "Anything for you, my Queen."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene e18s06-11 businesss_booming_mc_walk with dissolve
    pause
    scene e18s06-12 businesss_booming_dw_talk_watching with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    dw "You know, Samiya. This was {i}not{/i} how I expected this 'vacation' to go."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene e18s06-13 businesss_booming_sb_talk_watching with dissolve
    play voice4 samiya_yes2 noloop
    sb "Yeah-"
    scene e18s06-14 businesss_booming_dw_talk_watching with dissolve
    play voice3 dahlia_happy_laugh3 noloop
    dw "But I'm pretty pleased with it."
    scene e18s06-15 businesss_booming_sb_talk_smiles with dissolve
    play voice4 samiya_hm1 noloop volume 1.6
    sb "Good."
    scene e18s06-16 businesss_booming_dw_talk with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    dw "Now - it's time to put on my Mistress face."

    jump e18s06_montage_1

label e18s06_montage_1:

    $ renpy.music.set_volume(1.0, 3.0, "music")
    play sound sfx_washing_with_sponge1 loop
    scene e18s06-17 businesss_booming_montage_cleaning_dw_standingby with dissolve
    pause
    play sound2 mc_sex_sucking_slow1
    scene e18s06-18 businesss_booming_montage_cleaning_mc_lickhood_dw_hitpb_standingby with dissolve
    pause
    play sound2 sfx_cleaning_floor1 volume 1.6
    scene e18s06-19 businesss_booming_montage_cleaning_sb_pull_kehair with dissolve
    pause
    scene e18s06-20 businesss_booming_montage_cleaning_lo__look_mc with dissolve
    pause
    scene e18s06-21 businesss_booming_montage_cleaning_dw_spank_lo with dissolve
    pause
    play sound sfx_paper_rustl1 volume 2.5
    scene e18s06-22 businesss_booming_montage_sb_taking_money with dissolve
    pause
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene e18s06-23 businesss_booming_montage_mc_pb_ke_lo_walk with dissolve
    pause
    play sound sfx_washing_with_sponge1 loop
    stop sound2 fadeout 1.0
    scene e18s06-24 businesss_booming_montage_ke_hose with dissolve
    pause
    play sound2 sfx_water_hosepipe1
    scene e18s06-25 businesss_booming_montage_ke_spray_lo with dissolve
    play voice6 girl28_scared_ah2 noloop
    play voice7 girl30_happy_laugh2 noloop
    pause
    stop sound2 fadeout 1.0
    scene e18s06-a26 business_is_booming_montage_lo_wet-glambot-26-000_i with dissolve
    play voice6 girl28_angry_breathing noloop
    pause
    play sound2 sfx_camera_fly1 volume 2.5 noloop
    play sound3 ["<silence 2.5>", sfx_camera_fly1] volume 2.5 noloop
    scene e18s06-a26-glambot
    pause
    stop sound3 fadeout 1.0
    play sound2 sfx_water_hosepipe1
    stop sound fadeout 1.0
    scene e18s06-27 businesss_booming_montage_spray pb with dissolve
    play voice5 pete_angry_argh3 noloop
    pause
    play sound sfx_water_pouring1
    scene e18s06-28 businesss_booming_montage_mc_gets_hose with dissolve
    play voice2 mc_happy_laugh2 noloop
    play voice7 girl30_scared_ah4 noloop
    pause
    scene e18s06-29 businesss_booming_montage_ke_wet_pose with dissolve
    play voice7 girl30_disgust_oof noloop
    pause
    stop sound2 fadeout 1.0
    stop sound fadeout 1.0
    scene e18s06-30 businesss_booming_montage_dw_spanking_ke_mc_walking_to_sb_sitting with dissolve
    play voice3 dahlia_angry_ah1 noloop
    play sound3 sfx_whip_slap1 noloop
    play voice7 girl30_scared_ah1 noloop
    queue sound sfx_heels_steps2
    pause
    play sound sfx_cloth_rustling2 volume 1.5
    scene e18s06-31 businesss_booming_mc_sit with dissolve
    pause
    $ renpy.music.set_volume(0.6, 3.0, "music")
    scene e18s06-32 businesss_booming_sb_talk_lookmc with dissolve
    play voice4 samiya_haha1 noloop volume 1.8
    sb "Don't let Dahlia see you sitting there."
    scene e18s06-33 businesss_booming_mc_talk with dissolve
    play voice2 mc_no_nah1 noloop
    mc "I'm not worried about that happening."
    scene e18s06-34 businesss_booming_dw_talk_sb_look with dissolve
    play sound sfx_whip_slap3
    play voice3 dahlia_angry_argh1 noloop
    dw "You good for nothing slut! You got water on my shoes!"
    scene e18s06-35 businesss_booming_ke_talk with dissolve
    play voice7 girl30_pain_sobs1 noloop
    ke "I'm sorry, Mistress!"
    scene e18s06-36 businesss_booming_dw_talk with dissolve
    play voice3 dahlia_no_serious noloop
    dw "Not yet, you're not! You haven't {i}even begun{/i} to understand the meaning of the word sorry yet!"
    stop voice7 fadeout 3.0
    scene e18s06-37 businesss_booming_sb_talk_lookmc with dissolve
    play voice4 girl35_yes_aga1 noloop
    sb "You're right. You probably have 5-"
    scene e18s06-38 businesss_booming_dw_talk with dissolve
    play voice3 dahlia_angry_argh2 noloop
    dw "And you! You fucking baboon! Come over here, you're next!"
    scene e18s06-39 businesss_booming_sb_talk with dissolve
    play voice4 girl35_happy_laugh2 noloop
    sb "Ten. You got a good ten minutes before she notices."
    stop music fadeout 6.0
    $ renpy.music.set_volume(0.8, 6.0, "music")
    $ renpy.music.set_volume(0.8, 0.0, "music2")
    scene e18s06-40 businesss_booming_mc_talk_relaxes with dissolve
    play music2 music_miami_day fadein 8.0
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "So, how's the car wash doing?"
    scene e18s06-41 businesss_booming_sb_talk_relaxes with dissolve
    play voice4 samiya_huh5 noloop
    sb "What do you mean? We've had a great day so far."
    scene e18s06-42 businesss_booming_mc_talk with dissolve
    play voice2 d9s3_no noloop volume 1.7
    mc "I mean financially."
    scene e18s06-43 businesss_booming_sb_talk_surprised with dissolve
    play voice4 samiya_ou1 noloop volume 1.6
    sb "Why are you curious about our financials?"
    scene e18s06-44 businesss_booming_mc_talk with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "You know I was going to school for business, right?"
    scene e18s06-45 businesss_booming_sb_talk_hand with dissolve
    play voice4 girl35_thinking_oh1 noloop
    sb "I always forget that you're a college kid."
    scene e18s06-46 businesss_booming_mc_talk with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Oh yeah? Then what am I to you?"
    scene e18s06-47 businesss_booming_sb_talk with dissolve
    play voice4 samiya_mmm2 noloop
    sb "The best knight a gal could ask for."
    scene e18s06-48 businesss_booming_mc_talk with dissolve
    play voice2 mc_arrogant_heh3 noloop volume 1.3
    mc "Don't you mean a queen?"
    scene e18s06-49 businesss_booming_sb_talk_wide_smile with dissolve
    play voice4 girl35_happy_laugh3 noloop
    sb "I do."
    scene e18s06-50 businesss_booming_mc_talk with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "But that doesn't answer my question."
    scene e18s06-51 businesss_booming_sb_talk_sit_up with dissolve
    play voice4 samiya_cagh noloop
    sb "Nosy little bastard, aren't ya?"
    scene e18s06-52 businesss_booming_mc_talk with dissolve
    play voice2 d9s2_yeah noloop volume 1.9
    mc "Maybe."
    scene e18s06-53 businesss_booming_sb_talk with dissolve
    play voice4 samiya_huh3 noloop
    sb "You won't let this go if I don't tell you something, right?"
    scene e18s06-54 businesss_booming_mc_talk_sit_up with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "You know me so well, Samiya."
    scene e18s06-55 businesss_booming_sb_talk with dissolve
    play voice4 girl35_disappointed_mmm1 noloop
    sb "Okay, well... Shit, I never realized how awkward this would be to talk about out loud."
    scene e18s06-56 businesss_booming_mc_talk with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Talk about what?"
    scene e18s06-57 businesss_booming_sb_talk with dissolve
    play voice4 samiya_eeem1 noloop
    sb "Okay, so there's this guy I know... I, uhm, met him through work. He's an investment banker type, you know?"
    play voice2 mc_yes_aga1 noloop
    mc "Uh huh..."
    sb "And we started talking and..."
    scene e18s06-58 businesss_booming_mc_talk with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, do I smell sentimentalism? Or maybe a little something more?"
    scene e18s06-59 businesss_booming_sb_talk_slapknee with dissolve
    play voice4 girl35_no_angry1 noloop
    sb "No, you fucking idiot. Nothing like that. We've been talking about financial shit."
    scene e18s06-60 businesss_booming_mc_talk with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Like what?"
    scene e18s06-61 businesss_booming_sb_talk with dissolve
    play voice4 girl35_thinking_eem5 noloop
    sb "Like how to get into the stock market and shit."
    scene e18s06-62 businesss_booming_mc_talk_surprised with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What, are you trying to become a day trader?"
    play sound sfx_hair_scratch1
    scene e18s06-63 businesss_booming_mc_talk_pinchnose with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Don't tell me this guy has told you to get into crypto, because it's super volatile and most of it-"
    scene e18s06-64 businesss_booming_sb_talk with dissolve
    play voice4 girl35_no_angry5 noloop
    sb "No, moron. Do I look like some crypto bro asshole to you?"
    scene e18s06-65 businesss_booming_mc_talk with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Weeellllll..."
    scene e18s06-66 businesss_booming_sb_talk_slapknee with dissolve
    play voice4 samiya_kghhh noloop volume 1.6
    sb "Don't make me get Dahlia over here to punish you."
    scene e18s06-67 businesss_booming_mc_talk_handsup with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "All right, all right. So, just plain old day trading."
    scene e18s06-68 businesss_booming_sb_talk with dissolve
    play voice4 girl35_yes_yeah1 noloop
    sb "Yeah. Just, normal shit. Stocks and whatever."
    scene e18s06-69 businesss_booming_mc_talk_handsdown with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Uh huh. You want to start investing then?"
    scene e18s06-70 businesss_booming_sb_talk with dissolve
    play voice4 girl35_yes_aga3 noloop
    sb "Yeah... At least, I think so."
    scene e18s06-71 businesss_booming_sb_talk_sit_back with dissolve
    play voice4 girl35_disappointed_mff3 noloop
    sb "All those rich assholes I used to be around... All they did was talk about portfolios and opportunities, and..."
    sb "It's the best 'get-rich-quick' scheme I've ever heard."
    scene e18s06-72 businesss_booming_mc_talk with dissolve
    play voice2 mc_arrogant_nah1 noloop volume 1.4
    mc "Not everyone gets rich though."
    scene e18s06-73 businesss_booming_sb_talk with dissolve
    play voice4 girl35_thinking_eem6 noloop
    sb "At the very least, I'm setting aside something for the future..."
    scene e18s06-74 businesss_booming_mc_talk_surprised with dissolve
    play voice2 mc_arrogant_huh3 noloop volume 1.3
    mc "I did not take you for the type to think about the future."
    scene e18s06-75 businesss_booming_sb_talk_sad with dissolve
    play voice4 girl35_disappointed_geh5 noloop volume 1.4
    sb "I..."
    play voice2 d1s1_mmm noloop
    mct "Wait. Is Samiya... Is Samiya having an emotional moment? With me?"
    sb "Look. I want this to be different. I want... All of this, to be different. So I have to do things differently now."
    scene e18s06-76 businesss_booming_mc_talk with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "And you're starting by day trading?"
    scene e18s06-77 businesss_booming_sb_talk with dissolve
    play voice4 samiya_no1 noloop volume 1.4
    sb "No. I'm starting by trying to build us a future. All of us."
    scene e18s06-78 businesss_booming_mc_talk with dissolve
    play voice2 mc_scared_huuuh1 noloop
    mc "All of us, really?"
    scene e18s06-79 businesss_booming_sb_talk_smiling with dissolve
    play voice4 samiya_yes1 noloop
    sb "What kind of queen would I be if I didn't take care of my subjects?"
    stop music2 fadeout 3.0
    scene e18s06-80 businesss_booming_mc_talk_smile with dissolve
    play voice2 mc_happy_a1 noloop
    mc "You've got a good point there."
    $ renpy.music.set_volume(0.6, 0.0, "music")
    scene e18s06-81 businesss_booming_dw_talk with dissolve
    play music music_sexy_workout
    play voice3 dahlia_old_argh3 noloop
    dw "[mcname!u]! YOU WORM!"
    scene e18s06-82 businesss_booming_sb_talk_smiling_wicked with dissolve
    play voice4 girl35_happy_laugh4 noloop
    sb "Seems like your 10 minutes is up."
    scene e18s06-83 businesss_booming_mc_talk with dissolve
    play voice2 mc_pain_ou1 noloop
    mc "Oh shit."
    play sound sfx_throw_something1
    scene e18s06-84 businesss_booming_dw_talk_standing_over with dissolve
    play voice3 dahlia_angry_ah1 noloop
    dw "IS YOUR WORTHLESS ASS IN MY CHAIR!?"
    scene e18s06-85 businesss_booming_mc_talk with dissolve
    play voice2 d2s12_emmm noloop volume 1.3
    mc "Mistress-"
    scene e18s06-86 businesss_booming_dw_talk with dissolve
    play voice3 dahlia_old_argh noloop
    dw "There's only one thing that ass is useful for! {i}Punishment!{/i} Get over here!"
    play sound sfx_skirt_off2
    scene e18s06-87 businesss_booming_sb_talk_mc_stand with dissolve
    play voice4 girl35_thinking_eem1 noloop
    sb "Hope the talk was worth it."
    scene e18s06-88 businesss_booming_dw_talk with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "With you, my queen? Always."

    jump e18s06_montage_2

label e18s06_montage_2:

    $ renpy.music.set_volume(1.0, 3.0, "music")
    play sound sfx_heels_steps1
    scene e18s06-89 businesss_booming_mc_walk with dissolve
    pause
    scene e18s06-90 businesss_booming_sb_smile with dissolve
    pause
    play sound sfx_whip_slap6
    scene e18s06-91 businesss_booming_montage_spanking with dissolve
    pause
    play sound sfx_paper_rustl1 volume 2.0
    scene e18s06-92 businesss_booming_montage_money with dissolve
    pause
    play sound sfx_bus_startmove
    scene e18s06-93 businesss_booming_montage_car_pullup with dissolve
    stop sound fadeout 4.0
    pause
    play sound2 sfx_washing_with_sponge1
    scene e18s06-94 businesss_booming_montage_mc_ke with dissolve
    pause
    play sound3 sfx_cleaning_floor1 volume 2.5 noloop
    scene e18s06-95 businesss_booming_montage_pb_lo with dissolve
    pause
    scene e18s06-96 businesss_booming_montage_dw_yell with dissolve
    pause
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    play sound sfx_paper_rustl1 volume 2.0
    scene e18s06-97 businesss_booming_montage_handout_money with dissolve
    pause
    $ renpy.music.set_volume(0.5, 3.0, "music")
    play sound sfx_paper_rustl1 volume 2.5
    scene e18s06-98 businesss_booming_montage_sb_talk_money with dissolve
    play voice4 girl35_hey_laughing noloop
    sb "And thanks for choosing the Car Wash! Hope you come back soon!"
    play sound2 sfx_bus_startmove noloop fadein 1.5
    scene e18s06-99 businesss_booming_montage_driveoff with dissolve
    pause
    stop sound2 fadeout 3.0
    scene e18s06-100 businesss_booming_circle_sb_dw_talk with dissolve
    play voice3 dahlia_arrogant_huh noloop
    dw "So, how did the little subbies do today?"
    play sound sfx_paper_rustl1 volume 1.5
    scene e18s06-101 businesss_booming_circle_sb_alk with dissolve
    play voice4 girl35_happy_yeah3 noloop
    sb "Best day yet."
    scene e18s06-102 businesss_booming_circle_mc_talk with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Good, we worked our asses off today."
    scene e18s06-103 businesss_booming_circle_dw_talk with dissolve
    play voice3 dahlia_angry_hm2 noloop
    dw "Quiet you.{w} But seriously, we were super busy. Things really seem like they're picking up."
    scene e18s06-104 businesss_booming_circle_sb_talk with dissolve
    play voice4 samiya_yes3 noloop
    sb "They are. They really are..."
    play sound sfx_paper_slide1
    scene e18s06-105 businesss_booming_circle_dw_talk_subs with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    dw "We still have work to do, come on my little pets - let's get to cleaning."
    $ renpy.music.set_volume(0.3, 3.0, "music")
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps1
    scene e18s06-106 businesss_booming_sb_talk_everyonewalks with dissolve
    play voice4 girl35_thinking_hmf2 noloop
    sb "Wait a sec, [mcname]..."
    stop sound fadeout 2.0
    stop sound2 fadeout 2.0
    scene e18s06-107 businesss_booming_mc_talk_stop with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, Samiya? What's up?"
    scene e18s06-108 businesss_booming_sb_talk_stop with dissolve
    play voice4 girl35_thinking_hmm5 noloop
    sb "Do you trust me?"
    scene e18s06-109 businesss_booming_mc_talk_stop with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    scene e18s06-110 businesss_booming_sb_talk with dissolve
    play voice4 samiya_cugh noloop
    sb "It's a simple yes or no question. Do you trust me?"
    scene e18s06-111 businesss_booming_mc_talk with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "Of course, Samiya."
    scene e18s06-112 businesss_booming_sb_talk with dissolve
    play voice4 girl35_thinking_hmf5 noloop
    sb "How much do you trust me?"
    scene e18s06-113 businesss_booming_mc_talk_walks_closer with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Enough to fly away to some tropical island, live and work at some car wash, and do whatever you ask me to do."
    scene e18s06-114 businesss_booming_sb_talk with dissolve
    play voice4 samiya_eeem1 noloop volume 1.5
    sb "Even enough... To let me invest everything we've made?"
    scene e18s06-115 businesss_booming_mc_talk_front with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.5
    mc "You're my queen? Who else is better qualified to build us a yet undreamed of future?"
    scene e18s06-116 businesss_booming_sb_talk_smile with dissolve
    play voice4 samiya_mmm3 noloop volume 1.4
    sb "Thanks, [mcname]. You should probably get back with the crew, before Dahlia comes up with some sort of punishment for you."
    scene e18s06-117 businesss_booming_mc_talk_smile with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "You're right."
    $ renpy.music.set_volume(0.7, 3.0, "music")
    play sound sfx_heels_steps1 loop
    scene e18s06-118 businesss_booming_mc_walks with dissolve
    pause
    scene e18s06-119 businesss_booming_sb_smiling with dissolve
    pause
    stop sound fadeout 1.0

    stop sound4 fadeout 2.0
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    jump e18s07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
