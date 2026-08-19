init python:

    import random
    import pygame


    class MinigameProjectile(object):
        
        def __init__(self, icon_id):
            self.icon_id = icon_id
            self.give_point = 1
            self.is_shown = False
            self.screen_time = 0.0
            self.travel_time = 1.0
            self.max_time = 0.5
            self.x = 0
            self.y = 0
            self.spawn_st = 0.0
        
        def despawn(self, cooldown=True):
            self.x = 0
            self.y = 0
            self.screen_time = 2.0 if cooldown else 0.0
            self.is_shown = False


    class MinigameState(renpy.python.NoRollback):
        
        def __init__(self):
            self.player_hp = 3
            self.score = 0
            self.score_multiplier = 1.0
            self.difficulty = 0.5
            self.step = 0.0
            self.timer = 60.0
            self.speed_multiplier = [8.0, 6.0, 5.5, 5.0, 4.5, 4.0, 3.0, 2.5, 2.0, 2.0, 1.5, 1.5]
            self.running = False
            self.finished = False
            self.next_spawn_st = 0.5


    class MinigameDisplayable(renpy.Displayable):
        
        SPAWN_INTERVAL = 0.5
        GAME_DURATION = 60.0
        REDRAW_INTERVAL = 1.0 / 60.0
        ICON_ALIGN_X = 0.42
        ICON_ALIGN_Y = 0.98
        BAR_WIDTH = 100
        BAR_HEIGHT = 20
        BAR_Y_OFFSET = -10
        ICON_COUNT = 9
        SFX_GOOD = "audio/zvukipro/nonextended/sfx_d19s05_minigame_good.ogg"
        SFX_BAD = "audio/zvukipro/nonextended/sfx_d19s05_minigame_bad.ogg"
        
        _mask_surfaces = {}
        
        def __init__(self, **kwargs):
            super(MinigameDisplayable, self).__init__(**kwargs)
            
            self.icons = [
                renpy.displayable("minigame_icon_%d" % i)
                for i in range(self.ICON_COUNT)
            ]
            self.masks = [
                renpy.displayable(
                    "images/Day-19/s05/minigame/minigame_mask_%d.webp" % i
                )
                for i in range(self.ICON_COUNT)
            ]
            self.bar_solid = Solid("#FFFFFF")
            
            self.projectiles = [MinigameProjectile(i) for i in range(self.ICON_COUNT)]
            self.state = MinigameState()
            self._layout = []
            self._width = 1920
            self._height = 1080
        
        
        @property
        def player_hp(self):
            return self.state.player_hp
        
        @player_hp.setter
        def player_hp(self, value):
            self.state.player_hp = value
        
        @property
        def score(self):
            return self.state.score
        
        @property
        def score_multiplier(self):
            return self.state.score_multiplier
        
        @property
        def difficulty(self):
            return self.state.difficulty
        
        @property
        def step(self):
            return self.state.step
        
        @property
        def timer(self):
            return self.state.timer
        
        def reset(self):
            for p in self.projectiles:
                p.is_shown = False
                p.screen_time = 0.0
                p.x = 0
                p.y = 0
                p.spawn_st = 0.0
                p.travel_time = 1.0
                p.max_time = 0.5
            
            s = self.state
            s.running = True
            s.finished = False
            s.next_spawn_st = self.SPAWN_INTERVAL
            s.player_hp = 3
            s.score = 0
            s.score_multiplier = 1.0
            s.difficulty = 0.5
            s.step = 0.0
            s.timer = self.GAME_DURATION
            
            speeds = getattr(renpy.store, "d19s05_speed_multiplier", None)
            if speeds is not None:
                s.speed_multiplier = list(speeds)
            
            self._layout = []
            self._ensure_mask_surfaces()
            self._update_idle_speeds()
            self.sync_to_store()
            renpy.redraw(self, 0)
        
        def stop(self):
            self.state.running = False
            self.state.finished = True
            self.sync_to_store()
        
        def sync_to_store(self):
            s = self.state
            renpy.store.d19s05_player_hp = s.player_hp
            renpy.store.d19s05_minigame_score = s.score
            renpy.store.d19s05_score_multiplier = s.score_multiplier
            renpy.store.d19s05_difficulty = s.difficulty
            renpy.store.d19s05_step = s.step
            renpy.store.d19s05_minigame_timer = s.timer
        
        def _ensure_mask_surfaces(self):
            for i, mask in enumerate(self.masks):
                if i not in MinigameDisplayable._mask_surfaces:
                    try:
                        MinigameDisplayable._mask_surfaces[i] = renpy.load_surface(mask)
                    except Exception:
                        MinigameDisplayable._mask_surfaces[i] = None
        
        def _speed_index(self):
            s = self.state
            idx = int(s.step)
            if idx < 0:
                idx = 0
            elif idx >= len(s.speed_multiplier):
                idx = len(s.speed_multiplier) - 1
            return idx
        
        def _update_idle_speeds(self):
            travel = self.state.speed_multiplier[self._speed_index()]
            for p in self.projectiles:
                if not p.is_shown:
                    p.travel_time = travel
                    p.max_time = travel - 0.5
        
        def _finish(self):
            if self.state.finished:
                return
            self.state.finished = True
            self.state.running = False
            self.sync_to_store()
            renpy.end_interaction(True)
        
        def _apply_good_click(self, p):
            s = self.state
            s.score += p.give_point
            s.score_multiplier += 0.1
            renpy.play(self.SFX_GOOD, channel="sound5")
            p.despawn(cooldown=True)
        
        def _apply_bad_click(self, p):
            s = self.state
            s.player_hp -= 1
            s.score_multiplier = 1.0
            renpy.play(self.SFX_BAD, channel="sound5")
            p.despawn(cooldown=True)
        
        def _apply_miss(self, p):
            s = self.state
            if p.icon_id < 7:
                s.player_hp -= 1
                s.score_multiplier = 1.0
            p.despawn(cooldown=True)
        
        def _spawn_tick(self, st):
            s = self.state
            s.step += 0.1
            s.difficulty += 0.06
            random_chance = random.randint(1, 10)
            
            screen_empty = True
            for p in self.projectiles:
                if p.is_shown and p.icon_id < 6:
                    screen_empty = False
                    break
            
            for p in self.projectiles:
                if p.is_shown:
                    p.screen_time += self.SPAWN_INTERVAL
                    if p.screen_time > p.max_time:
                        self._apply_miss(p)
            
            if random_chance < round(s.difficulty) or screen_empty:
                pool = list(self.projectiles)
                random.shuffle(pool)
                for p in pool:
                    if p.is_shown:
                        continue
                    if p.screen_time:
                        p.screen_time -= self.SPAWN_INTERVAL
                    else:
                        p.x = random.randint(-400, 400)
                        if p.x > 350 or p.x < -350:
                            p.y = -720
                        elif p.x > 300 or p.x < -300:
                            p.y = -760
                        else:
                            p.y = -800
                        travel = p.travel_time
                        p.max_time = travel - 0.5
                        p.screen_time = 0.0
                        p.spawn_st = st
                        p.is_shown = True
                        break
        
        def _projectile_pos(self, p, st, iw, ih, width, height):
            elapsed = max(0.0, st - p.spawn_st)
            if p.travel_time > 0:
                progress = min(1.0, elapsed / p.travel_time)
            else:
                progress = 1.0
            
            base_x = self.ICON_ALIGN_X * width - self.ICON_ALIGN_X * iw
            base_y = self.ICON_ALIGN_Y * height - self.ICON_ALIGN_Y * ih
            x = base_x + p.x * progress
            y = base_y + p.y * progress
            return x, y, elapsed
        
        def _hit_test(self, p, lx, ly, iw, ih):
            if lx < 0 or ly < 0 or lx >= iw or ly >= ih:
                return False
            
            surf = MinigameDisplayable._mask_surfaces.get(p.icon_id)
            if surf is not None:
                sw, sh = surf.get_size()
                mx = int(lx * sw / float(iw)) if iw else 0
                my = int(ly * sh / float(ih)) if ih else 0
                if mx < 0 or my < 0 or mx >= sw or my >= sh:
                    return False
                try:
                    return surf.get_at((mx, my))[3] > 0
                except Exception:
                    return False
            
            return True
        
        def render(self, width, height, st, at):
            self._width = width
            self._height = height
            render = renpy.Render(width, height)
            self._layout = []
            s = self.state
            
            if not s.running:
                return render
            
            remaining = max(0.0, self.GAME_DURATION - st)
            s.timer = remaining
            
            if remaining <= 0.0 or s.player_hp <= 0:
                self._finish()
                return render
            
            while st >= s.next_spawn_st:
                self._update_idle_speeds()
                tick_st = s.next_spawn_st
                self._spawn_tick(tick_st)
                s.next_spawn_st += self.SPAWN_INTERVAL
                if s.player_hp <= 0:
                    self._finish()
                    return render
            
            self._update_idle_speeds()
            
            for p in self.projectiles:
                if not p.is_shown:
                    continue
                
                icon = self.icons[p.icon_id]
                child = renpy.render(icon, width, height, st, at)
                iw, ih = child.get_size()
                x, y, elapsed = self._projectile_pos(p, st, iw, ih, width, height)
                
                render.blit(child, (x, y))
                
                left = max(0.0, p.max_time - elapsed)
                if p.max_time > 0:
                    fraction = min(1.0, left / p.max_time)
                else:
                    fraction = 0.0
                fill_w = max(0, int(self.BAR_WIDTH * fraction))
                if fill_w > 0:
                    bar = renpy.render(
                        self.bar_solid,
                        fill_w,
                        self.BAR_HEIGHT,
                        st,
                        at,
                    )
                    bar_x = x + (iw - self.BAR_WIDTH) * 0.5
                    bar_y = y + ih + self.BAR_Y_OFFSET
                    render.blit(bar, (bar_x, bar_y))
                
                self._layout.append((p, x, y, iw, ih))
            
            renpy.redraw(self, self.REDRAW_INTERVAL)
            return render
        
        def event(self, ev, x, y, st):
            s = self.state
            if s.finished:
                return True
            
            if not s.running:
                return None
            
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                for p, px, py, iw, ih in reversed(self._layout):
                    lx = x - px
                    ly = y - py
                    if self._hit_test(p, lx, ly, iw, ih):
                        if p.icon_id < 7:
                            self._apply_good_click(p)
                        else:
                            self._apply_bad_click(p)
                        
                        renpy.redraw(self, 0)
                        
                        if s.player_hp <= 0:
                            self._finish()
                            return True
                        raise renpy.IgnoreEvent()
            
            return None
        
        def visit(self):
            return list(self.icons) + list(self.masks) + [self.bar_solid]
        
        def per_interact(self):
            if self.state.running:
                renpy.redraw(self, 0)


    def d19s05_minigame_hud(st, at):
        cdd = renpy.store.d19s05_cdd
        hp = max(0, min(3, int(cdd.player_hp)))
        t = max(0.0, float(cdd.timer))
        timer_text = "00:{:02.0f}".format(t)
        
        heart = renpy.displayable("images/Day-19/s05/minigame/minigame_heart_icon.webp")
        empty = renpy.displayable("images/Day-19/s05/minigame/minigame_no_heart_icon.webp")
        clock_icon = renpy.displayable("images/Day-19/s05/minigame/minigame_clock_icon.webp")
        
        left = Fixed(
            Solid("#00000050"),
            Transform(clock_icon, yalign=0.5, xpos=8),
            Transform(Text(timer_text, color="#FFFFFF", size=50), yalign=0.6, xpos=70),
            xsize=235,
            ysize=75,
        )
        right = Fixed(
            Solid("#00000050"),
            Transform(heart if hp >= 1 else empty, yalign=0.5, xpos=16),
            Transform(heart if hp >= 2 else empty, yalign=0.5, xpos=70),
            Transform(heart if hp >= 3 else empty, yalign=0.5, xpos=124),
            xsize=226,
            ysize=75,
        )
        
        children = [
            Transform(left, xalign=0.0, yalign=0.0),
            Transform(right, xalign=1.0, yalign=0.0),
        ]
        if hp <= 1:
            children.append(
                Transform(
                    renpy.displayable("images/Day-19/s05/minigame/minigame_low_hp.webp"),
                    alpha=0.2,
                )
            )
        
        d = Fixed(
            *children,
            xfill=True,
            yfill=True,
        )
        return (d, 0.1)


default persistent.minigame_max_score = 0
default d19s05_cdd = MinigameDisplayable()

screen minigame_screen():

    modal True

    key "mouseup_3" action NullAction()
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "K_PAUSE" action NullAction()
    key "pad_guide_press" action NullAction()
    key "pad_start_press" action NullAction()

    add d19s05_cdd

    add "minigame_book_overlay"

    add DynamicDisplayable(d19s05_minigame_hud)

    vbox:
        xalign 1.0
        yalign 1.0
        button:
            text _("Skip"):
                idle_color "#FFFFFF"
                hover_color "#E34364"
                outlines [ (absolute(1), "#000", 0, 0) ]
                size 45
            action (Function(d19s05_cdd.stop), Jump("d19s05_skip_minigame"), Hide("minigame_screen"))
            xalign 1.0
            if config.developer is True:
                keysym 'K_s'

transform minigame_low_hp():
    alpha 0.2
    block:
        linear 1.0 alpha 0.1
        linear 1.0 alpha 0.3
        repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
