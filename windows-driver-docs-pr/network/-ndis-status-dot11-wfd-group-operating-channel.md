---
title: NDIS_STATUS_DOT11_WFD_GROUP_OPERATING_CHANNEL
author: windows-driver-content
ms.assetid: CAEFF142-3A87-4824-A0B1-73809B64BA85
description: 
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
- NDIS_STATUS_DOT11_WFD_GROUP_OPERATING_CHANNEL Network Drivers Starting with Windows Vista
---

#  NDIS\_STATUS\_DOT11\_WFD\_GROUP\_OPERATING\_CHANNEL


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

The NDIS\_STATUS\_DOT11\_WFD\_GROUP\_OPERATING\_CHANNEL indication reports the current operating channel of a group.

The data type for this indication is the [**DOT11\_WFD\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/hh406639) structure.

The miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) to make an NDIS\_STATUS\_DOT11\_WFD\_GROUP\_OPERATING\_CHANNEL indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure through the *StatusIndication* parameter. When making this indication, the miniport driver must set the following members of the **NDIS\_STATUS\_INDICATION** structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_WFD\_GROUP\_OPERATING\_CHANNEL.

-   **StatusBuffer** must be set to the address of a [**DOT11\_WFD\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/hh406639) structure.

-   **StatusBufferSize** must be set to **sizeof**(DOT11\_WFD\_CHANNEL).

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
<td><p>Versions: Supported in Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

 

 




