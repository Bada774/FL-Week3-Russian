image e09s06-a12-glambot-1 = Movie(play = "images/E-09/s06/anim/e09s06-a12.webm", start_image = "e09s06-a12 mes-stands-front-mc-ask-how-looks-mc-ravishing-glambot-000", image = "e09s06-a12 mes-stands-front-mc-ask-how-looks-mc-ravishing-glambot-119", loop = False)

label e09s06:

    $ e09s06_kb_cb_done = False
    $ e09s06_ah_tr_done = False
    $ e09s06_jdg_done = False
    $ e09s06_tm_done = False

    scene black
    show screen scene_transistion(_("PARTY NIGHT!"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion

    $ renpy.music.set_volume(0.0, 0.0, "music")
    $ renpy.music.set_volume(0.5, 1.0, "music2")
    $ renpy.music.play(audio.music_athenas_call, "music" , True, None, True, 0.0)
    $ renpy.music.play(audio.music_athenas_call_radio, "music2", True, None, True, 0.0)

    scene e09s06-01 mc-mes-waiting-living-room-chilling_c1
    with Fade(0.5, 0.5, 0.5)
    pause
    scene e09s06-02 mes-never-thought-another-mask-mc-glad-find-her-excuse_c1 with dissolve
    play voice3 min_happy_mmm noloop
    mes "Mmmmm... I never thought I was going to have another reason to put on a mask!"
    play voice2 mc_happy_hah2 noloop
    mc "I'm glad we were able to find you an excuse!"
    scene e09s06-03 after-everything-lc-mc-not-name-saying-tonight_c1 with dissolve
    play voice3 min_disappointed_ehh1 noloop
    mes "After everything with Lydia, I just-"
    play voice2 d2s9_mchey noloop
    mc "Hey, that's not a name we're saying tonight."
    scene e09s06-04 mes-tries-speak-mc-no-buts with dissolve
    play voice3 min_surprised_ehh1 noloop
    mes "I know, but-"
    play voice2 mc_no_no1 noloop
    mc "Nope. No buts! Those days are behind us, and Fetish Locator Rebooted isn't going to dwell in the past. On to bigger and better things!"
    scene e09s06-05 mes-looks-mc-you-right-mc-damn-right with dissolve
    play voice3 min_arrogant_huh1 noloop
    mes "You know what? You're right!"
    play voice2 mc_yes_yeah2 noloop
    mc "Damn right I am!"
    play sound sfx_cloth_rustling3
    scene e09s06-06 mes-should-probably-start-getting-ready-mc-ask-any-tips with dissolve
    play voice3 min_thinking_emm noloop
    mes "All right, we should probably start getting ready. Guests should be arriving soon."
    play voice2 mc_thinking_hmm2 noloop
    mc "Got any tips you want to share about hosting one of these parties?"
    scene e09s06-07 mes-viagra-mc-laughs-what with dissolve
    play voice3 min_arrogant_heh1 noloop
    mes "Viagra."
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    mes "Everyone is showing up to get a taste of you tonight, [mcname]. And you can't disappoint. So be ready to fuck until the sun comes up. I recommend Viagra for that."
    scene e09s06-08 mes-explains-mc-meant-tips-for-hosting with dissolve
    play voice2 d4s4_mclaugh noloop volume 2.0
    mc "Hahaha - I meant about being a host."
    play sound sfx_barefoot_steps1
    scene e09s06-09 mes-goes-get-toga-just-be-charming-self-not-get-drunk with dissolve
    play voice3 min_arrogant_huh2 noloop
    mes "You know, just be your charming self. Talk to everyone, keep them entertained. Make sure you don't get sucked into any lengthy conversations. That kind of stuff."
    mes "Oh, and be careful of the libations. You need to stay sharp and focused, and getting drunk will ruin all of that."
    scene e09s06-10 mc-thoughtful-got-it-mes-offcam-and-never-take-off-smile with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.7
    mc "Got it. Keep moving, no drinking."
    play voice3 min_yes_ugu noloop
    mes "And never take off your smile."
    play sound sfx_heels_steps2
    scene e09s06-11 mes-appears-toga with dissolve
    pause
    $ renpy.music.set_volume(0.75, 3.0, "music")
    $ renpy.music.set_volume(0.0, 10.0, "music2")
    play sound sfx_camera_fly1 volume 3.0
    scene e09s06-a12-glambot-1 with Dissolve(0.2)
    pause
    play voice3 min_surprised_huh1 noloop
    mes "How does it look?"
    play voice2 mc_happy_oof3 noloop
    mc "Ravishing."
    stop sound fadeout 1.0
    scene e09s06-13 mes-haha-that-energy-lets-get-position-invite-guests with dissolve
    play voice3 min_old_laugh noloop
    mes "Haha. That's the energy to keep up tonight! Now come on, let's get into position to receive our guests."
    play sound sfx_heels_steps2 loop
    scene e09s06-14 mes-heads-towards-entrance-put-costume-on-mc-right with dissolve
    mes "And put your costume on! Can't start the party naked!"
    play voice2 mc_surprised_oh3 noloop
    mc "Oh, right!"
    stop sound fadeout 2.0
    scene e09s06-15 mc-mes-stand-ready-welcome-ppl_c1 with Fade(0.5, 0.5, 0.5)
    pause
    scene e09s06-16 mc-gah-nervous-mes-me-too with dissolve
    play voice2 mc_disappointed_meh1 noloop
    mc "Gah, I'm kind of nervous."
    play voice3 min_yes_aga noloop
    mes "Me too."
    scene e09s06-17 mc-really-done-this-before-mes-been-while_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.4
    mc "Really? But you've done this before."
    play voice3 min_yes_yeah1 noloop
    mes "Yeah, but it's been awhile. Plus, it's a nervous excitement."
    scene e09s06-18 mc-hm-maybe-that-too with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Huh... maybe that's it too."
    scene e09s06-19 mes-look-door-first-guests-arived-mc-very-promt with dissolve
    play voice3 min_thinking_hmm2 noloop
    mes "Looks like our first guests have arrived!"
    play voice2 mc_surprised_wow3 noloop
    mc "Wow. Very... prompt."
    $ renpy.music.set_volume(0.7, 10.0, "music")
    scene e09s06-20 mes-say-same-thing-about-timliness with dissolve
    play voice3 min_disappointed_mph noloop
    mes "You know what they say about timeliness."
    play sound sfx_heels_steps1
    scene e09s06-21 ah-tr-enter-mes-greets-them-tr-surprised-no-nicknames with dissolve
    stop sound fadeout 2.0
    play voice3 min_hey_simple noloop
    mes "Aaleyah, Tyrell. It's good to see you both." id e09s06_1e476a9b
    play voice4 terrell_huh1 noloop
    tr "Wait - are we not doing our usernames anymore?"
    scene e09s06-22 mc-nope-at-least-tonight-ah-what-about with dissolve
    play voice2 mc_no_nope2 noloop
    mc "Nope! At least not tonight!"
    play voice5 aaleyah_surprised_oh noloop
    ah "Oh, uhm... what about-"
    scene e09s06-23 mc-explains-tonight-private-event with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Don't worry - tonight is a private event. Everyone who's been invited knows the rules, and has agreed that 'what happens here, stays here'."
    mc "So no need to worry about anything tonight outside of having a little bit of safe, fetish filled fun!"
    scene e09s06-24 tr-ah-relax-tr-thanks-mcalways-happpy with dissolve
    play voice4 terrell_relief noloop
    tr "Awesome. Thanks, [mcname]! We've both been really excited about tonight."
    play voice2 mc_yes_sure1 noloop
    mc "And I'm happy you both could be here! Feel free to wander, you two are the first here, but we have some drinks and refreshments around the house."
    play sound sfx_heels_steps1 loop
    scene e09s06-25 ah-tr-enter-ah-sounds-good with dissolve
    play voice5 aaleyah_yes_aga4 noloop
    ah "Sounds good, thanks [mcname]!"
    stop sound fadeout 2.0
    scene e09s06-26 mes-impressive-mc-what with dissolve
    play voice3 min_surprised_wow noloop
    mes "Impressive, [mcname]."
    play voice2 mc_surprised_what7 noloop volume 0.7
    mc "What?"
    scene e09s06-27 mes-handle-that-well-mc-thanks with dissolve
    play voice3 min_old_hmm noloop volume 1.5
    mes "You handled that well. I don't think you have anything to worry about hosting this event."
    play voice2 mc_happy_a1 noloop
    mc "Thanks, Min."
    scene e09s06-28 mes-looks-door-another-prompt-arrival with dissolve
    play voice3 min_thinking_oh noloop
    mes "Another prompt arrival. People must be excited for tonight."
    play sound sfx_heels_steps1
    scene e09s06-29 hr-lo-appear-door-mes-doesnt-know-lo-name with dissolve
    stop sound fadeout 2.0
    mes "Hana, and..."
    scene e09s06-30 lo-introduces-herself-mes-no-need-formalities with dissolve
    play voice4 girl28_yes_yeah1 noloop
    lo "Londyn, a pleasure, Miss-"
    play voice3 min_no_nonono noloop
    mes "Please, no need for formalities. I'm Min, welcome to my home."
    scene e09s06-31 mc-didnt-expect-early-hr-well-should-arive-early with dissolve
    play voice2 mc_surprised_wow2 noloop
    mc "Wow, I didn't expect you two to show up so early."
    play voice5 girl30_thinking_hmm1 noloop
    hr "Well, as the head of your Oversight Committee, I thought I should arrive early to make sure everything was above board."
    scene e09s06-32 hr-also-want-sure-investment-wise-lo-oh-reminds-me with dissolve
    play voice5 girl30_arrogant_heh noloop
    hr "I also want to make sure my investment is being used wisely."
    play voice4 girl28_surprised_oh noloop
    lo "Oh, that reminds me!"
    play sound sfx_paper_slide1 volume 1.4
    scene e09s06-33 lo-donation-mc-wow-thanks with dissolve
    play voice4 girl28_happy_mmm1 noloop
    lo "A donation to the cause."
    play voice2 mc_scared_oh4 noloop
    mc "Wow, thank you, Londyn! But you didn't have to do this. You've already done more than enough."
    scene e09s06-34 lo-want-fl-rebooted-be-great-mc-oh with dissolve
    play voice4 girl28_hey_active noloop
    lo "I want to! I think Fetish Locator Rebooted is going to do great. Which reminds me, we should actually have a little chat."
    play voice2 mc_surprised_oh1 noloop
    mc "Oh?"
    scene e09s06-35 lo-but-now-hostly-duties-mc-speaking-of-ask-miss-togas with dissolve
    play voice4 girl28_disappointed_eeh2 noloop
    lo "But not right now, you have hostly duties to do!"
    play voice2 mc_arrogant_huh1 noloop
    mc "Speaking of, did you two miss the part about the togas in the invite?"
    scene e09s06-36 hr-smile-no-did-not-mc-well-those-not-looks-togas with dissolve
    play voice5 girl30_no_happy noloop
    hr "No, we did not."
    play voice2 mc_thinking_hmm1 noloop
    mc "Well, those don't look like togas."
    play sound sfx_cloth_planket3 volume 0.6
    scene e09s06-37 mc-shocked with dissolve
    play voice2 mc_scared_huuuh3 noloop volume 1.5
    pause
    scene e09s06-38 hr-lo-stand-in-togas with dissolve
    play voice2 mc_pain_ou1 noloop
    mc "Oh goddamn."
    play voice5 girl30_arrogant_pfhah noloop
    hr "Thought you might like these."
    play sound sfx_heels_steps1 loop
    scene e09s06-39 hr-lo-walk-start-walking-away-mc-deff-right-lo-laughs with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, you're definitely right about me liking those!"
    play voice4 girl28_happy_laugh1 noloop
    lo "Hahahaha!"
    scene e09s06-40 hr-going-make-sure-everything-setup-mc-believe-he-will with dissolve
    play voice5 girl30_thinking_emm2 noloop
    hr "I'm going to make sure everything is all set up. Definitely come find us later."
    play voice2 mc_scared_oh2 noloop
    mc "Oh believe me, I will!"
    stop sound fadeout 2.0
    scene e09s06-41 mes-wow-good-party-mc-that-it-is with dissolve
    play voice3 min_surprised_oh noloop
    mes "Wow... this is going to be a good party."
    play voice2 mc_happy_yes1 noloop
    mc "That it is!"
    scene e09s06-42 mes-looks-door-sounds-like-more-guests with dissolve
    play voice3 min_thinking_hmm3 noloop
    mes "Sounds like there are more guests!"
    play sound sfx_heels_steps1
    scene e09s06-43 cl-tl-stand-door-mes-greets-them-tl-of-course with dissolve
    stop sound fadeout 2.0
    mes "Cynthia, Professor Lewald - happy you could be here."
    play voice4 teresa_yes_ugu noloop
    tl "Of course. Thank you for your hospitality and for hosting this event."
    scene e09s06-44 mes-starts-speaking-actually with dissolve
    play voice3 min_arrogant_hm noloop
    mes "Actually-"
    scene e09s06-45 tl-looks-cl-where-manners-cl-thanks-mes with dissolve
    play voice4 teresa_disappointed_ehh1 noloop
    tl "Where are your manners? Thank Min for her hospitality."
    play voice5 cynthia_disappointed_ehh noloop volume 0.8
    cl "Thank you, Min."
    scene e09s06-46 mes-actually-her-home-mc-party with dissolve
    play voice3 min_thinking_mhh noloop
    mes "Actually, it may be my home, but [mcname] is your host for the evening. You should thank him."
    scene e09s06-47 tl-squints-hmmm-mc-yep-tl-starts-i with dissolve
    play voice4 teresa_thinking_hmm1 noloop
    tl "Hmmmm..."
    play voice2 d9s2_yeah noloop volume 2.0
    mc "Yep! But it's good to see you, Professor Lewald."
    tl "I-"
    scene e09s06-48 mes-look-over-shoulder-other-guests-tl-come-along-cl with dissolve
    play voice3 min_hey_greeting noloop
    mes "I hate to be rude, but I see more of our guests arriving."
    play voice4 teresa_yes_aga noloop
    tl "Later then. Come along, Cynthia."
    play sound sfx_heels_steps1 loop
    scene e09s06-49 tl-cl-enter-dissapear-into-party with dissolve
    pause
    scene e09s06-50 mh-judge-arive-mh-hello-mc-mc-greets-them with dissolve
    play voice4 daisy_hey noloop
    mh "Hello, [mcname]."
    play voice2 mc_happy_yay2 noloop
    if date_jdg is True:
        mc "Lyssa! Judge! It's good to see you both."
    else:
        mc "Lyssa, and..."
        mh "This is a friend of mine who has heard my stories about the old Fetish Locator parties and wanted to see one for herself."
        mc "Well, welcome to the show!"
    stop sound fadeout 1.0
    scene e09s06-51 mc-got-here-time-jdg-oh with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "You got here just in time."
    play voice5 girl27_surprised_oh4 noloop volume 1.5
    jdg "Oh?"
    scene e09s06-52 mc-yeah-lewald-never-like-him-mh-haha-ofc with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah. Lewald never liked me, saved me from a very uncomfortable conversation most likely."
    play voice4 lissa_haha2 noloop
    mh "Haha, of course. I do have a habit of arriving exactly when I am supposed to."
    scene e09s06-53 mc-all-need-gray-hat-judge-kaughs-can-imagine with dissolve
    play voice2 mc_happy_hah1 noloop
    mc "All you need now is the gray hat!"
    play voice5 girl27_happy_laugh1 noloop
    jdg "Hahahahaha! Can you imagine?"
    mc "Now it's all I can picture! Which is impressive because you two look ravishing."
    jdg "Mmmmm, I like the sound of that."
    scene e09s06-54 mc-now-all-can-picture-jdg-like-sound-mh-which-reminds-me_c1 with dissolve
    play voice4 lissa_oh2 noloop
    mh "Which reminds me-"
    play sound sfx_paper_rustl1
    scene e09s06-55 jdg-mh-hold-envelopes-mh-arj-called-sponsors-mc-too-kind-thanks_c1 with dissolve
    play voice4 dahlia_thinking_hmm1 noloop
    mh "AmRose called saying that Fetish Locator Rebooted is looking for new sponsors. We both brought a little something to contribute."
    play voice2 mc_thinking_mmm3 noloop
    mc "You are too kind! Thank you!"
    play sound sfx_paper_slide1
    scene e09s06-56 mc-takes-envelopes-mh-do-better-job-predeseccor-jdg-yes-pls_c1 with dissolve
    play voice4 lissa_aga noloop
    mh "Just make sure you do a better job than your predecessor."
    play voice5 girl27_yes_simple noloop
    jdg "Yes, please. My god, the information that came out during her trial..."
    if date_jdg is False:
        scene e09s06-57 mc-didnt-know-jdg-knows-jdg-keeps-on-pcurrent-affairs_c1 with dissolve
        play voice2 mc_disappointed_ah1 noloop
        mc "Oh, uh... I didn't realize you knew."
        play voice5 girl27_thinking_hmm noloop
        jdg "I... like to keep up on current affairs is all. Her trial has been pretty public, lots of water cooler talk about it."
        scene e09s06-58 mc-promises-fl-totally-diff-will-be-okay-folks-running-things_c1 with dissolve
        play voice2 mc_yes_yeah6 noloop
        mc "That there has been. But I promise you, Fetish Locator Rebooted is totally different, with a higher standard of security, anonymity, and safety."
    else:
        scene e09s06-58 mc-promises-fl-totally-diff-will-be-okay-folks-running-things_c1 with dissolve
        play voice2 mc_thinking_mmm1 noloop
    mc "I think with the folks I have running everything, we are going to be more than okay."
    scene e09s06-59 mh-mes-look-door-more-guests-coming-mes-yes-jdg-party-of-year_c1 with dissolve
    play voice4 lissa_oh noloop
    mh "I take it more guests are arriving?"
    play voice3 min_yes_happy noloop
    mes "They are!"
    play voice5 girl27_arrogant_hah noloop
    jdg "This is set to be the party of the year, so I can't say I'm surprised. We'll chat more later!"
    play sound sfx_heels_steps1 loop
    scene e09s06-60 mh-jdg-enter-party-mes-mc-prepare-next-couple_c1 with dissolve
    pause
    scene e09s06-61 mes-mc-greet-next-guests_c1 with dissolve
    play voice3 min_old_hey noloop
    mes "Hello. Welcome to the Fetish Locator Rebooted soft launch!"
    scene e09s06-62 cb-thank-you-mc-hey-kb-cb-too_c1 with dissolve
    play voice4 chloe_happy_hmm noloop
    cb "Thank you!"
    play voice2 mc_hey_hey10 noloop
    mc "Hey Kevin, hey Chloe! Glad you both could make it!"
    stop sound fadeout 1.0
    scene e09s06-63 cb-wouldnt-miss-tonight-promises-fun_c1 with dissolve
    play voice4 chloe_happy_yeah1 noloop
    cb "Wouldn't miss it! Tonight promises to be a ton of fun."
    play sound sfx_paper_rustl1
    scene e09s06-64 kb-holds-envelope-excited-donate-mc-didnt-have-to_c1 with dissolve
    play voice5 kevin_thinking_hmm6 noloop
    kb "We're so excited that we managed to pull together a little bit of cash to donate!"
    play voice2 mc_disappointed_off2 noloop
    mc "Oh, you guys! You didn't need to do that!"
    scene e09s06-65 kb-believe-both-see-investment-then-get-in-here_c1 with dissolve
    play voice5 kevin_no_uhuh1 noloop
    kb "Believe me, we both see this as an investment. We plan to cash that in tonight!"
    play voice2 mc_yes_okay2 noloop
    mc "Well then get in here! Wander around a bit, get some good food and drink, and I promise tonight is going to be a ton of fun."
    play sound sfx_heels_steps1 loop
    scene e09s06-66 cb-kb-enter-party_c1 with dissolve
    pause
    stop sound fadeout 2.0
    scene e09s06-67 mes-mc-turn-attention-next-guests_c1 with dissolve
    pause
    scene e09s06-68 pw-mk-tm-enter-house-pw-hi-mc-see-found-friends_c1 with hpunch
    play voice4 polly_hey noloop
    pw "Hi, [mcname]!"
    play voice2 mc_hey_hey8 noloop
    mc "Polly! Hey! I see you found some friends!"
    scene e09s06-69 pw-yes-did-met-on-the-way_c1 with dissolve
    play voice4 polly_aga noloop
    pw "I did! We were all walking the same direction, looking ridiculous, and figured we were all going to the same place!"
    scene e09s06-70 mk-why-dresscode-mc-half-fun-undressing_c1 with dissolve
    play voice5 maria_argh noloop
    mk "Speaking of, why the hell is there a dress code? Shouldn't we all just... be naked?"
    play voice2 d1s2_mchey noloop
    mc "Hey, half the fun of a sex party is undressing!"
    scene e09s06-71 mk-thought-freaky-one-mc-but-also-wanted-more-memorable_c1 with dissolve
    play voice5 maria_meeh noloop
    mk "And I thought I was the freaky one..."
    play voice2 mc_thinking_hmm4 noloop
    mc "But, we also wanted to do something memorable and fun for our first party. Plus, I think it's a good fit for the decadence and hedonism we have planned for tonight."
    scene e09s06-72 tm-fancy-way-say-greeks-fuck-mc-yes-all_c1 with dissolve
    play voice6 girl23_arrogant_ha noloop
    tm "Wow, that's a lot of fancy words to say the Greeks liked to fuck."
    play voice2 mc_yes_yes7 noloop
    mc "Yes it is, and yes they did!"
    scene e09s06-73 mc-gestures-come-in-hopes-all-greek-tonight-pw-hope-so_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Hopefully, we can be like the Greeks tonight."
    play voice4 polly_yes1 noloop
    pw "I hope so too!"
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene e09s06-74 pw-tm-mk-go-inside-party_c1 with dissolve
    pause
    stop sound2 fadeout 3.0
    play sound sfx_heels_run2
    scene e09s06-75 pw-runs-back-holding-envelope-almost-forgot-mc-thanks-pw_c1 with dissolve
    play voice4 polly_oh noloop
    pw "I almost forgot! Here's a little something from myself, and Nora!"
    play voice2 mc_scared_oh3 noloop
    mc "Thank you, Polly!"
    queue sound sfx_heels_steps1 loop
    scene e09s06-76 pw-dont-mention-hurries-back_c1 with dissolve
    play voice4 polly_nono noloop
    pw "Don't mention it. But, maybe swing by and buy some coffee from Nora."
    stop sound fadeout 2.0
    scene e09s06-77 mes-mc-turn-attention-next-guests_c1 with dissolve
    pause
    scene e09s06-78 dd-dw-enter-house_c1 with dissolve
    pause
    scene e09s06-79 mc-hey-daisy-dahlia-dd-hi-mc_c1 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Hey Daisy, hey Dahlia!"
    play voice4 daisy_hey noloop
    dd "Hi, [mcname]!"
    scene e09s06-80 mc-nervous-good-see-ya-look-great-dd-thank-you_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "It's good to see you. You look magnificent tonight."
    play voice4 daisy_aga noloop
    dd "Thank you!"
    scene e09s06-81 mc-dw-fierce-dw-thanks-mc-ask-excited-tonight-festivities_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.4
    mc "And you look... fierce, as always, Dahlia."
    play voice5 dahlia_angry_oh noloop
    dw "Thank you."
    mc "Excited for the festivities tonight?"
    scene e09s06-82 dd-excited-right-dw-hopefully_c1 with dissolve
    play voice4 daisy_yay noloop
    dd "We are! Right, Dahlia?"
    play voice5 dahlia_thinking_hmm1 noloop
    dw "Mmmhmmm. Hopefully, there is a suitable worm at this party for me."
    scene e09s06-83 mc-hope-so-too-dw-brought-gift_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "I, uhm, hope so too!"
    play voice5 dahlia_arrogant_heh noloop
    dw "We also brought a gift for you, our host."
    play sound sfx_paper_rustl1 volume 1.4
    scene e09s06-84 mc-nervous-dw-she-hands-envelope-both-enjoyed-fl_c1 with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "Oh, Dahlia, I-"
    play voice5 dahlia_disappointed_ehh2 noloop
    dw "Daisy and I have both always enjoyed Fetish Locator. We are both very happy to see it back."
    scene e09s06-85 mc-wow-thanks_c1 with dissolve
    play voice2 mc_surprised_wow4 noloop
    mc "Oh, wow! Thank you! I-"
    play sound sfx_heels_steps1 loop
    scene e09s06-86 dw-enters-party_c1 with dissolve
    play voice5 dahlia_disappointed_hmm1 noloop
    dw "If you'll excuse me, I'm in a spanking mood."
    play voice2 mc_yes_okay1 noloop
    mc "Okay, well, have fun!"
    scene e09s06-87 dd-goes-past-mc-see-around-mc_c1 with dissolve
    play voice4 daisy_haha noloop
    dd "See you around, [mcname]."
    scene e09s06-88 dd-dw-enter-party_c1 with dissolve
    pause
    stop sound fadeout 2.0
    scene e09s06-89 mes-thinks-that-went-well-mc-expected-one-late-arrival_c1 with dissolve
    play voice3 min_happy_phew noloop
    mes "Well, I think that was everyone."
    play voice2 mc_arrogant_hm3 noloop
    mc "I was expecting at least one fashionably late arrival."
    mes "You've put together quite an exciting affair. Everyone is ecstatic for the festivities."
    play sound sfx_cloth_rustling1
    scene e09s06-90 mes-hand-mc-shoulder-better-begin-prep-mc-shit-prolly-should-mes-keep-guests-entertained_c1 with dissolve
    play voice3 min_thinking_hmm1 noloop
    mes "You better begin preparing, in fact."
    play voice2 mc_disappointed_ehh1 noloop
    mc "Shit, I probably should..."
    mes "I'll keep your guests entertained in the meantime."
    play sound sfx_heels_steps2 loop
    scene e09s06-91 mes-leaves-mc-alone-with-thoughts_c1 with dissolve
    pause
    stop sound fadeout 2.0
    scene e09s06-92 label-pt2-mc-standing-outside-sy-walk-up-him_c1 with dissolve
    play voice2 d14s16_smell noloop
    mct "And now the real show begins..."
    mct "How the hell am I going to pull this off..."

    jump e09s06_part_2

label e09s06_part_2:

    scene e09s06-93 sy-ask-mc-what-doing-mc-bneing-nercous_c1 with Fade(0.5, 0.5, 0.5)
    play voice3 stacy_arrogant_huh2 noloop
    sy "Whatcha' doing?"
    play voice2 mc_disappointed_ehh2 noloop
    mc "Being nervous."
    scene e09s06-94 sy-why-mc-future-depends-on it_c1 with dissolve
    play voice3 stacy_mmm2 noloop
    sy "Why?"
    play voice2 mc_thinking_mmm5 noloop
    mc "Our future depends on how tonight goes."
    play sound sfx_heels_steps1 loop
    scene e09s06-95 arj-walks-into-frame-true-but-not-worried-mc-maybe-little_c1 with dissolve
    play voice4 amrose_yes_yeah1 noloop
    arj "That's true, but do Stacy and I look worried?"
    play voice2 mc_thinking_mmm4 noloop
    mc "Maybe a little?"
    stop sound fadeout 1.0
    scene e09s06-96 arj-well-not-so-nothing-worry_c1 with dissolve
    play voice4 amrose_no_simple3 noloop
    arj "Well, we're not, so you've got nothing to worry about."
    scene e09s06-97 mc-still-nervous-if-say-so-mc-comeon-go-mingle_c1 with dissolve
    play voice2 mc_arrogant_hm2 noloop
    mc "Okay... if you say so."
    play voice3 stacy_angry noloop
    sy "Come on, go mingle! Get everyone hyped up for the main event."
    scene e09s06-98 mc-repeats-if-say-so_c1 with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "If you say so."
    play sound sfx_barefoot_steps1 volume 1.7
    scene e09s06-99 arj-sy-watch-mc-heads-party_c1 with dissolve
    pause
    stop sound fadeout 1.0
    play sound4 d12s2_cafe_crowd fadein 2.0
    scene e09s06-100 menu-screen-choice-mc-how-talk-to_c1 with dissolve
    play voice2 d1s1_mmm noloop
    mct "Now... who to talk to?"
    $ renpy.music.set_volume(1.0, 3.0, "music")

    jump e09s06_part_2_menu

label e09s06_part_2_menu:
    menu:
        "Talk to Kevin and Chloe" if e09s06_kb_cb_done is False:
            $ e09s06_kb_cb_done = True
            jump e09s06_kb_cb

        "Talk to Aaleyah and Tyrell" if e09s06_ah_tr_done is False:
            $ e09s06_ah_tr_done = True
            jump e09s06_ah_tr

        "Talk to the Judge" if date_jdg is True and e09s06_jdg_done is False:
            $ e09s06_jdg_done = True
            jump e09s06_jdg

        "Talk to Talia" if e09s06_tm_done is False:
            $ e09s06_tm_done = True
            jump e09s06_tm
        "Get ready for the main event":

            jump e09s06_part_2_continue

label e09s06_kb_cb:

    scene e09s06-101 label-kb-cb-mc-walk-over-hey-kb-how-not-be-here_c1 with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "Kev! I honestly didn't expect to see you here, man."
    play voice4 kevin_happy_heh4 noloop
    kb "How could we not be here, man? You're my best friend after all!"
    scene e09s06-102 mc-true-kb-till-the-end-man_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "True! Can't imagine a Fetish Locator Party without you, man!"
    play voice4 kevin_happy_ooh noloop
    kb "Absolutely! Friends till the end, man!"
    scene e09s06-103 cb-walks-over-hey-mc-nice-see-you-cb-hope-that-true_c1 with dissolve
    play voice5 chloe_hey_whisper noloop
    cb "Hey, [mcname]!"
    play voice2 mc_thinking_hm noloop
    mc "It's good to see you, Chloe!"
    cb "Mmmmmm, I hope that's true."
    scene e09s06-104 mc-surprised-oh-cb-reacts_c1 with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "Oh?"
    play voice5 chloe_happy_mmm noloop
    if d20s03_sex is True:
        cb "You know, after last time... I'm happy to see you again."
    elif d13s01_kevin_feltching is True and d20s03_sex is False:
        cb "Just hoping to spend some quality time with you, is all."
        scene e09s06-105 mc-even-after-cb-maybe-change-mind_c1 with dissolve
        play voice2 mc_arrogant_hm1 noloop
        mc "Even after..."
        cb "Who knows? Maybe you'll change your mind."
    else:
        cb "You know, it's just good to spend some time with you."
    scene e09s06-106 moh-meaning-ask-kb-got-tickets-this-morning_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Well, I'm happy you both can make it."
    if d20s03_sex is True:
        mc "Oh, I've been meaning to ask you! When are you two leaving for the big day?"
        play voice4 kevin_thinking_hmm5 noloop
        kb "We actually just got our tickets this morning!"
        scene e09s06-107 mc-congrats-cb-yeah-both-excited_c1 with dissolve
        play voice2 mc_happy_a1 noloop
        mc "Oh, congrats! That's awesome!"
        play voice4 kevin_thinking_yeah1 noloop
        cb "Yeah, we're both pretty excited."
    else:
        mc "So anything new with you two?"
        play voice4 kevin_thinking_hmm5 noloop
        kb "Actually, we're going to go on a trip!"
        scene e09s06-107 mc-congrats-cb-yeah-both-excited_c1 with dissolve
        play voice2 mc_happy_a1 noloop
        mc "Oh, that's awesome! When do you two leave?"
        play voice4 kevin_thinking_yeah1 noloop
        cb "In a few days! It's pretty exciting stuff."
    scene e09s06-108 mc-smile-how-long-plan-be-gone-kb-decided-move_c1 with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "How long are you two planning on being gone?"
    play voice4 kevin_disappointed_oh1 noloop
    kb "We've actually decided... we're not coming back. We decided to move!"
    play voice2 mc_surprised_uh3 noloop
    mc "What! Oh my God! That's great! Wow... maybe a little unexpected, but that's fucking great!"
    scene e09s06-109 mc-that-great-cb-yes-cant-wait_c1 with dissolve
    play voice5 chloe_yes_yap2 noloop
    cb "It is! We both can't wait."
    scene e09s06-110 kb-hoping-have-fun-before-mc-right-place-should-keep-making-rounds_c1 with dissolve
    play voice4 kevin_happy_heh3 noloop
    kb "But we are hoping to have a little bit more fun before we go."
    play voice2 mc_thinking_hmm8 noloop
    mc "Well you're in the right place!"
    mc "But, I should keep making the rounds."
    scene e09s06-111 kb-of-dont-keep-cb-deff-see-later_c1 with dissolve
    play voice4 kevin_yes_yes1 noloop
    kb "Of course! Don't let us keep you."
    play voice5 chloe_yes_aga2 noloop
    cb "We'll {i}definitely{/i} see you later!"
    scene e09s06-112 mc-walk-away-end-label_c1 with dissolve
    pause

    jump e09s06_part_2_menu

label e09s06_ah_tr:

    scene e09s06-113 label-ah-mc-walk-over-ah_c1 with dissolve
    pause
    if date_ah is True:
        scene e09s06-114 mc-what-pleasant-surprise-ah-can-say-same-you_c1 with dissolve
        play voice2 mc_hey_hey6 noloop
        mc "Aaleyah! What a pleasant surprise!" id e09s06_ah_tr_160f0cff
        play voice4 aaleyah_hey_hey1 noloop
        ah "I can say the same to you!"
        scene e09s06-115 mc-oh-ah-mhm-mc-really-now_c1 with dissolve
        play voice2 mc_surprised_huh7 noloop
        mc "Oh?"
        play voice4 aaleyah_yes_aga1 noloop
        ah "Mmhmmm. Been thinking about you lately... about the last time I saw you."
        mc "Really now."
        scene e09s06-116 ah-seductively-looking-mc_c1 with dissolve
        play voice4 aaleyah_yes_yeah1 noloop
        ah "Mmmmmhmmmmm... It's a very {i}fond{/i} memory for me."
        play voice2 mc_thinking_mmm6 noloop
        mc "I feel the same."
        ah "Good, good... In fact, I was thinking-"
    else:
        scene e09s06-114 mc-what-pleasant-surprise-ah-can-say-same-you_c1 with dissolve
        play voice2 mc_hey_hey6 noloop
        mc "Hey, Aaleyah!" id e09s06_ah_tr_b5b52c1a
        play voice4 aaleyah_hey_hey1 noloop
        ah "Hey, [mcname]."
        scene e09s06-115 mc-oh-ah-mhm-mc-really-now_c1 with dissolve
        play voice2 mc_thinking_mmm6 noloop
        mc "Happy you and Terrell could make it tonight."
        play voice4 aaleyah_yes_yeah1 noloop
        ah "Yeah, me too."
        scene e09s06-116 ah-seductively-looking-mc_c1 with dissolve
        play voice4 aaleyah_happy_mmm1 noloop
        ah "Hopefully I can have a little bit of fun tonight."
    scene e09s06-117 tr-comes-over-hey-mchey-tr_c1 with dissolve
    play voice5 terrell_hey2 noloop
    tr "Hey, [mcname]."
    play voice2 d2s9_mchey noloop
    mc "Hey, Terrell. Glad you both could make it to the party!"
    play voice4 aaleyah_angry_egh1 noloop
    scene e09s06-118 ah-ugh-leaves_c1 with dissolve
    ah "Ugh..."
    scene e09s06-119 mc-what-that-about-tr-had-huge-fight_c1 with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "What's up with Aleyah?"
    play voice5 terrell_aah noloop
    tr "Oh, we got into a huge fight earlier."
    scene e09s06-120 mc-what-for-tr-she-transfer-schools_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "About what?"
    play voice5 terrell_angry2 noloop
    tr "She decided to transfer schools."
    scene e09s06-121 mc-what-seriously-tr-yes-explains_c1 with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What? Seriously?"
    play voice5 terrell_aga2 noloop
    tr "Uh huh... she's actually going to be going to the same school as that super hot chick that's here."
    scene e09s06-122 mc-more-specific-tr-chick-france_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Most of the women here are attractive, you'll have to be more specific."
    play voice5 terrell_mmm1 noloop
    tr "Uhm... her name is... France? I think?"
    mc "Do you mean Londyn?"
    scene e09s06-123 tr-realization-mc-didnt-work-well-wrong-name_c1 with dissolve
    play voice5 terrell_yeah1 noloop
    tr "That's it! Yeah, 'I see London, I see France'. That's my mnemonic device to remember her name."
    play voice2 mc_no_nah2 noloop
    mc "It didn't work that well... And you spelled her name wrong."
    scene e09s06-124 tr-what-mean-wrong-name-mc-nevermind_c1 with dissolve
    play voice5 terrell_huh3 noloop
    tr "What do you mean 'spelled her name wrong'?"
    play voice2 mc_disappointed_ehh4 noloop
    mc "Never mind."
    scene e09s06-125 tr-mc-look-over-ah-decided-she-moving-mc-uh-huh_c1 with dissolve
    play voice5 terrell_hmm3 noloop
    tr "But yeah, she decided that she's moving and I don't know if our relationship will survive long distance. But I'm willing to give it a shot."
    play voice2 mc_yes_aga2 noloop
    mc "Uh huh..."
    scene e09s06-126 tr-turns-back-mc-appreciate-party-mc-so-he-tr-as-long-not-ah_c1 with dissolve
    play voice5 terrell_hey1 noloop
    tr "Anyways, man, appreciate the party! I'm looking forward to having some sex with some women!"
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah, uhhh, so am I?"
    tr "As long as it's not Aaleyah." id e09s06_ah_tr_c2272e22
    scene e09s06-127 mc-fuck-me-look-ah-right-keep-making-rounds_c1 with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Right... Well, I should keep making the rounds."
    play voice5 terrell_wooh noloop
    tr "Yeah man! I'll see you later, after I have some sex!"
    scene e09s06-128 tr-goes-towards-ah_c1 with dissolve
    pause
    scene e09s06-129 mc-goes-back-party_c1 with dissolve
    pause

    jump e09s06_part_2_menu

label e09s06_jdg:

    scene e09s06-130 label-jdg-mc-approach-judge_c1 with dissolve
    pause
    scene e09s06-131 mc-hello-both-mh-jdg-reply-hi_c1 with dissolve
    play voice2 mc_hey_hello noloop
    mc "Hello to the both of you!"
    play voice4 girl27_hey_sexy noloop
    jdg "Evening, [mcname]."
    play voice5 dahlia_yes_ugu noloop
    mh "Hello."
    scene e09s06-132 mh-hold-glass-just-time-keep-jdg-company-mc-sure_c1 with dissolve
    play voice5 lissa_laugh noloop
    mh "Perfect timing. I was just about to refresh our drinks. Mind keeping the Judge company while I'm gone?"
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, not a problem at all!"
    play sound sfx_heels_steps1 loop
    scene e09s06-133 mh-leaves-for-a-while_c1 with dissolve
    pause
    stop sound fadeout 2.5
    scene e09s06-134 mc-surprised-see-here-jdg-why-that_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 2.0
    mc "I have to say, I'm a little surprised to see you here."
    play voice4 girl27_thinking_hmm4 noloop
    jdg "Mmmm, and why's that?"
    scene e09s06-135 mc-well-fisrt-fl-party-jdg-it-is_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Well, this is your first Fetish Locator party, isn't it?"
    play voice4 girl27_yes_simple3 noloop
    jdg "It is!"
    scene e09s06-136 mc-just-odd-time-jdg-ask-why-because-new-managerment_c1 with dissolve
    play voice2 mc_thinking_hm noloop
    mc "Just... an odd time to be trying it out, kind of."
    play voice4 girl27_arrogant_huh1 noloop
    jdg "What, because of the rebrand, new management, that stuff?"
    mc "Yep, that stuff. Especially with how familiar you are with the court case surrounding the... former owner."
    scene e09s06-137 jdg-looks-mc-that-doo-knows-what-look-for-only-positive-feedback_c1 with dissolve
    play voice4 girl27_happy_hmm3 noloop
    jdg "That I do. So I know what to look for."
    jdg "But, our mutual acquaintance has only said positive things about you and the new team running things."
    scene e09s06-138 jdg-seductive-look-can-have-fun-here-mc-dont-think_c1 with dissolve
    play voice4 girl27_thinking_mmm noloop
    jdg "And I think I can have a little bit of fun here too."
    play voice2 d2s12_emmm noloop
    mc "I don't think-"
    scene e09s06-139 jdg-not-usual-thing-could-get-rough-fuck-closes-mc-from-brute_c1 with dissolve
    play voice4 girl27_arrogant_hm5 noloop
    jdg "Not my usual thing, of course, but I think I could get a good, rough fucking here."
    jdg "Especially from a vicious brute like you."
    scene e09s06-140 mc-not-sure-if-jdg-quiet-dont-ruin-for-me_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "I don't know if-"
    play voice4 girl27_disappointed_mff noloop
    jdg "Quiet, don't ruin this for me."
    scene e09s06-141 jdg-stops-mc-talking-imagines_c1 with dissolve
    play voice4 girl27_thinking_hmm8 noloop
    jdg "I can imagine it, you, with your nice hard cock... fucking me. Mercilessly. Your shaft disappearing into my asshole."
    jdg "Pounding into me, harder, and harder... it hurts, but hurts {i}so good...{/i} Your balls slapping into me as you jackhammer your dick, cumming inside my asshole, filling me up-"
    play sound sfx_heels_steps1 loop
    scene e09s06-142 mh-returns-drink_c1 with dissolve
    pause
    stop sound fadeout 1.0
    scene e09s06-143 mh-hope-not-interupting-jdg-nothing-all_c1 with dissolve
    play voice5 lissa_ha noloop
    mh "Sorry, hope I'm not interrupting you two."
    play voice4 girl27_no_happy noloop
    jdg "Oh no! Not at all!"
    scene e09s06-144 mc-nope-deff-not-interupting-mh-good-here-drink-judge_c1 with dissolve
    play voice2 mc_no_nope2 noloop
    mc "Nope, definitely not interrupting, at all."
    play voice5 lissa_ugu2 noloop
    mh "Good! Here is your drink, Judge."
    scene e09s06-145 jdg-thanks-takes-drink-mc-hate-leave-two-other-guests_c1 with dissolve
    play voice4 girl27_thinking_hmm5 noloop
    jdg "Thank you!"
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "Well, I hate to leave you two, but there are more guests to attend to."
    scene e09s06-146 mh-ofc-excelent-host_c1 with dissolve
    play voice5 lissa_yes noloop
    mh "Of course! You've been an excellent host, [mcname]. I'd hate to keep you from your adoring fans."
    scene e09s06-147 mc-walks-away-end-label_c1 with dissolve
    pause

    jump e09s06_part_2_menu

label e09s06_tm:

    scene e09s06-148 mc-walks-over-tm_c1 with dissolve
    pause
    scene e09s06-149 mc-hey-tm-been-while-tm-prolly-last-party_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Hey, Talia! It's been awhile."
    play voice4 girl23_yes_yeeeah2 noloop
    tm "Yeah, probably since the last party."
    scene e09s06-150 mc-that-was-wild-night-tm-agrees_c1 with dissolve
    play voice2 d9s2_ugu noloop volume 1.6
    mc "Uh huh. That one was pretty wild, right?"
    play voice4 girl23_happy_relief noloop
    tm "It was... that it was."
    scene e09s06-151 mc-polite-what-been-upto-tm-got-mueer-gig_c1 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "So what have you been up to since then?"
    play voice4 girl23_thinking_hmm3 noloop
    tm "Well, the school year finished up, got a little summer gig. Nothing too crazy."
    scene e09s06-152 tm-yeah-tm-sound-you-had-crazy-summer_c1 with dissolve
    play voice2 d9s2_yeah noloop volume 1.7
    mc "Yeah."
    play voice4 girl23_happy_laugh1 noloop
    tm "Sounds like you've had a bit more of a crazy summer though."
    mc "Just a little bit... with the start up, and the-"
    scene e09s06-153 tm-lc-trial-mc-pretty-nuts-watch-news_c1 with dissolve
    play voice4 girl23_thinking_hmm4 noloop
    tm "Lydia's trial."
    play voice2 mc_yes_yeah3 noloop
    mc "Uhm... yep. It's been pretty nuts to watch on the news."
    scene e09s06-154 tm-so-much-info-mc-just-seen-news-tm-that-wild_c1 with dissolve
    play voice4 girl23_angry_ergh1 noloop
    tm "There's so much information coming out, with the servers, and the app, and... did you know about any of that stuff?"
    play voice2 mc_disappointed_ah1 noloop
    mc "I've... pretty much just seen what's on the news. That there was some shady stuff happening behind the scenes, that Lydia was behind it all, the whole 'retention program' being kind of super illegal..."
    tm "Yeah, that's wild."
    scene e09s06-155 mc-uncomfortable-never-thought-see-here-tm-always-enjoyed-parties_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "I have to say though, I never thought I'd see you here."
    play voice4 girl23_disappointed_oh noloop
    tm "What can I say? I did always really enjoy these."
    play sound sfx_cloth_rustling2
    scene e09s06-156 tm-puts-hand-mc-chest-eps-were-there-knows-how-liven-up-place_c1 with dissolve
    play voice4 girl23_thinking_hmm1 noloop
    tm "Especially when you were there."
    play voice2 mc_surprised_oh1 noloop
    mc "Oh, well, what can I say? I just know how to liven up the place."
    scene e09s06-157 tm-ill-say-mc-wel-uhm_c1 with dissolve
    play voice4 girl23_yes_yeeeah1 noloop
    tm "I'll say..."
    play voice2 mc_thinking_mmm4 noloop
    mc "Well, uhm-"
    scene e09s06-158 tm-been-long-summer-thinks-really-cool-fl-rebooted_c1 with dissolve
    play voice4 girl23_happy_relief noloop
    tm "I... I know I was sounding a little stand offish, it's just kind of been a long summer... But I do think it's super cool what you're doing with Fetish Locator Rebooted."
    scene e09s06-159 mc-thanks-tm-deff-hope-not-last-party_c1 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "Thank you, Talia."
    play voice4 girl23_thinking_hmm2 noloop
    tm "I definitely hope that this isn't the last party that happens."
    play sound sfx_cloth_rustling3
    scene e09s06-160 mc-things-go-smooth-wont-be-tm-good_c1 with dissolve
    play voice2 mc_hey_hey9 noloop
    mc "Hey, if things go according to plan - it won't be."
    play voice4 girl23_thinking_oh noloop
    tm "Good."
    scene e09s06-161 mc-starts-step-away-have-other-folk-tm-get-it_c1 with dissolve
    play voice2 mc_yes_okay3 noloop
    mc "Enjoy the party. Gotta make sure I say 'hello' to everyone."
    play voice4 girl23_yes_yeah noloop
    tm "Have fun, [mcname]."
    scene e09s06-162 mc-walk-back-end-label_c1 with dissolve
    pause

    jump e09s06_part_2_menu

label e09s06_part_2_continue:

    scene e09s06-163 mc-standing-thinking_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.7
    mct "I should probably start getting ready for the main event..."
    mct "Even though AmRose and Stacy told me absolutely nothing about what I was going to be doing." id e09s06_part_2_continue_902d1357
    scene e09s06-164 mc-walking-through-party-thinking_c1 with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "Except that I should be ready for a 'fuck-a-thon'... Which sounds pretty intense."
    mct "Well... here goes nothing!"

    jump e09s06_part_3

label e09s06_part_3:

    $ renpy.music.set_volume(0.0, 3.0, "music")
    $ renpy.music.set_volume(1.0, 3.0, "music2")
    scene e09s06-165 label-part-three-crowd-gathered-arj-sy-middle_c1 with Fade(0.5, 0.5, 0.5)
    pause
    scene e09s06-166 arj-hello-welcome-fl-rebooted-everyone-woooo_c1 with dissolve
    play voice4 amrose_hey_active2 noloop
    arj "Good evening, everyone! Thank you so much for coming out to the first ever party for Fetish Locator Rebooted!"
    play voice5 dahlia_happy_woohoo1 noloop
    play voice6 chloe_happy_woohoo1 noloop
    play voice7 terrell_wooh noloop
    play voice8 girl23_happy_woohoo noloop
    play voice2 girl30_happy_woohoo1 noloop
    play sound sfx_crowd_applause4
    "Everyone" "WOOOOOOOO!!!"
    scene e09s06-167 arj-sy-close-up-sy-means-much-arj-have-ton-festivities-tonight_c1 with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "We can't tell you how much it means to us that you're all here. Seriously, this is better than we could have ever hoped for!"
    play voice4 amrose_happy_yeah1 noloop
    arj "We have a ton of festivities planned tonight, for those of you who haven't already indulged! But, it's time to get into our main event!"
    scene e09s06-168 sy-being-just-small-first-party-has-special-even-planned_c1 with dissolve
    play voice3 stacy_thinking_emm4 noloop
    sy "Being just a small, little start up - our first party has a {i}special{/i} event planned."
    play sound sfx_barefoot_steps1 loop
    scene e09s06-169 arj-this-mc-most-know-sy-tonight-few-have-fun-with-him_c1 with dissolve
    play voice4 amrose_thinking_hmm1 noloop
    arj "This is our dear [mcname], who most of you know and love!"
    play voice3 stacy_yes_ugu1 noloop
    sy "And tonight, a special few of you are going to have the chance to have some fun with him! Right here, right now!"
    stop sound fadeout 1.0
    scene e09s06-170 arj-tonight-main-even-just-starting-out_c1 with dissolve
    play voice4 amrose_yes_happy1 noloop
    arj "Tonight's main event is a sort of auction, to spend some public sexy time with [mcname]."
    arj "Just starting out, we are looking for every donor we can to help keep our dream going."
    scene e09s06-171 sy-talking-explains-auction-works-money-go-server-ui-dev-etc_c1 with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    sy "So the way the auction will work, is that you can start screaming out donations - we're looking to raise $10,000."
    sy "That money will go to servers, UI development, improving hardware-"
    scene e09s06-172 medium-shot-arj-along-that-invested-more-events-sy-explains-goal_c1 with dissolve
    play voice4 amrose_arrogant_hmm2 noloop
    arj "Along with that, that money will be invested into being able to do more events like this!"
    play voice3 stacy_thinking_oh2 noloop
    sy "If we raise enough money to reach our goal, then everyone who donated will get a chance to come up here and have some fun with [mcname]!"
    sy "But only if we reach our goal. If we don't... then our poor stud will only have himself to play with tonight." id e09s06_part_3_7bdb3618
    scene e09s06-173 arj-who-beging-bidding_c1 with dissolve
    play voice4 amrose_arrogant_huh2 noloop
    arj "So - who would like to begin the bidding?"
    scene e09s06-174 crowd-shot_c1 with dissolve
    pause
    scene e09s06-175 mc-thinking-while-looking-crowd_c1 with dissolve
    play voice2 mc_angry_errr5 noloop
    mct "All right, now we just have to hope this works... Please, let this work!"
    mct "Uh oh... it's too quiet. What are we going to do if no one donates?"
    mct "Is Fetish Locator Rebooted really going to die before it even gets a chance to live?"
    scene e09s06-176 someone-bets-five-hundos-mct-wait-who-bet_c1 with dissolve
    play voice4 girl28_happy_woohoo1 noloop
    "???" "Five hundred dollars!"
    play voice2 mc_angry_huh2 noloop volume 1.4
    mct "Wait! Who said that!?"
    scene e09s06-177 lo-put-bid-hr-match-it_c1 with dissolve
    play voice4 girl28_arrogant_hah2 noloop
    lo "I'll put down five hundred bucks! His dick is worth that alone!"
    play voice5 girl30_arrogant_yeah1 noloop
    hr "And I'll match her bid!"
    scene e09s06-178 arj-sy-smiling-arj-that-thousand-sy-dont-shy-all-want-chance-fuck-mc_c1 with dissolve
    play voice4 amrose_happy_woo noloop
    arj "That's a thousand down! The first one is always the worst!"
    play voice3 stacy_hey noloop
    sy "Come on, don't be shy! We all want a chance to fuck [mcname] tonight!"
    scene e09s06-179 cb-bets-four-kb-another-two_c1 with dissolve
    play voice4 chloe_hey_active noloop
    cb "$400!"
    play voice5 kevin_happy_yay1 noloop
    kb "$200!"
    scene e09s06-180 tm-adds-hundred-kb-another-two_c1 with dissolve
    play voice6 girl23_happy_laugh2 noloop
    tm "$100!"
    play voice5 kevin_happy_ooh noloop
    kb "Shit, I'll do another $200!"
    scene e09s06-181 mk-bet-three-for-dick-ah-match-it_c1 with dissolve
    play voice3 min_disappointed_mph noloop
    mk "$300 for that dick!"
    play voice4 aaleyah_happy_phew noloop
    ah "I'll put up $300 too!"
    scene e09s06-182 tr-hey-ah-shut-it_c1 with dissolve
    play voice5 terrell_huh2 noloop
    tr "Hey!"
    play voice4 aaleyah_angry_grrr1 noloop
    ah "Quiet, Tyrell. Don't act like you're not going to watch [mcname] fuck me."
    tr "I-... Yeah..."
    scene e09s06-183 someone-bets-thousand-arj-sy-very-surprised-arj-thanks-sy-who-highest-bidder-so-far_c1 with dissolve
    play voice5 cynthia_hey_angry noloop
    "???" "A thousand dollars."
    play voice4 amrose_surprised_huh1 noloop
    arj "Wow! Thank you... Whoever just bid a thousand!"
    play voice3 stacy_yes_yeah2 noloop
    sy "Yeah! Who is our highest bidder so far?"
    scene e09s06-184 cl-in-crowd-would-be-me-mc-thinks-not-expected-lewald-aw-offcam-offers-five_c1 with dissolve
    play voice5 cynthia_happy_laugh1 noloop
    cl "That would be me."
    play voice2 mc_angry_huh1 noloop
    mct "Holy shit, I did {u}not{/u} expect that from Lewald."
    play voice6 kanya_happy_wooh noloop
    aw "$500!!"
    play sound sfx_heels_steps1 loop
    scene e09s06-185 mc-sees-aw-where-were-aw-running-company_c1 with dissolve
    play voice2 mc_hey_hey10 noloop
    mc "Allison! I was wondering where you were!"
    play voice6 kanya_arrogant_laugh noloop
    aw "Running a company ain't easy."
    stop sound fadeout 1.0
    scene e09s06-186 mc-come-on-cant-donate-work-here-aw-technically-not-her_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "But come on, I can't let you donate! You work here."
    play voice6 kanya_thinking_eeh5 noloop
    aw "Strictly speaking, it's not from me."
    scene e09s06-187 mc-then-who-aw-another-time-now-aution-run-mc-shit-right_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, than who-?"
    play voice6 kanya_no_nah2 noloop
    aw "That's a story for a different time. Right now, we've got an auction to run!"
    mc "Oh shit! That's right!"
    scene e09s06-188 gang-turns-back-crowd-sy-arj-talk_c1 with dissolve
    play voice3 stacy_hey_happy2 noloop
    sy "AmRose and I have also both decided to put in $500! Which brings us to the halfway mark!"
    play voice4 amrose_yes_yeah2 noloop
    arj "We're doing great so far, we just need a little more to get us to the top! Who else would like to bid?"
    scene e09s06-189 mc-nervous-looking-crowd-thinking_c1 with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "Uh oh... We were doing so well. Come on, we just need a few more bids..."
    mct "Come on, there has to be someone else who wants to bid..."
    scene e09s06-190 crowd-shot-arj-asking-anyone-else-mc-fuck-fuck-sy-going-once_c1 with dissolve
    play voice4 amrose_hey_attention noloop
    arj "Anyone else?"
    play voice2 mc_angry_hm1 noloop
    mct "Oh God... fuck. Fuck, fuck, fuck."
    scene e09s06-191 arj-sy-nervous-going-twice-mct-this-is-it_c1 with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "Going once?"
    play voice4 amrose_arrogant_huh4 noloop
    arj "Twice?"
    mct "This is it..."
    scene e09s06-192 jdg-steps-forward-fck-it-five-grand_c1 with dissolve
    play voice5 girl27_angry_err3 noloop
    jdg "Fuck it, $5,000!"
    scene e09s06-193 arj-mc-sy-shocked-what-jdg-what-have-as-much-fun-as-others_c1 with dissolve
    play voice4 amrose_surprised_uh2 noloop
    play voice3 stacy_surprised_ah2 noloop
    play voice2 mc_surprised_what8 noloop
    mc "What!?!"
    play voice5 girl27_arrogant_yeah2 noloop
    jdg "I want to have fun just as much as everyone else!"
    scene e09s06-194 sy-arj-sharing-look-sy-does-that-mean-arj-made-it_c1 with dissolve
    play voice3 stacy_surprised_huh2 noloop
    sy "Does that mean..."
    play voice4 amrose_happy_yeah2 noloop
    arj "We made it! We reached our goal!"
    play sound sfx_cloth_rustling2
    scene e09s06-195 arj-sy-hug-sy-holy-shit-made-it-aw-not-quite_c1 with dissolve
    play voice3 stacy_happy_yay3 noloop
    sy "Holy shit! We actually did it!"
    play voice4 kanya_arrogant_ha noloop
    aw "Not quite yet, you two."
    scene e09s06-196 arj-sy-look-mc-aw-first-man-has-fulfill-deal-sy-that-right-time-fucking_c1 with dissolve
    play voice4 kanya_thinking_hmm3 noloop
    aw "First, our man here has to fulfill his part of the deal."
    play voice3 stacy_arrogant_ha2 noloop
    sy "That's right! [mcname], it's time to get to fucking!"
    scene e09s06-197 sy-turns-crowd-who-first-arj-start-festivities-first-bid_c1 with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "All right! Who wants to go first!?"
    play voice4 amrose_thinking_emm noloop
    arj "I think it's only fair that Londyn and Hana start off the festivities, as they were the first to bid!"
    scene e09s06-198 sy-sounds-fair-end-scene_c1 with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Sounds fair to me!"

    stop music fadeout 20.0
    stop music2 fadeout 20.0
    jump e09s07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
