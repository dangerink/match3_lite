# -*- coding: utf-8 -*-
# __author__ = ink
import json
import os
import traceback, logging
from time import strftime, gmtime, time

from erlport import Atom

from match3 import btl_result
from match3.btl_result import BtlResult
from match3.model.world import World
from time import gmtime, strftime

def pythonLogger(folder_name, file_name=None):
    logger = logging.getLogger(folder_name)
    logger.setLevel(logging.DEBUG)
    today = strftime("%d_%b_%Y", gmtime())
    path = '{}/log'.format(os.getcwd())
    if not os.path.exists(path):
        os.mkdir(path)
    dir = '{}/{}'.format(path, folder_name)
    if not os.path.exists(dir):
        os.mkdir(dir)
    for file in os.listdir(dir):
        full_name = '{}/{}'.format(dir, file)
        if os.path.getctime(full_name) + 432000 < time():
            os.remove(full_name)
    file_name = file_name or today
    handler = logging.FileHandler('{}/{}.log'.format(dir, file_name), 'a')
    logger.addHandler(handler)
    return logger


def logger(uid):
    def write(text):
        logger = pythonLogger(uid)
        log_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        logger.info("INFO {}: {}".format(
            log_time, text))
        logger.handlers[0].stream.close()
        logger.removeHandler(logger.handlers[0])
    return write


def preload():
    try:
        def wrap(handler):
            def _inner(protocol, entry_point, context=None, uid=None, values=None, get_args=None, *args):
                try:
                    l = logger(uid)
                    values = dict(values)

                    world = World(uid, l, context, **values)
                    result = handler(protocol, entry_point, world, get_args)

                    btl_result = BtlResult(world.raw)
                    return btl_result.get_result(result)
                except :
                    try:
                        l(traceback.format_exc())
                    except:
                        pass
                    return Atom("error"), json.dumps({"result": "fail"})
            return _inner
        return wrap
    except :
        try:
            l = logger("info")
            l(traceback.format_exc())
        except:
            pass
        return Atom("error"), json.dumps({"result": "critical"})


