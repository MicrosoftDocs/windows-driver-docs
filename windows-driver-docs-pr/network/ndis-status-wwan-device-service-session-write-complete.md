---
title: NDIS_STATUS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE
ms.topic: reference
description: Miniport drivers use the NDIS_STATUS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE notification to report the status of a write operation on a device service session.NDIS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE structure.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WWAN_DEVICE_SERVICE_SESSION_WRITE_COMPLETE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE\_COMPLETE


Miniport drivers use the NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE\_COMPLETE notification to report the status of a write operation on a device service session.

Miniport drivers cannot use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE\_COMPLETE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_service_session_write_complete) structure.

## Requirements

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
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_DEVICE\_SERVICE\_SESSION\_WRITE\_COMPLETE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_service_session_write_complete)

 

