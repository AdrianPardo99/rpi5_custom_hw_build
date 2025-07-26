import os


def get_extra_message():
    lcd_extra_message = os.environ.get("LCD_EXTRA_MESSAGE", "")
    return lcd_extra_message


def split_text_into_part(source, size=22):
    return [source[i : i + size] for i in range(0, len(source), size)]


def group_list_by_default_sizes(list_source, group_by=4):
    groups = []
    for i in range(0, len(list_source), group_by):
        group = list_source[i : i + group_by]
        if group:
            groups.append(group)
    return groups
