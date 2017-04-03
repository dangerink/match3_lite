import hashlib

import simplejson

from match3.config import PLAYER_SIZE
from match3.preload import preload


@preload()
def admin_set_handler(protocol, entry_point, world, args):
    if entry_point != "admin":
        return '{"result": "error"}'
    data = simplejson.loads(dict(args)["data"])
    world.set_data(data)
    return '{"result": "ok"}'
