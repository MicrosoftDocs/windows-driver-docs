---
title: 802.1Q and 802.1p Processing on an Offloaded TCP Connection
description: 802.1Q and 802.1p Processing on an Offloaded TCP Connection
ms.assetid: 9655702e-4bec-45a1-b2a1-e2effc85a7f4
keywords:
- data I/O WDK TCP chimney offload , 802.1Q and 802.1p information
- I/O WDK TCP chimney offload , 802.1Q and 802.1p information
- received data processing WDK TCP chimney offload , 802.1Q and 802.1p information
- 802.1Q and 802.1p information WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# 802.1Q and 802.1p Processing on an Offloaded TCP Connection


\[The TCP chimney offload feature is deprecated and should not be used.\]




This section describes how an offload target processes IEEE 802.1Q and 802.1p information about an offloaded TCP connection. This section includes:

[802.1Q and 802.1p Information Supplied to an Offload Target](802-1q-and-802-1p-information-supplied-to-an-offload-target.md)

[Determining Whether to Fail an Offload Request Because of 802.1Q Information](determining-whether-to-fail-an-offload-request-because-of-802-1q-infor.md)

[Sending 802.1Q-Marked and 802.1p-Marked Packets on an Offloaded TCP Connection](sending-802-1q-marked-and-802-1p-marked-packets-on-an-offloaded-tcp-co.md)

[Receiving 802.1Q-Marked and 802.1p-Marked Packets on an Offloaded TCP Connection](receiving-802-1q-marked-and-802-1p-marked-packets-on-an-offloaded-tcp-.md)

Note that an offload target must support 802.1Q processing for offloaded TCP connections. An offload target must also support a zero virtual LAN (VLAN) tag and at least one nonzero VLAN tag per network interface.

An offload target can optionally support 802.1p.

 

 





