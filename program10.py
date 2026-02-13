from collections import defaultdict

def get_unique_users(records):
    return {user for _, user, _ in records}


def get_activity_count(records):
    activity_count = defaultdict(int)
    for _, _, activities in records:
        for activity in activities:
            activity_count[activity] += 1
    return dict(activity_count)


def get_user_activity_map(records):
    user_activities = defaultdict(set)
    for _, user, activities in records:
        user_activities[user].update(activities)
    return {user: sorted(acts) for user, acts in user_activities.items()}


def get_most_active_user(records):
    activity_totals = defaultdict(int)
    for _, user, activities in records:
        activity_totals[user] += len(activities)

    max_count = max(activity_totals.values())
    return min(user for user, count in activity_totals.items() if count == max_count)


def process_user_activities(records):
    return {
        "unique_users": get_unique_users(records),
        "activity_count": get_activity_count(records),
        "user_activity_map": get_user_activity_map(records),
        "most_active_user": get_most_active_user(records),
    }


# -------------------- RUN THE CODE --------------------

if __name__ == "__main__":
    records = [
        (1, "alice", ["login", "view", "logout"]),
        (2, "bob", ["login", "view"]),
        (3, "alice", ["login", "purchase"]),
        (4, "david", ["login", "view", "purchase", "logout"]),
    ]

    result = process_user_activities(records)
    print(result)
