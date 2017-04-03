from match3.preload import preload


@preload()
def get_user_handler(protocol, entry_point, world, data):
    return '{"result":"ok","data":"'+ str(world.player) + '"}'
