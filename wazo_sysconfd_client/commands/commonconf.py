# Copyright 2021-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import SysconfdCommand


class CommonConfApplyCommand(SysconfdCommand):
    resource = 'commonconf_apply'
    headers = {'Accept': 'application/json'}

    def __call__(self):
        r = self.session.get(self.base_url, headers=self.headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()


class CommonConfGenerateCommand(SysconfdCommand):
    resource = 'commonconf_generate'
    headers = {'Accept': 'application/json'}

    def __call__(self):
        r = self.session.post(self.base_url, headers=self.headers, json={})

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
