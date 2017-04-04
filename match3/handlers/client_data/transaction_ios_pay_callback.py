import traceback
import simplejson
import sys
from match3.btl_result import BtlOk
from match3.config import PACKAGE_NAME
from match3.preload import preload


@preload()
def transaction_ios_pay_callback_handler(protocol, entry_point, world, args):
    logger = world.logger
    logger("\n\ntransaction_ios_pay_callback")

    try:

        logger(args)
        logger(world.context)

        result = itunes_check(world)
        if result:
            world.pay_transaction(result["item"], {"order_id": result["order"],
                                               "purchaise_time": result["datetime"]})

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

        if bundle_id == PACKAGE_NAME and \
                        context.get("order") == transaction_id and \
                        context.get("item") == product_id:
            return dict(datetime=in_app.get("purchase_date"), order=transaction_id, item=product_id)
        else:
            logger("required check failed -> " + "\treceipt fields = " + simplejson.dumps(receipt))
    else:
        logger("iTunes status FAILED!!! -> " + str(world.uid) + " status = " + str(status))