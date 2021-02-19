# Copyright 2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client.command import RESTCommand

from .exceptions import SysconfdError


class SysconfdCommand(RESTCommand):
    @staticmethod
    def raise_from_response(response):
        raise SysconfdError(response)
