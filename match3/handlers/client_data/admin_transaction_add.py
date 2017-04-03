import traceback

import sys
from match3.preload import preload


@preload()
def admin_transaction_add_handler(protocol, entry_point, world, args):
    log = world.logger
    log("admin_transaction_add")
    log(str(args))
    args = dict(args)

    if entry_point != "admin":
        return '{"result": "error_auth"}'
    try:
        world.pay_transaction(args["product_id"], {"order_id": args["order_id"],
                               "purchase_time": args["purchase_time"]})

        log("admin_transaction_add completed")
        return '{"result": "ok"}'
    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        log(''.join('!! ' + line for line in lines))
        return '{"result": "error"}'




