music.play(music.builtin_playable_sound_effect(soundExpression.yawn),
    music.PlaybackMode.IN_BACKGROUND)
basic.show_leds("""
    . . . . .
    # # # # #
    . . . . .
    . # # # .
    . . . . .
    """)
basic.show_icon(IconNames.SURPRISED)
basic.show_leds("""
    . . . . .
    # # . # #
    . # # # .
    # . . . #
    . # # # .
    """)
music.play(music.builtin_playable_sound_effect(soundExpression.hello),
    music.PlaybackMode.IN_BACKGROUND)

def on_forever():
    basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever)
