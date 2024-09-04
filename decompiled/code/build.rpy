




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


    build.classify("game/images/E-03/**"      , None)
    build.classify("game/code/e03/**"         , None)

    build.classify("game/images/E-05/**"      , None)
    build.classify("game/code/e05/**"         , None)

    build.classify("game/images/E-09/**"      , None)
    build.classify("game/code/e09/**"         , None)

    build.classify("game/images/E-15/**"      , None)
    build.classify("game/code/e15/**"         , None)

    build.classify("game/images/E-16/**"      , None)
    build.classify("game/code/e16/**"         , None)

    build.classify("game/images/E-18/**"      , None)
    build.classify("game/code/e18/**"         , None)


    if not is_extended_edition:
        build.classify("game/**/extended/**"  , None)


    build.archive("scripts"                   , "all")
    build.archive("images"                    , "all")
    build.archive("audio"                     , "all")
    build.archive("video"                     , "all")
    build.archive("fonts"                     , "all")


    build.archive("others"                    , "all")
    build.archive("gui"                       , "all")
    build.archive("dlc_1_bonus"               , "all")


    if is_DLC_1_included is True:
        build.classify("game/images/extended/dlc-1-bonus/**" , "dlc_1_bonus")
    else:
        build.classify("game/images/extended/dlc-1-bonus/**" , None)

    build.classify("game/images/extended/**"  , "others")
    build.classify("game/images/utility/**"   , "others")
    build.classify("game/gui/**"              , "gui")


    build.archive("walkthrough_dlc"           , "all")
    build.archive("ending_04_dlc"             , "all")
    build.archive("ending_07_dlc"             , "all")
    build.archive("ending_11_dlc"             , "all")
    build.archive("ending_12_dlc"             , "all")
    build.archive("ending_14_dlc"             , "all")
    build.archive("ending_17_dlc"             , "all")


    if is_Walkthrough_DLC_included is True:
        build.classify("game/**/hints.rpyc"   , "walkthrough_dlc")
    else:
        build.classify("game/**/hints.rpyc"   , None)

    if is_DLC_1_included is True:
        
        build.classify("game/images/E-04/**"  , "ending_04_dlc")
        build.classify("game/code/e04/**"     , "ending_04_dlc")
        
        build.classify("game/images/E-07/**"  , "ending_07_dlc")
        build.classify("game/code/e07/**"     , "ending_07_dlc")
        
        build.classify("game/images/E-11/**"  , "ending_11_dlc")
        build.classify("game/**/e11/**"       , "ending_11_dlc")
        
        build.classify("game/images/E-12/**"  , "ending_12_dlc")
        build.classify("game/**/e12/**"       , "ending_12_dlc")
        
        build.classify("game/images/E-14/**"  , "ending_14_dlc")
        build.classify("game/**/e14/**"       , "ending_14_dlc")
        
        build.classify("game/images/E-17/**"  , "ending_17_dlc")
        build.classify("game/**/e17/**"       , "ending_17_dlc")
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


    build.classify("game/**.rpyc"             , "scripts")


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

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
