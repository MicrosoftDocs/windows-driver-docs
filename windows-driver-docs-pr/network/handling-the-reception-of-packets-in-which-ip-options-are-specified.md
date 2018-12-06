---
title: Handling receiving packets in which IP options are specified
description: Handling the Reception of Packets in Which IP Options are Specified
ms.assetid: 198c0ea6-41ce-4bdf-973c-1608e4fe1f1d
keywords:
- non-standard packets and messages WDK TCP chimney offload , IP options specified
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling the Reception of Packets in Which IP Options are Specified


\[The TCP chimney offload feature is deprecated and should not be used.\]

The host stack does not offload TCP connections that require the processing of IPv4 options. If an offload target receives an IPv4 datagram that has IP options set, it must indicate that datagram to the host stack through the non-offload NDIS interface by calling the [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) function. The host stack processes the IP options and forwards the TCP segment that is contained in the datagram to the offload target's [*MiniportTcpOffloadForward*](https://msdn.microsoft.com/library/windows/hardware/ff559458) function. The offload target processes the forwarded TCP segment and delivers the received data to the application through the TCP chimney's data I/O interface.

 

 





