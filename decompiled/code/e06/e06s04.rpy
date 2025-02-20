image e06s04-a44-glambot-1 = Movie(play = "images/E-06/s04/anim/e06s04-a44-2x-50fps.webm", start_image = "e06s04-a44 sy-glambot-44-000_i", image = "e06s04-a44 sy-glambot-44-119_i", loop = False)

label e06s04:

    scene black
    show screen scene_transistion(_("The Next Day"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene e06s04-01-lc-phone
    with Fade(0.5, 0.5, 0.9)
    queue music music_happy_beavers
    pause
    play sound sfx_barefoot_steps1 loop
    scene e06s04-02-mc-stairs with dissolve
    pause
    stop sound fadeout 1.5
    scene e06s04-03-lc-talk-mc with dissolve
    play voice3 lydia_lydiahey noloop
    lc "It's all set."
    play sound maria_kiss1
    scene e06s04-04-lc-kiss-mc with dissolve
    pause
    scene e06s04-05-lc-talk-mc with dissolve
    play voice3 lydia_hmmmm noloop
    lc "I'm going to go freshen up."
    scene e06s04-06-mc-talk-lc with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Alright lover."
    $ renpy.music.set_volume(0.3, 1.0, "sound3" )
    play sound3 park fadein 3.0
    scene e06s04-07-mc-pool with dissolve
    pause
    scene e06s04-08-mc-notice-arj-sy with dissolve
    pause
    scene e06s04-09-mc-talk-arj-sy with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Welcome to la Casa de Cox."
    scene e06s04-10-arj-talk-mc with dissolve
    play voice4 amrose_thinking_oh2 noloop
    arj "Where should we put our luggage?"
    scene e06s04-11-mc-talk-arj with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Don't worry about them. We're having a pool day. Min is already out there."
    scene e06s04-12-sy-talk-mc with dissolve
    play voice5 stacy_yay noloop
    sy "Yes."
    scene e06s04-13-arj-talk-mc with dissolve
    play voice4 amrose_arrogant_huh3 noloop
    arj "I'd rather get things organized."
    scene e06s04-14-mc-talk-arj with dissolve
    play voice2 mc_happy_a1 noloop
    mc "It's okay just to cut loose today, sweetheart."
    play sound sfx_cloth_rustling1
    scene e06s04-15-mc-talk-arj with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "We've got lunch coming in an hour. And I'll help move everything where it needs to go."
    mc "My first priority is everyone just gets to relax and have fun."
    scene e06s04-16-arj-talk-mc with dissolve
    play voice4 amrose_yes_okay2 noloop
    arj "Okay. I can relax. Totally."
    play sound maria_kiss2
    scene e06s04-17-arj-mc-kiss with dissolve
    pause
    scene e06s04-18-sy-smiles with dissolve
    play voice5 stacy_arrogant_huh3 noloop
    pause
    play voice4 amrose_surprised_uh2 noloop
    play sound sfx_skirt_off2
    scene e06s04-19-sy-grabs-arj with dissolve
    pause
    scene e06s04-20-sy-talk-arj with dissolve
    play voice5 stacy_hey noloop
    sy "Come on red, let's check out our quarters in the master's manse."
    scene e06s04-21-mc-pool with Dissolve(0.8)
    pause
    scene e06s04-22-mc-stand with dissolve
    pause
    play sound sfx_water_floatup2
    scene e06s04-23-mes-pool with dissolve
    pause
    play sound sfx_water_floatup1
    scene e06s04-24-mes-talk-mc with dissolve
    pause
    scene e06s04-25-mes-pool with dissolve
    pause
    scene e06s04-26-mes-talk-mc with dissolve
    play voice4 min_hey_simple noloop
    mes "Hey handsome."
    mes "What kept you?"
    play sound sfx_water_dive1
    scene e06s04-27-mc-talk-mes with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Final guests just arrived."
    scene e06s04-28-mes-talk-mc with dissolve
    play voice4 min_arrogant_huh1 noloop
    mes "Mmm. Think you have time to reapply my sunscreen before you have your hands full?"
    play sound sfx_paper_slide1
    scene e06s04-29-mc-looks-mes with dissolve
    pause
    scene e06s04-30-mc-talk-mes with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course."
    play sound sfx_handjob_cream1 loop
    play voice4 samiya_moans6
    scene e06s04-31-mc-applying-lotion with dissolve
    pause
    scene e06s04-32-mc-applying-lotion with dissolve
    pause
    scene e06s04-33-mc-applying-lotion with dissolve
    pause
    scene e06s04-34-mc-applying-lotion with dissolve
    pause
    scene e06s04-35-mc-applying-lotion with dissolve
    pause
    stop voice4 fadeout 1.0
    stop sound fadeout 1.0
    scene e06s04-36-mc-talk-mes with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "All done."
    scene e06s04-37-mes-talk-mc with dissolve
    play voice4 min_thinking_emm noloop
    mes "Umm. I think you missed a few spots?"
    scene e06s04-38-mc-talk-mes with dissolve
    play voice2 d4s4_mclaugh noloop volume 1.5
    mc "Haha. If I start on that, I'll never get to work on my own tan."
    play sound dahlia_kiss_french1
    play voice4 min_arrogant_hm noloop
    scene e06s04-39-mes-kiss-mc with dissolve
    pause
    scene e06s04-40-mes-talk-mc with dissolve
    play voice4 min_disappointed_ehh1 noloop
    if fl_watersports is True:
        mes "Spoilsport. But I'm sure I'll get some time with my favorite teacher tonight."
    else:
        mes "Mmm. I guess I can be patient. For now. Not like I have to wait as long as Lydia is."
    scene e06s04-41-mc-smiles with dissolve
    play voice2 mc_thinking_hmm5 noloop
    pause
    play sound sfx_sand_down1 volume 1.6
    scene e06s04-42-mc-dives with dissolve
    pause
    play sound sfx_water_run1
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound2 sfx_water_out1 volume 2.0 noloop
    scene e06s04-43-mc-swimming with dissolve
    stop sound fadeout 1.0
    pause
    scene e06s04-44-mes-notice-arj-sy with dissolve
    pause
    play sound ["<silence 0.3>", sfx_camera_fly1] volume 2.0
    scene e06s04-a44-glambot-1 with dissolve
    pause
    scene e06s04-45-mes-talk-arj-sy with dissolve
    play voice4 min_hey_greeting noloop
    mes "Hey you two."
    scene e06s04-46-arj-talk-sy with dissolve
    play voice5 amrose_thinking_hmm5 noloop
    arj "Hello Min."
    scene e06s04-47-sy-talks with dissolve
    play voice3 stacy_happy_wooh1 noloop
    sy "Cannonball!"
    play sound sfx_sand_down1 volume 1.6
    scene e06s04-48-sy-jumps with dissolve
    pause
    play sound sfx_water_run1
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound2 sfx_water_out1 volume 2.0 noloop
    scene e06s04-49-mes-talk-arj with dissolve
    play voice4 min_happy_relief noloop
    mes "Well, we certainly know who the wild card of the bunch is."
    scene e06s04-50-arj-talk-mes with dissolve
    play voice5 amrose_arrogant_huh1 noloop
    arj "I thought it might be you, Min."
    scene e06s04-51-mes-talk-arj with dissolve
    play voice4 min_arrogant_heh1 noloop
    mes "Me? Never. If anything, I'm Chaotic Lawful."
    scene e06s04-52-mes-talk-arj with dissolve
    play voice4 min_surprised_ehh2 noloop
    mes "Stacy, on the other hand, is completely Chaotic Neutral."
    scene e06s04-53-arj-talk-mes with dissolve
    play voice5 amrose_happy_laugh1 noloop
    arj "Absolutely."
    scene e06s04-54-mc-talk-sy with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "One of these days, you're going to hurt yourself pulling something like that."
    play voice3 stacy_arrogant_ha2 noloop
    play sound sfx_water_run2
    scene e06s04-55-sy-splashes-mc with dissolve
    stop sound fadeout 3.0
    play voice2 mc_angry_errr2 noloop
    pause
    scene e06s04-56-sy-talk-mc with dissolve
    play voice3 stacy_yes_fine3 noloop
    sy "Okay \"dad\"."
    scene e06s04-57-sy-talk-mc with dissolve
    sy "You know I'm not a little girl anymore, [mcname]."
    sy "I can take care of myself."
    scene e06s04-58-mc-talk-sy with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "I think that's exactly what you said before you wiped out your first time on a skateboard."
    scene e06s04-59-sy-talk-mc with dissolve
    play voice3 stacy_yes_yap1 noloop
    sy "Yup. By 'take care of myself', I mean I know I'll always have someone to help me when I screw up."
    play voice3 stacy_suckmoan3 noloop
    play voice2 d1s1_mmm noloop
    play sound maria_kiss2
    play sound2 sfx_water_dive1 noloop
    scene e06s04-60-sy-kiss-mc with dissolve
    pause
    scene e06s04-61-arj-talk-mes with dissolve
    play voice5 amrose_thinking_hmm3 noloop
    arj "So, Stacy and I will share a room. And then you and Lydia have your own rooms."
    scene e06s04-62-arj-talk-mes with dissolve
    play voice5 amrose_arrogant_huh4 noloop
    arj "How did you swing a room? Did [mcname] decide that?"
    scene e06s04-63-mes-talk-arj with dissolve
    play voice4 min_no_nope noloop
    mes "Nope. I called dibs when I moved in."
    scene e06s04-64-arj-talk-mes with dissolve
    play voice5 amrose_thinking_emm noloop
    arj "Well, that's not really fair, is it?"
    scene e06s04-65-mes-talk-arj with dissolve
    play voice4 min_disappointed_mph noloop
    mes "Fairest thing in the world. Everyone knows international dibs rules."
    scene e06s04-66-mes-talk-arj with dissolve
    play voice4 min_old_hmm noloop
    mes "I guess in this case, it was more a perk of being Lydia's best friend. She wanted to come to me first after she got out of jail."
    scene e06s04-67-arj-talk-mes with dissolve
    play voice5 amrose_thinking_oh1 noloop
    arj "I see."
    scene e06s04-68-mes-talk-arj with dissolve
    play voice4 min_happy_mmm noloop
    mes "But it's not all bad, I'm sure most nights we will all fall asleep curled up around [mcname] in whatever room the fun starts in."
    scene e06s04-69-arj-talk-mes with dissolve
    play voice5 amrose_thinking_hmm2 noloop
    arj "Mmm. That doesn't sound bad."
    play sound sfx_water_swim1
    scene e06s04-70-arj-mes-looks-mc-sy with dissolve
    play voice3 stacy_arrogant_hmm1 noloop
    pause
    stop sound fadeout 3.0
    scene e06s04-71-mes-talk-arj with dissolve
    play voice4 min_thinking_hmm3 noloop
    mes "You know... I brought all my bondage gear with me."
    scene e06s04-72-mes-talk-arj with dissolve
    play voice4 min_old_laugh noloop
    mes "If Stacy ever gives you trouble, we can tie her up in the basement."
    scene e06s04-73-arj-sy-chuckles with dissolve
    play voice5 amrose_happy_laugh3 noloop
    arj "Hehehe."

    jump e06s04_drinks

label e06s04_drinks:

    scene e06s04-74-time-passes with Fade(0.5, 0.5, 0.5)
    pause
    scene e06s04-75-lc-talks with dissolve
    play voice3 lydia_lydwow noloop
    lc "Now the welcoming party is in full swing."
    play sound sfx_water_floatup1
    scene e06s04-76-group-gather with dissolve
    pause
    scene e06s04-77-lc-looks-mc with dissolve
    pause
    scene e06s04-78-lc-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    lc "Hello Mr. Temptation."
    scene e06s04-79-lc-talk-mc with dissolve
    lc "Honey... it is getting harder and harder for me to wait till we're married."
    scene e06s04-80-mc-talk-lc with dissolve
    play voice2 d9s2_mcyes noloop volume 2.0
    mc "I know, sweetie. Don't worry, with everyone fully moved in, I'm sure I'll be kept busy."
    scene e06s04-81-lc-talk-mc with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    lc "Mmhmm. Thank god I'll at least be able to have some fun of my own watching you and the others until the big day."
    play sound sfx_drink_loop1 loop volume 3.0
    scene e06s04-82-sy-drinks with dissolve
    pause
    stop sound fadeout 1.0
    scene e06s04-83-arj-talk-lc with dissolve
    play voice4 amrose_happy_yeah1 noloop
    arj "Thank you, Lydia."
    play voice5 stacy_surprised_wow1 noloop
    scene e06s04-84-sy-talk-lc with dissolve
    sy "Wow. That's actually not bad at all, Lydia. You could give Iona a run for her money."
    scene e06s04-85-lc-talk-sy with dissolve
    play voice3 lydia_laugh noloop
    lc "Growing up, I was my parents' darling little helper."
    scene e06s04-86-lc-talk-sy with dissolve
    lc "But now I get to help those I chose."
    scene e06s04-87-mc-talk-lc with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "Cheers to that."
    scene e06s04-88-drinks-up with dissolve
    pause
    scene e06s04-89-drinks-up with dissolve
    pause
    play sound sfx_drink_loop1 loop volume 3.0
    play sound2 [gulp, "<silence 0.3>"]
    scene e06s04-90-lc-drinks with dissolve
    pause
    scene e06s04-91-arj-drinks with dissolve
    pause
    scene e06s04-92-mc-drinks with dissolve
    pause
    stop sound fadeout 1.5
    stop sound2 fadeout 1.5

    jump e06s04_later

label e06s04_later:

    scene e06s04-93-time-passes with Fade(0.5, 0.5, 0.5)
    queue sound sfx_handjob_cream1 loop
    pause
    scene e06s04-94-mes-talk-mc with dissolve
    play voice4 min_disappointed_off noloop
    mes "We will have to remember this day as the official start of your harem, [mcname]."
    scene e06s04-95-mc-talk-mes with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "You're right. Shit. I should have prepared something to honor the day."
    scene e06s04-96-arj-talk-mc with dissolve
    play voice5 amrose_no_nah noloop
    arj "It's alright, [mcname]. You've been busy with the wedding."
    scene e06s04-97-sy-talk-lc with dissolve
    play voice4 stacy_thinking_hmm4 noloop
    sy "I gotta ask you something, Lydia."
    scene e06s04-98-lc-talk-sy with dissolve
    play voice3 lydia_aga noloop
    lc "Of course, Stacy."
    scene e06s04-99-sy-talk-lc with dissolve
    play voice4 stacy_laugh4 noloop
    sy "You still have no jitters about all this? Having us all live here, and each of us getting our brains fucked to oblivion by the lucky stallion here."
    stop sound fadeout 1.0
    scene e06s04-100-arj-talk-lc with dissolve
    play voice5 amrose_yes_yeah4 noloop
    arj "I was also a little curious. Once upon a time, I had to get to the point of accepting I would have to share him."
    scene e06s04-101-arj-talk-lc with dissolve
    arj "Meeting Stacy helped. But you and I are very different."
    play sound sfx_handjob_cream1 loop fadein 1.0
    scene e06s04-102-lc-talk-arj with dissolve
    play voice3 lydia_lydyes noloop
    lc "Of course, I'm alright with it. I love [mcname] with all my heart, and nothing gets me more excited than seeing him fuck other girls."
    scene e06s04-103-sy-talk-lc with dissolve
    play voice4 stacy_mmm2 noloop
    sy "But you still want him to fuck you one day, right?"
    scene e06s04-104-lc-talk-sy with dissolve
    play voice3 lydia_moan1 noloop
    lc "One day, I want him to do everything he's been wanting to do to me since we met."
    lc "And of course, I'll probably want him to do everything he's done to all of you as well."
    stop sound fadeout 1.0
    scene e06s04-105-mc-talks with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Yoza!"
    scene e06s04-106-mes-talks with dissolve
    play voice5 min_disappointed_ehh2 noloop
    mes "With that mindset, I wonder which one of us will have the first bun in the oven."
    scene e06s04-107-sy-talks with dissolve
    play voice4 stacy_thinking_well1 noloop
    sy "I want to be first. That is definitely at the top on my bucket list."
    scene e06s04-109-lc-giggle with dissolve
    play voice3 dahlia_happy_laugh6 noloop
    lc "Hehehe."
    scene e06s04-108-arj-giggle with dissolve
    play voice5 amrose_happy_laugh6 noloop
    arj "Hahaha."
    play sound sfx_hands_clap4
    scene e06s04-110-arj-talk-mc with dissolve
    play voice5 amrose_arrogant_hmm2 noloop
    arj "All done."
    scene e06s04-111-lc-talk-mc with dissolve
    play voice3 lydia_thinking noloop volume 1.7
    lc "It will happen at the right moment."
    scene e06s04-112-lc-talk-mc with dissolve
    lc "But each day before the wedding is going to feel like torture."
    scene e06s04-113-lc-talk-mc with dissolve
    play voice3 lydia_oof noloop
    lc "I cannot wait to give you my virginity, [mcname]."
    scene e06s04-114-mc-talk-lc with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "It's going to be an amazing moment, my love."
    mc "I'll take you for the first time, and then shower you with pleasure while I fuck everyone else here."
    scene e06s04-115-arj-talk-lc with dissolve
    play voice5 amrose_hey_whisper noloop
    arj "I'd love to help out with the wedding."
    scene e06s04-116-lc-talk-arj with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    lc "Really?"
    scene e06s04-117-arj-talk-lc with dissolve
    play voice5 amrose_yes_ugu noloop
    arj "Of course. It will be like helping out my sister, I'd love to, Lydia."
    scene e06s04-118-mc-talk-arj-lc with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "There are a few things to work out."
    scene e06s04-119-sy-talk-lc with dissolve
    play voice4 stacy_yes_yeah2 noloop
    sy "Yeah. Who is running this shebang anyway?"
    scene e06s04-120-lc-talk-sy with dissolve
    play voice3 lydia_haha noloop
    lc "I think the most important missing piece is an officiant. It has to be someone we trust."
    scene e06s04-121-mes-talk-lc with dissolve
    play voice5 min_old_laugh noloop
    mes "And someone who won't freak out knowing that it's a wedding that includes an existing polyamorous harem."
    scene e06s04-122-lc-talk-mes with dissolve
    play voice3 dahlia_yes_aga noloop
    lc "Exactly. There are some libertine people around town, but not many are church folks."
    scene e06s04-123-mc-thinks with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Hmmm."
    scene e06s04-124-sy-talk-mc with dissolve
    play voice4 stacy_thinking_hmm3 noloop
    sy "What about Lyssa?"
    scene e06s04-125-mc-talk-sy with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "There is a thought."
    scene e06s04-126-sy-talk-mc with dissolve
    play voice4 stacy_yes_ugu1 noloop
    sy "She could totally do it. She's a lawyer she knows the legal side of things, and she told me once that she's a certified minister."
    sy "I think she even officiated a wedding for some of her friends."
    scene e06s04-127-mc-talk-lc with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Is that alright with you, my darling?"
    scene e06s04-128-lc-talk-mc with dissolve
    play voice3 dahlia_yes_ugu noloop
    lc "As long as we get to say our own vows, Lyssa sounds perfect for the job."
    scene e06s04-129-mc-talk-lc with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Great, I'll call her later today."
    scene e06s04-130-mes-talk-lc with dissolve
    play voice5 min_thinking_oh noloop
    mes "I can lend a hand as well. I know a delightful place close by that makes amazing cakes."
    scene e06s04-131-mes-talk-lc with dissolve
    mes "And I think I remember some of the details you always wanted for your big day, Lydia."
    play sound sfx_hands_clap2
    play sound4 ["<silence 0.06>", sfx_hands_clap1] noloop
    scene e06s04-132-lc-talk-mes with dissolve
    play voice3 lydia_huh2 noloop
    lc "You're the best!"
    scene e06s04-133-arj-talk-lc with dissolve
    play voice4 amrose_thinking_hmm1 noloop
    arj "Well, if the cake is taken, I'm sure I can handle decorations. Where are you two planning to have the event?"
    scene e06s04-134-mc-talk-lc with dissolve
    play voice2 mc_pain_ou1 noloop
    mc "Oh shoot. I didn't find a venue yet."
    scene e06s04-135-lc-talk-mc with dissolve
    play voice3 dahlia_no_nah noloop
    lc "We don't need one. We can have it right here."
    scene e06s04-136-mc-talk-lc with dissolve
    play voice2 mc_angry_huh2 noloop volume 1.4
    mc "You're serious, aren't you?"
    scene e06s04-137-lc-talk-mc with dissolve
    play voice3 lydia_lydiahey noloop
    lc "We don't need a big spot or some fancy place with a fancy name."
    scene e06s04-138-lc-talk-mc with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    lc "We just need a place where the whole harem can witness our wonderful day."
    lc "Right?"
    scene e06s04-139-mc-talk-lc with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Absolutely!"
    play sound dahlia_kiss_french1
    play sound2 sfx_cloth_rustling1 noloop
    scene e06s04-140-mc-kiss-lc with dissolve
    play voice3 lydia_haha noloop
    pause
    scene e06s04-141-mes-talk-mc with dissolve
    play voice5 min_happy_yay noloop
    mes "Great, looks like we've got things all settled. I'll create a binder so we don't lose track of anything."
    scene e06s04-142-mc-talk-lc with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "If you change your mind about having the wedding here, or you want anything else, just tell me."
    scene e06s04-143-lc-talk-mc with dissolve
    play voice3 lydia_uhuh noloop
    lc "All I need is you, [mcname]. Everything else will fall into place, I know it will. I love you, darling."
    $ unlock_gallery_slot("cg", "e06s04")
    scene e06s04-144-mc-talk-lc with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I love you, sweetheart."
    if date_dd is True:
        scene e06s04-145-sy-talk-mc with dissolve
        play voice4 stacy_angry noloop
        sy "I can't believe it, the wedding is coming up very shortly and we haven't planned out a bachelor party for [mcname]!"
        scene e06s04-146-mes-talk-sy with dissolve
        play voice5 min_arrogant_huh2 noloop
        mes "Isn't every day of his life a bachelor party?"
        scene e06s04-147-sy-talk-mes with dissolve
        play voice4 stacy_hey_angry1 noloop
        sy "Traditions exist for a reason. Just because [mcname] has all of us doesn't mean we should skip an important moment like this."
        scene e06s04-148-arj-talk-sy with dissolve
        play voice3 amrose_happy_laugh2 noloop
        arj "I'm sure he wouldn't say no to a special surprise that doesn't include a cock cage."
        scene e06s04-149-mes-talk-sy with dissolve
        play voice5 min_thinking_hmm2 noloop
        mes "Sounds like you're volunteering to take over this part of the planning Stacy."
        scene e06s04-150-sy-talk-mes with dissolve
        play voice4 stacy_thinking_hm1 noloop
        sy "Totally. I can put something together. No problem."
        scene e06s04-151-arj-talk-sy with dissolve
        play voice3 amrose_arrogant_huh2 noloop
        arj "You don't have to do it alone. In fact, I know a girl that I think would be perfect for the main event. She's always the best and makes a party really shine."
        scene e06s04-152-sy-talk-arj with dissolve
        play voice4 stacy_happy_yay2 noloop
        sy "Thanks Amrose."

    stop music fadeout 3.5
    stop sound3 fadeout 3.0
    jump e06s05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
