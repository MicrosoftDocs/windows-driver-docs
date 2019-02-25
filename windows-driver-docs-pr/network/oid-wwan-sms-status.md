---
title: OID_WWAN_SMS_STATUS
description: OID_WWAN_SMS_STATUS reports the status of the MB device's message store.
ms.assetid: a43451e6-f589-4963-acc7-855555655d37
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_SMS_STATUS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_SMS\_STATUS


OID\_WWAN\_SMS\_STATUS reports the status of the MB device's message store.

Set requests are not supported.

Query requests do not use a structure.

Miniport drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_SMS\_STATUS**](ndis-status-wwan-sms-status.md) status notification that indicates the status of the MB device's message store when completing query requests.

Remarks
-------

For more information about using this OID, see [WWAN SMS Operations](https://msdn.microsoft.com/library/windows/hardware/ff559131).

When processing this OID, miniport drivers can access the Subscriber Identity Module (SIM card), but should not access the provider network.

Miniport drivers should return NDIS\_STATUS\_NOT\_SUPPORTED if they do not support SMS text messages.

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
<td><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[WWAN SMS Operations](https://msdn.microsoft.com/library/windows/hardware/ff559131)

[**NDIS\_STATUS\_WWAN\_SMS\_STATUS**](ndis-status-wwan-sms-status.md)

 

 




