image e07s03-a129-1 = Movie(play = "images/E-07/s03/anim/e07s03-a129-1-2x-50fps.webm", start_image = "e07s03-a129-1 first-facefuck-anim-01")
image e07s03-a129-1-f = Movie(play = "images/E-07/s03/anim/e07s03-a129-1-2x-60fps.webm", start_image = "e07s03-a129-1 first-facefuck-anim-01")
image e07s03-a129-2 = Movie(play = "images/E-07/s03/anim/e07s03-a129-2-2x-50fps.webm", start_image = "e07s03-a129-2 first-facefuck-anim-01")
image e07s03-a129-2-f = Movie(play = "images/E-07/s03/anim/e07s03-a129-2-2x-60fps.webm", start_image = "e07s03-a129-2 first-facefuck-anim-01")
image e07s03-a129-3 = Movie(play = "images/E-07/s03/anim/e07s03-a129-3-2x-50fps.webm", start_image = "e07s03-a129-3 first-facefuck-anim-01")
image e07s03-a129-3-f = Movie(play = "images/E-07/s03/anim/e07s03-a129-3-2x-60fps.webm", start_image = "e07s03-a129-3 first-facefuck-anim-01")
image e07s03-a129-4 = Movie(play = "images/E-07/s03/anim/e07s03-a129-4-2x-50fps.webm", start_image = "e07s03-a129-4 first-facefuck-anim-01")
image e07s03-a129-4-f = Movie(play = "images/E-07/s03/anim/e07s03-a129-4-2x-60fps.webm", start_image = "e07s03-a129-4 first-facefuck-anim-01")
image e07s03-a129-5 = Movie(play = "images/E-07/s03/anim/e07s03-a129-5-2x-50fps.webm", start_image = "e07s03-a129-5 first-facefuck-anim-01")
image e07s03-a129-5-f = Movie(play = "images/E-07/s03/anim/e07s03-a129-5-2x-60fps.webm", start_image = "e07s03-a129-5 first-facefuck-anim-01")
image e07s03-a129-6 = Movie(play = "images/E-07/s03/anim/e07s03-a129-6-2x-50fps.webm", start_image = "e07s03-a129-6 first-facefuck-anim-01")
image e07s03-a129-6-f = Movie(play = "images/E-07/s03/anim/e07s03-a129-6-2x-60fps.webm", start_image = "e07s03-a129-6 first-facefuck-anim-01")

image e07s03-a215-1 = Movie(play = "images/E-07/s03/anim/e07s03-a215-1-2x-50fps.webm", start_image = "e07s03-a215-1 arj-gb-pb-anim-01")
image e07s03-a215-1-f = Movie(play = "images/E-07/s03/anim/e07s03-a215-1-2x-60fps.webm", start_image = "e07s03-a215-1 arj-gb-pb-anim-01")
image e07s03-a215-2 = Movie(play = "images/E-07/s03/anim/e07s03-a215-2-2x-50fps.webm", start_image = "e07s03-a215-2 arj-gb-pb-anim-01")
image e07s03-a215-2-f = Movie(play = "images/E-07/s03/anim/e07s03-a215-2-2x-60fps.webm", start_image = "e07s03-a215-2 arj-gb-pb-anim-01")
image e07s03-a215-3 = Movie(play = "images/E-07/s03/anim/e07s03-a215-3-2x-50fps.webm", start_image = "e07s03-a215-3 arj-gb-pb-anim-01")
image e07s03-a215-3-f = Movie(play = "images/E-07/s03/anim/e07s03-a215-3-2x-60fps.webm", start_image = "e07s03-a215-3 arj-gb-pb-anim-01")
image e07s03-a215-4 = Movie(play = "images/E-07/s03/anim/e07s03-a215-4-2x-50fps.webm", start_image = "e07s03-a215-4 arj-gb-pb-anim-01")
image e07s03-a215-4-f = Movie(play = "images/E-07/s03/anim/e07s03-a215-4-2x-60fps.webm", start_image = "e07s03-a215-4 arj-gb-pb-anim-01")

