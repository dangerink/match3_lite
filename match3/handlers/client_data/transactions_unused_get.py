import simplejson

from match3.btl_result import BtlOk
from match3.preload import preload


@preload()
def transactions_unused_get_handler(protocol, entry_point, world, data):
    return BtlOk(simplejson.dumps({"result": "ok",
                                   "unused_transactions": world.unused_transactions,
                                   "used_transactions_count": len(world.used_transactions),
                                   "last_transaction_ts": world.get_last_transaction()}))
