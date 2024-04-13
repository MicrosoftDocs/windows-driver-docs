---
title: NDIS_STATUS_WWAN_SMS_CONFIGURATION
ms.topic: reference
description: Miniport drivers use the NDIS_STATUS_WWAN_SMS_CONFIGURATION notification to inform the MB Service about either the completion of a previous OID_WWAN_SMS_CONFIGURATION \ 160;query or set request, or an event notification in the case of change in SMS configuration. Miniport drivers can also send unsolicited events with this notification.This notification uses the NDIS_WWAN_SMS_CONFIGURATION structure.
ms.date: 03/02/2023
keywords: 
 -NDIS_STATUS_WWAN_SMS_CONFIGURATION Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_SMS\_CONFIGURATION


Miniport drivers use the NDIS\_STATUS\_WWAN\_SMS\_CONFIGURATION notification to inform the MB Service about either the completion of a previous [OID\_WWAN\_SMS\_CONFIGURATION](oid-wwan-sms-configuration.md) query or set request, or an event notification in the case of change in SMS configuration.

Miniport drivers can also send unsolicited events with this notification.

This notification uses the [**NDIS\_WWAN\_SMS\_CONFIGURATION**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_sms_configuration) structure.

## Remarks

The miniport driver must send this unsolicited indication when the MB device's SMS subsystem is ready for SMS operation.

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


[OID\_WWAN\_SMS\_CONFIGURATION](oid-wwan-sms-configuration.md)

[**NDIS\_WWAN\_SMS\_CONFIGURATION**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_sms_configuration)

 

