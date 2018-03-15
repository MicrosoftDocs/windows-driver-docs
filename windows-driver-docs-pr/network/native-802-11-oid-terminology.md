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

