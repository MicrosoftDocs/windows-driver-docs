---
title: Other Native 802.11 indications
description: Other Native 802.11 indications
ms.assetid: 22905775-faef-43b9-ad46-8cfe8f630e31
keywords:
- Native 802.11 miniport drivers WDK networking , status indications
- miniport drivers WDK Native 802.11 , status indications
- status indications WDK networking , Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Other Native 802.11 indications


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Most of the indications made by the Native 802.11 miniport driver are specific to the Native 802.11 media. For example, a miniport driver can make a Native 802.11 indication whenever:

-   The 802.11 station has completed a scan request initiated through [OID\_DOT11\_SCAN\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413).

-   The maximum length is changed for 802.11 media access control (MAC) protocol data unit (MPDU) frames.

The miniport driver makes a Native 802.11 indication by calling [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600). The *StatusIndication* parameter of **NdisMIndicateStatusEx** is a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure, whose members are set as follows:

<a href="" id="statuscode"></a>**StatusCode**  
This member specifies the NDIS\_STATUS\_DOT11\_XXX status code for the indication. These status code values are define in Ndis.h. For more information about NDIS\_STATUS\_DOT11\_XXX codes, see [Status Indications](https://msdn.microsoft.com/library/windows/hardware/ff570879)

<a href="" id="statusbuffer"></a>**StatusBuffer**  
A pointer to a caller-allocated buffer that contains data that is specific to the indication made by the miniport driver.

<a href="" id="statusbuffersize"></a>**StatusBufferSize**  
The length, in bytes, of the buffer referenced by the *StatusBuffer* parameter.

The following topics describe the types of Native 802.11 indications:

[General Native 802.11 Indications](general-native-802-11-indications.md)

[Extensible AP Status Indications](https://msdn.microsoft.com/library/windows/hardware/ff560598)

[Extensible Station Indications](extensible-station-indications.md)

 

 





