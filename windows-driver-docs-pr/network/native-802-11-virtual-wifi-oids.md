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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")