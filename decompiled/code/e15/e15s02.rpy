image e15s02-a15-glambot = Movie(play = "images/E-15/s02/anim/e15s02-a15-2x-50fps.webm", start_image = "e15s02-a15 mes-talk-mc-glambot-15-000", image = "e15s02-a15 mes-talk-mc-glambot-15-149", loop = False)

label e15s02:

    scene black
    show screen scene_transistion(_("The next morning"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene e15s02-01-mc-office
    play music thinking_music_4 fadein 1.5 volume 3.5
    with Fade(0.5, 0.5, 0.5)
    pause
    play sound sfx_cloth_rustling2
    scene e15s02-02-mc with dissolve
    pause
    scene e15s02-03-sy-talk-mc with dissolve
    play voice3 stacy_arrogant_huh2 noloop
    sy "Someone is looking fancy."
    scene e15s02-04-mc-talk-sy with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yup. Got a big meeting in five minutes. Got to dress to impress."
    scene e15s02-05-sy-talk-mc with dissolve
    play voice3 stacy_happy_laugh4 noloop
    sy "Hahaha. Wait, so you don't just whip out your cock and make the sale?"
    scene e15s02-06-mc-talk-sy with dissolve
    play voice2 mc_no_nope1 noloop
    mc "Nope."
    play sound sfx_chair_slide1
    scene e15s02-07-mc-talk-sy with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "The product might sell itself, but for people interested in the premium packages, we have to put our best foot forward."
    scene e15s02-08-sy-talk-mc with dissolve
    play voice3 stacy_mmm2 noloop
    sy "Do you want me to leave?"
    scene e15s02-09-mc-talk-sy with dissolve
    play voice2 d9s3_no noloop volume 2.0
    mc "No, so long as you stay there, look cute, and keep quiet, it will be fine."
    play sound sfx_cloth_rustling3
    scene e15s02-10-sy-talk-mc with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "That's asking a lot of me. But since you've been such a great host, I'll do my best."
    scene e15s02-09-mc-talk-sy with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Thanks."
    scene e15s02-11-mc-inner-talk with dissolve
    play voice2 d14s16_smell noloop
    mct "Just like Min always says. 'The product sells itself, you just have to make them feel special and they'll open their wallet'."
    stop music fadeout 3.0
    scene e15s02-12-knock-knock with dissolve
    call knock from _call_knock_27
    scene e15s02-13-mc-inner-talk with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mct "Showtime."
    play sound sfx_door_openclosed1
    play music rich_bitch
    scene e15s02-14-min-walk with dissolve
    play sound2 sfx_heels_steps2
    queue sound sfx_heels_steps1 loop
    pause
    stop sound2 fadeout 1.0
    stop sound fadeout 1.0
    scene e15s02-a15 mes-talk-mc-glambot-15-000 with dissolve
    play voice3 min_hey_greeting noloop
    if persistent.is_special is True:
        mes "[mcname], may I present Mr. Douglas Melville, his wife Chloe Melville, and their daughter Olivia."
    else:
        mes "[mcname], may I present Mr. Douglas Melville, his wife Chloe Melville, and their maid, Olivia Small."
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.0>", sfx_camera_fly1] volume 2.0 noloop
    scene e15s02-a15-glambot
    pause
    play sound sfx_hands_clap3
    stop sound2 fadeout 1.0
    scene e15s02-16-mc-handshake with dissolve
    pause
    scene e15s02-17-mc-talk with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "So glad to meet you all. Welcome to the Waterfall Spa."
    if date_mh is True or d09_moneybags_done is True:
        scene e15s02-18-mc-inner-talk with dissolve
        play voice2 d1s1_mmm noloop volume 1.5
        mct "Why do I feel like I've seen him before?"
    if date_mh is True:
        play voice2 mc_pain_mff1 noloop
        mct "Oh shit. That's the client that Lyssa was against in court."
        scene e15s02-19-mc-inner-talk with dissolve
        mct "I hope this doesn't affect our dealings."
    elif d09_moneybags_done is True:
        play voice2 mc_pain_mff1 noloop
        mct "Wow. Now I know where I saw him before."
        mct "He was the client that liked getting off to me and Samiya fucking."
        scene e15s02-19-mc-inner-talk with dissolve
        mct "What a small kinky world."
        mct "Hmm. Well, I shouldn't bring that up unless he does."
    scene e15s02-20-dm-talk-mc with dissolve
    play voice4 melvil_yes_yesyes1 noloop
    ceo "Yes yes, great to be here. But who is she?"
    scene e15s02-21-mc-talk-dm with dissolve
    play voice2 mc_surprised_oh1 noloop
    mc "Ah just an intern. I hope you don't mind."
    scene e15s02-22-dm-talk-mc with dissolve
    play voice4 melvil_arrogant_haha1 noloop
    ceo "Haha. I suppose not."
    play sound sfx_cloth_rustling4 volume 2.0
    scene e15s02-23-everyone-sits-down with dissolve
    pause
    scene e15s02-24-mc-talk with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Like I was saying, we're very happy to have you here at the spa."
    scene e15s02-25-dm-talk-mc with dissolve
    play voice4 melvil_yes_yes4 noloop
    ceo "Yes. Better late than never."
    scene e15s02-26-dm-talk-mc with dissolve
    play voice4 melvil_thinking_hmm2 noloop
    ceo "When we entered the second month on the waiting list, I imagined this was going to end up just being a big waste of time."
    if persistent.is_special is True:
        scene e15s02-27-om-talk-dm with dissolve
        play voice5 girl34_arrogant_ha1 noloop
        ovs "Alright, Dad. Are you happy you got that out of your system?"
        scene e15s02-28-om-talk-mc with dissolve
        play voice5 girl34_thinking_hmm5 noloop
        ovs "Penny swore to me that this will be worth the wait."
        ovs "She said that Mr. Young here is a savant. A Master of the discipline."
        scene e15s02-32-mc-talk with dissolve
        play voice2 mc_thinking_hm noloop
        mc "I'm delighted that Penny had such a good time with us."
        scene e15s02-33-om-talk with dissolve
        play voice5 girl34_disappointed_mmf1 noloop
        ovs "Mmmhmm. Naturally, I hope to come out ahead of her."
        scene e15s02-34-mes-talk-om with dissolve
        play voice3 min_thinking_emm noloop
        mes "Our spa isn't really meant to be a place of competition, Olivia."
        scene e15s02-35-dm-talk with dissolve
        play voice4 melvil_surprised_what1 noloop
        ceo "What nonsense. To those in the top rung of society, you must always strive to lead."
        scene e15s02-36-dm-talk with dissolve
        play voice4 melvil_thinking_hmm1 noloop
        ceo " And since this practice appears to be the new {b}it{/b} thing, then we can't let our daughter get left behind."
        scene e15s02-37-mes-talk with dissolve
        play voice3 min_yes_simple noloop
        mes "You're very wise, Mr. Melville. I know how important it is for the younger generation to impress their parents, friends, and associates."
        scene e15s02-38-mc-inner-talk with dissolve
        play voice2 mc_thinking_mmm6 noloop
        mct "Ah Min. Perfectly able to take her frustration with her father and use it to our advantage."
        mct "God, she's the fucking best."
        scene e15s02-39-mes-talk with dissolve
        play voice3 min_surprised_ehh1 noloop
        mes "But making a big splash can take a lot of resources and training. And therefore, I recommend that your daughter enroll in our premium service."
        mes "Does that sound good to you, Olivia?"
        scene e15s02-40-om-talk with dissolve
        play voice5 girl34_yes_yeah5 noloop
        ovs "I guess."
        scene e15s02-41-cm-talk with dissolve
        play voice6 girl30_arrogant_heh noloop
        cm "I think it would be best if we heard the details on all the services. We want Olivia to be happy and comfortable."
        cm "So we need to know more about your... 'spa', and its services." id e15s02_e73682d9
    else:
        scene e15s02-28-om-talk-mc with dissolve
        play voice5 girl34_thinking_emm3 noloop
        ovs "Mr. Melville, I am sure Mr. Young meant no offense."
        scene e15s02-29-mc-talk-om with dissolve
        play voice2 mc_yes_yes2 noloop
        mc "Yes. And we're just delighted there is finally an opening for you."
        scene e15s02-30-dm-talk-mc with dissolve
        play voice4 melvil_thinking_emm1 noloop
        ceo "Not for us. For our Maid Olivia."
        scene e15s02-29-mc-talk-om with dissolve
        play voice2 mc_yes_sure1 noloop
        mc "Of course."
        scene e15s02-31-cm-talk with dissolve
        play voice6 girl30_arrogant_heh noloop
        cm "There has been talk among our peers that many people have come to you for..."
        cm "Your expertise. We know a young woman named Penny who gave you a rave review."
        scene e15s02-32-mc-talk with dissolve
        play voice2 mc_thinking_hm noloop
        mc "And I'm delighted that Penny had such a good time with us."
        scene e15s02-30-dm-talk-mc with dissolve
        play voice4 melvil_arrogant_huh2 noloop
        ceo "But of course, we'll be happy to pay more, within reason, so that our Maid will be even better at Watersports."
        ceo "Better than Penny or any other woman who comes through your program."
        scene e15s02-34-mes-talk-om with dissolve
        play voice3 min_thinking_emm noloop
        mes "Excuse me, Mr. Melville, but it's not really our practice to play into a competition."
        scene e15s02-35-dm-talk with dissolve
        play voice3 melvil_thinking_hmm3 noloop
        ceo "I'm afraid you're already in it. And we want our Maid to be the best she can be."
        scene e15s02-45-mc-talk-dm with dissolve
        play voice2 mc_yes_okay2 noloop volume 1.4
        mc "Well, if price is no object, we'll do our best."
        scene e15s02-41-cm-talk with dissolve
        play voice6 girl30_arrogant_yeah3 noloop
        cm "I think it would be best to hear the details on all the services."
        cm "I'd like to know exactly what our Maid will be going through at your... {w}'spa'." id e15s02_1d9f1d03
    scene e15s02-42-mes-talk with dissolve
    play voice3 min_yes_happy noloop
    mes "Of course."
    mes "My partner would be happy to give you an overview of everything we have to offer."
    scene e15s02-43-mc-talk with dissolve
    play voice2 mc_thinking_hmm1 noloop volume 1.3
    mc "Ahem. First, we have the Public Toilet service."
    mc "Put simply, this is a crash course in Watersports for anyone who has always wanted to try it."
    mc "It can be quite aggressive, so we don't recommend it for beginners."
    scene e15s02-44-dm-talk-mc with dissolve
    play voice4 melvil_thinking_huh2 noloop
    ceo "What does it involve?"
    scene e15s02-45-mc-talk-dm with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "For an entire work day, the customer takes on the role of a public toilet in one of our special bathrooms."
    mc "While they're at their 'station' They can be visited and used by any of our guests."
    scene e15s02-46-cm-talk with dissolve
    play voice6 girl30_disgust_oi noloop
    cm "People... {b}pay{/b} for that."
    scene e15s02-47-mes-talk with dissolve
    play voice3 min_yes_yeah1 noloop
    mes "It's quite an experience. And here you can do it under our watchful care, unlike other areas that... don't have the same approach as us."
    mes "The safety of our clients is paramount, of course, and someone from staff is always on hand."
    scene e15s02-48-dm-talk-mc with dissolve
    play voice4 melvil_happy_alright1 noloop
    ceo "I should think so. Alright, so that is one option. What are the others?"
    scene e15s02-49-mc-talk-dm with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "The second tier we offer is a Group Session. We have an experienced coach take new students through different techniques."
    mc "Each session basically focuses on one area of watersports."
    scene e15s02-50-mc-talk with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "And we offer different levels of training so people who have some understanding of the fetish don't have to start at square one."
    mc "I think this is our most flexible option. For price, it is the middle of the road."
    scene e15s02-51-dm-talk-mc with dissolve
    play voice4 melvil_thinking_and1 noloop volume 1.3
    ceo "And its effectiveness compared to the top level?"
    scene e15s02-52-mes-talk-dm with dissolve
    play voice3 min_happy_mmm noloop
    mes "I would say that the Group Sessions leave something to be desired compared to the one-on-one classes of our top package."
    mes "The supervisor has to share their expertise with multiple students after all."
    scene e15s02-53-dm-talk with dissolve
    play voice4 melvil_thinking_hmm4 noloop
    ceo "Mmmm. Well let's hear about this premium package of yours."
    scene e15s02-54-mc-talk with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "So our best service is Individual Training. I personally work hand-in-hand with the customer and train them from a beginner's level all the way up to advanced practices."
    mc "The training is daily, and the cost covers lodging, food, and care as they go through the coursework."
    scene e15s02-55-dm-talk-mc with dissolve
    play voice4 melvil_arrogant_huh1 noloop
    ceo "And how long does that take?"
    scene e15s02-56-mc-talk with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "It can vary by person. On average, it takes half a year. We've had some people longer, and some students finish all their lessons in four months."
    mc "But I never suggest that people go into this with a rushed mindset. Developing the skill can take patience. It can be a shock to some."
    scene e15s02-57-om-talk with dissolve
    if persistent.is_special is True:
        play voice5 girl34_disappointed_oh2 noloop
        ovs "I'm sure that I'll get everything mastered in two months. I can take anything."
        scene e15s02-58-dm-talk with dissolve
        play voice4 melvil_arrogant_haha2 noloop
        ceo "Haha, you see, my dear. Nothing to worry about."
    else:
        play voice5 girl34_disappointed_oh2 noloop
        ovs "I will do my best to complete your coursework in two months, Mr. Young."
        ovs "I'd never want to embarrass the Melvilles."
        scene e15s02-58-dm-talk with dissolve
        play voice4 melvil_arrogant_haha2 noloop
        ceo "You're the best, Olivia."
    scene e15s02-59-cm-talk with dissolve
    play voice6 girl30_hey_whisper noloop volume 1.8
    cm "Thank you for going over all of the options, Mr. Young."
    scene e15s02-60-mc-talk with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Of course. Can I answer any other questions?"
    scene e15s02-61-cm-look-dm with dissolve
    play voice6 girl30_thinking_mmm3 noloop
    cm "Mmhmm."
    scene e15s02-62-dm-talk-om with dissolve
    play voice4 melvil_happy_hmm1 noloop
    ceo "Anything, my dear?"
    scene e15s02-63-om-talk-dm with dissolve
    if persistent.is_special is True:
        play voice5 girl34_no_nouh1 noloop
        ovs "Nothing, daddy. You know which program I want to try."
        scene e15s02-64-dm-talk-om with dissolve
        play voice4 melvil_yes_yes2 noloop
        ceo "Yes..."
    else:
        play voice5 girl34_no_nouh1 noloop
        ovs "Nothing, Mr. Melville."
    scene e15s02-65-dm-talk-mc with dissolve
    play voice4 melvil_thinking_emm1 noloop
    ceo "Mr. Young, we will be happy to enroll in your most prestigious service."
    ceo "Olivia will get Individual Training."
    scene e15s02-66-dm-talk with dissolve
    play voice4 melvil_thinking_huh2 noloop
    if persistent.is_special is True:
        ceo "Nothing but the best for my darling."
    else:
        ceo "We will have nothing less than the best for our Maid."
        scene e15s02-67-om-talk with dissolve
        play voice5 girl34_disappointed_oh3 noloop
        ovs "You're too kind, Mr. Melville."
    scene e15s02-68-mc-talk with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "That is wonderful to hear, Sir."
    scene e15s02-69-mc-talk with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Ahem. Well, if everything is agreeable, then I'll have Ms. Eun-Soo reach out to you later today with the final details."
    play sound sfx_cloth_rustling3 volume 2.5
    scene e15s02-70-mc-talk-om with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "And once that is done, I'm sure we'll be seeing you soon, Olivia."
    scene e15s02-71-om-talk-mc with dissolve
    play voice5 girl34_yes_aga4 noloop
    ovs "I hope so."
    scene e15s02-72-dm-talk-mc with dissolve
    play voice4 melvil_happy_alright1 noloop
    ceo "Sounds like a deal, Mr. Young. We'll be waiting for your call."
    scene e15s02-73-mes-talk with dissolve
    play voice3 min_hey_simple noloop
    mes "Thank you for your time."
    scene e15s02-72-dm-talk-mc with dissolve
    play voice4 melvil_yes_yeah1 noloop
    ceo "The pleasure was all mine, Ms. Eun-Soo."

    jump e15s02_after_meeting

label e15s02_after_meeting:

    $ renpy.music.set_volume(0.4, 4.0, "music")
    play sound sfx_door_closed1
    scene e15s02-74-group-left with Fade(0.5, 0.5, 0.5)
    play voice3 min_happy_mmm noloop
    pause
    scene e15s02-75-sy-talk with dissolve
    play voice4 stacy_thinking_emm4 noloop
    sy "Is something wrong?"
    play sound sfx_heels_steps1 loop
    scene e15s02-76-mc-talk-sy with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Was it just me or was that like super-easy?"
    scene e15s02-77-mes-talk-mc with dissolve
    play voice3 min_surprised_what noloop
    mes "What do you mean? You did great. You're a natural salesman."
    scene e15s02-78-mc-min-kiss with dissolve
    play voice3 min_old_mff noloop
    play voice2 mc_thinking_mmm1 noloop
    play sound dahlia_kiss_french1
    play sound2 sfx_cloth_rustling2 noloop volume 2.5
    mes "Mmm."
    scene e15s02-79-mc-talk-mes with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Okay now what really happened?"
    scene e15s02-80-sy-laughs with dissolve
    play voice4 stacy_laugh4 noloop
    sy "Hehehe."
    scene e15s02-81-mes-talk-mc with dissolve
    play voice3 min_arrogant_huh1 noloop
    mes "From the looks of it, they had made up their minds before they even walked in the door."
    play voice2 mc_surprised_uh1 noloop
    mc "Really?"
    scene e15s02-85-mes-talk-mc with dissolve
    play voice3 min_yes_aga noloop
    mes "Some rich people are like that. They just want to feel the fear coming off people as they pour their heart and soul into a pitch."
    mes "But that doesn't mean you didn't do a great job. Precise and to the point. Just like we practiced."
    scene e15s02-82-sy-talk-mc with dissolve
    play voice4 stacy_hey_attention1 noloop
    sy "See, you totally could have just taken your dick out."
    scene e15s02-83-mes-talk with dissolve
    play voice3 min_arrogant_huh2 noloop
    mes "There will plenty of time for that once their money is in the bank."
    play voice4 stacy_yes_yeah1 noloop
    sy "Good point."
    scene e15s02-84-mc-talk with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I'm glad it's over, but it was pretty stressful."
    mc "I don't know if I want to put up with more families like that."
    scene e15s02-85-mes-talk-mc with dissolve
    play voice3 min_thinking_oh noloop
    mes "So long as you do great training Olivia, the rest will come along more easily."
    mes "And that means enough money for us to consider expanding."
    scene e15s02-86-mc-talk with dissolve
    play voice2 mc_thinking_hmm6 noloop
    mc "That would be great."
    mc "I just realized that having a full class of girls is a bit of a bummer."
    play sound sfx_chair_slide1
    scene e15s02-87-sy-talk-mc with dissolve
    play voice4 stacy_arrogant_huh3 noloop
    sy "What is wrong?"
    scene e15s02-88-mc-talk-sy with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "That means I'll have less time to spend with you, Stacy.."
    scene e15s02-87-sy-talk-mc with dissolve
    play voice4 stacy_thinking_well1 noloop
    sy "Well, so long as you don't mind me tagging along like in the meeting, we'll still get to hang out."
    play voice2 mc_thinking_hmm3 noloop
    mc "That could work."
    scene e15s02-89-mes-evil-eye with dissolve
    play voice3 min_thinking_hmm3 noloop
    mes "Hmm."
    scene e15s02-90-mc-talk-mes with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "Unless it doesn't."
    scene e15s02-91-mes-talk-mc with dissolve
    play voice3 min_disappointed_ehh1 noloop
    mes "Of course it could work. Just please make sure to follow [mcname]'s lead, Stacy."
    mes "We have to put our best foot forward. Especially around Olivia."
    scene e15s02-92-sy-talk with dissolve
    play voice4 stacy_yes_fine1 noloop
    sy "I will be the sexiest and most well-behaved intern you could ask for."
    scene e15s02-93-mes-talk-sy with dissolve
    play voice3 min_thinking_hmm2 noloop
    mes "Thank you."
    scene e15s02-94-mc-talk with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Great, it's settled."
    mc "Now it's time for us both to get back to work. I gotta start preparing for Olivia's training."
    scene e15s02-95-mes-talk-mc with dissolve
    play voice3 min_yes_ugu noloop
    mes "Good. I should have the Melville's payment plan organized within an hour."
    mes "With luck, I'll have their payment processed before lunch."
    mes "Oh, and don't forget, it's your turn to cook dinner tonight."
    play sound sfx_heels_steps1 loop
    scene e15s02-96-mc-talk-mes with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "What would I do without you?"
    scene e15s02-97-mes-talk-mc with dissolve
    play voice3 min_no_nah noloop
    mes "Fortunately for us both, you don't have to experience that."
    scene e15s02-98-sy-laughs with dissolve
    play voice4 stacy_happy_laugh3 noloop fadein 0.1
    sy "Hahaha."
    stop sound fadeout 1.5

    stop music fadeout 3.5
    jump e15s03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
