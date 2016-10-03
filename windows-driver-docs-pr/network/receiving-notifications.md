---
title: Receiving Notifications
description: Receiving Notifications
ms.assetid: 852243b2-35b0-4c94-9b3b-9855ed1a678a
keywords: ["notifications WDK Native 802.11 IHV Extensions DLL"]
---

# Receiving Notifications


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The operating system forwards IHV-specific indications from the Native 802.11 miniport driver by calling the [*Dot11ExtIhvReceiveIndication*](https://msdn.microsoft.com/library/windows/hardware/ff547512) function. For more information about how the driver makes this type of indication, see [IHV-Specific Indications](ihv-specific-indications.md).

When the [*Dot11ExtIhvReceiveIndication*](https://msdn.microsoft.com/library/windows/hardware/ff547512) function is called, the *pvBuffer* parameter is passed a pointer to a buffer that contains data in a format defined by the IHV.

 

 





