label e09s02:

    $ e09s02_goodguy = False

    play music languid_love_reverbed fadein 3.0
    scene black
    show screen scene_transistion(_("The next day"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound4 d12s2_cafe_crowd fadein 3.0 volume 0.6
    scene e09s02-01-restaurant
    with Fade(0.5, 0.5, 0.5)
    pause
    scene e09s02-02-mc-inner-talk with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.7
    mct "Man... I wonder how Hana is going to take the news..."
    play sound sfx_cloth_rustling2
    scene e09s02-03-mc-inner-talk with dissolve
    play voice2 d14s16_smell noloop
    mct "I have like 18 different bombshells to drop on her...{w} And she hasn't always been totally cool with me..."
    play sound2 sfx_heels_steps2
    scene e09s02-04-hr-restaurant with dissolve
    pause
    scene e09s02-05-mc-talk-hr with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Hey, Hana."
    scene e09s02-06-hr-talk-mc with dissolve
    play voice3 girl30_hey_quiet noloop
    hr "Hey, yourself."
    play sound2 sfx_bed_slide3 noloop volume 0.5
    scene e09s02-07-hr-talk-mc with dissolve
    play voice3 girl30_disappointed_mmm1 noloop
    hr "Did you already order me a coffee?"
    scene e09s02-08-mc-talk-hr with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah. It's just a drip - black. I assumed that was your usual order."
    scene e09s02-09-hr-talk-mc with dissolve
    play voice3 girl30_yes_yeah4 noloop
    hr "And why would you assume that?"
    scene e09s02-10-mc-talk-hr with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "I don't know. Isn't that what journalists drink?"
    play sound sfx_plate_place1 volume 0.7
    scene e09s02-11-hr-talk-mc with dissolve
    play voice3 girl30_thinking_hmm1 noloop
    hr "You've got a point there... and you're not wrong. This is my usual coffee order."
    scene e09s02-12-hr-talk-mc with dissolve
    play voice3 girl30_arrogant_heh noloop
    hr "So what's going on?"
    scene e09s02-13-mc-talk-hr with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "I, erm, wanted to talk to you about Fetish Locator."
    scene e09s02-14-hr-talk-mc with dissolve
    play voice3 girl30_yes_aga2 noloop
    hr "I heard that Lydia is going to trial."
    scene e09s02-15-mc-talk-hr with dissolve
    play voice2 mc_yes_yeah1 noloop
    if cage_ntr is False:
        mc "Yeah... I'm still shocked that she was a part of it... And now it's going to be talked about in front of a jury..."
    else:
        mc "I... I'm still in shock that she was behind the whole thing... And to know she might actually go to jail..."
    scene e09s02-16-hr-talk-mc with dissolve
    play voice3 girl30_disappointed_eeh1 noloop
    hr "Me too. Never would have expected that from little miss goody goody."
    hr "Is that why you wanted to have coffee?"
    scene e09s02-17-mc-talk-hr with dissolve
    play voice2 mc_no_no2 noloop
    mc "Not exactly..."
    scene e09s02-18-hr-talk-mc with dissolve
    play voice3 girl30_arrogant_huh1 noloop
    hr "Huh. I thought you were going to have some groundbreaking news to share with me."
    scene e09s02-19-mc-talk-hr with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "I do..."
    scene e09s02-20-hr-talk-mc with dissolve
    play voice3 girl30_arrogant_pfhah noloop
    hr "Well, what is it?"
    scene e09s02-22-mc-talk-hr with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Uhm..."
    scene e09s02-21-hr-talk-mc with dissolve
    play voice3 girl30_angry_ehh noloop
    hr "Come on, it can't be that bad, [mcname]. It's not like you're telling me that you're going to be running Fetish Locator now or something."
    hr "That's not what you're telling me, right?"
    scene e09s02-19-mc-talk-hr with dissolve
    play voice2 d1s5b_ehhh noloop
    mc "So... Here's the thing-"
    play sound sfx_bed_slide2 volume 0.8
    scene e09s02-23-hr-talk-mc with dissolve
    play voice3 girl30_disgust_mboeah noloop
    hr "Save it, I don't want to hear it."
    scene e09s02-24-mc-talk-hr with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "Hana-"
    scene e09s02-25-hr-talk-mc with dissolve
    play voice3 girl30_angry_err3 noloop
    hr "No, [mcname]. Fuck you."
    play sound sfx_cloth_planket2
    scene e09s02-26-mc-talk-hr with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Just, hang on-"
    scene e09s02-27-hr-talk-mc with dissolve
    play voice3 girl30_angry_mrr noloop
    hr "I don't want to hear whatever bull shit you're selling. You were just in the middle of all of this! You know how bad it can be!"
    scene e09s02-28-mc-talk-hr with dissolve
    play voice2 mc_yes_yes6 noloop
    mc "And that's why I'm perfect to run it!"
    play sound sfx_heels_steps1 loop
    scene e09s02-29-hr-talk-mc with dissolve
    play voice3 girl30_no_serious noloop
    hr "No."
    scene e09s02-30-mc-talk-hr with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Now, come on Hana-"
    scene e09s02-31-hr-talk-mc with dissolve
    play voice3 girl30_arrogant_hmf noloop
    hr "Fuck you.{w} I'm still running my piece."
    scene e09s02-32-mc-talk-hr with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "There's something else I need to tell you."
    scene e09s02-33-hr-talk-mc with dissolve
    play voice3 girl30_no_nope1 noloop
    hr "No. I'm leaving. Goodbye, [mcname]."
    scene e09s02-34-mc-talk-hr with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "It's about the Senator!"
    stop sound fadeout 1.0
    scene e09s02-35-hr-talk-mc with dissolve
    play voice3 girl30_arrogant_huh3 noloop
    hr "You have one minute."
    play sound sfx_bed_slide3 volume 0.5
    scene e09s02-36-mc-talk-hr with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "He was on Fetish Locator."
    scene e09s02-37-hr-talk-mc with dissolve
    play voice3 girl30_thinking_mmm2 noloop
    hr "I could have guessed-"
    scene e09s02-38-mc-talk-hr with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "And we have all of his data. Everything he sent or said while he was using the app."
    scene e09s02-39-hr-talk-mc with dissolve
    play voice3 girl30_angry_err4 noloop
    hr "That's exactly the reason that no one should be in charge. That the app should be shut down."
    scene e09s02-40-mc-talk-hr with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "But we can also stop him."
    mc "That's why I called. Look, I knew you were going to be mad about us taking over Fetish Locator."
    mc "But really, I called to tell you that we have a way for you to take down the Senator. Once and for all."
    scene e09s02-41-hr-thoughtful with dissolve
    pause
    scene e09s02-42-mc-talk-hr with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Please, Hana. No matter what you decide to do, at the very least let Fetish Locator do something good for your life."
    scene e09s02-43-hr-talk-mc with dissolve
    play voice3 girl30_thinking_emm2 noloop
    hr "What did you mean by 'us'."
    scene e09s02-44-mc-talk-hr with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Huh?"
    scene e09s02-45-hr-talk-mc with dissolve
    play voice3 girl30_thinking_hmm2 noloop
    hr "You said 'you' were going to be mad at {i}us.{/i} Who is 'us'?" id e09s02_1358c426
    scene e09s02-46-mc-talk-hr with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "Oh, it's me, and AmRose, and Stacy, and Allison."
    scene e09s02-47-hr-talk-mc with dissolve
    play voice3 girl30_arrogant_hah2 noloop
    hr "Really?"
    scene e09s02-48-mc-talk-hr with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, technically AmRose is the president of whatever we're doing."
    scene e09s02-49-hr-talk-mc with dissolve
    play voice3 girl30_surprised_huh3 noloop
    hr "Why her?"
    scene e09s02-50-mc-talk-hr with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Because she hates it the most. No one will make sure things stay above board more than AmRose will."
    mc "What we want to do is build a better Fetish Locator. Something new. Something that stays true to all the promises that Lydia made to us."
    mc "A safe place. Somewhere people can go to find community, explore fantasies without being judged."
    scene e09s02-51-hr-talk-mc with dissolve
    play voice3 girl30_arrogant_hm noloop
    hr "Hmph."
    scene e09s02-48-mc-talk-hr with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Maybe. But, we can do it."
    mc "And we're not above oversight."
    scene e09s02-49-hr-talk-mc with dissolve
    play voice3 girl30_disappointed_mmm2 noloop
    hr "Show me what you found on the Senator."
    play sound sfx_cloth_rustling5
    scene e09s02-52-mc-phone with dissolve
    pause
    play sound sfx_phone_tapping1 volume 1.6 loop
    scene e09s02-53-hr-talk-mc with dissolve
    hr "..."
    stop sound fadeout 1.0
    play voice3 girl30_disgust_oof noloop
    hr "Jesus..."
    scene e09s02-54-mc-talk-hr with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah. It's, uhm, hard to read..."
    scene e09s02-55-hr-talk-mc with dissolve
    play voice3 girl30_disgust_mmm noloop
    hr "I... I wish I could say I was surprised. He's a piece of shit, and these are the things a piece of shit sends on the internet."
    scene e09s02-56-hr-talk-mc with dissolve
    play voice3 girl30_surprised_wha1 noloop
    hr "Wait..."
    scene e09s02-57-mc-talk-hr with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "What is it?"
    scene e09s02-58-phone with dissolve
    play voice3 girl30_thinking_emm1 noloop
    hr "I know her..."
    scene e09s02-59-hr-talk-mc with dissolve
    play voice3 girl30_disappointed_mmm3 noloop
    hr "She used to be the Senator's old assistant."
    scene e09s02-60-mc-talk-hr with dissolve
    play voice2 mc_thinking_hm noloop
    mc "No shit..."
    scene e09s02-61-hr-talk-mc with dissolve
    play voice3 girl30_arrogant_yeah2 noloop
    hr "Yeah...{w} Jesus, the shit he was sending her."
    scene e09s02-62-mc-talk-hr with dissolve
    play voice2 mc_yes_yeah6 noloop
    mc "Yeah. We saw the unsolicited dick pics."
    scene e09s02-63-hr-talk-mc with dissolve
    play voice3 girl30_happy_oh1 noloop
    hr "It's so much more than that. He was coming after her career, her school admittance... Everything."
    scene e09s02-65-mc-talk-hr with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Yeah... It was tough to read. She's just one of a dozen."
    play sound sfx_cloth_rustling1
    scene e09s02-64-hr-talk-mc with dissolve
    play voice3 girl30_angry_uhh noloop
    hr "This bastard just won't leave anyone alone..."
    hr "She's how you bring him down."
    scene e09s02-62-mc-talk-hr with dissolve
    play voice2 mc_surprised_how2 noloop
    mc "How so?"
    scene e09s02-63-hr-talk-mc with dissolve
    play voice3 girl30_thinking_mmm1 noloop
    hr "You need her to prove the story. She previously worked for the Senator, she was the one who received his messages, she needs to verify everything."
    scene e09s02-66-mc-talk-hr with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "Do you think you'll be able to find her?"
    scene e09s02-67-hr-talk-mc with dissolve
    play voice3 girl30_yes_aga3 noloop
    hr "It'll take some time, but I should be able to. If you can give me a copy of everything you downloaded, that'll speed things up."
    play sound sfx_bandage_on1
    scene e09s02-68-mc-talk-hr with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "I brought a USB with all of the Senator's profile and messages and everything with me."
    play sound sfx_paper_slide1
    scene e09s02-69-usb with dissolve
    pause
    scene e09s02-70-hr-talk-mc with dissolve
    play voice3 girl30_disappointed_eeh2 noloop
    hr "Thank you."
    scene e09s02-71-mc-talk-hr with dissolve
    play voice2 mc_no_no5 noloop
    mc "You don't need to thank me."
    scene e09s02-72-hr-talk-mc with dissolve
    play voice3 girl30_disappointed_ehh1 noloop
    hr "This is something I've wanted for a long time..."
    hr "The Senator has thought himself untouchable for so long... paid the right bribes, put pressure on the right people..."
    scene e09s02-73-hr-talk-mc with dissolve
    play voice3 girl30_angry_ehh noloop
    hr "A morally corrupt son of a bitch... That can finally change..."
    menu:
        "It's just the right thing to do"(hint="e09s02m01c01"):
            $ e09s02_goodguy = True
            scene e09s02-74-mc-talk-hr with dissolve
            play voice2 mc_yes_yes1 noloop
            mc "When we found it, we knew we had to share it with you."
        "I hope it buys me a little good will"(hint="e09s02m01c02"):

            scene e09s02-74-mc-talk-hr with dissolve
            play voice2 mc_yes_yes1 noloop
            mc "I hope that it's a sign of good faith from us."

    scene e09s02-75-hr-talk-mc with dissolve
    play voice3 girl30_arrogant_eem noloop
    hr "You know, this changes nothing, right?"
    hr "I'm still going to run my piece on Fetish Locator. About how it's a bad thing, and anyone and everyone involved with it should be taken down."
    scene e09s02-76-mc-talk-hr with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Look..."
    if e09s02_goodguy:
        mc "You're going to do whatever you're going to do Hana. I'm not here to stop you."
        mc "But I want you to have that, at the very least. I don't know the whole story between you and the Senator, but I know it's bad."
        scene e09s02-77-mc-talk-hr with dissolve
        play voice2 mc_happy_a1 noloop
        mc "Maybe this can help bring you closure, bring him down, or whatever."
        mc "This isn't a bargaining chip, and it's not a demand. You can walk away right now and post the story, and I'll still know I did the right thing giving you this information."
        mc "And if there's anything else we can do to help, we're glad to do it. Even if your story runs."
    else:
        mc "I hope that us sharing this information with you would change your mind at least a little bit."
        mc "We just want to show you that we're going to run a different Fetish Locator."
        scene e09s02-77-mc-talk-hr with dissolve
        play voice2 mc_happy_a1 noloop
        mc "That we won't put up with the kind of behavior that Lydia perpetuated. Or the Senator. That we're going to do everything in our power to take them down."
        mc "But, I can't stop you. If you decide to run the Fetish Locator piece, that's your decision."
        mc "Just know, the Fetish Locator Rebooted would be different."
    play sound sfx_bed_slide2 volume 0.6
    scene e09s02-78-hr-talk-mc with dissolve
    play voice3 girl30_thinking_mmm3 noloop
    hr "Maybe... I can hold off for a while. Finding Londyn is going to take up a lot of my time."
    hr "When I find something, I'll make sure to let you know."
    scene e09s02-79-mc-talk-hr with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Please. And if there's anything we can do to help, we're always happy to do so."
    scene e09s02-80-hr-talk-mc with dissolve
    play voice3 girl30_yes_yeah2 noloop
    hr "I'll keep that in mind."
    play sound sfx_heels_steps1 loop
    scene e09s02-81-hr-talk-mc with dissolve
    play voice3 girl30_hey_bye6 noloop
    hr "I'll call, [mcname]."
    scene e09s02-82-mc-talk-hr with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "I look forward to it, Hana."
    stop sound fadeout 2.5
    scene e09s02-83-mc-inner-talk with dissolve
    play voice2 mc_angry_errr5 noloop
    mct "Well, that could have gone better..."
    mct "But it could have gone a whole lot worse."
    scene e09s02-84-mc-inner-talk with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mct "What was I expecting? That Hana would just up and accept that Fetish Locator being under new management was a good thing."
    play sound sfx_drink_slurp2
    scene e09s02-85-mc-inner-talk with dissolve
    mct "But somehow I feel like we just wandered into a whole new world of difficult... This Senator guy sounds like he's dangerous... or at the very least, powerful."
    mct "I hope I don't regret this..."
    scene e09s02-86-mc-inner-talk with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "Well, I better get back. I've got a brand to get back together!"
    stop music fadeout 3.0
    stop sound4 fadeout 3.0

    jump e09s03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
