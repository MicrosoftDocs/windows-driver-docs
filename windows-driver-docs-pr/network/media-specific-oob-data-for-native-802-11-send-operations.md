---
title: Media-Specific OOB Data for Native 802.11 Send Operations
description: Media-Specific OOB Data for Native 802.11 Send Operations
ms.assetid: c6bdd0b7-6f33-48bd-a736-9e1588ab91a7
keywords:
- OOB data WDK Native 802.11
- media-specific OOB data WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Media-Specific OOB Data for Native 802.11 Send Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Each packet sent by the 802.11 station through calls to the [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function has out-of-band (OOB) data. The OOB data contains media-specific parameters that the 802.11 station uses when transmitting the packet.

The miniport driver accesses the Native 802.11 OOB data through the [**NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568401) macro with the following parameters:

-   The *\_NBL* parameter, which has the pointer to the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure used for the received 802.11 packet.

-   The \_ *id* parameter, which has an identifier (ID) value of **MediaSpecificInformation**.

The data type for the Native 802.11 media-specific OOB data is the [**DOT11\_EXTSTA\_SEND\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff548632) structure.

In addition to media-specific OOB data, the miniport driver can access IEEE 802.1Q OOB data through the [**NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568401) macro using the following parameters:

-   A pointer to a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure derived from the *NetBufferLists* parameter of the [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function.

-   An identifier (ID) value of **Ieee8021QNetBufferListInfo**.

For more information about IEEE 802.1Q OOB data, see [**NDIS\_NET\_BUFFER\_LIST\_8021Q\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566565).

 

 





