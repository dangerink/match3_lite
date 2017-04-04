from match3.btl_result import BtlOk
from match3.preload import preload


@preload()
def transactions_use_handler(protocol, entry_point, world, args):
    log = world.logger
    log("transaction_use")
    log(str(args))
    world.use_transactions()
    log("transaction_use completed")
    return BtlOk('{"result": "ok"}')