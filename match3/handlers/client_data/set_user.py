import hashlib

from match3.btl_result import BtlOk
from match3.config import PLAYER_SIZE
from match3.preload import preload


@preload()
def set_user_handler(protocol, entry_point, world, args):
    data = dict(args)["data"]
    if len(data) < PLAYER_SIZE:
        world.set_player(data)
        return BtlOk('{"result": "ok"}')
    return BtlOk('{"result": "validation_error"}')
