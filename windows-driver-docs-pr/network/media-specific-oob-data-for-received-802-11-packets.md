---
title: Media-Specific OOB Data for Received 802.11 Packets
description: Media-Specific OOB Data for Received 802.11 Packets
ms.assetid: 0d53a5c9-8572-457f-8aa4-8c2472932722
keywords: ["OOB data WDK Native 802.11", "media-specific OOB data WDK Native 802.11"]
---

# Media-Specific OOB Data for Received 802.11 Packets


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The miniport driver must format each received 802.11 packet as a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure, with the packet data formatted as a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure and linked to the NET\_BUFFER\_LIST structure. Each NET\_BUFFER\_LIST structure must include out-of-band (OOB) data. The OOB data specifies the attributes of the received packet that are specific to the wireless LAN (WLAN) media.

The miniport driver accesses the Native 802.11 OOB data through the [**NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568401) macro with the following parameters:

-   The *\_NBL* parameter, which has the pointer to the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure used for the received 802.11 packet.

-   The \_ *id* parameter, which has an identifier (ID) value of **MediaSpecificInformation**.

The data type for the Native 802.11 media-specific OOB data is the [**DOT11\_EXTSTA\_RECV\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff548626) structure.

In addition to media-specific OOB data, the miniport driver can access IEEE 802.1Q OOB data through the [**NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568401) macro by using the following parameters:

-   A pointer to a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure derived from the *NetBufferLists* parameter of the [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function.

-   An identifier (ID) value of **Ieee8021QNetBufferListInfo**.

For more information about IEEE 802.1Q OOB data, see [**NDIS\_NET\_BUFFER\_LIST\_8021Q\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566565).

 

 





