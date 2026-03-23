music.play(music.builtinPlayableSoundEffect(soundExpression.yawn), music.PlaybackMode.InBackground)
basic.showLeds(`
    . . . . .
    # # # # #
    . . . . .
    . # # # .
    . . . . .
    `)
basic.showIcon(IconNames.Surprised)
basic.showLeds(`
    . . . . .
    # # . # #
    . # # # .
    # . . . #
    . # # # .
    `)
music.play(music.builtinPlayableSoundEffect(soundExpression.hello), music.PlaybackMode.InBackground)
basic.forever(function () {
    basic.showIcon(IconNames.Happy)
})
