image e11s07-a121-1 = Movie(play = "images/E-11/s07/anim/e11s07-a121-01-2x-50fps.webm", start_image = "e11s07-a121-01 dd-blowjob-anim-121-01-00_i")
image e11s07-a121-2 = Movie(play = "images/E-11/s07/anim/e11s07-a121-02-2x-50fps.webm", start_image = "e11s07-a121-02 dd-blowjob-anim-121-02-00_i")
image e11s07-a121-3 = Movie(play = "images/E-11/s07/anim/e11s07-a121-03-2x-50fps.webm", start_image = "e11s07-a121-03 dd-blowjob-anim-121-03-00_i")

image e11s07-a137-1 = Movie(play = "images/E-11/s07/anim/e11s07-a137-01-2x-50fps.webm", start_image = "e11s07-a137-01 dd-blowjob-anim-137-01-00_i")
image e11s07-a137-2 = Movie(play = "images/E-11/s07/anim/e11s07-a137-02-2x-50fps.webm", start_image = "e11s07-a137-02 dd-blowjob-anim-137-02-00_i")
image e11s07-a137-3 = Movie(play = "images/E-11/s07/anim/e11s07-a137-03-2x-50fps.webm", start_image = "e11s07-a137-03 dd-blowjob-anim-137-03-00_i")
image e11s07-a137-4 = Movie(play = "images/E-11/s07/anim/e11s07-a137-04-2x-50fps.webm", start_image = "e11s07-a137-04 dd-blowjob-anim-137-04-00_i")

image e11s07-a08-glam = Movie(play = "images/E-11/s07/anim/e11s07-a08-2x-50fps.webm", start_image = "e11s07-a08 alt-angle-dd-glambot-8-000_i", image = "e11s07-a08 alt-angle-dd-glambot-8-109_i", loop = False)

