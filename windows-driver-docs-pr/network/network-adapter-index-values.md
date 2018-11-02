---
title: Network Adapter Index Values
description: Network Adapter Index Values
ms.assetid: 969333DA-0282-474B-8D56-72CD623C5329
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Network Adapter Index Values


In the Hyper-V extensible switch interface, each network adapter that is connected to a port is assigned an NDIS\_SWITCH\_NIC\_INDEX value. This index value identifies the network connection on an extensible switch port.

The index value is unique for each network adapter connection to a port. Although most network adapters require only one index value, the port connection to the external network adapter may be assigned multiple index values. For example, if the external network adapter is bound to a team of physical network adapters, the external network adapter and each physical network adapter is assigned a unique index value.

The connections to network adapters in the extensible switch are identified through the following NDIS\_SWITCH\_NIC\_INDEX values:

<a href="" id="ndis-switch-default-nic-index"></a>NDIS\_SWITCH\_DEFAULT\_NIC\_INDEX  
This index value specifies the index for the network adapter that is connected to an extensible switch port. This index value applies to any network adapter that is directly connected to an extensible switch port, such as an external network adapter, internal network adapter, or virtual machine (VM) network adapter.

**Note**  NDIS\_SWITCH\_DEFAULT\_NIC\_INDEX is defined to be zero.

 

<a href="" id="1-32"></a>1-32  
This index value specifies the index for an underlying physical network adapter that is bound to the extensible switch external network adapter. Index values are assigned based on the following configurations:

-   If the external network adapter is bound to a single physical network adapter, it is assigned an index value of one.

-   If the external network adapter is bound to a load balancing fail over (LBFO) team of physical network adapters, the entire team is assigned an index value of one. An LBFO team is a configuration in which the external network adapter is bound to the virtual miniport edge of an LBFO provider. The LBFO provider itself can bind to a team of one or more physical network adapters.

    **Note**  To extensible switch extensions, an underlying LBFO team appears as a single network adapter that is bound to the external network adapter.

     

-   If the external network adapter is bound to an extensible switch team of physical network adapters, each adapter in the team is assigned a unique index value that is greater than or equal to one. An extensible switch team is a configuration in which a team of one or more physical network adapters is bound to the external network adapter.

For more information about the different configurations in which physical network adapters can be bound to the external network adapter, see [Types of Physical Network Adapter Configurations](types-of-physical-network-adapter-configurations.md).

 

 





