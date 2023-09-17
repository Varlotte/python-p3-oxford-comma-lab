def oxford_comma(items):
    if len(items) >= 3:
        comma_items = items[0:-1]
        return ', '.join(comma_items) + ', and ' + items[-1]
    elif len(items) == 2:
        return ' and '.join(items)
    else:
        return items[0]
