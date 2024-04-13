---
title: OID_WWAN_SMS_STATUS
ms.topic: reference
description: OID_WWAN_SMS_STATUS reports the status of the MB device's message store.
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_SMS_STATUS Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_SMS\_STATUS


OID\_WWAN\_SMS\_STATUS reports the status of the MB device's message store.

Set requests are not supported.

Query requests do not use a structure.

Miniport drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_SMS\_STATUS**](ndis-status-wwan-sms-status.md) status notification that indicates the status of the MB device's message store when completing query requests.

## Remarks

For more information about using this OID, see [WWAN SMS Operations](./mb-sms-operations.md).

When processing this OID, miniport drivers can access the Subscriber Identity Module (SIM card), but should not access the provider network.

Miniport drivers should return NDIS\_STATUS\_NOT\_SUPPORTED if they do not support SMS text messages.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[WWAN SMS Operations](./mb-sms-operations.md)

[**NDIS\_STATUS\_WWAN\_SMS\_STATUS**](ndis-status-wwan-sms-status.md)

 

