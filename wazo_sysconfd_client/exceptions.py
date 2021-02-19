# Copyright 2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from requests import HTTPError


class SysconfdError(HTTPError):
    def __init__(self, response):
        self.status_code = response.status_code
        self.message = response.text
        super(SysconfdError, self).__init__(self.message, response=response)
