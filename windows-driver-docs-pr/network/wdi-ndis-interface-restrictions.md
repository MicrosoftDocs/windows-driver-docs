---
title: WDI NDIS interface restrictions
description: The WDI IHV miniport driver has access to all of the functionality provided by NDIS and KMDF.
ms.assetid: 08996045-674B-465D-8880-088320770D2C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI NDIS interface restrictions


The WDI IHV miniport driver has access to all of the functionality provided by NDIS and KMDF. It is recommended that the IHV driver use the KMDF primitives for talking to the rest of the operating system whenever possible. While the model does not restrict the IHV miniport from calling any of the NDIS APIs, some NDIS APIs are called by the Microsoft WLAN component so the IHV driver should not call them.

The WDI IHV miniport driver needs to be aware of the following restrictions on NDIS interfaces.

Function | Restrictions | Alternative 
---|---|--- 
[**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) | Disallowed |  [**NdisMRegisterWdiMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/mt297596) 
[**NdisMDeregisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563578) | Disallowed |  [**NdisMDeregisterWdiMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/mt297595) 
[**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) | Disallowed with **MiniportAttributes** types:<br />[**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565934)<br />[**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923)<br />[**NDIS\_MINIPORT\_ADAPTER\_NATIVE\_802\_11\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565926) | None. These are queried using WDI commands. 
[**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) | Disallowed | The WDI data path receive handler to indicate received packets. 
[**NdisMSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563668) | Disallowed | The WDI data path send handler to complete sent packets.

 





