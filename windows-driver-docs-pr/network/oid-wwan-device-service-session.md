---
title: OID_WWAN_DEVICE_SERVICE_SESSION
ms.topic: reference
description: OID_WWAN_DEVICE_SERVICE_SESSION directs a miniport driver to open or close a device service session.NDIS_STATUS_WWAN_DEVICE_SERVICE_SESSION status notification containing a NDIS_WWAN_SET_DEVICE_SERVICE_SESSION structure that describes the result of the operation.
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_DEVICE_SERVICE_SESSION Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_DEVICE\_SERVICE\_SESSION


OID\_WWAN\_DEVICE\_SERVICE\_SESSION directs a miniport driver to open or close a device service session.

Query requests are not supported.

Miniport drivers must process set requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending a [**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SESSION**](./ndis-status-wwan-device-service-session.md) status notification containing a [**NDIS\_WWAN\_SET\_DEVICE\_SERVICE\_SESSION**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_set_service_session) structure that describes the result of the operation.

Miniport drivers should return NDIS\_STATUS\_NOT\_SUPPORTED if they do not support specified device service or operation.

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


[**NDIS\_WWAN\_SET\_DEVICE\_SERVICE\_SESSION**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_set_service_session)

[**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SESSION**](./ndis-status-wwan-device-service-session.md)

 

