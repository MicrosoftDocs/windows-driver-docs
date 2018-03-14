---
title: NDIS_STATUS_DOT11_WFD_INVITATION_REQUEST_SEND_COMPLETE
author: windows-driver-content
ms.assetid: 8BAD2F9D-F518-43DF-A7DE-95E707EAB5D5
description: 
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_DOT11_WFD_INVITATION_REQUEST_SEND_COMPLETE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_DOT11\_WFD\_INVITATION\_REQUEST\_SEND\_COMPLETE


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

The status of an invitation request transmission is reported with an NDIS\_STATUS\_DOT11\_WFD\_INVITATION\_REQUEST\_SEND\_COMPLETE indication. An invitation request is initiated by an [OID\_DOT11\_WFD\_SEND\_INVITATION\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh451806) OID.

The data type for this indication is the [**DOT11\_INVITATION\_REQUEST\_SEND\_COMPLETE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406484) structure.

The miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) to make an NDIS\_STATUS\_DOT11\_WFD\_INVITATION\_REQUEST\_SEND\_COMPLETE indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure through the *StatusIndication* parameter. When making this indication, the miniport driver must set the following members of the **NDIS\_STATUS\_INDICATION** structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_WFD\_INVITATION\_REQUEST\_SEND\_COMPLETE.

-   **StatusBuffer** must be set to the address of a [**DOT11\_INVITATION\_REQUEST\_SEND\_COMPLETE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406484) structure.

-   **StatusBufferSize** must be set to the total of both the size of [**DOT11\_INVITATION\_REQUEST\_SEND\_COMPLETE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406484) and the size of the list of returned Information Elements (IEs).

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
<td><p>Supported starting with Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**DOT11\_INVITATION\_REQUEST\_SEND\_COMPLETE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406484)

[OID\_DOT11\_WFD\_SEND\_INVITATION\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh451806)

 

 




