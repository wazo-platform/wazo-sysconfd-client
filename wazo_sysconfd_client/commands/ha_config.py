# Copyright 2021-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import SysconfdCommand


class HAConfigCommand(SysconfdCommand):
    resource = 'ha'
    headers = {'Accept': 'application/json'}

    def update(self, body):
        r = self.session.put(
            self._client.url('ha'), headers=self.headers, json=body
        )

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def get(self):
        r = self.session.get(self._client.url('ha'), headers=self.headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
