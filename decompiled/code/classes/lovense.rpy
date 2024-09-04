

























init python:

    import requests






    class Lovense():
        
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
                response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data)
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
                    response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data)
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
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data)
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
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data)
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
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data)
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
                    "apiVer": 1
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data)
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
                    "rule": "V:1;F:vpr;S:{}".format(interval),
                    "strength" : strpattern,
                    "timeSec": time,
                    "stopPrevious": int(stop_previous),
                    "apiVer": 1
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data)
                    except Exception:
                        renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                        persistent.lovense_connected = False
                        return
                else:
                    return
            else:
                data = {
                    "command": "Pattern",
                    "rule": "V:1;F:vpr;S:{}".format(interval),
                    "strength" : strpattern,
                    "timeSec": time,
                    "stopPrevious": int(stop_previous),
                    "apiVer": 1
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data)
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
                    "apiVer": 1
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data)
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
                    "apiVer": 1
                    }
                
                if persistent.lovense_connected is True:
                    try:
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data)
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
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data)
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
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data)
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
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data)
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
                        response = requests.post("http://{}:{}/command".format(persistent.lovense_ip, persistent.lovense_port), json = data)
                    except Exception:
                        renpy.notify(_("Connection with the Lovense toy failed! Please visit the Preference page to reconfigure."))
                        persistent.lovense_connected = False
                        return
                else:
                    return

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
