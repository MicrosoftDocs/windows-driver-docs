---
title: External Network Adapters
description: External Network Adapters
ms.assetid: 4029437C-97EA-4F21-A3F0-3B29DC650233
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# External Network Adapters


The external network adapter is exposed in the management operating system that runs in the Hyper-V parent partition. The external network adapter provides the connection to a Hyper-V external network. This network forwards packet traffic over the physical network interface of the host.

The external network is accessed by the Hyper-V parent partition and all child partitions that are connected to the extensible switch. Each instance of the extensible switch supports no more than one external network adapter connection.

The external network adapter is a virtual representation of the underlying physical network adapter on the host. The external network adapter forwards packets, object identifier (OIDs) requests, and NDIS status indications to and from one or more underlying physical network adapters.

Internally, the external network adapter binds to various configurations of underlying physical network adapters. Each of these configurations provides access to the external network interface through one or more physical network adapters. For more information about these physical adapter configurations, see [Types of Physical Network Adapter Configurations](types-of-physical-network-adapter-configurations.md).

If the extensible switch is configured to provide an external network adapter connection, the following steps occur when the switch is started:

1.  The protocol edge of the extensible switch issues an object identifier (OID) set request of [OID\_SWITCH\_PORT\_CREATE](https://msdn.microsoft.com/library/windows/hardware/hh598272) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that a port is being created for the external network adapter.

2.  The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_CREATE](https://msdn.microsoft.com/library/windows/hardware/hh598272) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that a network connection for the external network adapter is being created for the port that was previously created.

3.  The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_CONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598272) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that a network connection for the external network adapter is connected and operational. At this point, the extension can inspect, inject, and forward packets to the port that is connected to the external network adapter.

The following steps occur when the extensible switch with an external network adapter connection is stopped:

1.  The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_DISCONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598265) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that the connection to the external network adapter is being torn down.

2.  After all packet traffic and OID requests that target the network connection are completed, the protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598272) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that the connection to the external network adapter has been gracefully torn down and deleted.

3.  The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_PORT\_TEARDOWN](https://msdn.microsoft.com/library/windows/hardware/hh598279) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that the port that was used for the external network adapter connection is being torn down.

4.  The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_PORT\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598273) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that the port that was used for the external network adapter connection has been torn down and deleted.

 

 





