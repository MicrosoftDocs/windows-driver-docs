---
title: Native 802.11 Virtual WiFi OIDs
description: This section describes Native 802.11 Virtual WiFi OIDs and their characteristics.
keywords: ["Native 802.11 Virtual WiFi OIDs", "Native 802.11 WLAN Virtual WiFi OIDs", "WDK Native 802.11 Virtual WiFi OIDs", "Native 802.11 Virtual WiFi object identifiers"]
ms.assetid: B2D106FF-3FDF-4382-B76E-2C815917DD29
ms.author: windowsdriverdev
ms.date: 04/26/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 Virtual WiFi OIDs

>[!IMPORTANT]
> The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

The Native 802.11 Virtual Wireless Fidelity (Virtual WiFi) object identifiers (OIDs) are applicable only to miniport drivers that support the Native 802.11 Virtual WiFi operation mode.

>[!NOTE]
>The Native 802.11 Virtual WiFi operation mode is available in Windows 7 and later versions of the Windows operating systems.

In the following table, the R abbreviation specifies the requirements for Native 802.11 Extensible AP (ExtAP) OID query (Q), set (S), and NDIS 6.0 method (M) requests:

- R   
Indicates that support for the object is required. The miniport driver must not fail set or query requests for the object by returning NDIS_STATUS_NOT_SUPPORTED from its [MiniportOidRequest](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.
- O   
Indicates that support for the object is optional. The miniport driver can either support query or set requests for the object, or the driver can fail the request by returning NDIS_STATUS_NOT_SUPPORTED from its [MiniportOidRequest](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

| Name                                                                                                 | Q | S | M |
|---                                                                                                   |---|---|---|
| [OID_DOT11_CREATE_MAC](https://msdn.microsoft.com/library/windows/hardware/ff569124)                 |   |   | R |
| [OID_DOT11_DELETE_MAC](https://msdn.microsoft.com/library/windows/hardware/ff569140)                 |   | R |   |
| [OID_DOT11_VIRTUAL_STATION_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569435) | O |   |   |

