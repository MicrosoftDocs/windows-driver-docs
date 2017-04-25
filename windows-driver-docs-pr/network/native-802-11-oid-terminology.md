---
title: Native 802.11 OID terminology
description: This section describes terminology for Native 802.11 OIDs.
keywords: ["Native 802.11 OIDs", "Native 802.11 WLAN OIDs", "WDK Native 802.11 IDs", "Native 802.11 object identifiers", "Native 802.11 OID terminology", "Native 802.11 terminology"]
ms.assetid: F7F753B3-524A-4A90-9DFD-AFD40B167296
ms.author: windowsdriverdev
ms.date: 04/24/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 OID terminology

>[!IMPORTANT]
> The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

The Native 802.11 OID documentation uses the following terms to indicate functionality implemented by the wireless LAN (WLAN) software and hardware:

| Term | Meaning | 
| --- | --- |
| Miniport driver | Functionality implemented by miniport driver only |
| Network interface card (NIC) | Functionality implemented by NIC hardware only |
| 802.11 Station | Functionality implemented by miniport driver or NIC firmware/hardware |

The Native 802.11 interface defines scalar data types using the following reverse-Hungarian notation:

| Prefix | Data type | 
| --- | --- |
| b | BOOLEAN |
| u | ULONG |
| us | USHORT |
| uc | UCHAR |
| ull | ULONGLONG |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")