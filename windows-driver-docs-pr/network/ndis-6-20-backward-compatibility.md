---
title: NDIS 6.20 Backward Compatibility
description: NDIS 6.20 Backward Compatibility
ms.assetid: a2d71cae-aed2-4c23-9ad2-5c32d4ab2294
keywords:
- NDIS 6.20 WDK , backward compatibility
- backward compatibility WDK NDIS 6.20
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS 6.20 Backward Compatibility





NDIS 6.20 adds backward compatibility features to those that apply to NDIS 6.0 drivers. For information about NDIS 6.0 compatibility issues, see [NDIS 6.0 Backward Compatibility](ndis-6-0-backward-compatibility.md). In addition to the translation features that NDIS 6.0 provides for NDIS 5.x and earlier drivers, NDIS 6.20 also provides translation for the power management interface. NDIS 6.20 drivers must support the NDIS 6.20 power management interface.

NDIS 6.20 supports updated versions of the features that were added for NDIS 6.1. For more information about updates to NDIS 6.1 features, see [NDIS 6.20 Support for NDIS 6.1 Features](ndis-6-20-updates-to-ndis-6-1-features.md).

**Note**  The NDIS 6.20 interface supports more than 64 processors. Previous NDIS versions are limited to no more than 64 processors (32 in x86 versions of the operating system).

 

To remain backward compatible with older NDIS versions, drivers that have not been updated to support more than 64 processors default to processor group zero. For more information about processor groups, see the Kernel-Mode Driver Architecture Design documentation for processor groups.

Some NDIS 6.1 and earlier functions are obsolete and cannot be used with NDIS 6.20 drivers. See the requirements section of the reference page for a particular function to determine its NDIS version compatibility. For a list of obsolete interfaces, see [Obsolete Interfaces in NDIS 6.20](obsolete-interfaces-in-ndis-6-20.md).

The TCP/IP protocol driver that ships with Windows 7 has been updated to NDIS 6.20. The TCP/IP protocol driver is backward compatible with NDIS 6.1 and earlier drivers in the driver stack. However, to obtain the best performance on the Windows 7 driver stack, all drivers should be updated to NDIS 6.20.

NDIS 5.x and earlier NDIS drivers are deprecated in Microsoft Windows versions after Windows 7. No new NDIS 5.x drivers will be WHQL certified. All new drivers should be NDIS 6.0 or later drivers.

IrDA miniport drivers will not be supported in Microsoft Windows versions after Windows 7.

[IPsec task offload version 1](ipsec-offload-version-1.md) will not be supported in Microsoft Windows versions after Windows 7. All drivers that support IPsec task offload should be updated to support [IPsec task offload version 2](ipsec-offload-version-2.md).

Filter intermediate drivers will not be supported in Microsoft Windows versions after Windows 7. You should use the NDIS 6.0 filter drivers interface. For more information about filter drivers, see [NDIS Filter Drivers](ndis-filter-drivers.md).

802.11 drivers that emulate 802.3 will not be supported in Microsoft Windows versions after Windows 7. NDIS 802.11 drivers must support the native 802.11 interface. For more information about native 802.11, see [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560689).

NDIS WAN drivers will not be supported in Microsoft Windows versions after Windows 7. NDIS WAN drivers must be ported to the NDIS 6.0 CoNDIS WAN driver model. For more information about CoNDIS WAN, see WAN Miniport Drivers.

ATM and Token Ring drivers will not be supported in Microsoft Windows versions after Windows 7.

 

 





