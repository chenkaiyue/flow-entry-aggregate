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

class HugeTopo(Topo):
    logger.debug("Class HugeTopo")
    CoreSwitchList = []
    AggSwitchList = []
    EdgeSwitchList = []
    HostList = []
    iNUMBER = 0
    def __init__(self):
        logger.debug("Class HugeTopo init")
        iNUMBER = 4

        self.iNUMBER = iNUMBER
        self.iCoreLayerSwitch = iNUMBER
        self.iAggLayerSwitch = iNUMBER * 2
        self.iEdgeLayerSwitch = iNUMBER * 2
        self.iHost = self.iEdgeLayerSwitch * 2 


        #Init Topo
        Topo.__init__(self)

        logger.debug("Start create Core Layer Swich")
        self.createCoreLayerSwitch(self.iCoreLayerSwitch)
        logger.debug("Start create Agg Layer Swich ")
        self.createAggLayerSwitch(self.iAggLayerSwitch)
        logger.debug("Start create Edge Layer Swich ")
        self.createEdgeLayerSwitch(self.iEdgeLayerSwitch)
        logger.debug("Start create Host")
        self.createHost(self.iHost)

        self.createLink()
    """
    Create Switch and Host
    """

    def createCoreLayerSwitch(self, NUMBER):
        logger.debug("Create Core Layer")
        for x in range(1, NUMBER+1):
            PREFIX = "100"
            if x >= int(10):
                PREFIX = "10"
            self.CoreSwitchList.append(self.addSwitch(PREFIX + str(x)))

    def createAggLayerSwitch(self, NUMBER):
        logger.debug( "Create Agg Layer")
        for x in range(1, NUMBER+1):
            PREFIX = "200"
            if x >= int(10):
                PREFIX = "20"
            self.AggSwitchList.append(self.addSwitch(PREFIX + str(x)))

    def createEdgeLayerSwitch(self, NUMBER):
        logger.debug("Create Edge Layer")
        for x in range(1, NUMBER+1):
            PREFIX = "300"
            if x >= int(10):
                PREFIX = "30"
            self.EdgeSwitchList.append(self.addSwitch(PREFIX + str(x)))

    def createHost(self, NUMBER):
        logger.debug("Create Host")
        for x in range(1, NUMBER+1):
            PREFIX = "400"
            if x >= int(10):
                PREFIX = "40"
            self.HostList.append(self.addHost(PREFIX + str(x))) 

    """
    Create Link 
    """
    def createLink(self):
        logger.debug("Create Core to Agg")
        for x in range(0, self.iAggLayerSwitch, 2):
            self.addLink(self.CoreSwitchList[0], self.AggSwitchList[x])
            self.addLink(self.CoreSwitchList[1], self.AggSwitchList[x])
        for x in range(1, self.iAggLayerSwitch, 2):
            self.addLink(self.CoreSwitchList[2], self.AggSwitchList[x])
            self.addLink(self.CoreSwitchList[3], self.AggSwitchList[x])

        logger.debug("Create Agg to Edge")
        for x in range(0, self.iAggLayerSwitch, 2):
            self.addLink(self.AggSwitchList[x], self.EdgeSwitchList[x])
            self.addLink(self.AggSwitchList[x], self.EdgeSwitchList[x+1])
            self.addLink(self.AggSwitchList[x+1], self.EdgeSwitchList[x])
            self.addLink(self.AggSwitchList[x+1], self.EdgeSwitchList[x+1])

        logger.debug("Create Edge to Host")
        for x in range(0, self.iEdgeLayerSwitch):
            ## limit = 2 * x + 1 
            self.addLink(self.EdgeSwitchList[x], self.HostList[2 * x])
            self.addLink(self.EdgeSwitchList[x], self.HostList[2 * x + 1])


topos = { 'fattree1': ( lambda: HugeTopo() ) }