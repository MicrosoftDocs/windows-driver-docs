---
title: Internal Network Adapters
description: Internal Network Adapters
ms.assetid: 4E4B0EC9-8E4C-47FC-B608-EC6D18367A79
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Internal Network Adapters


The internal network adapter is exposed in the management operating system that runs in the Hyper-V parent partition. This type of network adapter provides access to an extensible switch for processes that run in the management operating system. This allows these processes to send or receive packets over the extensible switch.

If the extensible switch is configured to provide an internal network adapter connection, the following steps occur when the switch is started:

1.  The protocol edge of the extensible switch issues an object identifier (OID) set request of [OID\_SWITCH\_PORT\_CREATE](https://msdn.microsoft.com/library/windows/hardware/hh598272) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that a port is being created for the internal network adapter

2.  The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_CREATE](https://msdn.microsoft.com/library/windows/hardware/hh598272) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that a network connection for the internal network adapter is being created for the port that was previously created.

3.  The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_CONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598272) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that a network connection for the internal network adapter is connected and operational. At this point, the extension can inspect, inject, and forward packets to the port that is connected to the internal network adapter.

The following steps occur when the extensible switch with an internal network adapter connection is stopped:

1.  The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_DISCONNECT](https://msdn.microsoft.com/library/windows/hardware/hh598265) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that the connection to the external network adapter is being torn down.

2.  After all packet traffic and OID requests that target the network connection are completed, the protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_NIC\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598272) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that the connection to the external network adapter has been gracefully torn down and deleted.

3.  The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_PORT\_TEARDOWN](https://msdn.microsoft.com/library/windows/hardware/hh598279) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that the port that was used for the external network adapter connection is being torn down.

4.  The protocol edge of the extensible switch issues an OID set request of [OID\_SWITCH\_PORT\_DELETE](https://msdn.microsoft.com/library/windows/hardware/hh598273) down the extensible switch driver stack. This OID request notifies the underlying extensible switch extensions that the port that was used for the internal network adapter connection has been torn down and deleted.

 

 





