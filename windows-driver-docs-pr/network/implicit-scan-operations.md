---
title: Implicit Scan Operations
description: Implicit Scan Operations
ms.assetid: 2163895d-f92e-4d19-9bd4-994a8e6c255f
keywords:
- scan operations WDK Native 802.11 , implicit
- implicit scan operations WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Implicit Scan Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

If the miniport driver is operating in Extensible Station (ExtSTA) mode, the 802.11 station can perform an implicit scan on its own without a preceding set request of [OID\_DOT11\_SCAN\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413). The 802.11 station determines when to perform an implicit scan operation. For example, the station might periodically perform an implicit scan operation to update its cache of detected basic service set (BSS) networks.

When performing the implicit scan operation, the 802.11 station must follow these guidelines:

-   The 802.11 station can perform the implicit scan operation on any PHY supported by the 802.11 NIC and on any channel supported by the regulatory domain in which the station is currently operating. However, the 802.11 station must perform the implicit scan operation in a way that does not seriously degrade or impair network performance.

-   The 802.11 station can use either the active or passive scan methods, or a combination of both. If it uses the active scan method, the station is free to format the 802.11 Probe Request frames that it transmits at its discretion.

-   The 802.11 station must not perform an implicit scan operation if media streaming is enabled through a set request of [OID\_DOT11\_MEDIA\_STREAMING\_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569386).

If the miniport driver's current packet filter has enabled the NDIS\_PACKET\_TYPE\_802\_11\_DIRECTED\_MGMT and NDIS\_PACKET\_TYPE\_802\_11\_BROADCAST\_MGMT filter settings, the miniport driver must call [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) for all 802.11 Beacon and Probe Response frames received by the 802.11 station. When performing the scan operation, the miniport driver must indicate these frames regardless of whether the 802.11 station received the frames as part of the scan operation. For more information about the 802.11 packet filter settings, see [OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575).

 

 





