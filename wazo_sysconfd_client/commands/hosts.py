# Copyright 2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import SysconfdCommand


class HostsCommand(SysconfdCommand):

    resource = 'hosts'
    headers = {'Accept': 'application/json'}

    def __call__(self, body):
        r = self.session.post(self.base_url, headers=self.headers, json=body)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
