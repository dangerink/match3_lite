import traceback
import simplejson
import sys
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from base64 import b64decode
from match3.config import GOOGLE_PUBLIC_KEY, PACKAGE_NAME
from match3.preload import preload


@preload()
def transaction_pay_handler(protocol, entry_point, world, args):
    log = world.logger
    log("\n\ntransaction_pay")
    log(args)

    try:

        args = dict(args)
        google_data = simplejson.loads(args["payload"])

        purchase_data_string = google_data["json"]
        purchase_data = dict(simplejson.loads(purchase_data_string));

        product_id = purchase_data["productId"]

        package_name = purchase_data["packageName"]
        developer_payload = purchase_data["developerPayload"]
        order_id = purchase_data.get("orderId")

        if package_name != PACKAGE_NAME:
            log("wrong_package")
            return '{"result": "!!wrong_package"}'


        if order_id is None:
            log("test_transaction")
            order_id = "test_" + str(purchase_data["purchaseTime"])

        if order_id in world.get_transactions_order_ids(product_id):
            log("!!already_exists")
            return '{"result": "already_exists"}'

        if developer_payload != world.uid:
            log("!!bad_order")
            return '{"result": "bad_order"}'

        valid = validate_purchase(GOOGLE_PUBLIC_KEY,
                                  signedData=purchase_data_string,
                                  signature=google_data["signature"])
        if not valid:
            log("bad_signature")
            return '{"result": "bad_signature"}'

        world.pay_transaction(product_id, {"order_id": order_id,
                               "purchaise_time": purchase_data.get("purchaseTime")})

        log("transaction_pay completed")

        return '{"result": "ok"}'
    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        log(''.join('!!' + line for line in lines))
        return '{"result": "error"}'


def chunks(s, n):
    for start in range(0, len(s), n):
        yield s[start:start + n]


def pem_format(key):
    return '\n'.join([
        '-----BEGIN PUBLIC KEY-----',
        '\n'.join(chunks(key, 64)),
        '-----END PUBLIC KEY-----'
    ])


def validate_purchase(publicKey, signedData, signature):
    key = RSA.importKey(pem_format(publicKey))
    verifier = PKCS1_v1_5.new(key)
    data = SHA.new(signedData)
    sig = b64decode(signature)
    return verifier.verify(data, sig)