# Copyright 2021-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import SysconfdCommand


class CommonConfCommand(SysconfdCommand):
    resource = 'commonconf'
    headers = {'Accept': 'application/json'}

    def apply(self):
        r = self.session.get(self.base_url, headers=self.headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def generate(self):
        r = self.session.put(self.base_url, headers=self.headers, json={})
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
