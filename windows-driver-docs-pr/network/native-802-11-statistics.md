---
title: Native 802.11 Statistics
description: Native 802.11 Statistics
ms.assetid: e6bd2abf-faa2-463f-91df-a15924afae96
keywords:
- Native 802.11 miniport drivers WDK networking , statistics
- miniport drivers WDK Native 802.11 , statistics
- statistics WDK networking
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 Statistics


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The Native 802.11 miniport driver operating in Extensible Station (ExtSTA) mode returns statistical counters when the [OID\_DOT11\_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569420) object identifier (OID) is queried. The data type defined for this OID is the [**DOT11\_STATISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff548779) structure, which returns the following types of statistics:

-   Media Access Control (MAC) statistics. For more information about these statistics, see

-   [Extensible Station MAC Statistics](extensible-station-mac-statistics.md)

-   .

-   PHY statistics. For more information about these statistics, see [Extensible Station PHY Statistics](extensible-station-phy-statistics.md).

The miniport driver must unconditionally set all of the counters in the DOT11\_STATISTICS structure to zero, including MAC-layer and PHY-layer counters, when one of the following occurs:

-   The driver's

-   [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389)

-   function is called.

-   The driver's MiniportRequest function is called with a method request of the [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409), regardless of the type of reset operation specified in the method request.

 

 





