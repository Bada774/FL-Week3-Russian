label d16s04:

    if not hasattr(renpy.store, "week_1_goldstar"):
        if date_mes is True and fl_watersports is True:
            $ week_1_goldstar = True
        else:
            $ week_1_goldstar = False

    $ d16s04_cage_out = False
    $ d16s04_mes_studyhelp = False
    $ d16s04_gavecage = False
    $ d16_aw_reject = False

    scene black
    show screen scene_transistion(_("20 minutes later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    $ renpy.music.set_volume(0.3, 0.0, "sound2")
    play sound2 classroom fadein 3.0
    hide screen scene_transistion
    if date_mes is True:
        scene d16s04-01 mc-mes-classroom_c2
    else:
        scene d16s04-01-2 mc-mes-classroom-enter_c2
    with Fade(0.5, 0.5, 0.9)
    pause
    if date_mes is False:
        scene d16s04-49-3 mc-kb-classroom-thinking3_c2 with dissolve
    if d16s03_refuse_lc is False:
        mct "Phew, seems like everyone's a little late today."
    else:
        mct "Not a lot of people today.{w} Guess I'm early."

    $ renpy.music.set_volume(0.1, 10.0, "sound2")
    if date_mes is True:

        $ d16s04_mes_studyhelp = True

        scene d16s04-02 mc-mes-classroom2_c2 with dissolve
        play voice2 d2s9_mchey noloop
        mc "Hey."
        scene d16s04-02 mc-mes-classroom2_c1 with dissolve
        play voice3 min_hey_simple noloop
        mes "Hey yourself."
        scene d16s04-02 mc-mes-classroom2_c2 with dissolve
        play voice2 d1s5_mcthinks noloop
        mc "May I?"
        scene d16s04-02 mc-mes-classroom2_c1 with dissolve
        play voice3 min_yes_ugu noloop
        mes "Sure."
        $ renpy.music.set_volume(0.3, 0.0, "music")
        play music cute_times fadein 3.0
        play sound sfx_chair_slide1
        scene d16s04-14 mc-mes-classroom-talk10_c2 with dissolve
        mc "What are you reading there?"
        scene d16s04-14 mc-mes-classroom-talk10_c1 with dissolve
        play voice3 min_surprised_oh noloop
        mes "\"The Silent Patient.\" Lydia recommended it to me a while back."
        scene d16s04-13 mc-mes-classroom-talk9_c1 with dissolve
        play voice2 mc_thinking_hmm5 noloop
        mc "Huh."
        play voice3 min_old_laugh noloop
        mes "What?"
        scene d16s04-11 mc-mes-classroom-talk7_c2 with dissolve
        play voice2 mc_arrogant_hm3 noloop
        mc "Nothing. Just, I guess I never took you for a fiction type of a gal."
        scene d16s04-11 mc-mes-classroom-talk7_c1 with dissolve
        play voice3 min_surprised_huh2 noloop
        mes "What does that mean?"
        scene d16s04-08 mc-mes-classroom-talk4_c2 with dissolve
        play voice2 mc_thinking_mmm4 noloop
        mc "Well, you're one of the smartest people I know. The image I have of you in my head is you building rockets, fighting mummies, and climbing the Eiffel Tower or something."
        mc "I just never took you for someone that liked to spend a lot of time inside their own mind I guess."
        scene d16s04-12 mc-mes-classroom-talk8_c1 with dissolve
        mc "If that makes any sense."
        play voice3 min_yes_happy noloop
        mes "It does...I think."
        mes "And you're right, for the most part. I'm not big into books. I want to do stuff, not read about people doing stuff."
        scene d16s04-09 mc-mes-classroom-talk5_c1 with dissolve
        play voice3 min_old_hmm noloop
        mes "But I've been fed enough book reading propaganda by Lydia over the years and I just finally broke down I guess."
        mes "And I dunno. This sounded interesting, so I thought why not?"
        scene d16s04-04 mc-mes-classroom4_c2 with dissolve
        play voice2 mc_thinking_oh1 noloop
        mc "So how is it then?"
        scene d16s04-04 mc-mes-classroom4_c1 with dissolve
        play voice3 min_old_huh noloop
        mes "Reading books in general or the book specifically?"
        scene d16s04-17 mc-mes-classroom-talk13_c2 with dissolve
        play voice2 mc_arrogant_hm1 noloop
        mc "Both, I guess."
        scene d16s04-08 mc-mes-classroom-talk4_c1 with dissolve
        play voice3 min_arrogant_hm noloop
        mes "Well, it's been interesting. I remember reading some fiction stuff in high school and it was all so boring."
        scene d16s04-05 mc-mes-classroom-talk1_c1 with dissolve
        mes "Just pages upon pages of descriptions. Like, I don't care about the life of the great grandfather of the jeweler that etched the protagonist's heirloom toothpick!"
        mes "Move the story along already."
        scene d16s04-14 mc-mes-classroom-talk10_c2 with dissolve
        play voice2 mc_yes_yeah6 noloop
        mc "Yeah. Some writers go overboard with that."
        scene d16s04-14 mc-mes-classroom-talk10_c1 with dissolve
        play voice3 min_yes_yeah1 noloop
        mes "Yeah. Anyway, this, thankfully, doesn't do that."
        mes "Which I like."
        scene d16s04-06 mc-mes-classroom-talk2_c1 with dissolve
        mes "And it's been...interesting imagining this all out in my mind. You could even say it's been fun."
        scene d16s04-11 mc-mes-classroom-talk7_c2 with dissolve
        play voice2 mc_happy_wow2 noloop
        mc "Wow, well, I'm glad you're having fun."
        mc "Maybe you can read it to me sometime."
        scene d16s04-11 mc-mes-classroom-talk7_c1 with dissolve
        play voice3 min_surprised_ehh2 noloop
        mes "...Read it to you?"
        mes "...Why?"
        scene d16s04-08 mc-mes-classroom-talk4_c2 with dissolve
        play voice2 mc_thinking_hmm2 noloop
        mc "Well, let's see."
        mc "One, I like your voice, and I like hearing you talk.{w} Two, I like spending time with you."
        mc "Three, imagine us on the roof of your place with a nice bottle of wine and some cheese, reading under the stars. That sounds like a pretty amazing time to me."
        scene d16s04-08 mc-mes-classroom-talk4_c1 with dissolve
        play voice3 min_happy_relief noloop
        mes "Well, all the light pollution around here will probably make it so there's barely any stars visible. But uhm...that does sound nice."
        scene d16s04-14 mc-mes-classroom-talk10_c2 with dissolve
        play voice2 mc_arrogant_huh3 noloop
        mc "Maybe we can go somewhere away from here then."
        mc "Oh, there was something I wanted to ask, by the way. A favor."
        scene d16s04-12 mc-mes-classroom-talk8_c1 with dissolve
        play voice3 min_thinking_hmm2 noloop
        mes "Hm?"
        scene d16s04-17 mc-mes-classroom-talk13_c2 with dissolve
        play voice2 mc_disappointed_meh2 noloop
        mc "I'm having a rough time studying. All the FL stuff plus everything else.{w} And the finals are coming fast."
        mc "I was wondering if you'd be down to help me study?{w} If it's not a bother."
        scene d16s04-16 mc-mes-classroom-talk12_c1 with dissolve
        play voice3 min_no_happy noloop
        mes "Of course not."
        mes "Maybe we can study at my place."
        scene d16s04-07 mc-mes-classroom-talk3_c1 with dissolve
        play voice3 min_thinking_hmm3 noloop
        mes "I'll bring the cheese, you bring the wine."
        scene d16s04-14 mc-mes-classroom-talk10_c2 with dissolve
        play voice2 d4s4_mclaugh noloop
        mc "*Chuckles* I'm not sure we'll get much studying done at that point but sounds good to me."
        scene d16s04-18 mc-mes-classroom-talk14_c1 with dissolve
        play voice3 min_arrogant_heh2 noloop
        mes "I need to use the washroom. Talk to you later."
        scene d16s04-18 mc-mes-classroom-talk14_c2 with dissolve
        play voice2 mc_yes_yeah4 noloop
        mc "Alright. Bye."
    else:
        scene d16s04-01-3 mc-mes-classroom-enter2_c1 with dissolve
        pause
        play music cute_times fadein 3.0

    $ renpy.music.set_volume(0.2, 3.0, "music")

    scene d16s04-21 mc-kb-classroom-talk1_c1 with fade
    play voice3 kevin_thinking_hey1 noloop
    kb "Hey! [mcname]. Sup, man?"
    scene d16s04-55 mc-kb-classroom-talk6_c2 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Just waiting for the class to start.{w} What's up?"
    scene d16s04-21 mc-kb-classroom-talk1_c1 with dissolve
    play voice3 kevin_thinking_hmm6 noloop
    kb "Feels like we haven't talked in forever."
    scene d16s04-21 mc-kb-classroom-talk1_c2 with dissolve
    play voice2 mc_arrogant_hm2 noloop
    mc "Mood. The fuck you been up to anyway?"
    scene d16s04-22 mc-kb-classroom-talk1_c1 with dissolve
    play voice3 kevin_disappointed_ehh2 noloop
    kb "Eh, the usual, y'know? Hanging with Chloe. Studying. Oh, I got a part-time gig actually."
    play voice2 mc_scared_oh3 noloop
    mc "Oh shit, nice! Mr. Moneybags over here."
    scene d16s04-23 mc-kb-classroom-talk2_c1 with dissolve
    play voice3 kevin_thinking_hmm5 noloop
    kb "Moneybags my ass. It pays like dogshit."
    play voice2 mc_surprised_oof1 noloop
    mc "Oof. Welp, something's better than nothing, right?"
    scene d16s04-24 mc-kb-classroom-talk3_c1 with dissolve
    play voice3 kevin_thinking_yeah2 noloop
    kb "Yeah that's what I tell myself every day to not kill myself."
    play voice2 mc_arrogant_heh2 noloop
    mc "To you not killing yourself."
    scene d16s04-25 mc-kb-classroom-talk4_c1 with dissolve
    play voice3 kevin_happy_heh2 noloop
    kb "*Chuckles* To not killing myself."
    mc "You're not gonna kill yourself, right?"
    scene d16s04-26 mc-kb-classroom-talk5_c1 with dissolve
    kb "I'm fucking around man, I'm not gonna kill myself. Christ."
    scene d16s04-27 mc-kb-classroom-talk6_c1 with dissolve
    kb "I'm not ready to go on a grippy sock vacation just yet."
    scene d16s04-29 mc-kb-classroom-talk8_c1 with dissolve
    play voice3 kevin_surprised_huh1 noloop
    kb "Not to mention poor Chloe would be pretty bummed, and I can't do that to her."
    play voice2 mc_thinking_hmm2 noloop
    mc "How's it been with her anyway?"
    if date_cb is True:
        scene d16s04-30 mc-kb-classroom-talk9_c1 with dissolve
        play voice2 d2s9_confused noloop
        mc "Last we met, I uh..."
        scene d16s04-28 mc-kb-classroom-talk7_c1 with dissolve
        play voice3 kevin_thinking_hmm6 noloop
        kb "Came in her ass which I then ate?"
        play voice2 mc_yes_aga1 noloop
        mc "...Right."
        mc "That was..."
        scene d16s04-22 mc-kb-classroom-talk1_c1 with dissolve
        play voice3 kevin_thinking_hmm3 noloop
        kb "Interesting? Fucked up? Awoke something in you?"
        play voice2 mc_disappointed_ah1 noloop
        mc "All of the above I guess, sans a new awakening. But who the fuck knows anymore."
        scene d16s04-23 mc-kb-classroom-talk2_c1 with dissolve
        kb "What do you mean?"
        mc "This FL stuff has me doing stuff I never imagined."
        scene d16s04-24 mc-kb-classroom-talk3_c1 with dissolve
        kb "Good stuff or bad stuff?"
        mc "Only time will tell."
        scene d16s04-25 mc-kb-classroom-talk4_c1 with dissolve
        play voice3 kevin_happy_heh1 noloop
        kb "Dramatic fuck."
        play voice2 mc_arrogant_huh2 noloop
        if persistent.is_special is True:
            mc "You felched my cum outta your sister's ass!"
        else:
            mc "You felched my cum outta your girlfriend's ass!"
        mc "You can't talk."
        scene d16s04-26 mc-kb-classroom-talk5_c1 with dissolve
        play voice3 kevin_thinking_yeah1 noloop
        kb "Hedonism, baby. Life's fucked and we're all gonna die."
        kb "Gotta live it to the fullest while you're here."
        scene d16s04-27 mc-kb-classroom-talk6_c1 with dissolve
        kb "And waste not, want not, my friend. Gotta recycle where you can and not let anything go to waste."
        play voice2 mc_thinking_emm1 noloop
        mc "There {i}has{/i} to be better ways to live life. And there {i}{b}has{/b}{/i} to be better things to fucking recycle."
        scene d16s04-29 mc-kb-classroom-talk8_c1 with dissolve
        play voice3 kevin_arrogant_heh1 noloop
        kb "Try it before you razz me."
        play voice2 mc_disappointed_ehh4 noloop
        mc "Eh, I think I'm good."
        scene d16s04-28 mc-kb-classroom-talk7_c1 with dissolve
        play voice3 kevin_thinking_hmm5 noloop
        kb "A day's gon' come where you have to suck a creampie—maybe even your own, I ain't judging—from the ass and/or pussy of a person you love, and I want you to remember your old pal Kevo when it happens."
        play voice2 d4s4_mclaugh noloop
        mc "*Chuckles* Right, I'll keep you in mind."
        scene d16s04-24 mc-kb-classroom-talk3_c1 with dissolve
        kb "And, I forgot to mention. I got a Gold Star for that. So who's the creampie sucker now?"
    else:
        scene d16s04-28 mc-kb-classroom-talk7_c1 with dissolve
        play voice3 kevin_thinking_hmm6 noloop
        kb "Pretty good. Great even. God, I love that woman."
        play voice2 mc_yes_yeah2 noloop
        mc "Good for you, man. You deserve someone good."
        scene d16s04-22 mc-kb-classroom-talk1_c1 with dissolve
        play voice3 kevin_happy_heh2 noloop
        kb "Thanks."
        kb "It's always equal parts hilarious and nauseating whenever I suggest doing something to her."
        play voice2 mc_surprised_what2 noloop
        mc "Wait, what? Why?"
        scene d16s04-23 mc-kb-classroom-talk2_c1 with dissolve
        play voice3 kevin_thinking_hmm7 noloop
        kb "It's just that I always think that she isn't going to be into the shit I'm into, but nope. She just goes along with whatever."
        kb "I love how open minded she is about stuff."
        play voice2 mc_arrogant_hm1 noloop
        mc "Hm."
        scene d16s04-24 mc-kb-classroom-talk3_c1 with dissolve
        kb "Oh, we got a Gold Star recently as well."

    scene d16s04-37 mc-kb-classroom-talk17_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    if date_cb is True:
        mc "Still you. But hold up. You got a Gold Star?"
    else:
        if week_1_goldstar is True or d09s07_goldstar is True or d12s01_goldstar is True:
            mc "Hold up. You got a Gold Star?"
        else:
            mc "A Gold Star, huh?"
    if week_1_goldstar is True or d09s07_goldstar is True or d12s01_goldstar is True:
        scene d16s04-37 mc-kb-classroom-talk17_c2 with dissolve
        play voice3 kevin_thinking_yeah3 noloop
        kb "Yeah."
        scene d16s04-34 mc-kb-classroom-talk14_c1 with dissolve
        play voice2 mc_angry_huh2 noloop
        mc "...How?"
        scene d16s04-34 mc-kb-classroom-talk14_c2 with dissolve
        play voice3 kevin_surprised_what2 noloop
        kb "What do you mean how?"
        play voice2 mc_disappointed_ah1 noloop
        if is_antagonist_mode is False:
            mc "Are you in the VIP program?"
        else:
            mc "Are you in the retention program?"
        scene d16s04-46 mc-kb-classroom-open-talk1_c1 with dissolve
        play voice3 kevin_surprised_what3 noloop
        kb "The what now?"
        kb "My dude, I don't know what you're talking about. But I got a notification from FL a couple of days back saying that they released a new thing. That new thing was the Gold Star stuff."
        scene d16s04-46 mc-kb-classroom-open-talk1_c2 with dissolve
        play voice2 mc_arrogant_huh1 noloop
        mc "Huh, what else did it say?"
        scene d16s04-38 mc-kb-classroom-talk18_c2 with dissolve
        play voice3 kevin_disappointed_ehh2 noloop
        kb "Uhh, I don't remember. Something about how their closed beta was a success, so they're rolling it out to the masses."
        scene d16s04-38 mc-kb-classroom-talk18_c1 with dissolve
        play voice2 mc_arrogant_hm1 noloop
        mc "And what does it do exactly?"
        scene d16s04-38 mc-kb-classroom-talk18_c2 with dissolve
        play voice3 kevin_thinking_hmm4 noloop
        kb "The Gold Stars?"
    else:

        play voice2 d1s1_mmm noloop
        mct "AmRose told me about that a bit back."
        scene d16s04-37 mc-kb-classroom-talk17_c2 with dissolve
        play voice3 kevin_thinking_hmm4 noloop
        kb "You've never gotten one?"
        scene d16s04-46 mc-kb-classroom-open-talk1_c1 with dissolve
        play voice2 mc_no_no2 noloop
        mc "No."
        scene d16s04-46 mc-kb-classroom-open-talk1_c2 with dissolve
        play voice3 kevin_thinking_well noloop
        kb "Well, FL has a thing called \"Gold Stars.\" Basically, if you do some wild fetishey thing, you have a chance to get one."
        scene d16s04-38 mc-kb-classroom-talk18_c2 with dissolve
        kb "The main criteria is that what you're doing has to be pretty unique and out there."
        kb "There aren't any specific rules or fetishes that count, so you just have to freestyle it and figure it out."
        scene d16s04-38 mc-kb-classroom-talk18_c1 with dissolve
        play voice2 mc_thinking_hmm5 noloop
        if date_cb is True:
            mc "And you got one for felching Chloe?"
        else:
            mc "And you got one with Chloe?"
        mct "What did he even do with her?"
        scene d16s04-38 mc-kb-classroom-talk18_c2 with dissolve
        play voice3 kevin_thinking_yeah3 noloop
        kb "Yep."

    kb "It seems pretty interesting, said something about how you can restore daily streaks with it. Oh, you get cool badges and profile customization stuff. Discounts in the shop. Higher priority on any ads you post. Stuff like that."
    scene d16s04-39 mc-kb-classroom-talk19_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Huh..."
    scene d16s04-39 mc-kb-classroom-talk19_c2 with dissolve
    play voice3 kevin_thinking_yeah1 noloop
    kb "Yeah, it's just your usual gamify stuff. Pretty smart, IMO."
    scene d16s04-49 mc-kb-classroom-thinking1_c2 with dissolve
    play voice2 mc_angry_hm1 noloop
    if is_antagonist_mode is False:
        mct "It seems like the Gold Stars for the VIP program was a beta test or something."
    else:
        mct "It seems like the Gold Stars for the retention program was a beta test of sorts."
    mct "What does this mean? Has the function of the Stars changed?"
    play sound sfx_hair_scratch1 volume 0.7
    scene d16s04-49-2 mc-kb-classroom-thinking2_c2 with dissolve
    if is_antagonist_mode is False:
        mct "FL told me that I can use the Gold Stars to skip a challenge, but maybe that has changed now?"
    else:
        mct "FL told me that I can use the Gold Stars to skip the punishment, but maybe that has changed now?"
    scene d16s04-46 mc-kb-classroom-open-talk1_c1 with dissolve
    play voice3 kevin_thinking_hey1 noloop
    kb "You alright, man?"
    scene d16s04-46 mc-kb-classroom-open-talk1_c2 with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Hm? Yeah. Yeah, I'm alright."
    scene d16s04-46 mc-kb-classroom-open-talk1_c1 with dissolve
    mc "Just got lost in thought for a bit."
    play voice3 kevin_thinking_hmm7 noloop
    kb "Alright."

    $ renpy.music.set_volume(0.05, 5.0, "sound2")
    play voice4 cough noloop volume 0.7
    scene d16s04-40 mc-kb-rn-classroom-entry1_c2 with dissolve
    rn "Good morning, everyone."
    scene d16s04-31 mc-kb-classroom-talk11_c1 with dissolve
    pause
    scene d16s04-41 mc-kb-rn-classroom-entry21_c2 with dissolve
    rn "I was caught up with some personal things today, so it seems I was a bit late."
    scene d16s04-42 mc-kb-classroom-phone1_c1 with dissolve
    pause
    play sound sfx_phone_tapping1 volume 1.5
    scene d16s04-43 mc-kb-classroom-phone2_c2 with dissolve
    mct "Bingo. It's right here."
    if is_antagonist_mode is False:
        mct "Says here that I have one ongoing challenge and that I can reduce the length of it for three Gold Stars!"
    else:
        mct "Says here that I have one ongoing punishment and that I can reduce the length of it for three Gold Stars!"
    scene d16s04-44 mc-kb-classroom-phone3_c2 with dissolve
    play voice2 d1s5_mcthinks noloop
    if is_antagonist_mode is False:
        mct "And apparently I've gone through this challenge long enough that I could end it right now!"
    else:
        mct "And apparently I've gone through the punishment long enough that I can end it right now!"

    if fl_goldstars >= 3:
        mct "Jesus Christ, I have just barely enough."
        scene d16s04-45 mc-kb-classroom-phone4_c2 with dissolve
        mct "But I can end this!"
        mct "Wait... Should I do this later tonight or right now?"
        play voice2 d2s9_confused noloop
        scene d16s04-49-2 mc-kb-classroom-thinking2_c2 with dissolve
        mct "I want to be out of this fucking thing yesterday, but getting it off right now might be...awkward."

        menu:
            "Freedom, {i}{b}now{/b}{/i}"(hint="d16s04m01c01"):

                $ d16s04_cage_out = True
                $ cockcage_released = True
                $ fl_goldstars -= 3

                play sound sfx_hair_scratch1 volume 0.7
                scene d16s04-49 mc-kb-classroom-thinking1_c2 with dissolve
                play voice2 mc_angry_hm2 noloop
                mct "Fuck that. I want out, {i}{b}now{/b}{/i}"

                $ Lovense.stop()

                scene d16s04-45 mc-kb-classroom-phone4_c2 with dissolve
                mct "What now?"
                $ Lovense.vibrate(10)
                play sound cockcage_lock_off

                flr "Your request has been received and approved. Enjoy your freedom!"
                scene d16s04-47 mc-kb-classroom-open-pent1_c2 with dissolve

                $ Lovense.stop()

                play voice3 kevin_surprised_huh1 noloop
                kb "Huh?"
                scene d16s04-46 mc-kb-classroom-open-talk1_c2 with dissolve
                play voice2 mc_surprised_huh2 noloop
                mct "Shit, I forgot that Kevin was here."
                mc "Don't freak out. It's just I need to do this right now."
                scene d16s04-46 mc-kb-classroom-open-talk1_c1 with dissolve
                play voice3 kevin_happy_heh2 noloop
                kb "Alright...?"
                scene d16s04-48 mc-kb-classroom-open-pent2_c2 with dissolve
                play sound sfx_jeans_on1
                kb "..."
                mc "..."
                play sound sfx_cloth_rustling1
                scene d16s04-50 mc-kb-classroom-talk2_c2 with dissolve
                play voice2 mc_disappointed_ehh1 noloop
                if is_antagonist_mode is False:
                    mc "I failed a challenge from FL. This was my new challenge."
                else:
                    mc "I failed a thing from FL. This was my punishment."
                mc "You talking about the Gold Stars made me think and uh... yep."
                play voice3 kevin_happy_heh3 noloop
                kb "...Huh."

                $ fl_achievement_unlock("d16s10n01")
                $ unlock_gallery_slot("extra", "d16s10n01")

                if date_cb is True:

                    $ d16s04_gavecage = True

                    scene d16s04-50 mc-kb-classroom-talk2_c1
                    if cage_ntr is False:
                        show d16s04-50 mc-kb-classroom-talk2-lc_c1
                    with dissolve
                    play voice3 kevin_thinking_hmm4 noloop
                    kb "Can I have it?"
                    play voice2 mc_surprised_what1 noloop
                    mc "...What?"
                    play voice3 kevin_thinking_hmm7 noloop
                    kb "If you're not using it."
                    scene d16s04-50 mc-kb-classroom-talk2_c2 with dissolve
                    play voice2 mc_surprised_huh6 noloop
                    mc "...You want the cock cage that I wore?"
                    play voice3 kevin_thinking_yeah2 noloop
                    kb "Yep."
                    play voice2 d3s7_mcemm noloop
                    mc "..."
                    scene d16s04-51 mc-kb-classroom-cage_c1
                    play sound sfx_sextoy_uncuff1
                    if cage_ntr is False:
                        show d16s04-51 mc-kb-classroom-cage-lc_c1
                    with dissolve
                    play voice2 mc_yes_yeah1 noloop
                    mc "Yeah, sure, alright. Here."
                    scene d16s04-53 mc-kb-classroom-talk4_c1 with dissolve
                    play voice3 kevin_happy_thanks noloop
                    kb "Thanks man."
                    scene d16s04-53 mc-kb-classroom-talk4_c2 with dissolve
                    play voice2 mc_yes_aga2 noloop
                    mc "No problem. Reduce, reuse, recycle, right?"
                else:
                    scene d16s04-50 mc-kb-classroom-talk2_c1
                    if cage_ntr is False:
                        show d16s04-50 mc-kb-classroom-talk2-lc_c1
                    with dissolve
                    play voice3 kevin_thinking_hmm3 noloop
                    kb "Guess that's another use for the Gold Stars then."
                    kb "Versatile things."
                    scene d16s04-50 mc-kb-classroom-talk2_c2 with dissolve
                    play voice2 mc_yes_yeah1 noloop
                    mc "Yep."
                    scene d16s04-54 mc-kb-classroom-talk5_c1 with dissolve
                    play voice3 kevin_thinking_hmm4 noloop
                    kb "Hey, no one's gonna know about this from me."
                    kb "Scout's honor."
                    scene d16s04-54 mc-kb-classroom-talk5_c2 with dissolve
                    play voice2 mc_thinking_hmm2 noloop
                    mc "Thanks, man. I appreciate it."
                scene d16s04-49-4 mc-kb-classroom-thinking4_c2 with dissolve
                pause
            "Hold out for a better opportunity"(hint="d16s04m01c02"):


                play sound sfx_hair_scratch1 volume 0.7
                scene d16s04-49 mc-kb-classroom-thinking1_c2 with dissolve
                play voice2 mc_thinking_hmm5 noloop
                mct "I think it's best if I wait it out."
                mct "I waited this long, I can wait a couple more hours."
                scene d16s04-49-4 mc-kb-classroom-thinking4_c2 with dissolve
                pause
    else:

        scene d16s04-45 mc-kb-classroom-phone4_c2 with dissolve
        play voice2 mc_thinking_hmm5 noloop
        mct "Do I even have any?"
        "..."
        scene d16s04-44 mc-kb-classroom-phone3_c2 with dissolve
        play voice2 mc_angry_hm2 noloop
        mct "Damn."
        mct "Well, shit. There goes that plan."
        scene d16s04-43 mc-kb-classroom-phone2_c2 with dissolve
        mct "At least I know that it can be done."
        mct "Now where the hell do I find {i}{b}three{/b}{/i} Gold Stars...?"

    if date_sy is True:
        call buzz from _call_buzz_13
        scene d16s04-45 mc-kb-classroom-phone4_c2 with dissolve
        sy "Oi are you out of class yet?"
        mct "Stacy?"
        play sound sfx_message_out1
        mct "No it just started."
        scene d16s04-44 mc-kb-classroom-phone3_c2 with dissolve
        play sound sfx_message_in1
        sy "Ok well I got a thing I gotta go to."
        play sound sfx_message_in1
        sy "Could you pick me up after class?"
        mct "\"Thing\"?"
        scene d16s04-43 mc-kb-classroom-phone2_c2 with dissolve
        play sound sfx_message_out1
        mct "Sure."
        play sound sfx_message_in1
        sy "Nice luv u byeeee xoxo."
        play sound sfx_message_in1
        sy "Study hard ya dingus."
    elif date_aw is True:
        call buzz from _call_buzz_14
        scene d16s04-45 mc-kb-classroom-phone4_c2 with dissolve
        mct "Allison?"
        aw "Hey, are you busy?"
        scene d16s04-44 mc-kb-classroom-phone3_c2 with dissolve
        play sound sfx_message_out1
        mct "Depends what's up?"
        play sound sfx_message_in1
        aw "Can you come over for a bit?"
        if date_awvw:
            scene d16s04-43 mc-kb-classroom-phone2_c2 with dissolve
            play voice2 mc_thinking_hmm1 noloop
            mct "Hm, this might be my chance to talk to Allison about what went down at the party."
        menu:
            "I'll be over"(hint="d16s05m03c01"):
                play sound sfx_message_out1
                mct "Sure im in class rn."
                scene d16s04-45 mc-kb-classroom-phone4_c2 with dissolve
                play sound sfx_message_out1
                mct "I can be over in a bit tho."
                play sound sfx_message_in1
                aw "Great! Thank you."
            "I won't be able to come"(hint="d16s05m03c02"):


                $ d16_aw_reject = True

                play sound sfx_message_out1
                mct "Sorry im with someone rn."
                scene d16s04-45 mc-kb-classroom-phone4_c2 with dissolve
                play sound sfx_message_in1
                aw "Oh, it's alright then."
                play sound sfx_message_in1
                aw "See you later."

    play voice4 cough noloop volume 0.7
    scene d16s04-60 mc-kb-rn-classroom-exit_c2 with dissolve
    rn "Alright. Let's get started then, shall we?"
    stop sound2 fadeout 3.0
    stop music fadeout 3.0

    jump d16s05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
