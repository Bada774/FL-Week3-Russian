

image d03s06b-a1-s1 = Movie(play = "images/Week-1/d03s06b-a1-s1.webm", start_image = "d03s06b-28 cam-2-mk-arj-fuck-me-3-phone")

image d03s18-09-flash:
    pause 0.10
    "d03s18-09 mc-no-what-am-doing-with-flash"
    pause 0.30
    "d03s18-09 mc-no-what-am-doing"
    pause 0.1
    "d03s18-09 mc-no-what-am-doing-with-flash"
    pause 0.01
    "d03s18-09 mc-no-what-am-doing"
    pause 0.01
    "d03s18-09 mc-no-what-am-doing-with-flash"
    pause 0.02
    "d03s18-09 mc-no-what-am-doing"

image d04s18-12-finger-anim:
    pause 0.2
    "d03s18-12-02 delete-picture-3"
    pause 0.2
    "d03s18-12 delete-picture-2"
    repeat

image d03s02-43-mc-masturbate-anim:
    "d03s02-43-over mc-masturbates-0"
    pause 0.2
    "d03s02-43-over mc-masturbates-1"
    pause 0.2
    "d03s02-43-over mc-masturbates-2"
    pause 0.2
    "d03s02-43-over mc-masturbates-3"
    pause 0.2
    "d03s02-43-over mc-masturbates-4"
    pause 0.2
    "d03s02-43-over mc-masturbates-3"
    pause 0.2
    "d03s02-43-over mc-masturbates-2"
    pause 0.2
    "d03s02-43-over mc-masturbates-1"
    pause 0.2
    repeat



