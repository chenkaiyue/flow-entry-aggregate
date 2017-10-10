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

class NoLoopTopo(Topo):
    # logger.debug("Class HugeTopo")
    # CoreSwitchList = []
    # AggSwitchList = []
    # EdgeSwitchList = []
    # HostList = []
    # iNUMBER = 0
    def __init__(self):
        #Init Topo
        Topo.__init__(self)

        host1 = self.addHost("h1")
        host2 = self.addHost("h2")
        # host3 = self.addHost("h3")
  
        switch1 = self.addSwitch("s1")
        switch2 = self.addSwitch("s2")

        self.addLink(host1,switch1)
        self.addLink(switch1,switch2)
        self.addLink(host2,switch2)
        # self.addLink(host3,swithc1)        

topos = { 'nolooptopo': ( lambda: NoLoopTopo() ) }
