# Copyright 2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import SysconfdCommand


class DeleteMohCommand(SysconfdCommand):
    resource = 'moh'
    headers = {'Accept': 'application/json'}

    def __call__(self, moh_name):
        r = self.session.delete(
            self.base_url, headers=self.headers, params={'name': moh_name}
        )

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
