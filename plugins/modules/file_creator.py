#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path=""
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']
    result['path'] = path

    # check_mode
    if module.check_mode:
        module.exit_json(**result)

    # checking content if the file exists
    if os.path.exists(path):
        with open(path, 'r') as f:
            existing = f.read()
        if existing == content:
            module.exit_json(**result)

    # create or write
    with open(path, 'w') as f:
        f.write(content)

    result['changed'] = True
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
