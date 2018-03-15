---
title: NDIS_STATUS_DOT11_ROAMING_COMPLETION
author: windows-driver-content
description: NDIS_STATUS_DOT11_ROAMING_COMPLETION
ms.assetid: 7effcce4-e557-4255-92d4-8a1c0b3bda61
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_DOT11_ROAMING_COMPLETION Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_DOT11\_ROAMING\_COMPLETION


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

A miniport driver makes an NDIS\_STATUS\_DOT11\_ROAMING\_COMPLETION indication after the 802.11 station completes a roaming operation.

The miniport driver indicates the start of the roaming operation through the [NDIS\_STATUS\_DOT11\_ROAMING\_START](ndis-status-dot11-roaming-start.md) indication. Every NDIS\_STATUS\_DOT11\_ROAMING\_START indication made by the driver must have a corresponding NDIS\_STATUS\_DOT11\_ROAMING\_COMPLETION indication.

For more information about the roaming operation, see [Roaming Operations](https://msdn.microsoft.com/library/windows/hardware/ff570717).

The data type for this indication is the [**DOT11\_ROAMING\_COMPLETION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff548762) structure.

The [NDIS\_STATUS\_DOT11\_ROAMING\_START](ndis-status-dot11-roaming-start.md) and NDIS\_STATUS\_DOT11\_ROAMING\_COMPLETION indications define a roaming operation that is performed by the 802.11 station. The miniport driver cannot make the NDIS\_STATUS\_DOT11\_ROAMING\_COMPLETION indication unless it has made an NDIS\_STATUS\_DOT11\_ROAMING\_START indication at the beginning of the roaming operation.

The miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) to make an NDIS\_STATUS\_DOT11\_ROAMING\_COMPLETION indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure through the *StatusIndication* parameter. When making this indication, the driver must set the following members of the NDIS\_STATUS\_INDICATION structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_ROAMING\_COMPLETION.

-   **StatusBuffer** must be set to the address of a DOT11\_ROAMING\_COMPLETION\_PARAMETERS structure.

-   **StatusBufferSize** must be set to sizeof(DOT11\_ROAMING\_COMPLETION\_PARAMETERS).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the Windows operating systemss.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

 

 




