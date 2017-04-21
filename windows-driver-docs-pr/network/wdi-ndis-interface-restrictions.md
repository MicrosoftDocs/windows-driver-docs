---
title: WDI NDIS interface restrictions
description: The WDI IHV miniport driver has access to all of the functionality provided by NDIS and KMDF.
ms.assetid: 08996045-674B-465D-8880-088320770D2C
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDI NDIS interface restrictions


The WDI IHV miniport driver has access to all of the functionality provided by NDIS and KMDF. It is recommended that the IHV driver use the KMDF primitives for talking to the rest of the operating system whenever possible. While the model does not restrict the IHV miniport from calling any of the NDIS APIs, some NDIS APIs are called by the Microsoft WLAN component so the IHV driver should not call them.

The WDI IHV miniport driver needs to be aware of the following restrictions on NDIS interfaces.

Function
[**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654)
**Restrictions:**
Disallowed
*Alternative:*
[**NdisMRegisterWdiMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/mt297596)
[**NdisMDeregisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563578)
**Restrictions:**
Disallowed
*Alternative:*
[**NdisMDeregisterWdiMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/mt297595)
[**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672)
**Restrictions:**
Disallowed with **MiniportAttributes** types:
[**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565934)
[**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923)
[**NDIS\_MINIPORT\_ADAPTER\_NATIVE\_802\_11\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565926)
*Alternative:*
None. These are queried using WDI commands.
[**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598)
**Restrictions:**
Disallowed
*Alternative:*
The WDI data path receive handler to indicate received packets.
[**NdisMSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563668)
**Restrictions:**
Disallowed
*Alternative:*
The WDI data path send handler to complete sent packets.
 

 

 





