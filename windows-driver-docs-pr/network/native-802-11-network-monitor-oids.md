---
title: Native 802.11 Network Monitor OIDs
description: This section describes Native 802.11 Network Monitor OIDs and their characteristics.
keywords: ["Native 802.11 Network Monitor OIDs", "Native 802.11 WLAN Network Monitor OIDs", "WDK Native 802.11 Network Monitor OIDs", "Native 802.11 Network Monitor object identifiers"]
ms.assetid: 65B49544-04CE-49E0-98A2-47E8FF03A4AF
ms.author: windowsdriverdev
ms.date: 04/25/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 Network Monitor OIDs

>[!IMPORTANT]
> The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

This section defines the Native 802.11 object identifiers (OIDs) that are valid for set or query requests when the miniport driver is operating in Network Monitor (NetMon) mode. For more information about the NetMon operation mode, see [Network Monitor Operation Mode](network-monitor-operation-mode.md).

In the following table, these abbreviations are used to specify the requirements for Native 802.11 OID query (Q), set (S), and NDIS 6.0 method (M) requests:

- R   
Indicates that support for the object is required. The miniport driver must not fail set or query requests for the object by returning NDIS_STATUS_NOT_SUPPORTED from its [MiniportOidRequest](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.
- C   
Indicates that support for the object is conditionally required for certain hardware or software functionality. If the 802.11 station supports the functionality, the miniport driver must support query or set requests for the object. Otherwise, the miniport driver must fail the set or query requests by returning NDIS_STATUS_NOT_SUPPORTED from its [MiniportOidRequest](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

| Name                                                                                             | Q | S |
| ---                                                                                              |---|---|
| [OID_DOT11_CURRENT_CHANNEL](https://msdn.microsoft.com/library/windows/hardware/ff569127)        | C | C |
| [OID_DOT11_CURRENT_FREQUENCY](https://msdn.microsoft.com/library/windows/hardware/ff569130)      | C | C |
| [OID_DOT11_CURRENT_OPERATION_MODE](https://msdn.microsoft.com/library/windows/hardware/ff569132) | R | R |
| [OID_DOT11_CURRENT_PHY_ID](https://msdn.microsoft.com/library/windows/hardware/ff569135)         | R | R |
| [OID_DOT11_DESIRED_PHY_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569144)       | R | R |
| [OID_DOT11_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569420)             | R |   |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")