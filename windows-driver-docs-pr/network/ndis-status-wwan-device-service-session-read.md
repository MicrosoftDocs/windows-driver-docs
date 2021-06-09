---
title: NDIS_STATUS_WWAN_DEVICE_SERVICE_SESSION_READ
description: Miniport drivers use the NDIS_STATUS_WWAN_DEVICE_SERVICE_SESSION_READ notification to inform the MB Service that data has been received from an open device service session.NDIS_WWAN_DEVICE_SERVICE_SESSION_READ structure.
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WWAN_DEVICE_SERVICE_SESSION_READ Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SESSION\_READ


Miniport drivers use the NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SESSION\_READ notification to inform the MB Service that data has been received from an open device service session.

Miniport drivers can only use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_DEVICE\_SERVICE\_SESSION\_READ**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_service_session_read) structure.

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


[**NDIS\_WWAN\_DEVICE\_SERVICE\_SESSION\_READ**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_service_session_read)

 

