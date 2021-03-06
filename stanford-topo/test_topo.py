#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import Link, Intf, TCLink
from mininet.topo import Topo
from mininet.util import dumpNodeConnections
import logging
import os 

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger( __name__ )

class LiTopo(Topo):
    # logger.debug("Class HugeTopo")
    # CoreSwitchList = []
    # AggSwitchList = []
    # EdgeSwitchList = []
    # HostList = []
    # iNUMBER = 0
    def __init__(self):
        #Init Topo
        Topo.__init__(self)
        self.host = []
        self.switch = []
        self.createhost()
        self.createswitch()
        self.createlink()
        """
        host1 = self.addHost("h1")
        host2 = self.addHost("h2")
        host3 = self.addHost("h3")
        host4 = self.addHost("h4")
        host5 = self.addHost("h5")
        host6 = self.addHost("h6")
        host7 = self.addHost("h7")
        host8 = self.addHost("h8")
        host9 = self.addHost("h9")
	

  
        switch1 = self.addSwitch("s1")
        switch2 = self.addSwitch("s2")
        switch3 = self.addSwitch("s3")
        switch4 = self.addSwitch("s4")
        switch5 = self.addSwitch("s5")

        self.addLink(host1,switch2)
        self.addLink(host2,switch2)
        self.addLink(host3,switch2)

        self.addLink(host4,switch3)
        self.addLink(host5,switch3)
        self.addLink(host6,switch3)

        self.addLink(host7,switch4)
        self.addLink(host8,switch4)
        self.addLink(host9,switch4)


        self.addLink(switch1,switch5)
        self.addLink(switch4,switch5)
        self.addLink(switch3,switch1)
        self.addLink(switch2,switch1)
        """

        """
        host1 = self.addHost("h1")
        # host2 = self.addHost("h2")
        # host3 = self.addHost("h3")
        host4 = self.addHost("h4")
        host5 = self.addHost("h5")
        host6 = self.addHost("h6")
        # host7 = self.addHost("h7")
        # host8 = self.addHost("h8")
        # host9 = self.addHost("h9")
    

        # host3 = self.addHost("h3")
  
        switch1 = self.addSwitch("s1")
        switch2 = self.addSwitch("s2")
        switch3 = self.addSwitch("s3")
        # switch4 = self.addSwitch("s4")
        # switch5 = self.addSwitch("s5")

        self.addLink(host1,switch2)
        # self.addLink(host2,switch2)
        # self.addLink(host3,switch2)

        self.addLink(host4,switch3)
        self.addLink(host5,switch3)
        self.addLink(host6,switch3)

        # self.addLink(host7,switch4)
        # self.addLink(host8,switch4)
        # self.addLink(host9,switch4)


        # self.addLink(switch1,switch5)
        # self.addLink(switch4,switch5)
        self.addLink(switch3,switch1)
        self.addLink(switch2,switch1)
        """

    def createhost(self):
        for i in range(10,30):
            self.host.append(self.addHost(str(i)))

    def createswitch(self):
        for i in range(3):
            self.host.append(self.addSwitch(str(i)))

    def createlink(self):
        for i in range(0,2):
            self.addLink(self.switch[i],self.switch[2])

        for i in range(0,10):
            self.addLink(self.host[i],self.switch[0])
        for i in range(10,20):
            self.addLink(self.host[i],self.switch[1])

topos = { 'litopo': ( lambda: LiTopo() ) }