label e11s07:

    $ renpy.music.set_volume(0.6, 3.0, "sound3")
    scene e11s07-01-mc-talk with dissolve
    pause
    play voice2 mc_pain_cough2 noloop
    mc "Ahem."
    scene e11s07-02-mc-talk-ly with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "And you know the rest. That's the most of the story. I warned you it was long."
    scene e11s07-03-ly-talk-mc with dissolve
    play voice3 girl28_surprised_wow noloop
    ly "I'm happy you told it to me though! Wow... I had no idea you and Mom had done so much."
    scene e11s07-04-mc-talk-ly with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "We did. We did and saw a lot."
    mc "But your Mom and I, we've always known that you were the greatest thing we ever did."
    scene e11s07-05-ly-talk-mc with dissolve
    play voice3 girl28_scared_oh2 noloop
    ly "Dad you're going to make me blush!"
    scene e11s07-06-mc-talk-ly with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "Isn't it a Dad's job to embarrass his kid?"
    scene e11s07-a08 alt-angle-dd-glambot-8-000_i with dissolve
    play voice3 girl28_happy_mmm2 noloop
    pause
    $ renpy.music.set_volume(0.6, 0.0, "music")
    play music first_impression
    play sound ["<silence 0.2>", sfx_camera_fly1] volume 2.0
    scene e11s07-a08-glam
    pause
    stop sound fadeout 1.5
    scene e11s07-09-mc-talk with dissolve
    play voice2 mc_surprised_huh3 noloop
    mc "Holy shit!"
    scene e11s07-10-ly-talk-dd with dissolve
    play voice3 girl28_happy_wooh1 noloop
    ly "Mom!"
    play sound sfx_bed_slide2
    scene e11s07-11-dd-talk-ly with dissolve
    play voice4 daisy_hey noloop
    dd "Hey Lily!"
    play sound sfx_cloth_rustling2
    scene e11s07-12-ly-hug-dd with dissolve
    play voice3 girl28_happy_relief1 noloop
    pause
    $ renpy.music.set_volume(0.45, 8.0, "music")
    scene e11s07-13-ly-talk-dd with dissolve
    play voice3 girl28_surprised_eeh noloop
    ly "It's so good to see you Mom."
    scene e11s07-14-dd-talk-ly with dissolve
    play voice4 daisy_aga noloop
    dd "It's good to see you too sweetie."
    scene e11s07-15-mc-talk-dd with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "I'm happy you made it Daisy."
    scene e11s07-16-dd-talk-mc with dissolve
    play voice4 daisy_haha noloop
    dd "Did you ever doubt me?"
    scene e11s07-17-mc-talk-dd with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "You doubted you! You made it sound like you wouldn't be able to make it."
    scene e11s07-18-dd-talk-mc with dissolve
    play voice4 daisy_thinking noloop
    dd "I didn't think I was going to be able to but I did."
    scene e11s07-19-dd-talk-ly with dissolve
    play voice4 daisy_impressed noloop
    dd "Sorry sweetie, I had a work thing come up. Had to stay and deal with it."
    scene e11s07-20-ly-talk-dd with dissolve
    play voice3 girl28_yes_yeah3 noloop
    ly "That's okay Mom, you made it and that's what matters!"
    scene e11s07-21-dd-talk-ly with dissolve
    play voice4 daisy_oof noloop
    dd "How could I miss a chance to visit my daughter at uni!"
    scene e11s07-22-dd-talk-ly with dissolve
    play voice4 lydia_thinking noloop
    dd "The best university around, too."
    dd "Plus, I can visit Aunt Dahlia while I'm here."
    scene e11s07-23-ly-talk-dd with dissolve
    play voice3 girl28_surprised_oh noloop
    ly "Oh yeah! I forget she lives here sometimes."
    scene e11s07-21-dd-talk-ly with dissolve
    play voice4 dahlia_thinking_mmm1 noloop
    dd "She's super busy these days, but she can always make time for me and you."
    scene e11s07-24-mc-talk-dd with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "What about me?"
    scene e11s07-25-dd-talk-mc with dissolve
    play voice4 dahlia_happy_hmm2 noloop
    dd "I know she doesn't hate you? But I think it's because we're a package deal."
    scene e11s07-26-mc-inner-talk with dissolve
    play voice2 d1s1_mmm noloop
    mct "Now that I think about it... When was the last time I talked to Dahlia?"
    scene e11s07-27-ly-talk-dd with dissolve
    play voice3 girl28_hey_active noloop
    ly "How did you get here so fast? I remember Dad saying the tickets were almost sold out."
    scene e11s07-28-ly-talk-dd with dissolve
    play voice3 girl28_surprised_huh noloop
    ly "Wait, did you get a private flight here!?"
    scene e11s07-29-dd-talk-ly with dissolve
    play voice4 dahlia_yes_ugu noloop
    dd "Yes, I did."
    scene e11s07-30-ly-talk-dd with dissolve
    play voice3 girl28_happy_wooh2 noloop
    ly "Holy shit Mom, that's so cool!"
    scene e11s07-31-mc-talk with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "Shall we sit back down?"
    scene e11s07-32-dd-talk-mc with dissolve
    play voice4 dahlia_yes_yeah4 noloop
    dd "Yeah!"
    play sound sfx_cloth_rustling1
    scene e11s07-33-dd-talk-ly with dissolve
    play voice4 daisy_laugh noloop volume 1.7
    dd "Lily, you picked a good restaurant. Dahlia says the food here is delicious."
    scene e11s07-34-ly-talk-dd with dissolve
    play voice3 girl28_yes_yap3 noloop
    ly "Thanks Mom."
    scene e11s07-35-dd-talk-ly with dissolve
    play voice4 dahlia_happy_hmm1 noloop
    dd "So what did I miss?"
    scene e11s07-36-ly-talk-dd with dissolve
    play voice3 girl28_arrogant_yeah2 noloop
    ly "Dad just finished telling me all about your Bucket List Adventures!"
    scene e11s07-37-dd-talk-mc with dissolve
    play voice4 amrose_old_haha2 noloop
    dd "I hope he didn't tell you {i}all{/i} about it."
    scene e11s07-38-mc-talk-dd with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "I definitely skipped over some parts. And some specifics."
    scene e11s07-39-dd-talk-mc with dissolve
    play voice4 daisy_aga noloop
    dd "Good, I'm not sure I need my daughter knowing about our elevator escapades."
    scene e11s07-38-mc-talk-dd with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I may have mentioned a little bit about that."
    scene e11s07-41-dd-talk-mc with dissolve
    play voice4 dahlia_thinking_mmm2 noloop
    dd "Wh- Okay, well as long as she doesn't know about our mountaintop mounting!"
    scene e11s07-40-mc-talk-dd with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Uhhhh..."
    scene e11s07-51-dd-talk-mc with dissolve
    play voice4 dahlia_surprised_huh2 noloop
    dd "What parts didn't you tell her!?"
    scene e11s07-49-mc-talk-dd with dissolve
    play voice2 d2s12_emmm noloop
    mc "She doesn't know about our gondola gone gonzo!"
    scene e11s07-42-ly-talk with dissolve
    play voice3 girl28_hey_angry noloop
    ly "DAD! MOM! STOP!"
    scene e11s07-43-ly-talk with dissolve
    play voice3 girl28_arrogant_huh1 noloop
    ly "We are in public you know!"
    scene e11s07-44-dd-talk-mc with dissolve
    play voice4 daisy_yes noloop
    dd "Never stopped us before!"
    scene e11s07-45-ly-talk with dissolve
    play voice3 girl28_angry_grrr noloop
    ly "Oh. My. God. I'm going to die."
    scene e11s07-46-dd-talk-ly with dissolve
    play voice4 dahlia_arrogant_pff noloop
    dd "Oh pssshhh, you'll be fine. They know how to fix that now."
    scene e11s07-49-mc-talk-dd with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh! I never actually finished the story."
    mc "All of those papers I signed were for some experimental surgery that they said might work."
    scene e11s07-38-mc-talk-dd with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "And it worked. They were amazed, the doctors actually did a whole write up about the surgery."
    scene e11s07-47-dd-talk-ly with dissolve
    play voice4 dahlia_yes_aga noloop
    dd "We also made sure when you were younger that you didn't inherit the genes that gave you the heart condition."
    scene e11s07-48-ly-talk-dd with dissolve
    play voice3 girl28_yes_yeah2 noloop
    ly "I remember. Especially when you were in the hospital. Dad had me tested like seven times to make sure."
    scene e11s07-49-mc-talk-dd with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "I was nervous at the time. I just wanted to make sure you were healthy."
    scene e11s07-50-ly-talk-mc with dissolve
    play voice3 girl28_happy_mmm1 noloop
    ly "I know Dad."
    scene e11s07-51-dd-talk-mc with dissolve
    play voice4 daisy_impressed noloop
    dd "I know I've said it before, but I can't thank you enough for everything you did for me."
    scene e11s07-52-mc-talk-dd with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "I was happy to do it, love."
    scene e11s07-53-dd-talk-mc with dissolve
    play voice4 daisy_thinking noloop
    dd "Did we ever go to this restaurant while we were in school?"
    scene e11s07-54-mc-talk-dd with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "I don't... Think we did?"
    play voice4 dahlia_thinking_hmm4 noloop
    dd "Huh. I know I heard about you at this restaurant though."
    scene e11s07-55-ly-talk-dd with dissolve
    play voice3 girl28_surprised_what noloop
    ly "What the hell does that mean."
    scene e11s07-56-mc-talk-ly with dissolve
    play voice2 mc_hey_hey4 noloop
    mc "Language young lady!"
    scene e11s07-57-dd-talk-ly with dissolve
    play voice4 daisy_haha noloop
    dd "It means your Dad was a troublemaker in college."
    scene e11s07-58-ly-talk with dissolve
    play voice3 girl28_arrogant_hmm1 noloop
    ly "When you two get together, I swear."
    scene e11s07-59-dd-talk-ly with dissolve
    play voice4 daisy_ugu noloop
    dd "This is just what it's like when you share your life with someone."
    scene e11s07-60-dd-mc with dissolve
    pause
    scene e11s07-61-ly-talk with dissolve
    play voice3 girl28_scared_oh1 noloop
    ly "Oh shit, I'm going to be late to class!"
    scene e11s07-62-ly-talk-dd with dissolve
    play voice3 girl28_disappointed_geh noloop
    ly "I'm sorry I have to go Mom, I wish I could spend some more time with you."
    scene e11s07-63-dd-talk-ly with dissolve
    play voice4 daisy_uhuh noloop volume 2.0
    dd "That's okay sweetie."
    play sound sfx_cloth_rustling4
    scene e11s07-64-dd-ly-hug with dissolve
    pause
    scene e11s07-65-dd-talk-ly with dissolve
    play voice4 lydia_lydiahey noloop
    dd "I should be in town until tomorrow though! We can get together when you're done today and catch up."
    scene e11s07-66-ly-talk-dd with dissolve
    play voice3 girl28_happy_great1 noloop
    ly "That sounds great Mom!"
    play sound sfx_cloth_rustling5
    scene e11s07-67-ly-mc-hug with dissolve
    play voice2 d1s1_mmm noloop
    pause
    scene e11s07-68-mc-talk-ly with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "It was great that we were able to do this."
    scene e11s07-69-ly-talk-mc with dissolve
    play voice3 girl28_yes_yeah1 noloop
    ly "I agree! And I got to learn so much about you Dad."
    scene e11s07-70-ly-talk-mc with dissolve
    play voice3 girl28_happy_mmm3 noloop
    ly "Thank you."
    scene e11s07-71-mc-talk-ly with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course."
    scene e11s07-72-ly-talk with dissolve
    play voice3 girl28_happy_relief2 noloop
    ly "I love you both."
    scene e11s07-73-ly-talk with dissolve
    play voice3 girl28_hey_bye3 noloop
    ly "I'll see you both tonight!"
    scene e11s07-74-mc-dd-wave with dissolve
    pause

    jump e11s07_mc_dd