label week_1_recap:

    scene black
    show screen scene_transistion(_("Recap of Week-1 Events"))
    with Fade(0.3, 0.3, 0.3)
    pause
    hide screen scene_transistion
    show screen skip_recap("week_2_recap", 1)
    scene d01s01-01-1
    with Fade(0.3, 0.3, 0.3)
    pause
    $ renpy.music.set_volume(0.5, 0.0, "music")
    play music recap_music fadein 2.0
    scene d01s01-01-3
    pause 0.2
    scene d01s01-01-5
    pause 0.3
    scene d01s01-01-7
    pause 0.3
    scene d01s01-09 look-from-bed
    pause 0.4
    scene d01s01-11 look-at-sleeping-hana
    "After two weeks away, our hero [mcname] finally returned to college..."
    if d01s01_peeked_on_hana is True:
        scene d01s01-12 lifting-blanket
        "[mcname] noticed the new girl his roommate brought home."
    else:
        scene d01s01-24 mc-shower
        "[mcname] ignored the woman in his roommate's bed and went for a shower."
    scene d01s01-26 lydia-dream
    "[mcname] had his sights on one spectacular woman - the woman of his dreams - Lydia Cox."
    scene s02-07-kb-phone-talk
    "Then it was off to class, with his best male friend, Kevin Bennet. Keven introduced him to a new app."
    scene s02-19 phone-bg
    "FETISH LOCATOR. [mcname] promptly signed up for the app."
    scene s02-16-arj-sad
    show s02-16-arj-half-smile
    "With a few minutes left before class started, [mcname] made time for his best female friend, AmRose."
    scene s03-08 bg phone-message
    "[mcname] went to a basketball game to support his roommate, Pete and learned more about Fetish Locator from Kevin."
    scene s03-04 sitting-with-kb
    show s03-04-over kb-talks
    "Fetish Locator uses their own system of points. The points can be used for photos and exclusive events."
    scene s04-04 empty-corridor
    show s04-04-over pb-pointing-at-you-talks
    "Pete told [mcname] that Lydia would be at a Fetish Locator Party on Wednesday night, and that tickets cost 50 points!"
    if d01s05_points > 5:
        if d01s05_points == 12:
            scene s05-117-mc-cum-3
        else:
            scene s05-121-mc-cum-on-couch-3
        "[mcname] participated in a blitz challenge with AmRose after she fell asleep while the two watched a movie."
    elif fl_cumshot is True:
        scene s05-10 mc-with-dick
        show s05-10-over-2 cum-3
        "[mcname] participated in a blitz challenge all alone in his dorm room."
    scene s06-06 makinf-selfy
    "On Tuesday, Kevin informed [mcname] that it was possible to post ads on Fetish Locator."
    scene s06-11 lydia-medium
    "After class, he saw the sweet, lovely Lydia. But couldn't bring himself to talk to her yet."
    if d02s12_points == 12:
        scene s12-05 polly-bench-skirt
        "His advertisement brought him to Polly Wilson, who had something special planned."
    scene d03s08-31-empty-room at image_blur(7)
    show x-phone-background
    show d03s09-would-you-like-to-buy-it
    "[mcname] earned enough points for the ticket to the exclusive Fetish Locator Party hosted by Min."
    scene d03s10-33 cl-ill-take-it
    "Mustering up all his courage, [mcname] decided to bring Lydia a beverage and try to talk to her. However, her friend Cynthia cockblocked our hero."
    scene d03s16-12 lc-leaving
    "As luck would have it, it was Lydia that found him later on. Just as they were getting know each other, she was dragged away."
    scene d03s16-66 lc-pulled-by-jerome-2
    "During the Party's main event, [mcname] noticed Lydia getting literally dragged away."
    scene d03s17-29 lc-would-get-some-rest
    "Our hero intervened and stoped Lydia's assault and abduction. Lydia spent most of that night in delightful conversation with her hero. Eventually she fell asleep right besides [mcname]."
    scene d03s18-05 mc-with-phone
    "[mcname] became uncomfortably aroused enjoying the sight, sound, and smell of his obsession laying next to him."
    scene d03s18-06 mc-with-phone-2
    "An entire party worth of edging and blueballing had him going crazy. But he focused on trying to get some sleep. Just as his eyes closed, his phone woke him with a Blitz Challenge! Without thinking, he whipped out his engorged manhood and prepared to bust a nut."
    scene d03s18-07 mc-look-at-the-phone
    show d03s18-07-over mc-look-at-dick-pick
    "Fetish Locator took a picture of [mcname]'s hard cock while he was laying in bed next to Lydia."
    scene d03s18-12 delete-picture-2
    show d04s18-12-finger-anim
    "He panicked, tried to shut off his phone, delete the app, and do anything he could think of to prevent that picture from being uploaded."
    scene d03s18-13 phone-on-table-dark
    pause
    scene d03s18-14 phone-on-table
    "Despite his best attempts, he failed. Although he didn't realize this yet."
    scene d04s04-29 lc-nk-can-i-get-you-somthing
    "The next day Lydia and [mcname] met for a \"coffee date\". It turned out that the barista, Nora was Lydia's biggest fan. Knowing Nora's business was struggling, a plan to help her out artsted forming in [mcname]'s mind."
    scene d04s04-37 nk-talk-with-coffee
    "Lydia didn't take much convincing. She agreed to perform a brief concert at Nora's Coffee House..."
    scene d04s04-45 lc-mc-talking-on-phone
    if fl_enema is True:
        "Unfortunately, his coffee date with the love of his life was interrupted by AmRose..."
        scene d04s05-07 arj-removing-the-bottle
        "[mcname] helped out his friend who was in trouble while attempting to complete the Fetish of the Day Challenge."
    else:
        scene d04s05-05 arj-sick
        "Unfortunately, his coffee date with the love of his life was interrupted by AmRose... who was drunk off her ass and in dire need of his assistance."
    scene d04s05-20 mc-sitting-beside
    if is_antagonist_mode is False:
        "[mcname] came to her rescue, and in the process, learned that she was put into a secretive \"VIP Fetish Challenge Program\" to win one million dollars."
    else:
        "[mcname] came to her rescue, and in the process learned that she was being blackmailed and coerced by someone at Fetish Locator."
    scene d04s08-09 mc-fear-2
    "When he returned home that evening, [mcname] discovered he was in a nearly identical situation."
    if is_antagonist_mode is False:
        "When he tried to delete the app from his phone, he too got put into the VIP Fetish Challenge Program."
    else:
        "He was being blackmailed as well, by something called the Fetish Locator Retention Program."
    scene d05s01-08 mc-stands-with-phone
    "In the morning he was given a personal challenge. He had to earn 50 points by Monday morning."
    scene d05s05-08 arj-mc-both-in-train
    if is_antagonist_mode is False:
        "A little later that day, he let AmRose know that they were now in the same boat."
    else:
        "A little later that day, he let AmRose know that they were in the same boat of being blackmailed."
    scene black
    "Two weeks prior to the events of the main story..."
    scene s03-101 talk-to-sy
    show s03-101-over sy-pose-2-with-hand-laugh
    if persistent.is_special is True:
        "[mcname] visited home. There he saw his sister, Stacy, for the first time in many months."
    else:
        "[mcname] visited home. His close friend, Stacy, was living there temporarily. It was the first time he had seen her in months."
    if d02s07_seen_sy_shower is True:
        scene s07-106_v2 shower-pose-2-close
        "He could barely keep his eyes off of her."
    if d03s02_stacy_saw_masturbation is True:
        scene d03s02-43 mc-masturbates
        "Likewise, she kept a close eye on him."
    scene d06s02-05 sy-talks
    "On Saturday morning, Stacy moved to be closer to campus, where she will be starting classes in Autumn, and decided to stay at [mcname]'s dorm temporarily."
    scene d06s03-14 arj-sy-talk-3
    "Stacy and AmRose became fast friends. During lunch, AmRose shared how she met [mcname]... He had been dating AmRose's roommate, Karen, during Freshman year."
    scene d06s04-12 lc-mc-both-sit
    "After that lunch, [mcname] enjoyed a lovely date with Lydia and calmed her pre-concert jitters."
    scene d06s06-10 lc-sing-transform-3
    pause
    scene d06s06-47 lc-mc-kiss
    "The concert was a huge success - both for the coffee house's bottom line and for [mcname] and Lydia's budding relationship."
    if date_sy is True:
        scene d06s10-22 mc-sy-hj-top-without-blanket
        "Stacy and [mcname] became quite a bit closer that night too."
    scene d06s10-47 sb-leaving-3
    if date_sy is True:
        "But in the darkness of the night, her luggage was stolen from [mcname]'s room."
    else:
        "Stacy's luggage was stolen from [mcname]'s room that night."
    scene d07s02-56 car-mc-arj-sy-talk
    "On Sunday, [mcname] set Pete on the task of finding Stacy's luggage while he headed out to the beach with AmRose and Stacy for the \"Officially Unofficial\" start of the summer."
    scene d07s04h-33 hr-talk-sit-4-you
    "Surprisingly, while he was swimming he was picked up by Hana - the girl he had spied in Pete's bed almost a week earlier. She revealed that Pete was involved in Fetish Locator."
    if d07s04_hr_seen_arj_and_mk is True:
        scene d07s04-hr-14 hr-watch-this
        "As a form of proof, Hana revealed footage she had from hacking Pete's phone. It was footage showing AmRose and Maria doing the Wednesday Foot Fetish Challenge."
    scene d07s05-35-02 mc-arj-hands
    "At the end of the evening, AmRose and [mcname] took a romantic walk along the pier. AmRose confessed her true feelings for [mcname], even though she knew he was head-over-heels in love with Lydia."
    if date_arj_romance is True:
        scene d07s05-36 mc-arj-kiss
        "[mcname] decided that AmRose would be his secret girlfriend, while Lydia remained his public girlfriend."
    else:
        scene d07s05-38-02 mc-arj-knee-beg
        "[mcname] decided to take AmRose as a fuckbuddy and personal sex slave."
    if date_mes is True:
        scene s11b-02 talk-to-min
        "Over the past week [mcname] and Min, one of his classamtes, have drastically changed their 'friendship'"
        scene d03s13-71-02 mc-going-to-drink-2
        "[mcname] beat her in a pissing contest at her house..."
        scene d05s06-45 mc-mes-after-talk
        "Min and [mcname] became much closer friends while he taught her more about watersports..."
    if date_mh is True:
        scene d03s11-50 lyssa-anim-60
        "During the Party at Min's house, [mcname] met an exceptional woman named Lyssa. It turned out that she was hiding a rather massive secret."
        scene d05s05b-15-02 mh-feet
        "In addition to being a lawyer, she also owns a few properties around the city. Arrangements have been made for Stacy to rent one of her apartments."
        scene d07s04-mh-55 mh-mc-swallow-2
        "On the beach, Sunday, Lyssa and [mcname] shared an unforgettable experience together."
    if date_mk is True:
        scene d03s14-44 mk-bj-start-1
        "During the Magic & Mysticism Event, [mcname] experienced something inexplicably strange."
        scene d06s05-03 mk-enters
        "Later on, Maria interrupted [mcname] in the bathroom with an unusual offer."
        if d06s05_mk_toilet is True or d06s05_mk_cum is True:
            scene d06s05-16 mk-4-talk-2
            "[mcname] took advantage of the oppurtunity to humiliate Maria in a way she did not expect."
    if date_pw is True:
        scene s08-13 polly-in-front-of-mc
        "[mcname] met Polly in the park on Tuesday, where she convinced him to agree to her terms."
        scene s11-03-00 background
        show s11-03-00-over 03-16-pussy-enter
        scene d04s07-42 nk-cums
        "In order to get Polly and Nora together, [mcname] had to come up with a creative redefinition of a blind date. Something that Polly and Nora have both enjoyed twice so far."
        if fl_watersports is True:
            scene d05s04-44 mc-squatting-with-pw
            "Although now [mcname] has gained the upper hand in his dealings with Polly."
        scene d06s07-30 mc-nk-fuck-2-anim00
        "After Lydia's concert at Nora's coffee shop, Nora thanked [mcname] in a very special way."
        if d06s07_creampie is True:
            scene d06s07-54 mc-nk-cum-inside-5-nk-talks
            "Although he pushed his luck too far when he creampied her without asking first, and Nora threw him out."
        scene d07s04-pw-20-02 pw-beach-talk_c1
        "Polly and [mcname] had a lovely walk on the beach on Sunday."
        if d07s04_pw_rimjob is True:
            scene d07s04-pw-40 pw-mc-rimming-2_c2
            "Which surprisingly included Polly enjoying her tongue up his back door."
    if date_dd is True:
        scene d03s01-07 daisy-talk-to-mc
        scene d03s13-25 dd-blow-job-1
        "Wednesday morning, [mcname] was surprised by a half-naked woman next to his bed. Daisy has an infectious personality spreads joy wherever she goes."
        scene d07s04dd-10 dd-mc-bending-for-spank-2-2
        "Especially when it comes to bringing joy to [mcname]. On the beach on Sunday, Daisy really opened up about her submissive desires."
        scene d07s04dd-22-03 dd-mc-talk
        "But she felt unwell in the process..."
    if date_dw is True:
        scene d07s04dw-21 mc-dd-dw-spank-position-2
        "Dahlia has been very clear about her role as a dominatrix. And she enjoys using [mcname] as her plaything."
    scene d03s10-16 aw-talk
    "[mcname] had only a few small interactions with Allison, a driven athlete with a rocking bod."
    if date_cb is True:
        scene d05s02-20 keving-enters
        if persistent.is_special is True:
            "[mcname] learned that accepting Kevin's relationship with Kevin's sister has benefits."
        else:
            "[mcname] learned that accepting the peculiar nature of Kevin's relationship with Chloe has benefits."
    if date_jf is True:
        scene d05s05-42 jf-scared
        "[mcname] was surprised to stumble upon Jessie in a derelict apartment, but not nearly as surprised as she was."
    if date_vw is True:
        scene d07s04vw-63 mc-vw-get-in-position-3
        "Last, but not least, [mcname] and Vanessa explored the real estate market... and each other."
        scene black
    hide screen skip_recap

    jump week_2_recap
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
