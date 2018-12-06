---
title: NDIS 6.30 Backward Compatibility
description: NDIS 6.30 adds backward compatibility features to those that apply to NDIS 6.20 and NDIS 6.0 drivers.
ms.assetid: 71C2BBCF-206A-4C2D-BF9C-C4074FB9276D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS 6.30 Backward Compatibility


NDIS 6.30 adds backward compatibility features to those that apply to NDIS 6.20 and NDIS 6.0 drivers. For information about NDIS 6.20 compatibility issues, see [NDIS 6.20 Backward Compatibility](ndis-6-20-backward-compatibility.md). For information about NDIS 6.0 compatibility issues, see [NDIS 6.0 Backward Compatibility](ndis-6-0-backward-compatibility.md).

For more information about NDIS 6.30 features, see [Introduction to NDIS 6.30](introduction-to-ndis-6-30.md).

## Features that are no longer supported


The following features are not supported in Windows 8 and later:

-   TCP chimney offload is no longer supported for virtual machines. However, it is still supported for native use.
-   [IPsec task offload version 1](ipsec-offload-version-1.md). All drivers that support IPsec task offload should be updated to support [IPsec task offload version 2](ipsec-offload-version-2.md).
-   Filter intermediate drivers. Instead, use the NDIS 6.*x* filter driver interface. For more information about filter drivers, see [NDIS Filter Drivers](ndis-filter-drivers.md).
-   802.11 drivers that emulate 802.3. NDIS 802.11 drivers must support the native 802.11 interface. For more information about native 802.11, see [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560689).
-   NDIS WAN drivers. NDIS WAN drivers must be ported to the NDIS 6.0 CoNDIS WAN driver model. For more information about CoNDIS WAN, see [WAN Miniport Drivers](wan-miniport-drivers.md).

## Features that have been removed


The following features have been removed from Windows 8 and later:

-   NDIS 5.x and earlier
-   IrDA miniport drivers
-   NetDMA
-   Token Ring (802.5)

## Other changes


-   The TCP/IP protocol driver that ships with Windows 8 has been updated to NDIS 6.30. However, this change was relatively minor, so it's not worth porting your driver just for this feature. The TCP/IP protocol driver is backward compatible with NDIS 6.20 and earlier drivers in the driver stack.

 

 





