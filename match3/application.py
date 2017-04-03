from erlport import Protocol
from match3.handlers.client_data.admin_set import admin_set_handler
from match3.handlers.client_data.admin_transaction_add import admin_transaction_add_handler
from match3.handlers.client_data.set_user import set_user_handler
from match3.handlers.client_data.get_user import get_user_handler
from match3.handlers.client_data.transaction_pay import transaction_pay_handler
from match3.handlers.client_data.transactions_unused_get import transactions_unused_get_handler
from match3.handlers.client_data.transactions_use import transactions_use_handler
from match3.handlers.client_data.transactions_used_get import transactions_used_get_handler


class Match3Protocol(Protocol):
    handle_get = get_user_handler
    handle_set = set_user_handler
    handle_transaction_pay = transaction_pay_handler
    handle_transactions_use = transactions_use_handler
    handle_transactions_unused_get = transactions_unused_get_handler
    handle_transactions_used_get = transactions_used_get_handler
    handle_admin_transaction_add = admin_transaction_add_handler
    handle_admin_set = admin_set_handler


    def __init__(self, *args, **kwargs):
        super(Match3Protocol, self).__init__(*args, **kwargs)
