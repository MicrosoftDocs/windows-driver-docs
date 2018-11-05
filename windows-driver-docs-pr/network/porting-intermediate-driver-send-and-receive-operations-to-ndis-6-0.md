---
title: Porting intermediate driver send and receive to NDIS 6.0
description: Porting Intermediate Driver Send and Receive Operations to NDIS 6.0
ms.assetid: e7d4d7b7-e467-4af5-9a68-e272f6859653
keywords:
- porting intermediate drivers WDK networking , send and receive operations
- send operation porting WDK networking
- receive operation porting WDK networking
- data send/receive operation porting WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Intermediate Driver Send and Receive Operations to NDIS 6.0





Like NDIS 5.*x* intermediate drivers, NDIS 6.0 intermediate drivers can originate or forward send requests and receive indications.

However, data transfer code paths in NDIS 6.0 have changed in the following ways:

-   The [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures and [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures replace the [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structure.

-   Drivers can send and receive multiple packets in a single call without determining the number of packets beforehand because the packets are provided in a linked list of NET\_BUFFER structures instead of an array of NDIS\_PACKET structures.

-   The completion status of a send or receive operation is indicated in the **Status** member of the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. This completion status is not returned as a function return code or a parameter of the [**ProtocolSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570268) or [**NdisMSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563668) function.

-   The TCP/IP stack that is included in Windows Vista guarantees that all [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures in a NET\_BUFFER\_LIST structure are targeted for the same MAC address, IP address, and TCP port. Intermediate drivers are required to provide the same behavior on TCP/IP data sent to underlying drivers.

-   All send and receive operations are asynchronous.

Intermediate drivers must specify backfill requirements. The intermediate driver receives backfill requirements from underlying drivers in the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) or restart attributes. The intermediate driver specifies its backfill size requirements for its virtual miniports in the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure or restart attributes. The driver adds its backfill size requirement to the size that the underlying drivers reported.

NDIS 4.0 and 5.0 intermediate drivers must allocate a new [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structure to encapsulate data that they pass on. These intermediate drivers must also copy any out-of-band (OOB) data to the new packet. NDIS 5.1 intermediate drivers that support packet stacking avoid this extra data handling in most common cases. NDIS 6.0 provides context information with the NET\_BUFFER\_LIST and eliminates the need for packet stacking.

NDIS 6.0 also provides the ability to clone, fragment, and reassemble [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures. For more information about cloning, fragmenting, and reassembling NET\_BUFFER\_LIST structures, see [Derived NET\_BUFFER\_LIST Structures](derived-net-buffer-list-structures.md)

NDIS 6.0 filter drivers can bypass send and receive operations to improve system performance. For more information about filter drivers, see [NDIS 6.0 Filter Drivers](ndis-filter-drivers.md).

For more information about send and receive operations in the miniport upper edge of an intermediate driver, see [Porting Miniport Driver Send and Receive Operations to NDIS 6.0](porting-miniport-driver-send-and-receive-operations-to-ndis-6-0.md).

For more information about send and receive operations in the protocol lower edge of an intermediate driver, see [Porting Protocol Driver Send and Receive Operations to NDIS 6.0](porting-protocol-driver-send-and-receive-operations-to-ndis-6-0.md).

 

 





