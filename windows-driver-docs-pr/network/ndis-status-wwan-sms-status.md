---
title: NDIS_STATUS_WWAN_SMS_STATUS
description: Miniport drivers use the NDIS_STATUS_WWAN_SMS_STATUS notification to inform the MB Service about the following events The MB device's message store is full.A new SMS text message has arrived, with the new message corresponding to MessageIndex.Miniport drivers can also send unsolicited events with this notification.This notification uses the NDIS_WWAN_SMS_STATUS structure.
ms.assetid: 65553a3f-57af-49ef-a3b7-ed35df0a319d
ms.date: 08/08/2017
keywords: 
 -NDIS_STATUS_WWAN_SMS_STATUS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_SMS\_STATUS


Miniport drivers use the NDIS\_STATUS\_WWAN\_SMS\_STATUS notification to inform the MB Service about the following events:

-   The MB device's message store is full.

-   A new SMS text message has arrived, with the new message corresponding to *MessageIndex*.

Miniport drivers can also send unsolicited events with this notification.

This notification uses the [**NDIS\_WWAN\_SMS\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff567945) structure.

Remarks
-------

Miniport drivers must use NDIS\_STATUS\_WWAN\_SMS\_STATUS to inform the MB Service about the arrival of all non-class-0 (flash/alert) messages. To inform the MB Service about class-0 (flash/alert) message arrival, miniport drivers must use [**NDIS\_STATUS\_WWAN\_SMS\_RECEIVE**](ndis-status-wwan-sms-receive.md).

This indication could be a transactional notification for a *query* request of OID\_WWAN\_SMS\_STATUS or an unsolicited event.

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
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_SMS\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff567945)

[**NDIS\_STATUS\_WWAN\_SMS\_RECEIVE**](ndis-status-wwan-sms-receive.md)

 

 




