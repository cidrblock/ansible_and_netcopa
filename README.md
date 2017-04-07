

### Sample run
```
➜  /working ansible-playbook site.yml -i inventory.txt --check

PLAY [all] *********************************************************************

TASK [interface : set_fact] ****************************************************
ok: [cisco_ios-xe-00]

TASK [interface : Include OS files for interface] ******************************
included: /working/roles/interface/tasks/cisco_ios-xe.yml for cisco_ios-xe-00

TASK [interface : Set fact for desired interfaces configuration] ***************
ok: [cisco_ios-xe-00]

TASK [interface : Include OS files for interface] ******************************
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00
included: /working/roles/interface/tasks/cisco_ios-xe-interface.yml for cisco_ios-xe-00

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/0/2)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/0/0.30)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/2/2.61)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/0/0.10)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/0/0)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/0/1)] ***
changed: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
ok: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/0/2.30)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/0/3)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/1/1)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/1/0)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/1/3)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/1/2)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/1/4)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (Loopback47061)]
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (Loopback0)] ****
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/0/1.10)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/0/1.30)] ***
changed: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
ok: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/2/4)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/2/2)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/2/3)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/2/0)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [interface : Modify interface configuration as needed for (GigabitEthernet0/2/1)] ***
ok: [cisco_ios-xe-00]

TASK [interface : Append changes to log (cisco_ios-xe)] ************************
skipping: [cisco_ios-xe-00]

TASK [ansible_change_report : Show config changes for device] ******************
ok: [cisco_ios-xe-00] => {
    "msg": [
        "*** ROLE: interface ***",
        "interface GigabitEthernet0/0/1",
        "no negotiation auto",
        "*** ROLE: interface ***",
        "interface GigabitEthernet0/0/1.30",
        "ip address 10.0.0.200 255.255.255.0"
    ]
}

PLAY RECAP *********************************************************************
cisco_ios-xe-00            : ok=52   changed=2    unreachable=0    failed=0
```
