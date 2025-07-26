import os


def get_extra_message():
    lcd_extra_message = os.environ.get("LCD_EXTRA_MESSAGE", "")
    return lcd_extra_message
