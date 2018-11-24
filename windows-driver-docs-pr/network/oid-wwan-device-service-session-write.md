---
title: OID_WWAN_DEVICE_SERVICE_SESSION_WRITE
description: OID_WWAN_DEVICE_SERVICE_SESSION_WRITE directs the miniport driver to write data to the MB device for a device service session.NDIS_STATUS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE status notification containing a NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE structure that describes the completion status of the operation.
ms.assetid: C1389D7D-3C8E-41B5-8E00-617D699699A2
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_DEVICE_SERVICE_SESSION_WRITE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE


OID\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE directs the miniport driver to write data to the MB device for a device service session.

Query requests are not supported.

Miniport drivers must process set requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending a [**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh846208) status notification containing a [**NDIS\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh831861) structure that describes the completion status of the operation.

Miniport drivers should return NDIS\_STATUS\_ADAPTER\_NOT\_OPEN if the device service session is not open.

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
<td><p>Versions: Supported in Windows 8 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh846208)

[**NDIS\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/hh831860)

 

 