label e11s07_mc_dd:

    scene e11s07-75-dd-mc-sit with dissolve
    pause
    scene e11s07-76-mc-look-dd with dissolve
    pause
    scene e11s07-77-dd-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    dd "What? Have I got something on my face?"
    scene e11s07-78-mc-talk-dd with dissolve
    play voice2 mc_no_no2 noloop
    mc "No, nothing like that."
    scene e11s07-79-dd-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    dd "Then what is it?"
    scene e11s07-80-mc-talk-dd with dissolve
    play voice2 d1s5b_ehhh noloop
    mc "I'm just thinking about the life we have today."
    scene e11s07-81-dd-talk-mc with dissolve
    play voice3 daisy_oof noloop volume 1.8
    dd "Oh? Reminiscing are we?"
    scene e11s07-82-mc-talk-dd with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "A little bit. Being here, with you... To think all those years ago when you asked me to run away with you."
    mc "That it would turn into this."
    scene e11s07-83-mc-talk-dd with dissolve
    play voice2 mc_happy_a1 noloop
    mc "I'm happy I said 'yes'."
    mc "Can you imagine where we'd be if things had been different?"
    scene e11s07-84-dd-talk-mc with dissolve
    play voice3 lydia_thinking noloop volume 2.0
    dd "I probably would have gotten a cushy office job, or lived off my mom's money until..."
    scene e11s07-85-dd-talk-mc with dissolve
    play voice4 dahlia_happy_hmm2 noloop
    dd "And you? Well, you'd probably be the world's greatest porn star by now!"
    scene e11s07-86-mc-talk-dd with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "That sounds like a dream come true."
    scene e11s07-87-dd-talk-mc with dissolve
    play voice3 daisy_hey noloop
    dd "Hey!"
    scene e11s07-88-mc-talk-dd with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mc "I'm kidding. I wouldn't trade anything for the life we've made together."
    scene e11s07-89-dd-talk-mc with dissolve
    play voice3 dahlia_yes_ugu noloop
    dd "I couldn't imagine doing this with anyone other than you."
    scene e11s07-90-dd-talk-mc with dissolve
    play voice3 daisy_hmm1 noloop
    dd "Except maybe that hot Italian gondola man."
    scene e11s07-91-mc-talk-dd with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "Hell, I thought about running away with him!"
    scene e11s07-92-dd-talk-mc with dissolve
    play voice3 daisy_yay noloop
    dd "Good! It means you've got a good head on your shoulders."
    dd "Exactly what I want for the father of my child."
