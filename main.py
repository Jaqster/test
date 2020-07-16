def on_forever():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
basic.forever(on_forever)
basic.show_number(99)
basic.show_icon(IconNames.HEART)
