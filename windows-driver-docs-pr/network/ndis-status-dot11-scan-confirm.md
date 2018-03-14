---
title: NDIS_STATUS_DOT11_SCAN_CONFIRM
author: windows-driver-content
description: NDIS_STATUS_DOT11_SCAN_CONFIRM
ms.assetid: 065055c1-8fa5-46ac-827b-47e79670d10f
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_DOT11_SCAN_CONFIRM Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_DOT11\_SCAN\_CONFIRM


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

A miniport driver must make an NDIS\_STATUS\_DOT11\_SCAN\_CONFIRM indication after the 802.11 station completes an explicit scan operation that is initiated through a set request of [OID\_DOT11\_SCAN\_REQUEST](oid-dot11-scan-request.md).

The miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) to make an NDIS\_STATUS\_DOT11\_SCAN\_CONFIRM indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure through the *StatusIndication* parameter. When making this indication, the driver must set the following members of the NDIS\_STATUS\_INDICATION structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_SCAN\_CONFIRM.

-   **StatusBuffer** must be set to the address of a ULONG variable, which stores the appropriate NDIS\_STATUS\_xxxx code for the result of the scan operation.

-   **StatusBufferSize** must be set to sizeof(ULONG).

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

 

 




