# Arista CI Workshops

## **ATD Dual Datacenter Topology**

![Topologies](images/topologies.png)

Using the Dual DC ATD Lab, demonstrate how AVD is used to build Site 2 L2LS DC. Site 1 will be operational after following the Demo Prep section below.

## Demo Prep Site 1 and WAN/Hosts

Start a new Dual DC ATD Lab and build out Site 1 with the following steps

### Step #1

From the Programmability IDE

```bash
cd /home/coder/project/labfiles
git clone https://github.com/mthiel117/avd-demo.git
cd avd-demo
```

```bash
ansible-galaxy collection install -r requirements.yml
export ARISTA_AVD_DIR=$(ansible-galaxy collection list arista.avd --format yaml | head -1 | cut -d: -f1)
pip3 config set global.disable-pip-version-check true
pip3 install -r ${ARISTA_AVD_DIR}/arista/avd/requirements.txt
```

```bash
export LABPASSPHRASE=`cat /home/coder/.config/code-server/config.yaml| grep "password:" | awk '{print $2}'`
```

```bash
# Configures Core, Border, and Host nodes
make preplab
```

```bash
# Build Site 1 Full Configs
make build-site-1
```

```bash
# Move Site 2 Devices to Undefined Container
ansible-playbook playbooks/reset-lab.yml -i sites/site_2/inventory.yml
```

```bash
# Deploy Site 1 via CVP
ansible-playbook playbooks/cvp1.yml -i sites/site_1/inventory.yml
```

## OneLine Script to Prep Lab for Demo

Ensure that CVP has full started before running steps below.

>**CVP 2023.1.1 is currently UP**
>
>No pending tasks in CVP.

```bash
cd /home/coder/project/labfiles
git clone https://github.com/mthiel117/avd-demo.git
cd avd-demo

ansible-galaxy collection install -r requirements.yml
export ARISTA_AVD_DIR=$(ansible-galaxy collection list arista.avd --format yaml | head -1 | cut -d: -f1)
pip3 config set global.disable-pip-version-check true
pip3 install -r ${ARISTA_AVD_DIR}/arista/avd/requirements.txt

export LABPASSPHRASE=`cat /home/coder/.config/code-server/config.yaml| grep "password:" | awk '{print $2}'`

make preplab

make build-site-1

# Move Site 2 Devices to Undefined Container
ansible-playbook playbooks/reset-lab.yml -i sites/site_2/inventory.yml

ansible-playbook playbooks/cvp1.yml -i sites/site_1/inventory.yml
```

Lab Demo prep complete!!! Time to show off the goodness of AVD.

## Demo - Steps Build configs and deploy via CVP

Now with the Lab prepped with Site 1 and Core WAN, we can build out Site 2 for the demo.

### Step #1

Uncomment Site-2 Vars

  - SITE2_FABRIC_PORTS.yml
  - SITE2_FABRIC_SERVICES.yml

### Step #2

Build Site 2 Configs & Docs

```bash
make build-site-2
```

Show updated configs and documentation

### Step #3

```bash
make cvp-site-2
```

Watch tasks and containers get built in CVP

### Step #4

Create Change Control to execute Tasks.

Run some watchg commands to show live changes to the nodes.

Example: s2-spine1

```bash
watch show ip int br
```

*Show nodes moved to new containers and have configlets attached.*

### Step #5

Show traffic between Site 1 and Site 2.

From: s1-host1 ping s2-host1

```bash
ping 10.30.30.100
```

## Cleanup & Reset Lab - Move Site 2 nodes to undefined container

Use this playbook to reset Site 2 nodes t undefined container before doing a demo.  Need to also cleanup Containers in CVP.

```bash
ansible-playbook playbooks/reset-lab.yml -i sites/site_2/inventory.yml
```
## Arista Network Testing Automation (ANTA) Framework

**BONUS Material**

Run some network tests against the ATD Lab nodes.

Go [here](anta/README.md).