---
title: Native 802.11 Media Streaming
description: Native 802.11 Media Streaming
ms.assetid: 818ad430-b87b-4c51-8d48-0dff9d9269ad
keywords:
- send operations WDK Native 802.11
- receive operations WDK Native 802.11
- media streaming WDK , Native 802.11
- streaming data WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 Media Streaming


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

A Native 802.11 miniport driver must support the streaming of data over the wireless LAN (WLAN) media. Media streaming is enabled or disabled through an OID set request of [OID\_DOT11\_MEDIA\_STREAMING\_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569386).

When media streaming is enabled, the 802.11 station must follow these guidelines.

-   While connected to a basic service set (BSS) network, the 802.11 station must not do anything that can negatively affect the latency or bandwidth of the current association with an access point (AP) or peer station.

    For example, the 802.11 station must not perform an implicit scan operation using any PHY within the active PHY list while media streaming is enabled. For more information about the active PHY list, see [OID\_DOT11\_ACTIVE\_PHY\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569102).

    **Note**  If the 802.11 station supports multiple PHYs, it can perform an implicit scan operation using a PHY that is not in the active PHY list. This is possible as long as that PHY does not use a radio that is used by a PHY in the active PHY list.

     

-   If [OID\_DOT11\_SCAN\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413) is set, the 802.11 stations must perform an explicit scan operation on all PHYs specified in the set request.

-   If the 802.11 station loses connectivity with the BSSID that it is connected to, the station can perform an implicit scan operation by using any supported PHY prior to roaming to a new BSSID.

For more information about the explicit and implicit scan operations, see [Native 802.11 Scan Operations](native-802-11-scan-operations.md).

After media streaming is enabled, the miniport driver must operate in this mode until one of the following occurs.

-   Media streaming is explicitly disabled through an OID set request of [OID\_DOT11\_MEDIA\_STREAMING\_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569386).

-   The miniport driver's [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) function is called.

-   A method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) object identifier (OID) is made.

 

 





