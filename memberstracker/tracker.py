import pickle
import collections


Member = collections.namedtuple('Member', ['phone', 'username', 'first_name', 'last_name'])


class Tracker():
    _last_state = None
    _last_state_path = None

    def __init__(self, path):
        self._last_state_path = path

        try:
            self._fetch_last_state()
        except OSError:
            self._set_last_state({})

    @staticmethod
    def _get_members_map(members):
        return {m.id: Member(m.phone, m.username, m.first_name, m.last_name) for m in members}

    def _fetch_last_state(self):
        with open(self._last_state_path, 'rb') as last_state_file:
            self._last_state = pickle.load(last_state_file)

    def _set_last_state(self, members):
        self._last_state = members
        with open(self._last_state_path, 'wb') as last_state_file:
            pickle.dump(members, last_state_file)

    def update(self, members):
        current_members = self._get_members_map(members)

        current_ids = current_members.keys()
        previous_ids = self._last_state.keys()

        added_ids = current_ids - previous_ids
        added_users = [current_members[user_id] for user_id in added_ids]

        removed_ids = previous_ids - current_ids
        removed_users = [self._last_state[user_id] for user_id in removed_ids]

        self._set_last_state(current_members)

        return added_users, removed_users
