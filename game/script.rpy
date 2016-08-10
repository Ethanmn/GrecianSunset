# config.developer = False, DON'T FORGET BEFORE RELEASING


# Some Python mumbo jumbo to make the game work as wanted

init python:
    #config.side_image_only_not_showing = True
    _game_menu_screen = "game_menu"
    renpy.music.register_channel("ambience", mixer="sfx", loop=True, stop_on_mute=True, tight=False, file_prefix="audio/sfx/Ambience/", file_suffix=".ogg", buffer_queue=True)
    renpy.music.register_channel("sfx", mixer="sfx", loop=False, stop_on_mute=True, tight=False, file_prefix="audio/sfx/", file_suffix=".ogg")
    renpy.music.register_channel("bgm", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="audio/music/", file_suffix=".mp3",buffer_queue=True)
    renpy.music.register_channel("voc", mixer="voice", loop=False, stop_on_mute=True, tight=False, file_prefix="audio/voices/", file_suffix=".ogg")
    # Will this reset the instability every time?
    ins = 0

# The game starts here.
label start:

    # Lets jump right into it!
    call prologue

    return
