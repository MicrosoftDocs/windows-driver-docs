---
title: NDIS_STATUS_WWAN_SMS_DELETE
description: Miniport drivers use the NDIS_STATUS_WWAN_SMS_DELETE notification to inform the MB Service about the completion of a previous delete request through OID_WWAN_SMS_DELETE.
ms.assetid: 0083dcd9-4e18-4582-993a-c4402cb552de
ms.date: 08/08/2017
keywords: 
 -NDIS_STATUS_WWAN_SMS_DELETE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_SMS\_DELETE


Miniport drivers use the NDIS\_STATUS\_WWAN\_SMS\_DELETE notification to inform the MB Service about the completion of a previous delete request through [OID\_WWAN\_SMS\_DELETE](oid-wwan-sms-delete.md).

Miniport drivers cannot use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_SMS\_DELETE\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff567940) structure.

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


[OID\_WWAN\_SMS\_DELETE](oid-wwan-sms-delete.md)

[**NDIS\_WWAN\_SMS\_DELETE\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff567940)

 

 




