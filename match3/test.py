import simplejson
from erlport import Atom

from match3.handlers.client_data.admin_set import admin_set_handler
from match3.handlers.client_data.admin_transaction_add import admin_transaction_add_handler
from match3.handlers.client_data.get_user import get_user_handler

from match3.handlers.client_data.set_user import set_user_handler
from match3.handlers.client_data.transaction_pay import transaction_pay_handler
from match3.handlers.client_data.transactions_unused_get import transactions_unused_get_handler
from match3.handlers.client_data.transactions_use import transactions_use_handler

protocol = None
entry_point = "main"
uid = "1"
context = None
values = [(Atom("player"), '{"player":"ddd", "unused_transactions": ["trans123456"]}')]
values = [(Atom("player"), simplejson.dumps({"player":"ddd", "unused_transactions": {"r_starter_pack_10": [{"order_id": "GPA.1387-2118-8871-37321", "purchaise_time": 1484925738969}]}}))]
get_args = {"item":"r_starter_pack_1",
            "order":"GPA.1387-2118-8871-37321",
            "payload":'{"json":"{\\"orderId\\":\\"GPA.1387-2118-8871-37321\\",\\"packageName\\":\\"ru.kefirgames.fog\\",\\"productId\\":\\"r_starter_pack_1\\",\\"purchaseTime\\":1484925738969,\\"purchaseState\\":0,\\"developerPayload\\":\\"e6f22045d9544675971b7f32950b7c07\\",\\"purchaseToken\\":\\"ekbimahedplagnenlimajefm.AO-J1OwTLt42GUuocUJOzMDLAekRl03LjfEPzKSE8YJnTVcGlI15vf8oR5gHmq_KaJSdBHRGqiVu4sqfhJzEjCleT9EV3x_1A6SDxr4uL1pny8xU0kKN_YCZSh885zMsYPdVI4D_u-gd\\"}","signature":"PdvdML2C3CCxh7R5NS92GRiIQ2aaUCMm4kumEZ0kyCW8OhFBfy5F0m9kdJP+IxCY7KfwgIotm5Dt3p\/IAwIyBE8AVDVrrgxpFSZS3xII3onC4chI50A4AROcOm5d0L1LU7sMtuWn6PUgdksZfLGJ0RSSplHm\/hLv+kmc\/9w\/cB0CIlug9uf18Wy++wjjEG+gsL0p+U89DC1LjNh\/Ca8gVSAxTm9XmktPSZFXk6xINpHHTJgGQTiKUj4VV8hbPsHO0wQKFuyQ33ViobJZGODKIIb7NP3pDjPyCtKTJDqlqWYADsjlAQUhd4LwXdHmzxr9nJQA2CKQdhuKtDCay\/BjlA=="}',
            "product_id": "p", "order_id": "o","purchase_time": "t",
            "data":'{"used_transactions": "ololo"}'}



print get_user_handler(protocol, entry_point, context, uid, values, get_args), "_____________"

print set_user_handler(protocol, entry_point, context, uid, values, get_args), "_____________"
#print transaction_pay_handler(protocol, entry_point, context, uid, values, get_args), "_____________"
#print transactions_use_handler(protocol, entry_point, context, uid, values, get_args), "_____________"
#print transactions_unused_get_handler(protocol, entry_point, context, uid, values, get_args), "_____________"
#print admin_transaction_add_handler(protocol, "admin", context, uid, values, get_args), "_____________"
print admin_set_handler(protocol, "admin", context, uid, values, get_args),