label e07s03:

    $ e07s03_excited = False
    $ e07s03_give_all = False

    play sound2 sfx_plane_takeoff noloop
    scene black
    show screen scene_transistion(_("After a long flight"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    stop sound2 fadeout 3.0
    scene e07s03-01-they-enter-the-club
    with Fade(0.5, 0.5, 0.5)
    play music music_devet_ocasu
    pause
label replay_e07s03 hide:
    if _in_replay:
        $ renpy.music.set_volume(0.6, 0.0, "music")
        play music music_devet_ocasu
    scene e07s03-02-mc-talk with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "So this is the place?"
    scene e07s03-03-lc-talk-mc with dissolve
    play voice3 dahlia_yes_ugu noloop
    lc "Yes. The Devet Ocasu. The best bondage spot in all of Europe."
    scene e07s03-04-arj-exp with dissolve
    pause
    scene e07s03-05-lc-talk with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    lc "Keep moving."
    scene e07s03-06-gb-chair with dissolve
    pause
    scene e07s03-07-gb-notice-lc with dissolve
    pause
    scene e07s03-08-gb-talk-lc with dissolve
    play voice4 girl24_arrogant_huh1 noloop
    gb "Welcome to my dungeon, Lydia."
    play sound sfx_heels_steps1
    scene e07s03-09-lc-bow with dissolve
    stop sound fadeout 1.0
    pause
    scene e07s03-10-lc-talk-gb with dissolve
    play voice3 lydia_lydiahey noloop
    lc "Thanks for having us. Should I call you Domina Gizela?"
    scene e07s03-11-gb-talk-lc with dissolve
    play voice4 girl24_no_nah noloop
    gb "Gizela will be fine. You're my guest, not my servant, after all."
    scene e07s03-12-gb-talk with dissolve
    play voice4 girl24_thinking_hmm6 noloop
    gb "Mrmmm."
    play sound sfx_cloth_rustling2
    scene e07s03-13-gb-talk-lc with dissolve
    play voice4 girl24_arrogant_hah noloop
    gb "These must be your charges."
    scene e07s03-14-lc-talk-gb with dissolve
    play voice3 dahlia_yes_simple noloop
    lc "Yes. This one has been mine for a while. Very strong and dutiful, but dreadfully boring."
    scene e07s03-15-gb-talk-lc with dissolve
    play voice4 girl24_thinking_huh1 noloop
    gb "Perhaps an evening with us will give him new inspiration. Perhaps you'll receive some yourself."
    scene e07s03-16-lc-talk-gb with dissolve
    play voice3 dahlia_thinking_oh noloop
    lc "Now he... is my pride and joy. He's been obsessed with me since the moment he laid eyes on me."
    scene e07s03-17-gb-talk-lc with dissolve
    play voice4 girl24_thinking_emm2 noloop
    gb "And this one?"
    scene e07s03-18-lc-talk-gb with dissolve
    play voice3 dahlia_arrogant_ha noloop
    lc "They were kind of a package deal. But, she's proven to be quite the good pussy licker when properly motivated."
    scene e07s03-19-lc-talk with dissolve
    play voice3 dahlia_hey_active1 noloop
    lc "Slaves, why are you not bowing?"
    scene e07s03-20-lc-talk with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    lc "This woman is Domina Gizela. Mistress, Empress, Pani Sefova of this Castle."
    play sound sfx_cloth_dress_off1 volume 1.6
    scene e07s03-21-bow with dissolve
    pause
    scene e07s03-22-lc-talk with dissolve
    play voice3 dahlia_happy_yeah noloop
    lc "That's more like it."
    scene e07s03-23-gb-talk-lc with dissolve
    play voice4 girl24_arrogant_huh2 noloop
    gb "He is an impressive physical specimen. But his eyes tell me that he is a tool."
    scene e07s03-24-gb-talk with dissolve
    play voice4 girl24_arrogant_yeah1 noloop
    gb "Useful for certain problems. Incompatible for others."
    scene e07s03-25-lc-talk-gb with dissolve
    play voice3 dahlia_surprised_wow noloop
    lc "Woah. You can tell that all just by his eyes?"
    scene e07s03-26-gb-talk-lc with dissolve
    play voice4 girl24_yes_aga noloop
    gb "His eyes and other things. But... I shall not judge your slaves too harshly."
    scene e07s03-27-gb-talk with dissolve
    play voice4 girl24_thinking_hmm1 noloop
    gb "They've had a long trip after all."
    scene e07s03-28-gb-talk-zh with dissolve
    play voice4 girl24_angry_cough2 noloop
    gb "A {i}chair{/i} for our guest."
    play sound sfx_cloth_rustling1
    scene e07s03-29-slave-chair with dissolve
    pause
    scene e07s03-30-arj-talk with dissolve
    play voice5 amrose_happy_mmm noloop
    arj "Urmmmm."
    scene e07s03-31-mc-talk-arj with dissolve
    play voice2 d2s9_mchey noloop
    mc "What's wrong?"
    scene e07s03-32-arj-talk-mc with dissolve
    play voice5 amrose_no_long noloop
    arj "Nothing.{w} Okay, I am just a little concerned about being here, in a foreign country."
    scene e07s03-33-arj-talk-mc with dissolve
    play voice5 amrose_disappointed_ehh2 noloop
    arj "Under her command."
    scene e07s03-34-mc-talk-arj with dissolve
    play voice2 mc_happy_a1 noloop
    mc "[e07_lcname!t] would never do anything to really hurt us, AmRose. She loves us too much."
    scene e07s03-35-pb-talk-mc with dissolve
    play voice6 pete_disappointed_mmf1 noloop
    pb "You really must be something special, [mcname]. [e07_lcname!t] never took me on a trip before."
    scene e07s03-36-mc-talk-pb with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "Really. That's pretty cool."
    scene e07s03-37-lc-talk with dissolve
    play voice3 dahlia_angry_argh2 noloop
    lc "Why are my dogs making noise without permission?"
    scene e07s03-38-lc-talk-mc with dissolve
    play voice3 dahlia_angry_hm2 noloop
    lc "Tell me, [e07_mcname!t], what is all the noise about?"
    scene e07s03-39-mc-talk-lc with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Nothing, [e07_lcname!t]."
    scene e07s03-40-lc-talk-arj with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    lc "Good. [e07_arjname!t], come here."
    scene e07s03-41-lc-whisper-arj with dissolve
    play voice3 amrose_old_psst noloop
    pause
    scene e07s03-42-mc-inner-talk with dissolve
    play voice2 d1s5_mcthinks noloop
    mct "What is [e07_lcname!t] up to?"
    play sound sfx_paper_rustl1
    scene e07s03-43-arj-talk with dissolve
    play voice5 amrose_thinking_emm noloop
    arj "Uh... Hello."
    scene e07s03-44-lc-talk-arj with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    lc "Come now, you can do better than that."
    scene e07s03-45-arj-sigh with dissolve
    play voice5 amrose_angry_breath1 noloop
    arj "*sigh*"
    scene e07s03-46-arj-talk with dissolve
    play voice5 amrose_hey_active2 noloop
    arj "Greetings, fellow deviants. Tonight we have a special event for all those who find pleasure in the art of submission."
    arj "My Mistress Lydia has brought me and her other slaves across the sea and wishes to share a wonderful performance with you."
    scene e07s03-47-arj-talk with dissolve
    play voice5 amrose_happy_yeah1 noloop
    arj "These two males will prove that they are no better than dogs. Only suited to service the pleasure of their betters."
    arj "One of you will pleasure Domina Gizela, and one of you will pleasure [e07_lcname!t]."
    arj "Whoever makes their partner orgasm first will be rewarded. And whoever fails... will be punished."
    menu:
        "Fearful about the competition"(hint="e07s03m01c01"):
            $ e07s03_excited = False
            scene e07s03-48-c1-mc-inner-talk with dissolve
            play voice2 mc_pain_rrrr noloop
            mct "I can't believe [e07_lcname!t] brought us all the way here just so other people could watch me fail."
            mct "This is bad... but I have to focus. I can beat Pete. I have to beat Pete."
        "Excited to prove yourself"(hint="e07s03m01c02"):

            $ e07s03_excited = True
            scene e07s03-49-c2-mc-inner-talk with dissolve
            play voice2 mc_thinking_mmm1 noloop
            mct "Yes. This sounds great. I can't wait to show [e07_lcname!t] how good I can make her feel."
            mct "Pete will be the one to face punishment. My love will see that I am the superior servant."

    jump e07s03_after_choice

label e07s03_after_choice:

    scene e07s03-50-gb-talk-lc with dissolve
    play voice4 girl24_disappointed_oof noloop
    gb "How delightfully wicked. Make your choice."
    scene e07s03-51-lc-talk-gb with dissolve
    play voice3 dahlia_no_nonono noloop
    lc "No please, Domina. This is your kingdom, and I am just your guest."
    scene e07s03-52-lc-talk-gb with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    lc "Please take the first pick between my slaves."
    scene e07s03-53-gb-talk-lc with dissolve
    play voice4 girl24_thinking_hmm3 noloop
    gb "Very well..."
    scene e07s03-54-gb-look-pb-mc with dissolve
    gb "Hmmmm."
    scene e07s03-55-gb-talk-lc with dissolve
    play voice4 girl24_yes_ugu noloop
    gb "That one. This is the new one correct?"
    scene e07s03-56-lc-talk-gb with dissolve
    play voice3 lydia_lydyes noloop
    lc "Yes. I call it [e07_mcname!t]."
    scene e07s03-57-gb-talk-mc with dissolve
    play voice4 girl24_happy_laugh1 noloop
    gb "How fitting. How about it, you little pest? Do you have what it takes to make me climax before your Mistress does?"
    play sound sfx_hands_clap2 volume 0.3
    scene e07s03-58-gb-mc-chin with dissolve
    pause
    scene e07s03-59-lc-look-gb with dissolve
    pause
    scene e07s03-60-gb-talk-mc with dissolve
    play voice4 girl24_arrogant_hm1 noloop
    gb "Look at me when I'm talking to you."
    scene e07s03-61-gb-talk-lc with dissolve
    play voice4 girl24_thinking_mff noloop
    gb "Hmmmph. Still a little disobedient."
    scene e07s03-62-lc-talk-gb with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    lc "He is... still adjusting. But, if [e07_mcname!t] is who you want, he will serve you well."
    scene e07s03-63-lc-talk-mc with dissolve
    play voice3 dahlia_arrogant_yeah noloop
    lc "Won't you, my pet? You know what will happen to you if you fail to impress tonight."
    scene e07s03-64-lc-talk-mc with dissolve
    play voice3 dahlia_disgust_oof noloop
    lc "You'll embarrass us both here, in front of all our new friends."
    lc "But that is nothing compared to what will happen to you back home."
    scene e07s03-65-mc-nods with dissolve
    pause
    scene e07s03-66-mc-talk-lc with dissolve
    play voice2 d9s2_mcyes2 noloop volume 2.5
    mc "Yes, [e07_lcname!t]. I will do whatever is asked of me."
    scene e07s03-67-gb-talk-lc with dissolve
    play voice4 girl24_thinking_hmm4 noloop
    gb "Hmmph. I will take him then. But I'll make sure he is well equipped to service me."
    scene e07s03-68-lc-talk-gb with dissolve
    play voice3 dahlia_yes_aga noloop
    lc "Perfect. Please allow me a moment with him."
    play sound sfx_heels_steps1
    scene e07s03-69-gb-talk-lc with dissolve
    play voice4 girl24_yes_simple1 noloop
    gb "Don't make me wait too long."
    stop sound fadeout 1.0
    scene e07s03-70-lc-talk-mc with dissolve
    play voice3 dahlia_arrogant_heh noloop
    lc "I hope you're well prepared, [e07_mcname!t]."
    scene e07s03-71-mc-talk-lc with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "I don't think anyone could be prepared for this."
    scene e07s03-72-mc-talk-lc with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "But I'll try my best, [e07_lcname!t]. For you."
    scene e07s03-73-lc-talk-mc with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    lc "Good, you'll want to get off to a good start."
    scene e07s03-74-mc-talk-lc with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "A good start?"
    scene e07s03-75-lc-talk-mc with dissolve
    play voice3 dahlia_surprised_oh noloop
    lc "Didn't I tell you? Oh, how clumsy of me."
    scene e07s03-76-lc-talk-mc with dissolve
    play voice3 dahlia_happy_laugh3 noloop
    lc "This little competition is merely the first of many I have planned for you."
    scene e07s03-77-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mct "[e07_lcname!t] certainly likes her games. Fetish Locator, and now this."
    scene e07s03-78-mc-talk-lc with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "I'm a little worried. I'll do my best, but that was a long flight."
    scene e07s03-79-lc-talk-mc with dissolve
    play voice3 dahlia_yes_yeah4 noloop
    lc "Come now, [e07_mcname!t]. I have faith in your abilities."
    scene e07s03-80-lc-talk-mc with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    lc "I know you will do your best. But, I've gabbed enough, it's time for action."
    scene e07s03-81-mc-talk-lc with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "[e07_lcname!t]. Wait..."
    scene e07s03-82-lc-talk-mc with dissolve
    play voice3 dahlia_yes_questioning noloop
    lc "Yes?"
    scene e07s03-83-mc-talk-lc with dissolve
    play voice2 d1s5_mchappy noloop
    mc "What is the prize we're competing for?"
    scene e07s03-84-lc-talk-mc with dissolve
    play voice3 dahlia_surprised_huh1 noloop
    lc "I thought that would be obvious."
    scene e07s03-85-lc-talk-mc with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    lc "At the end of the contests, the best man will get the honor of breeding me."
    scene e07s03-86-mc-speechless with dissolve
    play voice2 d3s7_mcemm noloop
    mc "..."
    scene e07s03-87-lc-talk-mc with dissolve
    play voice3 dahlia_happy_laugh4 noloop
    lc "Calm yourself. You haven't won anything yet."
    lc "If there is a winner, there must be a loser."
    scene e07s03-88-mc-talk-lc with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "And what happens to the loser?"
    scene e07s03-89-lc-talk-mc with dissolve
    play voice3 dahlia_disgust_oeah noloop
    lc "The loser will be vasectomized. I have no need for worthless balls, after all."
    scene e07s03-90-lc-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    lc "I'm sure that will give you adequate motivation for tonight, and all the challenges ahead of you."
    scene e07s03-91-mc-talk-lc with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "You could say that."
    scene e07s03-92-lc-talk-mc with dissolve
    play voice3 lydia_aga noloop
    lc "Good. Now run along. Gizela is waiting."

    jump e07s03_contest_start

label e07s03_contest_start:

    scene e07s03-93-mc-stand with dissolve
    pause
    scene e07s03-94-gb-look-mc with dissolve
    pause
    scene e07s03-95-gb-talk-zh with dissolve
    play voice4 girl24_hey_angry noloop
    gb "Servant, bring me two face-dildos."
    scene e07s03-96-zh-talk-gb with dissolve
    play voice5 girl28_yes_simple noloop
    "Servant" "Yes Domina. Regular size?"
    scene e07s03-97-gb-talk-zh with dissolve
    play voice4 girl24_yes_calm noloop
    gb "Yes."
    scene e07s03-98-gb-talk-zh with dissolve
    play voice4 girl24_no_simple1 noloop
    gb "No."
    scene e07s03-99-gb-talk-zh with dissolve
    play voice4 girl24_arrogant_hm3 noloop
    gb "Extra large. I don't want to take the chance these pitiful men cannot bring my guest and I to a state of bliss."
    scene e07s03-100-zh-talk-gb with dissolve
    play voice5 girl28_yes_yeah1 noloop
    "Servant" "Right away, Domina."
    play sound sfx_cloth_rustling2
    scene e07s03-101-zh-with-face-dildo with dissolve
    pause
    if e07s03_excited is True:
        scene e07s03-102-c1-mc-inner-talk with dissolve
        play voice2 mc_thinking_hmm5 noloop
        mct "Well, this will be new."
        mct "I'd prefer fucking [e07_lcname!t] the old-fashioned way. Still, this will give me a chance to put on a good show for her."
        scene e07s03-103-c1-mc-inner-talk with dissolve
        play voice2 d3s11b_mcheh noloop volume 1.6
        mct "Maybe she'll let me fuck her after I'm done making Gizela cum."
    else:
        scene e07s03-104-c2-mc-look-zh with dissolve
        pause
        scene e07s03-105-c2-mc-inner-talk with dissolve
        play voice2 mc_pain_mff1 noloop
        mct "Oh my god. Why is [e07_lcname!t] making me pleasure another woman and not her?"
        mct "And with {b}that{/b}?"
        scene e07s03-106-c2-mc-talk-gb with dissolve
        play voice2 d1s5b_emmm noloop
        mc "Can't we just use our mouths and tongues?"
        scene e07s03-107-c2-gb-talk-mc with dissolve
        play voice4 girl24_arrogant_kgh1 noloop
        gb "Hah. Your pet seems hesitant. Unlike your bull."
        scene e07s03-108-c2-lc-talk-mc with dissolve
        play voice3 dahlia_angry_oh noloop
        lc "I don't recall asking you about your feelings on this matter, [e07_mcname!t]."
        scene e07s03-109-c2-mc-talk-lc with dissolve
        play voice2 mc_thinking_mmm5 noloop
        mc "Fine, I just... I guess this wasn't what I was expecting."
        scene e07s03-110-c2-lc-talk-mc with dissolve
        play voice3 dahlia_angry_argh1 noloop
        lc "Then hurry up and adapt, [e07_mcname!t]. I don't want to see any lack of effort from you."
        scene e07s03-111-c2-mc-talk-lc with dissolve
        play voice2 mc_yes_yes2 noloop
        mc "Yes, [e07_lcname!t]."
    play sound sfx_sextoy_uncuff1
    scene e07s03-112-mc-pb-dick with dissolve
    pause
    scene e07s03-113-pb-talk-mc with dissolve
    play voice5 pete_undermask_hey noloop
    pb "Hey, Dumbo."
    scene e07s03-114-mc-talk-pb with dissolve
    play voice2 mc_undermask_hey noloop
    mc "Hello, Horton."
    scene e07s03-115-gb-talk-arj with dissolve
    play voice4 girl24_arrogant_hm4 noloop
    gb "As you were, slave."
    scene e07s03-116-arj-talk-mc with dissolve
    play voice5 amrose_arrogant_huh3 noloop
    arj "[mcname], take your position between Lady Gizela's legs."
    scene e07s03-117-arj-talk-pb with dissolve
    play voice5 amrose_thinking_hmm1 noloop
    arj "Pete, get on your knees in front of our [e07_lcname!t]."
    scene e07s03-118-gb-talk-mc with dissolve
    play voice4 girl24_disappointed_ohh1 noloop
    gb "Don't disappoint your [e07_lcname!t]. Of course, since this is my house, you better not disappoint me either."
    scene e07s03-119-mc-talk-gb with dissolve
    play voice2 mc_undermask_yes noloop
    mc "Yes..."


    $ Lovense.stop()

    scene e07s03-120-mc-inner-talk with dissolve
    play voice2 mc_undermask_mmm noloop
    mct "This should be interesting."
    $ Lovense.vibrate(3)
    play voice2 mc_undermask_mff4 noloop
    play sound sfx_whip_slap1
    scene e07s03-121-gb-whip-mc with vpunch
    pause
    scene e07s03-122-mc-talk with dissolve
    play voice2 mc_undermask_orgasm2 noloop
    mc "Nrrraah!"
    scene e07s03-123-gb-talk-mc with dissolve
    play voice4 girl24_angry_argh1 noloop
    gb "How dare you! You were just going to slide in like you were sliding into my DMs?"
    scene e07s03-124-mc-talk-gb with dissolve
    play voice2 mc_undermask_orgasm noloop
    mc "Nrrrffff."
    scene e07s03-125-gb-talk-mc with dissolve
    play voice4 girl24_happy_laugh2 noloop
    gb "Haha. Excuse me. I forgot that you cannot ask for permission as you are."
    gb "You now have my permission."
    scene e07s03-126-gb-talk-mc with dissolve
    play voice4 girl24_hey_sexy noloop
    gb "Show me your hidden value, [e07_mcname!t]."
    scene e07s03-127-mc-inner-talk with dissolve
    mct "I'll show you where to stick that stick if you keep hitting me."
    scene e07s03-128-mc-gb-position with dissolve
    pause
    scene e07s03-a129-1 first-facefuck-anim-01 with dissolve
    pause
    play voice2 mc_undermask_breathing
    play voice4 girl24_sex_openmoans1
    play voice3 dahlia_sex_openmoans2
    play voice5 pete_undermask_breathing
    play sound2 sfx_vagina_penetration1_fast
    $ Lovense.pattern("5;8", 1400)
    scene e07s03-a129-1
    gb "*lightly sighs*"
    mc "*grunting*"
    pause
    scene e07s03-a129-2 with dissolve
    pause
    scene e07s03-a129-3 with dissolve
    pause
    scene e07s03-a129-4 with dissolve
    pause
    scene e07s03-a129-5 with dissolve
    pause
    scene e07s03-a129-6 with dissolve
    pause
    scene e07s03-133-gb-talk-mc with dissolve
    gb "Come on. Put your back into it."
    scene e07s03-134-lc-moaning with dissolve
    lc "*moaning*"
    scene e07s03-135-mc-talk with dissolve
    mct "This is easy. I just have to build up my pace."
    scene e07s03-136-mc-inner-talk with dissolve
    mct "But fuck, this is harder than it looks."
    scene e07s03-137-gb-talk-mc with dissolve
    gb "There you go. *moans* If your [e07_lcname!t] gets tired of you, I might have to take you."
    scene e07s03-138-gb-talk-mc with dissolve
    gb "Would you like that, my little peasant pig?"
    $ Lovense.pattern("6;10", 700)
    scene e07s03-a129-1-f with dissolve
    mc "*grunting*"
    pause
    scene e07s03-a129-2-f with dissolve
    pause
    scene e07s03-a129-3-f with dissolve
    pause
    scene e07s03-a129-4-f with dissolve
    pause
    scene e07s03-a129-5-f with dissolve
    pause
    scene e07s03-a129-6-f with dissolve
    pause
    scene e07s03-139-lc-talk with dissolve
    play voice3 dahlia_sex_openmoans1
    lc "Urhuah... hurrah... yes. Faster... Stronger!"
    scene e07s03-140-mc-inner-talk with dissolve
    mct "[e07_lcname!t]. Pete's already gotten her to moan more than Gizela is."
    mct "This is bad. Maybe I should punch it up, go for broke."
    scene e07s03-141-mc-inner-talk with dissolve
    mct "Or maybe Pete is going to wear himself out, and I can just keep going steady."
    play sound sfx_whip_slap1
    $ Lovense.stop()
    $ Lovense.vibrate(14)
    scene e07s03-121-gb-whip-mc with vpunch
    pause
    scene e07s03-143-mc-talk with dissolve
    $ Lovense.vibrate(5)
    play voice2 mc_undermask_orgasm2 noloop
    mc "Rnnghn..."
    scene e07s03-144-mc-inner-talk with dissolve
    mct "That was the other cheek now! Fuck me."
    scene e07s03-145-gb-talk-mc with dissolve
    play voice4 girl24_angry_err1 noloop
    gb "If you keep looking over there I'm going to start feeling jealous."
    scene e07s03-146-gb-talk-mc with dissolve
    play voice4 girl24_disappointed_eeh2 noloop
    gb "And you won't like me when I'm jealous..."
    scene e07s03-147-mc-inner-talk with dissolve
    mc "Mhmmmpff."
    mct "Okay, I can't fuck around anymore. I can't lose."
    menu:
        "Slow and steady"(hint="e07s03m02c01"):
            $ e07s03_give_all = False
            jump e07s03_slow_steady
        "Give it your all!"(hint="e07s03m02c02"):

            $ e07s03_give_all = True
            $ e07_mc_wins += 1
            jump e07s03_give_all

label e07s03_slow_steady:

    scene e07s03-148-c1-mc-inner-talk with dissolve
    play voice2 mc_undermask_hehe noloop
    mct "It will be better to stay restrained. Pete's been failing [e07_lcname!t]."
    mct "I'm sure he'll get her close, and then peter out before he makes her cum."
    play voice2 mc_undermask_breathing
    play voice4 girl24_sex_openmoans1
    mc "Mrrfff... Mrrmmff..."
    scene e07s03-149-c1-lc-talk-gb with dissolve
    $ Lovense.pattern("5;8", 1400)
    gb "Mmmm."
    lc "Oouhaah... These devices are perfect. I might have to steal them for home."
    scene e07s03-150-c1-gb-talk-lc with dissolve
    gb "*moaning lightly* Mmm. Wars have been fought over less, Lady Lydia."
    gb "Hmmm."
    scene e07s03-151-c1-lc-talk-gb with dissolve
    lc "What is- *moans* what is the problem?"
    scene e07s03-152-c1-gb-talk-lc with dissolve
    gb "Nothing. Just keep enjoying yourself."
    scene e07s03-153-c1-lc-talk with dissolve
    $ Lovense.stop()
    $ Lovense.vibrate(14)
    play voice3 dahlia_sex_orgasming1
    lc "Very welluuaah... that's it. Use those neck muscles, you beast!"
    lc "*panting and moaning*"
    stop voice5 fadeout 1.0
    scene e07s03-154-c1-lc-talk-pb with dissolve
    play voice3 dahlia_happy_phew noloop
    lc "Good work, my sweet dumb bull."
    scene e07s03-155-c1-pb-talk-lc with dissolve
    $ Lovense.vibrate(3)
    play voice5 pete_undermask_ugu noloop
    pb "Mrrmm."
    scene e07s03-156-c1-lc-talk with dissolve
    play voice3 dahlia_surprised_ah2 noloop
    lc "And how..."
    scene e07s03-157-c1-lc-talk-gb with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    lc "You're barely moaning at all, Gizela."
    scene e07s03-158-c1-gb-talk-lc with dissolve
    play voice4 girl24_arrogant_yeah3 noloop
    gb "I moaned louder the first time I rode on horseback."
    scene e07s03-159-c1-gb-talk-lc with dissolve
    play voice4 girl24_happy_mmm noloop
    gb "But I didn't want to punish him without your permission."
    stop sound fadeout 1.0
    stop voice2 fadeout 1.0
    stop sound2 fadeout 1.0
    scene e07s03-160-c1-lc-talk-mc with dissolve
    play voice3 dahlia_surprised_what noloop
    lc "Why you..."
    play sound sfx_leg_kick8
    scene e07s03-161-c1-mc-look-lc with dissolve
    $ Lovense.vibrate(6)
    play voice2 mc_undermask_orgasm noloop
    mc "..."
    play sound sfx_kick_leg1
    scene e07s03-162-c1-mc-ground with dissolve
    pause
    play sound sfx_whip_slap3
    $ Lovense.vibrate(12)
    scene e07s03-163-c1-lc-whips-mc with vpunch
    "*CRACK!*"
    play voice2 mc_undermask_mff5 noloop
    mc "Mfftrssfff."
    play sound sfx_whip_slap4
    $ Lovense.vibrate(15)
    scene e07s03-164-c1-lc-whips-mc with vpunch
    play voice2 mc_undermask_argh1 noloop
    "*CRACK!"
    scene e07s03-165-c1-lc-talk-mc with dissolve
    $ Lovense.vibrate(3)
    play voice3 dahlia_angry_ah1 noloop
    lc "You weren't giving your all to Lady Gizela."
    play sound sfx_sextoy_uncuff1
    scene e07s03-166-c1-lc-dildo with dissolve
    pause
    play sound sfx_skirt_off2
    scene e07s03-167-c1-lc-talk-mc with dissolve
    play voice3 dahlia_angry_ah2 noloop
    lc "What do you have to say for yourself?"
    scene e07s03-168-c1-mc-talk-lc with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "I'm sorry."
    mc "I was... saving my strength. I thought it would be the best strategy."
    scene e07s03-169-c1-gb-talk-lc with dissolve
    play voice4 girl24_happy_laugh5 noloop
    gb "Hahaha. Seems like he is still thinking too much on his own."
    scene e07s03-170-c1-lc-talk-mc with dissolve
    play voice3 dahlia_yes_angry noloop
    lc "Yes. It appears I've been too lenient with my new pet."

    jump e07s03_continue

label e07s03_give_all:

    scene e07s03-171-mc-inner-talk with dissolve
    play voice2 mc_undermask_hehe noloop
    mct "I will not fail you, [e07_lcname!t]."
    scene e07s03-172-facefuck-anim-2 with dissolve
    $ Lovense.pattern("6;13", 700)
    play voice2 mc_undermask_breathing
    play voice4 girl24_sex_openmoans2
    pause
    scene e07s03-174-gb-surprised with dissolve
    gb "*surprised* Ooouha."
    scene e07s03-173-facefuck-anim-2 with dissolve
    mc "*grunting like a hog*"
    scene e07s03-175-gb-talk-mc with dissolve
    gb "You're certainly tenacious, I'll give you that."
    scene e07s03-176-gb-talk with dissolve
    play voice4 girl24_sex_openmoans4
    gb "Oouha... ahurah.. ooouhaha..."
    scene e07s03-177-gb-talk-mc with dissolve
    play voice4 girl24_sex_orgasm2
    gb "Keep going. Don't you dare stop. Keep going keep going keep goinuaaaah!"
    play voice5 pete_undermask_mmm4 noloop
    queue voice5 pete_undermask_breathing
    play sound sfx_whip_slap3
    $ Lovense.stop()
    $ Lovense.vibrate(14)
    scene e07s03-178-lc-whips-pb with vpunch
    pb "Niauffafffhh."
    play voice3 dahlia_sex_orgasming1
    scene e07s03-179-lc-talk-pb with dissolve
    lc "Come on. Come on. I'm so-"
    play voice4 girl24_sex_orgasm6 noloop
    stop voice2 fadeout 1.0
    play sound sfx_whip_slap4
    $ Lovense.vibrate(15)
    scene e07s03-180-gb-cums with vpunch
    pause
    scene e07s03-181-mc-inner-talk with dissolve
    $ Lovense.vibrate(3)
    play voice2 mc_undermask_wooh3 noloop
    mct "Holy fuck."
    scene e07s03-182-gb-talk-mc with dissolve
    play voice4 girl24_sex_closedmoan1 noloop
    gb "That will be enough. Mmrrmm... Dare I say, more than enough."
    scene e07s03-183-mc-talk with dissolve
    play voice2 mc_undermask_oof1 noloop
    mct "Phew."
    scene e07s03-184-gb-talk-mc with dissolve
    play voice4 girl24_surprised_ohmy2 noloop
    gb "You are definitely not the worst pet I've played with."
    scene e07s03-185-gb-talk-mc with dissolve
    play voice4 girl24_disgust_mmm noloop
    gb "I can only imagine what you'd be like using that little knob of yours."
    stop voice5 fadeout 1.0
    stop sound2 fadeout 1.0
    scene e07s03-186-lc-talk-pb with dissolve
    play voice3 dahlia_angry_argh1 noloop
    lc "AGrrrrrr."
    scene e07s03-187-zh-talk with dissolve
    play voice6 girl28_happy_woohoo2 noloop
    "Servant" "Winner. [e07_mcname!t]!"
    scene e07s03-188-gb-talk-lc with dissolve
    play voice4 girl24_thinking_emm1 noloop
    gb "He may not look like much, but your pup has spirit, Lydia."
    scene e07s03-189-gb-talk-lc with dissolve
    play voice4 girl24_thinking_hmm2 noloop
    gb "Sorry that your bull couldn't properly perform. Maybe it's time to put him out to pasture."
    scene e07s03-190-gb-laughs with dissolve
    play voice4 girl24_happy_laugh4 noloop
    gb "Ah-hah-ha-ha-hah."
    scene e07s03-191-lc-talks-gb with dissolve
    play voice3 dahlia_yes_angry noloop
    lc "Of course. I will keep your wisdom in mind."
    play voice3 dahlia_angry_hm2 noloop
    play voice5 pete_undermask_dagh4 noloop
    play sound sfx_whip_slap4
    scene e07s03-192-lc-whips-pb with vpunch
    pause
    scene e07s03-193-pb-talk with dissolve
    play voice5 pete_undermask_ouch3 noloop
    pb "Offhhuguddfff!"
    play sound sfx_cloth_rustling2
    scene e07s03-194-lc-talk-pb with dissolve
    play voice3 dahlia_disgust_meh noloop
    lc "Just be happy you have the rest of the night to wipe the stain of defeat off me, [e07_pbname!t]."

    jump e07s03_continue

label e07s03_continue:

    scene e07s03-195-gb-talk with dissolve
    play voice4 girl24_thinking_hmm5 noloop volume 1.5
    gb "Mmmm. Now it's time for a second course."
    scene e07s03-196-gb-talk-lc with dissolve
    play voice4 girl24_hey_simple noloop volume 1.5
    gb "I tried, [e07_mcname!t]. Allow me to try this bull of yours."
    scene e07s03-197-lc-talk-gb with dissolve
    play voice3 dahlia_yes_yeah1 noloop
    lc "As you wish."
    scene e07s03-198-gb-looks-arj with dissolve
    play voice4 girl24_thinking_mff noloop
    gb "Mmm."
    gb "I'll play with her too."
    scene e07s03-200-lc-talk-arj with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    lc "Do as she says, pet."
    scene e07s03-201-mc-looks-gb with dissolve
    pause
    scene e07s03-202-gb-talk-zh with dissolve
    play voice4 girl24_disgust_boeagh1 noloop
    gb "This one's nipples disgust me. Cover them up with some pincers and chain."
    scene e07s03-203-zh-talk-gb with dissolve
    play voice6 girl28_yes_confident noloop
    "Servant" "Yes, Domina."
    play sound sfx_powder_latch_closed
    scene e07s03-204-zh-clamps with dissolve
    pause
    scene e07s03-205-pb-talk with dissolve
    play voice5 pete_pain_ouch1 noloop
    pb "Yeouch!"
    scene e07s03-206-gb-talk-pb with dissolve
    play voice4 girl24_surprised_huh4 noloop
    gb "Such pain after just one? How dreadful. I hope your cock is at least stronger."
    play sound sfx_cloth_rustling4
    scene e07s03-207-gb-pb with dissolve
    pause
    scene e07s03-208-gb-talk with dissolve
    play voice4 girl24_sex_openmoans1
    play voice5 pete_sex_openmoans2
    play sound sfx_vagina_penetration1_fast volume 0.6 loop
    gb "Mrrrrm... nothing like a big, white cock in the evening."
    scene e07s03-209-gb-talk-arj with dissolve
    gb "Come closer my child."
    play sound2 sfx_sex_fingering_slow1 volume 0.4
    scene e07s03-210-gb-finger-arj with dissolve
    pause
    scene e07s03-211-gb-talk-arj with dissolve
    gb "Is this too much for you? Watching a powerful woman dominate this supposedly powerful male?"
    scene e07s03-212-arj-talk-gb with dissolve
    play voice6 amrose_no_questioning1
    queue voice6 daisy_moaning
    arj "No... I mean... no it's not too mu-huaah... too much."
    scene e07s03-213-gb-talk-arj with dissolve
    play voice4 girl24_hey_active noloop
    queue voice4 girl24_sex_openmoans1
    gb "Tsk tsk tsk. Your eyes should always be on me, girl. Unless I say otherwise."
    scene e07s03-214-arj-talk-gb with dissolve
    play voice6 jessie_yes1 noloop
    queue voice6 amrose_old_moaning
    arj "*moaning* Yes... Yes, Domina."
    scene e07s03-a215-1 arj-gb-pb-anim-01 with dissolve
    pause
    $ Lovense.pattern("7;10", 1400)
    scene e07s03-a215-1
    pause
    scene e07s03-a215-2 with dissolve
    pause
    scene e07s03-a215-3 with dissolve
    pause
    scene e07s03-a215-4 with dissolve
    pause
    scene e07s03-219-gb-talk-pb with dissolve
    play voice4 girl24_sex_openmoans4
    play voice5 pete_sex_openmoans1
    gb "Keep going, bull. Only when you've made me cum three times will it be time for your to rest."
    scene e07s03-220-pb-talk with dissolve
    play voice5 pete_yes_simple3 noloop
    queue voice5 pete_sex_openmoans2
    pb "*grunts and hisses* Y-yess..."
    $ Lovense.pattern("7;10", 700)
    scene e07s03-a215-1-f with dissolve
    pause
    scene e07s03-a215-2-f with dissolve
    pause
    scene e07s03-a215-3-f with dissolve
    pause
    scene e07s03-a215-4-f with dissolve
    pause
    scene e07s03-221-gb-talk-pb with dissolve
    gb "Are you already going limp on me? Disgraceful."
    scene e07s03-222-pb-talk-gb with dissolve
    play voice5 pete_no_simple2 noloop
    queue voice5 pete_sex_openmoans2
    pb "No, ma'am. I'm going... I've got it... Nrrrah."
    scene e07s03-223-gb-talk-arj with dissolve
    play voice4 girl24_sex_openmoans5
    gb "Good. Now maybe I can focus on our sweet redhead here."
    scene e07s03-224-arj-talk-gb with dissolve
    gb "Do you like that? Or do you still wish these fingers belonged to that stud over there?"
    scene e07s03-225-gb-talk-arj with dissolve
    play voice6 amrose_old_orgasming
    arj "I don't... know... I'm not. We're not... oh god."
    scene e07s03-226-arj-talk with dissolve
    gb "You can tell me. I'll keep it between us girls.."
    scene e07s03-227-arj-falls with dissolve
    arj "Wuauah... oh god... I'm cumming... I'm about to."
    stop sound2 fadeout 1.0
    scene e07s03-228-gb-finger-arj with dissolve
    play voice6 daisy_sucking
    gb "Come on. Lick them and suck them."
    scene e07s03-229-gb-talk-arj with dissolve
    play voice4 girl24_no_long noloop
    queue voice4 girl24_sex_openmoans3
    gb "No. Don't even reach for that naughty pussy of yours."
    gb "I'm not ready to make it cum yet..."
    stop sound fadeout 1.0

    jump e07s03_after_competition

label e07s03_after_competition:

    $ renpy.music.set_volume(0.2, 1.5, "voice4")
    $ renpy.music.set_volume(0.2, 1.5, "voice5")
    $ renpy.music.set_volume(0.2, 1.5, "voice6")
    scene e07s03-230-lc-talk-mc with dissolve
    $ Lovense.stop()
    $ Lovense.vibrate(3)
    play voice3 dahlia_disgust_yah noloop
    lc "Stop staring like a useless perv. You're all mine for the moment."
    scene e07s03-231-mc-talk-lc with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Yes, [e07_lcname!t]."
    scene e07s03-232-lc-talk-slave with dissolve
    play voice3 dahlia_angry_hm1 noloop
    lc "You there. I want this one locked down."
    play sound sfx_chains_swings1 volume 2.0
    scene e07s03-233-mc-chair with dissolve
    stop sound fadeout 1.0
    pause
    if e07s03_give_all is True:
        scene e07s03-234-mc-talk-lc with dissolve
        play voice2 mc_thinking_emm1 noloop
        mc "Is something wrong, [e07_lcname!t]?"
        scene e07s03-235-lc-talk-mc with dissolve
        play voice3 dahlia_angry_ah2 noloop
        lc "Of course something is wrong, you half-wit."
        lc "You may have beaten [e07_pbname!t]. But for you to beat him, that means that you made me lose."
        scene e07s03-236-lc-talk-mc with dissolve
        play voice3 dahlia_arrogant_hm noloop
        lc "Surely you didn't mean for your [e07_lcname!t] to not enjoy an orgasm because of your pathetic ego?"
        lc "It was just a mistake, wasn't it?"
        scene e07s03-237-mc-talk-lc with dissolve
        play voice2 mc_yes_yes1 noloop
        mc "Yes. I mean... you want me to win against Pete, right?"
        scene e07s03-238-mc-talk-lc with dissolve
        play voice2 mc_disappointed_ah1 noloop
        mc "I have to prove that I'm better than him to get your love."
        scene e07s03-239-lc-talk-mc with dissolve
        play voice3 dahlia_yes_yeah3 noloop
        lc "Sure, you have to prove yourself to me. That's very important."
        play sound sfx_bandage_on1 volume 1.5
        scene e07s03-240-lc-foot with dissolve
        play voice3 dahlia_disappointed_ehh1 noloop
        lc "But you must always bear something else in mind. It is not your pleasure or happiness that matters."
        lc "It's mine you should be worried about."
        $ Lovense.vibrate(10)
        scene e07s03-242-mc-talk with dissolve
        play voice2 mc_pain_rrrr noloop
        mc "Mrrrrhmmm... L-[e07_lcname!t]."
        scene e07s03-241-lc-talk-mc with dissolve
        play voice3 dahlia_disappointed_ehh2 noloop
        lc "Since you robbed me of the chance to cum, I need to give you a new lesson."
        scene e07s03-243-mc-inner-talk with dissolve
        play voice2 mc_pain_mff2 noloop
        mct "Oh fuck me."
        play voice2 d7s4_mcbreathing
        play sound sfx_skirt_off1
        $ Lovense.vibrate(12)
        scene e07s03-244-lc-foot-anim-4 with dissolve
        pause
        play sound sfx_skirt_off3
        $ Lovense.vibrate(14)
        scene e07s03-245-lc-foot-anim-4 with dissolve
        pause
        scene e07s03-246-lc-talk-mc with dissolve
        play voice3 dahlia_arrogant_ha noloop
        lc "And no matter what, you know that is always your final purpose."
        scene e07s03-247-mc-talk-lc with dissolve
        play voice2 d1s5b_ehhh noloop volume 1.5
        mc "I am sorry, [e07_lcname!t]. I'd hoped my actions would please you."
        scene e07s03-248-lc-talk-mc with dissolve
        play voice3 dahlia_no_uhuh noloop
        lc "Well, they didn't. Why must you be so infuriating?"
        play sound sfx_skirt_off1 volume 1.5
        scene e07s03-249-mc-talk-lc with dissolve
        play voice2 mc_scared_huuuh3 noloop
        mc "Nhraah... I don't know... I'm sorry [e07_lcname!t]. I'll..."
        $ Lovense.vibrate(16)
        play voice2 mc_pain_argh1 noloop
        mc "*groans* I wasn't trying to embarrass you. It won't happen again."
        scene e07s03-250-lc-talk-mc with dissolve
        play voice3 dahlia_old_argh2 noloop
        lc "Promises, promises..."
    else:
        scene e07s03-235-lc-talk-mc with dissolve
        play voice3 dahlia_old_argh2 noloop
        lc "I can't believe you lost the contest, [e07_mcname!t]."
        lc "I thought potential public humiliation would inspire you to give it your all."
        scene e07s03-236-lc-talk-mc with dissolve
        play voice3 dahlia_arrogant_hm noloop
        lc "I was wrong."
        lc "Maybe I should just leave you here."
        lc "You and this pathetic cock."
        play sound sfx_bandage_on1 volume 1.5
        $ Lovense.vibrate(8)
        scene e07s03-240-lc-foot with dissolve
        play voice2 mc_pain_rrrr noloop
        mc "Nrrrghh... "
        mc "It was a tough competition, [e07_lcname!t]. Next time I'll be better prepared."
        scene e07s03-241-lc-talk-mc with dissolve
        play voice3 dahlia_arrogant_heh noloop
        lc "Hah! I don't even know if you deserve a \"next\" time, [e07_mcname!t]."
        play sound sfx_skirt_off1
        scene e07s03-243-mc-inner-talk with dissolve
        $ Lovense.vibrate(10)
        play voice2 mc_pain_mff4 noloop
        mct "My balls... they're going to turn into crushed grapes if [e07_lcname!t] continues."
        play voice2 d7s4_mcbreathing
        play sound sfx_skirt_off3
        $ Lovense.vibrate(12)
        scene e07s03-244-lc-foot-anim-4 with dissolve
        pause
        play sound sfx_skirt_off1
        $ Lovense.vibrate(4)
        scene e07s03-245-lc-foot-anim-4 with dissolve
        pause
        scene e07s03-246-lc-talk-mc with dissolve
        play voice3 dahlia_yes_simple noloop
        lc "Yes. But maybe it's something else."
        scene e07s03-243-mc-inner-talk with dissolve
        play voice2 mc_pain_mff5 noloop
        mct "Fuck... it hurts, but something about it feels so fucking good."
        scene e07s03-248-lc-talk-mc with dissolve
        play voice3 dahlia_surprised_huh2 noloop
        lc "You didn't want to win badly enough."
        lc "Perhaps you don't truly love me."
        lc "Is that it, [e07_mcname!t]? You don't love me anymore?"
        scene e07s03-247-mc-talk-lc with dissolve
        play voice2 mc_no_no4 noloop
        mc "No... Not at all, [e07_lcname!t]. You are my whole world, [e07_lcname]. I swear!"
        mc "Nrrrrah... No matter what else happens... I'll always love you."
        scene e07s03-250-lc-talk-mc with dissolve
        play voice3 dahlia_happy_laugh6 noloop
        lc "Hahaha... Mrmmm... I almost believe you."
        scene e07s03-249-mc-talk-lc with dissolve
        play voice2 mc_pain_ou1 noloop
        mct "Almost? But that's the truth."
    $ renpy.music.set_volume(1.0, 0.2, "voice4")
    $ renpy.music.set_volume(1.0, 0.2, "voice5")
    $ renpy.music.set_volume(1.0, 0.2, "voice6")
    stop voice6 fadeout 1.0
    play voice4 girl24_sex_orgasm4 noloop
    play voice5 pete_sex_orgasm1 noloop
    play sound mc_cum_sound1
    $ Lovense.vibrate(18)
    scene e07s03-251-pb-cums with vpunch
    pause
    scene e07s03-252-pb-talk with dissolve
    $ Lovense.vibrate(3)
    play voice5 pete_sex_orgasm3 noloop
    pb "Nurrrh. Fuck me... I think..."
    scene e07s03-253-pb-talk-gb with dissolve
    queue voice5 pete_angry_argh3 noloop
    pb "I think you fucking broke it, Domina Gizela."
    scene e07s03-254-gb-talk-pb with dissolve
    play voice4 girl24_arrogant_huh2 noloop
    gb "If I did, you aren't worthy of being called a bull."
    gb "I'm sure it's just a sprain, my submissives can see to it if needed."
    stop voice5 fadeout 1.0
    play sound sfx_skirt_off2
    scene e07s03-255-gb-talk-arj with dissolve
    play voice4 girl24_arrogant_hm2 noloop
    gb "Clean this mess up."

    $ Lovense.stop()

    $ renpy.end_replay()
    scene e07s03-256-arj-clean-gb with dissolve
    pause
    scene e07s03-257-pb-boner with dissolve
    $ Lovense.vibrate(1)
    play voice6 amrose_disappointed_oh5 noloop
    pause
    scene e07s03-258-pb-look-arj with dissolve
    arj "..."
    scene e07s03-259-arj-talk-gb with fade
    play voice6 amrose_hey_scared noloop
    arj "Mrmmm. I-I... I got him all clean, Lady Gizela."
    scene e07s03-260-gb-talk-arj with dissolve
    play voice4 girl24_surprised_oh1 noloop
    gb "Good. Looks like he's got one more round in him."
    scene e07s03-261-gb-talk-arj with dissolve
    play voice4 girl24_thinking_ah noloop
    gb "Why don't you mount him for me."
    scene e07s03-262-arj-talk-gb with dissolve
    play voice6 amrose_surprised_uh2 noloop
    arj "Me?"
    scene e07s03-263-gb-talk-arj with dissolve
    play voice4 girl24_yes_happy noloop
    gb "Yes. Doubtless many of my attendants have already achieved climax watching me."
    gb "But I'm sure some might prefer seeing how you look with an nice stiff cock stretching that tight hole of yours."
    gb "Come now, no need to be shy..."
    play voice6 amrose_happy_phew1 noloop
    scene e07s03-264-arj-pb with dissolve
    pause
    scene e07s03-265-mc-look-arj with dissolve
    pause
    scene e07s03-266-mc-talk-lc with dissolve
    play voice2 d2s9_confused noloop
    mc "Lydia - I mean [e07_lcname!t]. Please."
    scene e07s03-267-lc-talk-mc with dissolve
    play voice3 dahlia_angry_ah1 noloop
    lc "What is it now?"
    scene e07s03-266-mc-talk-lc with dissolve
    play voice2 d2s12_emmm noloop
    mc "When we talked about AmRose... you said she would mainly just be a servant of yours."
    mc "You told me that she wouldn't fuck other guys."
    scene e07s03-268-lc-laughs with dissolve
    play voice3 dahlia_happy_laugh5 noloop
    lc "Hahahahaha!"
    scene e07s03-269-lc-talk-mc with dissolve
    play voice3 dahlia_surprised_ah2 noloop
    lc "You really are full of surprises. Are you being serious? Shall I call it off?"
    scene e07s03-270-mc-talk-lc with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Please... Please [e07_lcname!t]."
    play voice3 dahlia_thinking_hmm3 noloop
    lc "Mmmm."
    play voice3 dahlia_hey_active2 noloop
    scene e07s03-271-lc-talk-arj-pb with dissolve
    lc "[e07_pbname!t]. Find some other hole to fuck. [e07_arjname!t], come here to attend me."
    play sound sfx_heels_steps2
    scene e07s03-272-arj-walk with dissolve
    pause
    stop sound fadeout 1.0
    scene e07s03-273-lc-talk-mc with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    lc "I didn't know you could be so controlling, my little pet. But don't worry."
    lc "Tonight, AmRose's only duties will be rubbing my feet while you serve me drinks."
    lc "Is that alright with you?"
    scene e07s03-274-mc-talk-lc with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Yes, [e07_lcname!t]."
    scene e07s03-275-lc-talk-mc with dissolve
    play voice3 dahlia_yes_ugu noloop
    lc "I hope you remember this blessing the next time you service me."
    lc "Let's just hope Domina Gizela is not too disappointed with your covetous nature."
    scene e07s03-276-arj-talk-mc with dissolve
    play voice6 amrose_disappointed_ehh1 noloop
    arj "[mcname]..."
    scene e07s03-277-arj-mc-hug with dissolve
    pause
    scene e07s03-278-lc-talk-arj-mc with dissolve
    play voice3 dahlia_angry_oh noloop
    lc "[e07_mcname!t], go get me a long island iced tea. [e07_arjname!t], my feet are feeling a little sore."
    scene e07s03-279-arj-talk-lc with dissolve
    play voice6 amrose_yes_confident2 noloop
    arj "Yes, [e07_lcname!t]."
    $ unlock_gallery_slot("scene", "e07s03")
    play voice5 chastity_closedmoans1
    play voice7 pete_sex_openmoans2
    scene e07s03-280-pb-fuck-zh with dissolve
    pause
    play voice6 amrose_disappointed_ehh2 noloop
    scene e07s03-281-arj-look-pb-zh with dissolve
    pause
    stop voice5 fadeout 1.0
    stop voice7 fadeout 1.0

    stop music fadeout 3.0

    $ Lovense.stop()


    jump e07s04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
