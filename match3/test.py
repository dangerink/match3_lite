import simplejson
from erlport import Atom

from match3.handlers.client_data.admin_set import admin_set_handler
from match3.handlers.client_data.admin_transaction_add import admin_transaction_add_handler
from match3.handlers.client_data.get_user import get_user_handler

from match3.handlers.client_data.set_user import set_user_handler
from match3.handlers.client_data.transaction_ios_pay import transaction_ios_pay_handler
from match3.handlers.client_data.transaction_ios_pay_callback import transaction_ios_pay_callback_handler
from match3.handlers.client_data.transaction_pay import transaction_pay_handler
from match3.handlers.client_data.transactions_unused_get import transactions_unused_get_handler
from match3.handlers.client_data.transactions_use import transactions_use_handler

protocol = None
entry_point = "main"
uid = 'e6f22045d9544675971b7f32950b7c07'
context = simplejson.dumps({"order": '700000172785742', "item": "crystals_30"})
values = [(Atom("player"), '{"player":"ddd", "unused_transactions": ["trans123456"]}')]
values = [
    (Atom("http"), simplejson.dumps({"status":0, "environment":"Production",
"receipt":{"receipt_type":"Production", "adam_id":1042276818, "app_item_id":1042276818, "bundle_id":"ru.kefirgames", "application_version":"4", "download_id":110016094761650, "version_external_identifier":818841974, "receipt_creation_date":"2017-04-02 22:50:18 Etc/GMT", "receipt_creation_date_ms":"1491173418000", "receipt_creation_date_pst":"2017-04-02 15:50:18 America/Los_Angeles", "request_date":"2017-04-02 22:50:21 Etc/GMT", "request_date_ms":"1491173421689", "request_date_pst":"2017-04-02 15:50:21 America/Los_Angeles", "original_purchase_date":"2017-03-10 21:53:07 Etc/GMT", "original_purchase_date_ms":"1489182787000", "original_purchase_date_pst":"2017-03-10 13:53:07 America/Los_Angeles", "original_application_version":"4",
"in_app":[
{"quantity":"1", "product_id":"crystals_30", "transaction_id":"700000172785742", "original_transaction_id":"700000172785742", "purchase_date":"2017-04-02 22:50:18 Etc/GMT", "purchase_date_ms":"1491173418000", "purchase_date_pst":"2017-04-02 15:50:18 America/Los_Angeles", "original_purchase_date":"2017-04-02 22:50:18 Etc/GMT", "original_purchase_date_ms":"1491173418000", "original_purchase_date_pst":"2017-04-02 15:50:18 America/Los_Angeles", "is_trial_period":"false"}]}})
           ),
    (Atom("player"), simplejson.dumps({"player":"ddd", "unused_transactions": {"r_starter_pack_10": [{"order_id": "GPA.1387-2118-8871-37321", "purchaise_time": 1484925738969}]}}))]
get_args = {"item":"r_starter_pack_1",
            "order":"GPA.1387-2118-8871-37321",
            "payload":'{"json":"{\\"orderId\\":\\"GPA.1387-2118-8871-37321\\",\\"packageName\\":\\"ru.kefirgames\\",\\"productId\\":\\"r_starter_pack_1\\",\\"purchaseTime\\":1484925738969,\\"purchaseState\\":0,\\"developerPayload\\":\\"e6f22045d9544675971b7f32950b7c07\\",\\"purchaseToken\\":\\"ekbimahedplagnenlimajefm.AO-J1OwTLt42GUuocUJOzMDLAekRl03LjfEPzKSE8YJnTVcGlI15vf8oR5gHmq_KaJSdBHRGqiVu4sqfhJzEjCleT9EV3x_1A6SDxr4uL1pny8xU0kKN_YCZSh885zMsYPdVI4D_u-gd\\"}","signature":"PdvdML2C3CCxh7R5NS92GRiIQ2aaUCMm4kumEZ0kyCW8OhFBfy5F0m9kdJP+IxCY7KfwgIotm5Dt3p\/IAwIyBE8AVDVrrgxpFSZS3xII3onC4chI50A4AROcOm5d0L1LU7sMtuWn6PUgdksZfLGJ0RSSplHm\/hLv+kmc\/9w\/cB0CIlug9uf18Wy++wjjEG+gsL0p+U89DC1LjNh\/Ca8gVSAxTm9XmktPSZFXk6xINpHHTJgGQTiKUj4VV8hbPsHO0wQKFuyQ33ViobJZGODKIIb7NP3pDjPyCtKTJDqlqWYADsjlAQUhd4LwXdHmzxr9nJQA2CKQdhuKtDCay\/BjlA=="}',
            "product_id": "p", "order_id": "o","purchase_time": "t",
            "data":'{"used_transactions": "ololo"}'}



print get_user_handler(protocol, entry_point, context, uid, values, get_args), "\n"
print set_user_handler(protocol, entry_point, context, uid, values, get_args), "\n"
print transaction_pay_handler(protocol, entry_point, context, uid, values, get_args), "\n"
print transactions_use_handler(protocol, entry_point, context, uid, values, get_args), "\n"
print transactions_unused_get_handler(protocol, entry_point, context, uid, values, get_args), "\n"
print admin_transaction_add_handler(protocol, "admin", context, uid, values, get_args), "\n"
print admin_set_handler(protocol, "admin", context, uid, values, get_args),"\n"
print transaction_ios_pay_handler(protocol, "admin", context, uid, values, get_args),"\n"
print transaction_ios_pay_callback_handler(protocol, "admin", context, uid, values, get_args),"\n"

