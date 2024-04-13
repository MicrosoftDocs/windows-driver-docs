---
title: NDIS_STATUS_WWAN_SMS_SEND
ms.topic: reference
description: Miniport drivers use the NDIS_STATUS_WWAN_SMS_SEND notification to inform the MB Service about the completion of a previous send request through OID_WWAN_SMS_SEND.
ms.date: 03/02/2023
keywords: 
 -NDIS_STATUS_WWAN_SMS_SEND Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_SMS\_SEND


Miniport drivers use the NDIS\_STATUS\_WWAN\_SMS\_SEND notification to inform the MB Service about the completion of a previous send request through [OID\_WWAN\_SMS\_SEND](oid-wwan-sms-send.md).

Miniport drivers cannot use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_SMS\_SEND\_STATUS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_sms_send_status) structure.

## Remarks

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
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[OID\_WWAN\_SMS\_SEND](oid-wwan-sms-send.md)

[**NDIS\_WWAN\_SMS\_SEND\_STATUS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_sms_send_status)

 

