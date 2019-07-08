# Edge Computing Slice
Edge Computing Slice aims to provide network and computing sharing resources to handle many user applications with special requirements over the unique infrastructure.

Here we bring some steps to follow to deploy and try our solution.

1. **Raspberry Installation**

* Download Raspberry Image: [Raspbian Buster with desktop and recommended software](https://www.balena.io/etcher/)
* Extract ISO file in a directory
* Uses a tool to mount ISO image on Raspberry SD-Card [Etcher](https://www.balena.io/etcher/)
* Start your Raspberry for the first time (make it updated)

2. **Installing OpenvSwitch on Raspberry**
* Dependences to compile OVS source:
  * Run: $ sudo apt-get install gcc flex bison
  * Run: $ sudo apt-get install bridge-utils
  * Run: $ sudo apt-get install make
  * Run: $ sudo apt-get install autoconf
  * Run: $ sudo apt-get install autoconf automake libtool perl graphviz bridge-utils git (**LXD requires _Linux Bridge_ installed**)
* Go to OVS page and download a desired release (>2.9.0 is required to work with NSH protocol) [2.10.0](https://www.openvswitch.org/releases/openvswitch-2.10.0.tar.gz)
* Extract tar file: $tar -zxvf <ovs.tar.gz>
* Open Extracted files on OVS directory: $ cd ovs
  * Run: $ ./boot
  * Run: $ ./configure --prefix=/usr --localstatedir=/var --sysconfdir=/etc (**Mandatory to LXD runs OVS commands**)
  * Run: $ sudo make
  * Run: $ sudo make install
* Setting up OVS:
  * Run: $ export PATH=$PATH:/usr/share/openvswitch/scripts
  * Run: $ ovs-ctl start (_Here all OVS deamons will run and OVS database will be populated_)
* Try OVS:
  * Run: # ovs-vsctl show

3. **Installing LXD (as snap) on Raspberry**
* Run: $ sudo apt-get install snap snapd
* Run: $ sudo snap install lxd
* Run: $ . /etc/profile.d/apps-bin-path.sh (_to put LXD commands available on bash_)
* Run: $ lxd init
* Run: # lxc launch ubuntu:16.04 <container-name>
* Run: # lxc network set testbr0 bridge.driver openvswitch (to change LXD network driver to OVS)
* Run: # lxc list



[Rodrigo Moreira](http://twitter.com/moreira_r) \
*E-mail*:
![alt text](https://github.com/romoreira/EdgeComputingSlice/blob/master/mail.PNG)

