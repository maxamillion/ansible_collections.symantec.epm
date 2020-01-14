#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2019, Adam Miller (admiller@redhat.com)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}
DOCUMENTATION = """
---
module: computers_info
short_description: Obtain information about Symantec Endpoint Protection Manager computers
description:
  - Obtain information about Symantec Endpoint Protection Manager computers
version_added: "2.9"
notes:
  - This module does not take any options
  - This module returns a dict of computer data and is meant to be registered to a
    variable in a Play for conditional use or inspection/debug purposes.

author: Ansible Security Automation Team (@maxamillion) <https://github.com/ansible-security>"
"""


# FIXME - provide correct example here
RETURN = """
"""

EXAMPLES = """
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_text

from ansible.module_utils.urls import Request
from ansible.module_utils.six.moves.urllib.parse import quote
from ansible.module_utils.six.moves.urllib.error import HTTPError
from ansible_collections.symantec.epm.plugins.module_utils.epm import (
    EPMRequest,
)

import copy
import json


def main():

    argspec = dict(
    )

    module = AnsibleModule(argument_spec=argspec, supports_check_mode=True)

    epm_request = EPMRequest(
        module, headers={"Content-Type": "application/json"}
    )

    computers = epm_request.get_by_path("sepm/api/v1/computers")

    if 'content' in computers:
        module.exit_json(computers=computers['content'], changed=False)
    else:
        module.fail_json(msg="Unable to query computers data")




if __name__ == "__main__":
    main()
