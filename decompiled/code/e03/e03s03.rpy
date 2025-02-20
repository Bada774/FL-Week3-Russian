image e03s03-a172-glambot-1 = Movie(play = "images/E-03/s03/anim/e03s03-a172-2x-50fps.webm", start_image = "e03s03-a172 sy-talk-mc-glambot-172-000_i", image = "e03s03-a172 sy-talk-mc-glambot-172-179_i", loop = False)

label e03s03:

    $ renpy.music.set_volume(0.75, 3.0, "music")
    $ renpy.music.set_volume(1.0, 3.0, "music2")
    scene black
    show screen scene_transistion(_("The next day"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene e03s03-01-mh-talk-mc-sy
    with Fade(0.5, 0.5, 0.5)
    play music music_investigation_preparations fadein 1.0
    play voice4 dahlia_disappointed_ehh2 noloop
    mh "Are you both ready for this?"
    scene e03s03-02-sy-talk-mh with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    sy "Maybe? I've never tried to infiltrate a cult before."
    scene e03s03-03-mc-talk-mh with dissolve
    play voice2 mc_happy_a1 noloop
    mc "I mean... it can't be that tough, right?"
    scene e03s03-04-mh-talk-mc-sy with dissolve
    play voice4 dahlia_disappointed_hmm2 noloop
    mh "Just, keep your guards up, okay? This might take some... unexpected turns."
    scene e03s03-05-sy-talk-mh with dissolve
    play voice3 stacy_hey noloop
    sy "Don't you worry, Lyssa. We got this! You're super smart, and with that camera we'll be home before dinner!"
    scene e03s03-06-mh-talk-sy with dissolve
    play voice4 dahlia_arrogant_yeah noloop
    mh "I hope so... {w} Speaking of, how does the camera look?"
    play sound sfx_cloth_rustling1 volume 0.5
    scene e03s03-07-sy-mc-lean with dissolve
    play voice3 stacy_surprised_oh1 noloop
    sy "Wow... You can't even tell it's there!"
    scene e03s03-08-sy-talk-mh with dissolve
    mc "..."
    play voice3 stacy_mmm1 noloop
    sy "[mcname]?"
    scene e03s03-09-mc-expression with dissolve
    play voice2 d2s9_confused noloop
    mc "Uhm, yeah?"
    scene e03s03-10-sy-talk-mc with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    sy "You're just staring at Lyssa's tits, aren't you."
    scene e03s03-11-mc-talk-sy with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "And you're not!?"
    play sound sfx_cloth_rustling2 volume 0.5
    scene e03s03-12-sy-talk-mc with dissolve
    play voice3 stacy_angry noloop
    sy "I can multitask!"
    scene e03s03-15-mh-talk-mc-sy with dissolve
    play voice4 dahlia_disappointed_ehh1 noloop
    mh "You two are hopeless, you know that? Now, come on. We should get going."
    mh "I've arranged for a driver to drop us off. The compound is way out of town, and I don't much feel like leaving my car out there for them."
    scene e03s03-16-sy-talk-mh with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Probably a good call."
    scene e03s03-17-mc-talk-mh with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "All right, well let's get this show on the road! I've always wanted to take down a cult."
    play sound sfx_heels_steps2 loop
    scene e03s03-18-mh-talk-mc with dissolve
    play voice4 dahlia_arrogant_heh noloop
    mh "I'm glad that we can fulfill your... dreams, [mcname]."
    scene e03s03-19-sy-talk-mh with dissolve
    play voice3 stacy_arrogant_hmm1 noloop
    if persistent.is_special is True:
        sy "I just want to be clear - he's the weirdo in the family. Most of my dreams at least make sense. Like, wanting you to fuck my ass, while [mcname]-"
    else:
        sy "I just want to be clear - he's a weirdo. Most of my dreams at least make sense. Like, wanting you to fuck my ass, while [mcname]-"
    scene e03s03-20-mh-talk-sy with dissolve
    play voice4 lissa_thinking noloop volume 1.5
    mh "Why don't we save that for after we dismantle this cult."
    scene e03s03-21-sy-talk-mh with dissolve
    play voice3 stacy_yes_fine2 noloop
    sy "Okay! Then let's go tear down a cult!"
    scene e03s03-22-mh-talk-mc with dissolve
    play voice4 lissa_haha2 noloop
    mh "Oh boy, she's really excited to infiltrate a cult we know nothing about."
    scene e03s03-23-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "You promised her that you'd fulfill one of her sexual fantasies if we bring down the cult."
    scene e03s03-24-mh-talk-mc with dissolve
    play voice4 lissa_mmm1 noloop
    mh "You're right... Let's just hope I can deliver on whatever she's dreamt up."
    play voice2 mc_thinking_mmm2 noloop
    mc "Me too."
    mh "Now come on, they're expecting us. Hate to be late on our first day."
    stop sound fadeout 1.0
    play sound2 sfx_supercar_drive1 fadein 1.0
    stop music fadeout 3.0
    scene black
    show screen scene_transistion(_("Four hours and twenty-nine minutes later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    stop sound2 fadeout 2.0
    hide screen scene_transistion
    scene e03s03-25-cult-lodge
    with Fade(0.5, 0.5, 0.5)
    queue music music_cult_hidden volume 1.5
    pause
    scene e03s03-26-cm-talk with dissolve
    play voice6 girl35_thinking_hmm1 noloop
    "Cult Member" "The High Priestess will be with you shortly."
    scene e03s03-27-sy-talk with dissolve
    play voice3 stacy_thinking_oh2 noloop
    sy "Wow. They got some nice digs here."
    scene e03s03-28-mc-talk with dissolve
    play voice2 d9s2_yeah noloop volume 2.3
    mc "You're telling me, this is definitely not what I expected for a cult."
    play voice4 dahlia_thinking_hmm1 noloop
    mh "Looks can be deceiving."
    scene e03s03-29-mc-talk with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "Ain't that the truth..."
    play sound sfx_door_open5 volume 1.4
    scene e03s03-30-noise with dissolve
    "*DOOR OPENING NOISE*"
    play sound sfx_door_closed1
    scene e03s03-31-hp-talk with dissolve
    play voice5 girl34_hey_scandalized3 noloop
    hp "Good morning, fellow travelers."
    scene e03s03-32-sy-talk-hp with dissolve
    play voice3 stacy_hey_attention1 noloop
    sy "Uhm, morning!"
    play sound sfx_heels_steps1 loop
    scene e03s03-33-mh-talk-hp with dissolve
    play voice4 dahlia_thinking_hmm2 noloop
    mh "Good morning, High Priestess."
    scene e03s03-34-hp-talk with dissolve
    play voice5 girl34_arrogant_huh1 noloop
    hp "What brings you three to my humble abode?"
    scene e03s03-35-mc-inner-talk with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "Man, this lady talks kind of funny."
    play sound sfx_cloth_rustling4
    scene e03s03-36-mh-talk-hp with dissolve
    play voice4 dahlia_thinking_oh noloop
    mh "We find ourselves... adrift in this storm of life. And we hope to seek shelter in the embrace of your... beliefs."
    scene e03s03-37-sy-talk-hp with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "Yeah, uh, what she said!"
    scene e03s03-38-hp-talk with dissolve
    play voice5 girl34_arrogant_ha4 noloop
    hp "Ahhh, more wayward souls... What about you, sir? Why are you here?"
    scene e03s03-39-mc-talk-hp with dissolve
    play voice2 d2s12_emmm noloop volume 1.4
    mc "Uhm, because I'm a, what'd you call it, wayward soul? And I need guidance."
    scene e03s03-40-hp-talk-mc with dissolve
    play voice5 girl34_thinking_eeh1 noloop
    hp "And what guidance do you seek here?"
    play voice2 d3s7_mcemm noloop
    mc "Errmmmm..."
    scene e03s03-41-mh-talk-hp with dissolve
    play voice4 dahlia_disappointed_ehh3 noloop
    mh "We seek guidance not of this world. Something that will let us rise above, become whole. Become... healed."
    scene e03s03-42-hp-talk with dissolve
    play voice5 girl34_arrogant_hm1 noloop
    hp "Then-"
    scene e03s03-43-hp-talk-mc with dissolve
    play voice5 girl34_surprised_ah2 noloop
    hp "Wait... You..."
    play sound sfx_cloth_rustling2 volume 1.4
    scene e03s03-44-hp-talk with dissolve
    play voice5 girl34_angry_ahem4 noloop
    hp "Ahem. Those who seek wisdom are welcome."
    hp "First, you must shed yourselves of this materialistic world."
    scene e03s03-45-sy-talk-hp with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "Like, give you my phone?"
    scene e03s03-46-hp-talk-sy with dissolve
    play voice5 girl34_yes_angry1 noloop
    hp "Your phone, clothes, everything. You must become detached from all that which tethers you to this plane, and blocks you from the next."
    scene e03s03-47-sy-talk with dissolve
    play voice3 stacy_disappointed_oh7 noloop
    sy "Oh..."
    scene e03s03-48-mc-inner-talk with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.3
    mct "Huh, that's a little kinky."
    scene e03s03-49-sy-talk-hp with dissolve
    play voice3 stacy_yes_okay1 noloop
    sy "I guess, we'll just... you know. Strip."
    scene e03s03-50-hp-talk with dissolve
    play voice5 girl34_yes_aga8 noloop
    hp "And we want you to leave {i}all{/i} of your worldly attachments behind."
    scene e03s03-51-mc-talk with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Shit, all of it?"
    scene e03s03-52-sy-talk-hp with dissolve
    play voice3 stacy_surprised_huh3 noloop
    sy "Including our underwear?"
    scene e03s03-53-hp-talk-sy with dissolve
    play voice5 girl34_yes_neutral1 noloop
    hp "Yes, including your underwear. You need to become naked; to this world, to us your commune, and to the spirit of everything."
    scene e03s03-54-sy-talk-hp with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "Well, that's kind of hot, lady... Whatever you want."
    play sound sfx_skirt_off2
    play sound2 sfx_jeans_fly1 noloop
    scene e03s03-55-mc-mh-sy with dissolve
    pause
    scene e03s03-56-hp-talk with dissolve
    play voice5 girl34_surprised_ohmy1 noloop
    hp "Oh my Goddess... I..."
    scene e03s03-57-hp-talk with dissolve
    play voice5 girl34_angry_ahem2 noloop
    hp "I, uhm, ahem. Now, one of your fellow members will come and collect your things, and give you your new coverings."
    play sound sfx_heels_steps1 loop
    scene e03s03-58-hp-talk with dissolve
    play voice5 girl34_happy_relief2 noloop
    hp "I need to, uhm... consult our literature. Your new friend will show you what you are going to be doing as a part of your first circle of learning."
    stop sound fadeout 1.5
    scene e03s03-59-cm-talk with dissolve
    play voice6 girl35_yes_ugu1 noloop
    "Cult Member" "I will collect your things for the cleansing, and you will don the garb of the student."
    scene e03s03-60-mc-talk-hp with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait, what's the garb of the student?"
    scene e03s03-61-sy-talk-hp with dissolve
    play voice3 stacy_huh2 noloop
    sy "And what the hell is the cleansing?"
    scene e03s03-62-cm-talk-hp with dissolve
    play voice6 girl35_thinking_hm2 noloop
    "Cult Member" "What I wear is the garb of the student. And the cleansing, well, the cleansing is the release of the material back to the material, through the most primal act we can muster."
    scene e03s03-63-mh-talk-cm with dissolve
    play voice4 dahlia_thinking_hmm3 noloop
    mh "Primal... like fire? Are you going to burn our things?" id e03s03_14941c57
    scene e03s03-62-cm-talk-hp with dissolve
    play voice6 girl35_yes_confident1 noloop
    "Cult Member" "Yes."
    scene e03s03-64-sy-talk-mh with dissolve
    play voice3 stacy_surprised_huh2 noloop
    sy "But I really like this outfit!"
    sy "And I worked hard getting us these outfits!"
    scene e03s03-65-mc-talk-sy with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Stacy!"
    scene e03s03-66-hp-cm with dissolve
    pause
    scene e03s03-67-sy-talk-cm with dissolve
    play voice3 stacy_angryhuh noloop
    sy "But, uhm, like you said. Attachments and whatever. Ugh."
    scene e03s03-68-cm-talk with dissolve
    play voice6 girl35_thinking_hmm5 noloop
    "Cult Member" "You will see the garb on your way out. Please, put it on while I collect your things."
    play sound sfx_barefoot_steps1 loop
    scene e03s03-69-mc-talk-mh with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "*whispers* Lyssa, I hope this is a {i}really{/i} good friend of yours."
    scene e03s03-70-mh-talk-mc with dissolve
    play voice4 daisy_ugu noloop
    mh "*whispers* Taking this cult will be worth it [mcname], I promise."
    stop music fadeout 3.0
    play sound sfx_door_openclosed2
    play sound4 sfx_greenhouse_ambience fadein 3.0 volume 0.8
    scene e03s03-71-cult-compound with fade
    queue music music_nordic_chopwater
    pause
    scene e03s03-72-sy-talk with dissolve
    play voice3 stacy_disgust_oh2 noloop
    sy "This thing is so fucking itchy."
    scene e03s03-73-mc-talk-sy with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "I know. Scratchy as hell."
    scene e03s03-74-mh-talk with dissolve
    play voice4 dahlia_thinking_hmm4 noloop
    mh "I want to thank you both for doing this, it means a lot."
    scene e03s03-75-mc-talk-mh with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I hope you've got a plan."
    scene e03s03-76-mh-talk-mc with dissolve
    play voice4 dahlia_yes_ugu noloop
    mh "I'm working on it, but I promise-"
    play sound sfx_footsteps_grass1 loop
    scene e03s03-77-cult-member with dissolve
    pause
    scene e03s03-78-cult-member with dissolve
    pause
    scene e03s03-79-sy-talk-mc with dissolve
    play voice3 stacy_oh2 noloop
    sy "'Ruh 'roh, [mcname]."
    play voice2 mc_pain_ou1 noloop
    mc "Oh shit!"
    stop sound fadeout 1.0
    scene e03s03-80-cm-talk-sy with dissolve
    play voice6 girl35_thinking_hmf5 noloop
    "Cult Member" "You've been given an highly honored task. You shall be providing the fuel for the cleansing."
    scene e03s03-81-sy-talk-cm with dissolve
    play voice3 stacy_arrogant_huh5 noloop
    sy "Oh! Oh that's not too shabby."
    play voice6 girl35_arrogant_hm1 noloop
    "Cult Member" "Why else do you think I had this tool for you to use?"
    scene e03s03-82-mc-talk-cm with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "Believe me, you don't want to know."
    play sound sfx_cloth_rustling2
    scene e03s03-83-cm-talk-sy with dissolve
    play voice6 girl35_thinking_hmf4 noloop
    "Cult Member" "It is your job, as the man, to carry the wood to be piled."
    scene e03s03-84-cm-talk-mh with dissolve
    play voice6 girl35_thinking_eem6 noloop
    "Cult Member" "And I have been instructed to have you watch them, to ensure they are doing the best job they can. {w}Do not allow them to slack off. If they do, there will be punishments."
    play sound sfx_footsteps_grass1 loop
    scene e03s03-85-cult-member with dissolve
    pause
    stop sound fadeout 2.0
    scene e03s03-86-sy-talk with dissolve
    play voice3 stacy_arrogant_huh4 noloop
    sy "So, we're chopping wood now?"
    scene e03s03-87-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "I guess so. We have to blend in, right? But what about the camera?"
    scene e03s03-88-mh-talk with dissolve
    play voice4 dahlia_thinking_mmm2 noloop
    mh "I guess that's gone now. We'll just have to figure something else out to prove that this cult is... nefarious."
    scene e03s03-89-mc-talk with dissolve
    play voice2 mc_thinking_hm noloop
    mc "I haven't seen anything nefarious yet."
    scene e03s03-90-sy-talk with dissolve
    play voice3 stacy_angry_breath1 noloop
    sy "Except them burning my favorite shirt."
    scene e03s03-91-mc-talk-sy with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "You have like twenty more at home of that {i}exact{/i} same shirt, Stacy."
    scene e03s03-92-sy-talk-mc with dissolve
    play voice3 stacy_yeahno noloop
    sy "Yeah, but I liked that one the most!"
    scene e03s03-93-mh-talk with dissolve
    play voice4 lissa_haha noloop
    mh "All right, quit your bickering. Come on, we need to start chopping wood or they'll get suspicious."
    scene e03s03-94-sy-talk with dissolve
    play voice3 stacy_thinking_emm4 noloop
    sy "So, should I just start chopping anything?"
    scene e03s03-95-mc-talk-sy with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "Uhm, I don't think-"
    scene e03s03-96-sy-talk with dissolve
    play voice3 stacy_arrogant_hmm2 noloop
    sy "I'm going to start with this tree!"
    scene e03s03-97-mh-talk-sy with dissolve
    play voice4 dahlia_hey_active1 noloop
    mh "Wait, Stacy-"
    play voice3 stacy_happy_wooh1 noloop
    play sound sfx_epic_jump1 volume 1.5
    play sound2 sfx_sand_run1
    scene e03s03-98-sy-talk with hpunch
    sy "TIMBER!"
    play sound sfx_axe_chop1
    stop sound2 fadeout 1.0
    scene e03s03-99-axe with hpunch
    pause
    scene e03s03-100-sy-talk with dissolve
    play voice3 stacy_surprised_ah1 noloop
    sy "Oh... Oh I think I like this..."
    play sound sfx_sand_run1 volume 4.0
    scene e03s03-101-cm-run with hpunch
    pause
    play voice6 girl35_angry_gergh noloop
    stop sound fadeout 1.0
    scene e03s03-102-cm-talk-sy with vpunch
    "Cult Member" "What are you doing!?"
    scene e03s03-103-sy-talk with dissolve
    play voice3 stacy_arrogant_huh2 noloop
    sy "Making firewood!"
    scene e03s03-104-cm-talk-sy with dissolve
    play voice6 girl35_no_angry3 noloop
    "Cult Member" "You don't need to cut down trees! We have logs ready to split over there!"
    scene e03s03-105-stump with dissolve
    play voice3 stacy_disappointed_oh3 noloop
    sy "Oh..."
    scene e03s03-107-mc-talk-cm with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Uhm, sorry about that. Someone is just, uhm, excited for her first day at cult camp!"
    scene e03s03-108-cm-talk-mc with dissolve
    play voice6 girl35_angry_cough1 noloop
    "Cult Member" "This isn't a cult! Or a camp! This is an isolated retreat where we can reconnect with nature."
    scene e03s03-109-sy-talk with dissolve
    play voice3 stacy_thinking_emm2 noloop
    sy "Kind of like a camp."
    play voice6 girl35_angry_err2 noloop
    scene e03s03-110-cm-talk-sy with vpunch
    "Cult Member" "It's not a camp!"
    scene e03s03-111-mc-talk with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "It sure sounds like a camp."
    play sound sfx_footsteps_grass1 fadein 1.0 volume 0.5
    scene e03s03-112-cm-walk with dissolve
    play voice6 girl35_arrogant_pff3 noloop
    "Cult Member" "...{w} Start splitting logs."
    stop sound fadeout 3.0
    scene e03s03-113-sy-talk with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "Does that mean... this is cult summer camp?"
    scene e03s03-114-mh-talk with dissolve
    play voice4 dahlia_arrogant_heh noloop
    mh "You two need to stop antagonizing them. We're trying to blend in, remember?"
    scene e03s03-115-mc-talk-mh with dissolve
    play voice2 mc_hey_hey8 noloop
    mc "We're not doing it on purpose!"
    scene e03s03-116-mh-talk-mc with dissolve
    play voice4 lissa_yes noloop
    mh "I know, I know. You two are just like this."
    scene e03s03-117-sy-talk-mh with dissolve
    play voice3 stacy_disappointed_oh1 noloop
    sy "You make it sound like it's a bad thing!"
    scene e03s03-118-mh-talk-sy with dissolve
    play voice4 lissa_lno noloop
    mh "It's not. I love you both exactly as you are."
    scene e03s03-119-sy-talk-mc with dissolve
    play voice3 stacy_happy_yay3 noloop
    sy "You hear that, [mcname]? Lyssa looooves us!"
    scene e03s03-120-mh-talk-sy with dissolve
    play voice4 lissa_laugh noloop
    mh "Of course I do. Now, get to chopping before that cultist comes back over here."
    scene e03s03-121-sy-talk with dissolve
    play voice3 stacy_yes_fine1 noloop
    sy "Okay. Take two!"
    play sound sfx_throw_something1
    scene e03s03-122-sy-talk with dissolve
    play voice3 stacy_arrogant_ha2 noloop
    sy "Annnnnd, hiyah!"
    play sound sfx_axe_chop2
    scene e03s03-123-axe with vpunch
    pause
    scene e03s03-124-sy-talk with dissolve
    play voice3 stacy_happy_relief1 noloop
    sy "Oh... This is going to be fun!"
    play sound sfx_throw_something1
    scene e03s03-125-montage with dissolve
    pause
    play sound sfx_axe_chop3
    $ renpy.music.set_volume(0.0, 2.0, "sound4")
    $ renpy.music.set_volume(1.6, 1.0, "music")
    scene e03s03-126-montage with fade
    pause
    scene e03s03-127-montage with dissolve
    pause
    scene e03s03-128-montage with dissolve
    pause
    scene e03s03-129-sy-firewood-mc with fade
    pause
    scene e03s03-130-water with dissolve
    pause
    scene e03s03-131-mc-firewood with dissolve
    pause
    $ renpy.music.set_volume(1.0, 3.0, "sound4")
    $ renpy.music.set_volume(0.75, 1.0, "music")
    scene e03s03-132-afternoon with dissolve
    pause
    scene e03s03-133-sy-talk with dissolve
    play voice3 stacy_angry_breath2 noloop
    sy "Fuck, I'm tired..."
    scene e03s03-134-mc-talk with dissolve
    play voice2 mc_disgust_meh4 noloop
    mc "Me too..."
    scene e03s03-135-sy-talk with dissolve
    play voice3 stacy_arrogant_laugh1 noloop
    sy "I wish I could've sat around all day."
    scene e03s03-136-mh-talk-sy with dissolve
    play voice4 dahlia_hey_active2 noloop
    mh "Hey, I'm just following their directions. I didn't ask for this."
    scene e03s03-137-sy-talk-mh with dissolve
    play voice3 stacy_disappointed_mmm2 noloop
    sy "I know, I know. I'm just bitching a little."
    play sound2 sfx_footsteps_grass1 volume 0.8 fadein 1.0
    scene e03s03-138-cm-talk with dissolve
    stop sound2 fadeout 1.5
    play voice6 girl35_thinking_hmf2 noloop
    "Cult Member" "The hour grows late. You have done a satisfactory job. Follow me to your lodgings."
    scene e03s03-139-sy-talk with dissolve
    play voice3 stacy_surprised_ohmy1 noloop
    sy "You hear that! We have {i}lodgings!{/i} I knew all this hard work would pay off!"
    scene e03s03-140-mc-talk-sy with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Don't get too excited, Stacy. She could mean anything by lodgings."
    play sound2 sfx_footsteps_grass1 volume 0.8 fadein 1.0
    scene e03s03-141-sy-talk-mc with dissolve
    play voice3 stacy_no_uhuh4 noloop
    sy "Nuh uh. Lodgings means fancy. Means good food and a warm shower. Exactly what we deserve after a long day of work!"
    scene e03s03-142-mc-talk with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.5
    mc "Oh boy."
    scene e03s03-143-mh-talk-mc with dissolve
    play voice4 dahlia_happy_hmm2 noloop
    mh "I have a feeling she's about to be very disappointed."
    scene e03s03-144-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah9 noloop
    mc "Me too..."
    stop sound2 fadeout 1.5
    scene e03s03-145-tent with dissolve
    pause
    scene e03s03-146-sy-talk-cm with dissolve
    play voice3 stacy_angry_argh2 noloop
    sy "This isn't a lodging! This is a tent!"
    scene e03s03-147-cm-talk-sy with dissolve
    play voice6 girl35_yes_yeah3 noloop
    "Cult Member" "And this is where you'll be staying while you are here!"
    scene e03s03-148-sy-talk-cm with dissolve
    play voice3 stacy_angry_argh4 noloop
    sy "That makes this a summer camp!"
    scene e03s03-149-cm-talk-sy with dissolve
    play voice6 girl35_angry_hm4 noloop
    "Cult Member" "Isolated retreat!"
    scene e03s03-150-mh-talk-sy with dissolve
    play voice4 dahlia_thinking_mmm1 noloop
    mh "Stacy, calm down."
    scene e03s03-151-mh-talk-cm with dissolve
    play voice4 dahlia_disappointed_ehh2 noloop
    mh "My apologies. It seems that some of us came more prepared for the realities of... unplugging, than others. You will have to forgive my friend for her outbursts."
    scene e03s03-152-cm-talk-mh with dissolve
    play voice6 girl35_thinking_hmm3 noloop
    "Cult Member" "I... I can find forgiveness for her, for your sake. But, see to it that she begins to learn her place in the world."
    play sound2 sfx_footsteps_grass1 volume 0.4 fadein 1.0
    scene e03s03-153-sy-talk with dissolve
    play voice3 stacy_surprised_ah2 noloop
    sy "Can I at least get a shower!?"
    play voice2 mc_angry_errr2 noloop
    scene e03s03-154-mc-talk-sy with vpunch
    mc "Stacy!"
    stop sound2 fadeout 3.0
    scene e03s03-155-sy-talk-mc with dissolve
    play voice3 stacy_angry noloop
    sy "What!?"
    scene e03s03-156-mc-talk-sy with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Come on, you have to calm down. We're doing this for Lyssa's friend."
    scene e03s03-157-sy-talk-mc with dissolve
    play voice3 stacy_disappointed_ehh3 noloop
    sy "Ugggggggh. I didn't agree to not showering though."
    scene e03s03-158-mh-talk-sy with dissolve
    play voice4 dahlia_disappointed_hmm1 noloop
    mh "The sooner we can finish this up, the sooner we can get you into a shower."
    scene e03s03-159-sy-talk-mh with dissolve
    play voice3 stacy_angryhuh noloop
    sy "Yeah, yeah... Only for you, Lyssa."
    play sound2 sfx_footsteps_grass1 volume 0.8 fadein 1.0
    scene e03s03-160-tent with dissolve
    pause
    play sound sfx_tent_closed1 volume 0.5
    stop sound2 fadeout 1.0
    stop sound4 fadeout 3.0
    stop music fadeout 7.0

    $ renpy.music.set_volume(0.3, 0.0, "sound3")
    play sound3 parknight fadein 4.0
    scene e03s03-161-mc-talk with fade
    play voice2 mc_arrogant_heh3 noloop
    mc "You know, there's something nice about this place."
    scene e03s03-162-sy-talk-mc with dissolve
    play voice3 stacy_disappointed_oh4 noloop
    sy "You're nuts."
    mc "Maybe... but there's a simplicity to working the land that is just... nice, you know?"
    scene e03s03-163-mh-talk-mc with dissolve
    play voice4 dahlia_yes_aga noloop
    mh "I agree with you, [mcname]."
    scene e03s03-164-sy-talk-mh with dissolve
    play voice3 stacy_surprised_huh3 noloop
    sy "Even you, Lyssa!? I'm shocked!"
    scene e03s03-165-mh-talk-sy with dissolve
    play voice4 lissa_moan1 noloop
    mh "It's... quiet here. I don't get quiet in the office. Or in court. Or at home. It's... peaceful here."
    play voice3 stacy_angry_argh1 noloop
    sy "This is how they get you! This is classic Cult 101 playbook shit!"
    scene e03s03-166-mc-talk-sy with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "What do you know about cults, Stacy?"
    scene e03s03-167-sy-talk-mc with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "I watched a whole documentary on them! First they separate you from everyone, and then they force you into their lifestyle, and then-"
    scene e03s03-168-mh-talk-sy with dissolve
    play voice4 lissa_aga noloop
    mh "Everything that my friend warned us about."
    scene e03s03-169-sy-talk with dissolve
    play voice3 stacy_hey_angry1 noloop
    sy "Then next thing you know, you won't wash your hair because you think little aliens will infect your brain!"
    scene e03s03-170-mc-talk with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "I don't think we have to worry about that, Stacy. I've got plenty of other things on my mind."
    scene e03s03-171-sy-talk-mc with dissolve
    play music music_strange_but_sexy
    play voice3 stacy_thinking_oh1 noloop
    sy "Oh really?"
    play sound4 sfx_cloth_rustling4 noloop
    scene e03s03-a172 sy-talk-mc-glambot-172-000_i with dissolve
    pause
    play sound ["<silence 0.5>", sfx_camera_fly1] volume 2.0
    play sound2 ["<silence 3.0>", sfx_camera_fly1] volume 2.0 noloop
    scene e03s03-a172-glambot-1
    pause
    play voice3 stacy_happy_hmm1 noloop
    sy "And what {i}do you{/i} have on your mind, [mcname]?"


    $ Lovense.stop()

    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene e03s03-173-mc-talk-sy with dissolve
    $ Lovense.vibrate(1)
    play voice2 mc_thinking_hmm7 noloop
    mc "You know, just the tent, and infiltrating, and-"
    play voice3 stacy_mmm2 noloop
    sy "Infiltrating? I have something for you to infiltrate."
    sy "You handled wood alllll day, maybe it's my turn to handle some wood."
    play voice2 mc_thinking_mmm1 noloop
    mc "You know, that sounds pretty nice."
    scene e03s03-174-mh-talk with dissolve
    play voice4 lissa_oh2 noloop
    mh "And what about little, old me?"
    scene e03s03-175-sy-talk-mh with dissolve
    play voice3 stacy_thinking_hmm3 noloop
    sy "I got a lot of practicing working a shaft today, maybe I can show you some of my new skills."
    scene e03s03-176-mh-talk-sy with dissolve
    play voice4 lissa_laugh2 noloop
    mh "I like the sound of that."
    scene e03s03-177-sy-talk with dissolve
    play voice3 stacy_moan4 noloop
    sy "Now... which one do I suck first?"

    $ Lovense.stop()


    play sound sfx_tent_closed1
    scene e03s03-178-cult-member with vpunch
    pause
    scene e03s03-179-sy-talk-cm with hpunch
    play voice3 stacy_scared_oof3 noloop
    sy "Hey! Haven't you ever heard of knocking!? We were in the middle of something." id e03s03_4f4d4a36
    scene e03s03-180-cm-talk with dissolve
    play voice6 girl35_thinking_eem5 noloop
    "Cult Member" "You... the High Priestess wants to see you."
    scene e03s03-181-sy-talk-cm with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "Me?"
    scene e03s03-182-cm-talk-sy with dissolve
    play voice6 girl35_no_angry1 noloop
    "Cult Member" "No, her."
    scene e03s03-183-mh-talk-cm with dissolve
    play voice4 dahlia_surprised_huh1 noloop
    mh "What did I-"
    play sound sfx_cloth_rustling2
    scene e03s03-184-cm-talk-mh with dissolve
    play voice6 girl35_angry_cough2 noloop
    "Cult Member" "The High Priestess can answer any questions you may have."
    scene e03s03-185-mh-talk-cm with dissolve
    play voice4 dahlia_thinking_hmm1 noloop
    mh "I guess... let me put on some clothes."
    scene e03s03-186-cm-talk-mh with dissolve
    play voice6 girl35_no_nah5 noloop
    "Cult Member" "You won't be needing them. We are all naked before the eyes of our goddess, we can all be naked as one."
    play voice4 lissa_thinking noloop volume 1.4
    mh "Uhm, sure. I'll follow you, then..."
    scene e03s03-187-mc-talk-mh with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "Wait, Lyssa!"
    scene e03s03-188-mh-talk-mc with dissolve
    play voice4 dahlia_happy_hmm1 noloop
    mh "Don't worry, [mcname]. I'll be fine. I'll be back before you know it."
    scene e03s03-189-sy-talk-mh with dissolve
    play voice3 stacy_disappointed_oh2 noloop
    sy "Be careful, Lyssa!"
    scene e03s03-190-mh-talk-sy with dissolve
    play voice4 lissa_ha noloop
    mh "You know me."
    play sound sfx_footsteps_grass1
    scene e03s03-191-sy-talk-mc with dissolve
    stop sound fadeout 3.5
    play voice3 stacy_disappointed_ehh2 noloop
    sy "Now what?"
    play voice2 mc_arrogant_hm3 noloop
    mc "I guess we wait for Lyssa to get back and see what she's learned."
    sy "I guess so..."
    scene e03s03-192-mc-talk-sy with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "In the meantime-"
    scene e03s03-193-sy-talk with dissolve
    play voice3 stacy_no_nah1 noloop
    sy "The weirdo killed the vibe."
    scene e03s03-194-mc-talk with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, you're right..."
    play sound sfx_cloth_rustling4
    scene e03s03-195-mc-talk-sy with dissolve
    play voice2 d7s6_moan1 noloop volume 1.4
    mc "How do you pass time without books or a tv or anything?"
    mc "Stacy?"
    scene e03s03-196-sy-sleep with dissolve
    play voice3 stacy_disappointed_snoring volume 0.3
    pause
    play sound sfx_cloth_rustling2
    scene e03s03-197-mc-talk with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "I guess that's one way to pass the time..."
    mc "I'm sure Lyssa will wake me up when she gets back..."
    stop voice3 fadeout 3.0
    stop music fadeout 5.0
    $ renpy.music.set_volume(1.0, 2.0, "sound3")
    scene e03s03-198-tent with dissolve
    pause

    play voice2 d7s6_awake noloop volume 1.8
    $ renpy.music.set_volume(0.3, 2.0, "sound3")
    scene e03s03-199-mc-talk with fade
    play sound sfx_cloth_rustling1
    mc "Lyssa? Are you back yet?"
    play sound sfx_hair_scratch1
    scene e03s03-200-mc-talk with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Lyssa's not back yet? That's not good..."
    mc "I hope she's okay... If she's not back by the morning... I'll have to figure something out..."
    play sound sfx_cloth_rustling3
    scene e03s03-201-mc-talk with dissolve
    play voice2 d1s1_mmm noloop
    mc "I really hope she's okay..."
    stop sound3 fadeout 2.5
    $ renpy.music.set_volume(1.0, 5.0, "sound3")

    jump e03s04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
