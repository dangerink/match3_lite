import simplejson

from match3.btl_result import BtlOk
from match3.preload import preload


@preload()
def transactions_used_get_handler(protocol, entry_point, world, data):
    return BtlOk(simplejson.dumps({"result": "ok","used_transactions": world.used_transactions}))
