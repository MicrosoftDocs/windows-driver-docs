---
title: WOL Patterns for NDIS Power Management
description: WOL Patterns for NDIS Power Management
ms.assetid: 44d49fe9-0983-4753-8f6f-f3445b5b9f3b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WOL Patterns for NDIS Power Management





Starting with NDIS 6.20, Wake-on-LAN (WOL) patterns are supported for the *wake on pattern match* method. This WOL method minimizes spurious wake-up events and ensures that the computer is brought back to running state when expected. The interface for WOL patterns identifies specific patterns that are based on the packet type (for example, TCP SYN packets on IPv4). Specific patterns provide reliable pattern matches.

There are two types of WOL patterns:

<a href="" id="wol-packet-"></a>WOL packet   
A packet in which the wake-up pattern defines a specific packet type (such as TCP SYN on IPv4).

<a href="" id="wol-bitmap-"></a>WOL bitmap   
A WOL pattern that is specified with an offset and bitmap.

**Note**  NDIS 6.20 and later versions of NDIS also support the *wake on magic packet* method. This method is separate from the *wake on pattern match* method.

 

Starting with NDIS 6.20, multiple protocol drivers can set WOL patterns on a network adapter. To ensure that the correct set of WOL patterns is set when the number of requested WOL patterns is higher than the number that the network adapter can support, protocol drivers assign a priority to each WOL pattern. When NDIS cannot add a new high-priority WOL pattern because the network adapter is out of resources, NDIS can delete the lower priority patterns.

For more information about managing WOL patterns, see [Adding and Deleting Wake on LAN Patterns](adding-and-deleting-wake-on-lan-patterns.md).

For more information about WOL methods supported in NDIS 6.20 and later versions, see [WOL Methods in NDIS 6.20](introduction-to-ndis-6-20.md).

 

 





