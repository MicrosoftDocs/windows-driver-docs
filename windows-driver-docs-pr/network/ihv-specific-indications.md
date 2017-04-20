---
title: IHV-Specific Indications
description: IHV-Specific Indications
ms.assetid: 6301fc2d-b409-43d0-95a0-fa6ad13192a9
keywords:
- ExtSTA status indications WDK Native 802.11
- Extensible Station status indications WDK Native 802.11
- IHV-specific indications WDK Native 802.11 miniport
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IHV-Specific Indications


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The Native 802.11 miniport driver, operating in Extensible Station (ExtSTA) mode, can make IHV-specific indications to the [Native 802.11 IHV Extensions DLL](https://msdn.microsoft.com/library/windows/hardware/ff560614). The operating system forwards these indications to the DLL by calling the [*Dot11ExtIhvReceiveIndication*](https://msdn.microsoft.com/library/windows/hardware/ff547512) IHV Handler function. If an IHV Extensions DLL is not installed, the operating system will discard the indication.

The Native 802.11 miniport driver makes an IHV-specific indication by calling the [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) function with the **StatusCode** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure set to [**NDIS\_STATUS\_MEDIA\_SPECIFIC\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567399). The **StatusBuffer** member of this structure points to a driver-allocated buffer, which. contains data in a format that is defined by the IHV.

 

 





