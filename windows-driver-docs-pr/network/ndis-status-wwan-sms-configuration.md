---
title: NDIS_STATUS_WWAN_SMS_CONFIGURATION
description: Miniport drivers use the NDIS_STATUS_WWAN_SMS_CONFIGURATION notification to inform the MB Service about either the completion of a previous OID_WWAN_SMS_CONFIGURATION \ 160;query or set request, or an event notification in the case of change in SMS configuration. Miniport drivers can also send unsolicited events with this notification.This notification uses the NDIS_WWAN_SMS_CONFIGURATION structure.
ms.assetid: 86dfe2dc-070b-43d9-b6fa-54dee985c65d
ms.date: 08/08/2017
keywords: 
 -NDIS_STATUS_WWAN_SMS_CONFIGURATION Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_SMS\_CONFIGURATION


Miniport drivers use the NDIS\_STATUS\_WWAN\_SMS\_CONFIGURATION notification to inform the MB Service about either the completion of a previous [OID\_WWAN\_SMS\_CONFIGURATION](oid-wwan-sms-configuration.md) query or set request, or an event notification in the case of change in SMS configuration.

Miniport drivers can also send unsolicited events with this notification.

This notification uses the [**NDIS\_WWAN\_SMS\_CONFIGURATION**](https://msdn.microsoft.com/library/windows/hardware/ff567935) structure.

Remarks
-------

The miniport driver must send this unsolicited indication when the MB device's SMS subsystem is ready for SMS operation.

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


[OID\_WWAN\_SMS\_CONFIGURATION](oid-wwan-sms-configuration.md)

[**NDIS\_WWAN\_SMS\_CONFIGURATION**](https://msdn.microsoft.com/library/windows/hardware/ff567935)

 

 




