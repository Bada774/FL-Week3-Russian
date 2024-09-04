label d19s08:

    if not hasattr(renpy.store, "d17s05_luvutoo"):
        if d17s05_love_mh_op is True or d17s05_love_mh_sy is True or d17s05_love_mh is True:
            $ d17s05_luvutoo = True
        elif True:
            $ d17s05_luvutoo = False

    $ d19s08_mh_pic = False
    $ d19s08_mh_talk = False
    $ d19s08_mh_help = False

    scene black
    show screen scene_transistion(_("30 minutes later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene d19s08-01 mc-arrives-sy-apartment_c1
    with Fade(0.5, 0.5, 0.9)
    pause
    scene d19s08-02 mc-knocks-sy-apartment-door_c1 with dissolve
    call knock from _call_knock_8
    scene d19s08-03 noone-answers-mc-wonders-why_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "Is Stacy not home?"
    play sound sfx_door_open5 volume 0.6
    scene d19s08-04 mc-tries-door-opens_c1 with dissolve
    $ renpy.music.set_volume(0.6, 4.5, "music")
    play music saxophone_sexy1
    pause
    play sound sfx_door_closed1
    scene d19s08-05 mc-looks-around-sy-apartment_c1 with dissolve
    $ renpy.music.set_volume(0.05, 1.0, "sound4")
    play sound4 shower fadein 1.5
    pause
    $ renpy.music.set_volume(0.6, 1.0, "sound4")
    scene d19s08-06 sy-taking-shower-startled_c1 with fade
    play voice3 stacy_hey noloop
    sy "Hello!? Did someone come in?"
    $ renpy.music.set_volume(0.05, 1.0, "sound4")
    scene d19s08-07 mc-answers-sy_c1 with fade
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah! It's me!"
    $ renpy.music.set_volume(0.6, 1.0, "sound4")
    scene d19s08-08 sy-not-happy-mc-walked-in-apartment_c1 with fade
    play voice3 polly_pollyangry noloop
    sy "Jesus, [mcname]! Don't sneak up on a girl like that! Christ."
    $ renpy.music.set_volume(0.05, 1.0, "sound4")
    scene d19s08-09 mc-tells-sy-keep-door-locked-chuckles_c1 with fade
    play voice2 d4s4_mclaugh noloop
    mc "I knocked! You weren't there."
    mc "If you didn't want me to come in, you should've just locked the door."
    $ renpy.music.set_volume(0.6, 1.0, "sound4")
    scene d19s08-06 sy-taking-shower-startled_c1 with fade
    play voice3 stacy_angry noloop
    sy "I swear if I was there, I'd smack you right now."
    $ renpy.music.set_volume(0.05, 1.0, "sound4")
    scene d19s08-10 mc-sits-table_c1 with fade
    stop sound4 fadeout 3.0
    play voice2 mc_thinking_mmm5 noloop
    mct "Man. This is Stacy's first apartment and the poor girl hasn't even had the time to decorate it or anything."
    mct "All because she's been hyper focused on this Fetish Locator stuff."
    scene d19s08-11 mc-looks-around-apartment-empty_c1 with dissolve
    mct "I need to treat her to something nice after all this blows over."

    if date_mh is True and d19s03_go_to_mh is False:
        $ d19s08_mh_talk = True
        call buzz from _call_buzz_36
        scene d19s08-12 mc-checks-phone-has-message_c1 with dissolve
        play voice2 mc_thinking_hmm3 noloop
        mct "Lyssa messaged me?{w} Let's see."
        scene d19s08-14 mh-picture-naked-kitchen_c1 with dissolve
        play sound sfx_message_in1
        mh "Thinking about you."
        scene d19s08-13 mc-checks-mh-message_c1 with dissolve
        play voice2 mc_surprised_wow2 noloop
        mct "Oh wow!"
        scene d19s08-15 mc-smiles-remembers-forgot-call-mh_c1 with dissolve
        play voice2 mc_surprised_huh3 noloop
        mct "Oh shit, right! I wanted to call Lyssa to talk about what to do with Zarah."
        scene d19s08-12 mc-checks-phone-has-message_c1 with dissolve
        mct "But is it even worth it? I {i}know{/i} that Zarah will not vote for me no matter what."
        mct "What's the point of trying? It'd just be a waste of time anyway."
        menu:
            "Ask Lyssa for help"(hint="d19s08m01c01"):
                $ d19s08_mh_help = True
                scene d19s08-16 mc-calls-mh_c1 with dissolve
                play voice2 mc_arrogant_heh1 noloop
                mct "I guess there still might be a chance. Might as well take it."
            "Don't bother"(hint="d19s08m01c02"):

                scene d19s08-16 mc-calls-mh_c1 with dissolve
                play voice2 mc_arrogant_hm3 noloop
                mct "Yeah. Fuck that. There's nothing I can do about Zarah. But I'm still gonna call Lyssa."

        scene d19s08-17 mh-lounge-eating-fruit_c1 with Fade(0.4, 0.4, 0.4)
        play sound sfx_bite_apple1
        pause
        call buzz from _call_buzz_37
        scene d19s08-18 mh-phone-rings-picks-up_c1 with dissolve
        pause
        scene d19s08-19 mh-talking-smiling_c1 with dissolve
        play voice3 lissa_mmm1 noloop
        mh "[mcname]? Miss me already?"
        scene d19s08-20 talking-about-picture_c1 with dissolve
        play voice2 mc_yes_yeah1 noloop
        if date_mh_bdsm is True:
            mc "Considering the picture you sent me, I'm thinking you were the one missing {i}me{/i} instead."
        elif date_mh_bdsm is False and d15s06_luvutoo is True and d17s05_luvutoo is True:
            mc "Of course I do. Always."
        if d19s08_mh_help is True:
            mc "I actually called to ask you something."
            scene d19s08-23 mh-turns-sideways-hand-between-thighs_c1 with dissolve
            play voice3 lissa_moan1 noloop
            mh "Ask away."
            scene d19s08-22 mc-wants-talk-about-zarrah_c1 with dissolve
            play voice2 mc_thinking_mmm4 noloop
            mc "Alright. So there's a woman, Zarah."
            play voice3 lissa_ugu2_phonetalk noloop
            mh "Mm-hm."
            mc "She's on the board of judges that will evaluate my finals.{w} And she's one mean bitch."
            mh "Ouch."
            scene d19s08-24 mc-explaining-about-zarah_c1 with dissolve
            play voice2 mc_yes_yeah5 noloop
            mc "Yeah. She fucking hates my guts."
            queue voice2 mc_thinking_emm1 noloop
            mc "She will absolutely tank me no matter how well I— What's that sound?"
        elif True:
            mc "How are you doing? I know we haven't exactly been able to talk that much lately."
            scene d19s08-23 mh-turns-sideways-hand-between-thighs_c1 with dissolve
            play voice3 lissa_moan1 noloop
            mh "It's alright. It's nice hearing your voice.{w} Though..."
            mh "I {i}have{/i} missed you, a little."
            scene d19s08-22 mc-wants-talk-about-zarrah_c1 with dissolve
            play voice2 d1s2_hmm noloop
            mc "Only a little? I'm sensing a lie."
            play voice3 lissa_ugu2_phonetalk noloop
            mh "A white lie."
            play voice2 mc_thinking_emm1 noloop
            mc "*Sigh* I'm sorry, Lyssa. I— What's that sound?"
        play sound sfx_handjob_cream1 fadein 1.0 loop
        scene d19s08-25 mh-starts-massaging-dick_c1 with dissolve
        play voice3 lissa_laugh2 noloop
        mh "...What sound?"
        stop sound fadeout 1.0
        scene d19s08-26 mc-tells-mh-zarah-out-to-get-him_c1 with dissolve
        play voice2 mc_thinking_hmm2 noloop
        mc "At first I thought it was just some fabric sound, but it's repetitive."
        mc "You're jerking off right now, are you?"
        play sound sfx_handjob_cream1 fadein 1.0 loop
        scene d19s08-28 mh-denies-jerking-off_c1 with dissolve
        play voice3 lissa_moan2 noloop
        mh "Absolutely not. What could possibly make you think that?"
        stop sound fadeout 1.0
        scene d19s08-27 mc-surprised-asks-mh-masturbating_c1 with dissolve
        play voice2 mc_happy_hah1 noloop
        mc "*Chuckles* Uh-huh."
        menu:
            "Ask for a picture"(hint="d19s08m02c01"):
                $ d19s08_mh_pic = True

                scene d19s08-29 mc-wants-picture-mh-masturbating_c1 with dissolve
                play voice2 mc_hey_hey3 noloop
                mc "Send me a picture."
                mh "I would, if I was doing anything. But considering I'm not doing anything, I have nothing to send."
                play voice2 mc_yes_yes2 noloop
                mc "Riiight."
                scene d19s08-30 mh-agrees-to-send-later_c1 with dissolve
                play voice3 lissa_haha noloop
                mh "*Laughs* Fine, fine. But not right now."
                mh "Continue what you were saying first."
            "Don't"(hint="d19s08m02c02"):

                pass

        if d19s08_mh_help is True:
            scene d19s08-31 mc-continues-talking-zarah_c1 with dissolve
            play voice2 mc_thinking_hmm5 noloop
            mc "Right. So, Zarah. She's gonna be one of my judges for my finals, and she absolutely hates me."
            mc "Even if I do well, she will fail me no matter what."
            mc "I called to ask if you knew if there were some sort of...I don't know. Legal action that I could take."
            scene d19s08-32 mh-talking-phone_c1 with dissolve
            play voice3 lissa_moan3 noloop
            mh "Hm. Spiteful school faculty is always a pain."
            mh "I don't know if there are any {i}legal{/i} actions we can take. For one thing, we can't exactly prove that she will unjustly fail you. Second of all, this isn't my area of expertise."
            mc "Damn."
            mh "{i}But{/i}, we still might be able to do something."
            scene d19s08-33 mh-talking-phone-looking-nails_c1 with dissolve
            play voice3 lissa_haha2 noloop
            mh "You'd be surprised at how much more open to negotiation people can be when you have a lawyer by your side."
            mh "I think the best course of action here is for you to speak with her directly."
            mh "Try to see if you can get her to say why she doesn't like you, or maybe even admit that she will vote against you no matter what."
            scene d19s08-38 mh-phone-pings-end-call_c1 with dissolve
            play voice3 lissa_aga noloop
            mh "I'll be there, hidden, listening in."
            mh "Once she's cornered, I'll talk to her. See if she can be reasoned with."
            mh "If not, well, we will have enough information to go directly to the school dean and sort it out there."
            scene d19s08-34 mc-frustrated-about-options_c1 with dissolve
            play voice2 mc_disappointed_ehh1 noloop
            mc "*Sigh* So in the end, talking with her is my only option, huh?"
            play voice3 lissa_phonetalk_yes noloop
            mh "It's the option most likely to work."
            if d17s05_mh_sy is True:
                scene d19s08-36 mc-continues-phonecall-mh_c1 with dissolve
                play voice2 d3s11b_mcheh noloop
                mc "*Chuckles* Y'know, Stacy said the same thing to me."
                play voice3 lissa_oh2_phonetalk noloop
                mh "She's a smart one."
                scene d19s08-35 mc-yells-sy_c1 with dissolve
                play voice2 mc_hey_hey1 noloop
                mc "Oi, dummy! Lyssa says that you're smart."
                play voice3 maria_ah noloop
                sy "*High-pitched noises of elation* AREYOUONCALLWITHLYSSARIGHTNOW?"
                sy "Tell her to come over!"
                scene d19s08-36 mc-continues-phonecall-mh_c1 with dissolve
                play voice2 mc_happy_yay2 noloop
                mc "She's so smart, she's trying to talk with dolphins now."
                play voice3 lissa_laugh_phonetalk noloop
                mh "*Laughs* She's adorable. You really need to stop teasing her so much."
                scene d19s08-16 mc-calls-mh_c1 with dissolve
                play voice2 mc_hey_hey2 noloop
                mc "I barely even tease her!"
                mc "Anyway, we've been derailed."
            scene d19s08-26 mc-tells-mh-zarah-out-to-get-him_c1 with dissolve
            play voice2 mc_arrogant_huh1 noloop
            mc "Alright. So lure Zarah out, talk with her, and see if we can get any incriminating information out of her."
            mc "Well, if I got nothing else, I might as well try that."
            mc "Are you free tomorrow?"
            scene d19s08-32 mh-talking-phone_c1 with dissolve
            play voice3 lissa_thinking noloop
            mh "Not exactly. But I'm sure I can make some time. Just let me know when you need me."
            scene d19s08-20 talking-about-picture_c1 with dissolve
            play sound sfx_phone_ping1_remoted volume 1.5
            mc "Great—"
        elif True:
            scene d19s08-31 mc-continues-talking-zarah_c1 with dissolve
            play voice2 mc_thinking_hmm5 noloop
            mc "Right. Well, I was just saying that I've been...going through some stuff. Plus the exams, and it's just been a bit of a clusterfuck all around."
            scene d19s08-38 mh-phone-pings-end-call_c1 with dissolve
            play voice3 nora_hey noloop
            mh "Hey. It's okay. I don't want this to become something we stress about."
            mh "You're going through a lot. I get it. You don't have to add me to that list as well."
            scene d19s08-37 mc-decides-to-try-lure-zarah_c1 with dissolve
            play voice2 mc_thinking_hmm1 noloop
            mc "I have nothing to worry about you."
            scene d19s08-33 mh-talking-phone-looking-nails_c1 with dissolve
            play voice3 lissa_aga noloop
            mh "You understand what I'm saying."
            mh "I'll still be there on the other side after everything settles down."
            scene d19s08-29 mc-wants-picture-mh-masturbating_c1 with dissolve
            play voice2 mc_thinking_hmm4 noloop
            mc "Maybe we can go someplace nice after this. Someplace far away."
            scene d19s08-32 mh-talking-phone_c1 with dissolve
            play voice3 lissa_ugu noloop
            mh "Exactly."
            if d17s05_mh_sy is True:
                mh "Maybe Stacy can join us as well."
                scene d19s08-36 mc-continues-phonecall-mh_c1 with dissolve
                play voice2 d3s11b_mcheh noloop
                mc "*Chuckles* She's going to flip when she hears that."
                scene d19s08-35 mc-yells-sy_c1 with dissolve
                play voice2 mc_hey_hey1 noloop
                mc "Oi, dummy! Lyssa says that we should go on a date, all three."
                play voice3 maria_ah noloop
                sy "*High-pitched noises of elation* AREYOUONCALLWITHLYSSARIGHTNOW?"
                sy "Tell her to come over!"
                scene d19s08-36 mc-continues-phonecall-mh_c1 with dissolve
                play voice2 mc_happy_yay2 noloop
                mc "She's so excited, she's trying to talk with dolphins now."
                play voice3 lissa_laugh_phonetalk noloop
                mh "*Laughs* She's adorable. You really need to stop teasing her so much."
                scene d19s08-16 mc-calls-mh_c1 with dissolve
                play voice2 mc_hey_hey2 noloop
                mc "I barely even tease her!"
                mc "Anyway, we've been derailed—"
            elif d17s05_mh_op is True:
                mh "Maybe Oliver can join us as well."
                scene d19s08-16 mc-calls-mh_c1 with dissolve
                play voice2 mc_yes_yeah2 noloop
                mc "Yeah—"
            play sound sfx_phone_ping1_remoted volume 1.5
            scene d19s08-20 talking-about-picture_c1 with dissolve
        play voice2 mc_happy_a1 noloop
        mc "You sure are in high demand tonight, huh?"
        scene d19s08-33 mh-talking-phone-looking-nails_c1 with dissolve
        play voice3 lissa_laugh2 noloop
        mh "*Chuckles* It's my dinner. It's here, finally."
        scene d19s08-37 mc-decides-to-try-lure-zarah_c1 with dissolve
        play voice2 mc_yes_okay3 noloop
        $ unlock_gallery_slot("cg", "d19s08mh")
        mc "You should go get that then. I'll talk to you later."
        if d15s06_luvutoo is True and d17s05_luvutoo is True:
            mh "I love you."
            play voice2 mc_yes_yeah1 noloop
            mc "Love you too."

    jump d19s09

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
