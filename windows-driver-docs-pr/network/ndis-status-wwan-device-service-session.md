---
title: NDIS_STATUS_WWAN_DEVICE_SERVICE_SESSION
ms.topic: reference
description: Miniport drivers use the NDIS_STATUS_WWAN_DEVICE_SERVICE_SESSION indication to report the completion of a device service session state change originated by OID_WWAN_DEVICE_SERVICE_SESSION.NDIS_WWAN_DEVICE_SERVICE_SESSION_INFO structure.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WWAN_DEVICE_SERVICE_SESSION Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SESSION


Miniport drivers use the NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SESSION indication to report the completion of a device service session state change originated by [OID\_WWAN\_DEVICE\_SERVICE\_SESSION](./oid-wwan-device-service-session.md).

Miniport drivers cannot use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_DEVICE\_SERVICE\_SESSION\_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_service_session_info) structure.

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


[OID\_WWAN\_DEVICE\_SERVICE\_SESSION](./oid-wwan-device-service-session.md)

[**NDIS\_WWAN\_DEVICE\_SERVICE\_SESSION\_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_service_session_info)

 

