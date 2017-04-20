---
title: General Status Indications
description: General Status Indications
ms.assetid: 5a7bed1c-3c03-4533-b8f1-ce8878bf7f86
keywords:
- general status indications WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# General Status Indications


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The Native 802.11 miniport driver can make the following general status indications:

-   [**NDIS\_STATUS\_RESET\_START**](https://msdn.microsoft.com/library/windows/hardware/ff567420)

-   [**NDIS\_STATUS\_RESET\_END**](https://msdn.microsoft.com/library/windows/hardware/ff567419)

The Native 802.11 miniport driver must not make other general status indications. In particular, the driver must not indicate its connection status through [**NDIS\_STATUS\_MEDIA\_CONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff567394) or [**NDIS\_STATUS\_MEDIA\_DISCONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff567396). The Native 802.11 framework defines various media-specific indications that the miniport driver must use instead for indicating media connection status. For more information about media-specific indications, see [Native 802.11 Status Indications](native-802-11-status-indications.md).

For more information about general status indications, see [NDIS General Status Indications](https://msdn.microsoft.com/library/windows/hardware/ff565659).

 

 





