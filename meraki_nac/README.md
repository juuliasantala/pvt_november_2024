# Meraki sites with Ansible

1. Define your Meraki API key in environment variables:
```bash
export MERAKI_DASHBOARD_API_KEY=<Key>
```

2. Update the `organizationId` in `meraki_sites` to match your environment. The sites will be created under the defined organization.

3. Run the script with `ansible-playbook`:
```bash
ansible-playbook -i hosts.yaml meraki_sites.yaml
```
