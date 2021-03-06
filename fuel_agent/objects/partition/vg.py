# -*- coding: utf-8 -*-

#    Copyright 2015 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from fuel_agent.objects import base


class VolumeGroup(base.Serializable):

    def __init__(self, name, pvnames=None, keep_data=False):
        self.keep_data = keep_data
        self.name = name
        self.pvnames = pvnames or []

    def add_pv(self, pvname):
        if pvname not in self.pvnames:
            self.pvnames.append(pvname)

    def to_dict(self):
        return {
            'name': self.name,
            'pvnames': self.pvnames,
            'keep_data': self.keep_data,
        }
