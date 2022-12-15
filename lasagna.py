"""declare expected bake time"""
EXPECTED_BAKE_TIME = 40
"""declare preparation time"""
PREPARATION_TIME = 2

def bake_time_remaining(time_elapsed):
    """returns the bake time remaining by subtracting
    the value entered on the time_elapsed parameter
    from the EXPECTED_BAKE_TIME constant"""
    return EXPECTED_BAKE_TIME - time_elapsed
    

def preparation_time_in_minutes(number_of_layers):
    """returns the preparation time by multiplying
    the value entered on the number_of_layers parameter
    by the PREPARATION_TIME constant"""
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """returns the elapsed time by adding
    the value recipe duration time to the
    value entered on the elapsed_bake_time parameter"""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time