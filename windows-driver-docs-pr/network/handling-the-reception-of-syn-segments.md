---
title: Handling the Reception of SYN Segments
description: Handling the Reception of SYN Segments
ms.assetid: a6301358-0ad0-45d4-a54b-3bbc47b5c8e4
keywords:
- non-standard packets and messages WDK TCP chimney offload , SYN segments
- SYN segments WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling the Reception of SYN Segments


\[The TCP chimney offload feature is deprecated and should not be used.\]

If an offload target receives a SYN segment on an offloaded TCP connection that is in the TIME\_WAIT state, the offload target should forward the segment to the host stack through the nonoffload NDIS interface by calling the [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) function.

When an offload target receives an in-order SYN segment in any state other than TIME\_WAIT, the target must upload the connection in CLOSED state. An out-of-order SYN segment must trigger blind-reset attack mitigation.

For more information, see the [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613).

 

 





