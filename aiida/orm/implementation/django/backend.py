# -*- coding: utf-8 -*-
###########################################################################
# Copyright (c), The AiiDA team. All rights reserved.                     #
# This file is part of the AiiDA code.                                    #
#                                                                         #
# The code is hosted on GitHub at https://github.com/aiidateam/aiida_core #
# For further information on the license, see the LICENSE.txt file        #
# For further information please visit http://www.aiida.net               #
###########################################################################
from __future__ import absolute_import
from aiida.orm.backend import Backend

from aiida.backends.djsite.queries import DjangoQueryManager
from . import authinfo
from . import computer
from . import log
from . import user


class DjangoBackend(Backend):

    def __init__(self):
        self._logs = log.DjangoLogCollection(self)
        self._users = user.DjangoUserCollection(self)
        self._authinfos = authinfo.DjangoAuthInfoCollection(self)
        self._computers = computer.DjangoComputerCollection(self)
        self._query_manager = DjangoQueryManager(self)

    @property
    def logs(self):
        return self._logs

    @property
    def users(self):
        return self._users

    @property
    def authinfos(self):
        return self._authinfos

    @property
    def computers(self):
        return self._computers

    @property
    def query_manager(self):
        return self._query_manager
