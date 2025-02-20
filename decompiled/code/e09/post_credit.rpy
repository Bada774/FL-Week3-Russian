image after_credits_glambot_a2 = Movie(play = "images/E-09/s99/anim/e09s99-a01-2x-60fps.webm", start_image = "e09s99-a01 falling-camera-anim-000", image = "e09s99-a01 falling-camera-anim-140", loop = False)

label dlc_2_postcredits:

    stop music fadeout 3.0
    play sound sfx_light_podium_1
    play sound4 sfx_lockerroom_ambience1 fadein 3.0
    scene e09s99-a01 falling-camera-anim-000 with dissolve
    pause
    play sound sfx_postcredit_camera_fall
    scene after_credits_glambot_a2 with dissolve
    pause
    $ renpy.music.set_volume(0.0, 0.0, "music")
    $ renpy.music.set_volume(1.0, 1.0, "music2")
    $ renpy.music.play(audio.label_supportme, "music" , True, None, True, 2.0)
    $ renpy.music.play(audio.label_supportme_reverbed, "music2", True, None, True, 2.0)
    play sound sfx_barefoot_steps1
    scene e09s99-04-dd-sy with dissolve
    pause
    stop sound fadeout 1.0
    scene e09s99-05-dd-talk-sy with dissolve
    play voice4 daisy_oof noloop
    dd "Woah. What happened here?"
    scene e09s99-06-sy-talk-dd with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "I don't know."
    play sound sfx_barefoot_steps1
    scene e09s99-07-sy-dd with dissolve
    pause
    stop sound fadeout 1.0
    scene e09s99-08-sy-talk-dd with dissolve
    play voice3 stacy_arrogant_hmm3 noloop
    sy "Why is the camera still rolling?"
    scene e09s99-09-dd-talk-sy with dissolve
    play voice4 daisy_thinking noloop volume 1.5
    dd "We finished filming right?"
    scene e09s99-10-sy-talk-dd with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "I thought so."
    play sound sfx_throw_something1
    scene e09s99-11-zp-talk with dissolve
    play voice5 postcredit_girl1_arrogant_hah noloop
    zp "It's a post-credit scene."
    scene e09s99-12-sy-talk-zp with dissolve
    play voice3 stacy_surprised_ah2 noloop
    sy "What? How?"
    play sound sfx_throw_something1
    scene e09s99-13-ir-talk-sy with dissolve
    play voice6 iona_hah1 noloop
    ir "We had to do something special, Stacy! This moment is to celebrate the release of the second DLC of Fetish Locator."
    scene e09s99-14-zp-talk-sy with dissolve
    play voice5 postcredit_girl1_yeah noloop
    zp "That means all 18 endings for Fetish Locator have been completed and are ready for players to enjoy."
    scene e09s99-15-sy-talk-zp with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "Wait! Does that mean this is an inception of post-credit scenes? Like a post-post credit scene?"
    scene e09s99-16-zp-talk-sy with dissolve
    play voice5 postcredit_girl1_geh noloop
    zp "Sure. Something like that."
    scene e09s99-17-ir-talk with dissolve
    play voice6 iona_hm1 noloop
    ir "The important thing is that it's been over a year since you made the previous post-credit scene!"
    scene e09s99-18-dd-talk with dissolve
    play voice4 daisy_aah noloop
    dd "Oh my! I was so focused on all the endings..."
    scene e09s99-19-sy-talk with dissolve
    play voice3 stacy_thinking_oh1 noloop
    sy "Woah. A year already? Does that mean you guys finished Taboo University?"
    play sound sfx_barefoot_steps1 loop
    scene e09s99-20-zp-talk-sy with dissolve
    play voice5 postcredit_girl1_yes_yeah2 noloop
    zp "We sure did. It was an absolute blast."
    zp "Here, follow me."
    $ renpy.music.set_volume(0.7, 1.0, "music")
    $ renpy.music.set_volume(0.0, 2.0, "music2")
    stop sound4 fadeout 2.0
    play sound sfx_magic_disappear2 volume 1.6
    play sound3 parknight fadein 3.0
    scene e09s99-21-party-pool with image_dissolve_e09s99_01_2
    pause
    play sound sfx_barefoot_steps1 loop
    scene e09s99-22-party-pool with dissolve
    pause
    stop sound fadeout 1.0
    scene e09s99-23-im-talk with dissolve
    play voice6 postcredit_girl25_hey_high noloop
    ima "Guys! Stacy!"
    scene e09s99-24-sy-talk-im with dissolve
    play voice3 stacy_hey noloop
    sy "Hey!"
    play sound sfx_cloth_rustling1
    scene e09s99-25-im-talk-sy with dissolve
    play voice6 postcredit_girl25_happy_relief1 noloop
    ima "We just finished the game! It's soooo big! So much stuff happened! And the last party, there was so much sex here!"
    scene e09s99-26-dd-talk with dissolve
    play voice4 daisy_haha noloop
    dd "I'm so excited to play it. I loved the premise, but I wanted to wait till the whole game was out."
    scene e09s99-27-zp-talk-dd with dissolve
    play voice5 postcredit_girl1_thinking_hmm2 noloop
    zp "Well, that day is finally here, Daisy. Now everyone can play Taboo University - Book One."
    scene e09s99-28-dd-talk-zp with dissolve
    play voice4 daisy_yay noloop
    dd "Woohoo!"
    scene e09s99-29-ir-talk with dissolve
    play voice6 iona_yes2 noloop
    ir "And we've already begun working on Book Two!"
    scene e09s99-30-zp-talk with dissolve
    play voice5 postcredit_girl1_surprised_ou noloop
    zp "Oh yes, we've already made a bunch of scenes! People should expect the first release of the next chapter soon!"
    scene e09s99-31-im-talk with dissolve
    play voice6 postcredit_girl25_thinking_hmm2 noloop
    ima "And what about Fetish Locator S&M? In the last post-credit scene, you hyped it up so much!"
    play sound sfx_magic_appears2
    stop sound3 fadeout 2.0
    play sound4 sfx_office_ambience1 fadein 3.0
    scene e09s99-32-cw-talk with image_dissolve_e09s99_02_1
    play voice7 postcredit_girl29_hey_happy noloop
    cw "I'm happy to report that S&M has launched, and we've already made several releases for the game."
    scene e09s99-33-dd-talk with dissolve
    play voice4 daisy_hey noloop
    dd "Hey, it's Nari!"
    scene e09s99-34-ns-talk-dd with dissolve
    play voice5 nari_hey_high noloop
    ns "Hello, Daisy!"
    play sound sfx_cloth_rustling4
    scene e09s99-35-dd-hugs-ns with dissolve
    pause
    scene e09s99-36-ir-talk with dissolve
    play voice6 iona_huh2 noloop
    ir "You know each other?"
    scene e09s99-37-dd-talk-ir with dissolve
    play voice4 daisy_yes noloop
    dd "Yes, this is Nari from Min's Ending!"
    scene e09s99-38-ns-talk-ir with dissolve
    play voice5 nari_yes_aga1 noloop
    ns "That was my very first appearance."
    scene e09s99-39-sy-talk with dissolve
    play voice3 stacy_happy_yay3 noloop
    sy "I love that ending!"
    scene e09s99-40-ns-talk with dissolve
    play voice5 nari_happy_laugh1 noloop
    ns "Thank you, Stacy."
    ns "I've been so honored that the team decided to give me a larger role in S&M."
    ns "But I did miss out on being in Min's other ending. I think it was called Weather Fall? How was it? I really wanted to be there."
    scene e09s99-41-sy-talk-ns with dissolve
    play voice3 stacy_thinking_oh2 noloop
    sy "We named it Waterfall - and it was great! The team went to the bottom of the ocean and beyond there! Very deep and wet!"
    scene e09s99-42-ns-talk-sy with dissolve
    play voice5 nari_thinking_hmm2 noloop
    ns "That sounds amazing. I'll have to check it out!"
    ns "I hope that I'll get some similar experiences in S&M."
    scene e09s99-43-cw-talk-ns with dissolve
    play voice6 postcredit_girl29_yes_aga1 noloop
    cw "I'm sure you'll get the chance, Nari. Just make sure not to do it during work hours."
    scene e09s99-44-ns-talk-cw with dissolve
    play voice5 nari_yes_yep noloop
    ns "Of course, Miss Watts."
    ns "I would never do naughty stuff during work. Hehehe."
    scene e09s99-45-cw-talk with dissolve
    play voice6 postcredit_girl29_thinking_hmm2 noloop
    cw "Hmmm."
    scene e09s99-46-sy-talk-zp with dissolve
    play voice3 stacy_laugh4 noloop
    sy "Haha. Like Nari said, there is already plenty of naughty stuff to find in S&M."
    scene e09s99-47-zp-talk-sy with dissolve
    play voice5 postcredit_girl1_arrogant_hah noloop
    zp "Nice. How different is S&M from Taboo University?"
    scene e09s99-48-sy-talk-zp with dissolve
    play voice3 stacy_thinking_emm3 noloop
    sy "It's a bit different, but nothing too crazy. Claire can probably explain it better."
    scene e09s99-49-cw-talk with dissolve
    play voice6 postcredit_girl29_thinking_hmm5 noloop
    cw "The key difference is that S&M has more of a sandbox style approach, compared to the playstyle of Fetish Locator and Taboo University."
    cw "We're giving the player more freedom. That includes the ability to unlock different characters, factions, and locations in whatever order they like."
    scene e09s99-50-ns-talk with dissolve
    play voice5 nari_thinking_oh noloop
    ns "And we've also added money mechanics and time management. These elements are part of the player building their Porn Studio."
    scene e09s99-51-sy-talk with dissolve
    play voice3 stacy_yes_yap2 noloop
    sy "It sounds complicated, but it's really pretty straightforward."
    sy "And I'll be there the whole time to guide you!"
    sy "S&M's story is also going to be huge. We're giving the player lots of cool and interesting quests to complete on their road to opening a porn studio."
    scene e09s99-54-dd-talk-cw with dissolve
    play voice4 daisy_hmm1 noloop
    dd "And there is still a lot of sex scenes and fetishes, right?"
    scene e09s99-55-ns-talk-dd with dissolve
    play voice5 nari_yes_emotional noloop
    ns "Of course! And we have some characters returning from FL as well! AmRose will play a role in the main story, and we also have new content for Lyssa!"
    scene e09s99-56-cw-talk-dd with dissolve
    play voice6 postcredit_girl29_yes_aga2 noloop
    cw "Correct. She's filming a sex scene as we speak!"
    scene e09s99-57-im-talk-cw with dissolve
    play voice7 postcredit_girl25_thinking_oh5 noloop
    ima "Oh! Even Lyssa is there?"
    scene e09s99-58-cw-talk-im with dissolve
    play voice6 postcredit_girl29_yes_aga3 noloop
    cw "Mmhmm."
    scene e09s99-59-ir-talk with dissolve
    play voice5 iona_hm2 noloop volume 1.7
    ir "So, it is a real continuation of Fetish Locator?"
    scene e09s99-60-sy-talk-ir with dissolve
    play voice3 stacy_yes_yap3 noloop
    sy "It totally is!"
    scene e09s99-61-zp-talk-sy with dissolve
    play voice4 postcredit_girl1_surprised_wow1 noloop
    zp "I'm so happy for you guys!"
    play sound sfx_cloth_rustling4
    scene e09s99-62-zp-hugs-sy with dissolve
    play voice3 stacy_suckmoan3 noloop
    pause
    scene e09s99-63-sy-talk-zp with dissolve
    play voice3 stacy_happy_relief1 noloop
    sy "And I'm happy you also got to finally launch your game!"
    scene e09s99-64-zp-kiss-sy with dissolve
    play voice3 stacy_happy_laugh2 noloop
    play sound maria_kiss2
    pause
    scene e09s99-65-zp-kiss-sy with dissolve
    play voice3 stacy_suckmoan1 noloop
    play sound dahlia_kiss_french1
    pause
    stop music fadeout 3.0
    stop sound4 fadeout 2.0

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
