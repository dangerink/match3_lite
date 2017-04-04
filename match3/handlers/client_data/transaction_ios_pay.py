import traceback
import simplejson
import sys
from erlport import Atom
from match3.btl_result import BtlOk, BtlRequest
from match3.config import ITUNES_URL
from match3.preload import preload


@preload()
def transaction_ios_pay_handler(protocol, entry_point, world, args):
    log = world.logger
    log("\n\ntransaction_ios_pay")
    log(args)

    try:
        args = dict(args)
        payload = args["payload"]
        product_id = args["item"]
        order_id = args["order"]

        if order_id in world.get_transactions_order_ids(product_id):
            log("!!already_exists")
            return BtlOk('{"result": "already_exists"}')
        fields = ["player"]

        body = simplejson.dumps({"receipt-data": payload})
        request = (ITUNES_URL, [(Atom("method"), Atom("post")), (Atom("body"), body)])
        fields.append(("http", request))

        return  BtlRequest("transaction_ios_pay_callback", fields, simplejson.dumps(args))

    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        log(''.join('!!' + line for line in lines))
        return BtlOk('{"result": "error"}')