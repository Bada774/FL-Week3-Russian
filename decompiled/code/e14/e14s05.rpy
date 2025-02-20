image e14s05-a61-glam = Movie(play = "images/E-14/s05/anim/e14s05-a61-4x-60fps.webm", start_image = "e14s05-a61-pw-walks-bg1-glambot-61-00", image = "e14s05-a61-pw-walks-bg1-glambot-61-89", loop = False)

label e14s05:

    scene black
    show screen scene_transistion(_("Some time later"))
    with Fade(0.9, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene e14s05-01-noras-cafe
    play music music_positive_hiphop fadein 1.5
    $ renpy.music.set_volume(1.0, 3.0, "sound4")
    play sound4 sfx_seawaves_ambience2 fadein 2.0
    with Fade(0.5, 0.5, 0.9)
    pause
    scene e14s05-02-nora-with-couple with dissolve
    pause
    $ renpy.music.set_volume(0.1, 3.0, "sound4")
    scene e14s05-03-pw-leaning with dissolve
    pause
    scene e14s05-04-mc-looks-at-nk with dissolve
    pause
    $ renpy.music.set_volume(0.3, 3.0, "music")
    scene e14s05-05-nk-talks-mc with dissolve
    play voice4 nora_heh noloop
    nk "How are the books looking Mr. Big Business?"
    scene e14s05-06-mc-talks-nk with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "They don't look that bad if I'm honest."
    scene e14s05-07-nk-talks-mc with dissolve
    play voice4 nora_hmm noloop volume 2.0
    nk "That deserves a drink and a break."
    scene e14s05-08-mc-talks-nk with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "After staring at all these numbers, I could go for a drink."
    scene e14s05-09-mc-nk-book with dissolve
    pause
    scene e14s05-10-nk-talks-pw with dissolve
    play voice4 nora_hey noloop
    nk "What are ya' thinking about?"
    scene e14s05-11-pw-talks-nk with dissolve
    play voice3 polly_emmm noloop
    pw "That couple from the other day, Gemma and Harry."
    play sound [sfx_coffee_machine, sfx_coffee_pouring]
    scene e14s05-12-nk-talks-pw with dissolve
    play voice4 aaleyah_thinking_oh noloop
    nk "The one we told about how we met?"
    scene e14s05-13-pw-talks-nk with dissolve
    play voice3 polly_aga noloop
    pw "That exact couple."
    scene e14s05-14-mc-talks with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Introspective again?"
    stop sound fadeout 1.0
    scene e14s05-15-pw-talks-mc with dissolve
    play voice3 polly_laugh2 noloop
    pw "I'm a deep thinker. Got lots to think about these days."
    play sound sfx_cup_slide1 volume 2.0
    scene e14s05-16-nk-puts-a-coffee with dissolve
    pause
    scene e14s05-17-mc-talks-nk with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "When you said drink, I thought you meant something with alcohol in it."
    scene e14s05-18-nk-talks-mc with dissolve
    play voice4 aaleyah_no_nah noloop
    nk "You're still on the clock [mcname]."
    scene e14s05-19-mc-talks with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Uuuugggghhhhhhhhhhh."
    play sound sfx_drink_slurp2
    scene e14s05-20-mc-takes-a-sip with dissolve
    pause
    scene e14s05-21-nk-talk-pw with dissolve
    play voice4 aaleyah_thinking_hmm3 noloop
    nk "Penny for your thoughts?"
    scene e14s05-22-pw-talks with dissolve
    play voice3 stacy_happy_hmm1 noloop
    pw "I'm just thinking about how good our life is nowadays."
    scene e14s05-23-mc-talks-pw with dissolve
    play voice2 d9s2_ugu noloop volume 2.5
    mc "It is pretty good, isn't it."
    scene e14s05-24-pw-talks-mc with dissolve
    play voice3 polly_impressed noloop
    pw "And how I want to share it with everyone else."
    scene e14s05-25-nk-talks-pw with dissolve
    play voice4 aaleyah_arrogant_heh noloop
    nk "You want to just start handing out blindfolds to people and hope it works?"
    pw "No. I'm thinking we should do like an event or something."
    play sound sfx_cup_place1
    scene e14s05-26-mc-talks-nk-pw with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "That's actually a pretty good idea."
    scene e14s05-27-mc-talks with dissolve
    mc "Events are good for cafes and bars. Think about it 'Ladies Night', 'Thirsty Thursdays', 'Singles Night'."
    scene e14s05-28-pw-talks with dissolve
    play voice3 stacy_yes_yeah1 noloop
    pw "Yeah, singles night! That's pretty much it!"
    scene e14s05-29-nk-talks with dissolve
    play voice4 aaleyah_surprised_oh noloop
    nk "A singles night with blindfolds?"
    scene e14s05-30-pw-talks with dissolve
    play voice3 polly_yes1 noloop
    pw "Yeah. You have to love that idea Nora."
    scene e14s05-31-mc-talks-nk with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "Of all people, you can't hate that idea."
    scene e14s05-32-nk-talks-pw with dissolve
    play voice4 aaleyah_thinking_hmm2 noloop
    nk "... I don't."
    scene e14s05-33-pw-talks with dissolve
    play voice3 stacy_happy_relief1 noloop
    pw "Does that mean we're going to do it!?"
    scene e14s05-34-mc-talks with dissolve
    play voice2 d9s2_mcyes noloop volume 2.5
    mc "I think it's a good idea."
    scene e14s05-35-pw-talks with dissolve
    play voice3 polly_wooh noloop
    pw "Great!! I've got an idea for a flier already!"
    scene e14s05-36-pw-runs-up with dissolve
    pause
    scene e14s05-37-nk-talks-mc with dissolve
    play voice4 aaleyah_disappointed_mff noloop
    nk "I'm shocked."
    scene e14s05-38-mc-talks-nk with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "About?"
    scene e14s05-39-nk-talks-mc with dissolve
    play voice4 aaleyah_disappointed_eeh2 noloop
    nk "That Polly had a good idea for this place that didn't require giving out a bunch of free drinks."
    scene e14s05-40-mc-talks-nk with dissolve
    play voice2 d9s2_yeah noloop volume 2.5
    mc "She's learning."
    scene e14s05-41-couple with dissolve
    pause
    scene e14s05-42-nk-talk-mc with dissolve
    play voice4 aaleyah_disappointed_eh1 noloop
    nk "God helps us all."
    scene e14s05-43-nk-walks with dissolve
    pause
    $ renpy.music.set_volume(0.5, 2.0, "sound4")
    scene e14s05-44-beach with dissolve
    pause
    scene e14s05-45-nk-talks-pw with dissolve
    play voice4 nora_heh noloop
    nk "How'd the fliers turn out?"
    scene e14s05-46-pw-fliers with dissolve
    pause
    scene e14s05-47-close-up-flier with dissolve
    pause
    scene e14s05-48-mc-talks-pw with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "Those look great, Polly."
    scene e14s05-49-pw-talk-mc with dissolve
    play voice3 polly_laugh noloop
    pw "Thank you! I've been thinking about this for a little bit."
    scene e14s05-50-mc-talk-pw with dissolve
    play voice2 mc_yes_okay2 noloop volume 1.7
    mc "This is your event, why don't you do the first sales pitch."
    scene e14s05-a61-pw-walks-bg1-glambot-61-00 with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 3.0>", sfx_camera_fly1] noloop volume 2.0
    scene e14s05-a61-glam
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene e14s05-62-pw-talk-bg1 with dissolve
    play voice3 polly_hey noloop
    pw "Hi! How's your day going?"
    scene e14s05-63-bg1-talks-pw with dissolve
    play voice5 girl28_hey_sexy noloop
    "Woman" "It's going well? Can I help you?"
    scene e14s05-64-pw-talks-bg1 with dissolve
    play voice3 stacy_thinking_hm1 noloop
    pw "I'm actually an owner at Nora's which is just down that way."
    scene e14s05-65-pw-talks-bg1 with dissolve
    pw "We're going to be hosting our first ever event!"
    scene e14s05-66-bg1-grabs-flier with dissolve
    pause
    scene e14s05-67-bg1-talks-pw with dissolve
    play voice5 girl28_disappointed_eeh2 noloop
    "Woman" "It's a... Blind dating event?"
    scene e14s05-68-pw-talks-bg1 with dissolve
    play voice3 stacy_yes_yeah2 noloop
    pw "Yeah! But with a twist. You're going to be {i}actually{/i} blind. We've got blindfolds and you'll be seated and-"
    scene e14s05-69-bg1-talks-pw with dissolve
    play voice5 girl28_arrogant_hah3 noloop
    "Woman" "It can't be as bad as my last date."
    scene e14s05-70-nk-talks-bg1 with dissolve
    play voice4 nora_nhey noloop
    nk "And we have plenty of alcohol for sale if it does!"
    scene e14s05-71-bg1-talks-nk with dissolve
    play voice5 girl28_arrogant_huh1 noloop
    "Woman" "Wait... I thought this was at a cafe?"
    scene e14s05-72-nk-talks-bg1 with dissolve
    play voice4 nora_aga noloop
    nk "It is. We're also a bar though."
    scene e14s05-73-bg1-talks-nk with dissolve
    play voice5 girl28_arrogant_hmm3 noloop
    "Woman" "Do we get, like, a singles night discount then?"
    scene e14s05-74-pw-talks-bg1 with dissolve
    play voice3 polly_yes1 noloop
    pw "Absolutely!"
    scene e14s05-75-nk-talks-pw with dissolve
    play voice4 aaleyah_disappointed_oof1 noloop
    nk "Wait, Polly-"
    scene e14s05-76-bg1-talks-pw with dissolve
    play voice5 girl28_happy_yeah1 noloop
    "Woman" "I've done worse for less!"
    scene e14s05-77-pw-talks-bg1 with dissolve
    play voice3 polly_laughter noloop
    pw "We'll see you there then! Ta-ta!"
    scene e14s05-78-nk-looks-bg1 with dissolve
    pause
    scene e14s05-79-nk-looks-pw with dissolve
    pause
    scene e14s05-80-nk-talks-bg1 with dissolve
    play voice4 amrose_old_psst2 noloop
    nk "Just... Don't tell your friends about the discount."
    scene e14s05-81-mc-walks with dissolve
    pause
    scene e14s05-82-bg1-talks with dissolve
    play voice5 girl28_arrogant_heh noloop
    "Woman" "This actually looks like fun."
    scene e14s05-83-pw-fliers with dissolve
    pause
    scene e14s05-84-bg2 with dissolve
    pause
    scene e14s05-85-pw-looks-bg2 with dissolve
    pause
    scene e14s05-86-pw-talks-nk with dissolve
    play voice3 stacy_hey_attention1 noloop
    pw "Hey Nora, why don't you try selling the event to her?"
    scene e14s05-87-nk-talks-pw with dissolve
    play voice4 aaleyah_disappointed_oh1 noloop
    nk "Uhhhhh, I mean. You've-you've been doing great! I think you should."
    scene e14s05-88-mc-talks-nk with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Come on. Give it a try."
    scene e14s05-89-nk-talks-mc with dissolve
    play voice4 aaleyah_surprised_huh1 noloop
    nk "You too, [mcname]?"
    scene e14s05-90-mc-talks-nk with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "I'm taking directions from the boss."
    scene e14s05-91-nk-talks-mc with dissolve
    play voice4 nora_arghh noloop
    nk "The damn cafe bar is named after me!"
    scene e14s05-92-pw-talks-nk with dissolve
    play voice3 polly_mmmuhuh noloop
    pw "We all know who's in charge though."
    scene e14s05-93-pw-talks-nk with dissolve
    pw "Come on, get in there. You got this."
    scene e14s05-94-mc-talk-nk with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah. Think of this like when you were getting comfortable being naked at the cafe!"
    scene e14s05-95-nk-talks-mc with dissolve
    play voice4 aaleyah_no_uhuh2 noloop
    nk "This is not like the cafe. There, I can see everyone staring at me!"
    scene e14s05-94-mc-talk-nk with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Everyone here is naked Nora, you're going to do great!"
    scene e14s05-96-nk-talks-pw with dissolve
    play voice4 aaleyah_angry_egh1 noloop
    nk "Do I haaaaave to?"
    scene e14s05-97-pw-talks-nk with dissolve
    play voice3 stacy_yes_yap2 noloop
    pw "Yep!"
    scene e14s05-99-bg2-talks-nk with dissolve
    play voice5 girl27_hey_sexy noloop
    "Woman" "Hey."
    scene e14s05-100-nk-talks-bg2 with dissolve
    play voice4 aaleyah_disappointed_mff2 noloop volume 1.4
    nk "Oh, uhm, hi. I'm Nora."
    scene e14s05-101-bg2-looks-nk-apron with dissolve
    nk "Oh yeah, it's on my tits - my apron!"
    scene e14s05-102-nk-apron with dissolve
    pause
    scene e14s05-103-nk-talks-bg2 with dissolve
    play voice4 aaleyah_thinking_oh noloop
    nk "We're doing an event. It's like a dating event and singles event and-"
    scene e14s05-104-nk-talks-mc with dissolve
    nk "And we're doing drink specials, and here's the flier."
    scene e14s05-105-nk-talk-bg2 with dissolve
    pause
    scene e14s05-106-bg2-talk-nk with dissolve
    play voice5 girl27_thinking_emm noloop
    "Woman" "Blind dating?"
    scene e14s05-107-nk-talks-bg2 with dissolve
    play voice4 aaleyah_yes_yeah1 noloop
    nk "Yeah. We're doing speed dating with a twist. Everyone wears a blindfold during the dates."
    scene e14s05-108-bg2-talks-nk with dissolve
    play voice5 girl27_surprised_oh2 noloop
    "Woman" "Oh, that's pretty cool."
    scene e14s05-109-nk-talks-bg2 with dissolve
    play voice4 nora_huuuh noloop
    nk "It's our way of trying to - Wait. You think it's cool?"
    scene e14s05-110-bg2-talks-nk with dissolve
    play voice5 girl27_yes_yeah6 noloop
    "Woman" "Yeah, and kind of kinky too. I'm about it."
    scene e14s05-112-nk-talks-bg2 with dissolve
    play voice4 nora_auh noloop
    nk "Oh, I wasn't really expecting you to be into it."
    scene e14s05-111-bg2-talks-nk with dissolve
    play voice5 girl27_surprised_huh3 noloop
    "Woman" "Why not?"
    scene e14s05-114-nk-talks-bg2 with dissolve
    play voice4 aaleyah_disappointed_eeh noloop
    nk "Uhhhh, I don't know."
    scene e14s05-113-bg2-talks-nk with dissolve
    play voice5 girl27_thinking_hmm5 noloop
    "Woman" "When is the event?"
    nk "It's on the flier."
    scene e14s05-115-bg2-talks-nk with dissolve
    play voice5 girl27_disappointed_mmm noloop
    "Woman" "Are you going to be there?"
    scene e14s05-109-nk-talks-bg2 with dissolve
    play voice4 aaleyah_yes_yep noloop
    nk "Yep, it's going to be at Nora's, I'm the owner."
    scene e14s05-116-nk-tits with dissolve
    play voice5 girl27_no_nouh noloop
    "Woman" "That's not what I'm staring at."
    scene e14s05-117-nk-talks-bg2 with dissolve
    play voice4 aaleyah_surprised_ah1 noloop
    nk "Ohhh, uhhh, unfortunately I'm, uhm, going to be running the event. Not participating."
    scene e14s05-118-bg2-talks-nk with dissolve
    play voice5 girl27_disappointed_ehh2 noloop
    "Woman" "That's a damn shame."
    scene e14s05-119-nk-talks-bg2 with dissolve
    play voice4 aaleyah_happy_laugh2 noloop
    nk "Well I'm glad we'll see you there!"
    scene e14s05-120-pw-talks-nk with dissolve
    play voice3 stacy_happy_wooh1 noloop
    pw "That was great!"
    scene e14s05-121-mc-talks-nk with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah! You killed it, Nora."
    scene e14s05-122-nk-talks with dissolve
    play voice4 aaleyah_angry_grrr1 noloop
    nk "God please don't make me do that again."
    scene e14s05-123-pw-talks-mc with dissolve
    play voice3 polly_laugh3 noloop
    pw "Come ooooon, it wasn't that bad!"
    scene e14s05-124-nk-talks-pw with dissolve
    play voice4 aaleyah_arrogant_pff noloop
    nk "I'd rather die than have to talk to another person about the event."
    scene e14s05-125-pw-talks-nk with dissolve
    play voice3 stacy_yes_fine3 noloop
    pw "That's okay. From here on out, I'll do the talking."
    scene e14s05-126-pw-talks-nk with dissolve
    play voice3 stacy_suckmoan2 noloop
    pw "All you need to do is hand out fliers and look hot."
    $ renpy.music.set_volume(0.8, 1.5, "music")
    $ renpy.music.set_volume(1.0, 2.0, "sound4")
    scene e14s05-127-montage with dissolve
    pause
    scene e14s05-128-montage with dissolve
    pause
    scene e14s05-129-montage with dissolve
    pause
    scene e14s05-130-montage with dissolve
    pause
    scene e14s05-131-mc-nk-pw with dissolve
    pause
    $ renpy.music.set_volume(0.6, 2.0, "sound4")
    $ renpy.music.set_volume(0.4, 2.5, "music")
    scene e14s05-132-pw-talks-nk with dissolve
    play voice3 stacy_happy_phew3 noloop
    pw "Aaaaaand that was the last one! Looks like we're done here."
    scene e14s05-133-nk-talks with dissolve
    play voice4 aaleyah_angry_cagh1 noloop
    nk "Thank Christ Almighty."
    scene e14s05-134-mc-talks-nk with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Come on Nora, it wasn't that bad."
    scene e14s05-135-nk-talks-mc with dissolve
    play voice4 nora_angrymoan noloop volume 1.8
    nk "I miss my counter."
    scene e14s05-136-pw-talks-mc with dissolve
    play voice3 polly_oh noloop
    pw "Oh! You know what I miss?"
    scene e14s05-137-mc-talks-pw with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "What's that, Polly?"
    scene e14s05-138-pw-talks-mc with dissolve
    play voice3 polly_angry noloop
    pw "Your dick in my ass. Let's go back to the cafe and fuck!"
    scene e14s05-139-nk-talks with dissolve
    play voice4 nora_oh noloop
    nk "Honestly, all the naked people has made me kind of horny. I could use with a dicking down too."
    scene e14s05-140-mc-talks with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "No complaints from me, let's go!"
    scene e14s05-141-nk-talks with dissolve
    play voice4 nora_hmm noloop volume 2.2
    nk "But after, we need to start getting ready for the event."
    scene e14s05-142-pw-talks-nk with dissolve
    play voice3 polly_nouh noloop
    pw "Come on Nora, all work and no play makes Jill a dull girl. Let's not think about that and have some fun!"
    scene e14s05-143-nk-talks-pw with dissolve
    play voice4 aaleyah_disappointed_mff noloop
    nk "Fiiiiine, no work talk for... At least for an hour."
    scene e14s05-144-pw-talks with dissolve
    play voice3 stacy_happy_yay3 noloop
    pw "Yay!"
    stop music fadeout 3.0
    stop sound4 fadeout 3.0

    jump e14s06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
