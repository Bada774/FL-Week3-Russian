image e02s09-a51-glambot-1 = Movie(play = "images/E-02/s09/anim/e02s09-a51-2x-50fps.webm", start_image = "e02s09-a51 mh-hesitant-mc-thinks-not-sounding-like-mh-glambot-51-00_i", image = "e02s09-a51 mh-hesitant-mc-thinks-not-sounding-like-mh-glambot-51-89_i", loop = False)

label e02s09:

    scene black
    show screen scene_transistion(_("Time to go home"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound4 sfx_fire_fireplace1 fadein 3.0
    $ renpy.music.set_volume(0.4, 0.0, "sound4" )
    scene e02s09-01 mc-mh-packing-stuff_c1
    with Fade(0.5, 0.5, 0.9)
    play sound sfx_jeans_fly1
    pause
    play voice3 lissa_thinking noloop volume 1.4
    mh "Everything set?"
    play voice2 mc_yes_yes1 noloop
    mc "Yes. We're good to go."
    stop sound4 fadeout 1.5
    $ renpy.music.set_volume(0.5, 0.0, "sound2" )
    play sound2 sfx_weather_arctic_wind fadein 3.0
    play sound sfx_cloth_suitcase_ride1
    scene e02s09-02 mh-mc-leaving-cabin_c1 with dissolve
    pause
    scene e02s09-03 mc-looking-back-resort_c1 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "I'm sorry to see it go."
    play voice3 lissa_moan1 noloop
    mh "We'll be back again, Baby."

    if e02s05_6 and e02s05_7 and e02s05_8:
        $ fl_achievement_unlock("e02s05n01")
        $ unlock_gallery_slot("extra", "e02s05n01")

    play sound sfx_cloth_suitcase_ride1
    scene e02s09-04 mc-mh-leave-snowy-peaks_c1 with dissolve
    pause
    stop sound2 fadeout 3.5
    stop sound fadeout 3.0
    scene black
    show screen scene_transistion(_("Back at the office"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_door_closed7
    scene e02s09-05 mh-mc-enter-office-mess_c1
    with Fade(0.5, 0.5, 0.5)
    $ renpy.music.set_volume(0.25, 0.0, "music" )
    play music memory_puzzles
    pause
    play voice3 dahlia_arrogant_huh noloop
    mh "Oliver?"
    scene e02s09-06 op-scared-relieved-mh-back_c1 with dissolve
    play voice4 oliver_ah2 noloop volume 1.5
    op "Lyssa! You're back! It's terrible!"
    scene e02s09-07 mh-steps-forward-wants-op-calm-down_c1 with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    mh "Oliver, take a breath. What happened?"
    play voice4 oliver_huh2 noloop volume 1.5
    op "Didn't you get my voicemail?"
    scene e02s09-08 mh-got-msg-didnt-understand-mc-nods-background_c1 with dissolve
    play voice3 lissa_yes noloop
    mh "It was a little difficult to understand you clearly."
    mct "That's putting it lightly."
    play voice2 d9s2_yeah noloop volume 2.0
    mc "It's alright, Oliver. We're here so you can just tell us what happened."
    scene e02s09-09 op-gives-mh-letter_c1 with dissolve
    play voice4 oliver_ehh2 noloop volume 1.6
    op "Right. Here you go, Lyssa."
    play sound sfx_paper_slide1
    scene e02s09-10 mh-reads-paper-mc-ask-what-is-it-mh-curses-latin_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.8
    mc "What is it?"
    play voice3 nora_huh noloop
    mh "Illi nothi!"
    scene e02s09-11 mc-confused-mh-explains-phrase_c1 with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "Ill what now?"
    play voice3 dahlia_angry_hm1 noloop
    mh "Illi nothi. Latin for \"those bastards\"!{w} I will bring ruin down on them for this!"
    scene e02s09-12 mc-tries-defuse-situation-wants-caught-up-situation_c1 with dissolve
    play voice2 mc_surprised_wow1 noloop
    mc "Wow wow wow. Let's not get biblical."
    mc "Can one of you please catch me up?"
    scene e02s09-13 mh-close-eyes-frustration-explains_c1 with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    mh "It is a letter from Silvercorp..."
    play voice2 d2s9_confused noloop
    mc "Who?"
    mh "They're one of the largest, most ruthless firms in the county."
    scene e02s09-14 op-corrects-mh-state-she-not-sure_c1 with dissolve
    play voice4 oliver_hey_happy noloop volume 1.4
    op "In the state!"
    play voice3 dahlia_thinking_hmm1 noloop
    mh "I don't know about that."
    scene e02s09-15 mc-talking-mh_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "So what? They're trying to buy you up or something? Big fish eating a smaller fish?"
    play voice3 lissa_lno noloop
    mh "I wish it was that. A problem like that would have a simple solution. This is much worse."
    mh "This is a letter of intent. Silvercorp is suing me over ethical violations that I apparently committed in a previous case."
    scene e02s09-16 mc-shocked_c1 with dissolve
    play voice2 mc_scared_huuuh3 noloop
    mc "Holy shit!"
    mc "What do you mean?"
    scene e02s09-17 mh-thinking-diabolical-move-talks-op-not-listening_c1 with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    mh "It is a rather diabolical move, framed by Silvercorp's trademark \"subtlety\"."
    mh "Oliver, refresh my memory. They are moving forward with the...{w} Fanderly Case correct?"
    mh "Oliver..."
    play sound sfx_cloth_rustling2
    scene e02s09-18 mh-arm-op-shoulder-he-gets-inspired_c1 with dissolve
    play voice3 dahlia_arrogant_hm noloop
    mh "This is not the end."
    scene e02s09-19 later-op-checks-phone-trial-two-weeks_c1 with dissolve
    play voice4 oliver_um1 noloop volume 1.4
    op "Yes. Fanderly didn't take the settlement. It's going to trial in uh... two weeks."
    scene e02s09-20 mh-apologizes-mc-no-worries-still-lost-mh-explains-again-letter_c1 with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    mh "I am sorry, [mcname]. It appears we will not be taking another trip for some time."
    play voice2 mc_thinking_emm1 noloop
    mc "That's okay. But I'm still a bit lost."
    scene e02s09-21 mh-talk-mc-listening_c1 with dissolve
    play voice3 dahlia_angry_oof noloop
    mh "The letter is a classic ploy."
    mh "If you think a lawyer is going to be brought in against you in an important case, sometimes the best, albeit most frivolous way to delay them..."
    play voice2 mc_surprised_huh6 noloop
    mc "Is to sue them?!{w} Feels kind of heavy-handed."
    scene e02s09-22 mh-rep-tarnished-mc-jesus_c1 with dissolve
    play voice3 nora_angrymoan noloop
    mh "Absolutely. But Silvercorp knew that if Fanderly's attorney brought me in, their case would be dead in the water."
    play voice2 mc_thinking_oh1 noloop
    mc "So it's like baseball. If you're facing off against a home run champ, you can just walk him."
    mh "Yes. But instead of beaning me with the ball, they are tarnishing my reputation."
    mc "Jesus..."
    scene e02s09-23 op-talk-mh-offered-way-out-mh-declines-on-spot_c1 with dissolve
    play voice4 oliver_mmm2 noloop
    op "They did offer us an out, Lyssa. Six months probation, review by the judiciary following completion of several ethics classes."
    play voice3 dahlia_no_serious noloop
    mh "Absolutely not, Oliver. We have to fight this, accepting any deal from them is not an option. Period."
    mh "Even if there were no punishment, it would be a black mark on my record that would never wash off."
    scene e02s09-24 mc-ready-fight-mh-thankful-but-hard-part_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah! We can't let these jerks get what they want."
    play voice3 lissa_ugu noloop
    mh "Thank you, [mcname]. But here comes the hard part."
    scene e02s09-25 mh-defending-herself-cant-defend-mc-aswell_c1 with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    mh "Because I'll be busy defending myself, that means I cannot defend anyone else."
    mh "Not until I clear this."
    scene e02s09-26 mc-how-help-mh-sends-op-coffee_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "How can I help?"
    play voice3 dahlia_thinking_mmm2 noloop
    mh "Oliver, please put on a new pot of coffee."
    play sound sfx_door_closed7
    play sound3 ["<silence 0.3>", sfx_chair_slide1] noloop
    scene e02s09-27 mh-shows-mc-stacks-docs-wants-organized_c1 with dissolve
    play voice3 lissa_thinking noloop
    mh "[mcname], I need you to start by organizing that pile by date."
    play sound maria_kiss1
    scene e02s09-28 mc-doing-work-mh-kisses-him-sorry-mc-okay_c1 with dissolve
    pause
    scene e02s09-29 mh-bending-over-mc-talk_c1 with dissolve
    play voice3 lissa_moan2 noloop
    mh "I am so sorry about this, Baby."
    play voice2 mc_hey_hey3 noloop
    mc "It's alright. You know me, always eager to help."
    mh "Indeed. But you should know...{w} This will not be a walk in the park."
    mc "Your fights are my fights, Lyssa. Let's do this."

    jump e02s09_home

label e02s09_home:

    $ renpy.music.set_volume(0.8, 2.0, "music" )
    scene black
    show screen scene_transistion(_("Late in the night"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.35, 3.0, "music" )
    play sound sfx_door_open2
    scene e02s09-30 mh-mc-home-bedroom-both-tired_c1
    with Fade(0.5, 0.5, 0.5)
    pause
    play voice2 mc_disgust_meh3 noloop
    mct "I never want to look at another legal form again."
    scene e02s09-31 mh-closes-eyes-wishes-still-resort_c1 with dissolve
    play voice3 lissa_moan1 noloop
    mh "Mmmm."
    mh "I wish we never came down from the mountains. I am so sorry you got dragged into this."
    scene e02s09-32 mc-gone-over-silver-lining_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "Don't be. We've gone over this."
    mc "Besides, there is already a silver lining."
    scene e02s09-33 mh-asking-what-mc-explain_c1 with dissolve
    play voice3 dahlia_surprised_huh1 noloop
    mh "There is?"
    play voice2 mc_yes_yeah4 noloop
    mc "Yup. Grinding away with you tonight taught me that I definitely dodged a bullet when I chose business over law."
    play voice3 lissa_haha2 noloop
    mh "Hahaha."
    scene e02s09-34 mh-affectionate-smile_c1 with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    mh "Well... I still very much appreciate everything you do for me, [mcname]."
    play voice2 mc_happy_a1 noloop
    mc "Thanks, but really, it's nothing."
    mc "I can't believe Silvercorp would stoop to something like this."
    mc "Are we sure they're not some kind of secret supervillain group? We could call in some superheros to help."
    play sound sfx_cloth_rustling4
    scene e02s09-35 mh-pulls-back-sad-would-be-amazing_c1 with dissolve
    play voice3 dahlia_angry_oh noloop
    mh "That would be amazing. But they are not evil. Distressing as this is, it is all just business."
    mh "I might have done the exact same thing if our roles were reversed."
    scene e02s09-36 mc-no-way-mh-helps-ppl-when-not-needed_c1 with dissolve
    play voice2 mc_no_noway noloop
    mc "No way. Not in a hundred years."
    mc "You help people. Even when you don't have to."
    scene e02s09-37 mh-asking-crazy-mc-admits-little-couples-handful_c1 with dissolve
    play voice3 lissa_moan3 noloop
    mh "Is it crazy that I'm already missing the couples?"
    play voice2 mc_arrogant_heh3 noloop
    mc "A little. They were kind of a handful."
    scene e02s09-38 mh-explains-what-felt-helping-couples-mc-smiles-agrees_c1 with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    mh "Not that part. I mean... It was so pure... just us working together to help people untangle their problems."
    mh "Reality can certainly hit hard when it wants to."
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah. But that's why we look for people to share it with."
    play sound dahlia_kiss_french1
    scene e02s09-39 mh-mc-kiss_c1 with dissolve
    pause
    play sound sfx_cloth_rustling2
    scene e02s09-40 mc-mh-chill-together_c1 with dissolve
    play voice3 lissa_ugu2 noloop
    mh "You are right. Not that you need to lighten my load or anything."
    mh "Soon, this will be over and I'll be back to my normal clients."
    play voice2 mc_happy_yay1 noloop
    mc "That's the spirit."

    jump e02s09_home_again

label e02s09_home_again:

    scene black
    $ renpy.music.set_volume(0.6, 3.0, "music" )
    show screen scene_transistion(_("One week later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.85, 6.0, "music" )
    scene e02s09-41 mc-brings-lunch-mh-she-tired_c1
    with Fade(0.5, 0.5, 0.5)
    pause
    mct "Each day since then, things have been a little hectic."
    scene e02s09-42 mc-mh-hug-each-other_c1 with Fade(0.5, 0.5, 0.5)
    mct "Like she feared, Lyssa has to put her other cases on hold while she deals with the Silvercorp lawsuit."
    scene e02s09-43 mc-mh-lunch-restaurant_c1 with Fade(0.5, 0.5, 0.5)
    mct "Not being able to help her smaller profile clients is certainly having an impact on her."
    scene e02s09-44 mc-lost-thoughts-while-lunch_c1 with dissolve
    mct "If not for this lunch, we might have gone a whole week where we were only both awake and being with one another for a few hours."
    mct "I knew there would be late nights, but I guess I imagined it would all be sorted in a few days."
    scene e02s09-45 mh-puts-brave-face-laughs_c1 with dissolve
    mct "I hate Silvercorp for putting her through this. It's grinding her down."
    mct "Each time I see her, I can tell that the pressure each day is getting to her, even if she puts up a good front."
    scene e02s09-46 mc-leaves-lunch-back-to-work_c1 with dissolve
    mct "It will be alright, Lyssa. I know you'll come out on top of this..."

    scene black
    show screen scene_transistion(_("Two weeks later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.4, 3.0, "music" )
    play sound sfx_door_open5
    scene e02s09-47 later-bedroom-mh-enters-mc-chilling-bed_c1
    with Fade(0.5, 0.5, 0.5)
    pause
    scene e02s09-48 mc-mh-hello-each-other_c1 with dissolve
    play voice3 nora_hey noloop
    mh "Hey sexy."
    play voice2 d2s9_mchey noloop volume 1.4
    mc "Hey gorgeous."
    scene e02s09-49 mh-undress_c1 with dissolve
    pause
    play sound sfx_cloth_rustling4
    scene e02s09-50 mh-waited-all-day-climbs-bed_c1 with dissolve
    play voice3 lissa_moan2 noloop
    mh "I have been thinking of you all day."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh really?"
    mh "Y-yes..."
    scene e02s09-a51 mh-hesitant-mc-thinks-not-sounding-like-mh-glambot-51-00_i with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mct "That sounded a little off for Lyssa."
    play sound sfx_camera_fly1
    scene e02s09-a51-glambot-1
    pause
    mc "Everything alright with the case?"
    stop sound fadeout 1.0
    scene e02s09-52 mc-asking-everything-okay-mh-dont-want-atalk-about-that_c1 with dissolve
    play voice3 dahlia_thinking_oh noloop
    mh "Oh yes. But I don't want to talk about that.{w} I just want you to rock my world."
    play voice2 mc_yes_okay2 noloop
    mc "Okay..."
    play sound maria_kiss2
    scene e02s09-53 mh-mc-kiss_c1 with dissolve
    play voice3 lissa_mmm2 noloop
    mh "Mmmm..."
    scene e02s09-54 mc-surprised-mh-feels-embarrassed_c1 with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Lyssa?"
    play voice3 lissa_oh noloop
    mh "Oh."
    mh "Well {i}this{/i} is embarrassing."
    mc "It's fine."
    mct "We all get a little limp dick now and then."
    play sound sfx_cloth_rustling5
    scene e02s09-55 mc-lays-mh-down-wants-speak-him-she-sniffs_c1 with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "Talk to me."
    play voice3 dahlia_pain_sobs noloop
    mh "*Sniffs*"
    scene e02s09-56 mh-explains-mc-just-cuddle-tonight_c1 with dissolve
    play voice3 allison_pain_sniff1 noloop
    mh "I don't know what's wrong with me."
    play voice2 mc_no_no5 noloop
    mc "Nothing is wrong with you. We can just cuddle tonight."
    scene e02s09-57 mh-tells-mc-been-patient-mc-not-about-change_c1 with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    mh "But you've been so patient with me."
    play voice2 mc_yes_yeah4 noloop
    mc "And that's not about to change."
    play sound sfx_cloth_rustling1
    scene e02s09-58 mc-cuddled-up-talks-about-judge_c1 with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    mh "The judge overseeing the case did not throw it out."
    play voice2 mc_pain_mff1 noloop
    mct "Fuck."
    scene e02s09-59 mc-going-to-trial-mh-confirms_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "So...{w} It's going to trial."
    play voice3 dahlia_thinking_mmm2 noloop
    mh "Yes..."
    mc "Forget about it. For tonight, it's all about just you and me."
    scene e02s09-58 mc-cuddled-up-talks-about-judge_c1 with dissolve
    play voice3 dahlia_angry_hm1 noloop
    mh "I should have fought harder, there must have been something I missed."
    play voice2 mc_thinking_mmm4 noloop
    mc "It will be alright."
    play sound maria_kiss3
    scene e02s09-60 mc-kiss-mh-forehead-tonight-all-about-them_c1 with dissolve
    pause
    play voice3 girl8_disappointed_snoring fadein 2.0
    scene e02s09-61 mc-calls-mh-she-already-asleep_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Lyssa?"
    scene e02s09-63 mc-thinking-while-mh-sleeps_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "It's good that she'll get a full night's rest anyhow."
    mct "Even superheroes need to rest in their battle against the villain."
    mct "Maybe that's what commercials are for."
    $ unlock_gallery_slot("cg", "e02s09")
    play sound maria_kiss1
    scene e02s09-64 mc-mh-sleep-cuddled_c1 with dissolve
    pause
    stop voice3 fadeout 2.0

    jump e02s09_next_morning

label e02s09_next_morning:

    scene black
    show screen scene_transistion(_("The next morning"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.2, 3.0, "music" )
    $ renpy.music.set_volume(0.05, 0.0, "sound2" )
    play sound2 park fadein 1.0
    scene e02s09-65 next-morning-mc-checking-phone-drinking-coffee-ask-mh-has-everything_c1
    with Fade(0.5, 0.5, 0.5)
    play voice2 mc_arrogant_huh1 noloop
    mc "Got everything?"
    scene e02s09-66 mh-confirms-has-transcripts_c1 with dissolve
    play voice3 lissa_aga noloop
    mh "Yes. I've got the transcript analysis all ready to go."
    play sound maria_kiss1
    scene e02s09-67 mh-kiss-mc-cheek_c1 with dissolve
    pause
    scene e02s09-68 mh-ask-see-mc-lunch-he-cant-make-today_c1 with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    mh "I'll see you at lunch?"
    play voice2 mc_no_no2 noloop
    mc "Not today."
    scene e02s09-69 mh-surprised_c1 with dissolve
    play voice3 lissa_oh2 noloop
    mh "Oh?{w} What are you up to?"
    scene e02s09-70 mc-grins-mh-dont-like-surprises-mc-promises_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "You'll see. I had an idea last night."
    play voice3 dahlia_disappointed_ehh3 noloop
    mh "I don't like surprises."
    mc "I promise, if you don't like this one, you can punish me for a week."
    mh "Mmm. Deal."
    play sound sfx_heels_steps1
    scene e02s09-71 mh-deal-leaves-work_c1 with dissolve
    pause
    stop sound fadeout 3.0
    scene e02s09-72 mc-alone-kitchen-looks-at-phone-time-get-work-done_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "Alright. Time for me to do a bit of work myself."
    mct "Let's see if all those business classes were worth a damn."
    stop sound2 fadeout 3.0

    stop music fadeout 3.0
    jump e02s10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
