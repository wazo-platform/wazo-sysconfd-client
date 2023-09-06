# Copyright 2021-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import SysconfdCommand


class DeleteVoicemailCommand(SysconfdCommand):
    resource = 'delete_voicemail'
    headers = {'Accept': 'application/json'}

    def __call__(self, mailbox, context=None):
        params = {'mailbox': mailbox}
        if context:
            params['context'] = context
        r = self.session.get(self.base_url, headers=self.headers, params=params)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()


class MoveVoicemailCommand(SysconfdCommand):
    resource = 'move_voicemail'
    headers = {'Accept': 'application/json'}

    def __call__(self, old_mailbox, old_context, new_mailbox, new_context):
        params = {
            'old_mailbox': old_mailbox,
            'old_context': old_context,
            'new_mailbox': new_mailbox,
            'new_context': new_context,
        }
        r = self.session.get(self.base_url, headers=self.headers, params=params)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()


class DeleteVoicemailsContextCommand(SysconfdCommand):
    resource = 'voicemails_context'
    headers = {'Accept': 'application/json'}

    def __call__(self, context):
        r = self.session.delete(self.base_url, headers=self.headers, params={'context': context})

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()