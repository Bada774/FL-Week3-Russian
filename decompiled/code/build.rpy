




init 1 python:




















    build.classify("**~"                      , None)
    build.classify("**.bak"                   , None)
    build.classify("**.bat"                   , None)
    build.classify("**.rar"                   , None)
    build.classify("**/.**"                   , None)
    build.classify("**/#**"                   , None)
    build.classify("**/thumbs.db"             , None)
    build.classify("**/desktop.ini"           , None)
    build.classify("**.txt"                   , None)
    build.classify("**.json"                  , None)
    build.classify("**.zip"                   , None)
    build.classify("**.psd"                   , None)


    build.classify("game/code/debug.rpy"      , None)
    build.classify("game/code/debug.rpyc"     , None)
    build.classify("game/code/config.rpy"     , None)
    build.classify("game/code/config.rpyc"    , None)


    build.classify("game/**.rpy"              , None)
    build.classify("game/cache/*.rpyb"        , None)


    build.classify("game/**.py"               , None)
    build.classify("game/**.pyc"              , None)


    build.classify("game/saves/persistent"    , None)
    build.classify("game/saves/*.save"        , None)


    build.classify("game/**.md"               , None)
    build.classify("game/tl/media/**"         , None)


    build.classify("game/audio/**/orig/**"    , None)
    build.classify("game/audio/**/wav/**"     , None)
    build.classify("game/audio/**/test/**"    , None)
    build.classify("game/audio/**/unused/**"  , None)





    if not is_extended_edition:
        build.classify("game/**/extended/**"  , None)


    build.archive("scripts"                   , "all")
    if only_build_code is False:
        build.archive("images"                    , "all")
        build.archive("audio"                     , "all")
        build.archive("video"                     , "all")
        build.archive("fonts"                     , "all")
        
        
        build.archive("others"                    , "all")
        build.archive("gui"                       , "all")
        
        
        build.archive("walkthrough_dlc"           , "all")
        build.archive("dlc_1_data"                , "all")
        build.archive("dlc_2_data"                , "all")
        
        
        if is_DLC_1_included is True:
            build.classify("game/images/extended/dlc-1-bonus/**" , "dlc_1_data")
        else:
            build.classify("game/images/extended/dlc-1-bonus/**" , None)
        if is_DLC_2_included is True:
            build.classify("game/images/extended/bonus-DLC-2/**" , "dlc_2_data")
        else:
            build.classify("game/images/extended/bonus-DLC-2/**" , None)
        
        build.classify("game/images/extended/**"  , "others")
        build.classify("game/images/utility/**"   , "others")
        build.classify("game/gui/**"              , "gui")
        
        
        if is_Walkthrough_DLC_included is True:
            build.classify("game/**/hints.rpyc"   , "walkthrough_dlc")
        else:
            build.classify("game/code/hints.rpyc"   , None)
        
        if is_DLC_1_included is True:
            
            build.classify("game/images/E-04/**"  , "dlc_1_data")
            build.classify("game/code/e04/**"     , "dlc_1_data")
            
            build.classify("game/images/E-07/**"  , "dlc_1_data")
            build.classify("game/code/e07/**"     , "dlc_1_data")
            
            build.classify("game/images/E-11/**"  , "dlc_1_data")
            build.classify("game/code/e11/**"       , "dlc_1_data")
            
            build.classify("game/images/E-12/**"  , "dlc_1_data")
            build.classify("game/code/e12/**"       , "dlc_1_data")
            
            build.classify("game/images/E-14/**"  , "dlc_1_data")
            build.classify("game/code/e14/**"       , "dlc_1_data")
            
            build.classify("game/images/E-17/**"  , "dlc_1_data")
            build.classify("game/code/e17/**"       , "dlc_1_data")
        else:
            build.classify("game/images/E-04/**"  , None)
            build.classify("game/code/e04/**"     , None)
            
            build.classify("game/images/E-07/**"  , None)
            build.classify("game/code/e07/**"     , None)
            
            build.classify("game/images/E-11/**"  , None)
            build.classify("game/code/e11/**"     , None)
            
            build.classify("game/images/E-12/**"  , None)
            build.classify("game/code/e12/**"     , None)
            
            build.classify("game/images/E-14/**"  , None)
            build.classify("game/code/e14/**"     , None)
            
            build.classify("game/images/E-17/**"  , None)
            build.classify("game/code/e17/**"     , None)
        
        if is_DLC_2_included is True:
            build.classify("game/images/E-03/**"  , "dlc_2_data")
            build.classify("game/code/e03/**"     , "dlc_2_data")
            
            build.classify("game/images/E-05/**"  , "dlc_2_data")
            build.classify("game/code/e05/**"     , "dlc_2_data")
            
            build.classify("game/images/E-09/**"  , "dlc_2_data")
            build.classify("game/code/e09/**"     , "dlc_2_data")
            
            build.classify("game/images/E-15/**"  , "dlc_2_data")
            build.classify("game/code/e15/**"     , "dlc_2_data")
            
            build.classify("game/images/E-16/**"  , "dlc_2_data")
            build.classify("game/code/e16/**"     , "dlc_2_data")
            
            build.classify("game/images/E-18/**"  , "dlc_2_data")
            build.classify("game/code/e18/**"     , "dlc_2_data")
        else:
            build.classify("game/images/E-03/**"  , None)
            build.classify("game/code/e03/**"     , None)
            
            build.classify("game/images/E-05/**"  , None)
            build.classify("game/code/e05/**"     , None)
            
            build.classify("game/images/E-09/**"  , None)
            build.classify("game/code/e09/**"     , None)
            
            build.classify("game/images/E-15/**"  , None)
            build.classify("game/code/e15/**"     , None)
            
            build.classify("game/images/E-16/**"  , None)
            build.classify("game/code/e16/**"     , None)
            
            build.classify("game/images/E-18/**"  , None)
            build.classify("game/code/e18/**"     , None)

    if only_build_code is True:
        build.classify("game/**/hints.rpyc"   , None)
        build.classify("game/code/e04/**"     , None)
        build.classify("game/code/e07/**"     , None)
        build.classify("game/code/e11/**"     , None)
        build.classify("game/code/e12/**"     , None)
        build.classify("game/code/e14/**"     , None)
        build.classify("game/code/e17/**"     , None)
        build.classify("game/code/e05/**"     , None)
        build.classify("game/code/e15/**"     , None)
        build.classify("game/code/e16/**"     , None)
        build.classify("game/code/e18/**"     , None)


    build.classify("game/**.rpyc"             , "scripts")

    if only_build_code is False:
        
        build.classify("game/**.webp"             , "images")
        build.classify("game/**.png"              , "images")
        build.classify("game/**.jpg"              , "images")
        
        
        build.classify("game/**.ogg"              , "audio")
        build.classify("game/**.mp3"              , "audio")
        build.classify("game/**.wav"              , "audio")
        
        
        build.classify("game/**.mp4"              , "video")
        build.classify("game/**.avi"              , "video")
        build.classify("game/**.webm"             , "video")
        
        
        build.classify("game/**.ttf"              , "fonts")
        build.classify("game/**.otf"              , "fonts")
    else:
        
        build.classify("game/**.webp"             , None)
        build.classify("game/**.png"              , None)
        build.classify("game/**.jpg"              , None)
        
        
        build.classify("game/**.ogg"              , None)
        build.classify("game/**.mp3"              , None)
        build.classify("game/**.wav"              , None)
        
        
        build.classify("game/**.mp4"              , None)
        build.classify("game/**.avi"              , None)
        build.classify("game/**.webm"             , None)
        
        
        build.classify("game/**.ttf"              , None)
        build.classify("game/**.otf"              , None)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
