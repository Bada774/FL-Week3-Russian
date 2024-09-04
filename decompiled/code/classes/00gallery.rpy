init -2 python:



    class FLGalleryUnlockCondition(object):
        def __init__(self, images):
            self.images = images
        def check(self, all_prior):
            for i in self.images:
                if not renpy.seen_image(i):
                    return False
            return True



    class FLGallery(Gallery, object):
        
        def disjointed_unlock_image(self, image, unlock):
            """
            :doc: gallery method
            Contrary to unlock_image, this method takes two images, one to display and one as condition.
            Useful when the image does not actually exist in the game.
            """
            self.image(image)
            self.unlock(unlock)
        
        def unlock(self, *images):
            self.unlockable.conditions.append(FLGalleryUnlockCondition(images))

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
