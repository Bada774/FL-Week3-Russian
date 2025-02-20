label e03s05:

    $ renpy.music.set_volume(1.0, 6.0, "music")
    $ renpy.music.set_volume(1.0, 6.0, "music2")
    scene black
    show screen scene_transistion(_("Later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    queue music music_nordic_chopwater fadein 1.0
    play sound4 sfx_greenhouse_ambience fadein 3.0
    play sound2 sfx_axe_chopping1 fadein 3.0
    scene e03s05-01 mc-sy-cc-forest1_c1
    with Fade(0.5, 0.5, 0.5)
    pause
    scene e03s05-02 mc-sy-cc-forest2_c1 with fade
    pause
    scene e03s05-03 mc-sy-cc-forest3_c1 with fade
    pause
    stop sound2 fadeout 1.0
    scene e03s05-04 mc-sy-cc-forest4_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "When do we get to see Lyssa?"
    scene e03s05-04 mc-sy-cc-forest4_c2 with dissolve
    play voice5 boy5_thinking_hmm2 noloop
    "Cult Member" "You can see the goddess when she deigns it. Now, get back to work."
    scene e03s05-05 mc-sy-cc-forest5_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "But, we want-"
    scene e03s05-05 mc-sy-cc-forest5_c2 with dissolve
    play voice5 boy5_hey_simple noloop
    "Cult Member" "A mortal does not get to make demands of a goddess, or of her loyal followers. Prove yourself, and maybe you'll be granted an audience!"
    play voice2 mc_angry_errr3 noloop
    mc "Mrreeeegggh."
    play sound2 sfx_axe_chopping1 fadein 1.0
    scene e03s05-07 mc-sy-cc-forest7_c1 with fade
    pause
    scene e03s05-08 mc-sy-cc-forest8_c1 with fade
    pause
    stop sound2 fadeout 1.0
    scene e03s05-10 mc-sy-cc-stand_c1 with dissolve
    play voice3 stacy_disappointed_ehh4 noloop
    sy "We're never going to be able to sneak away and find Lyssa if this guy keeps watching us!"
    play voice2 mc_yes_yeah6 noloop
    mc "I know. And he definitely doesn't trust us."
    sy "Which is crazy! We're like, the most trustable people ever."
    scene e03s05-10 mc-sy-cc-stand_c2 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "I don't know about that. We did infiltrate this cult to bring it down."
    scene e03s05-11 mc-sy-cc-talk_c1 with dissolve
    play voice3 stacy_disappointed_oh7 noloop
    sy "Oh yeah..."
    scene e03s05-11 mc-sy-cc-talk_c2 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "But we need to find an excuse to get away from him."
    scene e03s05-12 mc-sy-cc-look_c1 with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    sy "Oh, just leave that to me."
    play sound sfx_footsteps_grass1
    scene e03s05-13 mc-sy-cc-walk_c1 with dissolve
    stop sound fadeout 2.0
    play voice3 stacy_hey_attention1 noloop
    sy "Hey! I'm getting pretty thirsty. Can we get some water?"
    scene e03s05-13 mc-sy-cc-walk_c2 with dissolve
    play voice5 boy5_disappointed_ehh2 noloop
    "Cult Member" "Mmergg. You two have barely done anything so far!"
    scene e03s05-13-1 mc-sy-cc-ask_c1 with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Well that's because we're city folks who've never done a hard day's work in our lives! We need a devoted cul- errr, Dyma follower to show us how to do it!"
    scene e03s05-13-1 mc-sy-cc-ask_c2 with dissolve
    play voice5 boy5_thinking_huh noloop
    "Cult Member" "That couldn't hurt..."
    scene e03s05-13-2 mc-sy-cc-walk_c1 with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "Could you show me the right way to do it? I'm just so silly I don't think I'll ever figure it out on my own!"
    scene e03s05-13-2 mc-sy-cc-walk_c2 with dissolve
    play voice5 boy5_yes_aga noloop
    "Cult Member" "Give me the axe and I'll show you how it's done."
    scene e03s05-13-2 mc-sy-cc-walk_c1 with dissolve
    play voice3 stacy_thinking_oh2 noloop
    sy "Oh, but what about that water?"
    play voice5 boy5_thinking_hmm1 noloop
    "Cult Member" "I can get it after-"
    sy "But I am sooooo thirsty!"
    scene e03s05-13-3 mc-sy-cc-walk2_c2 with dissolve
    play voice5 boy5_hey_calm noloop
    "Cult Member" "You - go fetch the water. And come straight back. Don't wander around."
    scene e03s05-13-3 mc-sy-cc-walk2_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure! I can do that."
    play sound sfx_throw_something1
    scene e03s05-13-4 mc-sy-cc-cut_c1 with dissolve
    play voice5 boy5_arrogant_hm noloop
    "Cult Member" "So first - your grip on the axe is the most important part of the swing."
    scene e03s05-13-4 mc-sy-cc-cut_c2 with dissolve
    play voice3 stacy_disappointed_oh3 noloop
    sy "Oh! I never would have even thought about that!"
    stop music fadeout 6.0
    play sound sfx_footsteps_grass2 fadein 1.0 loop
    scene e03s05-13-8 mc-sy-cc-look_c1 with fade
    play voice2 mc_thinking_mmm4 noloop
    mct "Now, where would they keep Lyssa..."
    mct "Probably somewhere they could keep her secret. Wouldn't want her just walking around."
    scene e03s05-13-9 mc-sy-cc-walk3_c1 with dissolve
    mct "Hmmm... Where could it be?"
    scene e03s05-13-10 mc-sy-cc-walk4_c1 with dissolve
    mct "How have I never seen this before? It's a little obvious, but it's the perfect place."
    queue music music_cult_hidden_main fadein 1.0
    play sound sfx_footsteps_grass1
    $ renpy.music.set_volume(0.0, 3.0, "sound4")
    scene e03s05-14 mc-sy-cc-move_c1 with dissolve
    play voice2 d1s1_mmm noloop
    mct "Well, this is super weird..."
    stop sound fadeout 2.0
    scene e03s05-15 mc-sy-cc-talk_c1 with dissolve
    mct "Creepy cave... What the hell do they do in here?"
    scene e03s05-16 mc-sy-cc-talk2_c1 with dissolve
    play voice5 chloe_angry_argh3_reverbed noloop
    "Guard" "Get into your cell!"
    play voice2 mc_angry_hm2 noloop
    mct "What the fuck?"
    scene e03s05-16 mc-sy-cc-talk2_c3 with dissolve
    play voice5 chloe_arrogant_heh1 noloop
    "Guard" "You pretender. I cannot wait until your fate is decided before the High Priestess' tribunal."
    play sound sfx_metal_fence1 volume 1.3
    scene e03s05-16 mc-sy-cc-talk2_c2 with dissolve
    play voice3 girl30_scared_ah3 noloop
    "Lyssa?" "But I didn't do anything!"
    scene e03s05-14 mc-sy-cc-move_c3 with dissolve
    play voice5 chloe_happy_hmm noloop
    "Guard" "Impersonating a goddess is crime against nature itself!"
    scene e03s05-14 mc-sy-cc-move_c2 with dissolve
    play voice3 girl30_scared_ah5 noloop
    "Lyssa?" "But I didn't-"
    scene e03s05-15 mc-sy-cc-talk_c3 with dissolve
    play voice5 chloe_angry_argh2 noloop
    "Guard" "Quiet! Before I get the flogger back out!"
    "Lyssa?" "..."
    play sound sfx_footsteps_grass1 loop volume 0.7
    scene e03s05-17 mc-sy-cc-walk_c2 with dissolve
    play voice5 chloe_disappointed_off noloop
    "Guard" "Good. Now I need to walk this stress off. The negativity your aura gives off is bringing me down."
    scene e03s05-17 mc-sy-cc-walk_c3 with dissolve
    pause
    stop sound fadeout 3.0
    scene e03s05-18 mc-sy-cc-hide_c1 with dissolve
    pause
    scene e03s05-18 mc-sy-cc-hide_c2 with dissolve
    play voice3 girl30_surprised_what noloop
    "Lyssa?" "What, you come to ridicule me?"
    scene e03s05-19 mc-sy-cc-look_c1 with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "Lyssa! It's me - [mcname]! What the hell did they do to your hair?"
    play sound sfx_cloth_rustling2
    scene e03s05-19 mc-sy-cc-look_c2 with dissolve
    play voice3 girl30_surprised_huh1 noloop
    "Not Lyssa?" "Lyssa? Who the hell is Lyssa?"
    scene e03s05-20 mc-sy-cc-talk_c1 with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait-"
    mc "Wait, you're not Lyssa!"
    scene e03s05-20 mc-sy-cc-talk_c2 with dissolve
    play voice3 girl30_no_sad noloop
    ca "No, I'm Chiara."
    scene e03s05-21 mc-sy-cc-stand_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Well, I guess it doesn't matter. We're here to help take down the cult!"
    scene e03s05-21 mc-sy-cc-stand_c2 with dissolve
    play voice3 girl30_yes_aga2 noloop
    ca "You're doing a great job so far."
    scene e03s05-22 mc-sy-cc-stand2_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hey! We're trying. They took our friend and we're trying to find her."
    scene e03s05-22 mc-sy-cc-stand2_c2 with dissolve
    play voice3 girl30_thinking_oh2 noloop
    ca "She wouldn't happen to be trans, would she?"
    scene e03s05-23 mc-sy-cc-talk_c1 with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "She is!"
    scene e03s05-23 mc-sy-cc-talk_c2 with dissolve
    play voice3 girl30_arrogant_hah1 noloop
    ca "That explains why they set up the tribunal..."
    ca "Long story short, this cult thought I was their holy goddess until they found out I didn't have a dick. Then they locked me in here."
    ca "They thought that it still could be me though, so they kept me around. Until a few days ago, when suddenly I was told I have to go to a trial before the High Priestess for my crime against nature."
    scene e03s05-22 mc-sy-cc-stand2_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Huh..."
    mc "Good thing we're here to break you out! And, with what happened to you, you can help us bring down the cult!"
    scene e03s05-22 mc-sy-cc-stand2_c2 with dissolve
    play voice3 girl30_disappointed_ehh1 noloop
    ca "That's going to be awfully hard trapped in a cell."
    play voice2 d2s9_confused noloop volume 1.6
    mc "Right, uhm..."
    scene e03s05-24 mc-sy-cc-talk2_c1 with dissolve
    play voice5 chloe_happy_mmm_reverbed noloop
    "Guard" "Mmmm, it feels so good to be cleaned of that negative energy."
    play voice2 mc_pain_ou1 noloop
    mc "Oh shit! She's coming back!"
    scene e03s05-24 mc-sy-cc-talk2_c2 with dissolve
    play voice3 girl30_angry_ehh noloop
    ca "Go! If you get caught, they'll throw you in here with me!"
    scene e03s05-25 mc-sy-cc-talk3_c1 with dissolve
    play voice2 mc_angry_huh2 noloop volume 1.3
    mc "I promise, I'll figure out a way to get you out!"
    scene e03s05-25 mc-sy-cc-talk3_c2 with dissolve
    play voice3 girl30_angry_mrr noloop
    ca "Please, hurry!"
    play sound sfx_footsteps_grass1
    scene e03s05-26 mc-sy-cc-run_c1 with dissolve
    pause
    scene e03s05-26 mc-sy-cc-run_c3 with dissolve
    play voice5 chloe_disappointed_ehh2 noloop
    "Guard" "Now, do you promise to behave? Because you upset my tummy before and I don't like having an upset tummy."
    scene e03s05-26 mc-sy-cc-run_c2 with dissolve
    play voice3 girl30_yes_serious noloop
    ca "Yes, I promise..."
    $ renpy.music.set_volume(1.0, 3.0, "sound4")
    stop sound fadeout 1.0
    queue sound sfx_footsteps_grass2 loop
    $ renpy.music.set_volume(0.6, 3.0, "music")
    scene e03s05-27 mc-sy-cc-cut2_c2 with fade
    play voice5 boy5_yes_ugu noloop
    "Cult Member" "And all of that, with a good stance, is the best way to chop wood."
    scene e03s05-27 mc-sy-cc-cut2_c1 with dissolve
    play voice3 stacy_happy_yay1 noloop
    sy "Thank you! Wow, this has been super educational. I know I'm going to do so much better now!"
    stop sound fadeout 1.0
    scene e03s05-28 mc-sy-cc-talk_c1 with dissolve
    play voice3 stacy_hey_happy1 noloop
    sy "[mcname]! You're back!"
    scene e03s05-28 mc-sy-cc-talk_c2 with dissolve
    play voice5 boy5_surprised_eeh1 noloop
    "Cult Member" "Where's the water?"
    scene e03s05-29 mc-sy-cc-walk_c1 with dissolve
    play voice2 d2s12_emmm noloop volume 1.3
    mc "Oh, uhhhh, I couldn't find it?"
    play sound sfx_footsteps_grass2 loop
    scene e03s05-29 mc-sy-cc-walk_c2 with dissolve
    play voice5 boy5_angry_argh4 noloop
    "Cult Member" "Useless city slicker...{w} I'll go get it. Don't go anywhere."
    stop sound fadeout 2.0
    scene e03s05-30 mc-sy-cc-talk_c2 with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "What took you so long if you weren't getting water?"
    scene e03s05-30 mc-sy-cc-talk_c1 with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "I found someone locked up in a prison cell!"
    scene e03s05-31 mc-sy-cc-talk2_c2 with dissolve
    play voice3 stacy_surprised_huh2 noloop
    sy "What!?!"
    scene e03s05-31 mc-sy-cc-talk2_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah! And she looked {i}just{/i} like Lyssa!"
    play voice3 stacy_thinking_emm4 noloop
    sy "Are you sure it wasn't Lyssa?"
    mc "Yeah, I talked to her."
    scene e03s05-32 mc-sy-cc-talk3_c2 with dissolve
    play voice3 stacy_angry_argh1 noloop
    sy "What! Why are they keeping her in a prison cell?"
    play sound sfx_footsteps_grass2 loop fadein 2.0
    scene e03s05-32 mc-sy-cc-talk3_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "It sounds like they thought she was their goddess, but she wasn't trans, so..."
    play voice3 stacy_thinking_hmm3 noloop
    sy "That would explain why she looks like Lyssa! But... wouldn't her friend have told her that?"
    mc "Yeah, I think-"
    sy "Shhh! He's coming back."
    stop sound fadeout 1.0
    scene e03s05-33 mc-sy-cc-talk4_c1 with dissolve
    play voice5 boy5_disappointed_ehh1 noloop
    "Cult Member" "We are done for the day. Go back to your abode and freshen up."
    scene e03s05-33 mc-sy-cc-talk4_c2 with dissolve
    play voice3 stacy_hey noloop
    sy "Hey, where's the water!?"
    play voice5 boy5_arrogant_huh noloop
    "Cult Member" "There are more important tasks to be done. The goddess Dyma has called for a gathering this evening."
    scene e03s05-34 mc-sy-cc-talk5_c2 with dissolve
    play voice3 stacy_disappointed_oh1 noloop
    sy "Man... I just wanted some water..."
    play sound sfx_footsteps_grass2 loop
    scene e03s05-34 mc-sy-cc-talk5_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "Come on, we should get ready. It sounds like Lyssa has something planned for tonight."
    scene e03s05-35 mc-sy-cc-walk_c2 with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "What about the water! I'm a thirsty bitch."
    scene e03s05-35 mc-sy-cc-walk_c1 with dissolve
    play voice2 d9s2_yeah noloop volume 1.7
    mc "Don't worry, we'll get you some water."
    stop music fadeout 3.5
    scene e03s05-35 mc-sy-cc-walk_c3 with dissolve
    pause
    stop sound fadeout 1.0
    stop sound4 fadeout 2.0
    $ renpy.music.set_volume(1.0, 6.0, "music")
    scene e03s05-36 mc-sy-cc-hp-stand_c3 with fade
    queue music music_cult_award_ceremony
    play voice5 girl34_hey_angry3 noloop
    hp "My followers, I am so happy to be standing here this evening. As was promised and foretold, our goddess has come to us!"
    play sound sfx_crowd_expression_cheer5 loop fadein 1.0
    scene e03s05-36 mc-sy-cc-hp-stand_c1 with dissolve
    pause
    scene e03s05-36 mc-sy-cc-hp-stand_c2 with dissolve
    play voice5 girl34_thinking_hmm2 noloop
    hp "Tonight, I am proud to welcome Dyma, the goddess of beauty and love, to this mortal plane."
    scene e03s05-37 mc-sy-cc-hp-bows_c1 with dissolve
    pause
    play sound2 sfx_heels_steps1_slow loop
    scene e03s05-38 mc-sy-cc-hp-walk_c1 with dissolve
    $ fl_achievement_unlock("e03s01n01")
    $ unlock_gallery_slot("extra", "e03s01n01")
    pause
    scene e03s05-38 mc-sy-cc-hp-walk_c2 with dissolve
    play voice6 boy5_happy_yeah3 noloop
    "Cult Member" "Thank you, goddess! Thank you, Dyma!"
    scene e03s05-39 mc-sy-cc-hp-look_c1 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Oh my God..."
    scene e03s05-39 mc-sy-cc-hp-look_c2 with dissolve
    play voice3 stacy_yes_ugu1 noloop volume 1.7
    sy "Uh huh. These people are all cuckoo for cocoa puffs!"
    scene e03s05-40 mc-sy-cc-hp-look2_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah. This isn't going to be easy..."
    scene e03s05-40 mc-sy-cc-hp-look2_c2 with dissolve
    play voice3 stacy_mmm1 noloop
    sy "But... is it just me, or is Lyssa kind of extra hot all painted in gold like that?"
    scene e03s05-39 mc-sy-cc-hp-look_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "Come on, Stacy. We need to stay focused!"
    scene e03s05-39 mc-sy-cc-hp-look_c2 with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "Right! Focused. Not thinking about Lyssa's golden cock."
    play sound2 sfx_cloth_rustling2 noloop
    scene e03s05-41 mc-sy-cc-hp-sit_c1 with dissolve
    pause
    stop sound fadeout 6.0
    scene e03s05-41 mc-sy-cc-hp-sit_c2 with dissolve
    play voice5 girl34_thinking_hmm6 noloop
    hp "What is your first decree, my goddess?"
    scene e03s05-42 mc-sy-cc-hp-talk_c1 with dissolve
    play voice4 dahlia_disappointed_ehh3 noloop
    mh "I think, I would like to get to know each member of my... church, personally."
    scene e03s05-42 mc-sy-cc-hp-talk_c2 with dissolve
    play voice5 girl34_happy_yes noloop
    hp "Yes, my goddess! You should speak with-"
    scene e03s05-43 mc-sy-cc-hp-point_c1 with dissolve
    play voice4 dahlia_arrogant_hm noloop
    mh "I shall decide who speaks to me first."
    mh "First, I would like to speak to those two. They who helped me ascend."
    scene e03s05-43 mc-sy-cc-hp-point_c2 with dissolve
    play voice5 girl34_disappointed_oh3 noloop
    hp "Of course, Dyma...{w} You two! Approach the goddess and pay your respects!"
    scene e03s05-44 mc-sy-cc-hp-talk_c2 with dissolve
    play voice2 d2s9_mchey noloop
    mc "Hey, Ly-"
    play voice5 girl34_angry_ahem1 noloop
    hp "Kneel."
    play voice3 stacy_arrogant_huh2 noloop
    sy "Huh?"
    hp "Show your respect and bow before the goddess!"
    play sound sfx_cloth_rustling4 volume 1.5
    scene e03s05-45 mc-sy-cc-hp-knee_c2 with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "Oh, uhm..."
    mc "Uhm, thank you for choosing us, goddess, to speak to you."
    scene e03s05-45-1 mc-sy-cc-hp-plan1_tip_c1 with dissolve
    play voice5 girl34_yes_ugu1 noloop
    hp "Good. That is the right reverence to show the mighty Dyma."
    scene e03s05-45-2 mc-sy-cc-hp-plan2_c1 with dissolve
    play voice4 dahlia_disappointed_ehh2 noloop
    mh "I would like to speak to my members alone, High Priestess."
    scene e03s05-45-2 mc-sy-cc-hp-plan2_c2 with dissolve
    play voice5 girl34_surprised_ah3 noloop
    hp "But-"
    scene e03s05-45-1 mc-sy-cc-hp-plan1_tip_c1 with dissolve
    play voice4 dahlia_angry_argh2 noloop
    mh "You dare question your goddess?"
    scene e03s05-45-1 mc-sy-cc-hp-plan1_tip_c2 with dissolve
    play voice5 girl34_no_neutral3 noloop
    hp "No, Dyma. My deepest apologies. I will leave you to your grand plan."
    play sound sfx_heels_steps1
    scene e03s05-45-3 mc-sy-cc-hp-plan3_c1 with dissolve
    stop sound fadeout 4.0
    play voice4 dahlia_happy_hmm1 noloop
    mh "Boy, am I glad to see you two."
    scene e03s05-45-3 mc-sy-cc-hp-plan3_c3 with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Lyssa! Are you okay?"
    scene e03s05-45-4 mc-sy-cc-hp-plan4_c1 with dissolve
    play voice4 dahlia_yes_yeah4 noloop
    mh "Minus being painted gold and looking absolutely ridiculous, I'm fine."
    scene e03s05-45-3 mc-sy-cc-hp-plan3_c2 with dissolve
    play voice3 stacy_thinking_emm1 noloop
    sy "I think the gold makes you look hot."
    scene e03s05-45-5 mc-sy-cc-hp-plan5_c1 with dissolve
    play voice4 dahlia_arrogant_heh noloop
    mh "Thank you, Stacy."
    scene e03s05-45-6 mc-sy-cc-hp-plan6_c2 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "What have they been doing to you?"
    scene e03s05-45-7 mc-sy-cc-hp-plan7_c1 with dissolve
    play voice4 dahlia_arrogant_pff noloop
    mh "Mostly pampering and propaganda. The High Priestess is a zealot, absolutely. I think she actually believes I'm a goddess."
    scene e03s05-45-7 mc-sy-cc-hp-plan7_c2 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Apparently it's not the first time they've thought that about someone."
    scene e03s05-45-8 mc-sy-cc-hp-plan8_c1 with dissolve
    play voice4 dahlia_surprised_huh2 noloop
    mh "What?"
    scene e03s05-45-8 mc-sy-cc-hp-plan8_c2 with dissolve
    play voice3 stacy_arrogant_hmm1 noloop
    sy "[mcname] found someone locked up in a cell that looks exactly like you. They thought she was the goddess but I guess she didn't have the right bits."
    scene e03s05-45-8 mc-sy-cc-hp-plan8_c1 with dissolve
    play voice4 dahlia_disappointed_hmm2 noloop
    mh "Right bits?"
    scene e03s05-45-7 mc-sy-cc-hp-plan7_c2 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "She's got a vagina. Apparently, being trans is an important element to being Dyma."
    scene e03s05-45-6 mc-sy-cc-hp-plan6_c1 with dissolve
    play voice4 dahlia_thinking_oh noloop
    mh "Ahh. But you said she's locked up?"
    scene e03s05-45-8 mc-sy-cc-hp-plan8_c2 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Uh huh. They've got prisoner cells in this cave."
    scene e03s05-45-8 mc-sy-cc-hp-plan8_c1 with dissolve
    play voice4 dahlia_thinking_hmm1 noloop
    mh "The High Priestess conveniently left that out of the tour..."
    scene e03s05-45-5 mc-sy-cc-hp-plan5_c2 with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    sy "But it sounds like we don't even need the camera anymore. If we can get her out, then we'll have all the proof we need!"
    scene e03s05-45-5 mc-sy-cc-hp-plan5_c1 with dissolve
    play voice4 dahlia_happy_hmm2 noloop
    mh "I managed to get the camera back after they took our clothes and I've been recording for a few days."
    mh "But that, plus an eyewitness testimony is more than enough to get a warrant and to shut this place down."
    scene e03s05-45-8 mc-sy-cc-hp-plan8_c2 with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "But how are we going to get her out?"
    play voice2 mc_thinking_hmm7 noloop
    mc "What we need is a distraction."
    scene e03s05-45-8 mc-sy-cc-hp-plan8_c1 with dissolve
    play voice4 lissa_haha2 noloop
    mh "I have just the thing."
    play sound sfx_skirt_off2
    scene e03s05-46 mc-sy-cc-hp-talk_c1 with dissolve
    play voice4 dahlia_hey_active1 noloop
    mh "We must honor my return with a celebration! A veritable feast for my arrival!"
    scene e03s05-46 mc-sy-cc-hp-talk_c3 with dissolve
    play voice5 girl34_thinking_emm3 noloop
    hp "My goddess, we did not prepare food for you to enjoy this evening."
    scene e03s05-47 mc-sy-cc-hp-undress_c1 with dissolve
    play voice4 dahlia_no_uhuh noloop
    mh "I did not mean a feast of food, I mean of the more {i}carnal{/i} variety."
    play voice5 girl34_surprised_huh5 noloop
    hp "My goddess?"
    scene e03s05-46 mc-sy-cc-hp-talk_c1 with dissolve
    play voice4 dahlia_happy_woohoo1 noloop
    mh "Am I not the goddess of love?"
    mh "An orgy is the only festivity to consecrate my arrival!"
    play sound sfx_crowd_expression_cheer7 loop fadein 1.0
    scene e03s05-46 mc-sy-cc-hp-talk_c2 with dissolve
    pause
    scene e03s05-47 mc-sy-cc-hp-undress_c2 with dissolve
    play voice2 mc_surprised_huh8 noloop
    mc "{size=*0.6}Stacy! What are you doing?{/size}"
    scene e03s05-47 mc-sy-cc-hp-undress_c3 with dissolve
    play voice3 stacy_angry noloop
    sy "Getting ready for the orgy! What are you doing?"
    scene e03s05-48 mc-sy-cc-hp-talk_c2 with dissolve
    play voice2 mc_angry_errr6 noloop
    mc "{size=*0.6}The orgy is a distraction so we can go free Chiara!{/size}"
    play voice3 stacy_disappointed_oh2 noloop
    sy "Ohhh yeaaaaahhhh...{w} But what about the orgy?"
    mc "{size=*0.6}We can have our own orgy later!{/size}"
    scene e03s05-47 mc-sy-cc-hp-undress_c3 with dissolve
    play voice3 stacy_yes_fine4 noloop
    sy "Fiiiiiine."
    scene e03s05-48 mc-sy-cc-hp-talk_c3 with dissolve
    pause
    scene e03s05-49 mc-sy-cc-hp-talk2_c1 with dissolve
    play voice4 dahlia_thinking_hmm3 noloop
    mh "Once they get started, we can make our escape."
    scene e03s05-49 mc-sy-cc-hp-talk2_c2 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Sounds good to me."
    stop music fadeout 4.0
    stop sound fadeout 3.0
    play sound2 sfx_crowd_orgy1 loop fadein 1.0
    scene e03s05-50 mc-sy-cc-hp-montage_c1 with dissolve
    $ renpy.music.set_volume(0.8, 0.0, "music2")
    play music2 music_givemenegative2
    pause
    scene e03s05-50 mc-sy-cc-hp-montage_c2 with dissolve
    play voice4 dahlia_yes_aga noloop
    mh "I think their attention is occupied. Let's go."
    play voice3 stacy_thinking_hmm2 noloop
    sy "Lead the way, [mcname]!"
    stop sound2 fadeout 3.0
    scene e03s05-51 mc-sy-cc-hp-out_c1 with fade
    play sound sfx_door_open5
    pause
    queue sound sfx_heels_steps1
    scene e03s05-51 mc-sy-cc-hp-out_c2 with dissolve
    pause
    play sound sfx_footsteps_grass1
    scene e03s05-52 mc-sy-cc-hp-walk_c1 with fade
    play voice2 mc_hey_hey1 noloop
    mc "Hey!"
    scene e03s05-52 mc-sy-cc-hp-walk_c2 with dissolve
    play voice5 girl30_arrogant_huh2 noloop
    ca "Is this the rescue party?"
    stop sound fadeout 1.0
    scene e03s05-53 mc-sy-ca-mh-talk_c1 with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "It is! Let's get you out of here."
    scene e03s05-53 mc-sy-ca-mh-talk_c2 with dissolve
    play voice5 girl30_surprised_ohwow noloop
    ca "Quick, before the guard gets back."
    scene e03s05-54 mc-sy-ca-mh-talk2_c1 with dissolve
    play voice3 stacy_uhuh noloop
    sy "Oh, you don't have to worry about that. Lyssa here demanded an orgy we're all missing so he's probably super distracted right now."
    scene e03s05-54 mc-sy-ca-mh-talk2_c2 with dissolve
    play voice5 girl30_arrogant_heh noloop
    ca "Huh. Aren't you a little short to be a goddess?"
    scene e03s05-53 mc-sy-ca-mh-talk_c3 with dissolve
    play voice4 dahlia_disappointed_ehh1 noloop
    mh "Maybe. But, we can talk about that later."
    scene e03s05-53 mc-sy-ca-mh-talk_c2 with dissolve
    play voice5 girl30_thinking_emm2 noloop
    ca "There's one small hitch in the plan. The door is locked and I don't know where the key is."
    play sound sfx_metal_fence1
    scene e03s05-55 mc-sy-ca-mh-ask_c1 with dissolve
    queue sound sfx_chains_swings1 loop
    play voice3 stacy_arrogant_huh4 noloop
    sy "Leave that to me."
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Stacy, what are you doing?"
    scene e03s05-55 mc-sy-ca-mh-ask_c2 with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "I'm going to pick the lock!"
    play voice4 dahlia_surprised_huh1 noloop
    mh "You know how to pick locks?"
    sy "Uh huh!"
    scene e03s05-55 mc-sy-ca-mh-ask_c3 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Bull shit."
    scene e03s05-56 mc-sy-ca-mh-ask2_c2 with dissolve
    play voice3 stacy_happy_laugh1 noloop
    sy "You think all those times I walked in on you in the bathroom was because you 'accidentally' left the door unlocked?"
    scene e03s05-57 mc-sy-ca-mh-talk_c1 with dissolve
    play voice2 d4s8_scared noloop volume 1.7
    mc "I knew I wasn't forgetting to lock the door!"
    play sound sfx_door_locked1 volume 1.8
    scene e03s05-58 mc-sy-ca-mh-talk2_c2 with dissolve
    play voice3 stacy_yes_yap1 noloop
    sy "And, done!"
    play sound sfx_jail_door_open1
    scene e03s05-59 mc-sy-ca-mh-talk3_c1 with dissolve
    play voice2 mc_thinking_hmm9 noloop
    mc "What do you say we blow this popsicle stand?"
    scene e03s05-59 mc-sy-ca-mh-talk3_c2 with dissolve
    play voice5 girl30_disgust_oof noloop
    ca "Please!"
    play sound sfx_footsteps_grass1 loop
    play sound2 sfx_footsteps_grass1 volume 1.6
    scene e03s05-60 mc-sy-ca-mh-walk_c1 with dissolve
    pause
    scene e03s05-61 mc-sy-ca-mh-walk2_c1 with dissolve
    play voice3 stacy_arrogant_huh5 noloop
    sy "Do you think they'll notice we've gone?"
    play voice2 mc_no_no2 noloop
    mc "I doubt it. By the time they realize what's happened, we'll be long gone."
    scene e03s05-61 mc-sy-ca-mh-walk2_c2 with dissolve
    play voice5 girl30_thinking_eeh2 noloop
    ca "Can we not sit and talk about it, and get out of here?"
    scene e03s05-61 mc-sy-ca-mh-walk2_c3 with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Yep! Yep, yep, yep!"
    stop sound2 fadeout 1.0
    scene e03s05-62 mc-sy-ca-mh-walk3_c1 with dissolve
    pause
    scene e03s05-62 mc-sy-ca-mh-walk3_c2 with dissolve
    pause
    stop sound fadeout 2.0
    stop music2 fadeout 3.0

    jump e03s06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
