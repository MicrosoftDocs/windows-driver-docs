---
title: Managing Physical Network Adapter Connection Status
description: Managing Physical Network Adapter Connection Status
ms.assetid: B8C6EB48-59D7-469B-87C8-57E60CB5C5D2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing Physical Network Adapter Connection Status


The Hyper-V extensible switch architecture supports the connection to a single external network adapter for access to the underlying physical medium. The external network adapter can be bound to one or more underlying physical network adapters in a variety of configurations. For more information about these configurations, see [Types of Physical Network Adapter Configurations](types-of-physical-network-adapter-configurations.md).

The extensible switch interface notifies extensions of each physical network adapter connection status through the following steps:

1.  The protocol edge of the extensible switch issues an object identifier (OID) set request of [OID\_SWITCH\_NIC\_CREATE](https://msdn.microsoft.com/library/windows/hardware/hh598263). This OID request notifies underlying extensible switch extensions about the creation of network connection to the extensible switch external network adapter.

    When the network connection is created, it is assigned an NDIS\_SWITCH\_NIC\_INDEX value. This index value identifies the network connection of the adapter on an extensible switch port. The network connection to the external network adapter is assigned an NDIS\_SWITCH\_NIC\_INDEX value of **NDIS\_SWITCH\_DEFAULT\_NIC\_INDEX**.

2.  For every network adapter that is bound directly or indirectly to the external network adapter, the protocol edge of the extensible switch issues a separate OID set request of [OID\_SWITCH\_NIC\_CREATE](https://msdn.microsoft.com/library/windows/hardware/hh598263). This OID request notifies the extension about the creation of a network connection to an underlying network adapter.

    Each physical or virtual network adapter that is bound to the external network adapter is assigned an identifier in the following way:

    -   If a single physical adapter is bound to the external network adapter, it is assigned a NDIS\_SWITCH\_NIC\_INDEX value of one.

    -   If an load balancing fail over (LBFO) team of network adapters is bound to the external network adapter, it is assigned a NDIS\_SWITCH\_NIC\_INDEX value of one.

        **Note**  In the LBFO team configuration, only the virtual miniport edge of the LBFO provider that supports the LBFO team is considered to be bound to the external network adapter.




-   If an extensible switch team of network adapters is bound to the external network adapter, each physical network adapter in the team is assigned a unique NDIS\_SWITCH\_NIC\_INDEX value that is greater than or equal to one.

    **Note**  In the extensible switch team configuration, every physical network adapter in the team is considered to be bound to the external network adapter.




3.  The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_CONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598262) for the external network adapter.

    **Note**  At this point, the connection to the external network is not operational and cannot be used for packet traffic.



4.  For every network adapter that is bound to the external network adapter, the protocol edge of the extensible switch issues a separate OID set request of [OID\_SWITCH\_NIC\_CONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598262). This OID request is issued after the OID set request of [OID\_SWITCH\_NIC\_CREATE](https://msdn.microsoft.com/library/windows/hardware/hh598263) is completed successfully.

    The [OID\_SWITCH\_NIC\_CONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598262) OID request notifies the extension that the extensible switch network connection is now operational. If the external network adapter is bound to the virtual miniport edge of the MUX driver, the protocol edge issues a separate OID\_SWITCH\_NIC\_CONNECT request.

    **Note**  As soon as an [OID\_SWITCH\_NIC\_CONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598262) request is issued for a physical network adapter with a NDIS\_SWITCH\_NIC\_INDEX value greater than or equal to one, the connection to the external network is operational. At this point, packet traffic can be sent or received over the external network.



5.  If the external network connection is being torn down, the protocol edge of the extensible switch first issues a separate OID set request of [OID\_SWITCH\_NIC\_DISCONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598265) for every network adapter that is bound to the external network adapter. Once these OID requests are completed, the protocol edge of the extensible switch then issues separate OID set request of [OID\_SWITCH\_NIC\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598264) for every physical network adapter that is bound to the external network adapter,

    Once all network connections to the underlying physical adapters have been disconnected and deleted, the protocol edge of the extensible switch issues [OID\_SWITCH\_NIC\_DISCONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598265) and [OID\_SWITCH\_NIC\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598264) requests to disconnect and delete the external network adapter connection.

For more information on NDIS\_SWITCH\_NIC\_INDEX values, see [Network Adapter Index Values](network-adapter-index-values.md).









