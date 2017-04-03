import simplejson

from match3.preload import preload


@preload()
def transactions_unused_get_handler(protocol, entry_point, world, data):
    return simplejson.dumps({"result": "ok","unused_transactions": world.unused_transactions})
