from erlport import Atom
import simplejson


class World(object):

    def __init__(self, uid, logger, player, *args, **kwargs):

        self.uid = uid
        self.logger = logger
        try:
            fields = simplejson.loads(player or "{}") or {}
        except:
            fields = {"player": player}
        fields = fields if isinstance(fields, dict) else {"player": player}
        self.player = fields.get("player", {})
        self.used_transactions = fields.get("used_transactions", {})
        self.unused_transactions = fields.get("unused_transactions", {})
        self.changed = False

    def set_data(self, data):
        p = data.get("player")
        if p is not None: self.player = p

        used = data.get("used_transactions")
        if used is not None:  self.used_transactions = used

        unused = data.get("unused_transactions")
        if unused is not None:
            self.unused_transactions = unused

        self.changed = True

    def set_player(self, data):
        self.player = data
        self.changed = True

    def pay_transaction(self, prodict_id, transaction):
        unused = self.unused_transactions.setdefault(prodict_id, [])
        unused.append(transaction)
        self.changed = True

    def use_transactions(self):
        if self.unused_transactions:
            for item in self.unused_transactions:
                used = self.used_transactions.setdefault(item, [])
                used += self.unused_transactions[item]

            self.unused_transactions = {}
            self.changed = True

    def get_transactions_order_ids(self, product_id):
        return [item.get("order_id") for item in self.used_transactions.get(product_id, {})] + \
               [item.get("order_id") for item in self.unused_transactions.get(product_id, {})]

    @property
    def raw(self):
        result = dict()
        if self.changed and self.player is not None:
            data = {"player": self.player,
                           "used_transactions": self.used_transactions,
                           "unused_transactions": self.unused_transactions}

            d = simplejson.dumps(data)
            result.update({Atom("player"): d})
        return result.items()
