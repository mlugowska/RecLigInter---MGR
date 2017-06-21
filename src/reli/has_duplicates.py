def has_duplicates(interactions_in_time):
    return len(interactions_in_time) != len(set(interactions_in_time.values()))

