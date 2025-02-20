label e02s04:

    scene black
    show screen scene_transistion(_("The next day"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.4, 3.0, "music" )
    $ renpy.music.set_volume(0.4, 0.0, "sound2" )
    play sound2 d12s2_cafe_crowd fadein 3.0
    scene e02s04-01 mc-mh-talk1_c1
    with Fade(0.5, 0.5, 0.9)
    queue music caffee_theme_1
    pause
    play voice2 d1s5_mchappy noloop
    mc "How much?"
    mc "Come on, how much?"
    scene e02s04-01 mc-mh-talk1_c2 with dissolve
    play voice3 dahlia_arrogant_heh noloop
    mh "I am not going to bother answering that. It is really a silly question."
    scene e02s04-02 mc-mh-talk2_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "But I'm curious. Would you represent me in court for free, or would I have to pay you?"
    scene e02s04-02 mc-mh-talk2_c2 with dissolve
    play voice3 lissa_haha noloop
    mh "Of course I would do it pro-bono, [mcname]."
    scene e02s04-03 mc-mh-talk3_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "That means for free right?"
    scene e02s04-03 mc-mh-talk3_c2 with dissolve
    play voice3 lissa_yes noloop
    mh "Yes. But we do not have to worry about me representing you because you will not be committing any crimes, correct?"
    scene e02s04-04 mc-mh-talk4_c1 with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Of course not, but I'm glad to know you'd be in my corner."
    mc "Maybe I should try that out - being in your corner, I mean. During a trial."
    mc "Are you hiring?"
    scene e02s04-04 mc-mh-talk4_c2 with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    mh "I always keep my eyes open for talent."
    scene e02s04-05 mc-mh-talk5_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Well there is no one more talented than me. And we work so well together in the bedroom. Just imagine what we could do outside of it."
    scene e02s04-05 mc-mh-talk5_c2 with dissolve
    play voice3 lissa_laugh2 noloop
    mh "I do not need to imagine. We are out of the bedroom as often as we are in it."
    play sound sfx_cup_slide1
    scene e02s04-06 mc-mh-talk6_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.4
    mc "Ha! True. {w}Still, what if I was interested in pitching in?"
    scene e02s04-06 mc-mh-talk6_c2 with dissolve
    play voice3 dahlia_arrogant_pff noloop
    mh "I think you are pulling my leg."
    scene e02s04-07 mc-mh-talk7_c1 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Come on, I've always liked the law."
    scene e02s04-08 mc-mh-talk8_c2 with dissolve
    play voice3 lissa_thinking noloop volume 1.4
    mh "[mcname] I love you, but liking the law and applying yourself to it are two {i}very{/i} different things."
    mh "And you would need a lot of experience before working in any office."
    scene e02s04-08 mc-mh-talk8_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Even if I have an {i}in{/i} with a kickass lawyer?"
    play sound sfx_drink_slurp2
    scene e02s04-10 mc-mh-coffee1_c2 with dissolve
    play voice3 lissa_ha noloop
    mh "Flattery works in bed, but it will not get you into my office."
    play sound sfx_drink_loop1
    scene e02s04-09 mc-mh-talk9_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "Just think about it. I could be your sexy intern, bending over a file cabinet."
    mc "Giving you a massage whenever your shoulders need a little rubbing..."
    scene e02s04-11 mc-mh-talk10_c2 with dissolve
    play voice3 lissa_laugh noloop
    mh "You're already defeating your case, Mister. I would never get any work done."
    scene e02s04-11 mc-mh-talk10_c1 with dissolve
    play voice2 d4s4_mclaugh noloop volume 1.6
    mc "Hahaha. Can't blame a guy for trying."
    play sound cameraclick
    with Fade(.25, 0, .75, color="#fff")
    pause

    jump e02s04_photo

label e02s04_photo:

    scene e02s04-16 mc-mh-phone1_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "What was that?"
    scene e02s04-16 mc-mh-phone1_c2 with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    mh "Over there. That couple just took a picture of us."
    scene e02s04-17 mc-mh-phone2_c2 with dissolve
    play voice3 dahlia_arrogant_huh noloop
    mh "Excuse me, did you want something? A picture perhaps?"
    play sound sfx_paper_rustl1
    scene e02s04-17 mc-mh-phone2_c3 with dissolve
    play voice4 boy4_disappointed_oh noloop
    ap "Oh I'm so sorry. My wife asked to take a photo of her but my aim was off."
    play voice5 girl23_yes_yeeeah2 noloop
    atp "Hmmph. Yes, that's what happened."
    ap "Angela, stop."
    play voice4 girl12_thinking_huh2 noloop
    scene e02s04-17 mc-mh-phone2_c4 with dissolve
    play voice3 cynthia_arrogant_hm noloop
    pause
    play sound sfx_bed_slide3 volume 0.5
    scene e02s04-18 mc-mh-phone3_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "What's going on?"
    scene e02s04-18 mc-mh-phone3_c3 with dissolve
    play voice5 girl23_thinking_hmm3 noloop
    atp "Relax. It was nothing sinister. We, uh, couldn't help but overhear your conversation."
    play voice4 boy4_thinking_emm4 noloop
    ap "Can you..."
    play voice5 girl23_disappointed_ohh noloop
    atp "Oh, grow up, Alexander."
    scene e02s04-19 mc-mh-phone4_c1 with dissolve
    play voice3 dahlia_thinking_oh noloop
    mh "Wait, I recognize you. {w}Alexander Portillo, Channel Six, right?"
    scene e02s04-19 mc-mh-phone4_c3 with dissolve
    play voice4 boy4_disappointed_ehh2 noloop
    ap "Oh, uh-huh. Yes. I didn't imagine you'd recognize me. This is my wife, Angela."
    play voice5 girl23_happy_hmm noloop
    atp "And you are Melissa Harris."
    scene e02s04-20 mc-mh-phone5_c1 with dissolve
    play voice3 dahlia_yes_angry noloop
    mh "Pleased to meet you. This is my boyfriend, [mcname]. Now can you delete that photo?"
    scene e02s04-20 mc-mh-phone5_c3 with dissolve
    play voice4 boy4_thinking_oh1 noloop
    ap "So strict. It's not illegal to snap a few shots on vacation."
    scene e02s04-21 mc-mh-pic1_c1 with dissolve
    play voice3 dahlia_arrogant_hm noloop
    mh "Then perhaps you could explain why you took a picture of us."
    play sound sfx_phone_tapping1
    scene e02s04-25 mc-mh-pic5_c2 with dissolve
    play voice4 boy4_angry_err1 noloop
    pause
    stop sound fadeout 1.0
    scene e02s04-26 mc-mh-delete_c1 with dissolve
    play voice4 boy4_yes_yeah noloop
    ap "There, it's gone."
    scene e02s04-26 mc-mh-delete_c3 with dissolve
    play voice5 girl23_thinking_hmm1 noloop
    atp "And we're terribly sorry for disturbing you."
    scene e02s04-27 mc-mh-ok_c1 with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    mh "So, what was this? You were going to post a scoop of me while I'm on vacation?"
    scene e02s04-27 mc-mh-ok_c3 with dissolve
    play voice5 girl23_happy_laugh1 noloop
    atp "Hahaha. I'd have to be pretty desperate to try selling that. No offense."
    atp "You're a banging lawyer, but do you think anyone would care to find out that you summer up in the mountains?"
    scene e02s04-28 mc-mh-ok2_c2 with dissolve
    play voice4 boy4_angry_mmm1 noloop
    ap "Please excuse us, we were just excited and-"
    scene e02s04-27 mc-mh-ok_c3 with dissolve
    play voice5 girl23_disgust_voeah noloop
    atp "Not excited, just bored. We've skied and skied and then we noticed you and..."
    atp "Well you and I are like two peas in a pod, Ms. Harris."
    scene e02s04-29 mc-mh-ok3_c1 with dissolve
    play voice3 lissa_haha2 noloop
    mh "Two peas in a pod? {w}What do you mean by that?"
    scene e02s04-27 mc-mh-ok_c2 with dissolve
    play voice4 boy4_disappointed_ehh1 noloop
    ap "Listen, we're really sorry for bothering you. We should go."
    scene e02s04-27 mc-mh-ok_c3 with dissolve
    play voice5 girl23_hey_greeting noloop
    atp "You're just as curious as I am, Alexander."
    atp "You're transgender right?"
    play sound sfx_hands_clap3
    scene e02s04-34 mc-mh-facepalm_c2 with dissolve
    play voice4 boy4_angry_dough2 noloop
    ap "Angela!"
    play voice5 girl23_surprised_huh3 noloop
    atp "What?"
    scene e02s04-34 mc-mh-facepalm_c3 with dissolve
    play voice4 boy4_angry_breath1 noloop
    ap "That is inappropriate!"
    play voice5 girl23_disappointed_mpff noloop
    atp "Oh, come on."
    scene e02s04-35 mc-mh-ask_c1 with dissolve
    play voice3 lissa_aga noloop
    mh "I am. Is that why you were taking photos of me?"
    scene e02s04-35 mc-mh-ask_c2 with dissolve
    play voice5 girl23_no_unsure noloop volume 1.3
    atp "No. Well, it's... I mean it's really kind of a funny story."
    play voice4 boy4_arrogant_mmm1 noloop
    ap "I think Angela just panicked."
    scene e02s04-35 mc-mh-ask_c3 with dissolve
    play voice5 girl23_no_uhuh1 noloop
    atp "I did not panic. I just... well, I thought it was you but I didn't know it was you."
    atp "But {i}then{/i} I realized it was you and I thought..."
    atp "{i}But{/i} you're on vacation and I didn't want to bother you but I've wanted to meet you so I told Alexander to get your attention."
    scene e02s04-36 mc-mh-ask2_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Sounds a little strange, Angela."
    scene e02s04-35 mc-mh-ask_c3 with dissolve
    play voice5 girl23_disappointed_eh noloop
    atp "I will admit to being slightly flustered. It's uh... it's not easy for me... just."
    atp "I think it's better if I show you."
    play sound sfx_cloth_rustling4
    scene e02s04-27-2 mc-mh-show_c1 with dissolve
    pause
    scene e02s04-27-2 mc-mh-show_c2 with dissolve
    pause
    scene e02s04-27-2 mc-mh-show_c3 with dissolve
    play voice3 lissa_mmm1 noloop
    mh "Peas in a pod, hmmm?"
    scene e02s04-35 mc-mh-ask_c2 with dissolve
    play voice5 girl23_happy_laugh2 noloop
    atp "Haha. Yeah. So, do you mind if we chat?"
    scene e02s04-36 mc-mh-ask2_c1 with dissolve
    play voice3 lissa_yes noloop
    mh "Yes. But why don't we start fresh? I am Lyssa and this is my boyfriend, [mcname]."
    scene e02s04-36 mc-mh-ask2_c2 with dissolve
    play voice5 girl23_hey_hi noloop
    atp "Lyssa, [mcname]. Nice."
    atp "I'm Angela, and you know my husband, Alexander."
    play voice4 boy4_happy_relief1 noloop
    ap "Pleasure, and thanks for being so understanding."

    stop sound2 fadeout 3.0
    jump e02s04_fireplace

label e02s04_fireplace:

    scene e02s04-40 mc-mh-ap-atp-sofa1_c2
    with Fade(0.5, 0.5, 0.5)
    play sound4 sfx_fire_fireplace1 fadein 3.0 volume 0.7
    $ renpy.music.set_volume(1.0, 0.0, "sound4" )
    pause
    scene e02s04-40 mc-mh-ap-atp-sofa1_c3 with dissolve
    play voice5 girl23_surprised_huh1 noloop
    atp "So your assistant knows and you've told many of the people at the courthouse... and they don't care?"
    scene e02s04-41 mc-mh-ap-atp-sofa2_c1 with dissolve
    play voice3 lissa_ugu2 noloop
    mh "Correct."
    scene e02s04-41 mc-mh-ap-atp-sofa2_c2 with dissolve
    play voice5 girl23_surprised_why2 noloop volume 1.3
    atp "How do they not care? I've had people just give me blank stares when I told them."
    atp "Some days I wish I kept it a secret. Some people started acting different to me at work."
    atp "I'm one of the most accomplished executives at Channel Six. Not just in the company, but in the industry..."
    atp "... but I'm still just known as the \"Stallion\"."
    scene e02s04-42 mc-mh-ap-atp-sofa3_c1 with dissolve
    play voice3 lissa_moan1 noloop
    mh "I admire your bravery for putting yourself out there. I... My only advice would be to do your best to tune out the idiots."
    mh "I know that is not easy. As more people accept you, more people learn about you, and more idiots come out of the woodwork."
    scene e02s04-42 mc-mh-ap-atp-sofa3_c2 with dissolve
    play voice5 girl23_happy_relief noloop
    atp "Getting to open up about it feels good. And I appreciate you being, uh... {w}being patient with me."
    play voice3 dahlia_happy_hmm1 noloop
    mh "Water under the bridge, my dear."
    scene e02s04-40 mc-mh-ap-atp-sofa1_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "So how did you two get together?"
    scene e02s04-41 mc-mh-ap-atp-sofa2_c3 with dissolve
    play voice4 boy4_happy_mmm3 noloop
    ap "We met in college, both working on our journalism degrees. And we've been together ever since."
    scene e02s04-43 mc-mh-ap-atp-sofa4_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Working together in the same place. That's got to be nice."
    scene e02s04-43 mc-mh-ap-atp-sofa4_c2 with dissolve
    play voice4 boy4_yes_confident noloop
    ap "Uh-yeah. It's very nice. Lot of fun."
    scene e02s04-44 mc-mh-ap-atp-sofa5_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "So she makes the show run but you lead the show right?"
    scene e02s04-43 mc-mh-ap-atp-sofa4_c3 with dissolve
    play voice4 boy5_arrogant_hm noloop
    ap "Haha. You're very kind. With all the grit and effort that goes into it, it {i}looks{/i} like I run the show, but I just put my spin on whatever is on the teleprompter."
    ap "Well, my spin and my voice."
    scene e02s04-45 mc-mh-ap-atp-sofa6_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "You kind of sound like everyone else."
    scene e02s04-45 mc-mh-ap-atp-sofa6_c2 with dissolve
    play voice4 pete_arrogant_heh2 noloop
    ap "That's because I didn't turn on my \"newsreader voice\"."
    scene e02s04-46 mc-mh-ap-atp-sofa7_c1 with dissolve
    play voice2 mc_surprised_wow1 noloop
    mc "Woah. You like... it's almost like you turned into a different person. Not bad."
    scene e02s04-46 mc-mh-ap-atp-sofa7_c2 with dissolve
    play voice4 boy5_yes_yep noloop
    ap "Thanks. Yeah I call it my \"golden voice\". Usually it only comes out in the newsroom."
    scene e02s04-45 mc-mh-ap-atp-sofa6_c3 with dissolve
    play voice5 girl23_arrogant_haha noloop
    atp "His 'golden voice' comes out a lot when I shove a dildo up his ass."
    scene e02s04-42 mc-mh-ap-atp-sofa3_c3 with dissolve
    play voice4 boy4_surprised_what2 noloop
    ap "Angela. Really?!"
    scene e02s04-41 mc-mh-ap-atp-new1_c3 with dissolve
    play voice5 girl23_happy_ha noloop
    atp "What? I was running out of things to talk about."
    scene e02s04-41 mc-mh-ap-atp-new1_c2 with dissolve
    play voice4 boy4_yes_angry noloop
    ap "Yes, but you can stand to be a little more discreet about things."
    scene e02s04-41-3 mc-mh-ap-atp-new2_c3 with dissolve
    atp "Why are you acting embarrassed?"
    scene e02s04-41-3 mc-mh-ap-atp-new2_c2 with dissolve
    ap "Well it is embarrassing to me."
    scene e02s04-47 mc-mh-ap-atp-sofa8_c2 with dissolve
    play voice4 boy4_disappointed_geh2 noloop
    ap "I mean you two seem nice but I'm sure you don't want to hear details like that."
    scene e02s04-48 mc-mh-ap-atp-talk1_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "It's all good. We're just having a friendly conversation."
    play voice3 dahlia_yes_ugu noloop
    mh "Yes, very friendly."
    scene e02s04-48-2 mc-mh-ap-atp-talk2_c2 with dissolve
    play voice4 boy4_thinking_hmm1 noloop
    ap "So you won't tell anyone?"
    scene e02s04-48-3 mc-mh-ap-atp-talk3_c1 with dissolve
    play voice3 lissa_lno noloop
    mh "Of course not."
    play sound sfx_drink_loop1 loop
    scene e02s04-48-3 mc-mh-ap-atp-talk3_c2 with dissolve
    play voice5 girl23_thinking_hmm4 noloop
    atp "So tell me, [mcname]... Do you enjoy the other side? Having Lyssa take the wheel so to speak?"
    if e02s01_give_pleasure is True or e02s01_both is True:
        scene e02s04-48-4 mc-mh-ap-atp-talk4_c1 with dissolve
        play voice2 mc_yes_yeah1 noloop
        mc "Definitely. We enjoy switching things up now and then."
        scene e02s04-48-3 mc-mh-ap-atp-talk3_c3 with dissolve
        play voice5 girl23_arrogant_haha noloop
        atp "Haha. Alexander is always in the mood for me to toss his salad or stretch his starfish."
    else:
        scene e02s04-48-4 mc-mh-ap-atp-talk4_c1 with dissolve
        play voice2 mc_no_nah2 noloop
        mc "We haven't tried that yet."
        scene e02s04-48-3 mc-mh-ap-atp-talk3_c3 with dissolve
        play voice5 girl23_arrogant_haha noloop
        atp "Well don't wait too long. I'm sure Lyssa wouldn't mind trying out your backdoor, [mcname]"
    stop sound fadeout 1.0
    scene e02s04-48-6 mc-mh-ap-atp-talk6_c1 with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    mh "Different people like different things, Angela."
    scene e02s04-48-5 mc-mh-ap-atp-talk5_c2 with dissolve
    play voice5 girl23_yes_yeah noloop
    atp "Sure, but some people need others to lead the way - or they'll never be adventurous."
    scene e02s04-41 mc-mh-ap-atp-new1_c2 with dissolve
    play voice4 boy5_arrogant_hah noloop
    ap "That doesn't mean I want to be led by your cock every day, Angela."
    mct "Wow. I got the feeling these two were a bit high-strung, but this is something else."
    scene e02s04-41 mc-mh-ap-atp-new1_c3 with dissolve
    play voice5 girl23_surprised_oh1 noloop
    atp "This is the first I've heard that, Alexander."
    scene e02s04-41-3 mc-mh-ap-atp-new2_c2 with dissolve
    play voice4 boy5_disappointed_ehh1 noloop
    ap "*Sigh* That is a little surprising to hear. There have been many times where I've asked you to be more gentle and loving."
    scene e02s04-41-3 mc-mh-ap-atp-new2_c3 with dissolve
    play voice5 girl23_arrogant_ha noloop
    atp "So now I don't love you..."
    scene e02s04-41 mc-mh-ap-atp-new1_c2 with dissolve
    play voice4 boy4_no_angry noloop
    ap "That's not what I said. This- *sighs* This is why I wanted us to come."
    scene e02s04-41 mc-mh-ap-atp-new1_c3 with dissolve
    play voice5 girl23_yes_serious noloop
    atp "Yes, but there is no point now because the dumb therapist didn't show up."
    scene e02s04-41-3 mc-mh-ap-atp-new2_c2 with dissolve
    play voice4 boy4_angry_argh3 noloop
    ap "You must be so disappointed. From the moment I mentioned it, you didn't think it would help us."
    scene e02s04-41-3 mc-mh-ap-atp-new2_c3 with dissolve
    play voice5 girl23_arrogant_yeah noloop
    atp "So far I'm not wrong."
    scene e02s04-48-7 mc-mh-ap-atp-talk7_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "{size=-10}*whispers* So I was thinking, maybe we go play another round of chess.{/size}"
    scene e02s04-48-7 mc-mh-ap-atp-talk7_c3 with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    mh "{size=-10}*whispers* I'm not really in the mood to play games.{/size}"
    play voice2 d2s9_confused noloop
    mc "{size=-10}*whispers* Well how about at least we go to our cabin. You know...{/size}"
    mc "{size=-10}..away from them.{/size}"
    mh "{size=-10}*whispers* I want to help.{/size}"
    scene e02s04-48-8 mc-mh-ap-atp-talk8_c1 with dissolve
    mc "{size=-10}...{/size}"
    scene e02s04-48-8 mc-mh-ap-atp-talk8_c3 with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    mh "{size=-10}*whispers* [mcname].{/size}"
    scene e02s04-48-7 mc-mh-ap-atp-talk7_c1 with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "{size=-10}*whispers* Don't they seem beyond help?{/size}"
    scene e02s04-48-8 mc-mh-ap-atp-talk8_c3 with dissolve
    mh "{size=-10}*whispers* No one is beyond help.{/size}"
    scene e02s04-48-8 mc-mh-ap-atp-talk8_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "{size=-10}*whispers* Okay... so how exactly would we help?{/size}"
    scene e02s04-42 mc-mh-ap-atp-sofa3_c1 with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    mh "You mentioned a therapist. Did you two come here for some couple's therapy?"
    scene e02s04-41 mc-mh-ap-atp-sofa2_c3 with dissolve
    play voice5 girl23_yes_simple noloop
    atp "Yes, that was the plan."
    play voice4 boy4_angry_breath2 noloop
    ap "But the poor doctor got hurt or something on the trip here. So, he cancelled after we were already here."
    scene e02s04-40 mc-mh-ap-atp-sofa1_c1 with dissolve
    play voice2 d2s9_mchey noloop volume 1.4
    mc "At least this place is great for snowboarding. You get a nice vacation out of it."
    scene e02s04-40 mc-mh-ap-atp-sofa1_c2 with dissolve
    play voice4 boy4_arrogant_ahh1 noloop
    ap "Oh, absolutely."
    scene e02s04-44 mc-mh-ap-atp-sofa5_c1 with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    mh "Angela, Alexander, do you mind if I offer some suggestions?"
    scene e02s04-45 mc-mh-ap-atp-sofa6_c2 with dissolve
    play voice4 boy5_yes_aga noloop
    ap "I mean. Sure, but you're not a therapist are you?"
    scene e02s04-47 mc-mh-ap-atp-sofa8_c1 with dissolve
    play voice3 lissa_haha2 noloop
    mh "Oh no, but I've definitely seen my share of personalities in the courtroom. I might be able to give you an insight."
    scene e02s04-46 mc-mh-ap-atp-sofa7_c2 with dissolve
    play voice5 girl23_thinking_hmm3 noloop
    atp "I'm open to trying something. Just last month I tried to shake things up with that couple's dating site."
    play voice4 boy5_thinking_hmm3 noloop
    ap "This will be different. We'd both agree to this instead of you signing us for something without asking me."
    scene e02s04-48 mc-mh-ap-atp-talk1_c1 with dissolve
    play voice3 lissa_oh2 noloop
    mh "That is it, right there."
    play sound sfx_drink_loop1
    scene e02s04-48 mc-mh-ap-atp-talk1_c2 with dissolve
    play voice5 girl23_surprised_ah2 noloop
    atp "What's it?"
    scene e02s04-48-3 mc-mh-ap-atp-talk3_c1 with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    mh "Your husband is trying to tell you something. I am going to be brutally honest with you both. Alexander..."
    mct "It's always a treat getting to see Lyssa in action."
    stop sound fadeout 1.0
    scene e02s04-47 mc-mh-ap-atp-sofa8_c2 with dissolve
    play voice4 boy5_surprised_eeh2 noloop
    ap "Um. Yes?"
    scene e02s04-48 mc-mh-ap-atp-talk1_c1 with dissolve
    play voice3 nora_hey noloop
    mh "You seem like a very nice man, Alexander."
    mh "You're unassuming, calm, rational, but you are not outspoken - which seems odd given what you do for a living."
    scene e02s04-45 mc-mh-ap-atp-sofa6_c2 with dissolve
    play voice4 boy5_surprised_oh1 noloop
    ap "I suppose that's true."
    play sound sfx_drink_loop1
    scene e02s04-48-4 mc-mh-ap-atp-talk4_c1 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "But that's just work. You're playing a specific role, but that doesn't mean you want to do that all the time."
    scene e02s04-47 mc-mh-ap-atp-sofa8_c2 with dissolve
    play voice4 boy4_yes_confident noloop
    ap "Yes."
    play sound sfx_cup_place1
    scene e02s04-47 mc-mh-ap-atp-sofa8_c1 with dissolve
    play voice3 dahlia_arrogant_heh noloop
    mh "And you, Angela, you are the complete opposite. You are full of energy, you say whatever is on your mind."
    mh "Your job fits your personality perfectly. You're the one in charge, all the time."
    scene e02s04-45 mc-mh-ap-atp-sofa6_c3 with dissolve
    play voice5 girl23_yes_happy noloop
    atp "Damn right."
    scene e02s04-48-3 mc-mh-ap-atp-talk3_c1 with dissolve
    play voice3 dahlia_arrogant_hm noloop
    mh "And I think that is part of the problem. You two are just so opposite that without good and open communication, I think that things will get worse."
    mh "In the courtroom, if the lawyer and client are not honest with one another, there is no way they'll win the case."
    play voice2 mc_angry_huh2 noloop
    mct "Huh. On TV, clients are always holding back things from their lawyer. I guess it's different in the real world."
    scene e02s04-48-10 mc-mh-ap-atp-talk10_c2 with dissolve
    play voice5 girl23_surprised_huh2 noloop
    atp "So what, we should talk more?"
    scene e02s04-48-10 mc-mh-ap-atp-talk10_c3 with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    mh "Communicate more, yes. That's part of it."
    mh "I think there is something deeper just beneath the surface."
    play sound sfx_cloth_rustling2
    scene e02s04-49-2 mc-mh-ap-atp-leave2_c3 with dissolve
    play voice5 girl23_thinking_hmm2 noloop volume 1.4
    atp "Well we appreciate the advice. I think we'll give you two some space."
    atp "We don't want to take up any more of your vacation."
    scene e02s04-49-3 mc-mh-ap-atp-leave3_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Not a problem."
    play voice4 boy4_happy_mmm3 noloop
    ap "Thanks so much for your patience. And um... you'll keep this between us."
    play voice2 mc_yes_yes3 noloop
    mc "Of course. No problem."
    scene e02s04-49-3 mc-mh-ap-atp-leave3_c3 with dissolve
    play voice4 boy4_happy_relief1 noloop
    ap "Thanks."
    scene e02s04-49-3 mc-mh-ap-atp-leave3_c1 with dissolve
    play voice3 lissa_ugu noloop
    mh "I just hope it helps."
    play voice5 girl23_yes_yeeeah1 noloop
    atp "I guess we'll see."
    scene e02s04-49-4 mc-mh-ap-atp-leave4_c1 with dissolve
    play voice3 nora_hmm noloop volume 1.5
    mh "To our room?"
    play voice2 mc_thinking_mmm2 noloop
    mc "You read my mind."

    stop music fadeout 3.5
    stop sound4 fadeout 3.0
    jump e02s04_next_day

label e02s04_next_day:

    scene black
    show screen scene_transistion(_("The next morning"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play voice2 d7s6_snoring fadein 2.0
    play voice3 girl8_disappointed_snoring fadein 2.0
    scene e02s04-50 mc-mh-sleep1_c1
    with Fade(0.5, 0.5, 0.5)
    pause
    stop voice2 fadeout 1.0
    stop voice3 fadeout 1.0
    scene e02s04-50 mc-mh-sleep1_c2 with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    mh "Mmm. What time is it?"
    play music "<silence 0.35>" noloop
    queue music take_the_ride_calm
    play sound sfx_cloth_rustling1
    scene e02s04-52 mc-mh-sleep3_c1 with dissolve
    play voice2 d1s1_mmm noloop
    mc "Early. But I already feel fully rested. {w}These beds are amazing."
    play voice3 dahlia_happy_hmm2 noloop
    mh "Mmmhmm."
    scene e02s04-52 mc-mh-sleep3_c2 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "I know you don't want to talk about work. But I've got some pretty intense messages from Oliver on here."
    play voice3 lissa_oh noloop
    mh "Did he say which case is giving him trouble?"
    scene e02s04-53 mc-mh-sleep4_c1 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "He says it's privileged information. Not for my peasant eyes."
    scene e02s04-53 mc-mh-sleep4_c2 with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    mh "I haven't taken a real vacation in forever. {w}Can it {i}really{/i} be that important?"
    scene e02s04-54 mc-mh-sleep5_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "I don't think he'd go to this much effort if it wasn't important, Lyssa."
    scene e02s04-54 mc-mh-sleep5_c2 with dissolve
    play voice3 lissa_moan1 noloop
    mh "Okay. Alright, I'll call him tomorrow. Let me borrow your phone."
    play sound sfx_cloth_rustling1
    scene e02s04-55-4 mc-mh-phone4_c1 with dissolve
    mh "That does appear to be an above average amount of text messages."
    play voice2 mc_yes_aga2 noloop
    mc "Yup."
    scene e02s04-55-4 mc-mh-phone4_c2 with dissolve
    play voice3 lissa_haha noloop
    mh "I'll text him now."
    mh "Hey Oliver. This is Lyssa. Call you tomorrow."
    scene e02s04-55-5 mc-mh-phone5_c1 with dissolve
    mh "Done. I hope that didn't spoil things."
    mh "The more I step back into the work lake, the more my brain will leave vacation mountain."
    scene e02s04-55-5 mc-mh-phone5_c2 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "You're fine, Lyssa. A little work distraction is nothing compared to the distraction from yesterday."
    scene e02s04-56 mc-mh-talk1_c2 with dissolve
    play voice3 lissa_oh2 noloop
    mh "It was distracting. But... I kind of enjoyed it. Offering them some pointers."
    scene e02s04-56 mc-mh-talk1_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "You certainly got into your element."
    scene e02s04-57 mc-mh-talk2_c2 with dissolve
    play voice3 nora_hey noloop
    mh "We both did. Do you think it helped them? Angela and Alexander."
    scene e02s04-57 mc-mh-talk2_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.5
    mc "I don't think it could hurt. Man, can you imagine coming all this way out there for some special couples therapy and the therapist doesn't make it?"
    mc "Talk about bad luck."
    scene e02s04-57 mc-mh-talk2_c2 with dissolve
    play voice3 nora_mmm noloop volume 1.5
    mh "Mmm. Maybe it was meant to be..."
    scene e02s04-57 mc-mh-talk2_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "I know that look. What are you up to, Lyssa?"
    scene e02s04-57 mc-mh-talk2_c2 with dissolve
    play voice3 lissa_laugh2 noloop
    mh "I'll tell you on the way, but first we need to shower."
    scene e02s04-57 mc-mh-talk2_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Okay, I like where this is going so far."
    play sound dahlia_kiss_french1
    play voice2 mc_thinking_mmm4 noloop
    scene e02s04-59 mc-mh-kiss_c1 with dissolve
    pause
    play voice3 lissa_moan1 noloop
    scene e02s04-59 mc-mh-kiss_c2 with dissolve
    pause
    play sound maria_kiss2
    scene e02s04-59 mc-mh-kiss_c3 with dissolve
    pause
    play voice2 mc_disappointed_ah2 noloop
    play sound sfx_cloth_rustling4
    scene e02s04-59-2 mc-mh-getup_c1 with dissolve
    $ unlock_gallery_slot("cg", "e02s04")
    pause
    scene e02s04-59-2 mc-mh-getup_c2 with dissolve
    play voice3 lissa_ha noloop
    mh "Shower time, Baby."

    $ renpy.music.set_volume(0.7, 2.0, "music" )
    jump e02s04_next_day_2

label e02s04_next_day_2:

    scene black
    show screen scene_transistion(_("One shower later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.25, 2.0, "music" )
    play sound2 park fadein 3.0
    scene e02s04-61 mc-mh-ms-dn-entry2_c2
    with Fade(0.5, 0.5, 0.5)
    pause
    play voice3 dahlia_thinking_hmm1 noloop
    mh "Well well well, I see we have visitors."
    scene e02s04-60 mc-mh-ms-dn-entry1_c1 with dissolve
    play voice2 d1s2_mchey noloop volume 1.3
    mc "Hi. Can we help you?"
    scene e02s04-61 mc-mh-ms-dn-entry2-2_c4 with dissolve
    play voice4 cynthia_hey_happy noloop
    ms "Hello. We're in the next cabin over. I'm Mikaela and this is Dorothy."
    ms "Dorothy wanted to talk to you later, but I was hoping to catch you before you hit the slopes."
    scene e02s04-62 mc-mh-ms-dn-entry3_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Nice to meet you two."
    scene e02s04-62 mc-mh-ms-dn-entry3_c2 with dissolve
    play voice3 lissa_aga noloop
    mh "I'm Lyssa and this is my boyfriend. Let's get in from the cold."
    play sound sfx_door_closed1
    stop sound2 fadeout 3.0
    scene e02s04-63 mc-mh-ms-dn-inside1_c2 with fade
    play voice3 dahlia_thinking_hmm4 noloop
    mh "Everything alright, Mikaela?"
    scene e02s04-63 mc-mh-ms-dn-inside1_c4 with dissolve
    play voice4 cynthia_yes_yep1 noloop
    ms "Hmmm. Yup. I thought so."
    scene e02s04-63 mc-mh-ms-dn-inside1_c3 with dissolve
    play sound sfx_metal_fence1
    play voice3 dahlia_arrogant_huh noloop
    mh "What?"
    play voice5 girl12_thinking_hmm8 noloop
    dn "You two got the best cabin."
    play sound4 sfx_fire_fireplace1 fadein 3.0 volume 0.7
    $ renpy.music.set_volume(1.0, 0.0, "sound4" )
    scene e02s04-65 mc-mh-ms-dn-talk1_c1 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "Aren't they all the same layout?"
    scene e02s04-65 mc-mh-ms-dn-talk1_c4 with dissolve
    play voice4 cynthia_yes_aga noloop
    ms "Same layout, but ours keep getting hit with the wind. It's built secure enough, but that cold likes to sneak in through the walls."
    ms "But it's fine. If we didn't have a cold cabin, we wouldn't enjoy the sauna so much."
    scene e02s04-65 mc-mh-ms-dn-talk1_c3 with dissolve
    play voice5 girl12_thinking_hmm9 noloop
    dn "Mmhmm. That's true."
    scene e02s04-66 mc-mh-ms-dn-talk2_c2 with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    mh "So, what brings you over this early?"
    scene e02s04-66 mc-mh-ms-dn-talk2_c4 with dissolve
    play voice4 cynthia_disappointed_oof noloop
    ms "We wanted to apologize for how we acted yesterday."
    scene e02s04-66 mc-mh-ms-dn-talk2_c3 with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    mh "I don't understand."
    scene e02s04-66 mc-mh-ms-dn-talk2_c4 with dissolve
    play voice4 cynthia_arrogant_hm noloop
    ms "That couple just couldn't leave you alone to enjoy your vacation."
    scene e02s04-67 mc-mh-ms-dn-talk3_c3 with dissolve
    play voice5 girl12_yes_yeah5 noloop
    dn "We certainly could have stuck around and maybe given you an out."
    scene e02s04-68 mc-mh-ms-dn-talk4_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "That's really nice of you to be concerned, but it wasn't all bad."
    scene e02s04-74 mc-mh-ms-dn-diary5_c4 with dissolve
    play voice4 cynthia_surprised_huh noloop
    ms "Really? They weren't like stalking you or something?"
    scene e02s04-75 mc-mh-ms-dn-leave1_c1 with dissolve
    play voice2 d9s3_no noloop volume 1.7
    mc "No. It was more of a misunderstanding. I mean, don't get me wrong, they're an interesting pair, but not jerks or anything like that."
    scene e02s04-75 mc-mh-ms-dn-leave1_c2 with dissolve
    play voice3 lissa_yes noloop
    mh "Yes, we even ended up... I guess you'd say we shared a few words of potential wisdom."
    scene e02s04-75 mc-mh-ms-dn-leave1_c3 with dissolve
    play voice5 girl12_thinking_hmm7 noloop
    dn "Well, now you have to tell us what it was about."
    play voice4 cynthia_yes_yeah1 noloop
    ms "Totally. Hosts shouldn't tease their guests."
    scene e02s04-67 mc-mh-ms-dn-talk3_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mh "They were curious about us because I am transgender. We ended up talking after that about our relationships."
    scene e02s04-74 mc-mh-ms-dn-diary5_c4 with dissolve
    play voice4 cynthia_happy_mmm noloop
    ms "And you two are comfortable... talking with people about their relationships?"
    scene e02s04-75 mc-mh-ms-dn-leave1_c1 with dissolve
    play voice2 d3s11b_mcheh noloop
    mc "Hehe, well we're not usually super open around strangers, but everyone kept their clothes on."
    play voice3 lissa_ugu2 noloop
    mh "Mmhmm."
    scene e02s04-75 mc-mh-ms-dn-leave1_c4 with dissolve
    play voice4 cynthia_thinking_hmm4 noloop
    ms "Mind if I ask you something?"
    play voice3 lissa_aga noloop
    mh "Go ahead, I won't bite."
    play voice5 girl12_thinking_hmm6 noloop
    dn "Has your situation affected your sex life?"
    scene e02s04-76 mc-mh-ms-dn-leave2_c2 with dissolve
    play voice3 dahlia_thinking_oh noloop
    mh "[mcname] and I have a very great relationship. Despite whatever obstacles we may face, we overcome them through communication and love."
    scene e02s04-75 mc-mh-ms-dn-leave1_c3 with dissolve
    play voice4 cynthia_disappointed_oh noloop
    ms "That sounds wonderful."
    ms "We actually came to Snowy Peaks to talk to a counselor about it, but he didn't make it."
    scene e02s04-76 mc-mh-ms-dn-leave2_c1 with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "The other couple, they came to see him too."
    play sound sfx_pencil_writing1 volume 2.0
    scene e02s04-72 mc-mh-ms-dn-diary3_c3 with dissolve
    play voice5 girl12_thinking_oh1 noloop
    dn "Oh... that makes sense. Then maybe we should invite them to our next meeting."
    play voice3 dahlia_thinking_mmm1 noloop
    mh "Meeting?"
    stop sound fadeout 1.0
    scene e02s04-74 mc-mh-ms-dn-diary5_c4 with dissolve
    play voice4 cynthia_yes_calm noloop
    ms "Yes we met with Frank and Ashley - the Coopers. They're another couple here."
    scene e02s04-75 mc-mh-ms-dn-leave1_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Right, we met them earlier."
    scene e02s04-75 mc-mh-ms-dn-leave1_c3 with dissolve
    play voice4 cynthia_thinking_hmm1 noloop
    ms "That's great. Ever since we met them we've been having our own counseling sessions."
    play voice5 girl12_yes_aga5 noloop
    dn "Just minus the counselor."
    ms "Maybe we don't need one. You two seem to have things figured out. Maybe... you could listen in and share some advice."
    dn "Hmmm."
    scene e02s04-75 mc-mh-ms-dn-leave1_c4 with dissolve
    play voice4 cynthia_yes_yep1 noloop
    ms "The meetings are nice and casual, very low presh."
    ms "I'm sure Frank and Ashley would love to get your thoughts too!"
    scene e02s04-76 mc-mh-ms-dn-leave2_c2 with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    mh "We will certainly have to consider it."
    scene e02s04-76 mc-mh-ms-dn-leave2_c4 with dissolve
    play voice5 girl12_thinking_huh1 noloop
    dn "Great. We'll stay in touch."

    jump e02s04_end

label e02s04_end:

    play sound sfx_door_openclosed2
    scene e02s04-77 mc-mh-ms-dn-end1_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "Seems like everyone is here for therapy except us."
    mc "Is it even appropriate for us to get involved?"
    scene e02s04-77 mc-mh-ms-dn-end1_c2 with dissolve
    play voice3 dahlia_yes_ugu noloop
    mh "I think so. We're just offering advice based on our own experience."
    scene e02s04-78 mc-mh-ms-dn-end2_c2 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.6
    mc "It's strange how open they are with us."
    play voice3 lissa_thinking noloop
    mh "Some people have issues opening up to doctors because it can be difficult when the subject is sexual."
    mh "I mean some professionals don't even have the vocabulary to cover it."
    scene e02s04-78 mc-mh-ms-dn-end2_c1 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "And we do?"
    play voice3 dahlia_thinking_hmm4 noloop
    mh "We will after we spend some time studying up today. I'm going to need your phone again, [mcname]."
    play sound sfx_cloth_rustling4
    scene e02s04-79 mc-mh-ms-dn-end3_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Wait... we're actually doing this?"
    scene e02s04-79 mc-mh-ms-dn-end3_c2 with dissolve
    play voice3 lissa_ha noloop
    mh "You don't want to?"
    scene e02s04-80 mc-mh-ms-dn-end4_c1 with dissolve
    play voice2 mc_no_no2 noloop
    mc "No it's not that, it's just... I guess it is kind of exciting."
    mc "Everyone deserves love and if we can help some people with their problems, I'm game."
    scene e02s04-80 mc-mh-ms-dn-end4_c2 with dissolve
    play voice3 lissa_moan1 noloop
    mh "Good. And while we're preparing, we can figure out who we should focus our efforts on."

    stop music fadeout 3.0
    stop sound4 fadeout 3.0
    jump e02s05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
