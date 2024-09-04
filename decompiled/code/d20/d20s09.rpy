label d20s09:

    $ d20s09_lc_love = d10p2s08_love + d14s16_love_lc + d16s03_love_lc + d19s01lc_kiss

    scene black
    show screen scene_transistion(_("Back at the dorm"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene d20s09-01 mc-room-entry1_c1
    play sound ["<silence 0.4>", sfx_door_closed1]
    with Fade(0.5, 0.5, 0.9)
    pause
    queue music melancholy_god
    scene d20s09-01 mc-room-entry1_c2 with dissolve
    pause
    play voice2 d14s16_smell noloop
    scene d20s09-02 mc-room-entry2_c1 with dissolve
    mc "*Inhales and exhales*"
    scene d20s09-02 mc-room-entry2_c2_sepia3 with dissolve
    pause
    play sound sfx_reminiscence_gone
    scene d20s09-03 mc-room-timelapse-2_c2 with image_dissolve_1
    pause
    scene d20s09-04 mc-room-move1_c2 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mct "I miss when everything wasn't so damn complicated."
    if cage_ntr is True:
        mct "For being the dumbfuck Pete is, I always wondered why he was surprisingly well organized."
        mct "Wonder if that's something his \"mommy\" taught him."
        mct "Maybe I should burn it all. Send him a nice prison postcard with a picture—"
    play sound sfx_jeans_fly1
    scene d20s09-05 mc-room-open-bag_c2 with dissolve
    pause
    play sound sfx_bandage_on1
    scene d20s09-06 mc-room-pick1_c2 with dissolve
    play voice2 d1s5b_ehhh noloop
    mct "*Sigh* I need to get my stuff out of here."
    play sound sfx_paper_slide1
    scene d20s09-07 mc-room-pick2_c2 with dissolve
    pause
    play sound sfx_cup_slide1
    scene d20s09-08 mc-room-pick3_c2 with dissolve
    pause
    play sound sfx_door_creak2 volume 1.8
    scene d20s09-09 mc-room-pick4_c2 with dissolve
    pause
    play sound sfx_paper_bag_1
    scene d20s09-09-2 mc-room-photo1_c2 with dissolve
    pause
    stop sound fadeout 1.0
    scene d20s09-09-3 mc-room-photo2_c1 with dissolve
    pause
    scene d20s09-09-3 mc-room-photo2_c2 with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "I can't believe this is still here."
    scene d20s09-09-4 mc-room-photo3_c1 with dissolve
    mct "God. I can't believe I was so down bad that I {i}printed{/i} a physical picture of the girl I liked."
    mct "What the fuck was I even thinking?"
    play sound sfx_door_open2 volume 2.0
    scene d20s09-10 mc-hr-room-enter1_c1 with dissolve
    play voice2 mc_scared_huh2 noloop
    mc "Hana?"
    scene d20s09-10 mc-hr-room-enter1_c2 with dissolve
    play voice3 hana_emm noloop
    hr "Oh, hey. I didn't realize you were gonna be here."
    play sound sfx_door_closed9
    scene d20s09-11 mc-hr-room-enter2_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.5
    mc "What are you doing here?"
    scene d20s09-11 mc-hr-room-enter2_c2 with dissolve
    play voice3 aaleyah_thinking_hmm3 noloop
    hr "Just came back to get something of mine."
    scene d20s09-12 mc-hr-room-mic1_c2 with dissolve
    pause
    scene d20s09-12 mc-hr-room-mic1_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "What could you possibl—"
    play sound sfx_bandage_off1
    scene d20s09-13 mc-hr-room-mic2_c2 with dissolve
    play voice3 hana_argh noloop
    hr "This."
    scene d20s09-13 mc-hr-room-mic2_c1 with dissolve
    play voice2 mc_surprised_huh3 noloop
    mc "You bugged us!?"
    scene d20s09-14 mc-hr-room-talk2_c2 with dissolve
    play voice3 chloe_yes_aga2 noloop
    hr "Of course I did. I had to collect info through whatever means I had available."
    hr "But don't worry. This thing didn't work anyway. I barely got a signal, and even when I did, it wasn't anything important."
    scene d20s09-14 mc-hr-room-talk2_c1 with dissolve
    play voice2 mc_pain_mff2 noloop
    mc "You're fucking diabolical."
    scene d20s09-15 mc-hr-room-bed1_c2 with dissolve
    play voice3 chloe_arrogant_heh1 noloop
    hr "You gotta be in my profession."
    scene d20s09-15 mc-hr-room-bed1_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Anything to get the next scoop, huh?"
    scene d20s09-16 mc-hr-room-bed2_c2 with dissolve
    play voice3 chloe_yes_simple noloop
    hr "Pretty much. Though this one was a bit more personal."
    scene d20s09-16 mc-hr-room-bed2_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Right..."
    scene d20s09-17 mc-hr-room-bed3_c1 with dissolve
    pause
    scene d20s09-17 mc-hr-room-bed3_c2 with dissolve
    play voice3 chloe_disappointed_ehh7 noloop
    hr "So... How are you holding up?"
    scene d20s09-18 mc-hr-room-bed4_c1 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Not great."
    scene d20s09-18 mc-hr-room-bed4_c2 with dissolve
    play voice3 chloe_disappointed_oh noloop
    hr "Right. Sorry."
    scene d20s09-19 mc-hr-room-bed5_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.4
    mc "Nothing to be sorry about. I'll be \"not great\" for a while. That's just...how it is."
    scene d20s09-19 mc-hr-room-bed5_c2 with dissolve
    play voice3 hana_hmm noloop volume 1.3
    hr "I wanna ask something, and it's pretty rude. But I want to ask anyway."
    scene d20s09-20 mc-hr-room-talk1_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "When have you ever worried about being rude to me, Hana? Spit it out."
    scene d20s09-20 mc-hr-room-talk1_c2 with dissolve
    play voice3 hana_argh2 noloop
    hr "Do you still give a shit about her?"
    hr "She's some spoiled little brat that got too big for her breeches. What do you even see in her beyond a pair of tits?"
    scene d20s09-21 mc-hr-room-talk2_c1 with dissolve
    play voice2 mc_scared_huuuh3 noloop
    if d20s09_lc_love > 2:
        mc "I loved her..."
        scene d20s09-21 mc-hr-room-talk2_c2 with dissolve
        play voice3 hana_yeah2 noloop
        hr "Bullshit. You've known her for what, a couple of weeks? You really think that's \"love\"?"
    elif True:
        mc "I cared about her..."
        scene d20s09-21 mc-hr-room-talk2_c2 with dissolve
        play voice3 hana_yeah2 noloop
        hr "Yeah? And? She didn't give a damn about you."
    scene d20s09-20 mc-hr-room-talk1_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "What's your point, Hana? Did you just come here to tell me I'm a dumbass?"
    scene d20s09-20 mc-hr-room-talk1_c2 with dissolve
    play voice3 chloe_disappointed_ehh2 noloop
    hr "I— *Sigh* Look, man. I'm sorry she turned out to be a bitch."
    if fl_w2_sex_count > 5:
        hr "But you've fucked half the damn campus at this point. Not to mention that you have some great ladies supporting you."
    elif True:
        hr "But you have some great ladies supporting you."
    scene d20s09-21 mc-hr-room-talk2_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "So why should I feel bad that she turned out to be what she is? Is that what you're saying?"
    scene d20s09-21 mc-hr-room-talk2_c2 with dissolve
    play voice3 chloe_disappointed_mff noloop
    hr "I'm saying that I know what happened was shit. But there's better shit out there. You can't let yourself be weighed down by what happened."
    scene d20s09-23 mc-hr-room-talk4_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "You suck ass at emotional support."
    scene d20s09-23 mc-hr-room-talk4_c2 with dissolve
    play voice3 chloe_happy_hmm noloop
    hr "*Chuckles* I know."
    scene d20s09-22 mc-hr-room-talk3_c1 with dissolve
    play voice2 d2s9_mchey noloop
    mc "Hey. You wanna stay over?"
    scene d20s09-22 mc-hr-room-talk3_c2 with dissolve
    play voice3 chloe_surprised_huh3 noloop
    hr "Hm? Here?"
    scene d20s09-24 mc-hr-room-talk5_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah. One last night. For old-time's sake. Keep me company. I could use it."
    scene d20s09-24 mc-hr-room-talk5_c2 with dissolve
    play voice3 chloe_disappointed_ehh4 noloop
    hr "This place isn't exactly what I'd call comfortable, but... *Sigh* Alright. For old-time's sake."
    hr "I didn't have much going on tonight anyway."
    play sound sfx_cloth_rustling4
    scene d20s09-25 mc-hr-bed-talk1_c2 with Fade(0.4, 0.4, 0.4)
    play voice3 hana_hmm2 noloop
    hr "Can I ask you a question?"
    scene d20s09-25 mc-hr-bed-talk1_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "A question? Sure, as long as I don't get lamblasted again."
    scene d20s09-26 mc-hr-bed-talk2_c2 with dissolve
    hr "I'm pretty sure it's \"lambasted.\""
    scene d20s09-26 mc-hr-bed-talk2_c1 with dissolve
    mc "My version is more fun."
    scene d20s09-27 mc-hr-bed-talk3_c2 with dissolve
    play voice3 chloe_arrogant_heh2 noloop
    hr "*Chuckles* I guess. Anyway, I wanted to ask if you expected this to go somewhere?"
    scene d20s09-27 mc-hr-bed-talk3_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Define \"this.\""
    scene d20s09-28 mc-hr-bed-talk4_c2 with dissolve
    play voice3 hana_argh noloop
    hr "Us. In this room."
    scene d20s09-28 mc-hr-bed-talk4_c1 with dissolve
    play voice2 mc_arrogant_hm2 noloop
    mc "Are you asking if I expected us to have sex here or are you asking if I wanted more from our relationship?"
    scene d20s09-29 mc-hr-bed-talk5_c2 with dissolve
    hr "Both."
    scene d20s09-29 mc-hr-bed-talk5_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.4
    mc "Well, I certainly wouldn't say {i}no{/i} to you wanting to get frisky. But I didn't ask you to stay only because of that."
    mc "The thought only came when you started stripping."
    scene d20s09-25 mc-hr-bed-talk1_c2 with dissolve
    play voice3 chloe_arrogant_heh3 noloop
    hr "*Chuckles* Fair enough. What can I say? I like to be comfortable."
    hr "And what about the other thing?"
    scene d20s09-25 mc-hr-bed-talk1_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "I don't know. You're certainly interesting, I'll give you that."
    mc "But I have a sneaking suspicion that you wouldn't be into it even If I {i}did{/i} want it."
    scene d20s09-26 mc-hr-bed-talk2_c2 with dissolve
    play voice3 chloe_old_cangry noloop
    hr "Hm. You're surprisingly astute sometimes."
    scene d20s09-26 mc-hr-bed-talk2_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "I'm not sure if I should be offended or not."
    scene d20s09-27 mc-hr-bed-talk3_c2 with dissolve
    play voice3 chloe_disappointed_ehh5 noloop
    hr "Anyway. I'm glad to hear that you understand that. It's not that I don't like you. You're a fine enough guy."
    hr "It's just that something like that isn't what I want right now. I have other things to focus on."
    scene d20s09-27 mc-hr-bed-talk3_c1 with dissolve
    play voice2 mc_scared_oh2 noloop
    mc "Other things? Like Iona and—"
    scene d20s09-28 mc-hr-bed-talk4_c2 with dissolve
    play voice3 chloe_angry_hm noloop
    hr "Don't finish that sentence."
    hr "Like I said, you're a fine enough guy. But this isn't something that I want to talk about with you."
    hr "Still, if you even have half a brain, I'm sure you've figured out some of it by this point as well."
    hr "It's just...a lot. To say the least. And it's something that Iona and I need to figure out."
    scene d20s09-28 mc-hr-bed-talk4_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "I understand."
    mc "I'm sure you two will figure out how to move forward."
    scene d20s09-29 mc-hr-bed-talk5_c2 with dissolve
    play voice3 aaleyah_thinking_hmm3 noloop
    hr "Thank you. I appreciate that."
    hr "I'm feeling sleepy now, I think I'm gonna get some shuteye."
    scene d20s09-30 mc-hr-bed-talk6_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Alright."
    scene d20s09-31 mc-hr-bed-talk7_c2 with dissolve
    play voice3 aaleyah_disappointed_mff noloop
    hr "And, even if I might not be able to give you a relationship, maybe I'll help you out with that thing {i}that you totally didn't think about{/i} in the morning."
    scene d20s09-31 mc-hr-bed-talk7_c1 with dissolve
    play voice2 d4s4_mclaugh noloop
    mc "*Chuckles* That's a promise then."
    scene d20s09-32 mc-hr-bed-talk8_c2 with dissolve
    play voice3 aaleyah_happy_mmm1 noloop
    hr "Goodnight, [mcname]."
    play voice2 d7s6_moan1 noloop
    scene d20s09-32 mc-hr-bed-talk8_c1 with dissolve
    mc "Goodnight, Hana."

    stop music fadeout 3.0
    jump d21s01

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
