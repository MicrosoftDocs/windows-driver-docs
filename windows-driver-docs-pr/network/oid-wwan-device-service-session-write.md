---
title: OID_WWAN_DEVICE_SERVICE_SESSION_WRITE
description: OID_WWAN_DEVICE_SERVICE_SESSION_WRITE directs the miniport driver to write data to the MB device for a device service session.NDIS_STATUS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE status notification containing a NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE structure that describes the completion status of the operation.
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_DEVICE_SERVICE_SESSION_WRITE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE


OID\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE directs the miniport driver to write data to the MB device for a device service session.

Query requests are not supported.

Miniport drivers must process set requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending a [**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE\_COMPLETE**](./ndis-status-wwan-device-service-session-write-complete.md) status notification containing a [**NDIS\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE\_COMPLETE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_service_session_write_complete) structure that describes the completion status of the operation.

Miniport drivers should return NDIS\_STATUS\_ADAPTER\_NOT\_OPEN if the device service session is not open.

## Requirements

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


[**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE\_COMPLETE**](./ndis-status-wwan-device-service-session-write-complete.md)

[**NDIS\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_service_session_write)

 

