---
title: NDIS_STATUS_WWAN_SMS_SEND
description: Miniport drivers use the NDIS_STATUS_WWAN_SMS_SEND notification to inform the MB Service about the completion of a previous send request through OID_WWAN_SMS_SEND.
ms.assetid: f750b09c-1a7c-40d8-8a4e-a7f9f3160248
ms.date: 08/08/2017
keywords: 
 -NDIS_STATUS_WWAN_SMS_SEND Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_SMS\_SEND


Miniport drivers use the NDIS\_STATUS\_WWAN\_SMS\_SEND notification to inform the MB Service about the completion of a previous send request through [OID\_WWAN\_SMS\_SEND](oid-wwan-sms-send.md).

Miniport drivers cannot use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_SMS\_SEND\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff567944) structure.

Remarks
-------

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


[OID\_WWAN\_SMS\_SEND](oid-wwan-sms-send.md)

[**NDIS\_WWAN\_SMS\_SEND\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff567944)

 

 




