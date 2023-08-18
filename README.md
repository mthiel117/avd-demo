# Arista CI Workshops

## **ATD Dual Datacenter Topology**

In this example, the ATD lab is used to create the L2LS Dual Data Center topology below. The IP Network cloud (orange area) is pre-provisioned and is comprised of the border and core nodes in the ATD topology. Our focus will be creating the L2LS AVD data models to build and deploy configurations for Site 1 and Site 2 (blue areas) and connect them to the IP Network.

![Topologies](images/topologies.png)

Using the Dual DC ATD Lab, demonstrate AVD to build Site 2 L2LS DC. Site 1 will be operational aftre following the Demo Prep section below.

## Demo Prep Site 1 and WAN/Hosts

Start a Fresh Dual DC ATD Lab

Clone my Forked Repo to ATD Environment

```bash
cd labfiles
git clone https://github.com/mthiel117/ci-workshops-avd.git
```

```bash
git config --global user.name "Mark Thiel"
git config --global user.email "mthiel117@gmail.com"
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
make preplab
```

```bash
make build-site-1
```

```bash
ansible-playbook playbooks/cvp1.yml -i sites/site_1/inventory.yml
```

## Execute Tasks via CC

Lab Demo prep complete!!! Time to show off the goodness of AVD.

## Demo - Steps Build configs and deploy via CVP

Uncomment Site-2 Vars

```bash
make build-site-2
```

Show updated configs and documentation

```bash
ansible-playbook playbooks/cvp2.yml -i sites/site_2/inventory.yml
```

Watch tasks and containers get built in CVP

Execute Tasks via CC.


