---
title: NDIS_STATUS_WWAN_DEVICE_SERVICE_EVENT
ms.topic: reference
description: Miniport drivers use the NDIS_STATUS_WWAN_DEVICE_SERVICE_EVENT indication to notify the MB Service of device service changes.NDIS_WWAN_DEVICE_SERVICE_EVENT structure.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WWAN_DEVICE_SERVICE_EVENT Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_EVENT


Miniport drivers use the NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_EVENT indication to notify the MB Service of device service changes.

Miniport drivers can only use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_DEVICE\_SERVICE\_EVENT**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_service_event) structure.

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


[**NDIS\_WWAN\_DEVICE\_SERVICE\_EVENT**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_service_event)

 

