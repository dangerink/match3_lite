import traceback
from datetime import datetime
from time import time
import simplejson
import sys
from match3.btl_result import BtlOk
from match3.config import ITUNES_NO_CHECK, IOS_BUNDLE_ID
from match3.preload import preload


@preload()
def transaction_ios_pay_callback_handler(protocol, entry_point, world, args):
    logger = world.logger
    logger("\n\ntransaction_ios_pay_callback")
    now = str(int(time()))

    try:
        logger(args)
        logger(world.context)

        if ITUNES_NO_CHECK:
            context = simplejson.loads(world.context)
            result = dict(order="skip_check_{}".format(context.get("order")),
                          item=context.get("item"))
        else:
            result = itunes_check(world)

        if result:
            world.pay_transaction(result["item"], {"order_id": result["order"],
                                                   "purchaise_time": now})

            logger("transaction_ios_pay completed")

            return BtlOk('{"result": "ok"}')

        return BtlOk('{"result": "error"}')
    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        logger(''.join('!!' + line for line in lines))
        return BtlOk('{"result": "error"}')



def itunes_check(world):
    player, http, context, logger = world.player, world.http, simplejson.loads(world.context), world.logger
    reply = simplejson.loads(http or "{}")
    status = reply.get("status")
    receipt = reply.get("receipt")

    if status == 0:
        in_app = receipt.get("in_app")[0]
        bundle_id = receipt.get("bundle_id")
        transaction_id = in_app.get("transaction_id")
        product_id = in_app.get("product_id")
        bundle_id_check = bundle_id == IOS_BUNDLE_ID
        order_check = context.get("order") == transaction_id
        item_check = context.get("item") == product_id

        if bundle_id_check and order_check and item_check:
            return dict(order=transaction_id, item=product_id)
        else:
            logger("required check failed -> " + "\treceipt fields = " + simplejson.dumps(receipt))

    else:
        logger("iTunes status FAILED!!! -> " + str(world.uid) + " status = " + str(status))