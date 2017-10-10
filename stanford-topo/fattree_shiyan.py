#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.node import OVSKernelSwitch, UserSwitch 
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import Link, Intf, TCLink
from mininet.topo import Topo
from mininet.util import dumpNodeConnections
import logging
import user
import os
import time

logging.basicConfig(filename='./fattree.log', level=logging.INFO)
logger = logging.getLogger(__name__)


class Fattree(Topo):
    logger.debug("Class Fattree")
    SwitchList = []
    HostList = []

    def __init__(self):
        #Init Topo
        Topo.__init__(self)

    def createTopo(self):
        self.createSwitch()
        self.createHost()

    """
    Create Switch and Host
    """
    def createSwitch(self):
        for x in range(1,4):
            self.SwitchList.append(self.addSwitch('s'+str(x),cls=UserSwitch, listenPort=(6634+x-1)))


    def createHost(self):
        logger.debug("Create Host")
        for x in xrange(1, 20):
            self.HostList.append(self.addHost('h'+str(x)))

    """
    Add Link
    """
    def createLink(self):
        self.addLink(self.SwitchList[0],self.SwitchList[1])
        self.addLink(self.SwitchList[0],self.SwitchList[2])
        self.addLink(self.SwitchList[1],self.HostList[0])
        for i in range(1,19):
            self.addLink(self.SwitchList[2],self.HostList[i])
    
    def set_ovs_protocol_13(self,):
        self._set_ovs_protocol_13(self.SwitchList)

    def _set_ovs_protocol_13(self, sw_list):
            for sw in sw_list:
                cmd = "sudo ovs-vsctl set bridge %s protocols=OpenFlow13" % sw
                os.system(cmd)


def iperfTest(net, topo):
    # time.sleep(10)
    logger.debug("Start iperfTEST")
    # h1000, h1015, h1016 = net.get(
    #     topo.HostList[0], topo.HostList[14], topo.HostList[15])

    h1 = net.get(topo.HostList[0])
    h1.popen('iperf -s ')

    # h2 = net.get(topo.HostList[1])
    #iperf Server
    # h1.cmdPrint('iperf -s')
    # h2.cmdPrint('iperf -s')

    print "iperf test start"
    for  i in range(1,19,5):
        net.get(topo.HostList[i]).cmdPrint('iperf -c ' ,h1.IP())

    for  i in range(2,19,5):
        net.get(topo.HostList[i]).cmdPrint('iperf -c ' ,h1.IP())

    for  i in range(3,19,5):
        net.get(topo.HostList[i]).cmdPrint('iperf -c ' ,h1.IP())

    for  i in range(4,19,5):
        net.get(topo.HostList[i]).cmdPrint('iperf -c ' ,h1.IP())

    for  i in range(5,19,5):
        net.get(topo.HostList[i]).cmdPrint('iperf -c ' ,h1.IP())
    # net.get(topo.HostList[0]).cmdPrint('iperf -c ' ,h2.IP())

    #iperf Server
    # h1015.popen(
    #     'iperf -s -u -i 1 > iperf_server_samePod_result', shell=True)

    #iperf Client
    # h1016.cmdPrint('iperf -c ' + h1000.IP() + ' -u -t 10 -i 1 -b 100m')
    # h1016.cmdPrint('iperf -c ' + h1015.IP() + ' -u -t 10 -i 1 -b 100m')

    # for i in range(1,3):
    #     net.get(topo.HostList[i]).cmdPrint('iperf -c ' + h1.IP())
    # for i in range(1,3):
    #     net.get(topo.HostList[i]).cmdPrint('iperf -c ' + h1.IP())

def iperfTest2(net, topo):
    h1 = net.get(topo.HostList[0])
    h1.popen('iperf -s ')
    print "iperf test start"
    for  i in range(1,19):
        net.get(topo.HostList[i]).cmdPrint('iperf -c ' ,h1.IP())
        

def pingTest1(net,topo):
    logger.debug("Start Test all network")
    # net.pingAll()
    h1 = net.get(topo.HostList[0])
    for i in range(1,3):
        start = time.clock()
        print h1.cmd( 'ping -c 3', net.get(topo.HostList[i]).IP() ) 
        elapsed=(time.clock()-start)
        print "num:",i,"time cost:",elapsed

def pingTest2(net,topo):
    logger.debug("Start Test all network")
    # net.pingAll()
    h1 = net.get(topo.HostList[0])
    for i in range(1,19,5):
        start = time.clock()
        print h1.cmd( 'ping -c 3', net.get(topo.HostList[i]).IP() ) 
        elapsed=(time.clock()-start)
        print "num:",i,"time cost:",elapsed
    for i in range(2,19,5):
        start = time.clock()
        print h1.cmd( 'ping -c 3', net.get(topo.HostList[i]).IP() ) 
        elapsed=(time.clock()-start)
        print "num:",i,"time cost:",elapsed
    for i in range(3,19,5):
        start = time.clock()
        print h1.cmd( 'ping -c 3', net.get(topo.HostList[i]).IP() ) 
        elapsed=(time.clock()-start)
        print "num:",i,"time cost:",elapsed
    for i in range(4,19,5):
        start = time.clock()
        print h1.cmd( 'ping -c 3', net.get(topo.HostList[i]).IP() ) 
        elapsed=(time.clock()-start)
        print "num:",i,"time cost:",elapsed
    for i in range(5,19,5):
        start = time.clock()
        print h1.cmd( 'ping -c 3', net.get(topo.HostList[i]).IP() ) 
        elapsed=(time.clock()-start)
        print "num:",i,"time cost:",elapsed

def Packetloss(net,topo):
    h1 = net.get(topo.HostList[0])
    # h1.popen('iperf -s ')
    print "iperf test start"
    for  i in range(1,19):
        net.get(topo.HostList[i]).cmdPrint(' mtr -r ', h1.IP() )


def createTopo(ip="127.0.0.1", port=6633):
    logging.debug("LV1 Create Fattree")
    topo = Fattree()
    topo.createTopo()
    topo.createLink()

    logging.debug("LV1 Start Mininet")
    CONTROLLER_IP = ip
    CONTROLLER_PORT = port
    net = Mininet(topo=topo, link=TCLink, controller=None, autoSetMacs=False,
                  autoStaticArp=False,switch=UserSwitch)
    net.addController(
        'controller', controller=RemoteController,
        ip=CONTROLLER_IP, port=CONTROLLER_PORT)
    net.start()

    '''
        Set OVS's protocol as OF13
    '''
    # topo.set_ovs_protocol_13()

    logger.debug("LV1 dumpNode")
    # time.sleep(10)

    pingTest1(net,topo)
    # print "**************"
    # pingTest1(net,topo)

    
    # pingTest2(net,topo)
    # print "**************"
    # pingTest2(net,topo)


    # iperfTest(net, topo)
    # iperfTest(net, topo)

    # iperfTest2(net, topo)
    # iperfTest2(net, topo)
    
    Packetloss(net, topo)

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    if os.getuid() != 0:
        logger.debug("You are NOT root")
    elif os.getuid() == 0:
        createTopo()