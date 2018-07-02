#!/usr/bin/python
# -*- coding: utf-8 -*-
## Copyright (c) 2017, The Sumokoin Project (www.sumokoin.org)
'''
App top-level settings
'''

__doc__ = 'default application wide settings'

import sys
import os
import logging

from utils.common import getHomeDir, makeDir

USER_AGENT = "PrivatePay"
APP_NAME = "PrivatePay Wallet"
VERSION = [0, 0, 1]


_data_dir = makeDir(os.path.join(os.getcwd(), 'data'))
DATA_DIR = _data_dir

log_file  = os.path.join(DATA_DIR, 'logs', 'app.log') # default logging file
log_level = logging.DEBUG # logging level

seed_languages = [("1", "English")
                ]

# COIN - number of smallest units in one coin
COIN = 1000000000000.0

WALLET_DAEMON_PORT = 27444
RPC_DAEMON_PORT = 27445
