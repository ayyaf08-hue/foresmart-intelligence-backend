def normalize_value(value, min_v=0, max_v=1):
    return max(min_v, min(max_v, value))
