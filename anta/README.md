# Arista Network Test Automation (ANTA) Framework

## Repository

https://github.com/arista-netdevops-community/anta


## Documentation

https://www.anta.ninja/

## Get Started

### Install ANTA

``` bash
pip install anta
```

### Create ANTA Inventory File (inventory.yml)

Sample

```text
anta_inventory:
  hosts:
##########################################
# ATD Site 1 Spine and Leafs
##########################################
  - host: 192.168.0.10
    name: s1-spine1
    tags: ['fabric', 'spine']
  - host: 192.168.0.11
    name: s1-spine2
    tags: ['fabric', 'spine']
```

### Create Test Catalog (test-catalog.yml)

```text
anta.tests.software:
  - VerifyEOSVersion: # Verifies the device is running one of the allowed EOS version.
      versions: # List of allowed EOS versions.
        - 4.25.4M
        - 4.30.1F
        - '4.28.3M-28837868.4283M (engineering build)'
  - VerifyTerminAttrVersion:
      versions:
        - v1.22.1
        - v1.27.0
anta.tests.configuration:
  - VerifyZeroTouch: # Verifies ZeroTouch is disabled.
  - VerifyRunningConfigDiffs:

anta.tests.system:
  - VerifyReloadCause:
  - VerifyNTP:

anta.tests.mlag:
  - VerifyMlagStatus:
  - VerifyMlagInterfaces:
  - VerifyMlagConfigSanity:
```

## Create Environment Variables (anta.env)

These will be used to log into devices and set output directories instead iof speciying on command-line each time.

```text
#!/bin/zsh
echo 'Creating default anta variables'
export ANTA_USERNAME=arista
export ANTA_PASSWORD=$LABPASSPHRASE
export ANTA_ENABLE=true

export ANTA_INVENTORY=./inventory.yml

export ANTA_EXEC_SNAPSHOT_OUTPUT=./network-tests/$(date +%Y-%m-%d-%Hh-%Mmin)-snapshots

echo 'Build auto-complete for anta'
eval "$(_ANTA_COMPLETE=zsh_source anta)" > /dev/null
```

## Review ANTA Parameters

```bash
cat anta.env
```

## Source ANTA Parameters

```bash
source anta.env
```

## Run Tests

Runs Tests against inventory

```bash
anta nrfu table
```

Run Snapshot of commands

```bash
anta exec snapshot
```

Run command on specific device

```bash
anta debug run-cmd -c "show lldp neighbors" --device s1-spine1
```