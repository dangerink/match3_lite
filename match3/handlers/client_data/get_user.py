from match3.btl_result import BtlOk
from match3.preload import preload


@preload()
def get_user_handler(protocol, entry_point, world, data):
    return BtlOk('{"result":"ok","data":"'+ str(world.player) + '"}')
