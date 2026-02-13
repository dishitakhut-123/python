from collections import defaultdict

def process_user_activities(records):
    users = set()
    activity_count = defaultdict(int)
    user_acts = defaultdict(set)
    totals = defaultdict(int)

    for _, user, acts in records:
        users.add(user)
        totals[user] += len(acts)
        for a in acts:
            activity_count[a] += 1
            user_acts[user].add(a)

    return {
        "unique_users": users,
        "activity_count": dict(activity_count),
        "user_activity_map": {u: sorted(a) for u, a in user_acts.items()},
        "most_active_user": min(
            (u for u in totals if totals[u] == max(totals.values()))
        )
    }
