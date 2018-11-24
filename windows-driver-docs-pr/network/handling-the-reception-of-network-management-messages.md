---
title: Handling the Reception of Network Management Messages
description: Handling the Reception of Network Management Messages
ms.assetid: d5cdd9b9-cc67-4cdc-b919-5f26a8066b70
keywords:
- non-standard packets and messages WDK TCP chimney offload , network management messages
- network management messages WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling the Reception of Network Management Messages


\[The TCP chimney offload feature is deprecated and should not be used.\]

An offload target does not process Address Resolution Protocol (ARP), Internet Control Message Protocol (ICMP), or Routing Information Protocol (RIP) messages. Instead, an offload target forwards such messages to the host stack through the non-offload NDIS interface by calling the [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) function. The host stack processes such messages and, if necessary, updates state that has been offloaded to the offload target.

 

 