label replay_e11s07:

    if _in_replay:
        $ renpy.music.set_volume(0.45, 0.0, "music")
        play music first_impression
        $ renpy.music.set_volume(0.6, 0.0, "sound3")
        play sound3 d12s2_cafe_crowd fadein 3.0
    scene e11s07-93-mc-talk-dd with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Well enough of that, how was your flight?"
    scene e11s07-94-dd-talk-mc with dissolve
    play voice3 daisy_aah noloop
    dd "It was good! But I am starving."
    scene e11s07-95-mc-talk-dd with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Would you like me to get the waiter so you can order?"
    scene e11s07-96-dd-talk-mc with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    dd "Do they have polish sausage here?"
    scene e11s07-97-mc-talk-dd with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "I... Don't think so?"
    scene e11s07-98-dd-talk-mc with dissolve
    play voice3 daisy_thinking noloop
    dd "That's fine. I see some in front of me."
    scene e11s07-99-dd-kiss-mc with dissolve
    play sound maria_kiss2
    pause
    scene e11s07-100-dd-talk-mc with dissolve
    play voice3 daisy_hmm2 noloop
    dd "Besides, I always wanted to have my turn with you here."
    scene e11s07-101-mc-talk-dd with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What are you-"
    play sound sfx_cloth_planket2
    scene e11s07-102-dd-under-table with dissolve
    pause
    scene e11s07-103-mc-talk-dd with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Oh- oh!"
    scene e11s07-104-dd-talk-mc with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    dd "Besides, didn't someone just say something about a pornstar dream?"
    scene e11s07-105-mc-talk-dd with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Well, yes-"
    scene e11s07-106-dd-talk-mc with dissolve
    play voice3 daisy_aga noloop
    dd "Pull out your phone, we can get your career started right now!"
    scene e11s07-107-mc-talk-dd with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I love you Daisy."
    scene e11s07-108-dd-talk-mc with dissolve
    play voice3 daisy_yes noloop
    dd "I love you too, [mcname]."
    scene e11s07-111-dd-mc with dissolve
    pause
    scene e11s07-112-mc-talk-dd with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Uhmm... I can't see anything."
    scene e11s07-113-dd-hand with dissolve
    pause
    scene e11s07-114-mc-talk-dd with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "You need to-"
    scene e11s07-115-dd-talk-mc with dissolve
    play voice3 dahlia_yes_yeah4 noloop
    dd "I know how to work a phone, hunny."
    scene e11s07-116-mc-talk-dd with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Sorry, I-"
    scene e11s07-117-mc-talk-dd with dissolve
    play voice2 mc_surprised_wow2 noloop
    mc "Woah! Someone's feeling a little aggressive today."


    $ Lovense.stop()

    play sound sfx_jeans_on1
    scene e11s07-118-dd-talk-mc with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    dd "I told you, I'm hungry. I'm planning to drain your balls. Besides, I don't think I'm the only one that's excited."
    scene e11s07-119-mc-talk-dd with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Maybe, but you need to be quiet! Otherwise we're going to get caught."
    scene e11s07-120-dd-talk-mc with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    dd "Only one way for me to be quiet."
    $ Lovense.vibrate(1)
    scene e11s07-a121-01 dd-blowjob-anim-121-01-00_i with dissolve
    pause
    $ Lovense.pattern("7;10", 1400)
    scene e11s07-a121-1
    play voice3 daisy_dlick noloop volume 3.0
    play voice3 aaleyah_sucking_deep
    play voice2 d7s4_mcbreathing
    pause
    dd "Mmmmm!"
    scene e11s07-a121-2 with dissolve
    pause
    scene e11s07-a121-3 with dissolve
    pause
    scene e11s07-124-mc-talk-dd with dissolve
    mc "God, I can already tell that you're going to suck every drop out out of my balls!"
    scene e11s07-125-wa-talk-mc with dissolve
    play voice4 boy5_surprised_eeh1 noloop
    "Waiter" "Excuse me sir."
    scene e11s07-126-mc-look-wa with dissolve
    play voice2 mc_pain_rrrr noloop
    pause
    scene e11s07-127-wa-talk-mc with dissolve
    play voice4 boy5_thinking_huh noloop
    "Waiter" "Didn't a woman just join you?"
    scene e11s07-128-mc-talk-wa with dissolve
    play voice2 d1s5b_emmm noloop
    mc "Uhm, mmm, uh, yeah!"
    scene e11s07-129-wa-talk-mc with dissolve
    play voice4 boy5_thinking_hmm3 noloop
    "Waiter" "Okay? Did she want to order something?"
    scene e11s07-130-mc-talk-wa with dissolve
    play voice2 mc_scared_oh3 noloop
    mc "I actually think she, ooooo, found something to sate her appetite!"
    scene e11s07-131-wa-talk-mc with dissolve
    play voice4 boy5_thinking_hmm2 noloop
    "Waiter" "Ohhhkay. Well, I'll just bring the check then."
    scene e11s07-132-mc-talk-wa with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "Thankssss!"
    scene e11s07-133-mc-talk-dd with dissolve
    play voice2 d1s5_orgasm noloop
    queue voice2 d7s4_mcbreathing
    mc "God Daisy, how are you so damn good at blowjobs?"
    stop voice2 fadeout 1.0
    scene e11s07-134-dd-talk-mc with dissolve
    $ Lovense.stop()
    $ Lovense.vibrate(1)
    play voice3 daisy_haha noloop
    dd "Lots of practice."
    scene e11s07-135-mc-talk-dd with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "If you keep doing that thing with your tongue, I am going to cum so fast."
    scene e11s07-136-dd-talk-mc with dissolve
    play voice3 daisy_hmm1 noloop
    dd "Good, I want my {i}dessert.{/i}"
    scene e11s07-a137-01 dd-blowjob-anim-137-01-00_i with dissolve
    pause
    $ Lovense.pattern("7;12", 1000)
    scene e11s07-a137-1
    play voice3 aaleyah_sucking_deep
    play voice2 d7s4_mcbreathing
    pause
    dd "Glllck, gllllck!"
    scene e11s07-a137-2 with dissolve
    pause
    scene e11s07-a137-3 with dissolve
    pause
    scene e11s07-a137-4 with dissolve
    pause
    scene e11s07-140-mc-talk-dd with dissolve
    mc "Holy shit Daisy. Just like that."
    scene e11s07-141-mc-talk-dd with dissolve
    mc "Fuuuck, Daisy I'm just about to-"
    if persistent.is_special is True:
        scene e11s07-142-c1-ly-talk-dd with dissolve
        play voice4 girl28_hey_sexy noloop
        ly "Dad! Where's Mom?"
        scene e11s07-143-c1-mc-talk-ly with dissolve
        play voice2 mc_pain_mff5 noloop
        mc "Oh shit! Uhm, hi, ohhhh, hi Lily!"
        scene e11s07-144-c1-ly-talk-mc with dissolve
        play voice4 girl28_disappointed_eeh1 noloop
        ly "Uhm... Hi?"
        scene e11s07-145-c1-mc-talk-ly with dissolve
        play voice2 mc_pain_ffff noloop
        mc "Your, uhmmm, Mom is, uhhhh-"
        queue voice2 mc_surprised_oof1 noloop
        mc "- In the bathroom! Oh fu- yeah! What are you, ahhh, doing back here?"
        scene e11s07-146-c1-ly-talk-mc with dissolve
        play voice4 girl28_disappointed_oof noloop
        ly "I forgot my purse."
        scene e11s07-147-c1-mc-talk-ly with dissolve
        play voice2 mc_thinking_mmm2 noloop
        mc "Ooooooh, mmmm. That makes sense."
        scene e11s07-148-c1-ly-talk-mc with dissolve
        play voice4 girl28_disappointed_mmm2 noloop
        ly "Well I'm sad I missed mom again!"
        scene e11s07-149-c1-ly-talk-mc with dissolve
        play voice4 girl28_happy_mmm1 noloop
        ly "Give mom a kiss for me, love you Dad!"
        play sound maria_kiss1
        scene e11s07-150-c1-ly-kiss-mc with dissolve
        play voice2 mc_pain_mff1 noloop
        pause
        play voice2 d1s5_orgasm2 noloop
        play voice3 nora_sucking1 noloop
        $ Lovense.stop()
        $ Lovense.vibrate(20)
        scene e11s07-151-mc-cums with vpunch
        mc "MmmmmmMMMM!"
        scene e11s07-152-c1-ly-talk-mc with dissolve
        $ Lovense.vibrate(3)
        play voice4 girl28_surprised_huh noloop
        ly "You okay Dad? You're acting weird."
        scene e11s07-153-c1-mc-talk-ly with dissolve
        play voice2 mc_yes_yeah5 noloop
        mc "Yeah sweetie, I'm... Totally fine."
        scene e11s07-154-c1-ly-talk-mc with dissolve
        play voice4 girl28_disappointed_eeh2 noloop
        ly "Suuuure. But I am going to be so late, I need to go. Bye Dad!"
    else:
        scene e11s07-155-c2-wa-talk-mc with dissolve
        play voice4 boy5_disappointed_hmm noloop
        "Waiter" "Sir, your check."
        scene e11s07-156-c2-mc-talk-wa with dissolve
        play voice2 mc_pain_ou1 noloop
        mc "Oh shit! Uhm, hi, ohhhh, thanks!"
        scene e11s07-157-c2-mc-talk-wa with dissolve
        play voice2 mc_pain_mff5 noloop
        mc "Ka-keep the change!"
        scene e11s07-158-c2-wa-talk-mc with dissolve
        play voice4 boy5_yes_aga noloop
        "Waiter" "Thank you sir."
        scene e11s07-159-c2-wa-talk-mc with dissolve
        play voice4 boy5_happy_mmm1 noloop
        "Waiter" "Thank you for dining in today."
        play voice2 d1s5_orgasm2 noloop
        play voice3 nora_sucking1 noloop
        $ Lovense.stop()
        $ Lovense.vibrate(17)
        scene e11s07-151-mc-cums with vpunch
        pause
        play voice2 d1s5_orgasm noloop
        $ Lovense.vibrate(18)
        scene e11s07-160-c2-mc-talk with vpunch
        mc "MmmmmmMMMMHMM!"
        scene e11s07-161-c2-wa-talk-mc with dissolve
        $ Lovense.vibrate(3)
        play voice4 boy5_arrogant_hm noloop
        "Waiter" "We hope you come again soon."
        scene e11s07-162-c2-mc-talk-wa with dissolve
        play voice2 mc_yes_yeah5 noloop
        mc "Yeah, I, uhh, do too."
        scene e11s07-163-c2-wa-weird-look with dissolve
        pause

    play sound sfx_cloth_planket2
    scene e11s07-163-dd-talk-mc with dissolve
    $ Lovense.vibrate(1)
    play voice3 lissa_ha noloop
    dd "I still got it."
    scene e11s07-164-mc-talk-dd with dissolve
    play voice2 mc_scared_oh2 noloop
    mc "Holy shit you do. That might have been the best blowjob you've ever given me."

    $ Lovense.stop()


    $ renpy.end_replay()
    scene e11s07-165-dd-talk-mc with dissolve
    play voice3 lydia_thinking noloop volume 1.5
    dd "Good."
    play sound sfx_skirt_off2
    scene e11s07-166-dd-talk-mc with dissolve
    play voice3 daisy_haha noloop
    dd "I had fun too."
    scene e11s07-167-mc-talk-dd with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "How does the video look?"
    scene e11s07-168-dd-talk-mc with dissolve
    play voice3 daisy_aah noloop
    dd "Oh, I totally record that."
    scene e11s07-169-dd-talk-mc with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    dd "But that's okay! Because I realized that there's a bunch of places around town that I want to have sex at."
    scene e11s07-170-dd-talk-mc with dissolve
    play voice3 lydia_oops noloop volume 0.8
    dd "Oooo! Maybe we should start a new list. Like \"places to have sex\"! That would be fun."
    scene e11s07-171-mc-talk-dd with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "I think that sounds like a great idea."
    scene e11s07-172-dd-talk-mc with dissolve
    play voice3 daisy_yay noloop
    dd "Well {i}come{/i} on then! We don't have any time to lose!"
    $ unlock_gallery_slot("scene", "e11s07")
    scene e11s07-173-mc-smile with dissolve
    pause
    scene e11s07-174-dd-talk-mc with dissolve
    play voice3 daisy_impressed noloop
    dd "Well, what are you waiting for?"
    play sound sfx_bed_slide3 volume 0.6
    scene e11s07-175-mc-talk-dd with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Absolutely nothing. Let's go!"
    $ unlock_gallery_slot("cg", "e11s01")
    scene e11s07-176-glamour-shot with dissolve
    pause
    stop sound3 fadeout 3.0
    $ renpy.music.set_volume(1.0, 4.0, "music")
    play sound sfx_camera_fly1 volume 2.0
    scene ending_11_art_2 with Fade(1.25, 1.0, 1.75, color="#fff")
    pause
    call end_game_text (_("You have finished playing Ending #11!")) from _call_end_game_text_12
    $ persistent.finished_e11 = True
    $ fl_achievement_unlock("e11_finish")

    stop sound fadeout 1.0
    stop music fadeout 3.0
    jump end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
