---
title: OID_WWAN_SUBSCRIBE_DEVICE_SERVICE_EVENTS
description: OID_WWAN_SUBSCRIBE_DEVICE_SERVICE_EVENTS sets information about the list of device services for which the MB device must send NDIS_STATUS_WWAN_DEVICE_SERVICE_EVENT notifications.
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_SUBSCRIBE_DEVICE_SERVICE_EVENTS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_SUBSCRIBE\_DEVICE\_SERVICE\_EVENTS


OID\_WWAN\_SUBSCRIBE\_DEVICE\_SERVICE\_EVENTS sets information about the list of device services for which the MB device must send [**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_EVENT**](./ndis-status-wwan-device-service-event.md) notifications. The MB device should not indicate events for any device service which is not in this list.

Miniport drivers must process set requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending a [**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SUBSCRIPTION**](./ndis-status-wwan-device-service-subscription.md) status notification that contains the current list of event subscriptions on the MB device.

Callers requesting to set the MB device service event subscription list provide a [**NDIS\_WWAN\_SUBSCRIBE\_DEVICE\_SERVICE\_EVENTS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_subscribe_device_service_events) structure to the miniport driver with the appropriate information.

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


[**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_EVENT**](./ndis-status-wwan-device-service-event.md)

[**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SUBSCRIPTION**](./ndis-status-wwan-device-service-subscription.md)

[**NDIS\_WWAN\_SUBSCRIBE\_DEVICE\_SERVICE\_EVENTS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_subscribe_device_service_events)

 

