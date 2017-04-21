---
title: Native 802.11 Status Indications
description: Native 802.11 Status Indications
ms.assetid: f230a5a9-787a-4bcc-81ad-c001f065cf2e
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 Status Indications


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The Native 802.11 miniport driver indicates changes in hardware or software status by calling [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600). The *StatusIndication* parameter of **NdisMIndicateStatusEx** is a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure, whose members are set as follows:

<a href="" id="statuscode"></a>**StatusCode**  
Specifies the status code. The value is an NDIS\_STATUS\_XXX code. For more information about NDIS\_STATUS\_XXX codes, see [Status Indications](https://msdn.microsoft.com/library/windows/hardware/ff570879).

<a href="" id="statusbuffer"></a>**StatusBuffer**  
A pointer to a caller-allocated buffer that contains data that is specific to the indication made by the miniport driver.

<a href="" id="statusbuffersize"></a>**StatusBufferSize**  
The length, in bytes, of the buffer referenced by the *StatusBuffer* parameter.

The following topics discuss the types of indications made by the Native 802.11 miniport driver:

-   [General Status Indications](general-status-indications.md)

-   [Native 802.11 Status Indications](native-802-11-status-indications2.md)

For more information about how the miniport driver makes status indications, see [Adapter Status Indications](miniport-adapter-status-indications.md).

 

 





