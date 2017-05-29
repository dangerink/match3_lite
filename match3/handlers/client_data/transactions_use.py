from match3.btl_result import BtlOk
from match3.preload import preload


@preload()
def transactions_use_handler(protocol, entry_point, world, args):
    log = world.logger
    world.use_transactions(log)
    return BtlOk('{"result": "ok"}')