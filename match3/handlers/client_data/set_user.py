from match3.btl_result import BtlOk
from match3.config import PLAYER_SIZE
from match3.preload import preload

MIN_LENGTH = 10


@preload()
def set_user_handler(protocol, entry_point, world, args):
    data = dict(args)["data"]
    length = len(data)
    if  MIN_LENGTH < length < PLAYER_SIZE:
        world.set_player(data)
        return BtlOk('{"result": "ok"}')
    return BtlOk('{"result": "validation_error"}')
