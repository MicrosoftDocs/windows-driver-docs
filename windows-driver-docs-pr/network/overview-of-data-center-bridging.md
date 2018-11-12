---
title: Overview of Data Center Bridging
description: Overview of Data Center Bridging
ms.assetid: FEB3FDBB-8A3C-4907-A6D0-CB5E94BCFEFF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Data Center Bridging


IEEE 802.1 Data Center Bridging (DCB) is a collection of standards that defines a unified 802.3 Ethernet media interface, or *fabric*, for local area network (LAN) and storage area network (SAN) technologies. DCB extends the current 802.1 bridging specification to support the coexistence of LAN-based and SAN-based applications over the same networking fabric within a data center. DCB also supports technologies, such as Fibre Channel over Ethernet (FCoE) and iSCSI, by defining link-level policies that prevent packet loss.

DCB consists of the following 802.1 draft standards that specify how networking devices can interoperate within a unified data center fabric:

<a href="" id="priority-based-flow-control--pfc-"></a>Priority-based Flow Control (PFC)  
PFC is specified in the IEEE 802.1Qbb draft standard. This standard is part of the framework for the DCB interface.

PFC supports the reliable delivery of data by substantially reducing packet loss due to congestion. This allows loss-sensitive protocols, such as FCoE, to coexist with traditional loss-insensitive protocols over the same unified fabric.

PFC specifies a link-level flow control mechanism between directly connected peers. PFC is similar to IEEE 802.3 PAUSE frames but operates on individual 802.1p priority levels instead. This allows a receiver to pause a transmitter on any priority level.

For more information on PFC, see [Priority-based Flow Control (PFC)](priority-based-flow-control--pfc.md).

<a href="" id="enhanced-transmission-selection--ets-"></a>Enhanced Transmission Selection (ETS)  
ETS is a transmission selection algorithm (TSA) that is specified in the IEEE 802.1Qaz draft standard. This standard is part of the framework for the DCB interface.

ETS allocates bandwidth between traffic classes that are assigned to different IEEE 802.1p priority levels. Each traffic class is allocated a percentage of available bandwidth on the data link between directlyconnected peers. If a traffic class doesn't use its allocated bandwidth, ETS allows other traffic classes to use the available bandwidth that the traffic class is not using.

For more information on ETS, see [Enhanced Transmission Selection (ETS) Algorithm](enhanced-transmission-selection--ets--algorithm.md).

<a href="" id="data-center-bridging-exchange--dcbx--protocol"></a>Data Center Bridging Exchange (DCBX) Protocol  
The Data Center Bridging Exchange (DCBX) protocol is also specified in the IEEE 802.1Qaz draft standard. DCBX allows DCB configuration parameters to be exchanged between two directlyconnected peers. This allows these peers to adapt and tune Quality of Service (QoS) parameters to optimize data transfer over the connection.

DCBX is also used to detect conflicting QoS parameter settings between the network adapter (*local peer*) and the remote peer. Based on the local and remote QoS parameter settings, the miniport driver resolves the conflicts and derives a set of operational QoS parameters. The network adapter uses these operational parameters for the prioritized transmission of packets to the remote peer. For more information about how the driver resolves its operational NDIS QoS parameter settings, see [Resolving Operational NDIS QoS Parameters](resolving-operational-ndis-qos-parameters.md).

DCBX consists of DCB type-length-value (TLV) settings that are carried over the Link Layer Discovery Protocol (LLDP) packets. LLDP is specified in the IEEE 802.1AB-2005 standard.

**Note**  DCBX specifies that the local peer maintain configuration parameters from only one remote peer at any given time. As a result, the network adapter maintains only one set of local, remote, and operational NDIS QoS parameters.

 

Each ETS traffic class and PFC configuration setting is associated with an IEEE 802.1p priority level. The priority level is specified as a 3-bit value within a packet's 802.1Q tag. For NDIS packets, the 802.1p priority level is specified by the **UserPriority** member of the [**NDIS\_NET\_BUFFER\_LIST\_8021Q\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566565) structure that is associated with a packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

For more information about priority levels, see [IEEE 802.1p Priority Levels](ieee-802-1p-priority-levels.md).

 

 





