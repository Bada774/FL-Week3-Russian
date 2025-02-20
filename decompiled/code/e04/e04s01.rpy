label e04_menu_jump:

    stop music fadeout 2.0
    call start_ending_from_menu from _call_start_ending_from_menu_10
    $ mcname = persistent.mcname
    $ fl_watersports = persistent.fl_watersports
    $ d17s01_arj_assfuck = persistent.arj_assfuck
    $ d21s05_fivesome = persistent.mk_orgy
    $ d21s07_sex_dungeon = True
    $ e04s06_mk_available = False
    $ stop_all_sound()
    call hide_fl_points_overlay from _call_hide_fl_points_overlay_24
    $ date_mh = False
    $ d15s05_leave = False
    $ d15s05_rescue = False
    call screen e04_char_choice with Fade(0.5, 0.5, 0.5)

    jump d21s07_closing

label e04s01:

    call hide_fl_points_overlay from _call_hide_fl_points_overlay_25
    scene black
    show screen scene_transistion(_("Ending #4\nMy Sex Dungeon"))
    with Fade(0.9, 0.9, 0.9)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(1.0, 1.0, "sound")
    $ renpy.music.set_volume(1.0, 1.0, "sound2")
    $ renpy.music.set_volume(1.0, 1.0, "sound3")
    $ renpy.music.set_volume(1.0, 1.0, "sound4")
    $ renpy.music.set_volume(1.0, 1.0, "sound5")
    $ renpy.music.set_volume(1.0, 1.0, "voice2")
    $ renpy.music.set_volume(1.0, 1.0, "voice3")
    $ renpy.music.set_volume(1.0, 1.0, "voice4")
    $ renpy.music.set_volume(1.0, 1.0, "voice5")
    $ renpy.music.set_volume(1.0, 1.0, "voice6")
    scene black
    show screen scene_transistion(_("The Next Day"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.6, 1.0, "music")
    $ renpy.music.set_volume(0.5, 0.0, "sound3")
    play sound2 sfx_bus_startmove noloop
    play sound3 park fadein 1.5
    play music music_bdsm_arrival fadein 2.0
    scene e04s01-01 mc-pgc-mc-thinking-while-unload
    play sound sfx_car_door_closed1
    with Fade(0.5, 0.5, 0.5)
    stop sound2 fadeout 2.0
    pause
    scene e04s01-02 mc-pgc-mc-thinking-while-unload-look-at-item-in-hand with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "Well, I guess this is it. I've never done anything like this before."
    mct "I've fantasized about it long enough. I should be an expert by now."
    play sound sfx_metal_chain1 volume 1.5
    play sound2 sfx_heels_steps1 noloop
    scene e04s01-03 mc-pgc-mc-standing-with-lydia with dissolve
    stop sound2 fadeout 5.0
    play voice4 boy4_thinking_hmm1 noloop
    "Prison Guard" "Package delivery. Please state your name."
    scene e04s01-04 mc-pgc-mc-talk-look-at-lc with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "[mcname] Young.{w} Do you need to see my I.D. or something?"
    scene e04s01-05 mc-pgc-mc-talk-alt-confirm-name with dissolve
    play voice4 boy5_no_angry noloop
    "Prison Guard" "No, sir. This package is for you, then."
    "Prison Guard" "Lydia Cox, to be transferred to [mcname] Young. Please sign here."
    scene e04s01-06 mc-pgc-mc-thinking-something-feels-off with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "Huh. Not sure what I expected, but something doesn't feel right."
    scene e04s01-07 mc-pgc-mc-talk-confused with dissolve
    play voice2 d2s9_mchey noloop
    mc "Just like that?"
    play sound sfx_paper_rustl1 volume 1.4
    scene e04s01-08 mc-pgc-mc-talk-sign-hand-clipboard with dissolve
    play voice4 boy5_yes_ugu noloop
    "Prison Guard" "You sign for the package, then it's your problem."
    scene e04s01-09 mc-pgc-mc-talk-my-problem with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, okay. I'm signing."
    mc "Wait, what do you mean it's my problem?"
    play sound sfx_pen_writing3 volume 2.0
    scene e04s01-10 mc-pgc-mc-talk-look-at-lydia-manipulative with dissolve
    play voice4 boy5_arrogant_huh noloop
    "Prison Guard" "Thank you, sir. Be careful with her. She's a manipulative one."
    scene e04s01-12 mc-pgc-talk-smile-hold-something-hidden with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "I know that better than most."
    play sound sfx_keys_jingle1 volume 1.5
    scene e04s01-11 mc-pgc-talk-hand-something with dissolve
    stop sound fadeout 1.0
    play voice4 boy5_thinking_hmm3 noloop
    "Prison Guard" "She's all yours. Here's your key to her restraints."
    scene e04s01-13 mc-pgc-lc-talk-blowjob-offer with dissolve
    play voice4 boy5_arrogant_hah noloop
    "Prison Guard" "On the way here she offered me a blowjob if I \"loosened her restraints\"."
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Did you take the blowjob, at least?"
    scene e04s01-14 mc-pgc-lc-talk-blowjob-offer-lc-smile with dissolve
    play voice4 boy5_no_nah noloop
    "Prison Guard" "No sir, it wasn't worth it. I'm married."
    play voice2 mc_thinking_mmm4 noloop
    mc "Your wife would kill you?"
    "Prison Guard" "Nah, it's just that I would need to ask her permission."
    scene e04s01-15 mc-pgc-lc-talk-blowjob-offer-lc-smile-alt with dissolve
    play voice4 boy5_thinking_emm noloop
    "Prison Guard" "If I called to ask her permission every time some convict offered me sex... Well, I save that for the really good offers."
    play voice2 d4s4_mclaugh noloop
    mc "*laughs* Good point."
    play voice4 boy5_happy_laugh1 noloop
    "Prison Guard" "*laughs* Not that she isn't cute, but not my type."
    scene e04s01-16 mc-pgc-lc-talk-lydia-interrupt with dissolve
    play voice3 lydia_hmmmm noloop
    lc "Excuse me, Warden? [mcname]?"
    scene e04s01-17 mc-pgc-lc-talk-alt with dissolve
    play voice3 lydia_moan1 noloop
    lc "Could we pleeease go inside, Love? We wouldn't want the neighbors to see me like this."
    play sound sfx_heels_steps1
    scene e04s01-18 mc-pgc-lc-walk-away-talk with dissolve
    play voice4 boy5_arrogant_tshah noloop
    "Prison Guard" "Ha! See what I mean? She's already trying to play you."
    scene e04s01-19 mc-pgc-lc-response-hold-up with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "Don't worry. I brought something for this."
    play voice3 samiya_mfff noloop
    play sound sfx_spitcum1 volume 0.5
    scene e04s01-20 mc-lc-shove-gag-in-mouth with dissolve
    play voice2 shhh noloop
    mc "Shhhh, hon. It's okay."
    mc "You'll be put in your place soon enough."
    play sound sfx_car_door_open1
    scene e04s01-21 mc-lc-pgc-talk-response with dissolve
    play voice4 boy5_surprised_oh1 noloop
    "Prison Guard" "I see you have this well in hand."
    scene e04s01-22 mc-lc-talk-ball-gag-in-mouth with dissolve
    play voice3 samiya_mfff3 noloop
    lc "MMmmmphhh!"
    play sound sfx_car_door_closed1
    scene e04s01-23 mc-lc-pgc-talk-close-back with dissolve
    play voice4 boy5_hey_bye noloop
    "Prison Guard" "Good luck!"
    play voice2 mc_yes_yeah1 noloop
    mc "You too, it was a pleasure to meet you."
    play sound sfx_bus_startmove
    scene e04s01-24 mc-lc-pgc-wave-leave with dissolve
    pause
    scene e04s01-25 mc-lc-pgc-talk-walk-towards-pool with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Take your time. We have years."
    mc "You know, I almost want to thank you. I mean, what you did was horrible."
    play sound2 sfx_heels_steps1
    stop sound fadeout 3.0
    scene e04s01-26 mc-lc-pgc-talk-walk-towards-pool-2 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "Part of me wants to flay the skin from your body and toss you into a sausage maker while you're still alive and screaming."
    mc "Huh. That sounded much darker out loud than it did in my head."
    stop sound2 fadeout 1.0
    scene e04s01-27 mc-lc-pgc-talk-walk-towards-pool-3 with dissolve
    play voice2 mc_thinking_hmm5 noloop volume 1.5
    mc "On the other hand, your actions have brought this wonderful opportunity to me."
    mc "Living rent free. My own private torture dungeon. And the obligation to punish you for everything you did."
    mc "I like this place. Nice house, lovely yard, wonderful pools. It's pleasant."
    scene e04s01-28 mc-lc-pgc-talk-infront-of-pool with dissolve
    play voice2 mc_thinking_emm1 noloop volume 1.5
    mc "Standing right here I thought of the perfect demonstration to put you in your place."
    mc "Do you want to know what it was?"
    $ renpy.music.set_volume(0.85, 3.0, "music")
    play voice2 mc_happy_oof1 noloop
    play sound sfx_leg_kick6
    play sound2 sfx_epic_jump1 noloop
    scene e04s01-29 mc-lc-push-lc-in-pool with hpunch
    play voice3 samiya_mfff2 noloop
    mc "Say, \"goodnight\", slut."
    play sound sfx_water_run2 volume 1.5
    play sound4 sfx_water_floatup2 noloop volume 2.0
    play sound2 sfx_water_splash2 volume 5.0 noloop
    scene e04s01-30 mc-lc-push-in-water-drowning with vpunch
    stop sound fadeout 3.0
    pause
    $ renpy.music.set_volume(0.0, 1.0, "sound3")
    $ renpy.music.set_volume(0.2, 1.0, "music")
    play sound2 sfx_underwater_loop1
    play sound4 sfx_water_bubbles1
    scene e04s01-31 mc-lc-push-in-water-drowning-lc-pov with dissolve
    pause
    $ renpy.music.set_volume(0.6, 6.0, "music")
    stop sound2 fadeout 4.0
    stop sound4 fadeout 1.0
    scene black with Fade(0.5, 0.5, 0.5)
    pause
    $ renpy.music.set_volume(0.6, 3.0, "music")
    $ renpy.music.set_volume(0.5, 1.0, "sound3")
    stop sound2 fadeout 1.0
    play sound sfx_water_floatup1
    scene e04s01-32 mc-lc-wake-up-bitch with Fade(0.5, 0.5, 0.5)
    play voice2 mc_angry_errr2 noloop
    mc "Wake the fuck up, bitch. {w}I'm not going to let you die that peacefully."
    play voice3 amrose_angry_cough1 noloop
    lc "*muffled cough*"
    scene e04s01-33 mc-lc-pull-out-gag with dissolve
    play voice2 d1s5_mchappy noloop volume 2.0
    mc "Let's get that gag off you. Then we can talk."
    mc "That was just a little taste of what you can expect."
    play voice3 amrose_pain_coughs noloop
    lc "*cough* F- {w}fuck *cough, cough* you."
    scene e04s01-34 mc-lc-talk-laying-on-floor-stand with dissolve
    play voice2 mc_happy_hah1 noloop
    mc "By the end of your time served here you will have so much experience with cruel and unusual punishment that you'll be too afraid to have me charged for it."
    queue voice3 dahlia_pain_ah3 noloop
    lc "*cough* You couldn't even let me drown. *cough* Pansy."
    lc "You're weak."
    scene e04s01-35 mc-lc-talk-laying-on-floor-stand-mc-pov with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Is that so?"
    play voice3 dahlia_angry_hm1 noloop
    lc "Within a couple of weeks I'll be back on my throne, and you will be groveling at my feet."
    play voice2 mc_happy_oof3 noloop
    mc "Sounds like a bet. Very well, I accept."
    scene e04s01-36 mc-lc-grab-lc-totake-away with dissolve
    play voice2 mc_thinking_mmm1 noloop volume 1.4
    mc "Let me get you to your throne, your highness."
    mc "Then the real games shall begin."
    stop music fadeout 3.5
    stop sound3 fadeout 2.0

    jump e04s02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
