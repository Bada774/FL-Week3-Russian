

























init python:

    import requests






    class Lovense():
        solace_patterns = [
            
            [{"ts":0,"pos":0},{"ts":1000,"pos":100},{"ts":1800,"pos":20},{"ts":2600,"pos":80},{"ts":3400,"pos":0}],
            
            [{"ts":0,"pos":0},{"ts":500,"pos":100},{"ts":900,"pos":20},{"ts":1300,"pos":80},{"ts":1600,"pos":0}],
            
            [{"ts":0,"pos":0},{"ts":250,"pos":100},{"ts":500,"pos":20},{"ts":800,"pos":80},{"ts":1050,"pos":0}],
            
            [{"ts":0,"pos":0},{"ts":200,"pos":100},{"ts":400,"pos":20},{"ts":600,"pos":80},{"ts":800,"pos":0}],

            
            [{"ts":0,"pos":100},{"ts":1000,"pos":0},{"ts":1800,"pos":80},{"ts":2600,"pos":20},{"ts":3400,"pos":100}],
            
            [{"ts":0,"pos":100},{"ts":1000,"pos":0},{"ts":1200,"pos":0},{"ts":2000,"pos":80},{"ts":2250,"pos":80},{"ts":3000,"pos":20},{"ts":3300,"pos":20},{"ts":4100,"pos":100}],
            
            [{"ts":0,"pos":100},{"ts":500,"pos":0},{"ts":900,"pos":80},{"ts":1300,"pos":20},{"ts":1700,"pos":100}],
            
            [{"ts":0,"pos":100},{"ts":500,"pos":0},{"ts":650,"pos":0},{"ts":1000,"pos":80},{"ts":1100,"pos":80},{"ts":1500,"pos":20},{"ts":1600,"pos":20},{"ts":2000,"pos":100}],
            
            [{"ts":0,"pos":100},{"ts":250,"pos":0},{"ts":500,"pos":80},{"ts":800,"pos":20},{"ts":1000,"pos":100}],
            
            [{"ts":0,"pos":100},{"ts":250,"pos":0},{"ts":350,"pos":0},{"ts":600,"pos":80},{"ts":700,"pos":80},{"ts":1000,"pos":20},{"ts":1100,"pos":20},{"ts":1300,"pos":100}],
            
            [{"ts":0,"pos":100},{"ts":200,"pos":0},{"ts":400,"pos":80},{"ts":600,"pos":20},{"ts":800,"pos":100}],

            
            [{"ts":0,"pos":0},{"ts":1000,"pos":100},{"ts":2000,"pos":0},{"ts":3000,"pos":100},{"ts":4000,"pos":0}],
            
            [{"ts":0,"pos":0},{"ts":1000,"pos":100},{"ts":1750,"pos":0},{"ts":2500,"pos":100},{"ts":3500,"pos":0}],
            
            [{"ts":0,"pos":0},{"ts":500,"pos":100},{"ts":1000,"pos":0},{"ts":1500,"pos":100},{"ts":2000,"pos":0}],
            
            [{"ts":0,"pos":0},{"ts":500,"pos":100},{"ts":900,"pos":0},{"ts":1300,"pos":100},{"ts":1800,"pos":0}],
            
            [{"ts":0,"pos":0},{"ts":250,"pos":100},{"ts":500,"pos":0},{"ts":750,"pos":100},{"ts":1000,"pos":0}],
            
            [{"ts":0,"pos":0},{"ts":250,"pos":100},{"ts":450,"pos":0},{"ts":650,"pos":100},{"ts":900,"pos":0}],
            
            [{"ts":0,"pos":0},{"ts":200,"pos":100},{"ts":400,"pos":0},{"ts":600,"pos":100},{"ts":800,"pos":0}],

        ]
        
        
        @staticmethod
        def check_connection():
            data = {
                "command": "Function",
                "action": "Vibrate:10",
                "timeSec": 1,
                "stopPrevious": True,
                "apiVer": 1
                }
            
            try:
                response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data, timeout = 5)
                renpy.notify(_("Connection Successful!"))
                persistent.lovense_connected = True
            except Exception:
                renpy.notify(_("Connection failed!"))
                persistent.lovense_connected = False
        
        @staticmethod
        def stop(time=0):
            data = {
                "command": "Function",
                "action": "Stop",
                "timeSec": time,
                "apiVer": 1
                }
            
            if persistent.lovense_connected is True:
                try:
                    response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data, timeout = 5)
                except Exception:
                    renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                    persistent.lovense_connected = False
                    return
            else:
                return
        
        @staticmethod
        def vibrate(strength, time=0, stop_previous=False):
            if not renpy.in_rollback():
                data = {
                    "command": "Function",
                    "action": "Vibrate:{}".format(strength),
                    "timeSec": time,
                    "stopPrevious": int(stop_previous),
                    "apiVer": 1
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data, timeout = 5)
                    except Exception:
                        renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                        persistent.lovense_connected = False
                        return
                else:
                    return
            else:
                data = {
                    "command": "Function",
                    "action": "Vibrate:{}".format(strength),
                    "timeSec": time,
                    "stopPrevious": int(stop_previous),
                    "apiVer": 1
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data, timeout = 5)
                    except Exception:
                        renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                        persistent.lovense_connected = False
                        return
                else:
                    return
        
        @staticmethod
        def vibrot(strpattern="10", interval=1000, time=0, stop_previous=False):
            if not renpy.in_rollback():
                data = {
                    "command": "Pattern",
                    "rule": "V:1;F:vr;S:{}".format(interval),
                    "strength" : strpattern,
                    "timeSec": time,
                    "stopPrevious": int(stop_previous),
                    "apiVer": 1
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data, timeout = 5)
                    except Exception:
                        renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                        persistent.lovense_connected = False
                        return
                else:
                    return
            else:
                data = {
                    "command": "Pattern",
                    "rule": "V:1;F:vr;S:{}".format(interval),
                    "strength" : strpattern,
                    "timeSec": time,
                    "stopPrevious": int(stop_previous),
                    "apiVer": 2
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data, timeout = 5)
                    except Exception:
                        renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                        persistent.lovense_connected = False
                        return
                else:
                    return
        
        @staticmethod
        def pattern(strpattern="5;7;9;7", interval=1000, time=0, stop_previous=True):
            if not renpy.in_rollback():
                data = {
                    "command": "Pattern",
                    "rule": "V:1;F:v,p,r,t,f,s,d;S:{}".format(interval),
                    "strength" : strpattern,
                    "timeSec": time,
                    "stopPrevious": int(stop_previous),
                    "apiVer": 2
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data, timeout = 5)
                    except Exception:
                        renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                        persistent.lovense_connected = False
                        return
                else:
                    return
            else:
                data = {
                    "command": "Pattern",
                    "rule": "V:1;F:v,p,r,t,f,s,d;S:{}".format(interval),
                    "strength" : strpattern,
                    "timeSec": time,
                    "stopPrevious": int(stop_previous),
                    "apiVer": 2
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data, timeout = 5)
                    except Exception:
                        renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                        persistent.lovense_connected = False
                        return
                else:
                    return
        @staticmethod
        def setup_pattern_solace(pattern=0,delay=0):
            if pattern >= len(Lovense.solace_patterns):
                print("pattern index out of bounds")
                return
            if not renpy.in_rollback():
                data = {
                    "command": "PatternV2",
                    "type": "Setup",
                    "actions": Lovense.solace_patterns[pattern],
                    "apiVer": 1
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data, timeout = 5)
                        Lovense.play_pattern_solace(delay)
                    except Exception:
                        renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                        persistent.lovense_connected = False
                        return
                else:
                    return
            else:
                data = {
                    "command": "PatternV2",
                    "type": "Setup",
                    "actions": Lovense.solace_patterns[pattern],
                    "apiVer": 1
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data, timeout = 5)
                        Lovense.play_pattern_solace(delay)
                    except Exception:
                        renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                        persistent.lovense_connected = False
                        return
                else:
                    return
        
        
        @staticmethod
        def play_pattern_solace(delay=0):
            
            data = {
                "command": "PatternV2",
                "type": "Play",
                "startTime": delay,
                "apiVer": 1
            }
            
            if persistent.lovense_connected is True:
                try:
                    response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data, timeout = 5)
                    print("solace play sent")
                except Exception:
                    renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                    persistent.lovense_connected = False
                    return
            else:
                return
        
        @staticmethod
        def stop_pattern_solace():
            
            data = {
                "command": "PatternV2",
                "type": "Stop",
                "apiVer": 1
            }
            
            if persistent.lovense_connected is True:
                try:
                    response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data, timeout = 5)
                except Exception:
                    renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                    persistent.lovense_connected = False
                    return
            else:
                return
        
        @staticmethod
        def fadevib(strength, time=2, stop_previous=True):
            if not renpy.in_rollback():
                interval=time*1000/strength
                strpattern=""
                while strength>=0:
                    if strength>0:
                        strpattern+=str(strength)+";"
                    else:
                        strpattern+=str(strength)
                        continue
                    strength-1
                data = {
                    "command": "Pattern",
                    "rule": "V:1;F:vpr;S:{}".format(interval),
                    "strength" : strpattern,
                    "timeSec": time,
                    "stopPrevious": int(stop_previous),
                    "apiVer": 2
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data, timeout = 5)
                    except Exception:
                        renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                        persistent.lovense_connected = False
                        return
                else:
                    return
            else:
                interval=time*1000/strength
                strpattern=""
                while strength>=0:
                    if strength>0:
                        strpattern+=str(strength)+";"
                    else:
                        strpattern+=str(strength)
                        continue
                    strength-1
                data = {
                    "command": "Pattern",
                    "rule": "V:1;F:vpr;S:{}".format(interval),
                    "strength" : strpattern,
                    "timeSec": time,
                    "stopPrevious": int(stop_previous),
                    "apiVer": 2
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data, timeout = 5)
                    except Exception:
                        renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                        persistent.lovense_connected = False
                        return
                else:
                    return
        
        @staticmethod
        def rotate(strength, time=0, stop_previous=False):
            if not renpy.in_rollback():
                data = {
                    "command": "Function",
                    "action": "Rotate:{}".format(strength),
                    "timeSec": time,
                    "stopPrevious": int(stop_previous),
                    "apiVer": 1
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data, timeout = 5)
                    except Exception:
                        renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                        persistent.lovense_connected = False
                        return
                else:
                    return
            else:
                data = {
                    "command": "Function",
                    "action": "Rotate:{}".format(strength),
                    "timeSec": time,
                    "stopPrevious": int(stop_previous),
                    "apiVer": 1
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data, timeout = 5)
                    except Exception:
                        renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                        persistent.lovense_connected = False
                        return
                else:
                    return
        
        @staticmethod
        def pump(strength, time=0, stop_previous=False):
            if not renpy.in_rollback():
                data = {
                    "command": "Function",
                    "action": "Pump:{}".format(strength),
                    "timeSec": time,
                    "stopPrevious": int(stop_previous),
                    "apiVer": 1
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data, timeout = 5)
                    except Exception:
                        renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                        persistent.lovense_connected = False
                        return
                else:
                    return
            else:
                data = {
                    "command": "Function",
                    "action": "Pump:{}".format(strength),
                    "timeSec": time,
                    "stopPrevious": int(stop_previous),
                    "apiVer": 1
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data, timeout = 5)
                    except Exception:
                        renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                        persistent.lovense_connected = False
                        return
                else:
                    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
