init python:

    comics_gallery_slots = [
        ("comic_01",    _("Lyssa-Allison Comic Chapter - 1"),   _(""),  None),
        ("comic_02",    _("Lyssa-Allison Comic Chapter - 2"),   _(""),  None),
        ("comic_03",    _("Lyssa-Allison Comic Chapter - 3"),   _(""),  None),
        ("comic_04",    _("Lyssa-Allison Comic Chapter - 4"),   _(""),  None),
        ("comic_05",    _("Lyssa-Allison Comic Chapter - 5"),   _(""),  None),
        ("comic_06",    _("Lyssa-Allison Comic Chapter - 6"),   _(""),  None),
        ("comic_07",    _("Lyssa-Allison Comic Chapter - 7"),   _(""),  None),
        ("comic_08",    _("Lyssa-Allison Comic Chapter - 8"),   _(""),  None),
        ("comic_09",    _("Lyssa-Allison Comic Chapter - 9"),   _(""),  None),
    ]

    comics_gallery = FLGallery()
    comics_gallery.transition = dissolve
    comics_gallery.navigation = True
    comics_gallery.locked_button = "gallery_locked_button"
    comics_gallery.image_screen = "_comic_gallery"


    comics_gallery.button("comic_01")
    comics_gallery.image(
        "comics_chapter_01_page_01", "comics_chapter_01_page_02", "comics_chapter_01_page_03",
        "comics_chapter_01_page_04", "comics_chapter_01_page_05", "comics_chapter_01_page_06",
        "comics_chapter_01_page_07", "comics_chapter_01_page_08", "comics_chapter_01_page_09",
    )

    comics_gallery.button("comic_02")
    comics_gallery.image(
        "comics_chapter_02_page_01", "comics_chapter_02_page_02", "comics_chapter_02_page_03",
        "comics_chapter_02_page_04", "comics_chapter_02_page_05", "comics_chapter_02_page_06",
        "comics_chapter_02_page_07", "comics_chapter_02_page_08", "comics_chapter_02_page_09",
        "comics_chapter_02_page_10", "comics_chapter_02_page_11",
    )

    comics_gallery.button("comic_03")
    comics_gallery.image(
        "comics_chapter_03_page_01", "comics_chapter_03_page_02", "comics_chapter_03_page_03",
        "comics_chapter_03_page_04", "comics_chapter_03_page_05", "comics_chapter_03_page_06",
        "comics_chapter_03_page_07", "comics_chapter_03_page_08",
    )

    comics_gallery.button("comic_04")
    comics_gallery.image(
        "comics_chapter_04_page_01", "comics_chapter_04_page_02", "comics_chapter_04_page_03",
        "comics_chapter_04_page_04", "comics_chapter_04_page_05", "comics_chapter_04_page_06",
        "comics_chapter_04_page_07",
    )

    comics_gallery.button("comic_05")
    comics_gallery.image(
        "comics_chapter_05_page_01", "comics_chapter_05_page_02", "comics_chapter_05_page_03",
        "comics_chapter_05_page_04", "comics_chapter_05_page_05", "comics_chapter_05_page_06",
        "comics_chapter_05_page_07", "comics_chapter_05_page_08",
    )

    comics_gallery.button("comic_06")
    comics_gallery.image(
        "comics_chapter_06_page_01", "comics_chapter_06_page_02", "comics_chapter_06_page_03",
        "comics_chapter_06_page_04", "comics_chapter_06_page_05", "comics_chapter_06_page_06",
        "comics_chapter_06_page_07",
    )

    comics_gallery.button("comic_07")
    comics_gallery.image(
        "comics_chapter_07_page_01", "comics_chapter_07_page_02", "comics_chapter_07_page_03",
        "comics_chapter_07_page_04", "comics_chapter_07_page_05", "comics_chapter_07_page_06",
        "comics_chapter_07_page_07", "comics_chapter_07_page_08", "comics_chapter_07_page_09",
    )

    comics_gallery.button("comic_08")
    comics_gallery.image(
        "comics_chapter_08_page_01", "comics_chapter_08_page_02", "comics_chapter_08_page_03",
        "comics_chapter_08_page_04", "comics_chapter_08_page_05", "comics_chapter_08_page_06",
        "comics_chapter_08_page_07", "comics_chapter_08_page_08",
    )

    comics_gallery.button("comic_09")
    comics_gallery.image(
        "comics_chapter_09_page_01", "comics_chapter_09_page_02", "comics_chapter_09_page_03",
        "comics_chapter_09_page_04", "comics_chapter_09_page_05", "comics_chapter_09_page_06",
        "comics_chapter_09_page_07", "comics_chapter_09_page_08", "comics_chapter_09_page_09",
        "comics_chapter_09_page_10",
    )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
