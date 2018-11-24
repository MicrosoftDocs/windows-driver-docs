---
title: Handling the Reception of IP Fragments
description: Handling the Reception of IP Fragments
ms.assetid: bcda8057-db0f-420a-b7d1-c1ec5fe37882
keywords:
- non-standard packets and messages WDK TCP chimney offload , IP fragments
- IP fragments WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling the Reception of IP Fragments


\[The TCP chimney offload feature is deprecated and should not be used.\]

An offload target does not process received IPv4 or IPv6 fragments. Normally, an offload target does not receive IPv4 or IPv6 fragments on an offloaded TCP connection. An offload target should indicate any IPv4 or IPv6 fragments that it receives to the host stack through the non-offload NDIS interface by calling the [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) function. After the host stack has received all of the fragments of a fragmented IPv4 or IPv6 datagram, it assembles the datagram and forwards the TCP segment that is contained in the datagram to the offload target. The offload target processes the forwarded TCP segment and delivers the received data to the application through the TCP chimney data I/O interface.

 

 





