label e10s07:

    scene black
    show screen scene_transistion(_("Few days later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.4, 1.5, "music2")
    play music2 music_korean_ending fadein 0.7
    scene e10s07-01 mc-md-mes-sit-table-after-dinner_c1
    with Fade(0.5, 0.5, 0.9)
    pause
    scene e10s07-02 mc-thanks-md-for-dinner_c1 with dissolve
    play voice2 d1s5_mchappy noloop
    mc "Well, thank you for a lovely dinner."
    scene e10s07-03 md-tells-them-wait-more-to-talk_c1 with dissolve
    play voice4 pete_angry_ehh1 noloop
    md "Don't get up. There is one other item I want to discuss."
    scene e10s07-04 mc-whispers-mes-she-talks-to-md_c1 with dissolve
    play voice2 mc_arrogant_pff1 noloop
    mc "*whisper* I told you..."
    play voice3 min_yes_yeah1 noloop
    mes "Of course, father. What can we do for you?"
    scene e10s07-05 md-has-proposals-for-mc-mes_c1 with dissolve
    play voice4 pete_thinking_mmf noloop
    md "It is more what I can do for you. I have a couple proposals for you to...{w} entertain."
    md "Your little project has proven quite beneficial to the current investors."
    scene e10s07-06 mc-happy-to-have-investor-has-materials_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "If you are interested in investing, I can get you materials-"
    scene e10s07-05 md-has-proposals-for-mc-mes_c1 with dissolve
    play voice4 pete_happy_mmm2 noloop
    md "I already invested. Not in your funds, but in your business. I currently own 18 percent of the shares."
    scene e10s07-07 mes-cant-believe-md-already-invested_c1 with dissolve
    play voice3 min_scared_ah1 noloop
    mes "What?! Without even telling me?"
    scene e10s07-08 md-takes-out-tablet_c1 with dissolve
    play voice4 pete_yes_simple3 noloop
    md "You started this business without consulting me. I felt no obligation to inform you before now."
    play sound sfx_paper_rustl1
    scene e10s07-09 md-talks-affordable-mc-not-surprised_c1 with dissolve
    queue voice4 pete_thinking_hmm7 noloop
    md "It was surprisingly affordable. Your current employees seemed more than willing to cash out their shares."
    mct "Not surprising. Like any start-up, they probably figure their shares are worthless until someone offers them a deal."
    scene e10s07-10 mes-furious-blames-md-mc-tries-to-calm-her_c1 with dissolve
    play voice3 min_hey_angry2 noloop
    mes "I can't believe this.{w} This is something I'm doing - we are doing - for ourselves. You want to just-"
    play voice2 shhh noloop
    mc "Shhh, hon. Let's see what he proposes before we react."
    scene e10s07-11 md-hands-tablet-to-mc-he-reaches-take-it_c1 with dissolve
    play voice4 pete_thinking_hm noloop
    md "This is my proposal.{w} I will be presenting it to the board of directors at the next meeting."
    play voice2 mc_thinking_hmm5 noloop
    mc "Of course, you realize that your daughter is the Chairman, er, Chairwoman of the Board."
    play sound sfx_paper_slide1
    scene e10s07-12 mc-hands-tablet-to-mes_c1 with dissolve
    play voice4 pete_happy_relief1 noloop
    md "Of course, and I assume as CEO you have some shares as well. This offer is quite amicable for everyone involved."
    scene e10s07-13 mes-reading-data-on-tablet_c1 with dissolve
    play voice3 min_old_hmm noloop volume 1.3
    mes "You want to turn our company into a wholly owned subsidiary of the family's corporation."
    scene e10s07-14 md-explains-better-use-of-mes-talents_c1 with dissolve
    play voice4 pete_disgust_meh2 noloop
    md "[mcname] can remain there as CEO, but we've recently hired some professionals that can do things better than your rag-tag band of employees."
    scene e10s07-13 mes-reading-data-on-tablet_c1 with dissolve
    play voice3 min_arrogant_hm noloop volume 1.2
    mes "[mcname] is the CMO, I am CEO."
    mes "In your imagination I would just go back to my old job - the one I recently resigned from - I assume?"
    scene e10s07-14 md-explains-better-use-of-mes-talents_c1 with dissolve
    play voice4 pete_yes_simple1 noloop
    md "It would be a better use of your talents. We'll simply refuse and nullify your resignation."
    scene e10s07-15 mc-smirking-at-md-mes-looking-at-him_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "You are of course welcome to present this to the board..."
    play voice3 min_scared_huh noloop
    mes "How can you be so calm about this?!"
    play voice2 mc_angry_cough1 noloop
    mc "But I am confident nothing like that will happen."
    scene e10s07-16 mes-talks-md-being-irritated_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Between the two of us, we already have a controlling interest in our business."
    mc "So, the board rejecting your proposal is just a formality."
    scene e10s07-05 md-has-proposals-for-mc-mes_c1 with dissolve
    play voice4 pete_surprised_huh1 noloop
    md "This is unacceptable. You cannot-"
    scene e10s07-17 mes-mc-smirking-at-md-turn-down-proposal_c1 with dissolve
    play voice3 min_yes_serious noloop
    mes "Yes, we can."
    play voice2 mc_yes_ugu1 noloop
    mc "We have already built a successful business, and have clear goals to make it even more successful."
    scene e10s07-18 md-orders-mes-accept-proposal-has-big-plans_c1 with dissolve
    play voice4 pete_angry_cough1 noloop
    md "Listen to me, daughter. You will accept this proposal. I have big plans for you."
    scene e10s07-19 mc-tells-md-they-have-their-own-plans_c1 with dissolve
    play voice2 mc_no_uhuh1 noloop
    if e10s02_mes_partner is False:
        mc "We have other plans. We don't need your money."
        scene e10s07-20 mc-points-out-they-control-shares_c1 with dissolve
    elif True:
        mc "Eun-Soo has other plans. Would you like to tell him?"
        scene e10s07-20 mc-points-out-they-control-shares_c1 with dissolve
        play voice3 min_yes_active noloop
        mes "Yes, thank you.{w} Father - we don't want your money."
    play voice2 mc_thinking_mmm4 noloop
    mc "As I said, we own a controlling interest."
    play voice3 min_thinking_hmm1 noloop
    mes "We do not want you controlling our business or our lives."
    scene e10s07-14 md-explains-better-use-of-mes-talents_c1 with dissolve
    play voice4 pete_angry_ehh2 noloop
    md "You always have been a strong-willed child, but it is time to grow up."
    play sound sfx_cloth_rustling2
    scene e10s07-21 mes-stand-up-mc-helps-her-with-jacket_c1 with dissolve
    play voice3 min_yes_aga noloop
    mes "I couldn't agree more. This is my adulthood."
    play voice2 mc_thinking_mmm2 noloop
    mc "Thank you again for a lovely meal. I look forward to seeing you again soon."
    scene e10s07-22 mes-anounce-they-are-getting-married_c1 with dissolve
    play voice3 min_thinking_oh noloop
    mes "Oh, there's one other thing you should know."
    scene e10s07-23 mc-faces-md-knows-he-should-ask-permission_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "We're getting married."
    mc "I know that I should ask your permission or blessing, but..."
    scene e10s07-22 mes-anounce-they-are-getting-married_c1 with dissolve
    play voice3 min_happy_mmm noloop
    mes "Well, the wedding is happening whether you approve or not."
    scene e10s07-23 mc-faces-md-knows-he-should-ask-permission_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "So, what do you think?"
    play sound sfx_skirt_off1 volume 2.0
    scene e10s07-24 md-stands-up-walks-to-mc-mes_c1 with dissolve
    pause
    scene e10s07-25 mc-md-face-to-face_c1 with dissolve
    play voice4 pete_pain_mmm2 noloop
    md "You insult me. You reject my council. You reject my plans and expectations."
    md "Now you ask for my daughter's hand?"
    scene e10s07-26 md-accuses-mc-of-disrespect-mc-rejects-notion_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "I never insulted you. I have offered you nothing but respect."
    mc "All I've asked is that you show us the same respect you expect for yourself."
    scene e10s07-27 mc-tells-md-they-are-a-unit_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    if e10s02_mes_partner is True:
        mc "Your daughter and I are a unit. We move together as one."
    elif True:
        mc "Your guidance is no longer necessary. I can look after Min Eun-Soo."
    scene e10s07-28 mc-tells-md-he-takes-care-of-mes-now_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "This is about family. You have a choice."
    scene e10s07-29 md-bows-head-agrees-to-marriage_c1 with dissolve
    play voice4 pete_disappointed_mmf1 noloop
    md "I understand.{w} I underestimated you. Both of you, apparently."
    md "You have my permission, and my blessing."
    play voice5 boy5_happy_wooh1 noloop
    scene e10s07-30 mm-mb-go-congratulate-family_c1 with dissolve
    pause
    scene e10s07-31 mb-always-wanted-a-brother_c1 with dissolve
    play voice5 boy5_happy_relief noloop
    mb "I always wanted a younger brother.{w} Congrats, [mcname]."
    play voice2 d2s9_confused noloop
    mc "Thanks-"
    scene e10s07-32 mm-asking-if-mes-pregnant_c1 with dissolve
    play voice4 claudie_surprised_aah1 noloop
    mm "Are you pregnant?"
    play voice3 min_surprised_what noloop
    mes "What?! No, mom."
    play voice4 claudie_thinking_hmm2 noloop
    mm "And why not? I want grandbabies, and you're brother can't even seem to get a date."
    scene e10s07-33 mb-focued-on-business-mc-not-sterile_c1 with dissolve
    play voice5 boy5_hey_active noloop
    mb "Hey - I'm just focusing on work right now. There's plenty of time."
    play voice4 claudie_arrogant_ha3 noloop
    mm "You're not sterile, are you boy? That might be a deal breaker."
    play voice2 mc_surprised_what1 noloop
    mc "What? No."
    scene e10s07-32 mm-asking-if-mes-pregnant_c1 with dissolve
    play voice4 claudie_thinking_hmm4 noloop
    mm "Maybe you two just aren't doing it right. I remember when I saw your dad on our wedding night-"
    scene e10s07-34 md-tries-to-defuse-mes-on-the-pill_c1 with dissolve
    play voice5 pete_thinking_eeh1 noloop
    md "Honey, they don't need to know-"
    play voice3 min_old_laugh noloop
    mes "Mom! I'm on the pill."
    play voice5 pete_disappointed_oof1 noloop
    md "Oh, too much information."
    scene e10s07-35 mes-wants-something-nice-mm-tells-she-is-happy_c1 with dissolve
    play voice3 min_thinking_hmm2 noloop
    mes "Can you just say something nice about our engagement?"
    play voice4 claudie_yes_yeah1 noloop
    mm "Of course. I am overjoyed at your impending nuptials and certain my daughter couldn't have picked a nicer boy."
    mm "Well, maybe a nicer boy, but not one who is better suited for herself."
    scene e10s07-36 mc-takes-that-as-compliment_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Ha! I'll take that as a compliment."
    play voice4 claudie_thinking_hmm1 noloop
    mm "And of course I want lots of grandbabies from both of you as soon as possible."
    play voice2 mc_yes_sure1 noloop
    mc "I'll do what I can in that regard, ma'am."
    play voice4 claudie_happy_mmm1 noloop
    mm "And if you ever need any advice-"
    scene e10s07-37 mb-tells-mm-she-will-give-heart-attack_c1 with dissolve
    play voice5 boy5_happy_laugh2 noloop
    mb "Mom, you're going to give dad a heart attack."
    play voice4 claudie_yes_aga noloop
    mm "Fine, then why don't you two just kiss already and I'll be silent."
    play voice3 min_yes_ugu noloop
    mes "That we can do."
    play voice2 d1s1_mmm noloop
    play voice3 min_old_mff noloop
    play sound dahlia_kiss_french1
    scene e10s07-38 mc-mes-kiss-in-front-of-house_c1 with dissolve
    pause

    $ renpy.music.set_volume(1.0, 5.5, "music2")
    scene ending_10_art_2 with Fade(1.25, 1.0, 1.75, color="#fff")
    pause
    call end_game_text (_("You have finished playing ending 10!")) from _call_end_game_text
    $ persistent.finished_e10 = True
    $ fl_achievement_unlock("e10_finish")
    stop music2 fadeout 3.0

    jump end

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
