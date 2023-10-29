init python:

    import random

    class clicker_projectile:
        def __init__(self, icon, travel_time):
            self.icon = icon
            self.travel_time = travel_time
            
            self.give_point = 1
            self.is_shown = False
            self.screen_time = 0.0
            self.max_time = travel_time - 0.5
            self.x = 0
            self.y = 0
        
        def click_projectile(self, g, this):
            global d19s05_player_hp
            global d19s05_minigame_score
            global d19s05_score_multiplier
            
            if int(self.icon[-1]) < 7:
                d19s05_minigame_score += this.give_point
                d19s05_score_multiplier += 0.1
                renpy.play("audio/zvukipro/nonextended/sfx_d19s05_minigame_good.ogg", channel="sound5")
            else:
                d19s05_player_hp -= 1
                d19s05_score_multiplier = 1.0
                renpy.play("audio/zvukipro/nonextended/sfx_d19s05_minigame_bad.ogg", channel="sound5")
            
            self.x = 0
            self.y = 0
            self.screen_time = 2.0
            self.is_shown = False

    class projectile_handler:
        def __init__(self):
            self.spawn_time = 0.5
            self.screen_empty = False
            
            global d19s05_icons_list
            self.projectiles = d19s05_icons_list
        
        def random_projectile(self, og_list):
            shuffled_list = list(og_list)
            random.shuffle(shuffled_list)
            return iter(shuffled_list)
        
        def spawn_projectile(self):
            global d19s05_player_hp
            global d19s05_difficulty
            global d19s05_step
            
            d19s05_step += 0.1
            d19s05_difficulty += 0.06
            random_chance = random.randint(1,10)
            
            for i in self.projectiles:
                if i.is_shown is True and int(i.icon[-1]) < 6:
                    self.screen_empty = False
                    break
                self.screen_empty = True
            
            for i in self.projectiles:
                if i.is_shown is True:
                    i.screen_time += self.spawn_time
                    if i.screen_time > i.max_time:
                        i.x = 0
                        i.y = 0
                        i.screen_time = 2.0
                        i.is_shown = False
                        if int(i.icon[-1]) < 7:
                            d19s05_player_hp -= 1
                            d19s05_score_multiplier = 1.0
            
            if random_chance < round(d19s05_difficulty) or self.screen_empty is True:
                for i in self.random_projectile(self.projectiles):
                    if i.is_shown is True:
                        pass
                    else:
                        if i.screen_time:
                            i.screen_time -= self.spawn_time
                        else:
                            i.x = random.randint(-400, 400)
                            if i.x > 350 or i.x < -350:
                                i.y = -720
                            elif i.x > 300 or i.x < -300:
                                i.y = -760
                            else:
                                i.y = -800
                            i.is_shown = True
                            break

default persistent.minigame_max_score = 0

screen minigame_screen():

    $ g = projectile_handler()

    modal True

    key "mouseup_3" action NullAction()
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "K_PAUSE" action NullAction()
    key "pad_guide_press" action NullAction()
    key "pad_start_press" action NullAction()

    use minigame_ui()

    timer g.spawn_time repeat True action Function(g.spawn_projectile)

    for i in g.projectiles:
        $ mask_path = "images/Day-19/s05/minigame/minigame_mask_" + str(i.icon[-1]) + ".webp"
        if i.is_shown is False:
            $ i.travel_time = d19s05_speed_multiplier[int(d19s05_step)]
            $ i.max_time = i.travel_time - 0.5
        else:
            button:
                xalign 0.42
                yalign 0.98
                background None
                focus_mask mask_path
                action Function(i.click_projectile, g, i)
                vbox:
                    add i.icon
                    bar:
                        value (i.max_time - i.screen_time)
                        range i.max_time
                        xalign 0.5
                        ypos -10
                        xsize 100
                        ysize 20
                        left_bar "#FFF"

                at minigame_spawn(i.travel_time, i.x, i.y)

    add "minigame_book_overlay"

    if config.developer is True:
        vbox:
            xalign 0.01
            yalign 0.99
            spacing 10
            for i in g.projectiles:
                $ object_name = str(i.icon)
                if i.is_shown is True:
                    vbox:
                        text "[object_name]"
                        text "Screen Time: {}".format(i.screen_time) color "#FFFFFF"
                        text "Max Time: {}".format(i.max_time) color "#FFFFFF"

    if d19s05_player_hp <= 1:
        add "images/Day-19/s05/minigame/minigame_low_hp.webp" at minigame_low_hp

