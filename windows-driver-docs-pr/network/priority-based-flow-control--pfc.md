---
title: Priority-based Flow Control (PFC)
description: Priority-based Flow Control (PFC)
ms.assetid: 9DD8A66F-273F-4E5A-99EF-33C2EDF3240C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Priority-based Flow Control (PFC)


Priority-based Flow Control (PFC) is specified in the IEEE 802.1Qbb draft standard. This standard is part of the framework for the IEEE 802.1 Data Center Bridging (DCB) interface.

PFC enables flow control over a unified 802.3 Ethernet media interface, or *fabric*, for local area network (LAN) and storage area network (SAN) technologies. PFC is intended to eliminate packet loss due to congestion on a network link. This allows loss-sensitive protocols, such as Fibre Channel over Ethernet (FCoE), to coexist with traditional loss-insensitive protocols over the same unified fabric.

PFC specifies a link-layer flow control mechanism between directly connected peers. PFC is similar to IEEE 802.3 PAUSE frames but operates on individual 802.1p priority levels instead. This allows a receiver to pause a transmitter on any 802.1p priority level.

PFC uses the 802.3 PAUSE frame, and extends it with the following PFC fields:

-   An 8-bit mask that specifies which 802.1p priority levels should be paused.

-   A timer value for each priority specifying how long the traffic for that priority level should be paused.

When the receiver sends an 802.3 PAUSE frame with PFC data, the switch blocks the transmit of frames with the specified priority level to the port on which the receiver is connected. When the timer value expires, the switch resumes the transmit of paused frames on the port.

NDIS Quality of Service (QoS) parameters are specified through the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure. The **PfcEnable** member contains a bitmap, in which each bit specifies whether PFC is enabled for a 802.1p priority level.

For more information about priority levels, see [IEEE 802.1p Priority Levels](ieee-802-1p-priority-levels.md).

 

 





