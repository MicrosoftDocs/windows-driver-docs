---
title: OID_WWAN_SMS_DELETE
description: OID_WWAN_SMS_DELETE deletes SMS text messages stored in the MB device, or Subscriber Identity Module (SIM card), or any other auxiliary non-volatile memory or memories.
ms.assetid: b80fae94-35cc-4709-8346-d5a500d3fd49
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_SMS_DELETE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_SMS\_DELETE


OID\_WWAN\_SMS\_DELETE deletes SMS text messages stored in the MB device, or Subscriber Identity Module (SIM card), or any other auxiliary non-volatile memory or memories.

Query requests are not supported.

Set requests use the [**NDIS\_WWAN\_SMS\_DELETE**](https://msdn.microsoft.com/library/windows/hardware/ff567938) structure.

Miniport drivers process this OID asynchronously, and should return an NDIS\_STATUS\_INDICATION\_REQUIRED provisional response to any set requests. Miniport drivers should send an [**NDIS\_STATUS\_WWAN\_SMS\_DELETE**](ndis-status-wwan-sms-delete.md) indication when they have completed the transaction.

Remarks
-------

For more information about using this OID, see [WWAN SMS Operations](https://msdn.microsoft.com/library/windows/hardware/ff559131).

When processing this OID, miniport drivers can access the Subscriber Identity Module (SIM card), but should not access the provider's network.

Miniport drivers may receive requests to delete SMS text messages based on an index, or to delete all SMS text messages. Delete requests may consist of any one of the basic filters such as new (unread) messages, old (read) messages, draft messages, or sent messages.

Miniport drivers should return NDIS\_STATUS\_NOT\_SUPPORTED if they do not support SMS text messages, or the ability to delete SMS text messages.

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


[**NDIS\_WWAN\_SMS\_DELETE**](https://msdn.microsoft.com/library/windows/hardware/ff567938)

[WWAN SMS Operations](https://msdn.microsoft.com/library/windows/hardware/ff559131)

 

 