screen minigame_ui():

    timer 0.1 action (If(round(d19s05_minigame_timer) > 0, true = SetVariable("d19s05_minigame_timer", d19s05_minigame_timer - 0.1), false = (Jump("d19s05_after_minigame"), Hide("minigame_screen"))), If(d19s05_player_hp > 0, true = NullAction(), false = (Jump("d19s05_after_minigame"), Hide("minigame_screen")))) repeat If(round(d19s05_minigame_timer) > 0, true = True, false = False)

    frame:
        xalign 0.0
        yalign 0.0
        background "#00000050"
        xsize 235
        ysize 75
        has hbox:
            xfill True
            spacing -30
        add "images/Day-19/s05/minigame/minigame_clock_icon.webp" yalign 0.52
        if round(d19s05_minigame_timer) >= 10:
            text "00:{:.0f}".format(d19s05_minigame_timer) color "#FFFFFF" size 50 yalign 0.6
        else:
            text "00:0{:.0f}".format(d19s05_minigame_timer) color "#FFFFFF" size 50 yalign 0.6
    frame:
        xalign 1.0
        yalign 0.0
        background "#00000050"
        xsize 226
        ysize 75
        has hbox:
            xfill True
            spacing 10
        if d19s05_player_hp == 0:
            add "images/Day-19/s05/minigame/minigame_no_heart_icon.webp" yalign 0.5
        elif d19s05_player_hp >= 1:
            add "images/Day-19/s05/minigame/minigame_heart_icon.webp" yalign 0.5
        if d19s05_player_hp >= 2:
            add "images/Day-19/s05/minigame/minigame_heart_icon.webp" yalign 0.5
        elif d19s05_player_hp == 1 or d19s05_player_hp == 0:
            add "images/Day-19/s05/minigame/minigame_no_heart_icon.webp" yalign 0.5
        if d19s05_player_hp == 3:
            add "images/Day-19/s05/minigame/minigame_heart_icon.webp" yalign 0.5
        elif d19s05_player_hp <= 2 or d19s05_player_hp == 0:
            add "images/Day-19/s05/minigame/minigame_no_heart_icon.webp" yalign 0.5

    if config.developer is True:
        vbox:
            xsize 300
            xalign 0.99
            yalign 0.93
            spacing 5
            text ("Multiplier: [d19s05_score_multiplier]") color "#FFFFFF" xanchor 1.0 xalign 1.0
            text ("Score: [d19s05_minigame_score]") color "#FFFFFF" xanchor 1.0 xalign 1.0
            text ("Difficulty: [d19s05_difficulty]") color "#FFFFFF" xanchor 1.0 xalign 1.0
            text ("Step: [d19s05_step]") color "#FFFFFF" xanchor 1.0 xalign 1.0

    vbox:
        xalign 1.0
        yalign 1.0
        button:
            text _("Skip"):
                idle_color "#FFFFFF"
                hover_color "#E34364"
                outlines [ (absolute(1), "#000", 0, 0) ]
                size 45
            action (Jump("d19s05_skip_minigame"), Hide("minigame_screen"))
            xanchor 1.0
            xalign 1.0
            if config.developer is True:
                keysym 'K_s'

transform minigame_spawn(wait, posx, posy):
    subpixel True
    linear wait xoffset posx yoffset posy

transform minigame_low_hp():
    alpha 0.2
    block:
        linear 1.0 alpha 0.1
        linear 1.0 alpha 0.3
        repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
