---
title: NDIS 6.0 Backward Compatibility
description: NDIS 6.0 Backward Compatibility
ms.assetid: d03fa7b2-06d4-44b1-8b3f-a366c21ddd63
keywords:
- NDIS WDK , backward compatibility
- backward compatibility WDK networking
- compatibility WDK networking
- NDIS porting drivers WDK , backward compatibility
- porting drivers WDK networking , backward compatibility
- network driver porting WDK , backwar
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS 6.0 Backward Compatibility





The Windows Vista operating system supports NDIS 3.0 - 5.*x* miniport drivers and NDIS 4.0 - NDIS 5.*x* protocol and intermediate drivers. However, for longevity and improved performance, new drivers should be native NDIS 6.0 drivers. NDIS 6.0 provides a translation layer to accommodate drivers that are based on NDIS 3.0 - 5.*x*, but the translation might degrade system performance--particularly in the send and receive code paths. For more information about NDIS 6.0 send and receive code paths, see [Send and Receive Operations](send-and-receive-operations.md).

Because of the translation layer, NDIS 3.0 - 5.*x* and NDIS 6.0 drivers can exist in the same driver stack. However, the NDIS 3.0 - 5.*x* drivers do not benefit from the added features and performance of NDIS 6.0. For more information about the NDIS 6.0 driver stack, see [Driver Stack Management](driver-stack-management.md).

The TCP/IP protocol driver that ships with Windows Vista is updated to NDIS 6.0. Therefore, this driver does not require a translation layer to interface with the miniport drivers that are based on NDIS 6.0. If there are pre-NDIS 6.0 drivers in the stack, the translation might degrade system performance.

NDIS 4.0 - NDIS 5.*x* filter intermediate drivers are not recommended on Windows Vista and native NDIS 6.0 filter intermediate drivers are not supported, so you should use the NDIS 6.0 filter drivers interface. For more information about filter drivers, see [NDIS 6.0 Filter Drivers](ndis-filter-drivers.md).

Some NDIS 5.*x* and earlier functions are obsolete and cannot be used with NDIS 6.0 drivers. See the reference page for particular functions to determine their NDIS version compatibility.

Windows Vista does not currently support NDIS 6.0 IrDA miniport drivers, but Windows Vista does support NDIS 5.*x* versions of these drivers.

NDIS 6.0 does not support 802.11 drivers that emulate 802.3. However, for backward compatibility, Windows Vista supports NDIS 5.*x* versions of these drivers. NDIS 6.0 802.11 drivers must support the native 802.11 interface. For more information about native 802.11, see [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560689).

Windows Vista does not support NDIS WAN drivers for NDIS versions later than NDIS 4.0. However, for backward compatibility, Windows Vista supports NDIS WAN drivers that were written to the NDIS 4.0 specifications. To support the features that later NDIS versions provide, NDIS WAN drivers must be ported to the NDIS 6.0 CoNDIS WAN driver model. For more information about CoNDIS WAN, see [WAN Miniport Drivers](wan-miniport-drivers.md).

NDIS 6.0 does not support ATM and Token Ring drivers, but NDIS 3.0 - NDIS 5.*x* versions of these drivers are supported on Windows Vista.

Windows Vista does not support any versions of FDDI, ARCNET, or serialized intermediate drivers.

 

 





