#!/usr/bin/python
# -*- coding: utf-8 -*-
## Copyright (c) 2017-2018, The Sumokoin Project (www.sumokoin.org)
'''
App top-level settings
'''

__doc__ = 'default application wide settings'

import sys
import os
import logging
import socket

from utils.common import getHomeDir, makeDir

USER_AGENT = "PrivatePay Remote Wallet"
APP_NAME = "PrivatePay Remote Wallet"
VERSION = [0, 0, 1]


_data_dir = makeDir(os.path.join(getHomeDir(), 'PrivatepayRemote'))
DATA_DIR = _data_dir






log_file  = os.path.join(DATA_DIR, 'logs', 'app.log') # default logging file
log_level = logging.DEBUG # logging level

seed_languages = [("1", "English"), 
                  ("2", "Spanish"), 
                  ("3", "German"), 
                  ("4", "Italian"), 
                  ("5", "Portuguese"),
                  ("6", "Russian"),
                  ("7", "Japanese"),
                ]

# COIN - number of smallest units in one coin
COIN = 1000000000000.0

WALLET_RPC_PORT = 27444
WALLET_RPC_PORT_SSL = 27445
# DNS Resolve , Fixes a few issues for us
nodeserver = socket.gethostbyname('remote-node.privatepay.online')
REMOTE_DAEMON_HOST = nodeserver
REMOTE_DAEMON_PORT = 27445
REMOTE_DAEMON_SSL_PORT = 22226
REMOTE_DAEMON_ADDRESS = "%s:%s" % (REMOTE_DAEMON_HOST, REMOTE_DAEMON_PORT)
REMOTE_DAEMON_SSL_ADDRESS = "%s:%s" % (REMOTE_DAEMON_HOST, REMOTE_DAEMON_SSL_PORT)

RESOURCES_PATH = "../Resources" if sys.platform == 'darwin' and hasattr(sys, 'frozen') else "./Resources"
CA_CERTS_PATH = RESOURCES_PATH + "/certs/cacert-2018-03-07.pem"